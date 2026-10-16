package io.camunda.demo.hospital.domain;

import java.util.List;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * 预约占用仓储。联动：后续排班 / 资源不可用工作器按占用键防重复。
 */
public interface BookingSlotRepository extends JpaRepository<BookingSlot, Long> {

	Optional<BookingSlot> findByOccupancyKey(String occupancyKey);

	List<BookingSlot> findByCaseReferenceOrderByCreatedAtAsc(String caseReference);
}
