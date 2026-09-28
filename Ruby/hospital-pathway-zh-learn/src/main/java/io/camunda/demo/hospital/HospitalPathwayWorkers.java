package io.camunda.demo.hospital;

import io.camunda.client.CamundaClient;
import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.client.api.worker.JobClient;
import java.time.Duration;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/**
 * Classroom workers aligned with {@code Est/est：治疗预约与付款外部工作器.md} and the W02 Message Example
 * publish pattern.
 *
 * <ul>
 *   <li>{@code request-payment} — mock provider, publish BPMN message {@code payment-result}, then
 *       complete the send-task job ({@code autoComplete = false}).
 *   <li>{@code send-booking-confirmation} — mock patient notification; no inbound message wait.
 * </ul>
 *
 * Demo rule for payment: if {@code charge_amount} (default {@code 10.01}) ends with {@code 0},
 * the payment is {@code unsuccessful}; otherwise {@code successful}. Never stores card data.
 */
@Component
public class HospitalPathwayWorkers {

	private static final Logger LOG = LoggerFactory.getLogger(HospitalPathwayWorkers.class);

	private final CamundaClient camundaClient;

	public HospitalPathwayWorkers(CamundaClient camundaClient) {
		this.camundaClient = camundaClient;
	}

	@JobWorker(type = "request-payment", autoComplete = false)
	public void requestPayment(final JobClient jobClient, final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = text(vars.get("case_reference"));
		if (caseReference.isBlank()) {
			caseReference = text(vars.get("patientId"));
		}
		String amount = text(vars.get("charge_amount"));
		if (amount.isBlank()) {
			amount = "10.01";
		}

		if (caseReference.isBlank()) {
			jobClient
					.newFailCommand(job)
					.retries(Math.max(job.getRetries() - 1, 0))
					.errorMessage("payment-input-invalid: case_reference / patientId required")
					.send()
					.join();
			return;
		}

		try {
			Map<String, Object> out = new HashMap<>();
			out.put("case_reference", caseReference);
			out.put("charge_amount", amount);

			if (Boolean.TRUE.equals(vars.get("payment_requested_once"))) {
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
				camundaClient.newCompleteCommand(job.getKey()).variables(out).send().join();
				return;
			}

			boolean successful = !amount.trim().endsWith("0");
			Map<String, Object> messageVars = new HashMap<>();
			if (successful) {
				String tx = "TX-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
				String date = LocalDate.now().toString();
				messageVars.put("payment_status", "successful");
				messageVars.put("transaction_reference", tx);
				messageVars.put("payment_date", date);
				out.put("fundingStatus", "patient_paid");
				LOG.info(
						"request-payment SUCCESS case={} amount={} tx={} date={} (publishing payment-result)",
						caseReference,
						amount,
						tx,
						date);
			} else {
				messageVars.put("payment_status", "unsuccessful");
				messageVars.put("transaction_reference", null);
				messageVars.put("payment_date", null);
				out.put("fundingStatus", "patient_payment_required");
				LOG.info(
						"request-payment UNSUCCESSFUL case={} amount={} (publishing payment-result; demo rule: amount ending in 0 fails)",
						caseReference,
						amount);
			}

			camundaClient
					.newPublishMessageCommand()
					.messageName("payment-result")
					.correlationKey(caseReference)
					.variables(messageVars)
					.timeToLive(Duration.ofMinutes(10))
					.send()
					.join();

			out.putAll(messageVars);
			out.put("payment_requested_once", true);
			camundaClient.newCompleteCommand(job.getKey()).variables(out).send().join();
		} catch (Exception e) {
			LOG.error("request-payment failed to publish payment-result for case={}", caseReference, e);
			jobClient
					.newFailCommand(job)
					.retries(Math.max(job.getRetries() - 1, 0))
					.errorMessage("Could not publish payment-result: " + e.getMessage())
					.send()
					.join();
		}
	}

	@JobWorker(type = "send-booking-confirmation")
	public Map<String, Object> sendBookingConfirmation(final ActivatedJob job) {
		Map<String, Object> vars = job.getVariablesAsMap();
		String caseReference = text(vars.get("case_reference"));
		if (caseReference.isBlank()) {
			caseReference = text(vars.get("patientId"));
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
			out.put("case_reference", caseReference);
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
