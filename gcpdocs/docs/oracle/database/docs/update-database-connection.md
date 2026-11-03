---
url: https://docs.cloud.google.com/oracle/database/docs/update-database-connection/
title: Update Database Connections \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T08:18:59.936632+00:00
---

# Update Database Connections  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/update-database-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Update Database Connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to update a Database Connection.

You can update the password secret version, wallet secret version, and labels of a Database Connection.

When you want to rotate the database or wallet password, add a new secret version, then update the corresponding property. The service checks access to the new secret and re-validates connectivity.

## Update a Database Connection

To update a Database Connection, do the following:

### gcloud

Use the `gcloud oracle-database database-connections update` command to update a Database Connection.
    
    
    gcloud oracle-database database-connections update CONNECTION_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --password-secret-version="projects/<var>PROJECT_ID</var>/secrets/<var>SECRET_ID</var>/versions/<var>SECRET_VERSION</var>" \
        --wallet-secret-version="projects/<var>PROJECT_ID</var>/secrets/<var>SECRET_ID</var>/versions/<var>SECRET_VERSION</var>" \
        --update-labels=KEY=VALUE
    

Replace the following:

  * CONNECTION_ID: the ID of the Database Connection.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Database Connection is located.
  * For `password-secret-version` property, replace the following: 
    * PROJECT_ID: the ID of your Google Cloud project that contains the secret.
    * SECRET_ID: the ID of the secret.
    * SECRET_VERSION: the new version of the secret to use.
  * For `wallet-secret-version` property, replace the following: 
    * PROJECT_ID: the ID of your Google Cloud project that contains the database wallet.
    * SECRET_ID: the ID of the secret.
    * SECRET_VERSION: the new version of the secret to use.
  * For `update-labels` property, replace the following: 
    * KEY: the key of the label.
    * VALUE: the value of the label.



###  API 

To update a Database Connection, run the following `curl` command, and include only the fields that you want to update.

**Note:** The following `curl` command replaces the full label set, unlike the `gcloud oracle-database database-connections update` command.
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databaseConnections/CONNECTION_ID?updateMask=passwordSecretVersion,walletSecretVersion,labels" \
    -d \
    '{
      "passwordSecretVersion": "projects/PROJECT_ID/secrets/SECRET_ID/versions/SECRET_VERSION",
      "walletSecretVersion": "projects/PROJECT_ID/secrets/SECRET_ID/versions/SECRET_VERSION",
      "labels": {
        "KEY": "VALUE"
      }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Database Connection is located.
  * CONNECTION_ID: the ID of the Database Connection.
  * For `passwordSecretVersion` property, replace the following: 
    * PROJECT_ID: the ID of your Google Cloud project that contains the secret.
    * SECRET_ID: the ID of the secret.
    * SECRET_VERSION: the new version of the secret to use.
  * For `walletSecretVersion` property, replace the following: 
    * PROJECT_ID: the ID of your Google Cloud project that contains the database wallet.
    * SECRET_ID: the ID of the secret.
    * SECRET_VERSION: the new version of the secret to use.
  * For `labels` property, replace the following: 
    * KEY: the key of the label.
    * VALUE: the value of the label.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
