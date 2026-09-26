package io.camunda.demo.process_order;

import io.camunda.client.CamundaClient;
import io.camunda.client.annotation.JobWorker;
import io.camunda.client.api.response.ActivatedJob;
import io.camunda.client.api.worker.JobClient;
import org.springframework.stereotype.Component;

import java.time.Duration;
import java.util.HashMap;
import java.util.Map;

@Component
public class MessageHandeler {

    //Camunda Client (this is for message passing
    private final CamundaClient camundaClient;

    public MessageHandeler(CamundaClient camundaClient) {
        this.camundaClient = camundaClient;
    }

    @JobWorker(type = "send-appoinemt-request", autoComplete = false)
    public void sendAppointmentRequestToClinic(final JobClient jobClient, final ActivatedJob job){
        try
        {
            //Get Process Variables
            Map<String,Object> variables = job.getVariablesAsMap();
            variables.put(
                    "appoinment_confirmation",
                    "appoinment_confirmation"
            );
            /*
             * Publish the BPMN message using CamundaClient.
             */

            camundaClient.newPublishMessageCommand()
                    .messageName("new_appointment_request")
                    .correlationKey("new_appointment_request")
                    .variables(variables)
                    .timeToLive(Duration.ofMinutes(10))
                    .send()
                    .join();
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

    @JobWorker(type = "send-appointment-confirmation", autoComplete = false)
    public void sendAppointmentConfirmationToPatient(final JobClient jobClient, final ActivatedJob job){
        try
        {
            //Get Process Variables
            Map<String,Object> variables = job.getVariablesAsMap();
            //add the message corelation key
            variables.put("payment_confirmation","payment_confirmation");
            variables.put("appointment_cancel_request","appointment_cancel_request");
            /*
             * Publish the BPMN message using CamundaClient.
             */

            camundaClient.newPublishMessageCommand()
                    .messageName("appoinment_confirmation")
                    .correlationKey("appoinment_confirmation")
                    .variables(variables)
                    .timeToLive(Duration.ofMinutes(10))
                    .send()
                    .join();
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

    @JobWorker(type = "payment-error", autoComplete = false)
    public void sendPaymentError(final JobClient jobClient, final ActivatedJob job){
        try
        {
            //Get Process Variables
            Map<String,Object> variables = job.getVariablesAsMap();
            //add the message corelation key
            variables.put("payment_confirmation","payment_confirmation");
            variables.put("appointment_cancel_request","appointment_cancel_request");
            /*
             * Publish the BPMN message using CamundaClient.
             */

            camundaClient.newPublishMessageCommand()
                    .messageName("appoinment_confirmation")
                    .correlationKey("appoinment_confirmation")
                    .variables(variables)
                    .timeToLive(Duration.ofMinutes(10))
                    .send()
                    .join();
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

    @JobWorker(type = "send-payment-stastus", autoComplete = false)
    public void sendPaymentStatus(final JobClient jobClient, final ActivatedJob job){
        try
        {
            //Get Process Variables
            Map<String,Object> variables = job.getVariablesAsMap();
            //add the message corelation key
            variables.put("payment_confirmation","payment_confirmation");
            variables.put("appointment_cancel_request","appointment_cancel_request");
            variables.put("pament_status","ok");
            /*
             * Publish the BPMN message using CamundaClient.
             */

            camundaClient.newPublishMessageCommand()
                    .messageName("payment_confirmation")
                    .correlationKey("payment_confirmation")
                    .variables(variables)
                    .timeToLive(Duration.ofMinutes(10))
                    .send()
                    .join();
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

    @JobWorker(type = "send-cancel-appoinment-notice")
    public void sendCancelAppointmentNotice(final JobClient jobClient, final ActivatedJob job){
        try
        {
            //Get Process Variables
            Map<String,Object> variables = job.getVariablesAsMap();

            camundaClient.newPublishMessageCommand()
                    .messageName("appointment_cancel_request")
                    .correlationKey("appointment_cancel_request")
                    .variables(variables)
                    .timeToLive(Duration.ofMinutes(10))
                    .send()
                    .join();
            camundaClient.newCompleteCommand(job.getKey())
                    .variables(variables)
                    .send()
                    .join();

        }catch (Exception e){
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
