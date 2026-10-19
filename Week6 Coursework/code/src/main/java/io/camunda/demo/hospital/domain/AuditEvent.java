package io.camunda.demo.hospital.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;
import java.time.Instant;

/**
 * 审计事件表实体（audit_event）。
 *
 * <p>联动：只通过 {@link AuditEventWriter#append} 插入；查询走 {@link AuditEventRepository}。
 * 普通业务代码不应直接 {@code save} 已有行做修改。
 *
 * <p>注意：摘要载荷勿写入卡号或病历正文；表无业务更新接口是有意设计（PB-11）。
 */
@Entity
@Table(name = "audit_event", uniqueConstraints =
        @UniqueConstraint(name = "uk_audit_event_idempotency", columnNames = "idempotency_key"))
public class AuditEvent {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@Column(name = "actor", nullable = false, length = 128)
	private String actor;

	@Column(name = "action", nullable = false, length = 128)
	private String action;

	@Column(name = "case_reference", length = 128)
	private String caseReference;

	@Column(name = "occurred_at", nullable = false)
	private Instant occurredAt = Instant.now();

	@Column(name = "payload_summary", length = 512)
	private String payloadSummary;

	/** Optional: old append callers keep NULL; D receipts use one key per task occurrence. */
	@Column(name = "idempotency_key", length = 256)
	private String idempotencyKey;

	public String getIdempotencyKey() { return idempotencyKey; }

	public void setIdempotencyKey(String idempotencyKey) { this.idempotencyKey = idempotencyKey; }

	public Long getId() {
		return id;
	}

	public String getActor() {
		return actor;
	}

	public void setActor(String actor) {
		this.actor = actor;
	}

	public String getAction() {
		return action;
	}

	public void setAction(String action) {
		this.action = action;
	}

	public String getCaseReference() {
		return caseReference;
	}

	public void setCaseReference(String caseReference) {
		this.caseReference = caseReference;
	}

	public Instant getOccurredAt() {
		return occurredAt;
	}

	public void setOccurredAt(Instant occurredAt) {
		this.occurredAt = occurredAt;
	}

	public String getPayloadSummary() {
		return payloadSummary;
	}

	public void setPayloadSummary(String payloadSummary) {
		this.payloadSummary = payloadSummary;
	}
}
