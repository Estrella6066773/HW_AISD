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

/** D / Ryan：课堂演示，记录治疗变更的模拟通知。 */
@Component
public class MemberDPathwayWorkers {
    private static final Logger LOG = LoggerFactory.getLogger(MemberDPathwayWorkers.class);
    private final AuditEventWriter audit;

    public MemberDPathwayWorkers(AuditEventWriter audit) {
        this.audit = audit;
    }

    @JobWorker(type = "notify-care-change")
    public Map<String, Object> notifyCareChange(ActivatedJob job) {
        // 1. 读取表单经 BPMN 映射后的变量。
        Map<String, Object> variables = job.getVariablesAsMap();
        String patientId = (String) variables.get("patientId");
        String clinicianId = (String) variables.get("clinicianId");
        String target = (String) variables.get("changeTarget");
        if (patientId == null || patientId.isBlank() || clinicianId == null || clinicianId.isBlank()
                || target == null || !Set.of("treatment", "visit", "discharge", "invalid").contains(target)
                || !(variables.get("moneyAffected") instanceof Boolean)) {
            throw new IllegalArgumentException("Patient, clinician, change target and financial impact are required");
        }

        // 2. 缺少正式授权就跳过；涉钱变更仍交给 Finance 人工审核。
        boolean sent = !target.equals("invalid");
        String status = "SENT";
        if (!sent) {
            status = "SKIPPED_UNAUTHORISED";
        } else if (Boolean.TRUE.equals(variables.get("moneyAffected"))) {
            status = "SENT_FINANCE_REVIEW_REQUIRED";
        }

        // 3. 保存模拟通知。同一个节点重试时使用相同的键，复用原记录。
        String key = "member-D|notify-care-change|" + job.getProcessInstanceKey() + "|" + job.getElementInstanceKey();
        String action = sent ? "notify-care-change" : "notify-care-change-skipped";
        AuditEvent receipt = audit.append(clinicianId, action, patientId, key,
                "Mock notification to pathway team; target=" + target + "; status=" + status);
        LOG.info("Care change: patient={}, status={}, receipt={}", patientId, status, receipt.getId());

        // 4. 返回结果，Camunda 自动完成此服务任务，再继续走原来的网关。
        return Map.of("careChangeNotificationSent", sent,
                "careChangeNotificationStatus", status,
                "careChangeNotificationReference", "AUD-" + receipt.getId());
    }
}
