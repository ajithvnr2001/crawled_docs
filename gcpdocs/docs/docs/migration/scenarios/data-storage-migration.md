---
url: https://docs.cloud.google.com/docs/migration/scenarios/data-storage-migration/
title: Unstructured data and storage migration \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:20.468616+00:00
---

# Unstructured data and storage migration  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/scenarios/data-storage-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Unstructured data and storage migration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides architectural guidance and migration strategies for transferring unstructured datasets, object storage, and file shares to Cloud Storage on Google Cloud.

If you are a cloud architect, data engineer, or storage administrator, use the information on this page to evaluate data transfer methods, choose online or offline transfer tools, ensure data integrity, and optimize network bandwidth during migration.

Before you read this page, you should know the total size of your source datasets, available network transfer bandwidth, and your target migration timelines.

## Choose a data transfer method

When planning your data transfer, use the following table to choose a transfer method based on your dataset size and network bandwidth:

Scenario | Dataset size | Recommended solution | Considerations  
---|---|---|---  
**Online data transfer over high-bandwidth network** | Terabytes to petabytes |  [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) |  Automated, continuous online transfer with checksum verification.   
**Offline data transfer with limited bandwidth** | Multiple petabytes |  [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/overview) |  Secure, physical appliance shipment to bypass network constraints.   
  
## Online data transfer by using Storage Transfer Service

[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) automates online data transfers from on-premises storage, POSIX file systems, or third-party cloud providers to Cloud Storage.

### Key capabilities of Storage Transfer Service

Storage Transfer Service provides the following capabilities:

  * **Managed scalability** : scale transfers automatically without provisioning or managing local servers.
  * **Data integrity verification** : verify data accuracy automatically during transfer by using end-to-end MD5 checksums.
  * **Continuous incremental synchronization** : synchronize modified files continuously to minimize cutover downtime.



For information about the end-to-end transfer workflow, see [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).

## Offline data transfer by using Transfer Appliance

For large datasets where network bandwidth is constrained, use [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/overview) to ship data physically to Google Cloud.

## What's next

  * [Containerized application migration](https://docs.cloud.google.com/docs/migration/scenarios/container-migration)
  * [Multi-cloud workload migration](https://docs.cloud.google.com/docs/migration/scenarios/multi-cloud-migration)
  * [Storage Transfer Service documentation](https://docs.cloud.google.com/storage-transfer/docs/overview)
  * [Transfer Appliance documentation](https://docs.cloud.google.com/transfer-appliance/docs/4.0/overview)
  * [Data transfer architecture guide](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
