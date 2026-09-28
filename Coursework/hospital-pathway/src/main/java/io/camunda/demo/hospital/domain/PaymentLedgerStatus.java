package io.camunda.demo.hospital.domain;

/**
 * 支付流水状态。由后续支付类工作器写入 {@link PaymentLedger}；本切片只建库，不改现有 JobWorker。
 * 注意：不含卡号相关取值；{@code INVESTIGATE} 对应「服务商可能已扣款、本院待核对」。
 */
public enum PaymentLedgerStatus {
	SUCCESSFUL,
	UNSUCCESSFUL,
	INVESTIGATE
}
