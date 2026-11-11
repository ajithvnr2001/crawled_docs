---
url: https://docs.cloud.google.com/oracle/database/docs/test-database-connection/
title: Test Database Connections \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:28:21.988494+00:00
---

# Test Database Connections  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/test-database-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Test Database Connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to test a Database Connection.

After creating or updating a Database Connection, you can test it to check whether it was configured successfully.

## Test a Database Connection

To test a Database Connection, do the following:

### gcloud

Use the `gcloud oracle-database database-connections test` command to test a Database Connection.
    
    
    gcloud oracle-database database-connections test CONNECTION_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * CONNECTION_ID: the ID of the Database Connection.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Database Connection is located.



###  API 

To test a Database Connection, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections/CONNECTION_ID:test"
    -d '{}'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Database Connection is located.
  * CONNECTION_ID: the ID of the Database Connection.



If the test succeeds, then the response contains `{"success": true}`.

The test might fail with the following types of errors:

  * **API errors** : Authentication failures, database unavailability, network errors, and timeouts are returned as standard API errors (HTTP 4xx/5xx), not as `status: ERROR`.
  * **ORA errors** : ORA errors occur when the query is invalid. For example, `ORA-00942: table or view does not exist`. Oracle rejects the query and the call succeeds with `HTTP 200`. However, the `metadata.status` is `ERROR`. Therefore, check the `metadata.status` and `metadata.message` to determine the cause of the error.



For more information, see [Troubleshoot Database Connections and SQL runtime issues](https://docs.cloud.google.com/oracle/database/docs/troubleshoot-database-connection).

## What's next

  * [Execute SQL statements](https://docs.cloud.google.com/oracle/database/docs/execute-sql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 
