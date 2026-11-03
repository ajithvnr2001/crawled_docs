---
url: https://docs.cloud.google.com/oracle/database/docs/create-database-connection/
title: Create Database Connections \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T08:19:00.324601+00:00
---

# Create Database Connections  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/create-database-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Create Database Connections Stay organized with collections  Save and categorize content based on your preferences. 

Oracle Database@Google Cloud lets you create Database Connections. A Database Connection is a reusable, secure pointer to a specific Oracle database and user which lets Oracle Database@Google Cloud connect to the databases on your ODB Network.

You can use Database Connections to run SQL statements on your Oracle databases through applications, automation scripts, and agents, such as Model Context Protocol (MCP) server.

You can use Database Connections to run SQL statements on Oracle databases that are reachable through your ODB Network, such as Autonomous AI Databases, Exadata VM Cluster databases, and DB systems.

## Before you begin

  * Make sure that your ODB Network has service connectivity enabled.

You can either [Create a new ODB Network](https://docs.cloud.google.com/oracle/database/docs/create-odb-network) with service connectivity enabled, or [enable service connectivity on an existing ODB Network](https://docs.cloud.google.com/oracle/database/docs/create-odb-network#enable-service-connectivity).

  * Create a secret for the password and the wallet (required for mTLS only). For more information, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).




### Required roles and permissions

This section describes the Identity and Access Management (IAM) roles and permissions required to create and manage Database Connections, and execute SQL statements.

For more information about how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

#### Roles and permissions required to create and manage Database Connections, and execute SQL statements

Grant the following permissions to the user:

  * `oracledatabase.databaseConnections.list`: to list Database Connections.
  * `oracledatabase.databaseConnections.get`: to get Database Connection details.
  * `oracledatabase.databaseConnections.create`: to create a Database Connection.
  * `oracledatabase.databaseConnections.update` permission: to update a Database Connection.
  * `oracledatabase.databaseConnections.delete`: to delete a Database Connection.
  * `oracledatabase.databaseConnections.test`: to test a Database Connection.
  * `oracledatabase.databaseConnections.executeSql`: to execute SQL statements.
  * `oracledatabase.odbNetworks.use`: to use the ODB Network.
  * `oracledatabase.odbNetworks.get`: to get ODB Network details.

**Note:** `oracledatabase.databaseConnections.executeSql` is a data-access permission. It can read and modify database data, limited only by the privileges of the database user configured on the connection.



Oracle Database@Google Cloud Admin (`roles/oracledatabase.admin`) contains all the required permissions.

To follow the principles of least privilege, you can create a custom role. For example:

  * A "SQL runner" for an application or agent that contains the following permissions:
        
        oracledatabase.databaseConnections.get
        oracledatabase.databaseConnections.list
        oracledatabase.databaseConnections.executeSql
        

  * A "Connection manager" that contains the following permissions:
        
        oracledatabase.databaseConnections.*
        oracledatabase.odbNetworks.use
        oracledatabase.odbNetworks.get
        




#### Roles and permissions required to access secrets

When you create, update, test, or run SQL statements on a Database Connection, Oracle Database@Google Cloud uses a Google-managed service agent to read your database password secret and your wallet secret from Secret Manager.

The Oracle Database@Google Cloud service agent has the following email format:
    
    
    service-PROJECT_NUMBER@gcp-sa-oci.iam.gserviceaccount.com
    

Where PROJECT_NUMBER is the project number of the project that contains your ODB Network.

Grant the following role to the Oracle Database@Google Cloud service agent on the password secret and the wallet secret (if you configured one for mTLS):

  * Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)



Run the following command to grant the role:
    
    
    gcloud secrets add-iam-policy-binding SECRET_ID \
        --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-oci.iam.gserviceaccount.com" \
        --role="roles/secretmanager.secretAccessor" \
        --project=SECRET_PROJECT_ID
    

Replace the following:

  * SECRET_ID: the ID of the password or wallet secret in Secret Manager.
  * PROJECT_NUMBER: the project number of the project that contains your ODB Network.
  * SECRET_PROJECT_ID: the ID of the project that contains the secret.

**Note:** When validating connectivity, the create Database Connection and test Database Connection operations read the secret as the service agent of the project that hosts the ODB Network. However, the update Database Connection operation re-checks access as the service agent of the project that contains the Database Connection. If you're using Shared VPC, and both your ODB Network and Database Connection are in different projects, then grant the role to both service agents.

## Create database connection

When you create a Database Connection, its connectivity is validated at the time of creation. The service connects to the database with the given credentials before it accepts the create request. Wrong passwords, unreachable hosts, missing secret access, and TLS problems can fail the create call itself, not just the later queries.

To create a Database Connection, do the following:

### gcloud

Use the `gcloud oracle-database database-connections create` command to create a Database Connection.
    
    
    gcloud oracle-database database-connections create CONNECTION_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --display-name="DISPLAY_NAME" \
        --connection-string="CONNECTION_STRING" \
        --username="USERNAME" \
        --password-secret-version="projects/<var>PROJECT_ID</var>/secrets/<var>SECRET_ID</var>/versions/<var>SECRET_VERSION</var>" \
        --odb-network="projects/<var>PROJECT_ID</var>/locations/<var>REGION</var>/odbNetworks/<var>ODB_NETWORK_ID</var>" \
        --wallet-secret-version="projects/<var>PROJECT_ID</var>/secrets/<var>SECRET_ID</var>/versions/<var>SECRET_VERSION</var>"
    

Replace the following:

  * CONNECTION_ID: a unique ID for the Database Connection as per the following naming conventions:

    * Must start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens.
    * Must end with a lowercase letter or digit.
    * Must be between 1 and 63 characters.
  * PROJECT_ID: the ID of your Google Cloud project in which you want to create the Database Connection.

  * REGION: the region where you want to create the Database Connection.

  * DISPLAY_NAME: a display name for the Database Connection.

  * CONNECTION_STRING: the connection string of your database. It can be either **Oracle Easy Connect** (`host:port/service_name`) or **TNS descriptor**. For more information, see Connection string rules.

  * USERNAME: the database user that SQL runs as. For example, a dedicated application user with only the privileges it needs. The user's database privileges determine the SQL operations the user can perform.

  * For `password-secret-version` property, replace the following:

    * PROJECT_ID: the ID of your Google Cloud project that contains the secret.
    * SECRET_ID: the ID of the secret.
    * SECRET_VERSION: the version of the secret that contains the user's password.
  * For `odb-network` property, replace the following:

    * PROJECT_ID: the ID of your Google Cloud project that contains the ODB Network.
    * REGION: the region where the ODB Network is located.
    * ODB_NETWORK_ID: the ID of the ODB Network that you want to associate with the Database Connection.
  * For `wallet-secret-version` property, replace the following:

    * PROJECT_ID: the ID of your Google Cloud project that contains the secret.
    * SECRET_ID: the ID of the secret.
    * SECRET_VERSION: the version of the secret that contains the database wallet.



###  API 

To create a Database Connection, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections?databaseConnectionId=CONNECTION_ID" \
    -d \
    '{
      "displayName": "DISPLAY_NAME",
      "username": "USERNAME",
      "connectionString": "CONNECTION_STRING",
      "passwordSecretVersion": "projects/PROJECT_ID/secrets/SECRET_ID/versions/SECRET_VERSION",
      "odbNetwork": "projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID",
      "walletSecretVersion": "projects/PROJECT_ID/secrets/SECRET_ID/versions/SECRET_VERSION"
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project in which you want to create the Database Connection.
  * REGION: the region where you want to create the Database Connection.
  * CONNECTION_ID: a unique ID for the Database Connection as per the following naming conventions:

    * Must start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens.
    * Must end with a lowercase letter or digit.
    * Must be between 1 and 63 characters.
  * DISPLAY_NAME: a display name for the Database Connection.

  * CONNECTION_STRING: the connection string of your database. It can be either **Oracle Easy Connect** (`host:port/service_name`) or **TNS descriptor**. For more information, see Connection string rules.

  * USERNAME: the database user that SQL runs as. For example, a dedicated application user with only the privileges it needs. The user's database privileges determine the SQL operations the user can perform.

  * For `password-secret-version` property, replace the following:

    * PROJECT_ID: the ID of your Google Cloud project that contains the secret.
    * SECRET_ID: the ID of the secret.
    * SECRET_VERSION: the version of the secret that contains the user's password.
  * For `odb-network` property, replace the following:

    * PROJECT_ID: the ID of your Google Cloud project that contains the ODB Network.
    * REGION: the region where the ODB Network is located.
    * ODB_NETWORK_ID: the ID of the ODB Network that you want to associate with the Database Connection.
  * For `walletSecretVersion` property, replace the following:

    * PROJECT_ID: the ID of your Google Cloud project that contains the secret.
    * SECRET_ID: the ID of the secret.
    * SECRET_VERSION: the version of the secret that contains the database wallet.



If the create operation fails, see [Troubleshoot Database Connections and SQL runtime issues](https://docs.cloud.google.com/oracle/database/docs/troubleshoot-database-connection).

## Connection string rules

When providing a connection string for a Database Connection, consider the following:

  * Following formats are accepted:

    * Easy Connect: `host[:port]/service_name` (optionally with a leading `//`).
    * TNS descriptor: `(DESCRIPTION=(ADDRESS=...)(CONNECT_DATA=...)...)`. It must contain both `ADDRESS=` and `CONNECT_DATA=`.
  * Following syntax and parameters aren't supported:

    * **Easy Connect Plus** syntax, such as a protocol prefix like `tcps://` or parameters after `?`.

Use a TNS descriptor instead.

    * High-availability and timeout parameters in TNS:

      * `FAILOVER`
      * `FAILOVER_MODE`
      * `LOAD_BALANCE`
      * `RETRY_COUNT`
      * `RETRY_DELAY`
      * `CONNECT_TIMEOUT`
      * `TRANSPORT_CONNECT_TIMEOUT`

You must remove these parameters from the connection string copied from the Oracle console. For example, Autonomous AI Database profile strings include `retry_count` and `retry_delay` by default and must be removed before using with Database Connection.

  * Use the database's private IP as the host. DNS names of private endpoints aren't yet resolvable over the Private Service Connect interface path.

Do the following:

    * Use the database's private IP (`ADB: properties.privateEndpointIp`) as `HOST`.
    * Keep TLS hostname verification by adding `(SECURITY=(SSL_SERVER_DN_MATCH=YES)(SSL_SERVER_CERT_DN="CN=<original-hostname>"))`.

Example: Autonomous AI Database with TLS without wallet:
    
    (description=(address=(protocol=tcps)(port=1521)(host=10.10.0.5))(connect_data=(service_name=abc123_mydb_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)(ssl_server_cert_dn="CN=xyz.adb.us-ashburn-1.oraclecloud.com")))
    

  * TLS versus mTLS: For Autonomous AI Database with TLS (port 1521, no wallet) no wallet is needed. For mTLS (port 1522), provide `walletSecretVersion`.




## What's next

  * [Test Database Connections](https://docs.cloud.google.com/oracle/database/docs/test-database-connection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
