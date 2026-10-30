---
url: https://docs.cloud.google.com/knowledge-catalog/docs/databricks-unity-transfer/
title: Import metadata from Databricks Unity Catalog \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:39:13.447452+00:00
---

# Import metadata from Databricks Unity Catalog  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/databricks-unity-transfer/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Import metadata from Databricks Unity Catalog Stay organized with collections  Save and categorize content based on your preferences. 

Break down data silos and avoid switching between tools by using a Knowledge Catalog (formerly Dataplex Universal Catalog) connector to import metadata from Databricks Unity Catalog directly into Google Cloud.

This connector supports Databricks Unity Catalog instances hosted on Google Cloud, Microsoft Azure, or Amazon Web Services (AWS).

The following table lists the metadata that the Databricks Unity Catalog connector captures:

Category | Metadata captured  
---|---  
Technical | 

  * Metastore
  * Catalog
  * Schema
  * Table (managed Delta, external, streaming, online, feature, Apache Iceberg REST Catalog (IRC))
  * View (standard, materialized)
  * Volumes
  * Functions and procedures

  
Operational | 

  * Usage metrics (views over 30 and 90 days; reads, writes, frequent users, and frequently joined tables over 30 days)
  * Primary keys and foreign keys

  
Business | 

  * Tags (object, data classification)
  * Data quality (anomaly detection results from Data Quality Monitoring, and data drift and custom metrics from Lakehouse Monitoring)
  * Data profiling (from Lakehouse Monitoring)
  * Joins and relationships
  * Table and view owner, creation time, and last altered time

  
Semantic | 

  * Metric view (dimensions, measures, relationship mapping, certifications)
  * Metric view owner
  * Metric view usage (views over 30 and 90 days; reads, writes, frequent users, and frequently joined tables over 30 days)
  * Display names (from metric views)
  * Synonyms (from metric views)
  * Markdown comments

  
  
## Limitations

The Databricks Unity Catalog connector has the following limitations:

  * Lineage isn't supported.
  * Semantic tags and business glossaries aren't supported in the integration ([Genie API](https://docs.databricks.com/aws/en/genie/)).
  * The connector imports the metadata for your Iceberg tables, but it doesn't automatically link the imported entries to the corresponding Google Cloud Lakehouse Databricks Unity Catalog Iceberg REST Catalog (IRC) entries.



## Before you begin

Before you can import metadata from Databricks Unity Catalog, complete the following tasks:

  1. Grant the required roles and permissions.
  2. Enable the Dataplex API and BigQuery Data Transfer Service API.
  3. Meet the Databricks Unity Catalog prerequisites.
  4. Meet the networking prerequisites.



### IAM roles and permissions

To create and manage a Knowledge Catalog connector job, you need Identity and Access Management (IAM) roles that grant permissions for Knowledge Catalog and [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction).

To get the permissions that you need to configure a Databricks Unity Catalog connector, ask your administrator to grant you the following IAM roles:

  * To create and manage entry groups: [Dataplex Catalog Admin](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`), [Dataplex Catalog Editor](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`), or [Dataplex Entry Group Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`) on the project.
  * To view Databricks Unity Catalog metadata: [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project.
  * To create and manage BigQuery Data Transfer Service transfer jobs: [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`) on the project.
  * To view logs in Cloud Logging: [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project.



You must also grant the BigQuery Data Transfer Service service agent (`service-PROJECT_NUMBER@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com`) both of the following roles:

  * [Dataplex Entry Group Importer](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupImporter) (`roles/dataplex.entryGroupImporter`), on the destination entry group or on the project that contains it. This role lets the service agent import metadata into the entry group (`dataplex.entryGroups.import`).
  * [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryOwner) (`roles/dataplex.entryOwner`), on the project that contains the destination entry group. This role lets the service agent import usage, business, and data quality metadata and entry links. It includes the following permissions:

    * `dataplex.entryGroups.useDataProfileAspect`
    * `dataplex.entryGroups.useDataQualityScorecardAspect`
    * `dataplex.entryGroups.useManagedConnectorTypes`
    * `dataplex.entryGroups.useReferenceEntryLink`
    * `dataplex.entryGroups.useSchemaAspect`
    * `dataplex.entryGroups.useSchemaJoinAspect`
    * `dataplex.entryGroups.useSchemaJoinEntryLink`
    * `dataplex.entryGroups.useUsageAspect`
    * `dataplex.entryLinks.reference`

Grant this role on the project, not only on the entry group, because the import checks the `dataplex.entryLinks.reference` permission on the project. If the service agent doesn't have this permission on the project, then the transfer run fails with an error such as `Permission 'dataplex.entryLinks.reference' denied`, and no metadata is imported.




Instead of granting both of these roles, you can grant the [Dataplex Entry Group Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`) role on the project that contains the destination entry group. This role includes the permissions of both roles, and it also lets the service agent create, delete, and manage access to all entry groups in the project.

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Enable APIs

Enable the Dataplex API and BigQuery Data Transfer Service API.

[Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=dataplex.googleapis.com,bigquerydatatransfer.googleapis.com)

### Databricks Unity Catalog prerequisites

The service principal used for the Databricks Unity Catalog connector must have the following permissions in Databricks Unity Catalog:

  * `Can use` permission on the Databricks SQL warehouse used by the connector.
  * [`BROWSE` privilege](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#the-browse-privilege) on the target catalogs, or `USE CATALOG`, `USE SCHEMA`, and `SELECT` on the target catalogs, schemas, and tables or views.
  * `USE CATALOG` on the `system` catalog, plus `USE SCHEMA` and `SELECT` on the following system schemas: 
    * `system.information_schema`: required to read catalogs, schemas, tables, columns, volumes, routines, constraints, and tags.
    * `system.access` and `system.query`: optional, required to import usage metrics, usage insights, and query-history joins.
    * `system.data_quality_monitoring`: optional, required to import anomaly detection results.
  * Optional: `USE CATALOG`, `USE SCHEMA`, and `SELECT` on the Lakehouse Monitoring output tables (`TABLE_NAME_profile_metrics` and `TABLE_NAME_drift_metrics`) to import data profiling and drift metrics.



If you also want to run SQL queries or Spark jobs against the remote Databricks catalog, see [Set up a cross-cloud connection for Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks).

### Networking prerequisites

To let BigQuery Data Transfer Service securely connect to external databases or third-party cloud data sources with a private IP address inside a private network, configure a [network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments) through Private Service Connect.

If you connect to an on-premises environment or a cloud-hosted instance using a public IP address, then a network attachment isn't required.

**Note:** Private domains with a network attachment aren't supported.

## Configure a Databricks Unity Catalog connector

Configure a Databricks Unity Catalog connector using the Google Cloud console or the REST API.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog page.

[Go to Knowledge Catalog](https://console.cloud.google.com/dataplex)

  2. In the navigation menu, in the **Manage** section, click **Connectors** , and then click **Add connection**.

  3. In the **Connectors** list, select the **Databricks Unity Catalog** card.

  4. In the **Data source details** section, provide connection details for your Databricks Unity Catalog instance:

     * For **Network attachment** , select an existing network attachment if required, or create one.
     * Enter the **Workspace Host** , **SQL Warehouse HTTP Path** , **Client Id** , and **Client Secret**.
     * For **Databricks objects to transfer** , click **Browse** to select the metastores, catalogs, schemas, or individual objects (tables, views, volumes, functions, and procedures) to import into Knowledge Catalog. Selecting a metastore, catalog, or schema imports all objects in it.

You can also enter objects manually in the format `TYPE:METASTORE[/CATALOG[/SCHEMA[/OBJECT]]]`, where `TYPE` is `METASTORE`, `CATALOG`, `SCHEMA`, `TABLE`, `VIEW`, `VOLUME`, `FUNCTION`, or `PROCEDURE` (for example, `SCHEMA:my_metastore/main/sales`). Name patterns aren't supported.

  5. In the **Destination settings** section:

     * Click **Browse** and select an existing Knowledge Catalog entry group to store the imported metadata, or click **Create new entry group**.
     * Select whether to set permissions on the entry group now or later. To let users view the imported metadata, set permissions on the entry group. If you didn't grant the [Dataplex Entry Group Importer](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupImporter) (`roles/dataplex.entryGroupImporter`) role or the `dataplex.entryGroups.import` permission to the BigQuery Data Transfer Service service agent at the project level, then grant it on this entry group. You must still grant the [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryOwner) (`roles/dataplex.entryOwner`) role on the project because the `dataplex.entryLinks.reference` permission is checked at the project level. For more information, see IAM roles and permissions.
  6. In the **Transfer config name** section, for **Display name** , enter a name for the metadata import job.

  7. In the **Schedule options** section, configure the frequency for the metadata import job. If you select **On-demand** , then the job runs only when you manually trigger it.

  8. Optional: In the **Notification options** section, configure an email or Pub/Sub notification for job failures.

  9. Optional: In the **Advanced options** section, configure encryption settings. If you select a customer-managed encryption key ([CMEK](https://docs.cloud.google.com/knowledge-catalog/docs/cmek)), then the key encrypts any transient data staged before starting the Knowledge Catalog metadata import jobs. The key doesn't encrypt the metadata in the destination Knowledge Catalog entry group.

  10. Click **Save**.




### REST

Use the [`projects.locations.transferConfigs.create`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs/create) method. In the [`TransferConfig`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs#TransferConfig) resource, configure the following fields:

  * Set the `dataSourceId` field to `"databricks_unity"`.
  * In the `metadataDestination` field, populate the `dataplexConfiguration.entryGroup` field with the resource path of the target Knowledge Catalog entry group: `projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID`.
  * In the `params` field, set the following parameters: 
    * `connector.host` (required): the Databricks workspace hostname (for example, `dbc-a1b2345c-d6e7.cloud.databricks.com`).
    * `connector.httpPath` (required): the HTTP path of the Databricks SQL warehouse (for example, `/sql/1.0/warehouses/a1b2345c67890def`).
    * `connector.authentication.oauth.clientId` (required): the Databricks OAuth client ID.
    * `connector.authentication.oauth.clientSecret` (required): the Databricks OAuth client secret.
    * `connector.networkAttachment` (optional): the network attachment in the format `projects/PROJECT_ID/regions/REGION/networkAttachments/NETWORK_ATTACHMENT_ID`.
    * `assets` (required): the list of Databricks Unity Catalog objects to import in the format `TYPE:METASTORE[/CATALOG[/SCHEMA[/OBJECT]]]`, such as `["SCHEMA:my_metastore/main/sales"]`.
  * Optional: To keep the OAuth credentials out of the transfer configuration, store them in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview): 
    1. Set `connector.authentication.oauth.clientSecret` (and `connector.authentication.oauth.clientId`, if you want) to the secret version resource name in the format `projects/SECRET_PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID`, and add those parameter names to the `paramConfig.secretManagerManagedParams` field.
    2. Grant the [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) role on each secret to the BigQuery Data Transfer Service service agent of the project that contains the transfer configuration (`service-PROJECT_NUMBER@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com`). The secrets can be in a different project. If the service agent can't read a secret, then the run fails before it starts with an error such as `Failed to retrieve secret ... Permission 'secretmanager.versions.access' denied`. BigQuery Data Transfer Service reads the secrets at the start of each run, so if you set `VERSION_ID` to `latest`, then a rotated secret is used starting with the next run.



The following example shows a `TransferConfig` request body:
    
    
    {
      "displayName": "databricks-unity-metadata-import",
      "dataSourceId": "databricks_unity",
      "schedule": "every 24 hours",
      "params": {
        "connector.host": "dbc-a1b2345c-d6e7.cloud.databricks.com",
        "connector.httpPath": "/sql/1.0/warehouses/a1b2345c67890def",
        "connector.authentication.oauth.clientId": "CLIENT_ID",
        "connector.authentication.oauth.clientSecret": "CLIENT_SECRET",
        "assets": [
          "SCHEMA:my_metastore/main/sales"
        ]
      },
      "metadataDestination": {
        "dataplexConfiguration": {
          "entryGroup": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID"
        }
      }
    }
    

The job runs automatically based on your schedule, or you can trigger it manually.

## Monitor a Databricks Unity Catalog connector job

Monitor a Databricks Unity Catalog connector job using the Google Cloud console or the REST API.

### Console

  1. In the Google Cloud console, on the **Connectors** page, click the **Display name** of the Databricks Unity Catalog transfer job.
  2. On the **Run history** tab, click **View details** to view logs.
  3. To view the created entries, click the **Details** tab, and then click the **Metadata destination** entry group link.



### REST

  * To list the runs of a transfer configuration and view their state, use the [`projects.locations.transferConfigs.runs.list`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs.runs/list) method.
  * Each run imports the harvested metadata into Knowledge Catalog with a metadata import job whose ID is `dts-run-RUN_ID`. To view the result of the import, such as the number of created entries, filter the job's logs in Logging using the following query:
        
        logName="projects/PROJECT_ID/logs/dataplex.googleapis.com%2Fmetadata_job"
        AND resource.labels.metadata_job_id="dts-run-RUN_ID"
        

  * To view the result of an import without using Logging, call the [`projects.locations.metadataJobs.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/get) method on `projects/PROJECT_ID/locations/LOCATION/metadataJobs/dts-run-RUN_ID`. The `importResult` field shows the number of created, updated, unchanged, and deleted entries and entry links.


**Note:** A transfer run can show a state of `SUCCEEDED` even when its metadata import job ends with `SUCCEEDED_WITH_ERRORS`—for example, when an entry is rejected because one of its aspects is too large. Check the state and logs of the metadata import job to confirm that all entries were imported.

## Search and view Databricks Unity Catalog metadata

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In the **Filters** panel, filter for Databricks Unity Catalog assets by using the **Project** , **Systems** , and **Type aliases** sections. To filter for all Databricks Unity Catalog metadata, in the **Systems** section, select **Imported Context** , and then in the **Managed Connectors** subsection, select **Databricks Unity**.

  3. In the search field, enter a keyword or natural language search query. For example, to view all Databricks Unity Catalog assets through keyword search, enter `system=DATABRICKS`.

To learn more about searching for resources, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets). To learn more about the expressions that you can use in the search field, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax).




You can also use the [`LookupContext`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext) API to retrieve LLM context for specific Databricks Unity Catalog resources. For more information, see [Retrieve context for data assets](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context).

## What's next

  * Learn how to [manage connector jobs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-connector-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
