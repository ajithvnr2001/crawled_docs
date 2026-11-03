---
url: https://docs.cloud.google.com/oracle/database/docs/delete-database-connection/
title: Delete Database Connections \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T08:18:59.714129+00:00
---

# Delete Database Connections  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/delete-database-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Delete Database Connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete a Database Connection.

## Delete a Database Connection

To delete a Database Connection, do the following:

### gcloud

Use the `gcloud oracle-database database-connections delete` command to delete a Database Connection.
    
    
    gcloud oracle-database database-connections delete CONNECTION_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * CONNECTION_ID: the ID of the Database Connection.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Database Connection is located.



###  API 

To delete a Database Connection, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections/CONNECTION_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Database Connection is located.
  * CONNECTION_ID: the ID of the Database Connection.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
