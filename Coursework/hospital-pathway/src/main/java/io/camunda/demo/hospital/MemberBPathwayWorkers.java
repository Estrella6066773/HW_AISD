package io.camunda.demo.hospital;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.demo.hospital.domain.AuditEventWriter;
import io.camunda.demo.hospital.domain.BookingSlot;
import io.camunda.demo.hospital.domain.BookingSlotRepository;
import io.camunda.demo.hospital.domain.BookingSlotStatus;
import java.time.Instant;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/**
 * Member B workers: slot hold and resource-unavailable flagging.
 *
 * <p>Job types: {@code check-slot}, {@code reserve-appointment}, {@code flag-resource-unavailable}.
 * Writes {@link BookingSlot} and audit events.
 */
@Component
public class MemberBPathwayWorkers {

	private static final Logger LOG = LoggerFactory.getLogger(MemberBPathwayWorkers.class);

	private final BookingSlotRepository bookingSlotRepository;
	private final AuditEventWriter auditEventWriter;

	public MemberBPathwayWorkers(
			BookingSlotRepository bookingSlotRepository, AuditEventWriter auditEventWriter) {
		this.bookingSlotRepository = bookingSlotRepository;
		this.auditEventWriter = auditEventWriter;
	}

	@JobWorker(type = "check-slot")
	public Map<String, Object> checkSlot(final ActivatedJob job) {
		return upsertBooking(job, "check-slot", "visit", BookingSlotStatus.CONFIRMED);
	}

	@JobWorker(type = "reserve-appointment")
	public Map<String, Object> reserveAppointment(final ActivatedJob job) {
		return upsertBooking(job, "reserve-appointment", "treatment", BookingSlotStatus.CONFIRMED);
	}

	@JobWorker(type = "flag-resource-unavailable")
	public Map<String, Object> flagResourceUnavailable(final ActivatedJob job) {
		Map<String, Object> out =
				upsertBooking(job, "flag-resource-unavailable", "treatment", BookingSlotStatus.PENDING);
		out.put("treatmentSlotStatus", "pending");
		return out;
	}

	private Map<String, Object> upsertBooking(
			ActivatedJob job, String workerType, String resourceKind, BookingSlotStatus status) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = caseRef(vars);
		String window = text(vars.get("timeframe"));
		if (window.isBlank()) {
			window = resourceKind;
		}
		String occupancyKey = caseReference + "|" + resourceKind + "|" + window;
		Optional<BookingSlot> existing = bookingSlotRepository.findByOccupancyKey(occupancyKey);
		BookingSlot slot;
		if (existing.isPresent()) {
			slot = existing.get();
			if (status == BookingSlotStatus.PENDING) {
				slot.setRetryCount(slot.getRetryCount() + 1);
				slot.setLastRetryAt(Instant.now());
				slot.setStatus(BookingSlotStatus.PENDING);
			}
			bookingSlotRepository.save(slot);
			LOG.info(
					"{} reuse occupancy={} status={} retries={}",
					workerType,
					occupancyKey,
					slot.getStatus(),
					slot.getRetryCount());
		} else {
			slot = new BookingSlot();
			slot.setCaseReference(caseReference.isBlank() ? "UNKNOWN" : caseReference);
			slot.setOccupancyKey(occupancyKey);
			slot.setTimeWindow(window);
			slot.setStatus(status);
			slot.setCreatedAt(Instant.now());
			if (status == BookingSlotStatus.PENDING) {
				slot.setRetryCount(1);
				slot.setLastRetryAt(Instant.now());
			}
			bookingSlotRepository.save(slot);
			LOG.info("{} NEW occupancy={} status={}", workerType, occupancyKey, status);
		}
		auditEventWriter.append("member-B", workerType, caseReference, occupancyKey + " -> " + status);
		Map<String, Object> out = new HashMap<>();
		out.put("case_reference", caseReference);
		out.put("booking_occupancy_key", occupancyKey);
		out.put("booking_slot_status", slot.getStatus().name());
		return out;
	}

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
}
