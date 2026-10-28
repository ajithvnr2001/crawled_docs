---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-datatransferservice-transferrun-delete/
title: Delete a transfer run \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:01:51.426536+00:00
---

# Delete a transfer run  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-datatransferservice-transferrun-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Delete a transfer run Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a transfer run in the BigQuery Data Transfer Service.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html);
    import com.google.cloud.bigquery.datatransfer.v1.[RunName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.RunName.html);
    import java.io.IOException;
    
    public class DeleteTransferRun {
    
      /**
       * Deletes a transfer run.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the transfer run (for example, "us-central1").
       * @param transferConfigId The transfer configuration ID (for example,
       *     "1234a-5678-90b1-2c3d-4e5f67890g12").
       * @param runId The transfer run ID (for example, "6789b-0123-45c6-7d8e-9f0a12345b67").
       */
      public static void deleteTransferRun(
          String projectId, String location, String transferConfigId, String runId) {
        [RunName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.RunName.html) runName =
            [RunName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.RunName.html).[ofProjectLocationTransferConfigRunName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.RunName.html#com_google_cloud_bigquery_datatransfer_v1_RunName_ofProjectLocationTransferConfigRunName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                projectId, location, transferConfigId, runId);
    
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) client = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          client.deleteTransferRun(runName);
          System.out.printf("Deleted transfer run %s%n", runName);
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf("error: transfer run '%s' not found: %s%n", runName, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to delete transfer run '%s': %s%n", runName, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {
      DataTransferServiceClient,
    } = require('[@google-cloud/bigquery-data-transfer](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)');
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)();
    
    /**
     * Deletes a transfer run.
     * This action removes a specific execution instance of a transfer configuration.
     *
     * @param {string} projectId The Google Cloud project ID (for example, 'example-project-id').
     * @param {string} location The location of the transfer config (for example, 'us-central1').
     * @param {string} transferConfigId The ID of the transfer configuration (for example, '1234a123-123a-123a-123a-123456789abc').
     * @param {string} runId The ID of the transfer run (for example, '9876b987-987b-987b-987b-987654321cba').
     */
    async function deleteTransferRun(
      projectId,
      location = 'us-central1',
      transferConfigId = '1234a123-123a-123a-123a-123456789abc',
      runId = '9876b987-987b-987b-987b-987654321cba',
    ) {
      const name = client.[projectLocationTransferConfigRunPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/v1.datatransferserviceclient.html)(
        projectId,
        location,
        transferConfigId,
        runId,
      );
      const request = {
        name,
      };
    
      try {
        await client.deleteTransferRun(request);
        console.log(`Deleted transfer run ${name}.`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(`Transfer run ${name} not found.`);
        } else {
          console.error('Error deleting transfer run:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest)
    
    client = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    
    def delete_transfer_run(
        project_id: str,
        location: str,
        transfer_config_id: str,
        run_id: str,
    ) -> None:
        """Deletes a transfer run.
    
        A transfer run is a single execution of a data transfer configuration.
        This action is useful for cleaning up failed or unnecessary transfer
        executions.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the transfer run.
            transfer_config_id: The transfer configuration ID.
            run_id: The transfer run ID.
        """
        run_name = client.[run_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_run_path)(
            project=f"{project_id}/locations/{location}",
            transfer_config=transfer_config_id,
            run=run_id,
        )
    
        try:
            client.[delete_transfer_run](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_delete_transfer_run)(name=run_name)
            print(f"Deleted transfer run {run_name}")
        except google.api_core.exceptions.NotFound:
            print(f"Error: Transfer run '{run_name}' not found.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
