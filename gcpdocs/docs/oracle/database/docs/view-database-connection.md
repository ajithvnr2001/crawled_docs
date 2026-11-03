---
url: https://docs.cloud.google.com/oracle/database/docs/view-database-connection/
title: View Database Connections information \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T08:18:59.519310+00:00
---

# View Database Connections information  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/view-database-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  View Database Connections information Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view information about your Database Connections.

## View Database Connections information

To view information about your Database Connections, do the following:

### Console

  1. Go to the **Connection profiles** page.

[Go to Connection profiles](https://console.cloud.google.com/oracle/integrations/list)

You can view the list of the Database Connections.

  2. Click the name of a Database Connection to view its details.




### gcloud

  * **List Database Connections**

Use the `gcloud oracle-database database-connections list` command to list Database Connections.
        
        gcloud oracle-database database-connections list \
            --project=PROJECT_ID \
            --location=REGION
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project.
    * REGION: the region where your Database Connections are located.
  * **View Database Connection details**

Use the `gcloud oracle-database database-connections describe` command to view details of a Database Connection.
        
        gcloud oracle-database database-connections describe CONNECTION_ID \
            --project=PROJECT_ID \
            --location=REGION
        

Replace the following:

    * CONNECTION_ID: the ID of the Database Connection.
    * PROJECT_ID: the ID of your Google Cloud project.
    * REGION: the region where your Database Connection is located.



###  API 

  * **List Database Connections**

To list Database Connections, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project.
    * REGION: the region where your Database Connections are located.
  * **View Database Connection details**

To view details of a Database Connection, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections/CONNECTION_ID"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project.
    * REGION: the region where your Database Connection is located.
    * CONNECTION_ID: the ID of the Database Connection.



## States of a Database Connection

A Database Connection has the following states:

State | Description  
---|---  
`CREATING` | The Database Connection is being created. You can't execute SQL statements yet.  
`ACTIVE` | The Database Connection is ready to use.  
`DELETING` | The Database Connection is being deleted.  
`FAILED` | The Database Connection failed to be created. For the reason, check the `lifecycleDetails` field in the output of the `gcloud oracle-database database-connections describe` command. For more information, see [Troubleshoot Database Connections and SQL runtime issues](https://docs.cloud.google.com/oracle/database/docs/troubleshoot-database-connection).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
