package io.camunda.demo.treatment_booking;

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
 * 治疗预约与付款的外部工作器进程。
 * Maven 工程放在仓库的 {@code Coursework/}。启动后连接本机 Camunda（REST 8090，gRPC 26500），
 * 把打包进来的可执行模型和六张表单一并部署，然后保持运行。
 * 领任务的是 {@link TreatmentBookingWorkers}，本类只负责进程启动和部署。
 */
@SpringBootApplication
public class TreatmentBookingApplication {

	private static final Logger LOG = LoggerFactory.getLogger(TreatmentBookingApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(TreatmentBookingApplication.class, args);
	}

	/**
	 * 工作器开始领任务之前完成部署。
	 * {@code Coursework/pom.xml} 在编译时把 {@code ../Est} 下的可执行模型和 {@code ../Est/forms} 复制进 classpath。
	 * 表单文件里的 id 必须与模型中的 formId 相同，Tasklist 才能打开第一张表单。
	 */
	@Bean
	CommandLineRunner deployAndLogSubscription(CamundaClient camundaClient) {
		return args -> {
			PathMatchingResourcePatternResolver resolver = new PathMatchingResourcePatternResolver();
			Resource[] bpmnFiles = resolver.getResources("classpath*:bpmn/*.bpmn");
			Resource[] formFiles = resolver.getResources("classpath*:forms/*.form");
			if (bpmnFiles.length == 0 || formFiles.length == 0) {
				throw new IllegalStateException("未找到可部署的流程图或表单");
			}

			DeployResourceCommandStep2 command = null;
			for (Resource resource : bpmnFiles) {
				command = append(camundaClient, command, resource);
			}
			for (Resource resource : formFiles) {
				command = append(camundaClient, command, resource);
			}
			DeploymentEvent deployment = command.send().join();
			LOG.info("已部署治疗预约与付款流程，部署键 {}", deployment.getKey());
			LOG.info("已订阅任务类型 request-payment 与 send-booking-confirmation");
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
