package io.camunda.demo.process_order;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.client.api.worker.JobClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

@Component
public class ProcessPaymentWorker {
    private final static Logger LOG = LoggerFactory.getLogger(ProcessPaymentWorker.class);

    @JobWorker(type = "process-payment")
    public Map<String, Object> processPayment (final JobClient client, final ActivatedJob job) {

        // Get all process variables
        Map<String, Object> variables = job.getVariablesAsMap();

        // Get individual variables
        String cardNumber = (String) variables.get("textfield_tm0bf");
        String expirationDate = (String) variables.get("datetime_atvbjj");
        String cvv = (String) variables.get("textfield_udprea");


        LOG.info("Card Number: {}", cardNumber);
        LOG.info("Card Holder: {}", cardNumber);

        //Map<String, String> result = new HashMap<>();

        if(cardNumber == null || cardNumber == null || cvv == null) {
            variables.put("pament_status", "not_ok");
        } else if (cvv.isEmpty()) {
            variables.put("pament_status", "not_ok");
        }else if(cvv.equals("111")){
            client.newThrowErrorCommand(job).errorCode("0001").errorMessage("Invalid cvv").send();
        }
        else{
            LOG.info("Card Number: {}", cardNumber);
            LOG.info("CVV: {}", cvv);
            LOG.info("Expiration Date: {}", expirationDate);
            variables.put("pament_status", "ok");
        }


        return variables;
    }

}
