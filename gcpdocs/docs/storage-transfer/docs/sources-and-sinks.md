---
url: https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks/
title: Sources and sinks \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:53:06.091072+00:00
---

# Sources and sinks  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Sources and sinks Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service supports transfers across cloud object stores, URL lists, and on-premises or cloud file systems. The following table details the supported sources, destinations, and transfer types.

Storage system | Source | Destination | Transfer type | Notes  
---|---|---|---|---  
Cloud Storage | check_circle | check_circle | Agentless or agent-based | Cloud Storage is a valid sink for transfers from all sources. Transfers between cloud systems are agentless. Transfers paired with file systems are agent-based. To configure Cloud Storage as a source or sink, refer to the following pages:

  * [Configure access to a source: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage)
  * [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage)

  
Amazon Simple Storage Service (Amazon S3) | check_circle |  | Agentless | Transfers to Cloud Storage only. To configure Amazon S3, refer to [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3).  
S3-compatible storage | check_circle |  | Agent-based | Transfers to Cloud Storage only. To configure S3-compatible storage, refer to [Configure access to a source: S3-compatible storage](https://docs.cloud.google.com/storage-transfer/docs/source-s3-compatible).  
Azure Blob Storage, including Azure Data Lake Storage Gen2 | check_circle |  | Agentless | Transfers to Cloud Storage only. To configure Azure storage options, refer to [Configure access to a source: Microsoft Azure Storage](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure).  
Publicly accessible or signed HTTP and HTTPS URLs | check_circle |  | Agentless | Storage Transfer Service accepts a TSV file specifying a list of URLs to transfer. Transfers to Cloud Storage only. To configure access to a URL list, refer to [Configure access to a source: URL list](https://docs.cloud.google.com/storage-transfer/docs/source-url-list). For formatting details, see [Create a URL list](https://docs.cloud.google.com/storage-transfer/docs/create-url-list).  
File system | check_circle | check_circle | Agent-based | Storage Transfer Service supports transfers:

  * From file systems to Cloud Storage
  * From Cloud Storage to file systems
  * Between two file systems

See [Manage agent pools](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools) to configure agents and agent pools. To configure a file system as a source or sink, refer to the following pages:

  * [Configure access to a source: file system](https://docs.cloud.google.com/storage-transfer/docs/source-filesystem)
  * [Configure access to a sink: file system](https://docs.cloud.google.com/storage-transfer/docs/sink-filesystem)

  
Hadoop Distributed File System, HDFS | check_circle |  | Agent-based | Transfers to Cloud Storage only. To configure a transfer from an HDFS source, refer to [Transfer from HDFS to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agent-based/hdfs).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
