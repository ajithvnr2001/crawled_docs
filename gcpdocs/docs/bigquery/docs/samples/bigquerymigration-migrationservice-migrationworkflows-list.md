---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerymigration-migrationservice-migrationworkflows-list/
title: List migration workflows \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:46:19.413018+00:00
---

# List migration workflows  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerymigration-migrationservice-migrationworkflows-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  List migration workflows Stay organized with collections  Save and categorize content based on your preferences. 

Lists all migration workflows for the BigQuery Migration API in a specified project.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.migration.v2.[ListMigrationWorkflowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.ListMigrationWorkflowsRequest.html);
    import com.google.cloud.bigquery.migration.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.LocationName.html);
    import com.google.cloud.bigquery.migration.v2.[MigrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationServiceClient.html);
    import com.google.cloud.bigquery.migration.v2.[MigrationWorkflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.html);
    import java.io.IOException;
    
    public class ListMigrationWorkflows {
    
      /**
       * Lists migration workflows in a given project and location.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the migration workflows (for example, "us").
       */
      public static void listMigrationWorkflows(String projectId, String location) {
        [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.LocationName.html).of(projectId, location);
    
        [ListMigrationWorkflowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.ListMigrationWorkflowsRequest.html) request =
            [ListMigrationWorkflowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.ListMigrationWorkflowsRequest.html).newBuilder().setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.LocationName.html#com_google_cloud_bigquery_migration_v2_LocationName_toString__)()).build();
    
        try ([MigrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationServiceClient.html) client = [MigrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationServiceClient.html).create()) {
          System.out.printf("Workflows in parent '%s':%n", parent);
          int count = 0;
          for ([MigrationWorkflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationWorkflow.html) workflow : client.listMigrationWorkflows(request).iterateAll()) {
            System.out.printf("  %s%n", workflow.getName());
            System.out.printf("    Display Name: %s%n", workflow.getDisplayName());
            System.out.printf("    State: %s%n", workflow.getState());
            count++;
          }
    
          if (count == 0) {
            System.out.println("No migration workflows found.");
          }
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.out.printf("The parent resource '%s' was not found.%n", parent);
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to list migration workflows in '%s': %s%n", parent, err.getMessage());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
    /**
     * Lists all migration workflows in a project.
     *
     * This is useful to get an overview of all migration workflows in a project and location.
     *
     * @param {string} projectId The Google Cloud project ID (for example, 'example-project-id')
     * @param {string} location The Google Cloud location (for example, 'us')
     */
    async function listMigrationWorkflows(projectId, location = 'us') {
      const request = {
        parent: client.locationPath(projectId, location),
      };
    
      try {
        const [workflows] = await client.listMigrationWorkflows(request);
    
        if (workflows.length === 0) {
          console.error(
            `No workflows found in project ${projectId} at location ${location}.`,
          );
          return;
        }
    
        console.log('Workflows:');
        for (const workflow of workflows) {
          console.log(`  ${workflow.name}`);
          console.log(`    Display Name: ${workflow.displayName}`);
          console.log(`    State: ${workflow.state}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(`Project ${projectId} or location ${location} not found.`);
        } else {
          console.error('Error listing migration workflows:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest)
    
    client = [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest).[MigrationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.services.migration_service.MigrationServiceClient.html)()
    
    
    def list_migration_workflows(project_id: str, location: str) -> None:
        """Lists migration workflows in a given project and location.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The location of the migration workflows, for example, "us".
        """
    
        parent = f"projects/{project_id}/locations/{location}"
    
        try:
            workflow_pager = client.[list_migration_workflows](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.services.migration_service.MigrationServiceClient.html#google_cloud_bigquery_migration_v2_services_migration_service_MigrationServiceClient_list_migration_workflows)(parent=parent)
    
            print(f"Workflows in parent '{parent}':")
            count = 0
            for workflow in workflow_pager:
                print(f"- {workflow.name}")
                count += 1
    
            if not count:
                print("No migration workflows found.")
    
        except exceptions.NotFound:
            print(f"The parent resource '{parent}' was not found.")
            print("Please check that the project ID and location are correct.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
