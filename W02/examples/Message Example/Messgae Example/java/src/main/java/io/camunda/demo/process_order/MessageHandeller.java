package io.camunda.demo.process_order;

import io.camunda.client.CamundaClient;
import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.client.api.worker.JobClient;
import org.springframework.stereotype.Component;

import java.time.Duration;
import java.util.Map;

@Component
public class MessageHandeller {
    //Camunda Client (this is for message passing) - Step 01
    private final CamundaClient camundaClient;

    // Initialise the Camunda Client through the constructor - Step 02
    public MessageHandeller(CamundaClient camundaClient) {
        this.camundaClient = camundaClient;
    }

    /*Add the Job Worker
        * Step 03
        * Type should be same as the Message -> Task Definition -> Job Type
        * autoComplete = false

     */
    @JobWorker(type = "send-message-01", autoComplete = false)
    public void sendMessage01(final JobClient jobClient, final ActivatedJob job){
        try
        {
            //Get Process Variables - Step 03
            Map<String,Object> variables = job.getVariablesAsMap();

            /*
                *Step 03 (A)
                * Add this is you have not initialised the Message Subscription correlation key
                * Message -> Subscription correlation key

             */
            /*variables.put(
                    "appoinment_confirmation",
                    "appoinment_confirmation"
            );*/

            /*
                * Step 04
                * Publish the BPMN message using CamundaClient.
                * messageName => this is the "Name" of the message where you are expecting to send the message
                * correlationKey => this is the "Subscription correlation key" of the message where you are expecting to send the message
             */

            camundaClient.newPublishMessageCommand()
                    .messageName("Message01")
                    .correlationKey("Message01")
                    .variables(variables)
                    .timeToLive(Duration.ofMinutes(10))
                    .send()
                    .join();
            /*
                * Step 05
                * This completes the intermediate event/message sent task
             */
            camundaClient.newCompleteCommand(job.getKey())
                    .variables(variables)
                    .send()
                    .join();


        }catch(Exception e){
            e.printStackTrace();
            jobClient
                    .newFailCommand(job)
                    .retries(Math.max(job.getRetries() - 1, 0))
                    .errorMessage("Could not publish message: " + e.getMessage())
                    .send()
                    .join();
        }

    }

    @JobWorker(type = "send-message-02", autoComplete = false)
    public void sendMessage02(final JobClient jobClient, final ActivatedJob job){
        try
        {
            //Get Process Variables
            Map<String,Object> variables = job.getVariablesAsMap();
            variables.put("details","content");

            /*
             *Add this is you have not initialised the Message Subscription correlation key
             * Message -> Subscription correlation key

             */
            /*variables.put(
                    "appoinment_confirmation",
                    "appoinment_confirmation"
            );*/

            /*
             * Publish the BPMN message using CamundaClient.
             * messageName => this is the "Name" of the message where you are expecting to send the message
             * correlationKey => this is the "Subscription correlation key" of the message where you are expecting to send the message
             */

            camundaClient.newPublishMessageCommand()
                    .messageName("Message02")
                    .correlationKey("Message02")
                    .variables(variables)
                    .timeToLive(Duration.ofMinutes(10))
                    .send()
                    .join();
            /*
             * This completes the intermediate event/message sent task
             */
            camundaClient.newCompleteCommand(job.getKey())
                    .variables(variables)
                    .send()
                    .join();


        }catch(Exception e){
            e.printStackTrace();
            jobClient
                    .newFailCommand(job)
                    .retries(Math.max(job.getRetries() - 1, 0))
                    .errorMessage("Could not publish message: " + e.getMessage())
                    .send()
                    .join();
        }

    }

    @JobWorker(type = "send-error-message", autoComplete = false)
    public void sendErrorMessage(final JobClient jobClient, final ActivatedJob job){
        try
        {
            //Get Process Variables
            Map<String,Object> variables = job.getVariablesAsMap();
            variables.put("details","error");

            /*
             *Add this is you have not initialised the Message Subscription correlation key
             * Message -> Subscription correlation key

             */
            /*variables.put(
                    "appoinment_confirmation",
                    "appoinment_confirmation"
            );*/

            /*
             * Publish the BPMN message using CamundaClient.
             * messageName => this is the "Name" of the message where you are expecting to send the message
             * correlationKey => this is the "Subscription correlation key" of the message where you are expecting to send the message
             */

            camundaClient.newPublishMessageCommand()
                    .messageName("Message02")
                    .correlationKey("Message02")
                    .variables(variables)
                    .timeToLive(Duration.ofMinutes(10))
                    .send()
                    .join();
            /*
             * This completes the intermediate event/message sent task
             */
            camundaClient.newCompleteCommand(job.getKey())
                    .variables(variables)
                    .send()
                    .join();


        }catch(Exception e){
            e.printStackTrace();
            jobClient
                    .newFailCommand(job)
                    .retries(Math.max(job.getRetries() - 1, 0))
                    .errorMessage("Could not publish message: " + e.getMessage())
                    .send()
                    .join();
        }

    }


}
