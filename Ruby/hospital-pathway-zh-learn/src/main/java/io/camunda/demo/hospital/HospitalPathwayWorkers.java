package io.camunda.demo.hospital;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/**
 * Classroom workers for the two service tasks on
 * {@code Coursework/hospital-pathway/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn}.
 *
 * <ul>
 *   <li>{@code request-payment} — mock Payment Provider; returns result inline (no message catch).</li>
 *   <li>{@code send-booking-confirmation} — mock patient notification after treatment slot is ready.</li>
 * </ul>
 *
 * Demo rule for payment: if {@code charge_amount} (default {@code 10.01}) ends with {@code 0},
 * the payment is {@code unsuccessful}; otherwise {@code successful}. Never stores card data.
 */
@Component
public class HospitalPathwayWorkers {

	private static final Logger LOG = LoggerFactory.getLogger(HospitalPathwayWorkers.class);

	@JobWorker(type = "request-payment")
	public Map<String, Object> requestPayment(final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = text(vars.get("patientId"));
		if (caseReference.isBlank()) {
			caseReference = text(vars.get("case_reference"));
		}
		String amount = text(vars.get("charge_amount"));
		if (amount.isBlank()) {
			amount = "10.01";
		}
		boolean alreadyRequested = Boolean.TRUE.equals(vars.get("payment_requested_once"));

		Map<String, Object> out = new HashMap<>();
		if (alreadyRequested) {
			LOG.info(
					"request-payment idempotent reuse for case={} status={} ref={}",
					caseReference,
					vars.get("payment_status"),
					vars.get("transaction_reference"));
			out.put("payment_status", vars.get("payment_status"));
			out.put("transaction_reference", vars.get("transaction_reference"));
			out.put("payment_date", vars.get("payment_date"));
			out.put("payment_requested_once", true);
			out.put("fundingStatus", vars.get("fundingStatus"));
			out.put("charge_amount", amount);
			return out;
		}

		boolean successful = !amount.trim().endsWith("0");
		if (successful) {
			String tx = "TX-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
			String date = LocalDate.now().toString();
			out.put("payment_status", "successful");
			out.put("transaction_reference", tx);
			out.put("payment_date", date);
			out.put("fundingStatus", "patient_paid");
			LOG.info(
					"request-payment SUCCESS case={} amount={} tx={} date={}",
					caseReference,
					amount,
					tx,
					date);
		} else {
			out.put("payment_status", "unsuccessful");
			out.put("transaction_reference", null);
			out.put("payment_date", null);
			out.put("fundingStatus", "patient_payment_required");
			LOG.info(
					"request-payment UNSUCCESSFUL case={} amount={} (demo rule: amount ending in 0 fails)",
					caseReference,
					amount);
		}
		out.put("payment_requested_once", true);
		out.put("charge_amount", amount);
		out.put("case_reference", caseReference);
		return out;
	}

	@JobWorker(type = "send-booking-confirmation")
	public Map<String, Object> sendBookingConfirmation(final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = text(vars.get("patientId"));
		if (caseReference.isBlank()) {
			caseReference = text(vars.get("case_reference"));
		}
		String bookingReference = text(vars.get("booking_reference"));
		if (bookingReference.isBlank()) {
			bookingReference = "BK-" + (caseReference.isBlank() ? "DEMO" : caseReference);
		}

		if (Boolean.TRUE.equals(vars.get("confirmation_sent"))) {
			LOG.info(
					"send-booking-confirmation already sent case={} booking={}",
					caseReference,
					bookingReference);
			Map<String, Object> out = new HashMap<>();
			out.put("confirmation_sent", true);
			out.put("booking_reference", bookingReference);
			return out;
		}

		LOG.info(
				"send-booking-confirmation SENT case={} booking={} (mocked correspondence)",
				caseReference,
				bookingReference);
		Map<String, Object> out = new HashMap<>();
		out.put("confirmation_sent", true);
		out.put("booking_reference", bookingReference);
		out.put("case_reference", caseReference);
		return out;
	}

	private static String text(Object value) {
		return value == null ? "" : String.valueOf(value).trim();
	}
}
