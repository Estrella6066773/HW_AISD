package io.camunda.demo.hospital;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.demo.hospital.domain.AuditEvent;
import io.camunda.demo.hospital.domain.AuditEventWriter;
import java.util.Map;
import java.util.Set;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/** 护理变更通知。订阅 {@code notify-care-change}，把回执写入审计。 */
@Component
public class CareChangeWorkers {
    private static final Logger LOG = LoggerFactory.getLogger(CareChangeWorkers.class);
    private final AuditEventWriter audit;

    public CareChangeWorkers(AuditEventWriter audit) {
        this.audit = audit;
    }

    @JobWorker(type = "notify-care-change")
    public Map<String, Object> notifyCareChange(ActivatedJob job) {
        Map<String, Object> variables = job.getVariablesAsMap();
        String patientId = (String) variables.get("patientId");
        String clinicianId = (String) variables.get("clinicianId");
        String target = (String) variables.get("changeTarget");
        if (patientId == null || patientId.isBlank() || clinicianId == null || clinicianId.isBlank()
                || target == null || !Set.of("treatment", "visit", "discharge", "invalid").contains(target)
                || !(variables.get("moneyAffected") instanceof Boolean)) {
            throw new IllegalArgumentException("Patient, clinician, change target and financial impact are required");
        }

        boolean sent = !target.equals("invalid");
        String status = "SENT";
        if (!sent) {
            status = "SKIPPED_UNAUTHORISED";
        } else if (Boolean.TRUE.equals(variables.get("moneyAffected"))) {
            status = "SENT_FINANCE_REVIEW_REQUIRED";
        }

        String key = "member-D|notify-care-change|" + job.getProcessInstanceKey() + "|" + job.getElementInstanceKey();
        String action = sent ? "notify-care-change" : "notify-care-change-skipped";
        AuditEvent receipt = audit.append(clinicianId, action, patientId, key,
                "Mock notification to pathway team; target=" + target + "; status=" + status);
        LOG.info("Care change: patient={}, status={}, receipt={}", patientId, status, receipt.getId());

        return Map.of("careChangeNotificationSent", sent,
                "careChangeNotificationStatus", status,
                "careChangeNotificationReference", "AUD-" + receipt.getId());
    }
}
