---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-create-teradata-transfer/
title: Load data from Teradata \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T10:42:02.746725+00:00
---

# Load data from Teradata  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-create-teradata-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Load data from Teradata Stay organized with collections  Save and categorize content based on your preferences. 

Schedule recurring load jobs from Teradata into BigQuery.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Migrate schema and data from Teradata](https://docs.cloud.google.com/bigquery/docs/migration/teradata)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.bigquery.datatransfer.v1.[CreateTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html);
    import com.google.cloud.bigquery.datatransfer.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html);
    import com.google.cloud.bigquery.datatransfer.v1.[TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html);
    import com.google.protobuf.[Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    // Sample to create a teradata transfer config.
    public class CreateTeradataTransfer {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        final String projectId = "MY_PROJECT_ID";
        String datasetId = "MY_DATASET_ID";
        String databaseType = "Teradata";
        String bucket = "cloud-sample-data";
        String databaseName = "MY_DATABASE_NAME";
        String tableNamePatterns = "*";
        String serviceAccount = "MY_SERVICE_A<CCOUNT";>
        String schemaFil<>ePath = "/your-schema-path"[;](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
        MapString, Value params = new HashMap();
        params.put("database_type&[quot;](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html), Value.newBuilder().setStringValue(databaseType).build());
        params.put(&quo[t;buc](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)ket", Value.newBuilder().setStringValue(bucket).build());
        params.put("databas[e_nam](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)e", Value.newBuilder().setStringValue(databaseName).build());
        params.put("table_name[_patt](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)erns", Value.newBuilder().setStringValue(tableNamePatterns).build());
        params.put(["](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);agent_service_account", Value.newBuilder().setStringV[alue](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html)(serviceAccount).build());
        param[s](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html).put("schema_file_path", Value.newBuilder().setStringValue(schemaFilePath).build());
        TransferConfig transferConfig =
            TransferConfig.newBuilder()
                .setDestinationDatas[etId](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)(datasetId)
        [        ](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.Builder.html#com_google_protobuf_Struct_Builder_putAllFields_java_util_Map_java_lang_String_com_google_protobuf_Value__).setDisplayName("Your Teradata Config Name")
                .setDataSourceId("on_premises")
                .setParams(Struct.newBuilder().putAllFields(params).build())
                .setSchedule(&q[uot;every 24 h](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html)ours")
                .build();
        createTeradataT[ransfer](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html)(projectId, transferConfig);[
      }
    
      public static voi](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html)d createTeradataTra[nsfer](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html)(String projectI[d](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html), TransferConfig transferConfig)[
          throws IOException {](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html)
        try (DataTransfe[rServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html) client = DataTransferServiceClient.create()) {
          Proje[ctName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html#com_google_cloud_bigquery_datatransfer_v1_ProjectName_toString__) parent = ProjectName.of(projectId);
          CreateTransferConfigRequest request =
        [      ](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html)CreateTransferConfigRequest.newBuilder()
                  .setParent(parent.toString())
                  .setTransferConfig(transferConfig)
         [       ](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html#com_google_cloud_bigquery_datatransfer_v1_TransferConfig_getName__)  .build();
          [TransferConf](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html)ig config = client.createTransferConfig(request);
          System.out.println("Cloud teradata transfer created successfully :" + config.getName());
        } catch (ApiException ex) {
          System.out.print("Cloud teradata transfer was not created." + ex.toString());
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
