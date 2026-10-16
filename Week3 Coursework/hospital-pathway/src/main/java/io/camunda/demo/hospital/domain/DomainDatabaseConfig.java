package io.camunda.demo.hospital.domain;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * 启动时探测领域库表是否可用并打印行数，便于演示证明 schema 已落地。
 *
 * <p>联动：依赖 JPA {@code ddl-auto=update} 建表；不修改、不调用现有 JobWorker。
 * 注意：行数为 0 在首次启动时属正常；数据文件在 {@code ./data/hospital-domain.*}。
 */
@Configuration
public class DomainDatabaseConfig {

	private static final Logger LOG = LoggerFactory.getLogger(DomainDatabaseConfig.class);

	@Bean
	CommandLineRunner probeDomainDatabase(
			PaymentLedgerRepository paymentLedgerRepository,
			BookingSlotRepository bookingSlotRepository,
			AuditEventRepository auditEventRepository) {
		return args -> {
			long payments = paymentLedgerRepository.count();
			long bookings = bookingSlotRepository.count();
			long audits = auditEventRepository.count();
			LOG.info(
					"领域库就绪（H2 文件 ./data/hospital-domain）：payment_ledger={} 行, booking_slot={} 行, audit_event={} 行",
					payments,
					bookings,
					audits);
		};
	}
}
