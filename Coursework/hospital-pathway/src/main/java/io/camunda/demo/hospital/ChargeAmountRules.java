package io.camunda.demo.hospital;

import java.math.BigDecimal;
import java.util.regex.Pattern;

/**
 * 资金表单与 {@link HospitalPathwayWorkers}、{@link RefundWorkers} 共用的收费金额规则。
 *
 * <p>联动：Tasklist 上的 {@code funding_assessment} 用数字字段和条件必填先拦住非法输入。
 * 工作器仍要再查一次，因为空的 {@code charge_amount} 以前会被补成演示值 {@code 10.01} 并继续扣款或记账。
 *
 * <p>注意：只接受恰好两位小数的十进制字符串，范围 0.01 到 99999.99。
 * 表单字段必须 {@code serializeToString=true}，否则 {@code 10.00} 可能变成 {@code 10} 或 {@code 10.0}，精度校验会拒绝。
 * 格式合法之后，支付演示规则仍是「以 0 结尾则失败」，例如 {@code 10.00} 失败、{@code 10.01} 成功。
 */
public final class ChargeAmountRules {

	public static final BigDecimal MIN = new BigDecimal("0.01");
	public static final BigDecimal MAX = new BigDecimal("99999.99");

	private static final Pattern TWO_DECIMALS = Pattern.compile("^[0-9]+\\.[0-9]{2}$");

	private ChargeAmountRules() {}

	/**
	 * @param raw 流程变量 {@code charge_amount}，来自资金表单或上游任务
	 * @return 通过校验的原文字，供演示规则 {@code endsWith("0")} 使用
	 * @throws IllegalArgumentException 缺失、非数字、负数、小数位不是两位，或超出范围
	 */
	public static String require(Object raw) {
		String text = raw == null ? "" : String.valueOf(raw).trim();
		if (text.isEmpty()) {
			throw new IllegalArgumentException(
					"charge_amount required: enter a two-decimal amount from 0.01 to 99999.99");
		}
		if (!TWO_DECIMALS.matcher(text).matches()) {
			throw new IllegalArgumentException(
					"charge_amount precision: use exactly two decimal places, got '" + text + "'");
		}
		BigDecimal amount = new BigDecimal(text);
		if (amount.compareTo(MIN) < 0 || amount.compareTo(MAX) > 0) {
			throw new IllegalArgumentException(
					"charge_amount range: must be from 0.01 to 99999.99, got " + text);
		}
		return text;
	}
}
