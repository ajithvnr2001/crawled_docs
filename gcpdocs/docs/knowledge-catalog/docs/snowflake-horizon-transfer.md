---
url: https://docs.cloud.google.com/knowledge-catalog/docs/snowflake-horizon-transfer/
title: Import metadata from Snowflake Horizon \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:46.502786+00:00
---

# Import metadata from Snowflake Horizon  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/snowflake-horizon-transfer/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Import metadata from Snowflake Horizon Stay organized with collections  Save and categorize content based on your preferences. 

Break down data silos and avoid switching between tools by using a Knowledge Catalog (formerly Dataplex Universal Catalog) connector to import metadata from Snowflake Horizon directly into Google Cloud.

This connector supports Snowflake Horizon instances hosted on Google Cloud, Microsoft Azure, or Amazon Web Services (AWS).

The following table lists the metadata that the Snowflake Horizon connector captures:

Category | Metadata captured  
---|---  
Technical | 

  * Metastore (Snowflake account)
  * Catalog (database)
  * Schema
  * Table (including transient, external, dynamic, interactive, hybrid, and Apache Iceberg tables) and columns
  * View (standard, materialized, and secure)
  * Stages (internal and external), imported as filesets
  * User-defined functions (UDFs) and stored procedures

  
Operational | 

  * Usage metrics (views, reads, and writes over 30 and 90 days; frequent users and frequently joined tables over 30 days)
  * Primary keys and foreign keys

  
Business | 

  * Tags (object, column, and semantic view member tags)
  * Data quality (data metric function expectations, anomaly detection, and automatic data quality monitoring results)
  * Data profiling (data metric function measurements and data classification results)
  * Joins and relationships (inferred from query history, declared in semantic views, and view-to-table dependencies)
  * Owner (owning role), creation time, and last altered time

  
Semantic | 

  * Semantic view (logical tables, dimensions, facts, metrics, relationships, synonyms, sample values, and custom instructions)
  * Semantic view owner
  * Semantic view usage (views and reads over 30 and 90 days; frequent users and frequently joined tables over 30 days)

  
  
## Limitations

The Snowflake Horizon connector has the following limitations:

  * Lineage isn't supported.
  * The connector imports the metadata for your Iceberg tables, but it doesn't automatically link this metadata to the underlying physical tables in your Iceberg REST Catalog (IRC).
  * Tags, data quality and profiling results, classification results, query-history joins, and usage insights that read `ACCESS_HISTORY` (frequent users and frequently joined tables) require Snowflake Enterprise Edition or higher.



## Before you begin

Before you can import metadata from Snowflake Horizon, complete the following tasks:

  1. Grant the required roles and permissions.
  2. Enable the Dataplex API and BigQuery Data Transfer Service API.
  3. Meet the Snowflake Horizon prerequisites.
  4. Meet the networking prerequisites.



### IAM roles and permissions

To create and manage a Knowledge Catalog connector job, you need Identity and Access Management (IAM) roles that grant permissions for Knowledge Catalog and [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction).

To get the permissions that you need to configure a Snowflake Horizon connector, ask your administrator to grant you the following IAM roles:

  * To create and manage entry groups: [Dataplex Catalog Admin](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`), [Dataplex Catalog Editor](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`), or [Dataplex Entry Group Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`) on the project.
  * To view Snowflake Horizon metadata: [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project.
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

### Snowflake Horizon prerequisites

If you also want to run SQL queries or Spark jobs against the remote Snowflake catalog, see [Set up a cross-cloud connection for Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake).

The connector signs in to Snowflake as a Snowflake user with key-pair authentication and reads metadata from the `SNOWFLAKE.ACCOUNT_USAGE` schema. Password authentication isn't supported. A Snowflake administrator, such as a user with the `ACCOUNTADMIN` role, must complete the following steps:

  1. Create a role for the connector and grant it access to `ACCOUNT_USAGE` and to a warehouse that runs the metadata queries:
         
         CREATE ROLE IF NOT EXISTS DATAPLEX_CATALOG_READER;
         GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE
           TO ROLE DATAPLEX_CATALOG_READER;
         GRANT USAGE ON WAREHOUSE WAREHOUSE_NAME
           TO ROLE DATAPLEX_CATALOG_READER;
         

Replace `WAREHOUSE_NAME` with the name of the Snowflake warehouse that runs the metadata queries.

  2. Create a service user for the connector, or use an existing user, and grant it the role:
         
         CREATE USER IF NOT EXISTS USERNAME
           TYPE = SERVICE
           DEFAULT_ROLE = DATAPLEX_CATALOG_READER
           DEFAULT_WAREHOUSE = WAREHOUSE_NAME;
         GRANT ROLE DATAPLEX_CATALOG_READER TO USER USERNAME;
         

Replace `USERNAME` with the name of the Snowflake user for the connector.

  3. Generate an RSA key pair with the private key in PKCS#8 format:
         
         openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
         openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
         

To encrypt the private key, replace `-nocrypt` with `-v2 aes-256-cbc` and provide the passphrase when you configure the connector. Keep the private key file (`rsa_key.p8`) secure because you provide it when you configure the connector.

  4. Assign the public key to the Snowflake user:
         
         ALTER USER USERNAME SET RSA_PUBLIC_KEY='PUBLIC_KEY';
         

Replace `PUBLIC_KEY` with the contents of `rsa_key.pub`, excluding the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` lines.

  5. Optional: To import additional metadata, grant the connector role the following privileges:

     * **Data profiles and data quality results** : Grant the `SNOWFLAKE.DATA_QUALITY_MONITORING_VIEWER` application role:
           
           GRANT APPLICATION ROLE SNOWFLAKE.DATA_QUALITY_MONITORING_VIEWER
             TO ROLE DATAPLEX_CATALOG_READER;
           

Data quality results are imported only for the checks that the role can view, which requires `USAGE` on the database and schema, `SELECT` on the table, and `USAGE` on custom data metric functions.

     * **Primary keys and foreign keys** : Grant `USAGE` on the database and schema, and `SELECT` or `REFERENCES` on the tables.

     * **Sample values and custom instructions of semantic views** : Grant `REFERENCES` on the semantic views.




To find the account identifier that you enter when you configure the connector, run the following query in Snowflake:
    
    
    SELECT CURRENT_ORGANIZATION_NAME() || '-' || CURRENT_ACCOUNT_NAME();
    

**Note:** The connector reads metadata from `ACCOUNT_USAGE` views, which have a latency of up to 3 hours, and up to 24 hours for some views. Objects that you create or change might not appear until a later run.

### Networking prerequisites

To let BigQuery Data Transfer Service securely connect to external databases or third-party cloud data sources with a private IP address inside a private network, configure a [network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments) through Private Service Connect.

If you connect to an on-premises environment or a cloud-hosted instance using a public IP address, then a network attachment isn't required.

**Note:** Private domains with a network attachment aren't supported.

## Configure a Snowflake Horizon connector

Configure a Snowflake Horizon connector using the Google Cloud console or the REST API.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog page.

[Go to Knowledge Catalog](https://console.cloud.google.com/dataplex)

  2. In the navigation menu, in the **Manage** section, click **Connectors** , and then click **Add connection**.

  3. In the **Connectors** list, select the **Snowflake Horizon** card.

  4. In the **Data source details** section, provide connection details for your Snowflake account:

     * For **Network attachment** , select an existing network attachment if required, or create one.
     * For **Account Identifier** , enter your Snowflake account identifier without `.snowflakecomputing.com` (for example, `myorg-myaccount`). You can also enter an account locator, such as `xy12345.us-east-2.aws`.
     * For **Username** , enter the Snowflake user that you configured for key-pair authentication.
     * For **Private Key** , enter the PKCS#8 private key of the user, such as the contents of the `rsa_key.p8` file.
     * Optional: For **Private Key Passphrase** , if the private key is encrypted, then enter its passphrase.
     * Optional: For **Warehouse** , enter the warehouse that runs the metadata queries. If you don't specify a warehouse, then the connector uses the user's default warehouse.
     * Optional: For **Role** , enter the role that the connector uses, such as `DATAPLEX_CATALOG_READER`. If you don't specify a role, then the connector uses the user's default role.
     * For **Snowflake objects to transfer** , click **Browse** to select the databases, schemas, or individual objects (tables, views, semantic views, stages, functions, and procedures) to import. Selecting a database or schema imports all objects in it. Functions and procedures are listed with their argument types, such as `CALC(NUMBER, VARCHAR)`.

You can also enter objects manually in the format `TYPE:ACCOUNT/DATABASE[/SCHEMA[/OBJECT]]`, where `TYPE` is `CATALOG` (or `DATABASE`), `SCHEMA`, `TABLE`, `VIEW`, `SEMANTIC-MODEL`, `FILESET`, `FUNCTION`, or `PROCEDURE` (for example, `SCHEMA:myorg-myaccount/SALES/PUBLIC`). Enter `ACCOUNT` in the lowercase `ORG_NAME-ACCOUNT_NAME` format shown in **Browse**. Database, schema, and object names are case-sensitive. Name patterns aren't supported.

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

  * Set the `dataSourceId` field to `"snowflake_horizon"`.
  * In the `metadataDestination` field, populate the `dataplexConfiguration.entryGroup` field with the resource path of the target Knowledge Catalog entry group: `projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID`.
  * In the `params` field, set the following parameters: 
    * `connector.accountIdentifier` (required): your Snowflake account identifier without `.snowflakecomputing.com` (for example, `myorg-myaccount`) or an account locator (such as `xy12345.us-east-2.aws`).
    * `connector.authentication.username` (required): the Snowflake user.
    * `connector.authentication.privateKey` (required): the private key of the user in PKCS#8 PEM format.
    * `connector.authentication.privateKeyPassphrase` (optional): the passphrase of the private key, if the key is encrypted.
    * `connector.warehouse` (optional): the warehouse that runs the metadata queries. If you omit this parameter, then the connector uses the user's default warehouse.
    * `connector.role` (optional): the role that the connector uses. If you omit this parameter, then the connector uses the user's default role.
    * `connector.networkAttachment` (optional): the network attachment in the format `projects/PROJECT_ID/regions/REGION/networkAttachments/NETWORK_ATTACHMENT_ID`.
    * `assets` (required): the list of Snowflake objects to import in the format `TYPE:ACCOUNT/DATABASE[/SCHEMA[/OBJECT]]`, such as `["SCHEMA:myorg-myaccount/SALES/PUBLIC"]`.
  * Optional: To keep the private key out of the transfer configuration, store it in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview): 
    1. Set `connector.authentication.privateKey` (and `connector.authentication.privateKeyPassphrase`, if you use one) to the secret version resource name in the format `projects/SECRET_PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID`, and add those parameter names to the `paramConfig.secretManagerManagedParams` field.
    2. Grant the [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) role on each secret to the BigQuery Data Transfer Service service agent of the project that contains the transfer configuration (`service-PROJECT_NUMBER@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com`). The secrets can be in a different project. If the service agent can't read a secret, then the run fails before it starts with an error such as `Failed to retrieve secret ... Permission 'secretmanager.versions.access' denied`. BigQuery Data Transfer Service reads the secrets at the start of each run, so if you set `VERSION_ID` to `latest`, then a rotated key is used starting with the next run.



The following example shows a `TransferConfig` request body:
    
    
    {
      "displayName": "snowflake-metadata-import",
      "dataSourceId": "snowflake_horizon",
      "schedule": "every 24 hours",
      "params": {
        "connector.accountIdentifier": "myorg-myaccount",
        "connector.authentication.username": "USERNAME",
        "connector.authentication.privateKey": "PRIVATE_KEY",
        "connector.warehouse": "WAREHOUSE_NAME",
        "connector.role": "DATAPLEX_CATALOG_READER",
        "assets": [
          "SCHEMA:myorg-myaccount/SALES/PUBLIC"
        ]
      },
      "metadataDestination": {
        "dataplexConfiguration": {
          "entryGroup": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID"
        }
      }
    }
    

The job runs automatically based on your schedule, or you can trigger it manually.

## Monitor a Snowflake Horizon connector job

Monitor a Snowflake Horizon connector job using the Google Cloud console or the REST API.

### Console

  1. In the Google Cloud console, on the **Connectors** page, click the **Display name** of the Snowflake Horizon transfer job.
  2. On the **Run history** tab, click **View details** to view logs.
  3. To view the created entries, click the **Details** tab, and then click the **Metadata destination** entry group link.



### REST

  * To list the runs of a transfer configuration and view their state, use the [`projects.locations.transferConfigs.runs.list`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs.runs/list) method.
  * Each run imports the harvested metadata into Knowledge Catalog with a metadata import job whose ID is `dts-run-RUN_ID`. To view the result of the import, such as the number of created entries, filter the job's logs in Logging using the following query:
        
        logName="projects/PROJECT_ID/logs/dataplex.googleapis.com%2Fmetadata_job"
        AND resource.labels.metadata_job_id="dts-run-RUN_ID"
        

  * To view the result of an import without using Logging, call the [`projects.locations.metadataJobs.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/get) method on `projects/PROJECT_ID/locations/LOCATION/metadataJobs/dts-run-RUN_ID`. The `importResult` field shows the number of created, updated, unchanged, and deleted entries and entry links.


**Note:** A transfer run can show a state of `SUCCEEDED` even when its metadata import job ends with `SUCCEEDED_WITH_ERRORS`—for example, when an entry is rejected because one of its aspects is too large. Check the state and logs of the metadata import job to confirm that all entries were imported.

## Search and view Snowflake Horizon metadata

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In the **Filters** panel, filter for Snowflake Horizon assets by using the **Project** , **Systems** , and **Type aliases** sections. To filter for all Snowflake Horizon metadata, in the **Systems** section, select **Imported Context** , and then in the **Managed Connectors** subsection, select **Snowflake Horizon**.

  3. In the search field, enter a keyword or natural language search query. For example, to view all Snowflake Horizon assets through keyword search, enter `system=SNOWFLAKE`.

To learn more about searching for resources, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets). To learn more about the expressions that you can use in the search field, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax).




You can also use the [`LookupContext`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext) API to retrieve LLM context for specific Snowflake Horizon resources. For more information, see [Retrieve context for data assets](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context).

## What's next

  * Learn how to [manage connector jobs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-connector-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
