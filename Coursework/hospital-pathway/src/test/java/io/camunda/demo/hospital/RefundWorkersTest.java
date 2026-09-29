package io.camunda.demo.hospital;

import static org.assertj.core.api.Assertions.*;
import static org.mockito.Mockito.*;

import io.camunda.client.api.response.ActivatedJob;
import io.camunda.demo.hospital.domain.*;
import java.util.*;
import javax.sql.DataSource;
import org.junit.jupiter.api.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.*;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.orm.jpa.*;
import org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter;
import org.springframework.test.context.junit.jupiter.SpringJUnitConfig;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

/** Real H2/JPA; Camunda job mocked. Covers Ruby refund / investigate workers. */
@SpringJUnitConfig(RefundWorkersTest.DatabaseConfig.class)
class RefundWorkersTest {

	@Configuration
	@EnableTransactionManagement
	@EnableJpaRepositories(basePackageClasses = PaymentLedgerRepository.class)
	@Import({AuditEventWriter.class, RefundWorkers.class})
	static class DatabaseConfig {
		@Bean
		DataSource dataSource() {
			return new DriverManagerDataSource("jdbc:h2:mem:refund_workers_test;DB_CLOSE_DELAY=-1", "sa", "");
		}

		@Bean
		LocalContainerEntityManagerFactoryBean entityManagerFactory(DataSource source) {
			var factory = new LocalContainerEntityManagerFactoryBean();
			factory.setDataSource(source);
			factory.setPackagesToScan("io.camunda.demo.hospital.domain");
			factory.setJpaVendorAdapter(new HibernateJpaVendorAdapter());
			factory.setJpaPropertyMap(Map.of("hibernate.hbm2ddl.auto", "create-drop"));
			return factory;
		}

		@Bean
		PlatformTransactionManager transactionManager(jakarta.persistence.EntityManagerFactory factory) {
			return new JpaTransactionManager(factory);
		}
	}

	@Autowired RefundWorkers workers;
	@Autowired PaymentLedgerRepository ledgers;
	@Autowired AuditEventRepository audits;

	@BeforeEach
	void clean() {
		ledgers.deleteAll();
		audits.deleteAll();
	}

	private ActivatedJob job(Map<String, Object> vars) {
		var job = mock(ActivatedJob.class);
		when(job.getVariablesAsMap()).thenReturn(vars);
		return job;
	}

	@Test
	void resolvedRefundWritesSuccessfulLedger() {
		var vars = new HashMap<String, Object>();
		vars.put("patientId", "A-REF-001");
		vars.put("financeAdjustment", "resolved");
		vars.put("charge_amount", "25.50");

		var result = workers.requestRefund(job(vars));
		assertThat(result)
				.containsEntry("refund_recorded", true)
				.containsEntry("refund_status", "SUCCESSFUL");
		assertThat(ledgers.findAll()).singleElement().satisfies(row -> {
			assertThat(row.getCaseReference()).isEqualTo("A-REF-001");
			assertThat(row.getStatus()).isEqualTo(PaymentLedgerStatus.SUCCESSFUL);
			assertThat(row.getAmount()).isEqualTo("25.50");
			assertThat(row.getTransactionReference()).startsWith("RF-");
		});
		assertThat(audits.findAll()).singleElement().satisfies(e -> {
			assertThat(e.getAction()).isEqualTo("request-refund");
			assertThat(e.getActor()).isEqualTo("ruby");
		});
	}

	@Test
	void pendingRefundWritesInvestigateLedger() {
		var vars = Map.<String, Object>of(
				"case_reference", "A-REF-002", "financeAdjustment", "pending", "charge_amount", "10.01");
		assertThat(workers.requestRefund(job(new HashMap<>(vars))))
				.containsEntry("refund_recorded", false)
				.containsEntry("refund_status", "INVESTIGATE");
		assertThat(ledgers.findAll()).singleElement().satisfies(row ->
				assertThat(row.getStatus()).isEqualTo(PaymentLedgerStatus.INVESTIGATE));
	}

	@Test
	void refundRetryReusesSameLedgerRow() {
		var vars = new HashMap<String, Object>();
		vars.put("patientId", "A-REF-003");
		vars.put("financeAdjustment", "resolved");
		vars.put("charge_amount", "12.00");
		var task = job(vars);
		var first = workers.requestRefund(task);
		assertThat(workers.requestRefund(task)).isEqualTo(first);
		assertThat(ledgers.count()).isEqualTo(1);
		assertThat(audits.count()).isEqualTo(1);
	}

	@Test
	void markInvestigateWritesInvestigateAndSkipsAutoChargeFlag() {
		var vars = new HashMap<String, Object>();
		vars.put("patientId", "A-INV-001");
		vars.put("charge_amount", "10.00");
		vars.put("transaction_reference", "TX-DEMO01");

		assertThat(workers.markPaymentInvestigate(job(vars)))
				.containsEntry("payment_investigate", true)
				.containsEntry("payment_status", "investigate")
				.containsEntry("investigate_transaction_reference", "TX-DEMO01");
		assertThat(ledgers.findAll()).singleElement().satisfies(row -> {
			assertThat(row.getStatus()).isEqualTo(PaymentLedgerStatus.INVESTIGATE);
			assertThat(row.getTransactionReference()).isEqualTo("TX-DEMO01");
		});
	}

	@Test
	void missingCaseIdFailsWithoutWriting() {
		assertThatThrownBy(() -> workers.requestRefund(job(Map.of("financeAdjustment", "resolved"))))
				.isInstanceOf(IllegalArgumentException.class);
		assertThat(ledgers.count()).isZero();
		assertThat(audits.count()).isZero();
	}
}
