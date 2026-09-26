package io.camunda.demo.process_order;

import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.client.api.worker.JobClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.util.Map;

@Component
public class ProcessDetails {

    //Logger to log information in needed
    private final static Logger LOG = LoggerFactory.getLogger(ProcessDetails.class);

    /*Add the Job Worker
     * Type should be same as the Service Task -> Task Definition -> Job Type
     */

    @JobWorker(type = "process-details")
    public Map<String, Object> shipItems(final JobClient client,final ActivatedJob job) {
        //Get Process Variables
        Map<String,Object> variables = job.getVariablesAsMap();
        String firstName = (String) variables.get("first_name");
        String lastName = (String) variables.get("last_name");
        Boolean isConfirmed = (Boolean) variables.get("confirm");

        if (isConfirmed) {
            //add details to process
            variables.put("messge", firstName + " " + lastName + " " + isConfirmed);
        }else {
            variables.put("messge","Details Not confirmed");
            client.newThrowErrorCommand(job).errorCode("0001")
                    .errorMessage("You have Not confirmed the details")
                    .variables(variables)
                    .send();
        }

        return variables;
    }
}
