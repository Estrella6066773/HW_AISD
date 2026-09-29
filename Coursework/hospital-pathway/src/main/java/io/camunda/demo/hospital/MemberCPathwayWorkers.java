package io.camunda.demo.hospital;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.demo.hospital.domain.AuditEventWriter;
import java.util.HashMap;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/**
 * 成员 C（Ender）的 JobWorker：诊后信外发与转诊方通知。
 *
 * <p>联动：订阅全院 BPMN 上 {@code dispatch-clinic-letter} 与 {@code notify-referrer}；
 * 仅向 {@link AuditEventWriter} 追加审计事件，不新建领域表、不修改他人工作器。
 *
 * <p>重试语义：以 {@code caseReference|workerType} 作为幂等键，重复触发时复用同一条审计记录，
 * 因此重试不会在审计库里堆积重复行（与 D 的回执复用一致）。
 *
 * <p>注意：课堂 mock；不真正发送信件或邮件，仅记录外发结果，且绝不写入卡号或病历正文。
 */
@Component
public class MemberCPathwayWorkers {

	private static final Logger LOG = LoggerFactory.getLogger(MemberCPathwayWorkers.class);

	private final AuditEventWriter auditEventWriter;

	public MemberCPathwayWorkers(AuditEventWriter auditEventWriter) {
		this.auditEventWriter = auditEventWriter;
	}

	@JobWorker(type = "dispatch-clinic-letter")
	public Map<String, Object> dispatchClinicLetter(final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = caseRef(vars);
		String letterStatus = text(vars.get("letterStatus"));
		String notes = text(vars.get("DispatchLetterNotes"));
		String staffRole = text(vars.get("staffRole"));

		String idempotencyKey = caseReference + "|dispatch-clinic-letter";
		String reference = "C-DISPATCH-" + caseReference;
		String summary =
				"letterStatus=" + (letterStatus.isBlank() ? "unknown" : letterStatus)
						+ "; staffRole=" + (staffRole.isBlank() ? "unknown" : staffRole)
						+ "; notes=" + (notes.length() > 120 ? notes.substring(0, 120) : notes);

		auditEventWriter.append("member-C", "dispatch-clinic-letter", caseReference, idempotencyKey, summary);
		LOG.info("dispatch-clinic-letter case={} status={} ref={}", caseReference, letterStatus, reference);

		Map<String, Object> out = new HashMap<>();
		out.put("clinicLetterDispatchStatus", "dispatched");
		out.put("clinicLetterDispatchReference", reference);
		return out;
	}

	@JobWorker(type = "notify-referrer")
	public Map<String, Object> notifyReferrer(final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = caseRef(vars);
		String notes = text(vars.get("RedirectNotes"));
		String staffRole = text(vars.get("staffRole"));

		String idempotencyKey = caseReference + "|notify-referrer";
		String reference = "C-REFERRER-" + caseReference;
		String summary =
				"staffRole=" + (staffRole.isBlank() ? "unknown" : staffRole)
						+ "; notes=" + (notes.length() > 120 ? notes.substring(0, 120) : notes);

		auditEventWriter.append("member-C", "notify-referrer", caseReference, idempotencyKey, summary);
		LOG.info("notify-referrer case={} ref={}", caseReference, reference);

		Map<String, Object> out = new HashMap<>();
		out.put("referrerNotificationSent", true);
		out.put("referrerNotificationStatus", "sent");
		out.put("referrerNotificationReference", reference);
		return out;
	}

	private static String caseRef(Map<String, Object> vars) {
		String caseReference = text(vars.get("case_reference"));
		if (caseReference.isBlank()) {
			caseReference = text(vars.get("patientId"));
		}
		return caseReference.isBlank() ? "UNKNOWN" : caseReference;
	}

	private static String text(Object value) {
		return value == null ? "" : String.valueOf(value).trim();
	}
}
