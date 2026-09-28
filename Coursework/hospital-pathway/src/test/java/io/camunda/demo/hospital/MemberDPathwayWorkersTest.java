package io.camunda.demo.hospital;

import static org.assertj.core.api.Assertions.*;
import static org.mockito.Mockito.*;

import io.camunda.client.api.response.ActivatedJob;
import io.camunda.demo.hospital.domain.*;
import java.util.*;
import java.util.concurrent.*;
import javax.sql.DataSource;
import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.*;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.orm.jpa.*;
import org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter;
import org.springframework.test.context.junit.jupiter.SpringJUnitConfig;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

/** Real H2/JPA integration; only Camunda's incoming job is a test double. */
@SpringJUnitConfig(MemberDPathwayWorkersTest.DatabaseConfig.class)
class MemberDPathwayWorkersTest {
    @Configuration
    @EnableTransactionManagement
    @EnableJpaRepositories(basePackageClasses = AuditEventRepository.class)
    @Import({AuditEventWriter.class, MemberDPathwayWorkers.class})
    static class DatabaseConfig {
        @Bean DataSource dataSource() {
            return new DriverManagerDataSource("jdbc:h2:mem:member_d_test;DB_CLOSE_DELAY=-1", "sa", "");
        }
        @Bean LocalContainerEntityManagerFactoryBean entityManagerFactory(DataSource source) {
            var factory = new LocalContainerEntityManagerFactoryBean();
            factory.setDataSource(source);
            factory.setPackagesToScan("io.camunda.demo.hospital.domain");
            factory.setJpaVendorAdapter(new HibernateJpaVendorAdapter());
            factory.setJpaPropertyMap(Map.of("hibernate.hbm2ddl.auto", "create-drop"));
            return factory;
        }
        @Bean PlatformTransactionManager transactionManager(jakarta.persistence.EntityManagerFactory factory) {
            return new JpaTransactionManager(factory);
        }
    }

    @Autowired MemberDPathwayWorkers workers;
    @Autowired AuditEventRepository audits;
    @Autowired AuditEventWriter writer;
    @Autowired PaymentLedgerRepository payments;
    @Autowired DataSource source;

    @BeforeEach void cleanTestDatabase() { audits.deleteAll(); payments.deleteAll(); }

    private Map<String, Object> change() {
        var vars = new HashMap<String, Object>();
        vars.put("patientId", "D-TEST-001");
        vars.put("clinicianId", "DEMO-CLINICIAN");
        vars.put("modificationDecision", "discharge_unpaid");
        vars.put("changeTarget", "discharge");
        vars.put("moneyAffected", false);
        return vars;
    }

    private ActivatedJob job(long element, Map<String, Object> vars) {
        var job = mock(ActivatedJob.class);
        when(job.getKey()).thenReturn(element + 1000);
        when(job.getProcessInstanceKey()).thenReturn(100L);
        when(job.getElementInstanceKey()).thenReturn(element);
        when(job.getVariablesAsMap()).thenReturn(vars);
        return job;
    }

    @Test void authorisedChangeWritesAuditBeforeReturningSuccess() {
        var result = workers.notifyCareChange(job(1, change()));
        assertThat(result).containsEntry("careChangeNotificationSent", true)
                .containsEntry("careChangeNotificationStatus", "SENT");
        assertThat(audits.findAll()).singleElement().satisfies(event -> {
            assertThat(event.getAction()).isEqualTo("notify-care-change");
            assertThat(event.getCaseReference()).isEqualTo("D-TEST-001");
            assertThat(event.getActor()).isEqualTo("DEMO-CLINICIAN");
        });
    }

    @Test void sameTaskRetryReturnsOriginalAuditReference() {
        var task = job(2, change());
        var first = workers.notifyCareChange(task);
        var second = workers.notifyCareChange(task);
        assertThat(audits.count()).isEqualTo(1);
        assertThat(second).isEqualTo(first);
    }

    @Test void laterChangeForSamePatientCreatesNewEvent() {
        workers.notifyCareChange(job(3, change()));
        workers.notifyCareChange(job(4, change()));
        assertThat(audits.count()).isEqualTo(2);
    }

    @Test void unapprovedChangeDoesNotSendNotification() {
        var vars = change();
        vars.put("modificationDecision", "invalid");
        vars.put("changeTarget", "invalid");
        var result = workers.notifyCareChange(job(5, vars));
        assertThat(result).containsEntry("careChangeNotificationSent", false)
                .containsEntry("careChangeNotificationStatus", "SKIPPED_UNAUTHORISED");
        assertThat(audits.findAll()).noneMatch(e -> e.getAction().equals("notify-care-change"));
    }

    @Test void financialChangeReadsLedgerWithoutApprovingRefund() {
        var payment = new PaymentLedger();
        payment.setCaseReference("D-TEST-001");
        payment.setIdempotencyKey("D-TEST-001|original");
        payment.setAmount("10.01");
        payment.setStatus(PaymentLedgerStatus.SUCCESSFUL);
        payments.saveAndFlush(payment);
        var vars = change();
        vars.put("modificationDecision", "discharge_paid");
        vars.put("moneyAffected", true);
        var result = workers.notifyCareChange(job(6, vars));
        assertThat(result).containsEntry("careChangeNotificationStatus", "SENT_FINANCE_REVIEW_REQUIRED");
        assertThat(audits.findAll()).singleElement().satisfies(e ->
                assertThat(e.getPayloadSummary()).contains("financeReviewRequired=true", "paymentRows=1"));
        assertThat(payments.findAll()).singleElement().satisfies(e -> {
            assertThat(e.getStatus()).isEqualTo(PaymentLedgerStatus.SUCCESSFUL);
            assertThat(e.getAmount()).isEqualTo("10.01");
        });
        assertThat(result).doesNotContainKeys("fundingStatus", "financeAdjustment", "moneyAffected", "changeTarget");
    }

    @Test void paidChangeWithNoLedgerRemainsPendingFinanceReview() {
        var vars = change(); vars.put("modificationDecision", "discharge_paid"); vars.put("moneyAffected", true);
        assertThat(workers.notifyCareChange(job(7, vars)))
                .containsEntry("careChangeNotificationStatus", "SENT_FINANCE_REVIEW_REQUIRED");
        assertThat(payments.count()).isZero();
    }

    @Test void inconsistentRoutingVariablesAreRejected() {
        var vars = change(); vars.put("changeTarget", "treatment");
        assertThatThrownBy(() -> workers.notifyCareChange(job(8, vars))).isInstanceOf(IllegalArgumentException.class);
        assertThat(audits.count()).isZero();
    }

    @Test void missingCaseFailsWithoutAudit() {
        var vars = change(); vars.remove("patientId");
        assertThatThrownBy(() -> workers.notifyCareChange(job(9, vars))).isInstanceOf(IllegalArgumentException.class);
        assertThat(audits.count()).isZero();
    }

    @Test void conflictingCaseIdentifiersAreRejected() {
        var vars = change(); vars.put("case_reference", "ANOTHER-CASE");
        assertThatThrownBy(() -> workers.notifyCareChange(job(10, vars))).isInstanceOf(IllegalArgumentException.class);
    }

    @Test void onceFailureLeavesNoSuccessAndRetryCreatesOneEvent() {
        var vars = change(); vars.put("memberDNotificationFailure", "once");
        var task = job(11, vars);
        assertThatThrownBy(() -> workers.notifyCareChange(task)).isInstanceOf(IllegalStateException.class);
        assertThat(audits.count()).isZero();
        assertThat(workers.notifyCareChange(task)).containsEntry("careChangeNotificationSent", true);
        workers.notifyCareChange(task);
        assertThat(audits.count()).isEqualTo(1);
    }

    @ParameterizedTest
    @CsvSource({"enquiry_admin,AdminEnquiryNotes", "enquiry_clinical,ClinicalEnquiryNotes", "enquiry_finance,FinanceEnquiryNotes"})
    void enquiryAcknowledgesCorrectTeamWithoutCopyingClinicalText(String kind, String noteKey) {
        var vars = new HashMap<String, Object>();
        vars.put("patientId", "D-ENQUIRY"); vars.put("staffRole", "DEMO-STAFF");
        vars.put("requestKind", kind); vars.put(noteKey, "Private clinical detail: do not copy into audit.");
        var result = workers.acknowledgeEnquiry(job(12, vars));
        assertThat(result).containsEntry("enquiryAcknowledgementSent", true);
        assertThat(audits.findAll()).singleElement().satisfies(e -> {
            assertThat(e.getAction()).isEqualTo("ack-enquiry-routed");
            assertThat(e.getPayloadSummary()).contains(kind).doesNotContain("Private clinical detail");
        });
    }

    @Test void enquiryWithoutResponseFailsInsteadOfClosingSilently() {
        var vars = Map.<String, Object>of("patientId", "D-ENQUIRY", "staffRole", "DEMO", "requestKind", "enquiry_admin");
        assertThatThrownBy(() -> workers.acknowledgeEnquiry(job(13, vars))).isInstanceOf(IllegalArgumentException.class);
    }

    @Test void concurrentDeliveryProducesOnlyOneAuditRow() throws Exception {
        var task = job(14, change());
        try (var pool = Executors.newFixedThreadPool(4)) {
            var futures = new ArrayList<Future<Map<String, Object>>>();
            for (int i = 0; i < 4; i++) futures.add(pool.submit(() -> workers.notifyCareChange(task)));
            var results = new ArrayList<Map<String, Object>>();
            for (var f : futures) results.add(f.get(15, TimeUnit.SECONDS));
            assertThat(audits.count()).isEqualTo(1);
            assertThat(results).allMatch(result -> result.equals(results.getFirst()));
        }
    }

    @Test void existingMemberBAuditApiStillAllowsDistinctEvents() {
        writer.append("member-B", "check-slot", "D-TEST", "first attempt");
        writer.append("member-B", "check-slot", "D-TEST", "second attempt");
        assertThat(audits.count()).isEqualTo(2);
    }

    @Test void failedMockRollsBackAuditAndAllowsLaterRetry() {
        assertThatThrownBy(() -> writer.append("D", "notification", "D-ROLLBACK", "D-ROLLBACK-KEY",
                () -> { throw new IllegalStateException("Provider timeout"); }))
                .isInstanceOf(IllegalStateException.class);
        assertThat(audits.count()).isZero();
        var event = writer.append("D", "notification", "D-ROLLBACK", "D-ROLLBACK-KEY", () -> "mock recovered");
        assertThat(event.getId()).isNotNull();
        assertThat(audits.count()).isEqualTo(1);
    }

    @Test void existingReceiptSurvivesWorkerObjectRestart() {
        var task = job(20, change());
        var original = workers.notifyCareChange(task);
        var restarted = new MemberDPathwayWorkers(writer, payments);
        assertThat(restarted.notifyCareChange(task)).isEqualTo(original);
        assertThat(audits.count()).isEqualTo(1);
    }

    @Test void receiptKeyCannotBeReusedForAnotherCase() {
        writer.append("D", "notification", "CASE-A", "D-COLLISION", () -> "first");
        assertThatThrownBy(() -> writer.append("D", "notification", "CASE-B", "D-COLLISION", () -> "second"))
                .isInstanceOf(IllegalArgumentException.class);
        assertThat(audits.findAll()).singleElement().satisfies(e -> assertThat(e.getCaseReference()).isEqualTo("CASE-A"));
    }

    @Test void idempotencyIsBackedByDatabaseUniqueConstraint() {
        var jdbc = new JdbcTemplate(source);
        var count = jdbc.queryForObject("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS c "
                + "JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE k ON c.CONSTRAINT_NAME=k.CONSTRAINT_NAME "
                + "AND c.TABLE_SCHEMA=k.TABLE_SCHEMA WHERE c.TABLE_NAME='AUDIT_EVENT' "
                + "AND c.CONSTRAINT_TYPE='UNIQUE' AND k.COLUMN_NAME='IDEMPOTENCY_KEY'", Integer.class);
        assertThat(count).isEqualTo(1);
    }
}
