package io.camunda.demo.hospital.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;
import java.time.Instant;
import java.time.LocalDate;

/**
 * 支付流水表实体（payment_ledger）。
 *
 * <p>联动：后续 {@code request-payment} / 退款类工作器应先按 {@link #idempotencyKey} 查询再决定是否模拟扣款；
 * 流程变量仍由工作器写回引擎，本表是跨重试可核对的账本。
 *
 * <p>注意：表结构禁止卡号、安全码、病历正文；幂等键必须库内唯一。
 */
@Entity
@Table(
		name = "payment_ledger",
		uniqueConstraints =
				@UniqueConstraint(name = "uk_payment_ledger_idempotency", columnNames = "idempotency_key"))
public class PaymentLedger {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	/** 与 BPMN 消息关联键一致，通常来自 patientId / case_reference。 */
	@Column(name = "case_reference", nullable = false, length = 128)
	private String caseReference;

	/**
	 * 防重复扣款键。约定由调用方拼接，例如 {@code caseReference + "|" + chargeAmount}；
	 * 同一键第二次写入应失败或改为先查后复用。
	 */
	@Column(name = "idempotency_key", nullable = false, length = 256)
	private String idempotencyKey;

	@Column(name = "transaction_reference", length = 64)
	private String transactionReference;

	@Column(name = "amount", nullable = false, length = 32)
	private String amount;

	@Enumerated(EnumType.STRING)
	@Column(name = "status", nullable = false, length = 32)
	private PaymentLedgerStatus status;

	@Column(name = "payment_date")
	private LocalDate paymentDate;

	@Column(name = "created_at", nullable = false)
	private Instant createdAt = Instant.now();

	public Long getId() {
		return id;
	}

	public String getCaseReference() {
		return caseReference;
	}

	public void setCaseReference(String caseReference) {
		this.caseReference = caseReference;
	}

	public String getIdempotencyKey() {
		return idempotencyKey;
	}

	public void setIdempotencyKey(String idempotencyKey) {
		this.idempotencyKey = idempotencyKey;
	}

	public String getTransactionReference() {
		return transactionReference;
	}

	public void setTransactionReference(String transactionReference) {
		this.transactionReference = transactionReference;
	}

	public String getAmount() {
		return amount;
	}

	public void setAmount(String amount) {
		this.amount = amount;
	}

	public PaymentLedgerStatus getStatus() {
		return status;
	}

	public void setStatus(PaymentLedgerStatus status) {
		this.status = status;
	}

	public LocalDate getPaymentDate() {
		return paymentDate;
	}

	public void setPaymentDate(LocalDate paymentDate) {
		this.paymentDate = paymentDate;
	}

	public Instant getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(Instant createdAt) {
		this.createdAt = createdAt;
	}
}
