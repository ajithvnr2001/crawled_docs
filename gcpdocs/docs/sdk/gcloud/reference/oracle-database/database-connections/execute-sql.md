---
url: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/database-connections/execute-sql/
title: gcloud oracle-database database-connections execute-sql \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:39:11.707703+00:00
---

# gcloud oracle-database database-connections execute-sql  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/database-connections/execute-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud oracle-database database-connections execute-sql Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud oracle-database database-connections execute-sql - execute a SQL statement on a DatabaseConnection 
SYNOPSIS
    

`gcloud oracle-database database-connections execute-sql` (`DATABASE_CONNECTION` : `--location`=`LOCATION`) `--sql-statement`=`SQL_STATEMENT` [`--params`=[`name`=`NAME`],[`typeName`=`TYPENAME`],[`value`=`VALUE`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Executes a SQL statement on a DatabaseConnection. Supports `SELECT` queries as well as DML and DDL statements, which are autocommitted. 
EXAMPLES
     To execute a SQL statement on a DatabaseConnection with id `my-connection` in the location `us-east4`, run: 
    
    
    gcloud oracle-database database-connections execute-sql my-connection --location=us-east4 --sql-statement="SELECT 1 FROM DUAL"

To execute a parameterized SQL statement with bind variables (where `value` takes JSON) on a DatabaseConnection with id `my-connection` in the location `us-east4`, run: 
    
    
    gcloud oracle-database database-connections execute-sql my-connection --location=us-east4 --sql-statement="SELECT * FROM employees WHERE department_id = :dept_id AND status = :status" --params='name=dept_id,value=10' --params='name=status,value="ACTIVE"'

POSITIONAL ARGUMENTS
    

DatabaseConnection resource - The name of the DatabaseConnection in the following format: projects/{project}/locations/{location}/databaseConnections/{database_connection}. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `database_connection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATABASE_CONNECTION`
     ID of the databaseConnection or fully qualified identifier for the databaseConnection. 

To set the `database_connection` attribute: 

  * provide the argument `database_connection` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the databaseConnection resource. 

To set the `location` attribute: 

  * provide the argument `database_connection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--sql-statement`=`SQL_STATEMENT`
     The SQL statement to execute. 
OPTIONAL FLAGS
    

`--params`=[`name`=`NAME`],[`typeName`=`TYPENAME`],[`value`=`VALUE`]
     Optional: Bind variables (parameters) to be used with the SQL statement. Supports named bind variables (e.g., :dept_id, :status in Oracle SQL) or positional parameters (:1, :2). 

`name`
     The name of the SQL bind parameter (excluding the leading colon, e.g. "id"). If omitted, parameters bind positionally based on their order in the list. 
`typeName`
     Optional: Datatype hint for the parameter (e.g., "VARCHAR2", "NUMBER", "DATE", "TIMESTAMP"). If omitted, the Oracle driver will infer the type from the value string. 
`value`
     Use protobuf.Value so clients can pass ints, bools, and strings natively. 
`Shorthand Example:`
    
    
    --params=name=string,typeName=string,value={…} --params=name=string,typeName=string,value={…}

`JSON Example:`
    
    
    --params='[{"name": "string", "typeName": "string", "value": {…}}]'

`File Example:`
    
    
    --params=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `oracledatabase/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/oracle/database/docs>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
