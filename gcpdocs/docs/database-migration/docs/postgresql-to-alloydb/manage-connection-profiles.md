---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/manage-connection-profiles/
title: Manage connection profiles \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T11:35:58.375517+00:00
---

# Manage connection profiles  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/manage-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Manage connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to perform view, update, and delete operations for connection profiles.

## View a connection profile

You can view the following information about your connection profiles:

  * All configuration details provided during profile creation. For more information, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-connection-profiles).

  * Connection profile creation and last modification time.

  * A list of migration jobs that use this connection profile.




To view connection profile details, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click the display name of the connection profile that you want to view. 

A connection profile overview page appears.




### gcloud

Before using any of the command data below, make the following replacements: 

  * REGION with the identifier of the region where your connection profile is saved.
  * CONNECTION_PROFILE_ID with your connection profile identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration connection-profiles list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/list) command to list all profiles in a given region and view their identifiers. 


For more information on these values, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-connection-profiles). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    describe CONNECTION_PROFILE_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    describe CONNECTION_PROFILE_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    describe CONNECTION_PROFILE_ID ^
      --region=REGION

## Update a connection profile

You can modify the following connection profile details:

  * Display name
  * **For source connection profiles** : hostname or IP address, port, username, password, database name, and SSL/TLS certificates
  * **For destination connection profiles (existing cluster only)** : destination AlloyDB for PostgreSQL cluster identifier



To update a connection profile, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click the display name of the connection profile that you want to modify. 

An overview page appears for the connection profile.

  3. Click **Edit** and update your connection profile.
  4. Click **Save**.



### gcloud

Before using any of the command data below, make the following replacements: 

  * CONNECTION_PROFILE_ID with your connection profile identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration connection-profiles list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/list) command to list all profiles in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.
  * Optional: CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in the Google Cloud console. 
  * **For source connection profiles** : you can also pass flags such as `--host`, `--port`, `--username`, and `--password` to update your source database connection details. For the full list of supported flags, see the [ `gcloud database-migration connection-profiles update`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update) reference. 
  * **For destination connection profiles (existing cluster only)** : ALLOYDB_CLUSTER_ID with the cluster identifier of your destination AlloyDB for PostgreSQL cluster. For information on how to view AlloyDB for PostgreSQL cluster details, see [ View cluster details](https://docs.cloud.google.com/alloydb/docs/instance-view) in the AlloyDB for PostgreSQL documentation. 

For more information on these values, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-connection-profiles). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    update CONNECTION_PROFILE_ID \
      --region=REGION \
      --display-name=CONNECTION_PROFILE_NAME \
      --alloydb-cluster=ALLOYDB_CLUSTER_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    update CONNECTION_PROFILE_ID `
      --region=REGION `
      --display-name=CONNECTION_PROFILE_NAME `
      --alloydb-cluster=ALLOYDB_CLUSTER_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    update CONNECTION_PROFILE_ID ^
      --region=REGION ^
      --display-name=CONNECTION_PROFILE_NAME ^
      --alloydb-cluster=ALLOYDB_CLUSTER_ID

#### Result

The action is performed in an asynchronous manner. As such, this command returns an [ Operation entity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations) that represents a long-running operation: 
    
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata
      apiVersion: v1
      createTime: '2024-02-20T12:20:24.493106418Z'
      requestedCancellation: false
      target: CONNECTION_PROFILE_ID
      verb: update
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the connection profile details: 

  * Use the [ `gcloud database-migration connection-profiles describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/describe) command to view the updated connection profile details.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.



## Delete a connection profile

You can delete a connection profile only if there are no migration jobs that use that profile. If you want to delete a connection profile that is in use by a migration job, first [ delete all migration jobs](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions#delete) that are linked to the connection profile.

To delete a connection profile, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click the display name of the connection profile that you want to delete. 

A connection profile overview page appears.

  3. Click **Delete**.
  4. In the dialog, click **Delete**.



### gcloud

This command returns an interactive confirmation prompt that requires your input to complete. You can skip the confirmation prompt by using the [ optional `--quiet` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet).

Before using any of the command data below, make the following replacements: 

  * REGION with the identifier of the region where your connection profile is saved.
  * CONNECTION_PROFILE_ID with your connection profile identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration connection-profiles list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/list) command to list all profiles in a given region and view their identifiers. 


For more information on these values, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-connection-profiles). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    delete CONNECTION_PROFILE_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    delete CONNECTION_PROFILE_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    delete CONNECTION_PROFILE_ID ^
      --region=REGION

**Result**

The `delete` command returns an interactive prompt where you confirm the action. Enter `Y` to remove the connection profile: 
    
    
    You are about to delete connection_profile [CONNECTION_PROFILE_ID]
    
    Do you want to continue (Y/n)?
    

You can skip Google Cloud CLI interactive confirmation prompts by using the [ optional `--quiet` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
