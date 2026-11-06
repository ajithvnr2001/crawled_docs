---
url: https://docs.cloud.google.com/storage-transfer/docs/source-s3-compatible/
title: Configure access to a source: S3-compatible storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:53:06.312524+00:00
---

# Configure access to a source: S3-compatible storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/source-s3-compatible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a source: S3-compatible storage Stay organized with collections  Save and categorize content based on your preferences. 

To transfer data from an S3-compatible object storage provider (such as Ceph, MinIO, Cloudflare R2, or Wasabi), you must obtain API credentials from your storage provider and configure Storage Transfer Service agents with access to the source bucket.

## Prerequisites

Before configuring your transfer, ensure you have set up the following:

  * **User permissions:** Ensure your user account or user-managed service account has permission to configure transfers and agent pools. See [Required user permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-user).
  * **Agent-based project-level permissions:** Ensure you have configured the required project-level roles for your service agent and transfer agent account. See [Agent-based project-level permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-agent-based).
  * **Destination bucket permissions:** Grant the required permissions on your destination Cloud Storage bucket. See [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).



## Required source permissions

To authenticate to your S3-compatible storage provider, obtain an **access key ID** and **secret access key** from your provider's management console.

Ensure the access key credentials have the following minimum permissions on the source bucket:

Permission | Description | Required  
---|---|---  
`s3:ListBucket` | Allows Storage Transfer Service to list objects in the source bucket. | Always required.  
`s3:GetObject` | Allows Storage Transfer Service to read objects from the source bucket. | Always required.  
`s3:DeleteObject` | Allows Storage Transfer Service to delete source objects after copying. | Required if `deleteObjectsFromSourceAfterTransfer` is enabled.  
  
You provide these credentials as environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`) when starting your transfer agents.

## What's next

  * Learn how to [Install transfer agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents).
  * Learn how to [Manage agent pools](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools).
  * Learn how to [Transfer from S3-compatible storage to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agent-based/s3-compatible).
  * Learn how to [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
