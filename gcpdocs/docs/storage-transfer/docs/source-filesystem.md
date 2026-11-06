---
url: https://docs.cloud.google.com/storage-transfer/docs/source-filesystem/
title: Configure access to a source: file system \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:53:07.740897+00:00
---

# Configure access to a source: file system  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/source-filesystem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a source: file system Stay organized with collections  Save and categorize content based on your preferences. 

To transfer data from an on-premises or private cloud file system (such as POSIX-compliant file systems, NFS, or SMB), you must install and configure Storage Transfer Service agents on machines with network access to the source files.

## Prerequisites

Before configuring your transfer, ensure you have set up the following:

  * **User permissions:** Ensure your user account or user-managed service account has permission to configure transfer jobs and agent pools. See [Required user permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-user).
  * **Agent-based project-level permissions:** Ensure you have configured the required project-level roles for your service agent and transfer agent account. See [Agent-based project-level permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-agent-based).
  * **Destination permissions:** Depending on your transfer destination, configure the required sink permissions: 
    * For transfers to Cloud Storage, see [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).
    * For transfers to another file system, see [Configure access to a sink: file system](https://docs.cloud.google.com/storage-transfer/docs/sink-filesystem).



## Local file system permissions

Transfer agents run inside Docker or Podman containers on your host machines. To enable agents to read your files:

  1. **OS user permissions:** Ensure the operating system user running the container has **read** (and execute on directories) permissions for all files and directories you plan to transfer.
  2. **Mount directories:** When installing your agents, mount the directories you want to copy into the container using the `--mount-directories` flag (or `-v` flags in Docker):
         
         gcloud transfer agents install --pool=AGENT_POOL_NAME \
           --mount-directories=/path/to/source/dir
         

**Caution:** If multiple agents in the same agent pool run on different physical machines, they must all have uniform network access (such as a shared NFS mount) to the exact same paths. If one agent cannot access a path assigned to it, the transfer job fails.



To restrict which host directories agents can view, see [Restricting agent directory access](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#restrict-directory-access).

## Performance and optimization

  * To maximize throughput when transferring from large file systems, install multiple agents in your source agent pool (recommended minimum of 3). See [Best practices for transfer agents](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices).
  * For files larger than 1 GB, consider enabling [multipart uploads](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices#multipart-uploads).



## What's next

  * Learn how to [Install transfer agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents).
  * Learn how to [Create an agent pool](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools).
  * Learn how to [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).
  * Learn how to [Configure access to a sink: file system](https://docs.cloud.google.com/storage-transfer/docs/sink-filesystem).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
