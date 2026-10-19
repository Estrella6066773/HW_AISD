package io.camunda.demo.hospital.domain;

/**
 * 预约占用状态。供排班 / 资源不可用类工作器使用；与用户任务勾选互相独立，以本表为防重复事实源。
 */
public enum BookingSlotStatus {
	CONFIRMED,
	PENDING,
	ESCALATED
}
