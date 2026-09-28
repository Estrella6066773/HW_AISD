package io.camunda.demo.hospital.domain;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

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

	public AuditEventWriter(AuditEventRepository auditEventRepository) {
		this.auditEventRepository = auditEventRepository;
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
