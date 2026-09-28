package io.camunda.demo.hospital;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
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
 * Ruby 一责 JobWorker：退款 + 支付待调查。
 *
 * <p>图上挂点：{@code request-refund} 在 FinanceAdjustment 之后；
 * {@code mark-payment-investigate} 在进入 FundingIssue 之前。
 * 读写 {@link PaymentLedger}，并写 {@code audit_event}。既有 {@code request-payment} 不在本类。
 */
@Component
public class MemberAPathwayWorkers {

	private static final Logger LOG = LoggerFactory.getLogger(MemberAPathwayWorkers.class);

	/** 支付/退款流水表 */
	private final PaymentLedgerRepository paymentLedgerRepository;
	/** 审计只追加写入 */
	private final AuditEventWriter auditEventWriter;

	public MemberAPathwayWorkers(
			PaymentLedgerRepository paymentLedgerRepository, AuditEventWriter auditEventWriter) {
		this.paymentLedgerRepository = paymentLedgerRepository;
		this.auditEventWriter = auditEventWriter;
	}

	/**
	 * 线 13：财务表填完后自动跑。
	 * financeAdjustment=resolved → 流水 SUCCESSFUL；否则 INVESTIGATE。
	 */
	@JobWorker(type = "request-refund")
	public Map<String, Object> requestRefund(final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = caseRef(vars);
		if (caseReference.isBlank()) {
			throw new IllegalArgumentException("case_reference / patientId required for request-refund");
		}
		// 金额：表单未填则用演示默认值
		String amount = text(vars.get("charge_amount"));
		if (amount.isBlank()) {
			amount = "10.01";
		}
		// 来自 finance_adjustment 表单的 outcome
		String decision = text(vars.get("financeAdjustment"));
		if (decision.isBlank()) {
			decision = "pending";
		}
		PaymentLedgerStatus status =
				"resolved".equalsIgnoreCase(decision)
						? PaymentLedgerStatus.SUCCESSFUL
						: PaymentLedgerStatus.INVESTIGATE;
		// 幂等键：同一病例+决定+金额重试时复用原行，不插第二笔
		String idempotencyKey = caseReference + "|refund|" + decision + "|" + amount;
		PaymentLedger row =
				upsertLedger(
						caseReference,
						idempotencyKey,
						amount,
						status,
						"RF-" + shortId(),
						status == PaymentLedgerStatus.SUCCESSFUL ? LocalDate.now() : null);
		auditEventWriter.append(
				"ruby",
				"request-refund",
				caseReference,
				idempotencyKey,
				"Refund / adjustment mock; decision=" + decision + "; status=" + status);
		LOG.info(
				"request-refund case={} decision={} status={} tx={} key={}",
				caseReference,
				decision,
				status,
				row.getTransactionReference(),
				idempotencyKey);
		// 写回流程变量，供后续网关/演示查看
		Map<String, Object> out = new HashMap<>();
		out.put("case_reference", caseReference);
		out.put("refund_status", status.name());
		out.put("refund_transaction_reference", row.getTransactionReference());
		out.put("refund_recorded", status == PaymentLedgerStatus.SUCCESSFUL);
		return out;
	}

	/**
	 * 线 10 失败支：支付失败后、FundingIssue 人工之前。
	 * 先标 INVESTIGATE，避免自动再扣款。
	 */
	@JobWorker(type = "mark-payment-investigate")
	public Map<String, Object> markPaymentInvestigate(final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = caseRef(vars);
		if (caseReference.isBlank()) {
			throw new IllegalArgumentException(
					"case_reference / patientId required for mark-payment-investigate");
		}
		String amount = text(vars.get("charge_amount"));
		if (amount.isBlank()) {
			amount = "10.01";
		}
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

	private static String text(Object value) {
		return value == null ? "" : String.valueOf(value).trim();
	}

	private static String shortId() {
		return UUID.randomUUID().toString().substring(0, 8).toUpperCase();
	}
}
