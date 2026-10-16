package io.camunda.demo.hospital.domain;

/**
 * 账本状态。{@code request-refund} 按财务决定写入：全额/部分退款为 {@code SUCCESSFUL}，
 * 转款为 {@code TRANSFERRED}，保留费用为 {@code RETAINED}，结果未回为 {@code INVESTIGATE}。
 * {@code INVESTIGATE} 表示钱可能已经动过，禁止再自动扣款。
 */
public enum PaymentLedgerStatus {
	SUCCESSFUL,
	UNSUCCESSFUL,
	INVESTIGATE,
	TRANSFERRED,
	RETAINED
}
