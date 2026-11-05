---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job/
title: Create a migration job to a new destination cluster \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:17:48.816389+00:00
---

# Create a migration job to a new destination cluster  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Create a migration job to a new destination cluster Stay organized with collections  Save and categorize content based on your preferences. 

When you create your destination AlloyDB for PostgreSQL cluster with Database Migration Service, that cluster is provisioned as an AlloyDB for PostgreSQL cluster with a primary instance. Executing certain operations during the migration process might result in migration errors. As you migrate to a new destination cluster, keep the following operational considerations in mind:

  * **Avoid write operations on migrating data:** Don't perform write operations (such as `INSERT`, `UPDATE`, `DELETE`, or DDL schema changes) in the destination cluster on tables or databases included in the migration. Such operations might lead to replication conflicts with data coming from the source. 
  * **Manage database users:** You can create and manage database users at any time using standard `psql` commands or through AlloyDB for PostgreSQL in the Google Cloud console. For more information, see [Manage database users](https://docs.cloud.google.com/alloydb/docs/database-users/about) in the AlloyDB for PostgreSQL documentation. 



For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations). 

Creating a migration job includes:

  1. Defining settings for the migration job.
  2. Specifying information about the connection profile that you created for your source database (source connection profile).
  3. Defining settings for the destination AlloyDB for PostgreSQL cluster and creating the cluster.
  4. Setting up connectivity between the source and destination database environments.
  5. Testing the migration job to ensure that the connection information you provided for the job is valid.

**Note:** For private IP connectivity when you migrate to a new AlloyDB for PostgreSQL cluster created with Database Migration Service, you can only use the [private services access method (VPC peering)](https://docs.cloud.google.com/alloydb/docs/configure-connectivity). If you want to use Private Service Connect interfaces with your destination cluster, first [create the destination cluster directly in AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/cluster-create), and then follow the steps on the [Create a migration job to an existing destination cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance) page. 

To create a migration job to a new destination cluster, do the following:

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
     5. Select the [region](https://docs.cloud.google.com/docs/geography-and-regions) where you save the migration job. 

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases) must be saved in a single region. Select the region based on the location of the services that need your data, such as Compute Engine instances or App Engine apps, and other services. After you choose the destination region, this selection can't be changed. 

     6. Specify the migration job type: **Continuous** (snapshot + ongoing changes). AlloyDB for PostgreSQL homogeneous migrations exclusively support continuous migrations. 
     7. Review the prerequisites generated for your environment. Make sure your source database is configured appropriately. For more information, see [Configure source database](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database). 
  4. Click **Save and continue**.



### Specify information about the source connection profile

On the **Define a source** page, perform the following steps:

  1. From the **Source connection profile** drop-down menu, select the connection profile for your source database (or click **Create a connection profile** ; see [Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles)). 
  2. In the **Customize parallelism configurations** section, click **Show parallelism configurations**. 

During the initial full dump, the `pglogical` extension replicates data at the table level and doesn't split an individual non-partitioned table, leaf partition, or table without a primary key across multiple subscriptions. This means that enhanced data dump parallelism can't increase the initial dump speed for a single large non-partitioned table, because that table is copied within one subscription. For more information, see [Data dump parallelism considerations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#parallelism-considerations). 

The speed of data dump parallelism is related to the amount of load induced on your source database:

     * **Optimal (recommended)** : Balanced performance with optimal load on the source database. Database Migration Service creates up to 2 subscriptions per database (up to 2 total across all databases, with at least 1 subscription per migrated database). 
     * **Maximum** : Provides the highest dump speeds, but might cause increased load on the source database. Database Migration Service creates up to 4 subscriptions per database (up to 4 total across all databases, with at least 1 subscription per migrated database). 
     * **Minimum** : Takes the lowest amount of compute resources on the source database, but might have slower dump throughput. Database Migration Service creates 1 subscription per database. 

If you choose adjusted data dump parallelism settings, make sure to increase the `max_replication_slots`, `max_wal_senders`, and `max_worker_processes` parameters on your source database. 

  3. Click **Save and continue**.



### Configure and create the destination AlloyDB for PostgreSQL cluster

You now create a new destination AlloyDB for PostgreSQL cluster for your migration job. Clusters are the top-level resources in AlloyDB for PostgreSQL. They contain a single primary instance for read and write access to the database you create during the migration process. 

  1. On the **Define a destination** page, from the **Type of destination instance** drop-down menu, select **New cluster**.
  2. Choose a cluster type. Database Migration Service supports **Highly available** AlloyDB for PostgreSQL clusters, which can serve data from more than one zone in a region, with no read pools during initial provisioning. 
  3. Click **Continue**.
  4. Configure your cluster: 
     1. In the **Cluster ID** field, enter an identifier for the AlloyDB for PostgreSQL cluster or use the auto-generated identifier. 

Don't include sensitive or personally identifiable information in the identifier. You don't need to include the project ID in the cluster name. This is done automatically where appropriate.

     2. In the **Password** field, provide an alphanumeric password for the destination AlloyDB for PostgreSQL cluster. This is the password for the `postgres` administrator account in the cluster. 

You can either enter the password manually or click **Generate** to have Database Migration Service create one for you automatically.

     3. From the **Database version** drop-down menu, choose the database version for the destination cluster. 

[Learn more](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest) about cross-version migration support.

     4. In the **Network** field: 
        1. Select a network path to define which resources are available when setting the migration connectivity. Clusters are configured with a private IP network path. If you plan to connect to the source database with VPC peering, select the VPC where it resides.
        2. If your network isn't configured for [private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity), click **Set up connection** and follow the connection configuration wizard. 
        3. If a managed service network was never configured for the selected VPC, you can choose to either select an IP range and click **Connect** or use an automatically selected IP range and click **Allocate & Connect**. 
     5. (Optional) Configure data encryption options for your destination cluster.

#### Expand this section to see the optional steps.

Click **Show advanced options** to specify whether you want to manage the encryption of the data that's migrated from the source to the destination. By default, your data is encrypted with a key that's managed by Google Cloud.

If you want to manage your encryption, you can use a customer-managed encryption key (CMEK). The key must be in the same location as your AlloyDB for PostgreSQL cluster. For example, clusters located in **us-west1** can use only keys in **us-west1**.

        1. Select the **Use a customer-managed encryption key (CMEK)** radio button.
        2. From the **Select a customer-managed key** menu, select your CMEK.

If you don't see your key, click **Enter key resource name** to provide the resource name of the key that you want to use. For example, enter `projects/my-project-name/locations/my-location/keyRings/my-keyring/cryptoKeys/my-key` in the **Key resource name** field, and then click **Save**.

As part of creating the migration job, Database Migration Service verifies that the CMEK exists, and that Database Migration Service has permissions to use the key.

If Database Migration Service doesn't have these permissions, information appears specifying that the Database Migration Service service account can't use the CMEK. Click **Grant** to give Database Migration Service permissions to use the key.

For more information about encryption keys, see [Use CMEK](https://docs.cloud.google.com/alloydb/docs/use-cmek) in the AlloyDB for PostgreSQL documentation. 

     6. Click **Continue**.
  5. Configure your primary instance. A primary instance determines a cluster's compute capacity and supports read and write operations: 
     1. In the **Instance ID** field, enter an ID for your primary instance.
     2. Select a machine type for the primary instance.
     3. If you plan to use the **IP allowlist** connectivity method, select the **Enable outbound public IP** checkbox.
     4. (Optional) Configure database flags for your primary instance.

#### Expand this section to see the optional steps.

Click **Show advanced options** to set database flags for your primary instance. For information on supported flags, see [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags) in the AlloyDB for PostgreSQL documentation. For each flag:

        1. Click **Add flag**.
        2. Select a flag from the **New database flag** list.
        3. Provide a value for the flag.
        4. Click **Done**.

  6. Click **Save and continue** , and then confirm your choice by clicking **Create destination and continue**. Database Migration Service creates your destination AlloyDB for PostgreSQL cluster and its primary instance. This process can take several minutes. **Key point:**
     * Database Migration Service creates an AlloyDB for PostgreSQL cluster for which you are charged according to the configuration specified. If the migration job creation flow is exited before completion, use the **Cancel** button to clean up the cluster. If the browser or tab is closed, **Save and exit** is clicked, or the screen is navigated away from, then the AlloyDB for PostgreSQL cluster isn't cleaned up and must be deleted manually from the AlloyDB for PostgreSQL Clusters page. 
     * After the destination cluster is created, its configuration can be inspected directly in AlloyDB for PostgreSQL in the Google Cloud console. 



### Set up connectivity between the source database instance and destination cluster

From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the destination AlloyDB for PostgreSQL cluster connects to the source database. Current network connectivity methods for migrating to a new cluster include [ IP allowlist, VPC peering, reverse SSH tunnel, and TCP proxy through a cloud-hosted VM](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods).

If you want to use...| Then...  
---|---  
The IP allowlist network connectivity method, | Copy both outbound public IP addresses of your destination cluster's primary instance and use them to configure the network firewall for your source database server and in the `pg_hba.conf` file.  
The reverse SSH tunnel network connectivity method, | Select the Compute Engine VM instance that will host the tunnel. After specifying the instance, Google provides a script that performs the steps to set up the tunnel between the source and destination databases. Run the script in [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) from a machine that has connectivity to both the source database and to Google Cloud.  
The VPC peering network connectivity method, | Select the VPC network where the source database resides. The destination cluster connects to this network using private services access.  
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

On this final step, review the summary of the migration job settings, source, destination, and connectivity method, and then test the validity of the migration job setup. If any issues are encountered, you can modify the migration job settings. 

  1. On the **Test and create migration job** page, click **Test job**. 

If the test fails, address the problem in the appropriate part of the flow, and return to re-test. For information on troubleshooting a failing migration job test, see [Diagnose issues for AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/diagnose-issues). 

  2. When the migration job test finishes, click **Create and start job** to create the migration job and start it immediately, or click **Create job** to create the migration job without immediately starting it. 

If the job isn't started at the time that it's created, it can be started from the **Migration jobs** page by clicking **Start**. Regardless of when the migration job starts, your organization is charged for the existence of the destination cluster. 

When you start the migration job, Database Migration Service begins the initial full dump and continuous replication. For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#parallelism-considerations).

  3. Proceed to [Review the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions). 



### Google Cloud CLI

  1. Create the destination connection profile.  
When you migrate to a new destination cluster with Google Cloud CLI, you create the destination cluster and the connection profile in a single action.  
Run the following command (click the link to expand):

#### `gcloud database-migration connection-profiles create alloydb`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * DEST_CONN_ID with the destination connection profile identifier.
     * REGION with the region where you want to save the connection profile and create the destination cluster.
     * DEST_PASSWORD with the initial password for the `postgres` user on your destination AlloyDB for PostgreSQL cluster.
     * PRIMARY_ID with the ID for the primary instance in your destination AlloyDB for PostgreSQL cluster.
     * CPU_COUNT with the number of vCPUs for the primary instance (for example, `2`, `4`, `8`).
     * VPC_NETWORK with the name or full resource URI of the Virtual Private Cloud network configured for private services access.
     * Optional: To configure additional settings for your new destination AlloyDB for PostgreSQL cluster and primary instance, you can pass the following flags: 
       * `--enable-outbound-public-ip`: Enable outbound public IP on the primary instance (required if you use IP allowlist connectivity).
       * `--kms-key`, `--kms-keyring`, and `--kms-project`: Encrypt the destination cluster with a customer-managed encryption key (CMEK).
       * `--database-version`: Specify the PostgreSQL major version for the destination cluster (for example, `POSTGRES_15`).
       * `--database-flags`: Specify a comma-separated list of database flags (`KEY=VALUE`) for the destination primary instance.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create alloydb DEST_CONN_ID \
      --region=REGION \
      --password=DEST_PASSWORD \
      --primary-id=PRIMARY_ID \
      --cpu-count=CPU_COUNT \
      --network=VPC_NETWORK \
      --no-async

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create alloydb DEST_CONN_ID `
      --region=REGION `
      --password=DEST_PASSWORD `
      --primary-id=PRIMARY_ID `
      --cpu-count=CPU_COUNT `
      --network=VPC_NETWORK `
      --no-async

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create alloydb DEST_CONN_ID ^
      --region=REGION ^
      --password=DEST_PASSWORD ^
      --primary-id=PRIMARY_ID ^
      --cpu-count=CPU_COUNT ^
      --network=VPC_NETWORK ^
      --no-async

You should receive a response similar to the following:
    
    Waiting for connection profile [DEST_CONN_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile DEST_CONN_ID [OPERATION_ID]
    

  2. Create the migration job.   
If you use IP allowlist, VPC peering, or reverse-SSH tunnel connectivity, make sure to add the required flags, such as `--static-ip`, `--peer-vpc`, or `--vm`, `--vm-ip`, `--vm-port`, and `--vpc`. For more information, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods) and [Google Cloud CLI examples](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#EXAMPLES).  
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
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
