package io.camunda.demo.process_order;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import org.springframework.stereotype.Component;

import java.util.Map;

@Component
public class SendApoinmentCancelationEmail {
    @JobWorker(type = "send-apoinment-cancel-email")
    public Map<String,Object> sendFinalisedEmail (final ActivatedJob job) {
        Map<String, Object> result = job.getVariablesAsMap();
        System.out.println("Send apoinment-cancel-email");
        result.put("status", "Unsuccessful");
        return result;
    }
}
