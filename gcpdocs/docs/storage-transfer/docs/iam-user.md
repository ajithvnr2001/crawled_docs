---
url: https://docs.cloud.google.com/storage-transfer/docs/iam-user/
title: Required user permissions \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:49:31.894086+00:00
---

# Required user permissions  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/iam-user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Required user permissions Stay organized with collections  Save and categorize content based on your preferences. 

Creating, managing, or monitoring transfers with Storage Transfer Service requires IAM permissions and roles for your user account, automation tool, or service account.

These permissions apply to both agentless and agent-based transfers. For general information about granting IAM roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Required Storage Transfer Service permissions

To interact with Storage Transfer Service, you must grant one of the following predefined roles or equivalent custom permissions to your user account, group, or service account on the Google Cloud project creating the transfer:

Role | Key capabilities  
---|---  
**Storage Transfer Admin**  
(`roles/storagetransfer.admin`)  |  Full control over Storage Transfer Service resources: 

  * Create, run, edit, and delete transfer jobs.
  * Create, configure, and delete transfer agent pools.
  * Configure project-wide bandwidth limits.
  * View all transfer operations, status, and logs.

  
**Storage Transfer User**  
(`roles/storagetransfer.user`)  |  Create, update, and run transfer jobs and agent pools without deletion permissions: 

  * Create, get, update, and list transfer jobs.
  * Create, get, update, and list agent pools.
  * Configure project-wide bandwidth limits.
  * Run, pause, and resume transfer operations.
  * Cannot delete transfer jobs or agent pools.

  
**Storage Transfer Viewer**  
(`roles/storagetransfer.viewer`)  |  Read-only access to inspect transfer jobs, operations, and agent pools. Recommended for monitoring and auditing.   
  
For a detailed list of individual permissions in each role, see the [Role and permission reference](https://docs.cloud.google.com/storage-transfer/docs/access-control#predefined-roles). If you configure a transfer job to delegate permissions to a user-managed service account, your user account must also have the **Service Account User** (`roles/iam.serviceAccountUser`) role on that service account; see [Delegate service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions).

### Grant a Storage Transfer Service role on your project

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Ensure your transfer project is selected, then click **Grant access**.

  3. In the **New principals** field, enter your user account email or service account.

  4. In the **Select a role** drop-down list, search for and select `Storage Transfer Admin`, `Storage Transfer User`, or `Storage Transfer Viewer`.

  5. Optional: To allow the Google Cloud console to check for missing service agent permissions and prompt you to auto-grant them during transfer creation:

     1. Click **\+ Add another role**.
     2. Search for and select **Role Viewer** (`roles/iam.roleViewer`), which grants `resourcemanager.projects.getIamPolicy`.
  6. Click **Save**.




### gcloud

  1. Grant the Storage Transfer Service role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="PRINCIPAL" \
            --role="roles/storagetransfer.ROLE"

Replace:

     * PROJECT_ID: The project where you will run transfers.
     * PRINCIPAL: Your account formatted as `user:EMAIL` for a user account, or `serviceAccount:SA_EMAIL` for a service account.
     * ROLE: One of `admin`, `user`, or `viewer`.
  2. Optional: To allow the Google Cloud console to check for missing service agent permissions and prompt you to auto-grant them during transfer creation, grant the **Role Viewer** role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="PRINCIPAL" \
            --role="roles/iam.roleViewer"




## Required Cloud Storage permissions

To configure a transfer that uses Cloud Storage buckets as a source, sink, or intermediate staging location, your account must have permission to view and modify the bucket's IAM policy so you can grant required roles to the Storage Transfer Service service agent or transfer agent account.

Your account requires:

  * `storage.buckets.getIamPolicy`
  * `storage.buckets.setIamPolicy`



Either of the following predefined roles grant these permissions:

  * **Storage Admin** (`roles/storage.admin`)
  * **Storage Legacy Bucket Owner** (`roles/storage.legacyBucketOwner`)



### Grant a Cloud Storage role on a bucket

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **Bucket overflow** menu (more_vert) for the bucket and select **Edit access**.
  3. Click **\+ Add principal**.
  4. In the **New principals** field, enter your user account email or service account.
  5. In the **Select a role** drop-down list, search for and select `Storage Admin`.
  6. Click **Save**.



### gcloud

Run `gcloud storage buckets add-iam-policy-binding`:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
        --member="PRINCIPAL" \
        --role="roles/storage.admin"

Replace:

  * BUCKET_NAME: The name of your source, sink, or intermediate bucket.
  * PRINCIPAL: Your account formatted as `user:EMAIL` for a user account, or `serviceAccount:SA_EMAIL` for a service account.



## What's next

Next steps depend on whether your transfer requires transfer agents:

  * If your transfer is agentless, such as transfers between Cloud Storage buckets, Amazon S3 to Cloud Storage, or Azure Blob Storage to Cloud Storage, user access setup is complete. Proceed to [Configure access to your source and destination](https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks) or [Create a transfer](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).
  * If your transfer is agent-based, such as transfers involving file systems, HDFS, or S3-compatible storage, proceed to [Agent-based project-level permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-agent-based).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
