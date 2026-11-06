---
url: https://docs.cloud.google.com/kubernetes-engine/docs/kubernetes-engine-regulatory-compliance/
title: Regulatory support in Google Kubernetes Engine \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:46:11.907346+00:00
---

# Regulatory support in Google Kubernetes Engine  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/kubernetes-engine-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  Regulatory support in Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes the features, configurations and APIs in Google Kubernetes Engine that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Google Kubernetes Engine APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
container.googleapis.com | v1 |  SUPPORTED   
container.googleapis.com | v1alpha1 |  SUPPORTED   
container.googleapis.com | v1beta1 |  SUPPORTED   
containersecurity.googleapis.com | v1 |  SUPPORTED   
containersecurity.googleapis.com | v1beta |  SUPPORTED   
  
### Compliance supported regions

Google Kubernetes Engine is available for Data Boundary for ITAR in the following Google Cloud regions:

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



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Data Boundary for ITAR. By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[container.restrictNoncompliantDiagnosticDataAccess](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `True`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Authentication and authorization | 

  * `audiences`
  * `spec.groups`
  * `spec.token`
  * `spec.user`

  
Filtering and searching | 

  * `filter`

  
Kubernetes configuration | 

  * `cluster.nodeConfig.kubeletConfig.cpuManagerPolicy`
  * `cluster.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.cpuCfsQuotaPeriod`
  * `cluster.nodePools.config.kubeletConfig.evictionSoft.imagefsAvailable`

  
Network configuration | 

  * `cluster.ipAllocationPolicy.nodeIpv4CidrBlock`
  * `cluster.networkConfig.dnsConfig.clusterDnsDomain`
  * `cluster.nodePools.networkConfig.network`

  
Parent resources | 

  * `parent`

  
Resource identification | 

  * `clusterId`
  * `location`
  * `masterProjectId`
  * `name`
  * `projectId`
  * `zone`

  
Resource management and labels | 

  * `cluster.nodeConfig.resourceManagerTags.tags.key`
  * `cluster.resourceLabels.key`
  * `cluster.resourceLabels.value`

  
Storage and disk configuration | 

  * `cluster.nodeConfig.bootDiskKmsKey`
  * `cluster.nodeConfig.diskType`
  * `cluster.nodePools.config.storagePools`

  
Update parameters | 

  * `updateMask.paths`

  
Versioning and specifications | 

  * `apiVersion`
  * `kind`
  * `version`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
