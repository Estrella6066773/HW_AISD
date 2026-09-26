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
 * Deploys the hospital pathway BPMN plus all Camunda forms, then keeps running so the
 * service-task workers can process jobs.
 */
@SpringBootApplication
public class HospitalPathwayApplication {

	private static final Logger LOG = LoggerFactory.getLogger(HospitalPathwayApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(HospitalPathwayApplication.class, args);
	}

	@Bean
	CommandLineRunner deployHospitalPathway(CamundaClient camundaClient) {
		return args -> {
			PathMatchingResourcePatternResolver resolver = new PathMatchingResourcePatternResolver();
			Resource[] bpmnFiles = resolver.getResources(
					"classpath*:bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn");
			Resource[] formFiles = resolver.getResources("classpath*:forms/*.form");
			if (bpmnFiles.length != 1) {
				throw new IllegalStateException("未找到全院流程图");
			}
			if (formFiles.length < 10) {
				throw new IllegalStateException("表单数量不足，当前=" + formFiles.length);
			}

			DeployResourceCommandStep2 command = append(camundaClient, null, bpmnFiles[0]);
			for (Resource form : formFiles) {
				command = append(camundaClient, command, form);
			}

			DeploymentEvent deployment = command.send().join();
			LOG.info("已部署 Hospital_All_Processes_Simple_C8，部署键 {}", deployment.getKey());
			LOG.info("已部署 {} 个表单（硬编码下拉，无 valuesKey）", formFiles.length);
			LOG.info("Workers: request-payment, send-booking-confirmation (keep this process running)");
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
