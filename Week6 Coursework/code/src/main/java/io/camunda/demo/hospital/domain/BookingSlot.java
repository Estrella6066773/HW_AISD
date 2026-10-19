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

/**
 * 预约占用表实体（booking_slot）。
 *
 * <p>联动：排班占号、外部资源不可用等后续工作器共用本表做防重复；与 Tasklist 用户任务勾选并行存在时，
 * 以本表状态为「是否已建号」的权威记录。
 *
 * <p>注意：{@link #occupancyKey} 库内唯一；无合适号源时写 {@link BookingSlotStatus#PENDING}，禁止静默写成窗外 CONFIRMED。
 */
@Entity
@Table(
		name = "booking_slot",
		uniqueConstraints =
				@UniqueConstraint(name = "uk_booking_slot_occupancy", columnNames = "occupancy_key"))
public class BookingSlot {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@Column(name = "case_reference", nullable = false, length = 128)
	private String caseReference;

	/**
	 * 防重复占用键。例如病例号 + 时间窗 + 资源类型；同一键不得插入第二条占用。
	 */
	@Column(name = "occupancy_key", nullable = false, length = 256)
	private String occupancyKey;

	/** 人类可读的时间窗或资源说明，便于演示核对。 */
	@Column(name = "time_window", length = 128)
	private String timeWindow;

	@Enumerated(EnumType.STRING)
	@Column(name = "status", nullable = false, length = 32)
	private BookingSlotStatus status;

	@Column(name = "retry_count", nullable = false)
	private int retryCount = 0;

	@Column(name = "last_retry_at")
	private Instant lastRetryAt;

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

	public String getOccupancyKey() {
		return occupancyKey;
	}

	public void setOccupancyKey(String occupancyKey) {
		this.occupancyKey = occupancyKey;
	}

	public String getTimeWindow() {
		return timeWindow;
	}

	public void setTimeWindow(String timeWindow) {
		this.timeWindow = timeWindow;
	}

	public BookingSlotStatus getStatus() {
		return status;
	}

	public void setStatus(BookingSlotStatus status) {
		this.status = status;
	}

	public int getRetryCount() {
		return retryCount;
	}

	public void setRetryCount(int retryCount) {
		this.retryCount = retryCount;
	}

	public Instant getLastRetryAt() {
		return lastRetryAt;
	}

	public void setLastRetryAt(Instant lastRetryAt) {
		this.lastRetryAt = lastRetryAt;
	}

	public Instant getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(Instant createdAt) {
		this.createdAt = createdAt;
	}
}
