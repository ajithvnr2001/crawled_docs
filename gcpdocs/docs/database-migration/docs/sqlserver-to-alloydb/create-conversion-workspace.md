---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-conversion-workspace/
title: Create a conversion workspace and convert schema \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:55:04.698762+00:00
---

# Create a conversion workspace and convert schema  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-conversion-workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Create a conversion workspace and convert schema Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create a conversion workspace and use it to immediately perform deterministic code and schema conversion from SQL Server to PostgreSQL.

You can create interactive conversion workspaces in two ways:

  * **Through a direct database connection:** Database Migration Service connects directly to your running source database through a connection profile and retrieves the schema over a network connection.

  * **With schema files in Cloud Storage:** You can extract your schema metadata locally using Google-provided extraction scripts, upload the resulting files to a Cloud Storage bucket, and prepare your workspace without connecting to the source database.




## Connect directly to the source database

You can create an interactive conversion workspace and perform the schema conversion by connecting directly to the source database with Database Migration Service. Before you create the workspace in this way, make sure that you [ create a connection profile for your source database](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile).

### Required roles for the direct connection method

To get the permissions that you need to create a conversion workspace, ask your administrator to grant you the [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) IAM role on your project.

For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation.

This predefined role contains the permissions required to create a conversion workspace in Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a conversion workspace in Database Migration Service: 

  * `cloudaicompanion.entitlements.get`

This permission is included in the `roles/datamigration.admin` role. It is required for the [ Gemini-enhanced conversion features](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/code-conversion-with-gemini). 

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
     2. From the **Source database engine** drop-down menu, select your source SQL Server database. 
     3. From the **Destination database engine** select **AlloyDB for PostgreSQL**. 
     4. In the **Enable Gemini settings for your workspace** section, use the checkboxes to enable Gemini-powered conversion features. You can also enable these features later when you want to [ Convert code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/code-conversion-with-gemini). 

Gemini-powered conversion features require the Gemini for Google Cloud API. For more information, see [ Gemini-powered conversion features](https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms#gemini-conversion). 

     5. Click **Create workspace and continue**.
  4. On the **Define source and pull schema snapshot** page, do the following: 
     1. In the **Source connection method** section, select **Connection profile**. 
     2. From the **Source connection profile** drop-down menu, select the connection profile for your source database. 
     3. Click **Pull schema snapshot and continue**.

Database Migration Service is now connecting to the source database and retrieving your schema. This process can take several minutes. 

  5. On the **Select and convert objects** page, use the checkboxes to select which objects you want to convert to PostgreSQL syntax. 

You don't have to convert all your objects in one go. Instead, you can select just a few objects now and [ add more objects to the conversion](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/work-with-conversion-workspaces#add-source-objects) later. 

  6. Click **Convert and continue**. 

The conversion workspace opens.




## Use schema files stored in Cloud Storage

You can extract your schema metadata locally using Google-provided extraction scripts, upload the resulting files to a Cloud Storage bucket, and prepare your workspace without connecting to the source database.

### Required roles for using the schema files in Cloud Storage

To get the permissions that you need to create a conversion workspace using schema files stored in Cloud Storage, ask your administrator to grant the required IAM roles on your project for the following [ accounts involved in the migration process](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/access-control):

  * User account that creates the conversion workspace: [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * Database Migration Service service account: [ Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) role on the Cloud Storage bucket that stores the schema files. 

The email address of the Database Migration Service service account uses the following format: `service-PROJECT_NUMBER@gcp-sa-datamigration.iam.gserviceaccount.com`. Replace PROJECT_NUMBER with your Google Cloud project number. For more information about this service account, see [ Database Migration Service service account](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/access-control#dms_sa). 




For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation.

The `roles/datamigration.admin` predefined role contains the permissions required to create a conversion workspace in Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a conversion workspace in Database Migration Service: 

  * `cloudaicompanion.entitlements.get`

This permission is included in the `roles/datamigration.admin` role. It is required for the [ Gemini-enhanced conversion features](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/code-conversion-with-gemini). 

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
        2. From the **Source database engine** drop-down menu, select your source SQL Server database.
        3. From the **Destination database engine** drop-down menu, select **AlloyDB for PostgreSQL**.
        4. In the **Enable Gemini settings for your workspace** section, use the checkboxes to enable Gemini-powered conversion features and click **Continue**. 

You can also enable these features later when you want to [ Convert code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/code-conversion-with-gemini). Gemini-powered conversion features require the Gemini for Google Cloud API. For more information, see [ Gemini-powered conversion features](https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms#gemini-conversion). 

     4. On the **Define source and pull schema snapshot** page, in the **Source connection method** section, select **Cloud Storage**. 
     5. In the **Before selecting a folder** section, next to the **SQL Server metadata extractor** heading, click **Open**. Follow the instructions in the side panel to download and run the extraction utility against your source database to produce the schema metadata JSON files. This utility requires that you are able to establish a network connection with your source database. 
  2. Create a dedicated Cloud Storage bucket where you upload the schema metadata JSON files. For more information about creating Cloud Storage buckets, see [ Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) in the Cloud Storage documentation. 
  3. Inside the dedicated Cloud Storage bucket, create an empty, dedicated folder for the database schema files you exported in the previous steps. For more information about creating Cloud Storage folders, see [ Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders) in the Cloud Storage documentation. 
  4. Upload only the metadata JSON schema files you created with the Python scripts you retrieved from the Google Cloud console in the previous steps to the empty, dedicated database folder in your Cloud Storage bucket. 
  5. Continue creating your workspace in the Google Cloud console, or create a new one with Google Cloud CLI. 

### Console

     1. After you upload the extracted schema metadata files to a Cloud Storage bucket, continue on the **Define source and pull schema snapshot** page. 
     2. In the **Folder** field, click **Browse** , and select the folder that contains your schema files. 
     3. Click **Pull schema snapshot and continue**. 

Database Migration Service now parses the schema metadata from the bucket.

     4. On the **Select and convert objects** page, select the objects you want to convert and click **Convert and continue**. 

### gcloud

After you upload the extracted schema metadata files to a Cloud Storage bucket, you can create and initialize a new workspace with Google Cloud CLI. Follow these steps: 

     1. Create an empty conversion workspace.  
Run the following command (click to expand):

#### `gcloud database-migration conversion-workspaces create`
            
            gcloud database-migration conversion-workspaces create WORKSPACE_ID \
                  --region=REGION \
                  --source-database-engine=SQLSERVER \
                  --destination-database-engine=POSTGRESQL

Replace the following:

        * WORKSPACE_ID: With the identifier for your conversion workspace.
        * REGION: The region where you want to create the workspace.

     2. Initialize the workspace using your schema files in Cloud Storage.   
To parse and load the schema metadata files stored in your bucket into the conversion workspace, run the following command (click to expand):

#### `gcloud database-migration conversion-workspaces seed`
            
            gcloud database-migration conversion-workspaces seed WORKSPACE_ID \
                  --region=REGION \
                  --gcs-path=gs://BUCKET_NAME/PREFIX/

Replace the following:

        * WORKSPACE_ID: With the identifier for your conversion workspace.
        * REGION: The region where you want to create the workspace.
        * BUCKET_NAME: The name of the Cloud Storage bucket containing your schema files.
        * PREFIX: The path to the folder containing the extracted schema metadata files.




## What's next

You can now work with your conversion workspace to fix conversion issues, modify your objects with the interactive editor, and apply converted schema to your destination database. See [ Convert SQL Server code and schema to PostgreSQL syntax](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/convert-sql).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
