---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance/
title: Create a migration job to an existing destination cluster \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:33:46.726461+00:00
---

# Create a migration job to an existing destination cluster  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Create a migration job to an existing destination cluster Stay organized with collections  Save and categorize content based on your preferences. 

When you migrate to an existing destination AlloyDB for PostgreSQL cluster, Database Migration Service demotes the destination cluster to configure it as an external replica. Demoting a cluster doesn't place AlloyDB for PostgreSQL in read-only mode, but executing certain operations during the migration process might result in migration errors. As you migrate to an existing destination cluster, keep the following operational considerations in mind: 

  * **Cluster demotion:** Database Migration Service demotes the destination cluster to configure it as a replica of the source database. 
  * **Avoid write operations on migrating data:** Don't perform write operations (such as `INSERT`, `UPDATE`, `DELETE`, or DDL schema changes) in the destination cluster on tables or databases included in the migration. Such operations might lead to replication conflicts with data coming from the source. 
  * **Manage database users:** You can create and manage database users at any time using standard `psql` commands or through AlloyDB for PostgreSQL in the Google Cloud console. For more information, see [Manage database users](https://docs.cloud.google.com/alloydb/docs/database-users/about) in the AlloyDB for PostgreSQL documentation. 



For more information, see [Known limitations for existing destination clusters](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#existing-instance-limitations). 

Database Migration Service uses migration jobs to migrate data from your source database to the destination AlloyDB for PostgreSQL cluster. Creating a migration job for an existing destination cluster includes:

  * Defining settings for the migration job
  * Defining source settings and selecting databases to migrate
  * Selecting the existing destination AlloyDB for PostgreSQL cluster 
  * Demoting the existing cluster to configure it as a replica of the source database 
  * Setting up connectivity between the source and destination databases
  * Testing the migration job to ensure that the connection information you provided is valid



## Before you begin

Before you create a migration job to an existing destination AlloyDB for PostgreSQL cluster, make sure you:

  1. Verify that this migration type can support your scenario. For example, when you want to migrate to a cluster created outside Database Migration Service, the AlloyDB for PostgreSQL destination cluster must be empty or contain only system configuration data. For more details, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#existing-instance-limitations). 
  2. Create the destination AlloyDB for PostgreSQL cluster and its primary instance. See [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) in the AlloyDB for PostgreSQL documentation. 

  3. Prepare your source database instance. See the following pages: 
     1. [Configure source database](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database)
     2. [Create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles)
     3. [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods)



To create a migration job to an existing destination cluster, do the following:

### Console

### Define settings for the migration job

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. Click **Create migration job**. 

The migration job configuration wizard page opens. This wizard contains multiple panels that walk you through each configuration step.

You can pause the creation of a migration job at any point by clicking **Save and exit**. All of the data that you enter up to that point is saved in a draft migration job. You can finish your draft migration job later.

  3. On the **Get started** page, enter the following information: 
     1. Migration job name 

This is a human-readable name for your migration job. This value is displayed in the Google Cloud console.

     2. Migration job ID 

This is a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.

     3. From the **Source database engine** list, select **PostgreSQL**.
     4. From the **Destination database engine** list, select **AlloyDB for PostgreSQL**. 
     5. Select the region where you save the migration job. 

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination clusters) must be saved in a single region. Select the region where your existing destination cluster is located. After you choose the destination region, this selection can't be changed. 

     6. Choose **Continuous** (snapshot + ongoing changes) as the migration job type. Homogeneous migrations to AlloyDB for PostgreSQL exclusively support continuous migrations. 
  4. Click **Save and continue**.



### Specify information about the source connection profile

On the **Define a source** page, perform the following steps:

  1. From the **Source connection profile** drop-down menu, select the connection profile for your source database.
  2. In the **Customize parallelism configurations** section, click **Show parallelism configurations**. 

During the initial full dump, the `pglogical` extension replicates data at the table level and doesn't split an individual non-partitioned table, leaf partition, or table without a primary key across multiple subscriptions. This means that enhanced data dump parallelism can't increase the initial dump speed for a single large non-partitioned table, because that table is copied within one subscription. For more information, see [Data dump parallelism considerations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#parallelism-considerations). 

The speed of data dump parallelism is related to the amount of load induced on your source database:

     * **Optimal (recommended)** : Balanced performance with optimal load on the source database. Database Migration Service creates up to 2 subscriptions per database (up to 2 total across all databases, with at least 1 subscription per migrated database). 
     * **Maximum** : Provides the highest dump speeds, but might cause increased load on the source database. Database Migration Service creates up to 4 subscriptions per database (up to 4 total across all databases, with at least 1 subscription per migrated database). 
     * **Minimum** : Takes the lowest amount of compute resources on the source database, but might have slower dump throughput. Database Migration Service creates 1 subscription per database. 

If you choose adjusted data dump parallelism settings, make sure to increase the `max_replication_slots`, `max_wal_senders`, and `max_worker_processes` parameters on your source database. 

  3. Click **Save and continue**.



### Select the destination AlloyDB for PostgreSQL cluster

  1. From the **Type of destination instance** menu, select **Existing cluster**. 
  2. In the **Select destination cluster** section, select your destination AlloyDB for PostgreSQL cluster. 
  3. Review the information in the **Cluster details** section, and click **Select and continue**.

To migrate to an existing destination database, Database Migration Service demotes the target cluster and configures it as a replica. To signify that the demotion can be safely performed, in the confirmation window, enter the destination cluster identifier. 

  4. Click **Confirm and continue**.



### Set up connectivity between the source database instance and destination cluster

From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the destination AlloyDB for PostgreSQL cluster connects to the source database. Current network connectivity methods include [IP allowlist, reverse SSH tunnel, Private Service Connect interfaces, VPC peering, and TCP proxy through a cloud-hosted VM](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods). 

If you want to use...| Then...  
---|---  
The IP allowlist network connectivity method, | Copy both outbound public IP addresses of your destination cluster's primary instance and use them to configure the network firewall for your source database server and in the `pg_hba.conf` file.  
The reverse SSH tunnel network connectivity method, | Select the Compute Engine VM instance that will host the tunnel. After specifying the instance, Google provides a script that performs the steps to set up the tunnel between the source and destination databases. Run the script in [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) from a machine that has connectivity to both the source database and to Google Cloud.  
The Private Service Connect interfaces connectivity method, | Database Migration Service automatically establishes the required connections. This connectivity method is only available if you have a Private Service Connect-enabled destination cluster with a network attachment. For more information on Private Service Connect, see [Configure Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect) in the AlloyDB for PostgreSQL documentation.   
The VPC peering network connectivity method, | Select the VPC network where the source database resides. The AlloyDB for PostgreSQL cluster connects to this network using private services access.  
The TCP proxy through a cloud-hosted VM connectivity method, | Enter the required details for the new Compute Engine VM instance that will host the TCP proxy. After specifying the details, the Google Cloud console provides a script that sets up the proxy between the source and destination databases. Run the script on a machine with an updated Google Cloud CLI. After running the script, enter the newly created VM's private IP address and click **Configure and continue**.  
  
After you select and configure network connectivity, click **Configure and continue**.

### Configure migration databases

You can migrate all databases from your source instance, or choose only specific databases. 

  1. From the **Databases to migrate** list, select one of the following options: 
     * **All databases** : Selects all databases that exist on the source.
     * **Specific databases** : Lets you select specific databases from all databases that exist on the source.
  2. If you want to migrate specific databases, filter the list that appears and select the databases that you want Database Migration Service to migrate into your destination.

If the list doesn't appear and a database discovery error is displayed, click **Reload**. If database discovery fails, the job migrates all databases. You can continue with creating a migration job and fix connectivity errors later.

  3. Click **Save and continue**.



### Test, create, and run the migration job

On this final step, review the summary of the migration job settings, source, destination, and connectivity method, and then test the validity of the migration job setup. If any issues are encountered, you can modify the migration job's settings. Not all settings are editable. 

  1. On the **Test and create migration job** page, click **Test job**. 

If the test fails, address the problem in the appropriate part of the flow, and return to re-test. For information on troubleshooting a failing migration job test, see [Diagnose issues for AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/diagnose-issues). 

  2. When the migration job test finishes, click **Create and start job** to create the migration job and start it immediately, or click **Create job** to create the migration job without immediately starting it. 

If the job isn't started at the time that it's created, it can be started from the **Migration jobs** page by clicking **Start**. Regardless of when the migration job starts, your organization is charged for the existence of the destination cluster. 

Your migration is now in progress. When you start the migration job, Database Migration Service begins the initial full dump and continuous replication. For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#parallelism-considerations).

  3. Proceed to [Review the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions).



### Google Cloud CLI

When you migrate to an existing cluster by using Google Cloud CLI, you must manually create the connection profile for the destination cluster. This isn't required when you use the Google Cloud console, as Database Migration Service takes care of creating and removing the destination connection profile for you.

  1. Create the destination connection profile.  
Create the destination connection profile for your existing destination cluster by running the [`gcloud database-migration connection-profiles create`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create) command (click the link to expand):

#### `gcloud database-migration connection-profiles create postgresql`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * DEST_CONN_ID with the destination connection profile identifier.
     * REGION with the region where you want to save the connection profile. This region should be the same as your destination cluster region. 
     * DEST_CLUSTER with the ID of your pre-created destination AlloyDB for PostgreSQL cluster.
     * DEST_USER with the username of the migration user on your destination database.
     * DEST_PASSWORD with the password for the migration user in the destination database.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql DEST_CONN_ID \
      --region=REGION \
      --alloydb-cluster=DEST_CLUSTER \
      --username=DEST_USER \
      --password=DEST_PASSWORD \
      --role=DESTINATION \
      --no-async

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql DEST_CONN_ID `
      --region=REGION `
      --alloydb-cluster=DEST_CLUSTER `
      --username=DEST_USER `
      --password=DEST_PASSWORD `
      --role=DESTINATION `
      --no-async

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql DEST_CONN_ID ^
      --region=REGION ^
      --alloydb-cluster=DEST_CLUSTER ^
      --username=DEST_USER ^
      --password=DEST_PASSWORD ^
      --role=DESTINATION ^
      --no-async

You should receive a response similar to the following:
    
    Waiting for connection profile [DEST_CONN_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile DEST_CONN_ID [OPERATION_ID]
    

  2. Create the migration job.   
The following example represents a migration scenario where you use Private IP connectivity between the source and destination databases. If you use a different connectivity type (for example IP allowlist, VPC peering, or a reverse-SSH tunnel), make sure to add the required flags, such as `--static-ip`, `--peer-vpc`, or `--vm`, `--vm-ip`, `--vm-port`, and `--vpc`. For more information, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods) and [Google Cloud CLI examples](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#EXAMPLES).  
Run the following command (click the link to expand): 

#### `gcloud database-migration migration-jobs create`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.
     * REGION with the region identifier where you want to save the migration job.
     * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
     * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile. For more information, see [Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles).
     * DESTINATION_CONNECTION_PROFILE_ID with a machine-readable identifier of the destination connection profile. 
     * Optional: Database Migration Service migrates all databases in your source by default. If you want to migrate only specific databases, use the `--databases-filter` flag and specify their identifiers as a comma-separated list.

For example: `--databases-filter=my-business-database,my-other-database`

You can later edit migration jobs that you created with the `--databases-filter` flag by using the [`gcloud database-migration migration-jobs update`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update) command.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    create MIGRATION_JOB_ID \
      --no-async \
      --region=REGION \
      --display-name=MIGRATION_JOB_NAME \
      --source=SOURCE_CONNECTION_PROFILE_ID \
      --destination=DESTINATION_CONNECTION_PROFILE_ID \
      --type=CONTINUOUS

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    create MIGRATION_JOB_ID `
      --no-async `
      --region=REGION `
      --display-name=MIGRATION_JOB_NAME `
      --source=SOURCE_CONNECTION_PROFILE_ID `
      --destination=DESTINATION_CONNECTION_PROFILE_ID `
      --type=CONTINUOUS

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    create MIGRATION_JOB_ID ^
      --no-async ^
      --region=REGION ^
      --display-name=MIGRATION_JOB_NAME ^
      --source=SOURCE_CONNECTION_PROFILE_ID ^
      --destination=DESTINATION_CONNECTION_PROFILE_ID ^
      --type=CONTINUOUS

You should receive a response similar to the following:
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    

  3. Demote the destination database.  
Database Migration Service requires that you demote the existing destination cluster to configure it as an external replica before you start the migration job. Run the [`gcloud database-migration migration-jobs demote-destination`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/demote-destination) command (click the link to expand):

#### `gcloud database-migration migration-jobs demote-destination`

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

     * REGION with the identifier of the region where your migration job is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    demote-destination MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    demote-destination MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    demote-destination MIGRATION_JOB_ID ^
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
      verb: demote-destination
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

     * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
     * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.

  4. Optional: Verify the migration job.  
At this point, your migration job is configured and connected to your destination cluster. You can manage it by using the [`verify`, `start`, `stop`, `restart`, and `resume` operations](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs). We recommend that you first verify your migration job by running the [`gcloud database-migration migration-jobs verify`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/verify) command (click the link to expand):

#### `gcloud database-migration migration-jobs verify`

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

     * REGION with the identifier of the region where your migration job is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    verify MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    verify MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    verify MIGRATION_JOB_ID ^
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
      verb: verify
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

     * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
     * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.

  5. Start the migration job.  
Start the migration job by running the [`gcloud database-migration migration-jobs start`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/start) command (click the link to expand):

#### `gcloud database-migration migration-jobs start`

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

     * REGION with the identifier of the region where your migration job is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    start MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    start MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    start MIGRATION_JOB_ID ^
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
      verb: start
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

     * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
     * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.

  6. Promote the migration job.  
Once the migration reaches the Change Data Capture (CDC) phase, you can promote the destination cluster from a replica to a standalone primary cluster. Run the [`gcloud database-migration migration-jobs promote`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/promote) command (click the link to expand):

#### `gcloud database-migration migration-jobs promote`

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




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
