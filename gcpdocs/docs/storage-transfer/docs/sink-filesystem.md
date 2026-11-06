---
url: https://docs.cloud.google.com/storage-transfer/docs/sink-filesystem/
title: Configure access to a sink: file system \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:53:05.934633+00:00
---

# Configure access to a sink: file system  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/sink-filesystem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a sink: file system Stay organized with collections  Save and categorize content based on your preferences. 

When transferring data to an on-premises or private cloud file system (such as POSIX, NFS, or SMB), you must configure the following:

  * **Local file system permissions:** Grant the destination transfer agents OS-level write access to your target directories.
  * **Intermediate bucket permissions (file-to-file only):** Grant IAM roles on the intermediate Cloud Storage bucket used to stage files between file systems.



## Prerequisites

  * **User permissions:** Ensure your user account or user-managed service account has permission to configure transfer jobs and agent pools. See [Required user permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-user).
  * **Agent-based project-level permissions:** Ensure you have configured the required project-level roles for your service agent and transfer agent account. See [Agent-based project-level permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-agent-based).



## Local target file system permissions

Transfer agents write files directly to your host file system. To enable successful writes:

  1. **OS user permissions:** Ensure the operating system user running the container process has **read, write, and execute** permissions on the destination directory tree.

  2. **Mount directories:** When installing your destination agents, mount the target directory path into the container using the `--mount-directories` flag:
         
         gcloud transfer agents install --pool=DESTINATION_POOL_NAME \
          --mount-directories=/path/to/destination/dir

**Caution:** All agents in the destination agent pool must have uniform, identical file system paths to the destination directory. If different agents write to mismatched paths, data corruption or transfer failures will occur.



## Intermediate bucket permissions (file-to-file transfers)

Transfers between two file systems use an intermediate Cloud Storage bucket to stage files during transfer.

The following predefined roles grant the required access on the intermediate bucket to the service agent:

  * **Storage Object Creator** (`roles/storage.objectCreator`)
  * **Storage Object Viewer** (`roles/storage.objectViewer`)
  * **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)



The following role grants the required access on the intermediate bucket to the transfer agent account(s):

  * **Storage Object User** (`roles/storage.objectUser`)



Grant these roles on the intermediate bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **Bucket overflow** menu (more_vert) for the intermediate bucket and select **Edit access**.
  3. Click **\+ Add principal**.
  4. In **New principals** , enter your [service agent email](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#find-service-agent).
  5. Select `Storage Object Creator`, `Storage Object Viewer`, and `Storage Legacy Bucket Reader` from the **Select a role** drop-down menus.
  6. Click **\+ Add principal** again.
  7. Enter the email address of the **transfer agent account(s)** used for your source and destination agent pools.
  8. Select `Storage Object User` from the **Select a role** drop-down menu.
  9. Click **Save**.



### gcloud

  1. Grant logging and metadata roles to the **service agent** :
         
         gcloud storage buckets add-iam-policy-binding gs://INTERMEDIATE_BUCKET_NAME \
             --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.objectCreator
         
         gcloud storage buckets add-iam-policy-binding gs://INTERMEDIATE_BUCKET_NAME \
             --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.objectViewer
         
         gcloud storage buckets add-iam-policy-binding gs://INTERMEDIATE_BUCKET_NAME \
             --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.legacyBucketReader

  2. Grant object management roles to the **transfer agent account(s)** for both the source and destination agent pools:
         
         gcloud storage buckets add-iam-policy-binding gs://INTERMEDIATE_BUCKET_NAME \
             --member=serviceAccount_OR_user:TRANSFER_AGENT_ACCOUNT --role=roles/storage.objectUser

Replace:

     * INTERMEDIATE_BUCKET_NAME: The name of your intermediate staging bucket.
     * SERVICE_AGENT_EMAIL: The [service agent email](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#find-service-agent).
     * serviceAccount_OR_user: Specify either `serviceAccount` if your transfer agent account is a service account, or `user` if your agents were installed with a user account.
     * TRANSFER_AGENT_ACCOUNT: The email of the account running the transfer agents. Repeat this command if your source and destination agent pools use different accounts.



### REST API

  1. Generate an access token to authenticate your request. If you are using the `gcloud` CLI, run:
         
         gcloud auth print-access-token

  2. Retrieve the existing bucket IAM policy (`GET https://storage.googleapis.com/storage/v1/b/<var>INTERMEDIATE_BUCKET_NAME</var>/iam`), append the following bindings to its `bindings` array, and save the merged policy as `intermediate_policy.json`:
         
         {
           "bindings": [
             {
               "role": "roles/storage.objectCreator",
               "members": ["serviceAccount:SERVICE_AGENT_EMAIL"]
             },
             {
               "role": "roles/storage.objectViewer",
               "members": ["serviceAccount:SERVICE_AGENT_EMAIL"]
             },
             {
               "role": "roles/storage.legacyBucketReader",
               "members": ["serviceAccount:SERVICE_AGENT_EMAIL"]
             },
             {
               "role": "roles/storage.objectUser",
               "members": ["serviceAccount_OR_user:TRANSFER_AGENT_ACCOUNT"]
             }
           ]
         }

Replace:

     * SERVICE_AGENT_EMAIL: The [service agent email](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#find-service-agent).
     * serviceAccount_OR_user: Specify either `serviceAccount` if your transfer agent account is a service account, or `user` if your agents were installed with a user account.
     * TRANSFER_AGENT_ACCOUNT: The email of the account that installed your transfer agents. If your source and destination agent pools use different accounts, include both accounts in the `members` array for `roles/storage.objectUser`.
  3. Update the intermediate bucket policy via `curl`:
         
         curl -X PUT --data-binary @intermediate_policy.json \
             -H "Authorization: Bearer OAUTH2_TOKEN" \
             -H "Content-Type: application/json" \
             "https://storage.googleapis.com/storage/v1/b/INTERMEDIATE_BUCKET_NAME/iam"

Replace:

     * OAUTH2_TOKEN: The OAuth 2.0 access token generated in step 1.
     * INTERMEDIATE_BUCKET_NAME: The name of your intermediate bucket.



For more information on file-to-file architectures, see [File system to file system transfers](https://docs.cloud.google.com/storage-transfer/docs/file-to-file).

## Performance and optimization

  * To maximize throughput when transferring to large file systems, install multiple agents in your destination agent pool (recommended minimum of 3). See [Best practices for transfer agents](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices).
  * For large files in file-to-file transfers, consider enabling [multipart uploads](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices#multipart-uploads) to the intermediate bucket. When using **Storage Object User** (`roles/storage.objectUser`), required multipart upload permissions (`storage.multipartUploads.*`) are included automatically.



## What's next

  * Learn how to [Install transfer agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents).
  * Learn how to [Configure access to a source: file system](https://docs.cloud.google.com/storage-transfer/docs/source-filesystem).
  * Learn how to [Configure access to a source: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage).
  * Learn how to [Transfer data between file systems](https://docs.cloud.google.com/storage-transfer/docs/file-to-file).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
