package io.camunda.demo.hospital;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.demo.hospital.domain.AuditEvent;
import io.camunda.demo.hospital.domain.AuditEventWriter;
import io.camunda.demo.hospital.domain.PaymentLedgerRepository;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/**
 * D / Ryan: mock care-change notifications and enquiry acknowledgements.
 * Human approval stays in Forms. Each mock receipt is committed to the shared H2
 * audit table before this method returns and Camunda automatically completes the job.
 * No real correspondence is sent; payment_ledger is read-only here.
 */
@Component
public class MemberDPathwayWorkers {
    private static final Logger LOG = LoggerFactory.getLogger(MemberDPathwayWorkers.class);
    private static final Map<String, String> CHANGE_TARGETS = Map.of(
            "reschedule_unpaid", "treatment", "reschedule_paid", "treatment",
            "follow_up_unpaid", "visit", "follow_up_paid", "visit",
            "discharge_unpaid", "discharge", "discharge_paid", "discharge");
    private static final Map<String, String> ENQUIRY_NOTES = Map.of(
            "enquiry_admin", "AdminEnquiryNotes",
            "enquiry_clinical", "ClinicalEnquiryNotes",
            "enquiry_finance", "FinanceEnquiryNotes");
    private final AuditEventWriter audit;
    private final PaymentLedgerRepository payments;
    private final Set<String> demoFailures = ConcurrentHashMap.newKeySet();

    public MemberDPathwayWorkers(AuditEventWriter audit, PaymentLedgerRepository payments) {
        this.audit = audit;
        this.payments = payments;
    }

    @JobWorker(type = "notify-care-change")
    public Map<String, Object> notifyCareChange(ActivatedJob job) {
        Map<String, Object> vars = job.getVariablesAsMap();
        String caseReference = caseReference(vars);
        String actor = required(vars.get("clinicianId"), "clinicianId", 128);
        String decision = required(vars.get("modificationDecision"), "modificationDecision", 64);
        String target = text(vars.get("changeTarget"));
        String key = receiptKey(job, "notify-care-change");

        if (decision.equals("invalid") && target.equals("invalid")) {
            AuditEvent event = audit.append(actor, "notify-care-change-skipped", caseReference, key,
                    () -> "mock=true; sent=false; reason=formal clinical authorisation missing");
            LOG.info("notify-care-change SKIPPED case={} receipt={} (no authorised change)", caseReference, event.getId());
            return changeResult(false, "SKIPPED_UNAUTHORISED", event);
        }

        boolean financial = decision.endsWith("_paid");
        if (!target.equals(CHANGE_TARGETS.get(decision))
                || !(vars.get("moneyAffected") instanceof Boolean affected) || affected != financial) {
            throw new IllegalArgumentException("member-D-input-invalid: decision, changeTarget and moneyAffected disagree");
        }
        AuditEvent event = audit.append(actor, "notify-care-change", caseReference, key, () -> {
            simulateAvailability(vars, key);
            int paymentRows = financial ? payments.findByCaseReferenceOrderByCreatedAtAsc(caseReference).size() : 0;
            return "mock=true; decision=" + decision + "; target=" + target
                    + "; recipient=pathway-team; financeReviewRequired=" + financial
                    + "; paymentRows=" + paymentRows;
        });
        demoFailures.remove(key);
        LOG.info("notify-care-change mock receipt available case={} receipt={} financeReviewRequired={}",
                caseReference, event.getId(), financial);
        return changeResult(true, financial ? "SENT_FINANCE_REVIEW_REQUIRED" : "SENT", event);
    }

    @JobWorker(type = "ack-enquiry-routed")
    public Map<String, Object> acknowledgeEnquiry(ActivatedJob job) {
        Map<String, Object> vars = job.getVariablesAsMap();
        String caseReference = caseReference(vars);
        String actor = required(vars.get("staffRole"), "staffRole", 128);
        String kind = text(vars.get("requestKind"));
        String noteField = ENQUIRY_NOTES.get(kind);
        if (noteField == null || text(vars.get(noteField)).isBlank()) {
            throw new IllegalArgumentException("member-D-input-invalid: enquiry type and its recorded response required");
        }
        String key = receiptKey(job, "ack-enquiry-routed");
        AuditEvent event = audit.append(actor, "ack-enquiry-routed", caseReference, key, () -> {
            simulateAvailability(vars, key);
            return "mock=true; enquiryType=" + kind + "; recipient=requester; responseRecorded=true; status=resolved";
        });
        demoFailures.remove(key);
        LOG.info("ack-enquiry-routed mock receipt available case={} kind={} receipt={}", caseReference, kind, event.getId());
        return Map.of("enquiryAcknowledgementSent", true,
                "enquiryAcknowledgementReference", "AUD-" + event.getId());
    }

    private static Map<String, Object> changeResult(boolean sent, String status, AuditEvent event) {
        return Map.of("careChangeNotificationSent", sent, "careChangeNotificationStatus", status,
                "careChangeNotificationReference", "AUD-" + event.getId());
    }

    private static String receiptKey(ActivatedJob job, String type) {
        if (job.getProcessInstanceKey() <= 0 || job.getElementInstanceKey() <= 0) {
            throw new IllegalArgumentException("member-D-input-invalid: process and element instance keys required");
        }
        return "member-D|" + type + "|" + job.getProcessInstanceKey() + "|" + job.getElementInstanceKey();
    }

    private static String caseReference(Map<String, Object> vars) {
        String reference = text(vars.get("case_reference"));
        String patient = text(vars.get("patientId"));
        if (!reference.isEmpty() && !patient.isEmpty() && !reference.equals(patient)) {
            throw new IllegalArgumentException("member-D-input-invalid: case_reference differs from patientId");
        }
        return required(reference.isEmpty() ? patient : reference, "patientId / case_reference", 128);
    }

    /** Local demo only: once fails one delivery; always can be cleared in Operate before retry. */
    private void simulateAvailability(Map<String, Object> vars, String key) {
        String mode = text(vars.get("memberDNotificationFailure"));
        if (mode.isEmpty() || mode.equals("none")) return;
        if (!mode.equals("once") && !mode.equals("always")) {
            throw new IllegalArgumentException("memberDNotificationFailure must be none, once or always");
        }
        if (mode.equals("always") || demoFailures.add(key)) {
            LOG.warn("Member D mock notification temporarily unavailable key={} mode={}", key, mode);
            throw new IllegalStateException("member-D-notification-unavailable: simulated delivery failure");
        }
    }

    private static String required(Object value, String field, int max) {
        String result = text(value);
        if (result.isEmpty() || result.length() > max) {
            throw new IllegalArgumentException("member-D-input-invalid: " + field + " required, max " + max);
        }
        return result;
    }

    private static String text(Object value) { return value == null ? "" : String.valueOf(value).trim(); }
}
