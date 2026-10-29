---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-guide/
title: Migrate from self-managed SQL Server using Distributed Availability Groups \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:00.614235+00:00
---

# Migrate from self-managed SQL Server using Distributed Availability Groups  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Migrate from self-managed SQL Server using Distributed Availability Groups Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to migrate databases from a self-managed SQL Server Enterprise Edition instance to Cloud SQL for SQL Server Enterprise Edition over a private network connection by using a Distributed Availability Group (DAG) in Database Migration Service.

With a DAG migration, Database Migration Service streams both the initial full load (known as the `FULL_DUMP` phase) and continuous transaction log replication (known as the Change Data Capture - `CDC` \- phase) directly over the network between your source Availability Group and your destination Cloud SQL for SQL Server Availability Group. For more information about the architecture, prerequisites, and limitations of DAG migrations, see [About Distributed Availability Group (DAG) migrations](https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-overview). To migrate by using backup files stored in Cloud Storage, see [Migrate your SQL Server databases to Cloud SQL for SQL Server](https://docs.cloud.google.com/database-migration/docs/sqlserver/guide).

To perform a Distributed Availability Group migration, you complete the following high-level tasks:

  1. Create and prepare your destination Cloud SQL for SQL Server instance.
  2. Prepare your source SQL Server instance and Availability Group.
  3. Establish bidirectional private network connectivity and configure a Linked Server.
  4. Create connection profiles and run the migration job.
  5. Monitor and verify your migration.
  6. Promote, fail back, or complete the migration.



## Costs

For homogeneous migrations to Cloud SQL, Database Migration Service is offered at no additional charge. However, standard Cloud SQL and network pricing applies. To estimate your usage costs, use the [pricing calculator](https://docs.cloud.google.com/products/calculator).

## Before you begin

  1. Verify that your source and destination databases meet all prerequisites and limitations for Distributed Availability Group migrations (including running Enterprise Edition, storing data files in the default data directory, and not using `sa` as the database owner). See [About Distributed Availability Group (DAG) migrations](https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-overview).
  2. Choose the Google Cloud region for your migration. Database Migration Service is a fully regional product; all entities related to your migration (source and destination connection profiles, migration job, and destination Cloud SQL for SQL Server instance) must reside in the same region.
  3. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. Enable the Database Migration Service, Compute Engine, and Cloud SQL Admin APIs. 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,datamigration.googleapis.com,sqladmin.googleapis.com)




### Required roles

Make sure that the following IAM roles are granted in your Google Cloud project:

  * User account that performs the migration: 
    * [Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`)
    * [Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`)
  * Database Migration Service service account (`service-<var>PROJECT_NUMBER</var>@gcp-sa-datamigration.iam.gserviceaccount.com`): 
    * [Database Migration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.serviceAgent) (`roles/datamigration.serviceAgent`)
    * [Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`)
    * [Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`)



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create and prepare your destination Cloud SQL for SQL Server instance

In this step, you create your destination Cloud SQL for SQL Server Enterprise Edition instance and enable the database flag required for Linked Servers.

  1. Create your destination Cloud SQL for SQL Server instance. For detailed creation instructions, see [Create a Cloud SQL for SQL Server instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance). Ensure that your instance meets the following requirements for Distributed Availability Group migrations: 
     * Select **Enterprise Edition** (version 2017, 2019, 2022, or 2025).
     * Configure private networking to align with how you plan to connect your source SQL Server instance and destination Cloud SQL for SQL Server instance. Enable [ Private Services Access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip) if you plan to connect your instances over Virtual Private Cloud peering, or use [ Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect) if you plan to connect your instances by using an inbound Private Service Connect endpoint and an outbound Private Service Connect network attachment. 

Don't enable both Private Services Access and Private Service Connect on the same destination Cloud SQL for SQL Server instance. Cloud SQL for SQL Server doesn't support Linked Servers when both are enabled. For full networking setup details, see Establish bidirectional private network connectivity. 

     * Keep [Point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/configure-pitr) disabled and don't add read replicas until after you complete and delete the DAG migration job.
     * If any source database is owned by a Windows Active Directory login, either change the source database owner to a SQL login before migrating, or join the destination Cloud SQL for SQL Server instance to Active Directory so that Database Migration Service can automatically create the corresponding Windows login on the destination instance when the migration job starts. For instructions, see [Configure Managed Microsoft AD for Cloud SQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/ad).
  2. Enable the `cloudsql enable linked servers` database flag (set to `on`) on your destination Cloud SQL for SQL Server instance. For instructions on setting flags, see [Manage linked servers](https://docs.cloud.google.com/sql/docs/sqlserver/manage-linked-servers) and [Configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags). 

This flag is needed at a later point in this guide when you create and verify the Linked Server on your destination Cloud SQL for SQL Server instance. 




## Prepare your source SQL Server instance

In this step, you enable Always On Availability Groups on your source SQL Server instance, create a Database Mirroring endpoint and certificate, create a dedicated SQL login for Database Migration Service, and prepare your source Availability Group.

### Enable Always On Availability Groups

Ensure that the Always On Availability Groups feature is enabled on your source SQL Server instance:

  * For Windows, see [Enable and disable Always On availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/enable-and-disable-always-on-availability-groups-sql-server) in the Microsoft documentation.
  * For Linux, see [Configure SQL Server Always On availability group for high availability on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-availability-group-configure-ha) in the Microsoft documentation.



### Create the Database Mirroring endpoint and certificate

In SQL Server, Distributed Availability Groups stream data and transaction logs between instances over TCP `DATABASE_MIRRORING` (`DBM`) endpoints (default port `5022`). Because your self-managed SQL Server instance and your destination Cloud SQL for SQL Server instance are standalone instances, they require certificate-based mutual authentication and AES encryption to establish trust over the `DBM` endpoint.

You only need to create a certificate and bind it to the `DATABASE_MIRRORING` endpoint on your source SQL Server instance. You don't need to manually export certificate files or create certificates on your destination Cloud SQL for SQL Server instance:

  * When you start the migration job, Database Migration Service automatically configures the `DATABASE_MIRRORING` endpoint and certificate on your destination Cloud SQL for SQL Server instance and uses your Linked Server to exchange the public keys between both instances.
  * When you delete the migration job after completing your cutover, Database Migration Service automatically removes the imported certificates from both instances.



If your source SQL Server instance doesn't already have a `DATABASE_MIRRORING` endpoint authenticated with a certificate, create one:

  1. Connect to your source instance with a SQL client, for example the [`sqlcmd`](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility) utility. 
  2. Run the following T-SQL commands to create a database master key, a certificate, and a `DATABASE_MIRRORING` endpoint listening on your chosen `DBM` port (default `5022`): 
         
         USE [master];
         GO
         
         IF NOT EXISTS (SELECT * FROM sys.symmetric_keys WHERE symmetric_key_id = 101)
         BEGIN
             CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'MASTER_KEY_PASSWORD';
         END
         GO
         
         CREATE CERTIFICATE [SOURCE_CERT_NAME]
             WITH SUBJECT = 'AlwaysOn AG Certificate',
             EXPIRY_DATE = 'CERT_EXPIRY_DATE';
         GO
         
         CREATE ENDPOINT [HADR_ENDPOINT_NAME]
             STATE = STARTED
             AS TCP (LISTENER_PORT = SOURCE_DBM_PORT_NUMBER)
             FOR DATABASE_MIRRORING (
                 ROLE = ALL,
                 AUTHENTICATION = CERTIFICATE [SOURCE_CERT_NAME],
                 ENCRYPTION = REQUIRED ALGORITHM AES
             );
         GO

Replace the following:

     * `MASTER_KEY_PASSWORD` with a password to encrypt the database master key.
     * `SOURCE_CERT_NAME` with a name for your source Database Mirroring certificate (for example, `dbmCertificate`).
     * `CERT_EXPIRY_DATE` with the expiration date for the certificate in `YYYYMMDD` format.
     * `HADR_ENDPOINT_NAME` with the name of your Database Mirroring endpoint.
     * `SOURCE_DBM_PORT_NUMBER` with the TCP port number for Database Mirroring traffic (default `5022`).



### Create the dedicated Database Migration Service login and permissions

Database Migration Service connects to your source SQL Server instance through the Linked Server using a dedicated SQL login that you supply in the source connection profile. You can configure this login by granting the `sysadmin` server role or by configuring least-privilege permissions with the `gcp_dms_db` helper database:

#### Grant sysadmin role

If your security policy permits granting the `sysadmin` server role to the migration login, run the following T-SQL commands:
    
    
    USE [master];
    GO
    CREATE LOGIN [SOURCE_USERNAME] WITH PASSWORD = 'SOURCE_PASSWORD';
    CREATE USER [SOURCE_USER] FOR LOGIN [SOURCE_USERNAME];
    ALTER SERVER ROLE [sysadmin] ADD MEMBER [SOURCE_USERNAME];
    GRANT CONNECT ON ENDPOINT::[HADR_ENDPOINT_NAME] TO [SOURCE_USERNAME];
    GO

Replace the following:

  * `SOURCE_USERNAME` with the SQL login name that Database Migration Service uses to connect to your source instance (for example, `cloud_dms_login`).
  * `SOURCE_PASSWORD` with the password for the `SOURCE_USERNAME` login.
  * `SOURCE_USER` with the database user name mapped to `SOURCE_USERNAME` (for example, `cloud_dms_user`).
  * `HADR_ENDPOINT_NAME` with the name of your Database Mirroring endpoint (for example, `Hadr_endpoint`).



#### Least privilege (gcp_dms_db)

If your security policy prohibits granting `sysadmin` to the migration login, create the dedicated `gcp_dms_db` helper database (owned by `sa` with `TRUSTWORTHY ON`), create the three Database Migration Service wrapper stored procedures, and grant granular permissions to your migration login:
    
    
    USE [master];
    GO
    
    CREATE DATABASE [gcp_dms_db];
    GO
    
    ALTER AUTHORIZATION ON DATABASE::[gcp_dms_db] TO [sa];
    ALTER DATABASE [gcp_dms_db] SET TRUSTWORTHY ON;
    GO
    
    USE [gcp_dms_db];
    GO
    
    CREATE OR ALTER PROCEDURE dbo.gcp_dms_set_dag_commit_mode
        @dag_name NVARCHAR(128),
        @source_ag NVARCHAR(128),
        @dest_ag NVARCHAR(128),
        @commit_mode NVARCHAR(30)
    WITH EXECUTE AS 'dbo'
    AS
    BEGIN
        SET NOCOUNT ON;
        IF @commit_mode NOT IN ('SYNCHRONOUS_COMMIT', 'ASYNCHRONOUS_COMMIT')
        BEGIN
            RAISERROR('Invalid commit mode. Must be SYNCHRONOUS_COMMIT or ASYNCHRONOUS_COMMIT.', 16, 1);
            RETURN;
        END
        DECLARE @sql NVARCHAR(MAX);
        SET @sql = N'USE master; ALTER AVAILABILITY GROUP ' + QUOTENAME(@dag_name) +
                   N' MODIFY AVAILABILITY GROUP ON ' +
                   QUOTENAME(@source_ag, '''') + N' WITH (AVAILABILITY_MODE = ' + @commit_mode + N'), ' +
                   QUOTENAME(@dest_ag, '''') + N' WITH (AVAILABILITY_MODE = ' + @commit_mode + N');';
        EXECUTE sp_executesql @sql;
    END;
    GO
    
    CREATE OR ALTER PROCEDURE dbo.gcp_dms_set_dag_secondary
        @dag_name NVARCHAR(128)
    WITH EXECUTE AS 'dbo'
    AS
    BEGIN
        SET NOCOUNT ON;
        DECLARE @sql NVARCHAR(MAX);
        SET @sql = N'USE master; ALTER AVAILABILITY GROUP ' + QUOTENAME(@dag_name) + N' SET (ROLE = SECONDARY);';
        EXECUTE sp_executesql @sql;
    END;
    GO
    
    CREATE OR ALTER PROCEDURE dbo.gcp_dms_failover_dag
        @dag_name NVARCHAR(128)
    WITH EXECUTE AS 'dbo'
    AS
    BEGIN
        SET NOCOUNT ON;
        DECLARE @sql NVARCHAR(MAX);
        SET @sql = N'USE master; ALTER AVAILABILITY GROUP ' + QUOTENAME(@dag_name) + N' FORCE_FAILOVER_ALLOW_DATA_LOSS;';
        EXECUTE sp_executesql @sql;
    END;
    GO
    
    USE [master];
    GO
    
    CREATE LOGIN [SOURCE_USERNAME] WITH PASSWORD = 'SOURCE_PASSWORD';
    CREATE USER [SOURCE_USER] FOR LOGIN [SOURCE_USERNAME];
    GRANT VIEW SERVER STATE TO [SOURCE_USERNAME];
    -- Note: Run GRANT VIEW SERVER PERFORMANCE STATE on SQL Server 2022 and later:
    GRANT VIEW SERVER PERFORMANCE STATE TO [SOURCE_USERNAME];
    GRANT VIEW ANY DEFINITION TO [SOURCE_USERNAME];
    GRANT ALTER ANY AVAILABILITY GROUP TO [SOURCE_USERNAME];
    GRANT CONNECT ON ENDPOINT::[HADR_ENDPOINT_NAME] TO [SOURCE_USERNAME];
    GRANT CREATE CERTIFICATE TO [SOURCE_USER];
    GO
    
    USE [gcp_dms_db];
    GO
    
    CREATE USER [SOURCE_USER] FOR LOGIN [SOURCE_USERNAME];
    GRANT EXECUTE ON dbo.gcp_dms_set_dag_commit_mode TO [SOURCE_USER];
    GRANT EXECUTE ON dbo.gcp_dms_set_dag_secondary TO [SOURCE_USER];
    GRANT EXECUTE ON dbo.gcp_dms_failover_dag TO [SOURCE_USER];
    GO
    
    -- Repeat the following block for EACH user database in your source Availability Group:
    USE [DATABASE_NAME];
    GO
    
    CREATE USER [SOURCE_USER] FOR LOGIN [SOURCE_USERNAME];
    ALTER ROLE [db_backupoperator] ADD MEMBER [SOURCE_USER];
    GO

Replace the following:

  * `SOURCE_USERNAME` with the SQL login name that Database Migration Service uses to connect to your source instance (for example, `cloud_dms_login`).
  * `SOURCE_PASSWORD` with the password for the `SOURCE_USERNAME` login.
  * `SOURCE_USER` with the database user name mapped to `SOURCE_USERNAME` (for example, `cloud_dms_user`).
  * `HADR_ENDPOINT_NAME` with the name of your Database Mirroring endpoint (for example, `Hadr_endpoint`).
  * `DATABASE_NAME` with the name of each source database in your Availability Group. Granting `db_backupoperator` on each migrated database is required by Database Migration Service preflight verification and allows flushing transaction logs with `CHECKPOINT` during promotion.



### Prepare your source databases and Availability Group

You can migrate databases from an existing Always On Availability Group or create a new standalone Availability Group (`CLUSTER_TYPE = NONE`). Before continuing, verify the following requirements:

  * Every database in the Availability Group uses the `FULL` recovery model, is **not** owned by `sa`, and stores its data files (`.mdf` and `.ndf`) in the default data directory.
  * If you reuse an existing Availability Group, confirm that your Database Mirroring endpoint is configured on port `5022` (or your chosen DBM port), that `SECONDARY_ROLE (ALLOW_CONNECTIONS = ALL)` is enabled on the replica so secondary databases remain readable with standard connection strings after promotion flips the DAG roles, and that your migration login has `CONNECT ON ENDPOINT`. If your source Availability Group has multiple replicas and an Availability Group listener configured, use the listener IP address as `<var>SOURCE_HOST_IP_ADDRESS</var>` when configuring your Linked Server and source connection profile so that the migration can resume if a failover occurs in the source Availability Group.



To prepare a database and create a new standalone Availability Group (`CLUSTER_TYPE = NONE`), run the following T-SQL commands:
    
    
    USE [master];
    GO
    
    ALTER DATABASE [DATABASE_NAME] SET RECOVERY FULL;
    GO
    
    -- If the database is owned by 'sa', change the owner to another login:
    ALTER AUTHORIZATION ON DATABASE::[DATABASE_NAME] TO [DB_OWNER_LOGIN];
    GO
    
    -- Initialize the local SQL Server transaction log chain for the Availability Group:
    BACKUP DATABASE [DATABASE_NAME] TO DISK = 'NUL';
    GO
    
    CREATE AVAILABILITY GROUP [SOURCE_AVAILABILITY_GROUP_NAME] WITH (CLUSTER_TYPE = NONE)
        FOR REPLICA ON N'SOURCE_SERVER_NAME' WITH (
            ENDPOINT_URL = N'TCP://localhost:SOURCE_DBM_PORT_NUMBER',
            FAILOVER_MODE = MANUAL,
            AVAILABILITY_MODE = SYNCHRONOUS_COMMIT,
            SEEDING_MODE = MANUAL,
            PRIMARY_ROLE (ALLOW_CONNECTIONS = READ_WRITE),
            SECONDARY_ROLE (ALLOW_CONNECTIONS = ALL)
        );
    GO
    
    ALTER AVAILABILITY GROUP [SOURCE_AVAILABILITY_GROUP_NAME] ADD DATABASE [DATABASE_NAME];
    GO

Replace the following:

  * `DATABASE_NAME` with the name of the database to include in your Availability Group.
  * `DB_OWNER_LOGIN` with a non-`sa` login to own the database.
  * `SOURCE_AVAILABILITY_GROUP_NAME` with the name of your source Availability Group (for example, `source_ag`).
  * `SOURCE_SERVER_NAME` with the server name of your source SQL Server instance (matching the value returned by `SELECT @@SERVERNAME`).
  * `SOURCE_DBM_PORT_NUMBER` with the TCP port number of your Database Mirroring endpoint (default `5022`).

**Note:** Running `BACKUP DATABASE ... TO DISK = 'NUL'` is a local SQL Server requirement to initialize the database's transaction log chain after switching to the `FULL` recovery model before adding it to an Availability Group. This command initializes the local log chain for the Availability Group and doesn't create or upload any backup files. When you start the migration job, Database Migration Service configures the Distributed Availability Group to stream the initial full load directly over the network.

## Establish bidirectional private network connectivity

For DAG migrations, Database Migration Service communicates with your destination Cloud SQL for SQL Server instance through internal Google Cloud APIs, executes orchestration queries on your source SQL Server instance through a Linked Server on the destination Cloud SQL for SQL Server instance, and streams data directly between the two instances over a private network. This migration requires that you establish **bidirectional private IP connectivity** directly between your source SQL Server host and your destination Cloud SQL for SQL Server instance through your Virtual Private Cloud network. Public IP connectivity between the source and destination instances isn't supported.

### Required ports and IP addresses

Your network configuration must allow traffic between your source SQL Server instance and your destination Cloud SQL for SQL Server instance on the following two TCP ports:

Port | Direction | Purpose  
---|---|---  
**SQL Server database port** (default `1433`) | From the destination Cloud SQL for SQL Server instance to the source SQL Server instance | Used by the Linked Server on your destination Cloud SQL for SQL Server instance to run preflight validation, certificate exchange, and DAG orchestration queries on your source instance.  
**Database Mirroring (`DBM`) port** (default `5022`) | Bidirectional between the source SQL Server instance and the destination Cloud SQL for SQL Server instance | Used by the source and destination Availability Groups to stream the initial full load during `FULL_DUMP`, ongoing database changes during `CDC`, and reverse replication during `FAILBACK`.  
  
When you configure your Linked Server and connection profiles later in this guide, you provide two private IP addresses:

  * `SOURCE_HOST_IP_ADDRESS` (used in the Linked Server `@datasrc` parameter and the source connection profile `--host` flag) is the private IP address of your source SQL Server host (or the Availability Group listener IP address, which is preferred if configured for a multi-replica source Availability Group so the migration can resume if a failover occurs in the source Availability Group) that is reachable from your destination Cloud SQL for SQL Server instance.
  * `DESTINATION_HOST_IP_ADDRESS` (used in the destination connection profile `--host` flag) is the private IP address of your destination Cloud SQL for SQL Server instance (or its Private Service Connect endpoint IP address) that is reachable from your source SQL Server host.



### Configure your private networking method

Complete the network routing configuration for the networking method (**Private Services Access** or **Private Service Connect**) that you enabled on your destination Cloud SQL for SQL Server instance:

#### Private Services Access

[Private Services Access](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip) peers your Virtual Private Cloud network with the Google-managed service producer Virtual Private Cloud network that hosts your destination Cloud SQL for SQL Server instance:

  1. Verify that your Virtual Private Cloud network has an allocated internal IPv4 address range and a private connection (Virtual Private Cloud peering to `servicenetworking-googleapis-com`) enabled for your destination Cloud SQL for SQL Server instance. For instructions, see [Configure private IP for Cloud SQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip).
  2. Configure routing to your source SQL Server host based on where it is hosted: 
     * If your source instance runs on a Compute Engine virtual machine in the same Virtual Private Cloud network, no additional routing is required. The virtual machine and the Cloud SQL for SQL Server instance can reach each other's private IP addresses directly over the Virtual Private Cloud peering connection.
     * If your source instance runs on-premises, in another cloud provider, or in another Virtual Private Cloud network, complete the following steps so that routes are exchanged across the transitive peering boundary: 
       1. Connect your external network to your Virtual Private Cloud network by using Cloud VPN or Cloud Interconnect. For instructions, see [Access a Cloud SQL instance from an external source](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#vpn).
       2. In Cloud Router, advertise the Cloud SQL for SQL Server allocated IP address range to your source network. For instructions, see [Advertise custom IP ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip).
       3. Update the `servicenetworking-googleapis-com` peering connection in your Virtual Private Cloud network to enable **Export custom routes** so that your Cloud SQL for SQL Server instance learns the routes to your source network. For instructions, see [Update a peering connection](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#update-peer-connection).
  3. Record the private IP addresses for your migration: 
     * Use your source SQL Server host's internal IP address as `SOURCE_HOST_IP_ADDRESS`.
     * Use the **Private IP address** assigned to your destination Cloud SQL for SQL Server instance (shown on the instance **Overview** page) as `DESTINATION_HOST_IP_ADDRESS`.



#### Private Service Connect

If you use [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) instead of Private Services Access, you must configure both an inbound Private Service Connect endpoint (so your source instance can connect to Cloud SQL for SQL Server on port `5022`) and an outbound Private Service Connect interface (so Cloud SQL for SQL Server can initiate Linked Server and DAG connections to your source instance on ports `1433` and `5022`):

  1. Verify that your destination Cloud SQL for SQL Server instance has Private Service Connect enabled (without Private IP) and specifies your allowed consumer projects. For instructions, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect).
  2. To allow inbound connections from your source SQL Server host to your destination Cloud SQL for SQL Server instance, reserve an internal IP address in your Virtual Private Cloud subnet and create a Private Service Connect endpoint (forwarding rule) that targets your Cloud SQL for SQL Server instance's service attachment. For instructions, see [Create a Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#create-psc-endpoint).
  3. To allow outbound connections from your destination Cloud SQL for SQL Server instance to your source SQL Server host (required for Linked Server and outbound DAG connections), create a Virtual Private Cloud network attachment in the subnet that can route to your source host and configure Private Service Connect outbound connectivity on your destination Cloud SQL for SQL Server instance. For instructions, see [Create and manage network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments) and [Configure Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#configure-psc-outbound).
  4. Record the private IP addresses for your migration: 
     * Use your source SQL Server host's private IP address as `SOURCE_HOST_IP_ADDRESS`.
     * Use the internal IP address of your Private Service Connect endpoint (forwarding rule) in your Virtual Private Cloud network as `DESTINATION_HOST_IP_ADDRESS`.



### Configure Virtual Private Cloud and source host firewall rules

  1. In your Virtual Private Cloud network, create ingress and egress firewall rules that allow TCP traffic between your source SQL Server IP address (`SOURCE_HOST_IP_ADDRESS`) and your destination Cloud SQL for SQL Server IP range (or Private Service Connect endpoint and network attachment subnet) on both the database port (default `1433`) and the Database Mirroring port (default `5022`). For more information about creating firewall rules, see [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).
  2. On your source SQL Server machine, verify the following network and host firewall settings: 
     * TCP/IP is enabled in SQL Server Configuration Manager (or `mssql-conf` on Linux) and the instance listens on a static TCP port (default `1433`).
     * The operating system firewall (such as Windows Defender Firewall or Linux `iptables` or `firewalld`) allows inbound TCP connections on both your database port (default `1433`) and your Database Mirroring port (default `5022`), and outbound TCP connections to `DESTINATION_HOST_IP_ADDRESS` on port `5022`.



### Verify reachability with Cloud SQL connectivity tests

Before you configure your Linked Server, we recommend running three connectivity tests from the **Connections > Connectivity tests** tab of your Cloud SQL for SQL Server instance in the Google Cloud console. For instructions on how to run a connectivity test, see [Manage connectivity tests](https://docs.cloud.google.com/sql/docs/sqlserver/manage-connectivity-tests):

  1. To test outbound Linked Server connectivity on port `1433`, set **Source** to **Current Cloud SQL instance** , **Destination** to `SOURCE_HOST_IP_ADDRESS`, and **Destination port** to `1433` (or your custom database port).
  2. To test outbound Database Mirroring connectivity on port `5022`, set **Source** to **Current Cloud SQL instance** , **Destination** to `SOURCE_HOST_IP_ADDRESS`, and **Destination port** to `5022` (or your custom `DBM` port).
  3. To test inbound Database Mirroring connectivity on port `5022`, set **Source** to `SOURCE_HOST_IP_ADDRESS`, **Destination** to **Current Cloud SQL instance** (or `DESTINATION_HOST_IP_ADDRESS` if you use Private Service Connect), and **Destination port** to `5022` (or your custom `DBM` port).



### Create and verify the Linked Server on your destination Cloud SQL for SQL Server instance

After your network connectivity is in place, connect to your destination Cloud SQL for SQL Server instance and create the Linked Server pointing to your source SQL Server instance:

  1. Connect to your Cloud SQL instance with a SQL client. You can use the following methods: 
     * [`sqlcmd` client](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip). You can use this method to connect to your instance private IP, but it might require that you create a Compute Engine virtual machine. 
     * [`gcloud sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect) command. This command works only for Cloud SQL instances that have a public IP address enabled. 
  2. Sign in as the `sqlserver` user and run the following T-SQL commands for your destination Cloud SQL for SQL Server version to create a Linked Server pointing to your source SQL Server instance, map `@locallogin = N'sqlserver'` to your source migration login, enable `rpc out`, and test the connection with `OPENQUERY` (for more information about Linked Server options on Cloud SQL, see [Manage linked servers](https://docs.cloud.google.com/sql/docs/sqlserver/manage-linked-servers)): 

#### Cloud SQL for SQL Server 2017, 2019, and 2022
         
         USE [master];
         GO
         
         EXEC master.dbo.sp_addlinkedserver
             @server = N'LINKED_SERVER_NAME',
             @srvproduct = N'',
             @provider = N'SQLNCLI',
             @datasrc = N'SOURCE_HOST_IP_ADDRESS,SOURCE_PORT_NUMBER';
         GO
         
         EXEC master.dbo.sp_addlinkedsrvlogin
             @rmtsrvname = N'LINKED_SERVER_NAME',
             @useself = N'False',
             @locallogin = N'sqlserver',
             @rmtuser = N'SOURCE_USERNAME',
             @rmtpassword = N'SOURCE_PASSWORD';
         GO
         
         EXEC master.dbo.sp_serveroption
             @server = N'LINKED_SERVER_NAME',
             @optname = N'rpc out',
             @optvalue = N'TRUE';
         GO
         
         SELECT * FROM OPENQUERY([LINKED_SERVER_NAME], 'SELECT @@VERSION AS SourceServerVersion');
         GO

#### Cloud SQL for SQL Server 2025
         
         USE [master];
         GO
         
         EXEC master.dbo.sp_addlinkedserver
             @server = N'LINKED_SERVER_NAME',
             @srvproduct = N'',
             @provider = N'MSOLEDBSQL19',
             @datasrc = N'SOURCE_HOST_IP_ADDRESS,SOURCE_PORT_NUMBER',
             @provstr = N'Encrypt=Optional;TrustServerCertificate=Yes;Authentication=SqlPassword;UID=Placeholder;';
         GO
         
         EXEC master.dbo.sp_addlinkedsrvlogin
             @rmtsrvname = N'LINKED_SERVER_NAME',
             @useself = N'False',
             @locallogin = N'sqlserver',
             @rmtuser = N'SOURCE_USERNAME',
             @rmtpassword = N'SOURCE_PASSWORD';
         GO
         
         EXEC master.dbo.sp_serveroption
             @server = N'LINKED_SERVER_NAME',
             @optname = N'rpc out',
             @optvalue = N'TRUE';
         GO
         
         SELECT * FROM OPENQUERY([LINKED_SERVER_NAME], 'SELECT @@VERSION AS SourceServerVersion');
         GO

Replace the following:

     * `LINKED_SERVER_NAME` with the name for your Linked Server on Cloud SQL for SQL Server (for example, `source_sql_linked_server`).
     * `SOURCE_HOST_IP_ADDRESS` with the private IP address of your source SQL Server instance (or the Availability Group listener IP address if configured for a multi-replica source Availability Group).
     * `SOURCE_PORT_NUMBER` with the port number where your source SQL Server database engine accepts connections (default `1433`).
     * `SOURCE_USERNAME` with the dedicated SQL login name that you created on your source instance in Create the dedicated Database Migration Service login and permissions.
     * `SOURCE_PASSWORD` with the password for the `SOURCE_USERNAME` login.



## Create connection profiles and run the migration job

Use the Google Cloud CLI to create the source and destination connection profiles, create the continuous DAG migration job, verify the migration configuration, and start the migration job:

  1. Create the source connection profile.  
Run the [`gcloud database-migration connection-profiles create sqlserver`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver) command (click to expand):

#### `gcloud database-migration connection-profiles create sqlserver`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.
         
         gcloud database-migration connection-profiles create sqlserver SOURCE_CONNECTION_PROFILE_ID \
             --no-async \
             --display-name=SOURCE_CONNECTION_PROFILE_NAME \
             --region=REGION \
             --role=SOURCE \
             --host=SOURCE_HOST_IP_ADDRESS \
             --port=SOURCE_PORT_NUMBER \
             --dbm-port=SOURCE_DBM_PORT_NUMBER \
             --username=SOURCE_USERNAME \
             --password=SOURCE_PASSWORD

Replace the following:

     * `SOURCE_CONNECTION_PROFILE_ID` with a machine-readable identifier for your source connection profile (for example, `sqlserver-dag-source-profile`).
     * `SOURCE_CONNECTION_PROFILE_NAME` with a human-readable name for your source connection profile. This value is displayed in Database Migration Service in the Google Cloud console.
     * `REGION` with the identifier of the region where you want to save the connection profile (for example, `us-central1`).
     * `SOURCE_HOST_IP_ADDRESS` with the private IP address of your source SQL Server instance (or the Availability Group listener IP address if configured for a multi-replica source Availability Group).
     * `SOURCE_PORT_NUMBER` with the port number where your source SQL Server database engine accepts connections (default `1433`).
     * `SOURCE_DBM_PORT_NUMBER` with the TCP port number of your source Database Mirroring endpoint (default `5022`).
     * `SOURCE_USERNAME` with the dedicated SQL login name that you created on your source instance in Create the dedicated Database Migration Service login and permissions.
     * `SOURCE_PASSWORD` with the password for the `SOURCE_USERNAME` login.

  2. Create the destination connection profile.  
Run the [`gcloud database-migration connection-profiles create sqlserver`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver) command (click to expand):

#### `gcloud database-migration connection-profiles create sqlserver`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.
         
         gcloud database-migration connection-profiles create sqlserver DESTINATION_CONNECTION_PROFILE_ID \
             --no-async \
             --display-name=DESTINATION_CONNECTION_PROFILE_NAME \
             --region=REGION \
             --role=DESTINATION \
             --cloudsql-instance=CLOUDSQL_INSTANCE_ID \
             --host=DESTINATION_HOST_IP_ADDRESS \
             --port=DESTINATION_PORT_NUMBER \
             --dbm-port=DESTINATION_DBM_PORT_NUMBER \
             --username=sqlserver \
             --password=CLOUD_SQL_DB_USER_PASSWORD

Replace the following:

     * `DESTINATION_CONNECTION_PROFILE_ID` with a machine-readable identifier for your destination connection profile (for example, `sqlserver-dag-dest-profile`).
     * `DESTINATION_CONNECTION_PROFILE_NAME` with a human-readable name for your destination connection profile. This value is displayed in Database Migration Service in the Google Cloud console.
     * `REGION` with the identifier of the region where you want to save the connection profile.
     * `CLOUDSQL_INSTANCE_ID` with the name of your destination Cloud SQL for SQL Server instance.
     * `DESTINATION_HOST_IP_ADDRESS` with the private IP address of your destination Cloud SQL for SQL Server instance (or its Private Service Connect endpoint IP address) as reachable from your source SQL Server instance.
     * `DESTINATION_PORT_NUMBER` with the database port number of your destination Cloud SQL for SQL Server instance (`1433`).
     * `DESTINATION_DBM_PORT_NUMBER` with the Database Mirroring port number of your destination Cloud SQL for SQL Server instance (`5022`).
     * `CLOUD_SQL_DB_USER_PASSWORD` with the password for the `sqlserver` user on your destination Cloud SQL for SQL Server instance (`--username` must be set to `sqlserver`).

  3. Create the continuous DAG migration job.  
Run the [`gcloud database-migration migration-jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create) command (click to expand):

#### `gcloud database-migration migration-jobs create`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.
         
         gcloud database-migration migration-jobs create MIGRATION_JOB_ID \
             --no-async \
             --display-name=MIGRATION_JOB_NAME \
             --region=REGION \
             --type=CONTINUOUS \
             --source=SOURCE_CONNECTION_PROFILE_ID \
             --destination=DESTINATION_CONNECTION_PROFILE_ID \
             --sqlserver-dag-source-ag=SOURCE_AVAILABILITY_GROUP_NAME \
             --sqlserver-dag-linked-server=LINKED_SERVER_NAME

Replace the following:

     * `MIGRATION_JOB_ID` with a machine-readable identifier for your migration job (for example, `sqlserver-dag-job`).
     * `MIGRATION_JOB_NAME` with a human-readable name for your migration job. This value is displayed in the Google Cloud console.
     * `REGION` with the identifier of the region where you want to create the migration job.
     * `SOURCE_CONNECTION_PROFILE_ID` with the identifier of your source connection profile.
     * `DESTINATION_CONNECTION_PROFILE_ID` with the identifier of your destination connection profile.
     * `SOURCE_AVAILABILITY_GROUP_NAME` with the name of the Availability Group on your source SQL Server instance.
     * `LINKED_SERVER_NAME` with the name of the Linked Server that you configured on your destination Cloud SQL for SQL Server instance in Create and verify the Linked Server on your destination Cloud SQL for SQL Server instance.

  4. Verify the migration job configuration.  
Before starting a DAG migration job, you must run `verify` to validate bidirectional network connectivity, Linked Server RPC access, `gcp_dms_db` permissions (if using least privilege), source database owners (verifying that no database is owned by `sa`), and default data file paths. Run the [`gcloud database-migration migration-jobs verify`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/verify) command (click to expand):

#### `gcloud database-migration migration-jobs verify`
         
         gcloud database-migration migration-jobs verify MIGRATION_JOB_ID \
             --region=REGION

Replace the following:

     * `MIGRATION_JOB_ID` with the identifier of your migration job.
     * `REGION` with the identifier of the region where the migration job is saved.

You can check the status of the verification operation by running the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command.

  5. Start the migration job.  
After verification succeeds, run the [`gcloud database-migration migration-jobs start`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/start) command (click to expand):

#### `gcloud database-migration migration-jobs start`
         
         gcloud database-migration migration-jobs start MIGRATION_JOB_ID \
             --region=REGION

Replace the following:

     * `MIGRATION_JOB_ID` with the identifier of your migration job.
     * `REGION` with the identifier of the region where the migration job is saved.

**Caution:** When you start the DAG migration job, Database Migration Service automatically sets the `cloud sql enable dag support` flag to `on` on your destination Cloud SQL for SQL Server instance. Don't manually modify or remove the `cloud sql enable dag support` flag. 



## Monitor and verify your migration

While the DAG migration job is running, you can monitor its progress in the Google Cloud console, query your destination databases in read-only mode during `CDC`, and manage active replication.

### Monitor progress in the Google Cloud console

You can monitor a running DAG migration job in the Google Cloud console on the **Migration job details** page, just like other Database Migration Service migration jobs:

  * In the **Databases** table on the migration job details page, view the real-time phase (`Full dump` during the initial full load, `CDC` during continuous replication, and any database-level error messages) and **Restore lag** for each database in your Availability Group.
  * In the **Monitoring** tab, view the **Restore lag** (`datamigration.googleapis.com/migration_job/max_replica_sec_lag`, which reports the Distributed Availability Group replication lag in seconds per database) chart.



For more information about monitoring metrics and job states, see [Migration job metrics](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-metrics) and [Migration job status codes](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses).

### Verify migrated databases in read-only mode during CDC

Unlike backup-based migrations (where destination databases remain in the `RESTORING` state until promotion), Distributed Availability Group migrations allow you to query your destination Cloud SQL for SQL Server databases in **read-only mode** as soon as they enter the `CDC` phase.

For each database owned by a SQL login on the source instance, Database Migration Service automatically creates a login on the destination Cloud SQL for SQL Server instance prefixed with `gcp_dms_`, a 6-character identifier, and the source owner name (for example, `gcp_dms_a1b2c3_myowner`). To query the database with that login before promotion, connect to your destination Cloud SQL for SQL Server instance as `sqlserver`, find the generated login name in `sys.server_principals`, and reset its password:
    
    
    SELECT name FROM sys.server_principals WHERE name LIKE 'gcp_dms_%';
    GO
    ALTER LOGIN [GENERATED_DMS_OWNER_LOGIN] WITH PASSWORD = 'NEW_OWNER_PASSWORD';
    GO

Replace the following:

  * `GENERATED_DMS_OWNER_LOGIN` with the generated database owner login name returned by the query.
  * `NEW_OWNER_PASSWORD` with a new password for the login.



For more information about verifying migrated objects and data, see [Verify a migration](https://docs.cloud.google.com/database-migration/docs/sqlserver/verify-migration).

### Manage an active DAG migration job (Optional)

While your migration job is running in the `CDC` phase, you can perform the following management operations:

  * Add or remove databases in your source Availability Group on your source SQL Server instance by running `ALTER AVAILABILITY GROUP ... ADD DATABASE` or `ALTER AVAILABILITY GROUP ... REMOVE DATABASE`. Database Migration Service automatically detects the change on its next polling cycle and updates the destination Cloud SQL for SQL Server instance.
  * Temporarily halt data replication by running [`gcloud database-migration migration-jobs stop`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/stop). Stopping a DAG migration job should only be used for a defined, short period, because updates continue to accumulate in the transaction logs while replication is halted and can cause transaction log disks to fill up. From a stopped state, you can either run [`gcloud database-migration migration-jobs resume`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/resume) to resume data replication, or run [`gcloud database-migration migration-jobs delete`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/delete) to complete the migration and perform the necessary cleanup.
  * Restart a failed migration job by running [`gcloud database-migration migration-jobs restart`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/restart). Restarting a DAG migration job deletes the migrated databases on your destination Cloud SQL for SQL Server instance, recreates the Distributed Availability Group, and re-runs the initial full load over the network.



## Promote, fail back, or complete the migration

When you are ready to switch your applications to Cloud SQL for SQL Server, promote the migration job. In a DAG migration, promoting the job switches Cloud SQL for SQL Server to the read/write Primary and transitions the migration job into the `FAILBACK` phase (`PHASE_FAILBACK` in Google Cloud CLI and API responses) with active reverse replication back to your source SQL Server instance:

  1. Stop application writes to your source SQL Server databases and check the **Restore lag** metric in the Google Cloud console to confirm that replication lag has reached zero.
  2. Promote the migration job to cut over to Cloud SQL.  
Run the [`gcloud database-migration migration-jobs promote`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/promote) command (click to expand):

#### `gcloud database-migration migration-jobs promote`
         
         gcloud database-migration migration-jobs promote MIGRATION_JOB_ID \
             --region=REGION

Replace the following:

     * `MIGRATION_JOB_ID` with the identifier of your migration job.
     * `REGION` with the identifier of the region where the migration job is saved.

During promotion, Database Migration Service performs the following actions:

     * Sets the Distributed Availability Group to synchronous commit, issues a `CHECKPOINT` on all source databases, waits for all transactions to synchronize with zero data loss, and reverses the Availability Group roles so your destination Cloud SQL for SQL Server instance becomes the read/write **Primary** and your original source SQL Server instance becomes the **Secondary**.
     * Keeps the migration job in the `Running` state and transitions the substate to the **`FAILBACK` phase** (`PHASE_FAILBACK` in Google Cloud CLI and API responses), continuously replicating new writes from your destination Cloud SQL for SQL Server back to the source SQL Server instance.

After promotion completes, connect your applications to your new Cloud SQL for SQL Server instance.

  3. (Optional) Fail back to your source SQL Server instance.  
If you encounter an issue after switching your applications to Cloud SQL for SQL Server while the migration job is in the `FAILBACK` phase, you can revert the cutover with zero data loss by stopping application writes on Cloud SQL for SQL Server and running the [`gcloud database-migration migration-jobs promote`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/promote) command with the `--failback` flag (click to expand):

#### `gcloud database-migration migration-jobs promote --failback`
         
         gcloud database-migration migration-jobs promote MIGRATION_JOB_ID \
             --region=REGION \
             --failback

Replace the following:

     * `MIGRATION_JOB_ID` with the identifier of your migration job.
     * `REGION` with the identifier of the region where the migration job is saved.

Running `promote` with the `--failback` flag during the `FAILBACK` phase synchronizes all changes written to Cloud SQL for SQL Server, switches the replication direction again so your original source SQL Server Availability Group becomes the read/write **Primary** and Cloud SQL for SQL Server becomes the **Secondary** , and returns the migration job to the `CDC` phase. Note that `--failback` is valid only when the migration job is in the `FAILBACK` phase; running `promote` without `--failback` during the `FAILBACK` phase (or passing `--failback` during the `CDC` phase) fails validation with a `FAILED_PRECONDITION` error and leaves the migration job running.

  4. (Optional) Stop data replication before deleting the migration job.  
If you want to halt data replication before permanently deleting the migration job, run the [`gcloud database-migration migration-jobs stop`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/stop) command (click to expand):

#### `gcloud database-migration migration-jobs stop`
         
         gcloud database-migration migration-jobs stop MIGRATION_JOB_ID \
             --region=REGION

Replace the following:

     * `MIGRATION_JOB_ID` with the identifier of your migration job.
     * `REGION` with the identifier of the region where the migration job is saved.

**Caution:** Stopping a migration job halts data replication, but should only be used for a defined, short period because updates continue to accumulate in the transaction logs while replication is halted. From a `Stopped` state, you can either run [`gcloud database-migration migration-jobs resume`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/resume) to resume data replication, or run `gcloud database-migration migration-jobs delete` in the next step to complete the migration and perform the necessary cleanup. 
  5. Complete the migration and delete the migration job.  
Once you verify that your applications are fully operational with the new Cloud SQL for SQL Server destination instance, and you no longer need reverse replication to the source SQL Server instance, delete the migration job (from either the `Running` or `Stopped` state) to complete the migration and perform the necessary cleanup. Run the [ `gcloud database-migration migration-jobs delete`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/delete) command (click to expand):

#### `gcloud database-migration migration-jobs delete`

This command returns an interactive confirmation prompt that requires your input to complete. You can skip the confirmation prompt by using the [ optional `--quiet` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet).
         
         gcloud database-migration migration-jobs delete MIGRATION_JOB_ID \
             --region=REGION

Replace the following:

     * `MIGRATION_JOB_ID` with the identifier of your migration job.
     * `REGION` with the identifier of the region where the migration job is saved.

Deleting the migration job completes the migration, stops any active reverse replication, drops the Distributed Availability Group and Database Mirroring certificates on both instances, and lets you enable Cloud SQL for SQL Server features that are restricted during DAG replication (such as [Point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/configure-pitr) or read replicas). 

After you delete the migration job, you can optionally disable or remove the `cloud sql enable dag support` database flag on your destination Cloud SQL for SQL Server instance, drop the Linked Server on your Cloud SQL for SQL Server instance (`EXEC master.dbo.sp_dropserver @server = N'LINKED_SERVER_NAME', @droplogins = 'droplogins';`), and remove the `gcp_dms_db` helper database and migration login on your source SQL Server instance. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
