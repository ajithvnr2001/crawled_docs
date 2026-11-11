---
url: https://docs.cloud.google.com/composer/docs/composer-regulatory-compliance/
title: Regulatory support in Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:10:44.355986+00:00
---

# Regulatory support in Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-regulatory-compliance/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Resources ](https://docs.cloud.google.com/composer/docs/resources)



Send feedback 

#  Regulatory support in Managed Service for Apache Airflow Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Managed Service for Apache Airflow that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Managed Service for Apache Airflow APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
composer.googleapis.com | v1 |  SUPPORTED   
composer.googleapis.com | v1alpha2 |  SUPPORTED   
composer.googleapis.com | v1beta1 |  SUPPORTED   
  
### Compliance supported regions

Managed Service for Apache Airflow is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### API fields for sensitive data

#### Resource: composer.googleapis.com/Dag

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `composer.googleapis.com` REST API: `GET` `/v1alpha2/{dag=projects/*/locations/*/environments/*/dags/*}:getSourceCode` RPC methods:

  * `google.cloud.orchestration.airflow.dags.v1alpha2.Dags.GetSourceCode`

| 

  * `code`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Airflow command execution | 

  * `command`
  * `executionId`
  * `parameters`
  * `pod`
  * `subcommand`

  
Database and encryption configuration | 

  * `environment.config.databaseConfig.machineType`
  * `environment.config.databaseConfig.zone`
  * `environment.config.encryptionConfig.kmsKeyName`
  * `environment.storageConfig.bucket`

  
Environment software configuration | 

  * `environment.config.softwareConfig.airflowConfigOverrides.key`
  * `environment.config.softwareConfig.airflowConfigOverrides.value`
  * `environment.config.softwareConfig.envVariables.key`
  * `environment.config.softwareConfig.envVariables.value`
  * `environment.config.softwareConfig.pypiPackages.key`
  * `environment.config.softwareConfig.pypiPackages.value`

  
Maintenance and recovery configuration | 

  * `environment.config.maintenanceWindow.recurrence`
  * `environment.config.recoveryConfig.scheduledSnapshotsConfig.snapshotCreationSchedule`
  * `environment.config.recoveryConfig.scheduledSnapshotsConfig.snapshotLocation`
  * `environment.config.recoveryConfig.scheduledSnapshotsConfig.timeZone`
  * `snapshotLocation`
  * `snapshotPath`

  
Network and connectivity | 

  * `environment.config.masterAuthorizedNetworksConfig.cidrBlocks.cidrBlock`
  * `environment.config.masterAuthorizedNetworksConfig.cidrBlocks.displayName`
  * `environment.config.nodeConfig.network`
  * `environment.config.nodeConfig.subnetwork`
  * `environment.config.webServerNetworkAccessControl.allowedIpRanges.description`
  * `environment.config.webServerNetworkAccessControl.allowedIpRanges.value`

  
Node configuration | 

  * `environment.config.nodeConfig.composerInternalIpv4CidrBlock`
  * `environment.config.nodeConfig.composerNetworkAttachment`
  * `environment.config.nodeConfig.location`
  * `environment.config.nodeConfig.machineType`
  * `environment.config.nodeConfig.serviceAccount`
  * `environment.config.nodeConfig.tags`

  
Paging and filtering | 

  * `filter`
  * `pageToken`
  * `updateMask.paths`

  
Resource identification | 

  * `environment`
  * `environment.labels.key`
  * `environment.labels.value`
  * `environment.name`
  * `name`
  * `parent`

  
User workloads configuration | 

  * `userWorkloadsConfigMap.data.key`
  * `userWorkloadsConfigMap.data.value`
  * `userWorkloadsConfigMap.name`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
