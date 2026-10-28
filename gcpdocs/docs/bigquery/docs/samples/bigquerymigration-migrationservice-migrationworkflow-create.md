---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerymigration-migrationservice-migrationworkflow-create/
title: Create a migration workflow \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:01:39.265599+00:00
---

# Create a migration workflow  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerymigration-migrationservice-migrationworkflow-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a migration workflow Stay organized with collections  Save and categorize content based on your preferences. 

Creates a migration workflow in the BigQuery Migration API. A migration workflow contains a list of subtasks that are executed to migrate a data warehouse to BigQuery.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html);
    import com.google.cloud.bigquery.migration.v2.[BigQueryDialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.BigQueryDialect.html);
    import com.google.cloud.bigquery.migration.v2.[CreateMigrationWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.CreateMigrationWorkflowRequest.html);
    import com.google.cloud.bigquery.migration.v2.[Dialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.Dialect.html);
    import com.google.cloud.bigquery.migration.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.LocationName.html);
    import com.google.cloud.bigquery.migration.v2.[MigrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationServiceClient.html);
    import com.google.cloud.bigquery.migration.v2.[MigrationTask](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationTask.html);
    import com.google.cloud.bigquery.migration.v2.[MigrationWorkflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.html);
    import com.google.cloud.bigquery.migration.v2.[TeradataDialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TeradataDialect.html);
    import com.google.cloud.bigquery.migration.v2.[TranslationConfigDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TranslationConfigDetails.html);
    import java.io.IOException;
    import java.util.Map;
    
    public class CreateMigrationWorkflow {
    
      /**
       * Creates a Teradata SQL translation migration workflow to batch translate Teradata SQL scripts
       * and DDL into BigQuery-compatible SQL. The translation task reads input files from a Cloud
       * Storage source path and writes the converted output to a Cloud Storage target path.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the migration workflow (for example, "us").
       * @param gcsSourcePath The Cloud Storage path for a directory of files to translate in a batch
       *     (for example, "gs://example-bucket/example-input-folder/").
       * @param gcsTargetPath The Cloud Storage path to write back the translated output files to (for
       *     example, "gs://example-bucket/example-output-folder/").
       */
      public static void createMigrationWorkflow(
          String projectId, String location, String gcsSourcePath, String gcsTargetPath) {
        [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.LocationName.html).of(projectId, location);
    
        [Dialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.Dialect.html) sourceDialect =
            [Dialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.Dialect.html).newBuilder()
                .[setTeradataDialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.Dialect.Builder.html#com_google_cloud_bigquery_migration_v2_Dialect_Builder_setTeradataDialect_com_google_cloud_bigquery_migration_v2_TeradataDialect_)(
                    [TeradataDialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TeradataDialect.html).newBuilder().[setMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TeradataDialect.Builder.html#com_google_cloud_bigquery_migration_v2_TeradataDialect_Builder_setMode_com_google_cloud_bigquery_migration_v2_TeradataDialect_Mode_)([TeradataDialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TeradataDialect.html).Mode.SQL).build())
                .build();
    
        [Dialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.Dialect.html) targetDialect =
            [Dialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.Dialect.html).newBuilder().[setBigqueryDialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.Dialect.Builder.html#com_google_cloud_bigquery_migration_v2_Dialect_Builder_setBigqueryDialect_com_google_cloud_bigquery_migration_v2_BigQueryDialect_)([BigQueryDialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.BigQueryDialect.html).getDefaultInstance()).build();
    
        [TranslationConfigDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TranslationConfigDetails.html) translationConfigDetails =
            [TranslationConfigDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TranslationConfigDetails.html).newBuilder()
                .[setGcsSourcePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TranslationConfigDetails.Builder.html#com_google_cloud_bigquery_migration_v2_TranslationConfigDetails_Builder_setGcsSourcePath_java_lang_String_)(gcsSourcePath)
                .[setGcsTargetPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TranslationConfigDetails.Builder.html#com_google_cloud_bigquery_migration_v2_TranslationConfigDetails_Builder_setGcsTargetPath_java_lang_String_)(gcsTargetPath)
                .[setSourceDialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TranslationConfigDetails.Builder.html#com_google_cloud_bigquery_migration_v2_TranslationConfigDetails_Builder_setSourceDialect_com_google_cloud_bigquery_migration_v2_Dialect_)(sourceDialect)
                .[setTargetDialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TranslationConfigDetails.Builder.html#com_google_cloud_bigquery_migration_v2_TranslationConfigDetails_Builder_setTargetDialect_com_google_cloud_bigquery_migration_v2_Dialect_)(targetDialect)
                .build();
    
        [MigrationTask](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationTask.html) task =
            [MigrationTask](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationTask.html).newBuilder()
                .setType("Translation_Teradata2BQ")
                .[setTranslationConfigDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationTask.Builder.html#com_google_cloud_bigquery_migration_v2_MigrationTask_Builder_setTranslationConfigDetails_com_google_cloud_bigquery_migration_v2_TranslationConfigDetails_)(translationConfigDetails)
                .build();
    
        [MigrationWorkflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.html) migrationWorkflow =
            [MigrationWorkflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.html).newBuilder()
                .[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.Builder.html#com_google_cloud_bigquery_migration_v2_MigrationWorkflow_Builder_setDisplayName_java_lang_String_)("Example Teradata to BigQuery Migration Workflow")
                .[putTasks](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.Builder.html#com_google_cloud_bigquery_migration_v2_MigrationWorkflow_Builder_putTasks_java_lang_String_com_google_cloud_bigquery_migration_v2_MigrationTask_)("translation-task", task)
                .build();
    
        [CreateMigrationWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.CreateMigrationWorkflowRequest.html) request =
            [CreateMigrationWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.CreateMigrationWorkflowRequest.html).newBuilder()
                .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.LocationName.html#com_google_cloud_bigquery_migration_v2_LocationName_toString__)())
                .[setMigrationWorkflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.CreateMigrationWorkflowRequest.Builder.html#com_google_cloud_bigquery_migration_v2_CreateMigrationWorkflowRequest_Builder_setMigrationWorkflow_com_google_cloud_bigquery_migration_v2_MigrationWorkflow_)(migrationWorkflow)
                .build();
    
        try ([MigrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationServiceClient.html) client = [MigrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationServiceClient.html).create()) {
          [MigrationWorkflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.html) response = client.createMigrationWorkflow(request);
          System.out.printf("Created migration workflow: %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.html#com_google_cloud_bigquery_migration_v2_MigrationWorkflow_getName__)());
          System.out.printf("  Display Name: %s%n", response.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.html#com_google_cloud_bigquery_migration_v2_MigrationWorkflow_getDisplayName__)());
          System.out.printf("  State: %s%n", response.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.html#com_google_cloud_bigquery_migration_v2_MigrationWorkflow_getState__)());
          System.out.println("  Tasks:");
          for (Map.Entry<String, MigrationTask> entry : response.getTasksMap().entrySet()) {
            MigrationTask createdTask = entry.getValue();
            System.out.printf("    - %s:%n", entry.getKey());
            System.out.printf("        Type: %s%n", createdTask.getType());
            System.out.printf("        State: %s%n", createdTask.getState());
          }
        } catch (AlreadyExistsException err) {
          System.err.printf(
              "error: migration workflow already exists in location '%s' for project '%s': %s%n",
              location, projectId, err.getMessage());
        } catch (InvalidArgumentException err) {
          System.err.printf(
              "error: invalid argument creating migration workflow in location '%s' for project '%s': %s%n",
              location, projectId, err.getMessage());
        } catch (ApiException | IOException err) {
          System.err.printf(
              "error: failed to create migration workflow in location '%s' for project '%s': %s%n",
              location, projectId, err.getMessage());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
    /**
     * Creates a migration workflow.
     *
     * Batch translate Teradata SQL scripts and DDL into BigQuery-compatible SQL.
     * It configures a translation task that reads input files from a
     * Google Cloud Storage source bucket and writes the converted output to a target bucket.
     *
     * @param {string} projectId The Google Cloud project ID (for example, 'example-project-id').
     * @param {string} location The Google Cloud location (for example, 'us').
     * @param {string} gcsSourcePath The Cloud Storage path for the source data (for example, 'gs://example-bucket/example-input-folder').
     * @param {string} gcsTargetPath The Cloud Storage path for the translated results (for example, 'gs://example-bucket/example-output-folder').
     */
    async function createMigrationWorkflow(
      projectId,
      location,
      gcsSourcePath,
      gcsTargetPath,
    ) {
      const parent = client.locationPath(projectId, location);
      const migrationWorkflow = {
        displayName: 'Example BTEQ Migration Workflow',
        tasks: {
          'translation-task': {
            type: 'Translation_Teradata2BQ',
            translationConfigDetails: {
              gcsSourcePath,
              gcsTargetPath,
              sourceDialect: {
                teradataDialect: {
                  mode: '[SQL](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2.teradatadialect.mode.html)',
                },
              },
              targetDialect: {
                bigqueryDialect: {},
              },
            },
          },
        },
      };
    
      const request = {
        parent,
        migrationWorkflow,
      };
    
      try {
        const [workflow] = await client.createMigrationWorkflow(request);
        console.log(`Created migration workflow: ${workflow.name}`);
        console.log(`  Display Name: ${workflow.displayName}`);
        console.log(`  State: ${workflow.state}`);
        console.log('  Tasks:');
        for (const taskName in workflow.tasks) {
          const task = workflow.tasks[taskName];
          console.log(`    - ${taskName}:`);
          console.log(`        Type: ${task.type}`);
          console.log(`        State: ${task.state}`);
        }
      } catch (err) {
        if (err.code === status.INVALID_ARGUMENT) {
          console.error(
            `Error: Invalid argument provided for creating Migration '${migrationWorkflow.displayName}'. ` +
              `Details: ${err.message}. Please check the request parameters and ensure they are valid.`,
          );
        } else {
          console.error('Error creating migration workflow:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest)
    from google.cloud.bigquery_migration_v2.types import (
        migration_entities,
        translation_config,
    )
    
    
    def create_migration_workflow(
        project_id: str, location: str, gcs_source_path: str, gcs_target_path: str
    ) -> None:
        """Creates a Teradata SQL translation workflow
    
        Creates a migration workflow to batch translate Teradata SQL scripts
        and DDL into BigQuery-compatible SQL. It configures a translation task
        that reads input files from a Google Cloud Storage source bucket and
        writes the converted output to a target bucket.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the migration workflow (for example, us).
            gcs_source_path: The Cloud Storage path for a directory of files to
                translate in a batch (for example, gs://example-bucket/example-input-folder/).
            gcs_target_path: The Cloud Storage path to write back the corresponding
                input files to (for example, gs://example-bucket/example-output-folder/).
        """
        client = [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest).[MigrationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.services.migration_service.MigrationServiceClient.html)()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        source_dialect = [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest).[Dialect](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.Dialect.html)()
        source_dialect.teradata_dialect = [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest).[TeradataDialect](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.TeradataDialect.html)(
            mode=[bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest).[TeradataDialect](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.TeradataDialect.html).[Mode](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.TeradataDialect.Mode.html).SQL
        )
        target_dialect = [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest).[Dialect](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.Dialect.html)()
        target_dialect.bigquery_dialect = [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest).[BigQueryDialect](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.BigQueryDialect.html)()
    
        translation_config_details = [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest).[TranslationConfigDetails](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.TranslationConfigDetails.html)(
            gcs_source_path=gcs_source_path,
            gcs_target_path=gcs_target_path,
            source_dialect=source_dialect,
            target_dialect=target_dialect,
        )
    
        task = migration_entities.[MigrationTask](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.MigrationTask.html)(
            type="Translation_Teradata2BQ",
            translation_config_details=translation_config_details,
        )
    
        workflow = migration_entities.[MigrationWorkflow](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.MigrationWorkflow.html)(
            display_name="Example Teradata to BigQuery Migration Workflow",
            tasks={"translation-task": task},
        )
    
        try:
            response = client.[create_migration_workflow](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.services.migration_service.MigrationServiceClient.html#google_cloud_bigquery_migration_v2_services_migration_service_MigrationServiceClient_create_migration_workflow)(
                parent=parent,
                migration_workflow=workflow,
            )
            print(f"Created migration workflow: {response.name}")
            print(f"Display name: {response.display_name}")
            print(f"State: {response.state.name}")
        except exceptions.AlreadyExists as e:
            print(f"Migration workflow already exists: {e}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
