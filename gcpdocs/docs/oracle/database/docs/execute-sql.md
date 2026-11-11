---
url: https://docs.cloud.google.com/oracle/database/docs/execute-sql/
title: Execute SQL statements \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:28:46.620632+00:00
---

# Execute SQL statements  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/execute-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Execute SQL statements Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to execute SQL statements against Oracle databases.

You can execute all types of SQL statements including data manipulation language (DML), data definition language (DDL), and data query language (DQL).

You can use [Database Connections](https://docs.cloud.google.com/oracle/database/docs/create-database-connection) to run SQL statements on Oracle databases that are reachable through your ODB Network, such as Autonomous AI Databases, Exadata VM Cluster databases, and DB systems.

## Before you begin

  1. Completed all the prerequisites described in [create Database Connection](https://docs.cloud.google.com/oracle/database/docs/create-database-connection#before-you-begin).
  2. Grant the [required roles and permissions](https://docs.cloud.google.com/oracle/database/docs/create-database-connection#required-roles-and-permissions).
  3. [Create a Database Connection](https://docs.cloud.google.com/oracle/database/docs/create-database-connection#create-database-connection).
  4. [Test the Database Connection](https://docs.cloud.google.com/oracle/database/docs/test-database-connection).

If the test is successful, then you can use your Database Connection to execute SQL statements.

If the test fails, see [Troubleshoot Database Connections and SQL runtime issues](https://docs.cloud.google.com/oracle/database/docs/troubleshoot-database-connection).




## Execute SQL statements

For executing SQL statements, consider the following:

  * **Autocommit** : Each call is its own transaction. There are no multi-statement transactions across calls.
  * **API errors** : Authentication failures, database unavailability, network errors, and timeouts are returned as standard API errors (HTTP 4xx/5xx), not as `status: ERROR`.
  * **ORA errors** : ORA errors occur when the query is invalid. For example, `ORA-00942: table or view does not exist`. Oracle rejects the query and the call succeeds with `HTTP 200`. However, the `metadata.status` is `ERROR`. Therefore, check the `metadata.status` and `metadata.message` to determine the cause of the error.
  * **Result size limit** : Large results are cut off and `status: PARTIAL` is returned. The current limit is 10 MB (10,485,760 bytes) per response.
  * **Timeouts** : The current statement timeout is 30 seconds, and the API deadline is 60 seconds. Timeouts return `QUERY_TIMEOUT`.
  * **Security** : We recommend using bind variables (`params`) instead of building SQL strings by concatenation, to prevent SQL injection. 

Also, since `database_connection_executesql` is marked `destructive_hint: true` and runs DML and DDL statements with autocommit, an agent (including one manipulated through prompt injection) can modify or drop data. We recommend creating connections used by agents with a least-privilege or read-only database user.




To execute a SQL statement, do the following:

### gcloud

Use the `gcloud oracle-database database-connections execute-sql` command to execute a SQL statement.
    
    
    gcloud oracle-database database-connections execute-sql CONNECTION_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --sql-statement="SQL_STATEMENT" \
        --params='name=NAME,value=VALUE'
    

Replace the following:

  * CONNECTION_ID: the ID of the Database Connection.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Database Connection is located.
  * SQL_STATEMENT: the SQL statement to execute. If the statement contains spaces or shell special characters, then it must be quoted. Runs in autocommit.
  * The `params` property lets you specify optional bind variables. Replace the following: 
    * NAME: the name of the variable.
    * VALUE: the value of the variable.



###  API 

To execute a SQL statement, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections/CONNECTION_ID:executeSql" \
    -d \
    '{
      "sqlStatement": "SQL_STATEMENT",
      "params": [{ "name": "NAME", "value": "VALUE" }]
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Database Connection is located.
  * CONNECTION_ID: the ID of the Database Connection.
  * SQL_STATEMENT: the SQL statement to execute. If the statement contains spaces or shell special characters, then it must be quoted. Runs in autocommit.
  * The `params` property lets you specify optional bind variables. Replace the following: 
    * NAME: the name of the variable.
    * VALUE: the value of the variable.



## Sample execute SQL commands

  * **Parameterized SELECT statement**
        
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections/CONNECTION_ID:executeSql" \
        -d \
        '{
          "sqlStatement": "SELECT :val AS greeting FROM DUAL",
          "params": [{ "name": "val", "value": "Hello World" }]
        }'
        

  * **Create table**
        
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections/CONNECTION_ID:executeSql" \
        -d \
        '{
          "sqlStatement": "CREATE TABLE customers (customer_id INTEGER GENERATED BY DEFAULT ON NULL AS IDENTITY, email_address VARCHAR2(255) NOT NULL, full_name VARCHAR2(255) NOT NULL, CONSTRAINT customers_pk PRIMARY KEY (customer_id), CONSTRAINT customers_email_u UNIQUE (email_address))"
        }'
        

  * **Insert rows**
        
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections/CONNECTION_ID:executeSql" \
        -d \
        '{
          "sqlStatement": "INSERT ALL INTO customers (customer_id, email_address, full_name) VALUES (1, 'alex@example.com', 'Alex C') INTO customers (customer_id, email_address, full_name) VALUES (2, 'charlie@example.com', 'Charlie V') INTO customers (customer_id, email_address, full_name) VALUES (3, 'kim@example.com', 'Kim R') SELECT 1 FROM DUAL"
        }'
        

  * **Query with a bind variable**
        
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections/CONNECTION_ID:executeSql" \
        -d \
        '{
          "sqlStatement": "SELECT customer_id, full_name FROM customers WHERE customer_id <= :max_id ORDER BY customer_id",
          "params": [{ "name": "max_id", "value": 2, "typeName": "NUMBER" }]
        }'
        

  * **Example response**
        
        {
          "sqlResults": [{
            "columns": [{ "name": "CUSTOMER_ID", "type": "NUMBER" }, { "name": "FULL_NAME", "type": "VARCHAR2" }],
            "rows": [{ "values": [{ "value": "1" }, { "value": "Alex C" }] }]
          }],
          "metadata": { "status": "OK", "executionDuration": "0.092s" }
        }
        




## Execute SQL statements using Oracle Database@Google Cloud remote MCP server

You can also execute SQL statements on your databases through MCP remote server.

For more information, see [Use the Oracle Database@Google Cloud remote MCP server](https://docs.cloud.google.com/oracle/database/docs/use-oracledatabase-mcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 
