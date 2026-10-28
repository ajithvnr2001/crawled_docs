---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/serverless-staging-bucket/
title: Managed Service for Apache Spark staging buckets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:58:12.379848+00:00
---

# Managed Service for Apache Spark staging buckets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/serverless-staging-bucket/




#  Managed Service for Apache Spark staging buckets Stay organized with collections  Save and categorize content based on your preferences. 

Staging buckets let you store workload dependencies, configuration files, and job driver console output for Managed Service for Apache Spark. When you run workloads, the service creates a Cloud Storage bucket in your project or reuses an existing staging bucket from previous batch creation requests. For more information, see [Managed Service for Apache Spark staging and temp buckets](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket).

The service manages these project-level buckets in [Cloud Storage locations](https://docs.cloud.google.com/storage/docs/locations#location-r) matching workload Compute Engine zones. Workloads in the same region share buckets, which are created with Cloud Storage [soft delete retention](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) set to 0 seconds.

To locate the Managed Service for Apache Spark default staging bucket, in the Google Cloud console, go to **[Cloud Storage](https://console.cloud.google.com/storage/browser)** and filter the results using the `dataproc-staging-` prefix. 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
