package io.camunda.demo.process_order;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

@Component
public class SendApoinmentConfirmationEmail {
    @JobWorker(type = "send-apoinment-finalised-email")
    public Map<String,Object> sendFinalisedEmail (final ActivatedJob job) {
        Map<String, Object> result = job.getVariablesAsMap();
        System.out.println("Send apoinment-finalised-email");
        result.put("status", "success");
        return result;
    }
}
