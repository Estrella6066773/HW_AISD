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
 * 部署全院流程 {@code Hospital_All_Processes_Simple_C8}。
 * 依据 {@code Coursework/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn}：
 * 每个工作步骤都是用户任务，指派给 demo，共用表单 {@code hospital_task_form}。
 * 协作图上指向支付服务、排程和信函服务的箭头只表示对外往来，流程里没有消息订阅，也没有服务任务。
 * 因此本进程不注册任务工作器。部署写入引擎后进程可以退出；Tasklist 从引擎领取用户任务，不依赖本进程继续运行。
 * 人提交表单后，引擎用各任务的输出映射写入网关变量。
 */
@SpringBootApplication
public class HospitalPathwayApplication {

	private static final Logger LOG = LoggerFactory.getLogger(HospitalPathwayApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(HospitalPathwayApplication.class, args);
	}

	/**
	 * 启动时部署流程图和共用表单。没有任务工作器时，Spring 进程在部署结束后退出，部署本身留在引擎上。
	 * classpath 里的文件由 {@code Coursework/pom.xml} 从本目录复制。
	 * 表单 id 必须是 {@code hospital_task_form}，与模型中每个用户任务的 formId 相同。
	 * 提交变量是 {@code patientId}、{@code action}、{@code notes}；网关不直接读 {@code action}，
	 * 而读各任务输出映射写回的 {@code requestKind}、{@code fundingStatus} 等流程变量。
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
			LOG.info("用户任务使用表单 hospital_task_form，指派给 demo。本流程没有外部任务类型");
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
