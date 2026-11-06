---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/parameter-manager-regulatory-compliance/
title: Regulatory support in Secret Manager \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T08:21:04.187090+00:00
---

# Regulatory support in Secret Manager  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/parameter-manager-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/secret-manager/docs/resources)



Send feedback 

#  Regulatory support in Secret Manager Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Secret Manager that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Secret Manager APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
parametermanager.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Secret Manager is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### API fields for sensitive data

#### Resource: parametermanager.googleapis.com/ParameterVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `parametermanager.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/parameters/*}/versions` RPC methods:

  * `google.cloud.parametermanager.v1.ParameterManager.CreateParameterVersion`

| 

  * `parameterVersion.payload.data`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Filtering and sorting | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Metadata, labels, and tags | 

  * `parameter.labels.key`
  * `parameter.labels.value`
  * `parameter.tags.key`
  * `parameter.tags.value`

  
Operational control and encryption | 

  * `parameter.kmsKey`
  * `requestId`
  * `updateMask.paths`

  
Resource identification and naming | 

  * `name`
  * `parameter.name`
  * `parameterId`
  * `parameterVersion.name`
  * `parameterVersionId`
  * `parent`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
