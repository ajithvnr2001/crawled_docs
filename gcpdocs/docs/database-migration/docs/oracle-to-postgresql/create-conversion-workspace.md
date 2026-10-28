---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/
title: Create a conversion workspace and convert schema \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:11:40.680994+00:00
---

# Create a conversion workspace and convert schema  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/

[ Skip to main content ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/)
  * [Deutsch](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/?hl=fr)
  * [Português – Brasil](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/?hl=pt-br)
  * [中文 – 简体](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/?hl=zh-cn)
  * [日本語](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdatabase-migration%2Fdocs%2Foracle-to-postgresql%2Fcreate-conversion-workspace%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Connect directly to the source database](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#connect-directly)
    * [Required roles for the direct connection method](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#required-roles)
    * [Create a conversion workspace with a connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#create-ws-connection-profile)
  * [Use schema files stored in Cloud Storage](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#use-cloud-storage)
    * [Required roles for using the schema files in Cloud Storage](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#required-roles-cloud-storage)
    * [Create a conversion workspace with schema files](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#create-ws-storage-schema-files)
  * [Legacy conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#legacy-ws)
  * [What's next](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)


Was this helpful?
Send feedback 
#  Create a conversion workspace and convert schema Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Connect directly to the source database](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#connect-directly)
    * [Required roles for the direct connection method](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#required-roles)
    * [Create a conversion workspace with a connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#create-ws-connection-profile)
  * [Use schema files stored in Cloud Storage](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#use-cloud-storage)
    * [Required roles for using the schema files in Cloud Storage](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#required-roles-cloud-storage)
    * [Create a conversion workspace with schema files](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#create-ws-storage-schema-files)
  * [Legacy conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#legacy-ws)
  * [What's next](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#whats-next)


This page shows you how to create a conversion workspace and use it to immediately perform deterministic code and schema conversion from Oracle to PostgreSQL.
You can create interactive conversion workspaces in two ways:
  * **Through a direct database connection:** Database Migration Service connects directly to your running source database through a connection profile and retrieves the schema over a network connection.
  * **With schema files in Cloud Storage:** You can extract your schema metadata locally using Google-provided extraction scripts, upload the resulting files to a Cloud Storage bucket, and prepare your workspace without connecting to the source database.


## Connect directly to the source database
You can create an interactive conversion workspace and perform the schema conversion by connecting directly to the source database with Database Migration Service. Before you create the workspace in this way, make sure that you [ create a connection profile for your source database](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-source-connection-profile).
### Required roles for the direct connection method
To get the permissions that you need to create a conversion workspace, ask your administrator to grant you the [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) IAM role on your project.
For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation.
This predefined role contains the permissions required to create a conversion workspace in Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 
Required permissions
The following permissions are required to create a conversion workspace in Database Migration Service: 
  * `cloudaicompanion.entitlements.get`
This permission is included in the `roles/datamigration.admin` role. It is required for the [ Gemini-enhanced conversion features](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini). 
  * `datamigration.conversionworkspaces.apply`
  * `datamigration.conversionworkspaces.commit`
  * `datamigration.conversionworkspaces.convert`
  * `datamigration.conversionworkspaces.create`
  * `datamigration.conversionworkspaces.delete`
  * `datamigration.conversionworkspaces.get`
  * `datamigration.conversionworkspaces.getIamPolicy`
  * `datamigration.conversionworkspaces.list`
  * `datamigration.conversionworkspaces.rollback`
  * `datamigration.conversionworkspaces.seed`
  * `datamigration.conversionworkspaces.setIamPolicy`
  * `datamigration.conversionworkspaces.update`


You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 
### Create a conversion workspace with a connection profile
To create a conversion workspace where Database Migration Service connects to your source database and prepares the initial snapshot of your source database objects, follow these steps:
  1. In the Google Cloud console, go to **Conversion workspaces**. 
[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)
  2. Click **Set up workspace**.
  3. On the **Create a conversion workspace** page, do the following: 
    1. Enter the name, identifier, and region for your conversion workspace.
    2. From the **Source database engine** drop-down menu, select **Oracle**. 
    3. From the **Destination database engine** select **Cloud SQL for PostgreSQL**. 
    4. In the **Enable Gemini settings for your workspace** section, use the checkboxes to enable Gemini-powered conversion features. You can also enable these features later when you want to [ Convert code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini). 
Gemini-powered conversion features require the Gemini for Google Cloud API. For more information, see [ Gemini-powered conversion features](https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms#gemini-conversion). 
    5. Click **Create workspace and continue**.
  4. On the **Define source and pull schema snapshot** page, do the following: 
    1. In the **Source connection method** section, select **Connection profile**. 
    2. From the **Source connection profile** drop-down menu, select the connection profile for your source database. 
    3. Click **Pull schema snapshot and continue**.
Database Migration Service is now connecting to the source database and retrieving your schema. This process can take several minutes. 
  5. On the **Select and convert objects** page, use the checkboxes to select which objects you want to convert to PostgreSQL syntax. 
You don't have to convert all your objects in one go. Instead, you can select just a few objects now and [ add more objects to the conversion](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces#add-source-objects) later. 
  6. Click **Convert and continue**. 
The conversion workspace opens.
  7. When you open a new workspace for the first time, you can upgrade it to access the Gemini-powered auto-conversion feature. Do the following: 
     * In the **Introducing Gemini auto-conversion** dialog, select the **Upgrade workspace to explore the new experience** checkbox, and click **Continue**. 
     * In the **Convert source objects with Gemini?** dialog, click **Convert**. 
Database Migration Service now performs the conversion process again to apply Gemini-powered conversion enhancements on top of the deterministic conversion results. For more information on Gemini auto-conversion feature, see [ Gemini auto-conversion](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini#auto-conversion). 


## Use schema files stored in Cloud Storage
You can extract your schema metadata locally using Google-provided extraction scripts, upload the resulting files to a Cloud Storage bucket, and prepare your workspace without connecting to the source database.
### Required roles for using the schema files in Cloud Storage
To get the permissions that you need to create a conversion workspace using schema files stored in Cloud Storage, ask your administrator to grant the required IAM roles on your project for the following [ accounts involved in the migration process](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/access-control):
  * User account that creates the conversion workspace: [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * Database Migration Service service account: [ Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) role on the Cloud Storage bucket that stores the schema files. 
The email address of the Database Migration Service service account uses the following format: `service-PROJECT_NUMBER@gcp-sa-datamigration.iam.gserviceaccount.com`. Replace PROJECT_NUMBER with your Google Cloud project number. For more information about this service account, see [ Database Migration Service service account](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/access-control#dms_sa). 


For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation.
The `roles/datamigration.admin` predefined role contains the permissions required to create a conversion workspace in Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 
Required permissions
The following permissions are required to create a conversion workspace in Database Migration Service: 
  * `cloudaicompanion.entitlements.get`
This permission is included in the `roles/datamigration.admin` role. It is required for the [ Gemini-enhanced conversion features](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini). 
  * `datamigration.conversionworkspaces.apply`
  * `datamigration.conversionworkspaces.commit`
  * `datamigration.conversionworkspaces.convert`
  * `datamigration.conversionworkspaces.create`
  * `datamigration.conversionworkspaces.delete`
  * `datamigration.conversionworkspaces.get`
  * `datamigration.conversionworkspaces.getIamPolicy`
  * `datamigration.conversionworkspaces.list`
  * `datamigration.conversionworkspaces.rollback`
  * `datamigration.conversionworkspaces.seed`
  * `datamigration.conversionworkspaces.setIamPolicy`
  * `datamigration.conversionworkspaces.update`


You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 
### Create a conversion workspace with schema files
To create a conversion workspace with schema files, follow these steps.
  1. Retrieve the Python scripts from the Google Cloud console. Follow these steps: 
    1. In the Google Cloud console, go to **Conversion workspaces**. 
[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)
    2. Click **Set up workspace**.
    3. On the **Create a conversion workspace** page: 
      1. Enter the workspace name, identifier, and region.
      2. From the **Source database engine** drop-down menu, select **Oracle**.
      3. From the **Destination database engine** drop-down menu, select **Cloud SQL for PostgreSQL**.
      4. In the **Enable Gemini settings for your workspace** section, use the checkboxes to enable Gemini-powered conversion features and click **Continue**. 
You can also enable these features later when you want to [ Convert code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini). Gemini-powered conversion features require the Gemini for Google Cloud API. For more information, see [ Gemini-powered conversion features](https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms#gemini-conversion). 
    4. On the **Define source and pull schema snapshot** page, in the **Source connection method** section, select **Cloud Storage**. 
    5. In the **Before selecting a folder** section, next to the **Oracle metadata extractor** heading, click **Open**. Follow the instructions in the side panel to download and run the extraction utility against your source database to produce the schema metadata JSON files. This utility requires that you are able to establish a network connection with your source database. 
  2. Create a dedicated Cloud Storage bucket where you upload the schema metadata JSON files. For more information about creating Cloud Storage buckets, see [ Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) in the Cloud Storage documentation. 
  3. Inside the dedicated Cloud Storage bucket, create an empty, dedicated folder for the database schema files you exported in the previous steps. For more information about creating Cloud Storage folders, see [ Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders) in the Cloud Storage documentation. 
  4. Upload only the metadata JSON schema files you created with the Python scripts you retrieved from the Google Cloud console in the previous steps to the empty, dedicated database folder in your Cloud Storage bucket. 
  5. Continue creating your workspace in the Google Cloud console, or create a new one with Google Cloud CLI. 
[Console](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#console)[gcloud](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/#gcloud) More
    1. After you upload the extracted schema metadata files to a Cloud Storage bucket, continue on the **Define source and pull schema snapshot** page. 
    2. In the **Folder** field, click **Browse** , and select the folder that contains your schema files. 
    3. Click **Pull schema snapshot and continue**. 
Database Migration Service now parses the schema metadata from the bucket.
    4. On the **Select and convert objects** page, select the objects you want to convert and click **Convert and continue**. 
After you upload the extracted schema metadata files to a Cloud Storage bucket, you can create and initialize a new workspace with Google Cloud CLI. Follow these steps: 
    1. Create an empty conversion workspace.  
Run the following command (click to expand):
`gcloud database-migration conversion-workspaces create` 
```
  gcloud database-migration conversion-workspaces create WORKSPACE_ID \
      --region=REGION \
      --source-database-engine=ORACLE \
      --destination-database-engine=POSTGRESQL
```

Replace the following:
       * WORKSPACE_ID: With the identifier for your conversion workspace.
       * REGION: The region where you want to create the workspace.
    2. Initialize the workspace using your schema files in Cloud Storage.   
To parse and load the schema metadata files stored in your bucket into the conversion workspace, run the following command (click to expand):
`gcloud database-migration conversion-workspaces seed` 
```
  gcloud database-migration conversion-workspaces seed WORKSPACE_ID \
      --region=REGION \
      --gcs-path=gs://BUCKET_NAME/PREFIX/
```

Replace the following:
       * WORKSPACE_ID: With the identifier for your conversion workspace.
       * REGION: The region where you want to create the workspace.
       * BUCKET_NAME: The name of the Cloud Storage bucket containing your schema files.
       * PREFIX: The path to the folder containing the extracted schema metadata files.


## Legacy conversion workspaces
Legacy conversion workspaces are an older, more limited type of conversion workspaces. We don't recommend using the legacy type of conversion workspaces for your migrations. If you need to use a legacy conversion workspace, expand the **Create a legacy conversion workspace and convert schema** section for more information.
Create a legacy conversion workspace and convert schema
Legacy conversion workspaces use Ora2Pg configuration files. Before you create a legacy conversion workspace, make sure you first create your Ora2Pg configuration outside Database Migration Service. For more information, see [ Work with legacy conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/legacy-conversion-workspaces). 
  1. In the Google Cloud console, go to **Conversion workspaces**. 
[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)
  2. Click **Set up workspace**.
  3. On the **Create a conversion workspace** page, do the following: 
    1. Enter the name, identifier, and region for your conversion workspace.
    2. From the **Source database engine** drop-down menu, select **Oracle**. 
    3. From the **Destination database engine** select **Cloud SQL for PostgreSQL**. 
    4. Expand the **Customize workspace configurations** section, and select the **Enable legacy conversion workspace** checkbox. 
    5. Click **Create workspace and continue**.
  4. On the **Connect to source and convert objects** page, do the following: 
    1. From the **Source connection profile** drop-down menu, select the connection profile for your source database. 
    2. In the **Configuration file** box, click **Browse** and use the system file picker to select your conversion mapping file. 
You can upload multiple conversion mapping files by clicking **Add file**. 
    3. In the **Convert the configuration** section, click **Pull schema and convert**. 
Database Migration Service is now connecting to the source database, retrieving your schema and converting it to the destination SQL schema according to the rules defined in your conversion mapping file. This process can take several minutes. 
  5. Click **Save and close**. 
The conversion workspace details page opens.


You can now apply the converted schema to your destination database. If your source database includes tables that don't have primary keys, you also need to manually create primary key constraints in the converted tables in the destination database after you apply the converted schema. For more information, see [ Work with legacy conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/legacy-conversion-workspaces). 
## What's next
You can now work with your conversion workspace to fix conversion issues, modify your objects with the interactive editor, and apply converted schema to your destination database. See [ Convert Oracle code and schema to PostgreSQL syntax](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/convert-sql).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
