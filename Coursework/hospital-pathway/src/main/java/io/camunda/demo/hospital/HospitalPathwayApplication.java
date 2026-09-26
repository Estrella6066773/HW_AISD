package io.camunda.demo.hospital;

import io.camunda.client.CamundaClient;
import io.camunda.client.api.command.DeployResourceCommandStep1;
import io.camunda.client.api.command.DeployResourceCommandStep1.DeployResourceCommandStep2;
import io.camunda.client.api.response.DeploymentEvent;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

/**
 * Deploys {@code Hospital_All_Processes_Simple_C8} and keeps the process listening for
 * the two classroom service tasks. Package layout lives under
 * {@code Coursework/hospital-pathway/}: BPMN + {@code hospital_task_form} + these workers.
 * User tasks still drive clinical / finance decisions; {@code request-payment} and
 * {@code send-booking-confirmation} cover the automated hand-offs.
 */
@SpringBootApplication
public class HospitalPathwayApplication {

	private static final Logger LOG = LoggerFactory.getLogger(HospitalPathwayApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(HospitalPathwayApplication.class, args);
	}

	/**
	 * Deploys the BPMN and shared form from this Maven module. Workers stay registered
	 * for the lifetime of the process. Form id must remain {@code hospital_task_form}.
	 */
	@Bean
	CommandLineRunner deployHospitalPathway(CamundaClient camundaClient) {
		return args -> {
			PathMatchingResourcePatternResolver resolver = new PathMatchingResourcePatternResolver();
			Resource[] bpmnFiles = resolver.getResources(
					"classpath*:bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn");
			Resource[] formFiles = resolver.getResources("classpath*:forms/hospital_task_form.form");
			if (bpmnFiles.length != 1 || formFiles.length != 1) {
				throw new IllegalStateException("未找到全院流程图或共用表单 hospital_task_form");
			}

			DeployResourceCommandStep2 command = null;
			for (Resource resource : bpmnFiles) {
				command = append(camundaClient, command, resource);
			}
			for (Resource resource : formFiles) {
				command = append(camundaClient, command, resource);
			}
			DeploymentEvent deployment = command.send().join();
			LOG.info("已部署全院流程 Hospital_All_Processes_Simple_C8，部署键 {}", deployment.getKey());
			LOG.info(
					"用户任务: hospital_task_form / demo。服务任务: request-payment, send-booking-confirmation");
		};
	}

	private static DeployResourceCommandStep2 append(
			CamundaClient camundaClient, DeployResourceCommandStep2 command, Resource resource)
			throws Exception {
		byte[] bytes = resource.getInputStream().readAllBytes();
		String name = resource.getFilename();
		if (command == null) {
			DeployResourceCommandStep1 first = camundaClient.newDeployResourceCommand();
			return first.addResourceBytes(bytes, name);
		}
		return command.addResourceBytes(bytes, name);
	}
}
