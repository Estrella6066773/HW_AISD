package io.camunda.demo.treatment_booking;

import io.camunda.client.CamundaClient;
import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.client.api.worker.JobClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.Duration;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

/**
 * 医院流程里两个服务任务的外部工作器。
 * 任务类型必须与 {@code Est/W02_Treatment_Booking_Payment_Executable.bpmn} 里的
 * {@code zeebe:taskDefinition type} 一致。行为以 {@code Est/est：治疗预约与付款外部工作器.md} 为准。
 * 引擎在服务任务激活后把任务交给本类；本类不由用户任务或其他流程调用。
 */
@Component
public class TreatmentBookingWorkers {

	private static final Logger LOG = LoggerFactory.getLogger(TreatmentBookingWorkers.class);
	private static final String MESSAGE_PAYMENT_RESULT = "payment-result";

	private final CamundaClient camundaClient;

	public TreatmentBookingWorkers(CamundaClient camundaClient) {
		this.camundaClient = camundaClient;
	}

	/**
	 * 处理「发出付款请求」。
	 * 先发布消息 {@code payment-result}，关联键是病例号，再完成任务。
	 * {@code autoComplete = false}，避免消息尚未发出时任务已被引擎完成。
	 * 可执行模型上没有 {@code payment-input-invalid} 的错误边界事件，抛出该错误后流程会停成事件，留给步骤 7 查看。
	 */
	@JobWorker(type = "request-payment", autoComplete = false)
	public void requestPayment(final JobClient jobClient, final ActivatedJob job) {
		Map<String, Object> variables = job.getVariablesAsMap();
		String caseReference = text(variables.get("case_reference"));
		String amountText = twoDecimalText(variables.get("charge_amount"));
		boolean paymentRequired = truth(variables.get("patient_payment_required"));
		boolean alreadyRequested = truth(variables.get("payment_requested_once"));

		try {
			if (caseReference == null || amountText == null || !paymentRequired) {
				LOG.info("付款请求输入无效，病例号={}", caseReference);
				jobClient
						.newThrowErrorCommand(job)
						.errorCode("payment-input-invalid")
						.errorMessage("病例号、金额或是否需要患者付款无效，未发出付款消息")
						.send()
						.join();
				return;
			}

			if (alreadyRequested) {
				LOG.info("付款请求已经发出过，沿用原结果，病例号={}", caseReference);
				complete(job, existingPayment(variables));
				return;
			}

			Map<String, Object> result = new HashMap<>();
			if (amountText.endsWith("0")) {
				result.put("payment_status", "unsuccessful");
				result.put("transaction_reference", "");
				result.put("payment_date", "");
			} else {
				result.put("payment_status", "successful");
				result.put("transaction_reference", "TX-" + caseReference + "-" + System.currentTimeMillis());
				result.put("payment_date", LocalDate.now().toString());
			}
			LOG.info(
					"付款请求结果，病例号={}，状态={}",
					caseReference,
					result.get("payment_status"));

			camundaClient
					.newPublishMessageCommand()
					.messageName(MESSAGE_PAYMENT_RESULT)
					.correlationKey(caseReference)
					.variables(result)
					.timeToLive(Duration.ofMinutes(10))
					.send()
					.join();

			result.put("payment_requested_once", true);
			complete(job, result);
		} catch (RuntimeException exception) {
			LOG.warn("发出付款请求失败，病例号={}", caseReference, exception);
			jobClient
					.newFailCommand(job)
					.retries(Math.max(job.getRetries() - 1, 0))
					.errorMessage("未能发布付款结果消息：" + exception.getMessage())
					.send()
					.join();
		}
	}

	/**
	 * 处理「发出预约确认」。
	 * 只写回 {@code confirmation_sent}，不发布消息。模型里没有等待预约确认消息的捕获事件。
	 * 显式完成任务，这样抛出 {@code booking-input-invalid} 之后不会再自动完成一次。
	 */
	@JobWorker(type = "send-booking-confirmation", autoComplete = false)
	public void sendBookingConfirmation(final JobClient jobClient, final ActivatedJob job) {
		Map<String, Object> variables = job.getVariablesAsMap();
		String caseReference = text(variables.get("case_reference"));
		String bookingReference = text(variables.get("booking_reference"));
		LOG.info("发出预约确认，病例号={}，预约号={}", caseReference, bookingReference);

		if (bookingReference == null) {
			jobClient
					.newThrowErrorCommand(job)
					.errorCode("booking-input-invalid")
					.errorMessage("预约号为空，未发出预约确认")
					.send()
					.join();
			return;
		}

		Map<String, Object> result = new HashMap<>();
		result.put("confirmation_sent", true);
		complete(job, result);
	}

	private void complete(ActivatedJob job, Map<String, Object> variables) {
		camundaClient.newCompleteCommand(job.getKey()).variables(variables).send().join();
	}

	private static Map<String, Object> existingPayment(Map<String, Object> variables) {
		Map<String, Object> result = new HashMap<>();
		result.put("payment_status", variables.get("payment_status"));
		result.put("transaction_reference", variables.get("transaction_reference"));
		result.put("payment_date", variables.get("payment_date"));
		result.put("payment_requested_once", true);
		return result;
	}

	private static String text(Object value) {
		if (value == null) {
			return null;
		}
		String text = value.toString().trim();
		return text.isEmpty() ? null : text;
	}

	private static boolean truth(Object value) {
		if (value instanceof Boolean flag) {
			return flag;
		}
		return value != null && "true".equalsIgnoreCase(value.toString().trim());
	}

	/**
	 * 金额按两位小数比较是否以 0 结尾。{@code 10.50} 算作失败路径，{@code 10.01} 算作成功路径。
	 * 表单数字进入流程后可能是整数或小数，不能直接用 {@code toString} 判断末位。
	 */
	private static String twoDecimalText(Object value) {
		if (value == null) {
			return null;
		}
		String raw = value.toString().trim();
		if (raw.isEmpty()) {
			return null;
		}
		BigDecimal amount = value instanceof BigDecimal decimal
				? decimal
				: value instanceof Number number
						? BigDecimal.valueOf(number.doubleValue())
						: new BigDecimal(raw);
		return amount.setScale(2, RoundingMode.HALF_UP).toPlainString();
	}
}
