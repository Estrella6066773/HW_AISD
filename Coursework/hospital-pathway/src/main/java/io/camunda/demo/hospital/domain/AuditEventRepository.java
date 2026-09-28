package io.camunda.demo.hospital.domain;

import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * 审计事件只读查询面。写入请走 {@link AuditEventWriter}，避免业务侧误用 {@code save} 覆盖历史行。
 */
public interface AuditEventRepository extends JpaRepository<AuditEvent, Long> {

	List<AuditEvent> findByCaseReferenceOrderByOccurredAtAsc(String caseReference);

	List<AuditEvent> findAllByOrderByOccurredAtAsc();
}
