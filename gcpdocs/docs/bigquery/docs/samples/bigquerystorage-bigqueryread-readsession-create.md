---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-bigqueryread-readsession-create/
title: Create a BigQuery read session \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:08:34.212491+00:00
---

# Create a BigQuery read session  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-bigqueryread-readsession-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a BigQuery read session Stay organized with collections  Save and categorize content based on your preferences. 

Create a new read session to specify the BigQuery table to read from, the columns to project, and an optional row filter.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.storage.v1.[BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient.html);
    import com.google.cloud.bigquery.storage.v1.[CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.html);
    import com.google.cloud.bigquery.storage.v1.[DataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.DataFormat.html);
    import com.google.cloud.bigquery.storage.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ProjectName.html);
    import com.google.cloud.bigquery.storage.v1.[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html);
    import com.google.cloud.bigquery.storage.v1.[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).[TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.html);
    import com.google.cloud.bigquery.storage.v1.[TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html);
    import java.io.IOException;
    
    public class CreateReadSession {
    
      /**
       * Creates a BigQuery Storage read session for a specified table, projecting selected columns and
       * applying an optional row filter.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param datasetId The BigQuery dataset ID containing the table (for example,
       *     "example_dataset").
       * @param tableId The BigQuery table ID to read from (for example, "example_table").
       */
      public static void createReadSession(String projectId, String datasetId, String tableId) {
        [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ProjectName.html) parent = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ProjectName.html).of(projectId);
        [TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html) table = [TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html).of(projectId, datasetId, tableId);
    
        // If no fields are specified, all fields will be returned.
        [TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.html) readOptions =
            [TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.html).newBuilder()
                .[addSelectedFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_addSelectedFields_java_lang_String_)("field_01")
                .[addSelectedFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_addSelectedFields_java_lang_String_)("field_02")
                .[setRowRestriction](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_setRowRestriction_java_lang_String_)("field_03 > 100")
                .build();
    
        [ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html) readSession =
            [ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).newBuilder()
                .setTable(table.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html#com_google_cloud_bigquery_storage_v1_TableName_toString__)())
                .[setDataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_Builder_setDataFormat_com_google_cloud_bigquery_storage_v1_DataFormat_)([DataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.DataFormat.html).ARROW)
                .[setReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_Builder_setReadOptions_com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_)(readOptions)
                .build();
    
        [CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.html) request =
            [CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.html).newBuilder()
                .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ProjectName.html#com_google_cloud_bigquery_storage_v1_ProjectName_toString__)())
                .[setReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.Builder.html#com_google_cloud_bigquery_storage_v1_CreateReadSessionRequest_Builder_setReadSession_com_google_cloud_bigquery_storage_v1_ReadSession_)(readSession)
                .[setMaxStreamCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.Builder.html#com_google_cloud_bigquery_storage_v1_CreateReadSessionRequest_Builder_setMaxStreamCount_int_)(1)
                .build();
    
        try ([BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient.html) client = [BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient.html).create()) {
          [ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html) session = client.createReadSession(request);
          System.out.printf("Successfully created read session: %s%n", session.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html#com_google_cloud_bigquery_storage_v1_ReadSession_getName__)());
          if (session.[getStreamsCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html#com_google_cloud_bigquery_storage_v1_ReadSession_getStreamsCount__)() > 0) {
            System.out.printf("Stream found: %s%n", session.[getStreams](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html#com_google_cloud_bigquery_storage_v1_ReadSession_getStreams_int_)(0).getName());
          } else {
            System.out.println("No streams found in the session.");
          }
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf(
              "error: table '%s' not found: %s%n", table, err.getMessage());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to create read session for table '%s': %s%n", table, err.getMessage());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {BigQueryReadClient} = require('[@google-cloud/bigquery-storage](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/overview.html)');
    const {status} = require('@grpc/grpc-js');
    
    const client = new [BigQueryReadClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)();
    
    /**
     * Creates a read session for a BigQuery table.
     *
     * @param {string} projectId The project ID to use for billing and quota (e.g., 'my-project-id').
     * @param {string} datasetId The ID of the dataset to read from (e.g., 'my_dataset').
     * @param {string} tableId The ID of the table to read from (e.g., 'my_table').
     */
    async function createReadSession(
      projectId, datasetId, tableId
    ) {
      const parent = `projects/${projectId}`;
      const table = `projects/${projectId}/datasets/${datasetId}/tables/${tableId}`;
    
      const readOptions = {
        selectedFields: ['field_01', 'field_02'],
        rowRestriction: 'field_03 > 100',
      };
    
      const request = {
        parent,
        readSession: {
          table,
          dataFormat: '[AVRO](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.dataformat.html)',
          readOptions,
        },
        maxStreamCount: 1,
      };
    
      try {
        const [session] = await client.createReadSession(request);
    
        console.log(`Read session created: ${session.name}`);
        console.log('Session details:');
        console.log(`  Table: ${session.table}`);
        console.log(`  Data format: ${session.dataFormat}`);
        console.log(`  Estimated row count: ${session.estimatedRowCount}`);
    
        if (session.streams.length > 0) {
          const streamName = session.streams[0].name;
          console.log(`  First stream: ${streamName}`);
        } else {
          console.log('  No streams found in the session.');
        }
    
        if (session.avroSchema && session.avroSchema.schema) {
          console.log('  AVRO schema:');
          console.log(`  ${session.avroSchema.schema}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(
            `Could not find table ${table}. Please ensure the table exists and you have permission to read it.`,
          );
        } else {
          console.error('Error creating read session:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.bigquery_storage_v1 import BigQueryReadClient
    from google.cloud.bigquery_storage_v1.types import [DataFormat](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.DataFormat.html), [ReadSession](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.ReadSession.html)
    
    client = BigQueryReadClient()
    
    
    def create_read_session(
        project_id: str,
        dataset_id: str,
        table_id: str,
    ) -> None:
        """Creates a read session for a BigQuery table.
    
        Args:
            project_id: The project ID that will be billed for the read session.
            dataset_id: The dataset ID of the table to read from.
            table_id: The table ID of the table to read from.
        """
    
        parent = f"projects/{project_id}"
        table = [client](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.client.html).[table_path](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.services.big_query_read.BigQueryReadClient.html#google_cloud_bigquery_storage_v1_services_big_query_read_BigQueryReadClient_table_path)(project_id, dataset_id, table_id)
    
        # If no fields are specified, all fields will be returned.
        read_options = [ReadSession](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.ReadSession.html).[TableReadOptions](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.ReadSession.TableReadOptions.html)(
            selected_fields=["field_01", "field_02"], row_restriction="field_03 > 100"
        )
    
        read_session = ReadSession(
            table=table,
            data_format=[DataFormat](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.DataFormat.html).ARROW,
            read_options=read_options,
        )
    
        try:
            session = [client](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.client.html).[create_read_session](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.services.big_query_read.BigQueryReadClient.html#google_cloud_bigquery_storage_v1_services_big_query_read_BigQueryReadClient_create_read_session)(
                parent=parent,
                read_session=read_session,
                max_stream_count=1,
            )
    
            print(f"Successfully created read session: {session.name}")
            if session.streams:
                print(f"Stream found: {session.streams[0].name}")
            else:
                print("No streams found in the session.")
    
        except NotFound:
            print(
                f"Could not find the table '{table}'. Please check that the table exists."
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
