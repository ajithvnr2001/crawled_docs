---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/
title: Minimum permissions required for the Cloud Data Fusion Service Account \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:03:16.698535+00:00
---

# Minimum permissions required for the Cloud Data Fusion Service Account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/

[ Skip to main content ](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/)
  * [Deutsch](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=de)
  * [Español](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=es-419)
  * [Français](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=id)
  * [Italiano](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=it)
  * [Português](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=ja)
  * [한국어](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Required permissions for the Cloud Data Fusion Service Account](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/#permissions)
  * [What's next](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)


Was this helpful?
Send feedback 
#  Minimum permissions required for the Cloud Data Fusion Service Account Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Required permissions for the Cloud Data Fusion Service Account](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/#permissions)
  * [What's next](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions/#whats_next)


This document explains which permissions to give to the Cloud Data Fusion Service Account when you create a custom role that lets it access your resources.
By default, the [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) Identity and Access Management role is assigned to the Cloud Data Fusion Service Account. This role is highly permissive. Instead, you can use custom roles to provide only the permissions that the service account principal needs.
For more information about the Cloud Data Fusion service accounts, see [Service accounts in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts).
For more information about creating custom roles, see [Create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating).
## Required permissions for the Cloud Data Fusion Service Account
When you create a custom role for the Cloud Data Fusion Service Account, give the following permissions based on the tasks you plan to perform in your instance. This lets Cloud Data Fusion access your resources.  
| Task  | Permissions required  |  
| --- | --- |  
| Get Managed Service for Apache Spark clusters  | 
  * `dataproc.clusters.get`

 |  
| Create Cloud Storage bucket per Cloud Data Fusion instance and upload files for Managed Service for Apache Spark job execution  | 
  * `storage.buckets.get`
  * `storage.objects.get`
  * `storage.buckets.create`
  * `storage.objects.create`
  * `storage.objects.update`
  * `storage.buckets.delete`
  * `storage.objects.delete`

 |  
| Publish logs to Cloud Logging  | 
  * `logging.logEntries.create`

 |  
| Publish Cloud metrics to Cloud Monitoring  | 
  * `monitoring.metricDescriptors.create`
  * `monitoring.metricDescriptors.get`
  * `monitoring.metricDescriptors.list`
  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`
  * `monitoring.timeSeries.create`

 |  
| Create a Cloud Data Fusion instance with [VPC peering](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip)  | 
  * `compute.globalOperations.get`
  * `compute.networks.addPeering`
  * `compute.networks.removePeering`
  * `compute.networks.update`
  * `compute.networks.get`

 |  
| Create a Cloud Data Fusion instance with [ DNS peering zone](https://docs.cloud.google.com/data-fusion/docs/how-to/resolve-domain-names) between customer and tenant projects  | 
  * `dns.managedZones.create`
  * `dns.managedZones.delete`
  * `dns.managedZones.get`
  * `dns.managedZones.list`
  * `dns.networks.bindPrivateDNSZone`
  * `dns.networks.targetWithPeeringZone`

 |  
| Create a Cloud Data Fusion instance with [Private Service Connect](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect)  | 
  * `compute.networkAttachments.get`
  * `compute.networkAttachments.update`
  * `compute.networkAttachments.list`

 |  
## What's next
  * Learn more about [creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).
  * Learn more about [access control options in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/access-control).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
