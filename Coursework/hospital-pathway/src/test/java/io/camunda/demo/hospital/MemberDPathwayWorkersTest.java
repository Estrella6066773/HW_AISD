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

    @BeforeEach void cleanTestDatabase() { audits.deleteAll(); }

    private Map<String, Object> change() {
        return new HashMap<>(Map.of("patientId", "D-TEST-001", "clinicianId", "DEMO-CLINICIAN",
                "changeTarget", "discharge", "moneyAffected", false));
    }

    private ActivatedJob job(long element, Map<String, Object> vars) {
        var job = mock(ActivatedJob.class);
        when(job.getProcessInstanceKey()).thenReturn(100L);
        when(job.getElementInstanceKey()).thenReturn(element);
        when(job.getVariablesAsMap()).thenReturn(vars);
        return job;
    }

    @Test void approvedChangeSavesNotification() {
        var result = workers.notifyCareChange(job(1, change()));
        assertThat(result).containsEntry("careChangeNotificationSent", true)
                .containsEntry("careChangeNotificationStatus", "SENT");
        assertThat(audits.findAll()).singleElement().satisfies(event -> {
            assertThat(event.getCaseReference()).isEqualTo("D-TEST-001");
            assertThat(event.getActor()).isEqualTo("DEMO-CLINICIAN");
            assertThat(event.getAction()).isEqualTo("notify-care-change");
        });
    }

    @Test void missingApprovalSkipsNotification() {
        var vars = change(); vars.put("changeTarget", "invalid");
        assertThat(workers.notifyCareChange(job(2, vars)))
                .containsEntry("careChangeNotificationSent", false)
                .containsEntry("careChangeNotificationStatus", "SKIPPED_UNAUTHORISED");
        assertThat(audits.findAll()).singleElement().satisfies(e ->
                assertThat(e.getAction()).isEqualTo("notify-care-change-skipped"));
    }

    @Test void paidChangeStillNeedsHumanFinanceReview() {
        var vars = change(); vars.put("moneyAffected", true);
        assertThat(workers.notifyCareChange(job(3, vars)))
                .containsEntry("careChangeNotificationStatus", "SENT_FINANCE_REVIEW_REQUIRED")
                .doesNotContainKeys("moneyAffected", "changeTarget", "fundingStatus", "financeAdjustment");
    }

    @Test void invalidInputCanBeCorrectedAndRetried() {
        var vars = change(); vars.remove("clinicianId");
        var task = job(4, vars);
        assertThatThrownBy(() -> workers.notifyCareChange(task)).isInstanceOf(IllegalArgumentException.class);
        assertThat(audits.count()).isZero();
        vars.put("clinicianId", "DEMO-CLINICIAN");
        assertThat(workers.notifyCareChange(task)).containsEntry("careChangeNotificationSent", true);
        assertThat(audits.count()).isEqualTo(1);
    }

    @Test void retriesReuseReceiptButLaterChangesGetNewReceipts() {
        var task = job(5, change());
        var first = workers.notifyCareChange(task);
        assertThat(workers.notifyCareChange(task)).isEqualTo(first);
        assertThat(audits.count()).isEqualTo(1);
        workers.notifyCareChange(job(6, change()));
        assertThat(audits.count()).isEqualTo(2);
    }

    @Test void unknownTargetIsRejected() {
        var vars = change(); vars.put("changeTarget", "unknown");
        assertThatThrownBy(() -> workers.notifyCareChange(job(7, vars))).isInstanceOf(IllegalArgumentException.class);
        assertThat(audits.count()).isZero();
    }

    @Test void memberBOriginalAppendStillWorks() {
        writer.append("member-B", "check-slot", "D-TEST", "first attempt");
        writer.append("member-B", "check-slot", "D-TEST", "second attempt");
        assertThat(audits.count()).isEqualTo(2);
    }
}
