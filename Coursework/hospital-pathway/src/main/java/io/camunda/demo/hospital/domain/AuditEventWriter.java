package io.camunda.demo.hospital.domain;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.TransactionDefinition;
import org.springframework.transaction.support.TransactionTemplate;
import org.springframework.dao.DataIntegrityViolationException;
import java.util.Objects;
import java.util.function.Supplier;

/**
 * 审计事件只追加写入。
 *
 * <p>联动：后续转诊决策、治疗授权、支付、退款等节点在完成业务后调用 {@link #append}；
 * 查询用 {@link AuditEventRepository}。不提供 update/delete 业务方法（PB-11）。
 *
 * <p>注意：{@code payloadSummary} 截断到 512 字符；禁止传入卡号或病历正文。
 */
@Service
public class AuditEventWriter {

	private final AuditEventRepository auditEventRepository;
	private final TransactionTemplate receiptTransaction;

	public AuditEventWriter(AuditEventRepository auditEventRepository, PlatformTransactionManager transactions) {
		this.auditEventRepository = auditEventRepository;
		this.receiptTransaction = new TransactionTemplate(transactions);
		this.receiptTransaction.setPropagationBehavior(TransactionDefinition.PROPAGATION_REQUIRES_NEW);
	}

	/**
	 * Add one immutable mock receipt per task occurrence, committed before job completion.
	 * The supplier computes local mock metadata only; it must not send real email or charge money.
	 * A competing insert is rolled back before looking up the winning committed receipt.
	 */
	public AuditEvent append(String actor, String action, String caseReference,
			String idempotencyKey, Supplier<String> mockSummary) {
		String key = requireText(idempotencyKey, "idempotencyKey");
		if (key.length() > 256) throw new IllegalArgumentException("idempotencyKey too long");
		String safeActor = requireText(actor, "actor");
		String safeAction = requireText(action, "action");
		String safeCase = requireText(caseReference, "caseReference");
		try {
			return receiptTransaction.execute(status -> auditEventRepository.findByIdempotencyKey(key)
					.map(event -> matching(event, safeActor, safeAction, safeCase))
					.orElseGet(() -> {
						AuditEvent event = new AuditEvent();
						event.setActor(safeActor);
						event.setAction(safeAction);
						event.setCaseReference(safeCase);
						event.setIdempotencyKey(key);
						event.setPayloadSummary(trimToMax(mockSummary.get(), 512));
						return auditEventRepository.saveAndFlush(event);
					}));
		} catch (DataIntegrityViolationException duplicateOrInvalidData) {
			return auditEventRepository.findByIdempotencyKey(key)
					.map(event -> matching(event, safeActor, safeAction, safeCase))
					.orElseThrow(() -> duplicateOrInvalidData);
		}
	}

	private static AuditEvent matching(AuditEvent event, String actor, String action, String caseReference) {
		if (!Objects.equals(event.getActor(), actor) || !Objects.equals(event.getAction(), action)
				|| !Objects.equals(event.getCaseReference(), caseReference)) {
			throw new IllegalArgumentException("Receipt key reused for a different case, actor or action");
		}
		return event;
	}

	@Transactional
	public AuditEvent append(String actor, String action, String caseReference, String payloadSummary) {
		AuditEvent event = new AuditEvent();
		event.setActor(requireText(actor, "actor"));
		event.setAction(requireText(action, "action"));
		event.setCaseReference(blankToNull(caseReference));
		event.setPayloadSummary(trimToMax(payloadSummary, 512));
		return auditEventRepository.save(event);
	}

	private static String requireText(String value, String field) {
		if (value == null || value.isBlank()) {
			throw new IllegalArgumentException(field + " required");
		}
		return value.trim();
	}

	private static String blankToNull(String value) {
		if (value == null || value.isBlank()) {
			return null;
		}
		return value.trim();
	}

	private static String trimToMax(String value, int max) {
		if (value == null) {
			return null;
		}
		String trimmed = value.trim();
		if (trimmed.length() <= max) {
			return trimmed;
		}
		return trimmed.substring(0, max);
	}
}
