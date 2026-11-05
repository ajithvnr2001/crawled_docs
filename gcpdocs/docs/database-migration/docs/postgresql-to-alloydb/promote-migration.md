---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/promote-migration/
title: Promote a migration job \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T11:11:14.227346+00:00
---

# Promote a migration job  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/promote-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Promote a migration job Stay organized with collections  Save and categorize content based on your preferences. 

For continuous migrations, you can initiate the promotion process when you are ready to cut over your applications to the destination databases. Promoting the migration job disconnects the destination AlloyDB for PostgreSQL cluster from the source and transforms it into an independent standalone primary cluster so you can direct application traffic to the cluster. 

  1. Stop all writes, running scripts, and client connections to the source database. The cutover downtime window begins here. 
  2. Wait until the [ replication delay metric](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-metrics) is at or close to zero. This ensures that the migration job has processed all outstanding changes from the source. 

You can promote a migration even if the replication delay isn't at zero. This can reduce database cutover time, but might affect data currency in the destination. 

  3. Perform the promote action: 

### Console

     1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

     2. On the **Jobs** tab, click the display name of the migration job that you want to promote. 

The migration job details page opens.

     3. On the migration job toolbar, click **Promote**. 

The promote migration job dialog appears.

     4. In the dialog, ensure that no errors are displayed, and then click **Promote**.

### gcloud

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

     * REGION with the identifier of the region where your migration job is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    promote MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    promote MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    promote MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The action is performed in an asynchronous manner. As such, this command returns an [ Operation entity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations) that represents a long-running operation: 
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata
      apiVersion: v1
      createTime: '2024-02-20T12:20:24.493106418Z'
      requestedCancellation: false
      target: MIGRATION_JOB_ID
      verb: promote
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

     * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
     * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.

  4. The destination AlloyDB for PostgreSQL cluster is promoted. The destination cluster is disconnected from the source, becomes an independent standalone primary cluster, and is ready for full application traffic. The migration job status changes to `Completed`. 
  5. (Optional) **Re-install extensions:** If your source database used extensions that aren't migrated by Database Migration Service (such as [`pg_cron`](https://docs.cloud.google.com/alloydb/docs/reference/extensions#pg_cron)), re-install and configure those extensions on your destination cluster. 
  6. You can now connect your applications to the AlloyDB for PostgreSQL cluster and delete the completed migration job. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
