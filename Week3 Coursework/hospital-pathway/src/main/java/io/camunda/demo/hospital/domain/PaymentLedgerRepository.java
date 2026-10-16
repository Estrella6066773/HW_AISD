package io.camunda.demo.hospital.domain;

import java.util.List;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * 支付流水仓储。联动：后续支付工作器按幂等键查询；本切片不注入现有 JobWorker。
 */
public interface PaymentLedgerRepository extends JpaRepository<PaymentLedger, Long> {

	Optional<PaymentLedger> findByIdempotencyKey(String idempotencyKey);

	List<PaymentLedger> findByCaseReferenceOrderByCreatedAtAsc(String caseReference);
}
