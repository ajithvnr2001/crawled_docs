---
url: https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer/
title: Schedule a Snowflake transfer \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:38:27.659185+00:00
---

# Schedule a Snowflake transfer  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Schedule a Snowflake transfer

The Snowflake connector provided by the BigQuery Data Transfer Service lets you schedule and manage automated transfer jobs to migrate data from Snowflake into BigQuery using public IP allowlists.

## Overview

The Snowflake connector engages migration agents in the Google Kubernetes Engine and triggers a load operation from Snowflake to a staging area within the Cloud Storage bucket.

  * For Amazon Web Services (AWS) or Azure or Google Cloud-hosted Snowflake accounts, the data is first staged in your Cloud Storage bucket, which is then transferred to BigQuery with the BigQuery Data Transfer Service.



The following diagram illustrates public data transfers from Snowflake accounts hosted on Amazon Web Services (AWS) or Azure or Google Cloud-hosted Snowflake accounts.

![Public Data transfers from AWS or Azure or Google Cloud-hosted Snowflake accounts to BigQuery](https://docs.cloud.google.com/static/bigquery/images/snowflake-public-overview.png)

## Limitations

Data transfers made using the Snowflake connector are subject to the following limitations:

  * The Snowflake connector only supports transfers from tables within a single Snowflake database and schema. To transfer from tables with multiple Snowflake databases or schemas, you can set up each transfer job separately.
  * The speed of loading data from Snowflake to your Amazon S3 bucket or Azure Blob Storage container or Cloud Storage bucket is limited by the Snowflake warehouse you have chosen for this transfer.
  * BigQuery writes data from Snowflake to Cloud Storage as Parquet files. Parquet files don't support the [`TIMESTAMP_TZ` and `TIMESTAMP_LTZ`](https://community.snowflake.com/s/article/How-To-Unload-Timestamp-data-in-a-Parquet-file) data types. If your data contains these types, you can export it to Amazon S3 as CSV files and then import the CSV files into BigQuery. For more information, see [Introduction to Amazon S3 data transfers](https://docs.cloud.google.com/bigquery/docs/s3-transfer-intro).



## Before you begin

The following sections describe the steps you must take to set up a Snowflake transfer.

### Prepare your Google Cloud project

Create and configure your Google Cloud project for a Snowflake transfer with the following steps:

  1. [Create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) or select an existing project.

**Note:** If you don't plan on keeping the resources created during this Snowflake transfer, create a new Google Cloud project instead of selecting an existing one. You can then delete the project once you are done with your Snowflake transfer.
  2. Verify that you have completed all actions required to [enable the BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/enable-transfer-service).

  3. [Create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets) to store your data. You don't need to create any tables.




### Get required IAM roles

To create and manage Snowflake data transfers, all required user and service accounts must have the roles that are described in the following table:

Identity | Role | Target resource  
---|---|---  
User account | `roles/bigquery.user` | Google Cloud project  
User account | `roles/bigquery.dataOwner` | Destination BigQuery dataset  
User account | `roles/iam.serviceAccountUser` | Dedicated service account  
Dedicated service account | `roles/storage.objectViewer` | Staging Cloud Storage bucket, and the bucket or buckets that contain the schema mapping files  
BigQuery Data Transfer Service service agent | `roles/storage.objectViewer` | Staging Cloud Storage bucket  
BigQuery Data Transfer Service service agent | `roles/bigquery.dataEditor` | Destination BigQuery dataset  
BigQuery Data Transfer Service service agent | `roles/iam.serviceAccountTokenCreator` |  Dedicated service account, if you use a [cross-project service account](https://docs.cloud.google.com/bigquery/docs/enable-transfer-service#cross-project_service_account_authorization)  
Snowflake Google Cloud service account | `roles/storage.objectUser` | Staging Cloud Storage bucket  
Snowflake Google Cloud service account | `roles/storage.bucketViewer` | Staging Cloud Storage bucket  
  
The following sections provide more details about the required roles and permissions for each identity.

#### Get user account permissions

To get the permissions that you need to create and manage transfer configurations and run jobs with a user account, ask your administrator to grant you the following IAM roles: 

  * Create and manage transfer configurations and run jobs: [BigQuery User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`) on the project 
  * Manage and grant access to the destination dataset: [BigQuery Data Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`) on the destination BigQuery dataset 
  * Create or update transfer configurations with a dedicated service account: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the dedicated service account 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and manage transfer configurations and run jobs with a user account. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage transfer configurations and run jobs with a user account:

  * `bigquery.transfers.get`
  * `bigquery.transfers.update`
  * `bigquery.datasets.get`
  * `bigquery.datasets.getIamPolicy`
  * `bigquery.datasets.update`
  * `bigquery.jobs.create`
  * `bigquery.datasets.setIamPolicy`
  * `iam.serviceAccounts.actAs`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Get dedicated service account permissions

To ensure that the dedicated service account has the necessary permissions to use a service account to read translation metadata, custom schema, or staging files during transfer execution, ask your administrator to grant the [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) IAM role to the dedicated service account on the Cloud Storage staging bucket, and the bucket or buckets that contain the schema mapping files. **Important:** You must grant this role to the dedicated service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

#### Get BigQuery Data Transfer Service service agent permissions

To ensure that BigQuery Data Transfer Service service agent has the necessary permissions to use a service agent to run the transfer, ask your administrator to grant the following IAM roles to BigQuery Data Transfer Service service agent: 

**Important:** You must grant these roles to BigQuery Data Transfer Service service agent, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Read unloaded data files during transfer execution: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the Cloud Storage staging bucket 
  * Write transferred data into destination tables: [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the destination BigQuery dataset 
  * Authorize transfers that use a cross-project service account: [Service Account Token Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) on the cross-project dedicated service account 



If the dedicated service account is in the same project where the BigQuery Data Transfer Service is enabled, Google automatically grants the required `iam.serviceAccounts.getAccessToken` permission. You only need to grant the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) manually if the dedicated service account is in a different project. For more information, see [Cross-project service account authorization](https://docs.cloud.google.com/bigquery/docs/enable-transfer-service#cross-project_service_account_authorization).

#### Get Snowflake Google Cloud service account permissions

To ensure that Snowflake Google Cloud service account has the necessary permissions to write and manage unloaded data files in the staging bucket, ask your administrator to grant the following IAM roles to Snowflake Google Cloud service account on the Cloud Storage staging bucket: 

**Important:** You must grant these roles to Snowflake Google Cloud service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)
  * [Storage Bucket Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`)



These predefined roles contain the permissions required to write and manage unloaded data files in the staging bucket. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to write and manage unloaded data files in the staging bucket:

  * `storage.buckets.get`
  * `storage.objects.get`
  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.list`



### Prepare staging bucket

To prepare for a Snowflake data transfer, create a staging bucket and then configure it to allow write access from Snowflake. You must stage the Snowflake data in a Cloud Storage bucket before you can load it into BigQuery. The staging bucket must not have the hierarchical namespace feature enabled.

To create and configure a staging bucket, do the following:

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. [Create and configure a Snowflake storage integration object](https://docs.snowflake.com/en/user-guide/data-load-gcs-config) to allow Snowflake to write data into the Cloud Storage bucket as an external stage. 
         
         CREATE STORAGE INTEGRATION STORAGE_INTEGRATION_NAME
         TYPE = EXTERNAL_STAGE
         STORAGE_PROVIDER = 'GCS'
         ENABLED = TRUE
         STORAGE_ALLOWED_LOCATIONS = ('gcs://STAGING_BUCKET_NAME/');
         
         -- Describe integration to retrieve Snowflake Google Cloud service account
         DESCRIBE INTEGRATION STORAGE_INTEGRATION_NAME;

Replace the following:

     * `STORAGE_INTEGRATION_NAME`: the name of the new storage integration object.
     * `STAGING_BUCKET_NAME`: the name of the Cloud Storage bucket you created.
  3. When you run the [`DESCRIBE INTEGRATION` command](https://docs.snowflake.com/en/user-guide/data-load-gcs-config#step-2-retrieve-the-cloud-storage-service-account-for-your-snowflake-account), the Cloud Storage service account is listed under the `STORAGE_GCP_SERVICE_ACCOUNT` field. Grant the Cloud Storage service account the following permissions on the Cloud Storage bucket:

     * `storage.buckets.get`
     * `storage.objects.create`
     * `storage.objects.delete`
     * `storage.objects.get`
     * `storage.objects.list`
  4. To allow access to the staging bucket, grant the [BigQuery Data Transfer Service service agent](https://docs.cloud.google.com/bigquery/docs/enable-transfer-service#service_agent) the `roles/storage.objectViewer` role:
         
         gcloud storage buckets add-iam-policy-binding gs://STAGING_BUCKET_NAME \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com \
             --role=roles/storage.objectViewer




For a Snowflake private data transfer, [create the staging bucket and configure it for private connectivity](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#prepare_staging_bucket).

If your Google Cloud organization enforces domain-restricted sharing with the `constraints/iam.allowedPolicyMemberDomains` constraint, granting IAM roles on the staging bucket to the `STORAGE_GCP_SERVICE_ACCOUNT` service account fails because that service account belongs to Snowflake's external organization.

You can't derive Snowflake's Google Workspace customer ID from the service account email address. Obtain the customer ID in one of the following ways:

  * If your Snowflake account is hosted on Google Cloud, run `SELECT SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO();` in Snowflake with the `ACCOUNTADMIN` role, and find the `snowflake-customer-directory-id` value in the output.
  * If your Snowflake account is hosted on AWS or Azure, contact Snowflake Support to request the Google Workspace customer ID for your `STORAGE_GCP_SERVICE_ACCOUNT` service account.



To add Snowflake's customer ID to the allowed list for your project, update the organization policy:
    
    
    gcloud resource-manager org-policies allow \
        iam.allowedPolicyMemberDomains EXTERNAL_CUSTOMER_ID \
        --project=PROJECT_ID

Replace the following:

  * `EXTERNAL_CUSTOMER_ID`: Snowflake's Google Workspace customer ID.
  * `PROJECT_ID`: the ID of the Google Cloud project that contains your staging bucket.



For more information, see [Restrict identities with domain-restricted sharing](https://docs.cloud.google.com/organization-policy/restrict-domains#predefined-constraint).

### Create a Snowflake user with the required permissions

During a Snowflake transfer, the Snowflake connector connects to your Snowflake account using a JDBC connection. You must create a new Snowflake user with a custom role that only has the necessary privileges to perform the data transfer.

The following table lists the required roles and privileges for the custom role named `MIGRATION_ROLE`:

Identity | Role or privilege | Target resource | Purpose  
---|---|---|---  
Migration User | `MIGRATION_ROLE` | Snowflake account | Authenticate using RSA Key-Pair and execute migration operations.  
Migration Role | `USAGE` | Snowflake warehouse | Provide compute capacity for query execution.  
| `USAGE` | Snowflake database and schema | Access the database and schema containing source tables.  
| `SELECT` | Source tables | Read table metadata and extract data for transfer.  
| `USAGE` | Storage integration | Authorize unloading data to the external Cloud Storage staging bucket.  
  
To create and configure the custom role and migration user, run the following SQL commands in your Snowflake account:

  1. Create the custom role, `MIGRATION_ROLE`:
         
         CREATE ROLE MIGRATION_ROLE;

Replace `MIGRATION_ROLE` with the name of the custom role that you are creating.

  2. Grant the custom role the required permissions:
         
         GRANT USAGE ON WAREHOUSE WAREHOUSE_NAME TO ROLE MIGRATION_ROLE;
         GRANT USAGE ON DATABASE DATABASE_NAME TO ROLE MIGRATION_ROLE;
         GRANT USAGE ON SCHEMA DATABASE_NAME.SCHEMA_NAME TO ROLE MIGRATION_ROLE;
         GRANT SELECT ON ALL TABLES IN SCHEMA DATABASE_NAME.SCHEMA_NAME TO ROLE MIGRATION_ROLE;
         GRANT USAGE ON INTEGRATION STORAGE_INTEGRATION_OBJECT_NAME TO ROLE MIGRATION_ROLE;

Replace the following:

     * `WAREHOUSE_NAME`: the name of your data warehouse.
     * `DATABASE_NAME`: the name of your Snowflake database.
     * `SCHEMA_NAME`: the name of your Snowflake schema.
     * `STORAGE_INTEGRATION_OBJECT_NAME`: the name of your Snowflake storage integration object.
  3. Create the migration user as a service user:
         
         CREATE USER MIGRATION_USER TYPE = SERVICE;

Replace `MIGRATION_USER` with the username for the migration user. Setting `TYPE = SERVICE` creates a service user that authenticates with a key pair and is exempt from interactive multi-factor authentication (MFA).

  4. Assign the custom role to the migration user:
         
         GRANT ROLE MIGRATION_ROLE TO USER MIGRATION_USER;
         ALTER USER MIGRATION_USER SET DEFAULT_ROLE = MIGRATION_ROLE;




#### Generate key pair for authentication

Due to the [deprecation of single-factor password sign-ins by Snowflake](https://docs.snowflake.com/en/user-guide/security-mfa-rollout), we recommend that you use a key pair for authentication. Configure a key pair by doing the following:

  1. Generate a 2048-bit PKCS#8 private key in PEM format. Choose whether to generate an unencrypted or an encrypted private key:

     * To generate an unencrypted private key, run the following command:
           
           openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt

     * To generate an encrypted private key, run the following command and enter a passphrase when prompted:
           
           openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 des3 -inform PEM -out rsa_key.p8

  2. Generate the corresponding public key:
         
         openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub

  3. Assign the public key, excluding the header, footer, and line breaks, to your Snowflake migration user:
         
         ALTER USER MIGRATION_USER SET RSA_PUBLIC_KEY='PUBLIC_KEY_STRING';

Replace `PUBLIC_KEY_STRING` with the body of the generated public key in the `rsa_key.pub` file.




For more information, see [Configuring key-pair authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth#configuring-key-pair-authentication).

#### Allow unloading to inline external locations

The Snowflake connector unloads data to inline external locations during the transfer. If your Snowflake account restricts unloading to inline locations, the transfer fails.

To allow unloading to inline locations, run the following SQL command in your Snowflake account. You must have the `ACCOUNTADMIN` role in Snowflake to run this command.
    
    
    ALTER ACCOUNT SET PREVENT_UNLOAD_TO_INLINE_URL = false;

Alternatively, you can use `SET` to allow unloading on the migration user with the following command:
    
    
    ALTER USER MIGRATION_USER SET PREVENT_UNLOAD_TO_INLINE_URL = false;

Replace `MIGRATION_USER` with the username for the migration user.

## Additional prerequisites for optional configurations

To configure optional features for your Snowflake transfer, such as private connectivity or incremental transfers, you must complete these prerequisites that are described in the following sections.

### Add network policies

For public connectivity, the Snowflake account allows public connection with database credentials by default. However, you might have configured network rules or policies that could prevent the Snowflake connector from connecting to your account. In this case, you must add the necessary IP addresses to your allowlist. For more information, see [Configure network policies for Snowflake transfers](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-network-policies).

### Schema detection and mapping

To define your schema, you can use the BigQuery Data Transfer Service to automatically detect schema and data type mapping when transferring data from Snowflake to BigQuery. Alternatively, you can use the translation engine to define your schema and data types manually.

For more information, see [Schema detection and mapping for Snowflake](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema).

### Enable incremental transfers

To set up an incremental Snowflake data transfer, see [Set up incremental transfers for Snowflake](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-incremental).

### Enable private connectivity

If you want to create a private Snowflake data transfer, you must [configure your network for private connectivity](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity).

## Set up a Snowflake transfer

Before you set up a Snowflake transfer, ensure that you have the following information:

  * Your Snowflake account identifier, which is the prefix in your Snowflake account URL. For example, `ACCOUNT_IDENTIFIER.snowflakecomputing.com`.
  * The username and the associated private key with appropriate permissions to your Snowflake database. It can just have the required permissions to execute the data transfer.
  * The URI of the staging bucket to use for the transfer. We recommend that you set up a lifecycle policy for this bucket to avoid unnecessary charges.
  * The URI of the Cloud Storage bucket where you have stored the [schema mapping files obtained from the translation engine](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema).



To create a Snowflake transfer configuration, do the following:

###  Console 

  1. Go to the Data transfers page in the Google Cloud console.

[Go to Data transfers](https://console.cloud.google.com/bigquery/transfers)

  2. Click add **Create transfer**.

  3. In the **Source type** section, select **Snowflake Migration** from the **Source** list.

  4. In the **Transfer config name** section, enter a name for the transfer, such as `My migration`, in the **Display name** field. The display name can be any value that lets you identify the transfer if you need to modify it later.

  5. In the **Schedule options** section, in the **Repeat frequency** list, select an option to specify how often this data transfer runs. To specify a custom repeat frequency, select **Custom**. If you select **On-demand** , then this transfer runs when you [manually trigger the transfer](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer).

  6. In the **Destination settings** section, choose the dataset you created from the **Dataset** list.

  7. In the **Snowflake Credentials** section, do the following:

     1. For **Account Identifier** , enter a unique identifier for your Snowflake account, which is a combination of your organization name and account name. The identifier is the prefix of the Snowflake account URL and not the complete URL. For example, `ACCOUNT_IDENTIFIER.snowflakecomputing.com`.
     2. For **Username** , enter the username of the Snowflake user whose credentials and authorization is used to access your database to transfer the Snowflake tables. We recommend using the user that you created for this transfer.
     3. For **Authentication Mechanism** , select a Snowflake user authentication method:

###  PASSWORD 

        * For **Password** , enter the password of the Snowflake user.

###  KEY_PAIR 

        * For **Private Key** , enter the private key linked with the public key associated with the Snowflake user.
        * For **Is Private Key Encrypted** , select this field if the private key is encrypted with a passphrase.
        * For **Private Key Passphrase** , enter the passphrase for the encrypted private key. This field is required if you have selected **Is Private Key Encrypted**. For more information, see Generate key pair for authentication.

     * For **Warehouse** , enter a [warehouse](https://docs.snowflake.com/en/user-guide/warehouses-tasks) that is used for the execution of this data transfer.
     * For **Snowflake Database** , enter the name of the Snowflake database that contains the tables included in this data transfer.
     * For **Snowflake Schema** , enter the name of the Snowflake schema that contains the tables included in this data transfer.
  8. In the **Network Connectivity** section, if you are creating a [private data transfer](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity), select **Use Private Network** , and then do the following:

     * For **PSC Service Attachment** , enter the service attachment URI for private connectivity to Snowflake. For more information, see [Create a private Snowflake transfer configuration](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#create-transfer-config).
     * For **Private Network Service** , if your Snowflake account is hosted on AWS or Azure, enter the Service Directory service self-link for your network load balancer. For more information, see [Create a private Snowflake transfer configuration](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#create-transfer-config).
  9. In the **Storage Configuration** section, do the following:

     1. For **Storage integration object name** , enter the name of the Snowflake storage integration object. This is a required field unless you are specifying a pre-configured Snowflake external stage using the `bq mk` command or the API to create the transfer configuration.
     2. Optional: For **Max file size** , specify the maximum size of each file unloaded from Snowflake to the staging location (in MB).
     3. For **Cloud Provider** , select `AWS` or `AZURE` or `GCP` depending on which cloud provider is hosting your Snowflake account.

        * For **GCS URI** , enter the URI of the Cloud Storage bucket to use as a staging bucket.
  10. In the **Service Account** section, do the following:

     1. For **Service Account** , enter a service account to use with this data transfer. The service account should belong to the same Google Cloud project where the transfer configuration and destination dataset is created. The service account must have the `storage.objects.list` and `storage.objects.get` [required permissions](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema#required_service_account_permissions).
  11. In the **Schema Configuration** section, do the following:

     1. For **Ingestion type** , select **Full** or **Incremental**. For more information, see [Configure incremental transfers](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-incremental#configure_incremental_transfers).
     2. For **Table name patterns** , specify the tables to transfer by entering a semicolon-separated list of table names or patterns, such as `TABLE1_REGEX;TABLE2_REGEX`. Patterns must follow Java regular expression syntax. This field is required: 
        * `lineitem;ordertb` matches tables that are named `lineitem` and `ordertb`.
        * `.*` matches all tables in the schema.
     3. Optional: If you want to specify a custom translation output path, select **Use BigQuery Translation Engine Output**.
     4. Optional: For **Translation output GCS path** , specify a path to the Cloud Storage folder that contains the [schema mapping files from the translation engine](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema). You can leave this empty to have the Snowflake connector automatically detect your schema. 
        * The path should follow the format `translation_target_base_uri/metadata/config/db/schema/` and must end with `/`.
     5. Optional: To map Snowflake `NUMBER(p, 0)` types to BigQuery `INT64`, select **Map zero scale Snowflake NUMBER to BigQuery INT64**.
  12. Optional: In the **Notification options** section, do the following:

     1. Click the toggle to enable email notifications. When you enable this option, the transfer administrator receives an email notification when a transfer run fails.
     2. For **Select a Pub/Sub topic** , choose your [topic](https://docs.cloud.google.com/pubsub/docs/overview#types) name or click **Create a topic**. This option configures Pub/Sub run [notifications](https://docs.cloud.google.com/bigquery/docs/transfer-run-notifications) for your transfer.
  13. If you use [CMEKs](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption), in the **Advanced options** section, select **Customer-managed key**. A list of your available CMEKs appears for you to choose from. For information about how CMEKs work with the BigQuery Data Transfer Service, see Specify encryption key with transfers.

  14. Click **Save**.

  15. The Google Cloud console displays all the transfer setup details, including a **Resource name** for this transfer.




###  bq 

Enter the `bq mk` command and supply the `--transfer_config` flag. The following template includes mutually exclusive and conditional parameters for all supported configurations. When you run the command, include only the parameters that apply to your authentication mechanism, network connectivity mode, staging storage location, and schema mapping method.

**Note:** After you create a transfer configuration, you can't modify the `use_private_network`, `staging_gcs_uri`, `staging_s3_uri`, `azure_storage_account`, or `staging_azure_container` parameters.
    
    
    bq mk \
      --transfer_config \
      --project_id=PROJECT_ID \
      --data_source=snowflake_migration \
      --target_dataset=DATASET_NAME \
      --display_name='DISPLAY_NAME' \
      --params='{
        "account_identifier": "ACCOUNT_IDENTIFIER",
        "username": "MIGRATION_USER",
        "auth_mechanism": "AUTH_MECHANISM",
        "password": "PASSWORD",
        "private_key": "PRIVATE_KEY_STRING",
        "is_private_key_encrypted": PRIVATE_KEY_ENCRYPTED,
        "private_key_passphrase": "PRIVATE_KEY_PASSPHRASE",
        "service_account": "SERVICE_ACCOUNT_EMAIL",
        "warehouse": "WAREHOUSE_NAME",
        "database": "DATABASE_NAME",
        "schema": "SCHEMA_NAME",
        "table_name_patterns": "TABLE_NAME_PATTERNS",
        "cloud_provider": "CLOUD_PROVIDER",
        "staging_gcs_uri": "STAGING_BUCKET_URI",
        "staging_s3_uri": "STAGING_S3_URI",
        "aws_access_key_id": "AWS_ACCESS_KEY_ID",
        "aws_secret_access_key": "AWS_SECRET_ACCESS_KEY",
        "azure_storage_account": "AZURE_STORAGE_ACCOUNT",
        "staging_azure_container": "STAGING_AZURE_CONTAINER",
        "azure_sas_token": "AZURE_SAS_TOKEN",
        "storage_integration_object_name": "STORAGE_INTEGRATION_NAME",
        "max_file_size_mb": MAX_FILE_SIZE_MB,
        "use_private_network": USE_PRIVATE_NETWORK,
        "service_attachment": "SERVICE_ATTACHMENT_URI",
        "private_network_service": "SERVICE_DIRECTORY_LINK",
        "ingestion_type": "INGESTION_TYPE",
        "specify_translation_output": SPECIFY_TRANSLATION_OUTPUT,
        "translation_output_gcs_path": "TRANSLATION_OUTPUT_GCS_PATH",
        "custom_schema_file_path": "CUSTOM_SCHEMA_PATH",
        "convert_number_to_int64": CONVERT_NUMBER_TO_INT64
      }'

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID. If the `--project_id` flag isn't specified, the default project is used.
  * `DATASET_NAME`: the BigQuery target dataset for the transfer configuration.
  * `DISPLAY_NAME`: the display name for the transfer configuration. The display name can be any value that lets you identify the transfer if you need to modify it later.



Configure the applicable `--params` parameters for your Snowflake transfer configuration:

Parameter details  
---  
`ACCOUNT_IDENTIFIER` |  Specify a unique identifier for your Snowflake account, which is a combination of your organization name and account name. The identifier is the prefix of the Snowflake account URL (`ACCOUNT_IDENTIFIER.snowflakecomputing.com`) and not the complete URL. For example, `org-account`.  
`MIGRATION_USER` |  Specify the username of the Snowflake user whose credentials and authorization are used to access your database to transfer the Snowflake tables. For example, `MIGRATION_USER`.  
`AUTH_MECHANISM` |  Specify the Snowflake user authentication method. Supported values are `PASSWORD` and `KEY_PAIR`. For more information, see Generate key pair for authentication.  
`PASSWORD` |  Specify the password of the Snowflake user. Include this parameter only if you specify `PASSWORD` in the `auth_mechanism` parameter.  
`PRIVATE_KEY_STRING` |  Specify the private key in PKCS#8 PEM format that corresponds to the public key assigned to the Snowflake user. Include this parameter only if you specify `KEY_PAIR` in the `auth_mechanism` parameter. In the `--params` JSON string, replace all line breaks in the PEM key with `\n`. For example, `-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----` for an unencrypted key, or `-----BEGIN ENCRYPTED PRIVATE KEY-----\n...\n-----END ENCRYPTED PRIVATE KEY-----` for an encrypted key.  
`PRIVATE_KEY_ENCRYPTED` |  Optional: Specify `true` if the private key is encrypted with a passphrase. The default value is `false`.  
`PRIVATE_KEY_PASSPHRASE` |  Specify the passphrase for the encrypted private key. Include this parameter only if you specify `KEY_PAIR` in the `auth_mechanism` parameter and `true` in the `is_private_key_encrypted` parameter.  
`SERVICE_ACCOUNT_EMAIL` |  Specify the email address of the dedicated service account to use with this data transfer, in the format `SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com`. We recommend that the service account belong to the same Google Cloud project where the transfer configuration and destination dataset are created. The service account must have the `storage.objects.list` and `storage.objects.get` [required permissions](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema#required_service_account_permissions).  
`WAREHOUSE_NAME` |  Specify a [warehouse](https://docs.snowflake.com/en/user-guide/warehouses-tasks) that is used to run this data transfer. For example, `COMPUTE_WH`.  
`DATABASE_NAME` |  Specify the name of the Snowflake database that contains the tables included in this data transfer. For example, `SF_DB`.  
`SCHEMA_NAME` |  Specify the name of the Snowflake schema that contains the tables included in this data transfer. For example, `PUBLIC`.  
`TABLE_NAME_PATTERNS` |  Specify the tables to transfer by entering a semicolon-separated list of table names or patterns that match table names in the schema, such as `TABLE1_REGEX;TABLE2_REGEX`. Patterns must follow Java regular expression syntax. This parameter is required. For example:

  * `lineitem;ordertb` matches tables that are named `lineitem` and `ordertb`.
  * `.*` matches all tables in the schema.

  
`CLOUD_PROVIDER` |  Specify the cloud provider that hosts your Snowflake account. Supported values are `AWS`, `AZURE`, and `GCP`.  
`STAGING_BUCKET_URI` |  For the `staging_gcs_uri` parameter, specify the URI of the Cloud Storage staging bucket. Include this parameter when `cloud_provider` is `GCP`, or for public data transfers from `AWS`\- or `AZURE`-hosted Snowflake accounts. You can't modify this parameter after you create the transfer configuration. For example, `gs://staging-bucket/staging/`.  
`STAGING_S3_URI` |  For the `staging_s3_uri` parameter, specify the [URI of the Amazon S3 staging bucket](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#aws_3). Include this parameter for private data transfers when `cloud_provider` is `AWS` and `staging_gcs_uri` isn't specified. You can't modify this parameter after you create the transfer configuration. For example, `s3://staging-bucket/staging/`.  
`AWS_ACCESS_KEY_ID` |  For the `aws_access_key_id` parameter, specify the [access key ID](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#snowflake_key_pair) for the Amazon IAM user with read access to the Amazon S3 staging bucket. Include this parameter when `staging_s3_uri` is specified.  
`AWS_SECRET_ACCESS_KEY` |  For the `aws_secret_access_key` parameter, specify the [secret access key](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#snowflake_key_pair) paired with `aws_access_key_id`. Include this parameter when `staging_s3_uri` is specified.  
`AZURE_STORAGE_ACCOUNT` |  For the `azure_storage_account` parameter, specify the [Azure storage account name](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#azure_3) used to stage unloaded data. Include this parameter for private data transfers when `cloud_provider` is `AZURE` and `staging_gcs_uri` isn't specified. You can't modify this parameter after you create the transfer configuration.  
`STAGING_AZURE_CONTAINER` |  For the `staging_azure_container` parameter, specify the [Azure Blob Storage container name](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#azure_3) in the Azure storage account. Include this parameter when `azure_storage_account` is specified. You can't modify this parameter after you create the transfer configuration.  
`AZURE_SAS_TOKEN` |  For the `azure_sas_token` parameter, specify the [shared access signature (SAS) token](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#azure_sas_token) used to authenticate read requests to the Azure Blob Storage container. Include this parameter when `azure_storage_account` is specified.  
`STORAGE_INTEGRATION_NAME` |  Specify the name of the Snowflake storage integration object. For example, `STORAGE_INTEGRATION_NAME`.  
`MAX_FILE_SIZE_MB` |  Optional: Specify the maximum size, in MB, of each file unloaded from Snowflake to the staging location. The value must be between `16` and `5120`. The default value is `512`.  
`USE_PRIVATE_NETWORK` |  Optional: If you are creating a [private data transfer](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity), set to `true`. The default value is `false`. You can't modify this parameter after you create the transfer configuration.  
`SERVICE_ATTACHMENT_URI` |  Optional: If you are creating a private data transfer, specify the service attachment URI for private connectivity to Snowflake. For more information, see [Create a private Snowflake transfer configuration](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#create-transfer-config). For example, `projects/PROJECT_ID/regions/REGION/serviceAttachments/SERVICE_ATTACHMENT`.  
`SERVICE_DIRECTORY_LINK` |  Optional: If you are creating a private data transfer from an `AWS`\- or `AZURE`-hosted Snowflake account, specify the Service Directory service self-link for the network load balancer. For more information, see [Create a private Snowflake transfer configuration](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-private-connectivity#create-transfer-config). For example, `projects/PROJECT_ID/locations/LOCATION/namespaces/NAMESPACE/services/SERVICE_NAME`.  
`INGESTION_TYPE` |  Specify the ingestion mode for the transfer. Supported values are `Full` and `Incremental`. For more information, see [Configure incremental transfers](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-incremental#configure_incremental_transfers).  
`SPECIFY_TRANSLATION_OUTPUT` |  Optional: Specify `true` when providing a path in the `translation_output_gcs_path` parameter so that the path is displayed in the Google Cloud console. The default value is `false`.  
`TRANSLATION_OUTPUT_GCS_PATH` |  Optional: Specify a path to the Cloud Storage folder that contains the [schema mapping files from the translation engine](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema). Leave this parameter unset to have the Snowflake connector automatically detect your schema.

  * The path must follow the format `gs://TRANSLATION_BUCKET_BASE_URI/metadata/config/DATABASE_NAME/SCHEMA_NAME/` and must end with a forward slash (`/`).

For example, `gs://sf_test_translation/output/metadata/config/database_name/schema_name/`.  
`CUSTOM_SCHEMA_PATH` |  Optional: If you are using a custom schema, specify the path to the custom schema file in Cloud Storage. For example, `gs://bucket_name/schemas/custom_schema.json`.  
`CONVERT_NUMBER_TO_INT64` |  Optional: Specify `true` to map Snowflake `NUMBER(p, 0)` data types to BigQuery `INT64`. Otherwise, Snowflake `NUMBER` data types are mapped to BigQuery `NUMERIC` or `BIGNUMERIC` depending on their precision and scale. The default value is `false`.  
**Note:** You can't configure notifications using the command-line tool.

###  API 

Use the [`projects.locations.transferConfigs.create`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs/create) method and supply an instance of the [`TransferConfig`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs#TransferConfig) resource.

For full transfers (when `ingestion_type` is `Full`), if you create multiple transfers for the same Snowflake tables or run the same transfer configuration multiple times, the transfer overwrites the data in the existing BigQuery destination tables.

### Configure a Snowflake transfer for schema mapping

The BigQuery Data Transfer Service supports three schema mapping methods for Snowflake transfers, automatic schema detection, translation engine output, and manual schema mapping. For more information, see [Schema detection and mapping reference](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema).

To see an example of a transfer configuration that supports each of these schema mapping methods, select one of the following options:

###  Automatic detection 

[Automatic schema detection reference](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema#enable_automatic_default_schema_detection) automatically maps Snowflake data types to equivalent BigQuery data types without requiring external metadata or schema definition files.

The following command shows how to create a transfer configuration that uses automatic schema detection:
    
    
    bq mk \
      --transfer_config \
      --project_id=PROJECT_ID \
      --data_source=snowflake_migration \
      --target_dataset=DATASET_NAME \
      --display_name='Snowflake Auto Detection Transfer' \
      --params='{
        "account_identifier": "ACCOUNT_IDENTIFIER",
        "username": "MIGRATION_USER",
        "auth_mechanism": "KEY_PAIR",
        "private_key": "PRIVATE_KEY_STRING",
        "service_account": "SERVICE_ACCOUNT_EMAIL",
        "warehouse": "WAREHOUSE_NAME",
        "database": "DATABASE_NAME",
        "schema": "SCHEMA_NAME",
        "table_name_patterns": "orders;lineitem",
        "cloud_provider": "GCP",
        "staging_gcs_uri": "gs://STAGING_BUCKET_NAME/staging/",
        "storage_integration_object_name": "STORAGE_INTEGRATION_NAME",
        "ingestion_type": "Full"
      }'

###  Translation output 

Uses metadata and schema mapping generated by the BigQuery [batch SQL translator](https://docs.cloud.google.com/bigquery/docs/migration/batch-sql-translator) to handle complex table and data type mappings. For more information, see [Translation output schema configuration](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema#manually_define_schema_using_translation_engine_output).

**Note:** The `table_name_patterns` parameter is required. Specify `.*` to transfer all tables in the schema, or specify semicolon-separated table names or regular expression patterns, such as `orders;lineitem`, to transfer a subset of tables.

The following command shows how to create a transfer configuration that uses the output from the translation engine for schema mapping:
    
    
    bq mk \
      --transfer_config \
      --project_id=PROJECT_ID \
      --data_source=snowflake_migration \
      --target_dataset=DATASET_NAME \
      --display_name='Snowflake Translation Output Transfer' \
      --params='{
        "account_identifier": "ACCOUNT_IDENTIFIER",
        "username": "MIGRATION_USER",
        "auth_mechanism": "KEY_PAIR",
        "private_key": "PRIVATE_KEY_STRING",
        "service_account": "SERVICE_ACCOUNT_EMAIL",
        "warehouse": "WAREHOUSE_NAME",
        "database": "DATABASE_NAME",
        "schema": "SCHEMA_NAME",
        "table_name_patterns": "orders;lineitem",
        "cloud_provider": "GCP",
        "staging_gcs_uri": "gs://STAGING_BUCKET_NAME/staging/",
        "storage_integration_object_name": "STORAGE_INTEGRATION_NAME",
        "ingestion_type": "Full",
        "specify_translation_output": true,
        "translation_output_gcs_path": "gs://TRANSLATION_BUCKET/output/metadata/config/DATABASE_NAME/SCHEMA_NAME/"
      }'

###  Custom schema 

Provide a [custom JSON schema file](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer-schema#custom_schema_file) in Cloud Storage to rename columns, customize data types, or designate primary keys.

The following command shows how to create a transfer configuration that uses a custom schema for schema mapping:
    
    
    bq mk \
      --transfer_config \
      --project_id=PROJECT_ID \
      --data_source=snowflake_migration \
      --target_dataset=DATASET_NAME \
      --display_name='Snowflake Custom Schema Transfer' \
      --params='{
        "account_identifier": "ACCOUNT_IDENTIFIER",
        "username": "MIGRATION_USER",
        "auth_mechanism": "KEY_PAIR",
        "private_key": "PRIVATE_KEY_STRING",
        "service_account": "SERVICE_ACCOUNT_EMAIL",
        "warehouse": "WAREHOUSE_NAME",
        "database": "DATABASE_NAME",
        "schema": "SCHEMA_NAME",
        "table_name_patterns": "orders;lineitem",
        "cloud_provider": "GCP",
        "staging_gcs_uri": "gs://STAGING_BUCKET_NAME/staging/",
        "storage_integration_object_name": "STORAGE_INTEGRATION_NAME",
        "ingestion_type": "Full",
        "custom_schema_file_path": "gs://CONFIG_BUCKET/schemas/custom_schema.json"
      }'

## Specify encryption key with transfers

You can specify [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek) to encrypt data for a transfer run. You can use a CMEK to support transfers from [Snowflake](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-migration-intro). 

When you specify a CMEK with a transfer, the BigQuery Data Transfer Service applies the CMEK to any intermediate on-disk cache of ingested data so that the entire data transfer workflow is CMEK compliant.

You cannot update an existing transfer to add a CMEK if the transfer was not originally created with a CMEK. For example, you cannot change a destination table that was originally default encrypted to now be encrypted with CMEK. Conversely, you also cannot change a CMEK-encrypted destination table to have a different type of encryption.

You can update a CMEK for a transfer if the transfer configuration was originally created with a CMEK encryption. When you update a CMEK for a transfer configuration, the BigQuery Data Transfer Service propagates the CMEK to the destination tables at the next run of the transfer, where the BigQuery Data Transfer Service replaces any outdated CMEKs with the new CMEK during the transfer run. For more information, see [Update a transfer](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#update_a_transfer).

You can also use [project default keys](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption#project_default_key). When you specify a project default key with a transfer, the BigQuery Data Transfer Service uses the project default key as the default key for any new transfer configurations.

**Note:** For Snowflake transfers, CMEK encryption handles encryption of the data in the BigQuery destination tables as well as encryption of data in the intermediate Cloud Storage tenant bucket used during the transfer process for Snowflake on Amazon S3 or Azure Blob Storage.

## Quotas and limits

BigQuery has a load quota of 15 TB for each load job for each table by default. Internally, Snowflake compresses the table data, so the exported table size is larger than the table size reported by Snowflake.

To improve load times for larger tables and to remove the 15TB BigQuery load limit, specify the [`PIPELINE` job type](https://docs.cloud.google.com/bigquery/docs/migration/snowflake-transfer#quotas_and_limits) for your reservation assignment.

Because of [Amazon S3's consistency model](https://docs.cloud.google.com/bigquery/docs/s3-transfer-intro#consistency_considerations), it's possible that some files won't be included in the transfer to BigQuery.

## Optimize data transfer performance

You can monitor the performance of your data transfers by viewing the [logs for the data transfer](https://docs.cloud.google.com/bigquery/docs/dts-monitor). To improve the performance of your data transfers, we recommend that you perform the following optimization steps:

  * Keep your Snowflake instance, staging bucket, and BigQuery dataset in the same region
  * You can improve table unload speeds by doing the following: 
    * Increase the size of your Snowflake virtual warehouse, especially when transferring large Snowflake tables (1 TiB or higher).
    * Adjust the `MAX_FILE_SIZE` option in the transfer configuration. 
      * Smaller file sizes can improve transfer speeds, but making it too small can lead to too many files.
  * You can improve table load speeds by increasing the number of BigQuery slot reservations for `PIPELINE` and `QUERY` job types.
  * When making a full transfer, avoid clustering and partitioning on the destination BigQuery table.
  * When making an incremental transfer in Upsert mode, consider clustering and partitioning on primary key columns to improve transfer performance. 
    * However, avoid clustering and partitioning on non-primary key columns to prevent slower merge operations.



## Pricing

For information on BigQuery Data Transfer Service pricing, see the [Pricing](https://cloud.google.com/bigquery/pricing#data-transfer-service-pricing) page.

  * If the Snowflake warehouse and the Amazon S3 bucket are in different regions, then Snowflake applies egress charges when you run a Snowflake data transfer. There are no egress charges for Snowflake data transfers if both the Snowflake warehouse and the Amazon S3 bucket are in the same region.
  * When data is transferred from AWS to Google Cloud, inter-cloud egress charges are applied. 



## What's next

  * Learn more about the [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/transfer-service-overview).
  * Migrate SQL code with the [Batch SQL translation](https://docs.cloud.google.com/bigquery/docs/batch-sql-translator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
