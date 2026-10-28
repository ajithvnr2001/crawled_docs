---
url: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/
title: Troubleshoot deleting clusters \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:02:07.957494+00:00
---

# Troubleshoot deleting clusters  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/

[ Skip to main content ](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/)
  * [Deutsch](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=de)
  * [Español](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=es-419)
  * [Français](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=id)
  * [Italiano](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=it)
  * [Português](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=ja)
  * [한국어](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Skip cluster deletion](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/#skip_cluster_deletion)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)


Was this helpful?
Send feedback 
#  Troubleshoot deleting clusters Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Skip cluster deletion](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/#skip_cluster_deletion)


This page shows you how to resolve issues with deleting ephemeral Managed Service for Apache Spark clusters in Cloud Data Fusion.
When Cloud Data Fusion creates an ephemeral Managed Service for Apache Spark cluster during pipeline run provisioning, the cluster gets deleted after the pipeline run is finished. In rare cases, the cluster deletion fails.
**Strongly recommended** : Upgrade to the most recent Cloud Data Fusion version to ensure proper cluster maintenance.
## Skip cluster deletion
For debugging purposes, you can stop the automatic deletion of an ephemeral cluster.
To stop the deletion, set the `Skip Cluster Deletion` property to `True`. You must manually delete the cluster after you finish debugging.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
