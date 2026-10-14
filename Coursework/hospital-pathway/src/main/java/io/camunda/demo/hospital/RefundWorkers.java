package io.camunda.demo.hospital;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.client.api.worker.JobClient;
import io.camunda.demo.hospital.domain.AuditEventWriter;
import io.camunda.demo.hospital.domain.PaymentLedger;
import io.camunda.demo.hospital.domain.PaymentLedgerRepository;
import io.camunda.demo.hospital.domain.PaymentLedgerStatus;
import java.time.Instant;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.UUID;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/**
 * 退款工作器。线 13 写退款；线 10 支付失败时把账本标成待调查。
 *
 * <p>图上挂点：{@code request-refund} 在 FinanceAdjustment 之后；
 * {@code mark-payment-investigate} 在进入 FundingIssue 之前。
 * 读写 {@link PaymentLedger}，并写 {@code audit_event}。既有 {@code request-payment} 不在本类。
 */
@Component
public class RefundWorkers {

	private static final Logger LOG = LoggerFactory.getLogger(RefundWorkers.class);

	/** 支付/退款流水表 */
	private final PaymentLedgerRepository paymentLedgerRepository;
	/** 审计只追加写入 */
	private final AuditEventWriter auditEventWriter;

	public RefundWorkers(
			PaymentLedgerRepository paymentLedgerRepository, AuditEventWriter auditEventWriter) {
		this.paymentLedgerRepository = paymentLedgerRepository;
		this.auditEventWriter = auditEventWriter;
	}

	/**
	 * V2 图上 {@code FinanceAdjustment} 完成后的作业入口。
	 * 表单只展示原收费，部分退款是否低于原收费由 {@link #requestRefund(ActivatedJob)} 判断。
	 * 判断失败时立刻把作业标成失败并且剩余重试次数为 0，不再按图上的 {@code retries="3"} 把同一句错误重复三次。
	 * 技术性异常仍交给 Camunda 按剩余次数重试。
	 */
	@JobWorker(type = "request-refund", autoComplete = false)
	public void completeRefundJob(final JobClient jobClient, final ActivatedJob job) {
		try {
			Map<String, Object> out = requestRefund(job);
			jobClient.newCompleteCommand(job).variables(out).send().join();
		} catch (IllegalArgumentException rejected) {
			jobClient.newFailCommand(job).retries(0).errorMessage(rejected.getMessage()).send().join();
		}
	}

	/**
	 * 线 13：财务表填完后，由 V2 图上的 {@code AdjustmentOutcome} 读取 {@code financeAdjustment}。
	 * 全额/部分退款、转款、保留费用各自写不同账本状态；{@code pending} 留在调查，不补 10.01。
	 * 测试直接调用本方法。金额或决定不合法时抛出 {@link IllegalArgumentException}，由 {@link #completeRefundJob} 转成一次失败。
	 */
	public Map<String, Object> requestRefund(final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = caseRef(vars);
		if (caseReference.isBlank()) {
			throw new IllegalArgumentException("case_reference / patientId required for request-refund");
		}
		String decision = text(vars.get("financeAdjustment"));
		if (decision.isBlank()) {
			decision = "pending";
		}
		// 未知取值直接失败，避免再掉进同一个“已解决”分支。
		AdjustmentOutcome outcome = resolveAdjustment(decision, vars);
		String idempotencyKey = caseReference + "|refund|" + decision + "|" + outcome.amount();
		PaymentLedger row =
				upsertLedger(
						caseReference,
						idempotencyKey,
						outcome.amount(),
						outcome.status(),
						outcome.referencePrefix() + shortId(),
						outcome.dated() ? LocalDate.now() : null);
		auditEventWriter.append(
				"ruby",
				"request-refund",
				caseReference,
				idempotencyKey,
				"Refund / adjustment mock; decision="
						+ decision
						+ "; status="
						+ outcome.status());
		LOG.info(
				"request-refund case={} decision={} status={} tx={} key={}",
				caseReference,
				decision,
				outcome.status(),
				row.getTransactionReference(),
				idempotencyKey);
		// 写回流程变量。网关看 financeAdjustment，不看 refund_recorded。
		Map<String, Object> out = new HashMap<>();
		out.put("case_reference", caseReference);
		out.put("financeAdjustment", decision);
		out.put("refund_status", outcome.status().name());
		out.put("refund_transaction_reference", row.getTransactionReference());
		out.put("refund_recorded", outcome.status() == PaymentLedgerStatus.SUCCESSFUL);
		return out;
	}

	/**
	 * 财务决定和账本的对应关系。{@code resolved} 只保留给已经在跑的旧实例，和新表单的全额退款同等处理。
	 * 部分退款必须低于原收费；转款和保留费用不记成退款成功。
	 */
	private static AdjustmentOutcome resolveAdjustment(String decision, Map<String, Object> vars) {
		return switch (decision) {
			case "refund_full", "resolved" ->
					new AdjustmentOutcome(
							requireAdjustmentAmount(vars), PaymentLedgerStatus.SUCCESSFUL, "RF-", true);
			case "refund_partial" ->
					new AdjustmentOutcome(
							requirePartialAmount(vars), PaymentLedgerStatus.SUCCESSFUL, "RF-", true);
			case "transfer" ->
					new AdjustmentOutcome(
							requireAdjustmentAmount(vars), PaymentLedgerStatus.TRANSFERRED, "TR-", true);
			case "retain" ->
					new AdjustmentOutcome(
							requireAdjustmentAmount(vars), PaymentLedgerStatus.RETAINED, "RT-", true);
			case "pending" ->
					new AdjustmentOutcome(
							statedOrUnspecified(firstAmount(vars)), PaymentLedgerStatus.INVESTIGATE, "RF-", false);
			default ->
					throw new IllegalArgumentException(
							"financeAdjustment not recognised: " + decision);
		};
	}

	/** 全额退款、转款、保留费用都要有两位小数金额。优先用本次填写的调整金额。 */
	private static String requireAdjustmentAmount(Map<String, Object> vars) {
		return ChargeAmountRules.require(firstAmount(vars));
	}

	/**
	 * 部分退款使用 adjustmentAmount。原 charge_amount 存在时，部分金额必须更小，避免把全额退款标成部分退款。
	 */
	private static String requirePartialAmount(Map<String, Object> vars) {
		String partial = ChargeAmountRules.require(vars.get("adjustmentAmount"));
		String originalText = text(vars.get("charge_amount"));
		if (!originalText.isEmpty()) {
			String original = ChargeAmountRules.require(originalText);
			if (new java.math.BigDecimal(partial).compareTo(new java.math.BigDecimal(original)) >= 0) {
				throw new IllegalArgumentException(
						"adjustmentAmount must be lower than charge_amount for a partial refund");
			}
		}
		return partial;
	}

	private static Object firstAmount(Map<String, Object> vars) {
		String adjustment = text(vars.get("adjustmentAmount"));
		if (!adjustment.isEmpty()) {
			return vars.get("adjustmentAmount");
		}
		return vars.get("charge_amount");
	}

	private record AdjustmentOutcome(
			String amount, PaymentLedgerStatus status, String referencePrefix, boolean dated) {}

	/**
	 * 线 10 失败支：支付失败后、FundingIssue 人工之前。
	 * 先标 INVESTIGATE，避免自动再扣款。
	 */
	// 线 10 失败支。只把账本标成 INVESTIGATE，不发布消息。
	@JobWorker(type = "mark-payment-investigate")
	public Map<String, Object> markPaymentInvestigate(final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = caseRef(vars);
		if (caseReference.isBlank()) {
			throw new IllegalArgumentException(
					"case_reference / patientId required for mark-payment-investigate");
		}
		// 待调查路径可能还没有收费金额（资助待定）。有金额就校验；没有就记账为未提供，不补 10.01。
		String amount = statedOrUnspecified(vars.get("charge_amount"));
		String priorTx = text(vars.get("transaction_reference"));
		String idempotencyKey =
				caseReference + "|investigate|" + (priorTx.isBlank() ? amount : priorTx);
		PaymentLedger row =
				upsertLedger(
						caseReference,
						idempotencyKey,
						amount,
						PaymentLedgerStatus.INVESTIGATE,
						priorTx.isBlank() ? "INV-" + shortId() : priorTx,
						null);
		auditEventWriter.append(
				"ruby",
				"mark-payment-investigate",
				caseReference,
				idempotencyKey,
				"Payment investigate mock; priorTx=" + (priorTx.isBlank() ? "none" : priorTx));
		LOG.info(
				"mark-payment-investigate case={} status=INVESTIGATE tx={} key={}",
				caseReference,
				row.getTransactionReference(),
				idempotencyKey);
		Map<String, Object> out = new HashMap<>();
		out.put("case_reference", caseReference);
		out.put("payment_status", "investigate");
		out.put("payment_investigate", true);
		out.put("investigate_transaction_reference", row.getTransactionReference());
		return out;
	}

	/** 先按幂等键查询；已有则复用，没有则新建并保存。 */
	private PaymentLedger upsertLedger(
			String caseReference,
			String idempotencyKey,
			String amount,
			PaymentLedgerStatus status,
			String transactionReference,
			LocalDate paymentDate) {
		Optional<PaymentLedger> existing = paymentLedgerRepository.findByIdempotencyKey(idempotencyKey);
		if (existing.isPresent()) {
			PaymentLedger row = existing.get();
			LOG.info(
					"payment_ledger reuse key={} status={} tx={}",
					idempotencyKey,
					row.getStatus(),
					row.getTransactionReference());
			return row;
		}
		PaymentLedger row = new PaymentLedger();
		row.setCaseReference(caseReference);
		row.setIdempotencyKey(idempotencyKey);
		row.setAmount(amount);
		row.setStatus(status);
		row.setTransactionReference(transactionReference);
		row.setPaymentDate(paymentDate);
		row.setCreatedAt(Instant.now());
		return paymentLedgerRepository.save(row);
	}

	/** 优先 case_reference，否则用表单里的 patientId。 */
	private static String caseRef(Map<String, Object> vars) {
		String caseReference = text(vars.get("case_reference"));
		if (caseReference.isBlank()) {
			caseReference = text(vars.get("patientId"));
		}
		return caseReference;
	}

	/**
	 * 支付失败后的调查必须沿用真实金额。资助待定、表单上没有金额时，记 {@code unspecified}，避免账本出现假的 10.01。
	 */
	private static String statedOrUnspecified(Object raw) {
		String text = raw == null ? "" : String.valueOf(raw).trim();
		if (text.isEmpty()) {
			return "unspecified";
		}
		return ChargeAmountRules.require(raw);
	}

	private static String text(Object value) {
		return value == null ? "" : String.valueOf(value).trim();
	}

	private static String shortId() {
		return UUID.randomUUID().toString().substring(0, 8).toUpperCase();
	}
}
