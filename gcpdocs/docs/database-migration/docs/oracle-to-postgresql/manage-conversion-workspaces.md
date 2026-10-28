---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/manage-conversion-workspaces/
title: Manage conversion workspaces \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T18:09:37.786951+00:00
---

# Manage conversion workspaces  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/manage-conversion-workspaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Manage conversion workspaces Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage multiple conversion workspaces in your projects. From the list of conversion workspaces, you can:

  * Select a specific conversion workspace to access the conversion editor, view and modify workspace details, apply generated schema and code to your destination database, and create a migration job.

  * Use the more_vert**More** menu to delete a workspace.




## View conversion workspace details

To view conversion workspace details, use the **Conversion workspaces** page in the Google Cloud console or Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to **Conversion workspaces**.



[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  1. From the list of available workspaces, select the one you want to work with.

Conversion workspace editor page appears.

  2. Select **Edit configuration** > **View details**.




The **Conversion workspace details** panel opens.

###  gcloud 

  1. List all workspaces available in a particular region to retrieve their identifiers:
         
         gcloud database-migration conversion-workspaces list \
             --region=REGION
         

Replace:

     * `REGION` with the name of the region where the conversion workspace is located.

Example:
    
    gcloud database-migration conversion-workspaces list \
        --region=us-central1
    

The list of available workspaces and their identifiers is printed to standard output.

  2. Retrieve details for a specific workspace:
         
         gcloud database-migration conversion-workspaces describe CONVERSION_WORKSPACE \
           --region=REGION
         

Replace:

     * `CONVERSION_WORKSPACE` with the identifier or the fully qualified name of the conversion workspace

     * `REGION` with the name of the region where the conversion workspace is located.

Example:
    
    gcloud database-migration conversion-workspaces describe my-conversion-workspace-id \
      --region=us-central1
    




## Modify conversion workspace settings

Information that you can modify for a conversion workspace includes the display name, the source configuration (the source connection profile or Cloud Storage folder), and custom conversion mapping files.

  1. Go to the **Conversion workspaces** page in the Google Cloud console: 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click the display name of the conversion workspace that you want to modify. 

The conversion workspace editor opens.

  3. To modify the workspace display name: 
     1. Select **Edit configuration** > **View details**. The **Conversion workspace details** panel opens. 
     2. In the **Conversion workspace name** row, click the edit**edit** icon. 
     3. In the **Conversion workspace name** field, enter the new display name for the conversion workspace. 
     4. Click **Save**.
  4. To modify the source configuration for your workspace: 

### Edit connection profile

If your workspace connects directly to the source database using a connection profile, you can either adjust the settings of the existing connection profile, or change the workspace source configuration to use a different connection profile or switch in-flight to provide schema files stored in a Cloud Storage bucket: 

     * To adjust the connection settings of your existing source connection profile: 
       1. Select **Edit configuration** > **View details**.
       2. In the **Source connection profile** row, click the link to the connection profile associated with the workspace. 
       3. On the connection profile page, adjust any details as required. For more information, see [ Manage connection profiles](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/manage_connection-profiles). 
     * To select a different connection profile or switch in-flight to use schema files stored in a Cloud Storage bucket: **Caution:** Editing the source configuration removes all selected objects, clears the draft schema, and resets any existing custom mappings and DDL modifications in the workspace. 
       1. Select **Edit configuration** > **Edit source configuration**.
       2. In the confirmation dialog, click **Edit profile**.
       3. On the **Define source and pull schema snapshot** page, select a different source connection profile or select **Cloud Storage** and specify a folder path, click **Pull schema snapshot and continue** , and select the objects to convert. 

### Edit Cloud Storage

If your workspace uses schema files stored in Cloud Storage, you can change the source configuration to point to a different Cloud Storage folder, or switch in-flight to provide schema files through a direct connection using a connection profile: 

**Caution:** Editing the source configuration removes all selected objects, clears the draft schema, and resets any existing custom mappings and DDL modifications in the workspace. If you only want to refresh the schema from the same Cloud Storage folder while preserving your customizations, upload the updated files to the same folder and use **Pull source schema snapshot again** instead. For more information, see [ Pull source schema and code snapshot](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces#pull-snapshot). 
     1. Select **Edit configuration** > **Edit source configuration**.
     2. In the confirmation dialog, click **Edit profile**.
     3. On the **Define source and pull schema snapshot** page, select a different **Cloud Storage** folder path or select **Connection profile** to connect directly to your source database, click **Pull schema snapshot and continue** , and select the objects to convert. 

  5. You can also modify what custom conversion mapping files are used in your workspace. For more information, see [ Use custom conversion mappings](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces#use-custom-mappings). 



## Delete a conversion workspace

You can delete a conversion workspace only if it's not used by active migration jobs.

To delete a conversion workspace that's linked to active migration jobs, first, delete all active migration jobs that are linked to the conversion workspace. Then, delete the conversion workspace.

  1. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Next to the conversion workspace you want to delete, click more_vert**More** > **Delete**.

  3. In the dialog confirmation box, click **Delete**.




## Review all conversion workspaces

You can review all conversion workspaces from the [ ](https://console.cloud.google.com/dbmigration/conversion-workspaces) page. The list displays a default set of high-level information for each conversion workspace, including:

  * The conversion workspace **display name** and **ID**.
  * The **version ID** of the most-recent version of the conversion workspace that's saved. By having multiple versions of a conversion workspace, you can compare objects in each workspace and identify differences between the workspaces. Versioning can also be used for tracking purposes.
  * The **conversion state** that represents whether this conversion workspace was used to pull objects from the source and convert them. 
  * **Activity** indicates if the conversion workspace is in use by one or more active migration jobs, where an active migration job is any migration job that's not in `COMPLETED` status. The number of jobs next to the status indicates the total number of jobs (both active and inactive) referencing the conversion workspace.
  * The **source** and **destination** database engines (database types) for which the conversion workspace is configured.
  * When the conversion workspace was **created**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
