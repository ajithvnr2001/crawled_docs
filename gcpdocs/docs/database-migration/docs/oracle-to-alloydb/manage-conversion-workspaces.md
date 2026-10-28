---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/
title: Manage conversion workspaces \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:04:13.802103+00:00
---

# Manage conversion workspaces  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/

[ Skip to main content ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/)
  * [Deutsch](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=de)
  * [Español](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=id)
  * [Italiano](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=it)
  * [Português](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdatabase-migration%2Fdocs%2Foracle-to-alloydb%2Fmanage-conversion-workspaces%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [View conversion workspace details](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#view-details)
  * [Modify conversion workspace settings](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#edit-workspace)
  * [Delete a conversion workspace](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#delete_a_conversion_workspace)
  * [Review all conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#review-details)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)


Was this helpful?
Send feedback 
#  Manage conversion workspaces Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [View conversion workspace details](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#view-details)
  * [Modify conversion workspace settings](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#edit-workspace)
  * [Delete a conversion workspace](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#delete_a_conversion_workspace)
  * [Review all conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#review-details)


This page describes how to manage multiple conversion workspaces in your projects. From the list of conversion workspaces, you can:
  * Select a specific conversion workspace to access the conversion editor, view and modify workspace details, apply generated schema and code to your destination database, and create a migration job.
  * Use the more_vert**More** menu to delete a workspace.


## View conversion workspace details
To view conversion workspace details, use the **Conversion workspaces** page in the Google Cloud console or Google Cloud CLI.
[ Console ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#console)[ gcloud ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#gcloud) More
  1. In the Google Cloud console, go to **Conversion workspaces**.


[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)
  1. From the list of available workspaces, select the one you want to work with.
Conversion workspace editor page appears.
  2. Select **Edit configuration** > **View details**.


The **Conversion workspace details** panel opens.
  1. List all workspaces available in a particular region to retrieve their identifiers:

```
gcloud database-migration conversion-workspaces list \
    --region=REGION

```

Replace:
     * `REGION` with the name of the region where the conversion workspace is located.
Example:

```
gcloud database-migration conversion-workspaces list \
    --region=us-central1

```

The list of available workspaces and their identifiers is printed to standard output.
  2. Retrieve details for a specific workspace:

```
gcloud database-migration conversion-workspaces describe CONVERSION_WORKSPACE \
  --region=REGION

```

Replace:
     * `CONVERSION_WORKSPACE` with the identifier or the fully qualified name of the conversion workspace
     * `REGION` with the name of the region where the conversion workspace is located.
Example:

```
gcloud database-migration conversion-workspaces describe my-conversion-workspace-id \
  --region=us-central1

```



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
[Edit connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#edit-connection-profile)[Edit Cloud Storage](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-conversion-workspaces/#edit-cloud-storage) More
If your workspace connects directly to the source database using a connection profile, you can either adjust the settings of the existing connection profile, or change the workspace source configuration to use a different connection profile or switch in-flight to provide schema files stored in a Cloud Storage bucket: 
     * To adjust the connection settings of your existing source connection profile: 
       1. Select **Edit configuration** > **View details**.
       2. In the **Source connection profile** row, click the link to the connection profile associated with the workspace. 
       3. On the connection profile page, adjust any details as required. For more information, see [ Manage connection profiles](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage_connection-profiles). 
     * To select a different connection profile or switch in-flight to use schema files stored in a Cloud Storage bucket: 
       1. Select **Edit configuration** > **Edit source configuration**.
       2. In the confirmation dialog, click **Edit profile**.
       3. On the **Define source and pull schema snapshot** page, select a different source connection profile or select **Cloud Storage** and specify a folder path, click **Pull schema snapshot and continue** , and select the objects to convert. 
If your workspace uses schema files stored in Cloud Storage, you can change the source configuration to point to a different Cloud Storage folder, or switch in-flight to provide schema files through a direct connection using a connection profile: 
    1. Select **Edit configuration** > **Edit source configuration**.
    2. In the confirmation dialog, click **Edit profile**.
    3. On the **Define source and pull schema snapshot** page, select a different **Cloud Storage** folder path or select **Connection profile** to connect directly to your source database, click **Pull schema snapshot and continue** , and select the objects to convert. 
  5. You can also modify what custom conversion mapping files are used in your workspace. For more information, see [ Use custom conversion mappings](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/work-with-conversion-workspaces#use-custom-mappings). 


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


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
