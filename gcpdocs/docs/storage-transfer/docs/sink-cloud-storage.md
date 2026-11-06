---
url: https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage/
title: Configure access to a sink: Cloud Storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:53:06.032849+00:00
---

# Configure access to a sink: Cloud Storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a sink: Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service can use a Cloud Storage destination (sink) bucket in two transfer types:

  * **Agentless transfers:** Cloud-to-cloud transfers such as AWS S3, Azure Blob Storage, or Cloud Storage to Cloud Storage. Permissions are granted to the Storage Transfer Service service agent.

  * **Agent-driven transfers:** Transfers from file systems, HDFS, or S3-compatible storage to Cloud Storage that use transfer agents and agent pools. Permissions must be granted to both the service agent and the transfer agent account.




## Auto-granting permissions in the Google Cloud console

If you're using the Google Cloud console to create an agentless transfer and have the required user permissions, the service agent will automatically be granted the required permissions on your destination bucket.

You can skip the steps on this page. If required, [configure access to your source](https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks), then [create a transfer](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).

## Prerequisites

  * **User account permissions:** To grant the required IAM roles listed on this page, your user account (or user-managed service account) must have permissions to modify IAM policies on your destination bucket and agent pool project. For details on user account requirements, see [User account permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-user#resource-permissions).

  * **Agent-based transfer project permissions:** For agent-driven transfers, ensure you have configured the required project-level roles for your service agent and transfer agent account. See [Agent-based project-level permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-agent-based).




## Find the service agent's email

The [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) is created automatically when you first create a transfer job, run `gcloud transfer` setup commands, visit the **Storage Transfer** page in the Google Cloud console, or call [`googleServiceAccounts.get`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get).

To obtain the service agent's email, which is used to identify it in Storage Transfer Service commands:

  1. Go to the [`googleServiceAccounts.get` reference page](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get). An interactive panel opens, titled **Try this method**.
  2. In the panel, under **Request parameters** , enter your project ID.
  3. Click **Execute**.



Copy the value of `accountEmail`. It uses the format: `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.

## Grant the required permissions

Select your transfer type to view the steps for granting access.

### Agentless transfer

The following predefined roles together grant the required permissions on the destination bucket to the service agent:

  * **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)
  * **Storage Object User** (`roles/storage.objectUser`), or **Storage Object Admin** (`roles/storage.objectAdmin`) if preserving object ACLs (`ACL_PRESERVE`).



Add the service agent to the destination bucket IAM policy:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **Bucket overflow** menu (more_vert) for the destination bucket.
  3. Choose **Edit access**.
  4. Click **\+ Add principal**.
  5. In **New principals** , enter your service agent email.
  6. Select `Storage Legacy Bucket Reader` from the **Select a role** drop-down menu.
  7. Click **Add another role** and select `Storage Object User`, or `Storage Object Admin` if preserving object ACLs.
  8. Click **Save**.



### gcloud

Run the following `gcloud storage` commands:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
    --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.OBJECT_ROLE
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
    --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.legacyBucketReader

Replace:

  * BUCKET_NAME: The name of your destination bucket.
  * SERVICE_AGENT_EMAIL: The service agent email.
  * OBJECT_ROLE: Specify `objectUser` by default, or `objectAdmin` if preserving object ACLs (`ACL_PRESERVE`).



### REST API

  1. Generate an access token to authenticate your request. If you are using the `gcloud` CLI, run:
         
         gcloud auth print-access-token

  2. Retrieve the existing bucket IAM policy (`GET https://storage.googleapis.com/storage/v1/b/<var>BUCKET_NAME</var>/iam`), append the following bindings to its `bindings` array, and save the merged policy as `sink_policy.json`:
         
         {
         "bindings": [
           {
             "role": "roles/storage.OBJECT_ROLE",
             "members": ["serviceAccount:SERVICE_AGENT_EMAIL"]
           },
           {
             "role": "roles/storage.legacyBucketReader",
             "members": ["serviceAccount:SERVICE_AGENT_EMAIL"]
           }
         ]
         }

Replace:

     * SERVICE_AGENT_EMAIL: The service agent email.
     * OBJECT_ROLE: Specify `objectUser` by default, or `objectAdmin` if preserving object ACLs (`ACL_PRESERVE`).
  3. Submit a `PUT` request using `curl`:
         
         curl -X PUT --data-binary @sink_policy.json \
           -H "Authorization: Bearer OAUTH2_TOKEN" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Replace:

     * OAUTH2_TOKEN: The OAuth 2.0 access token generated in step 1.
     * BUCKET_NAME: The name of your destination bucket.



### Agent-driven transfer

The following predefined roles grant the required access on the destination bucket to the service agent:

  * **Storage Object Creator** (`roles/storage.objectCreator`)
  * **Storage Object Viewer** (`roles/storage.objectViewer`)
  * **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)



The following role grants the required access on the destination bucket to the transfer agent account:

  * **Storage Object User** (`roles/storage.objectUser`)



Grant these roles on the destination bucket.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **Bucket overflow** menu (more_vert) for the destination bucket and select **Edit access**.
  3. Click **\+ Add principal**.
  4. In **New principals** , enter your service agent email.
  5. Select `Storage Object Creator`, `Storage Object Viewer`, and `Storage Legacy Bucket Reader` from the **Select a role** drop-down menu.
  6. Click **\+ Add principal** again.
  7. Enter your **transfer agent account** email. This is the user or service account used when installing transfer agents. For example, `my-agent-sa@PROJECT_ID.iam.gserviceaccount.com` or `user@example.com`.
  8. Select `Storage Object User` from the **Select a role** drop-down menu.
  9. Click **Save**.



### gcloud

  1. Grant logging and viewer roles to the **service agent** :
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.objectCreator
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.objectViewer
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.legacyBucketReader

  2. Grant write and management roles to the **transfer agent account** :
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount_OR_user:TRANSFER_AGENT_ACCOUNT --role=roles/storage.objectUser

Replace:

     * BUCKET_NAME: The name of your destination bucket.
     * SERVICE_AGENT_EMAIL: The service agent email.
     * serviceAccount_OR_user: Specify either `serviceAccount` if your transfer agent account is a service account, or `user` if your agents were installed with a user account.
     * TRANSFER_AGENT_ACCOUNT: The email of the account that installed your transfer agents. For example, `my-agent-sa@PROJECT_ID.iam.gserviceaccount.com` or `user@example.com`.



### REST API

  1. Generate an access token to authenticate your request. If you are using the `gcloud` CLI, run:
         
         gcloud auth print-access-token

  2. Retrieve the existing bucket IAM policy (`GET https://storage.googleapis.com/storage/v1/b/<var>BUCKET_NAME</var>/iam`), append the following bindings to its `bindings` array, and save the merged policy as `agent_sink_policy.json`:
         
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

     * SERVICE_AGENT_EMAIL: The service agent email.
     * serviceAccount_OR_user: Specify either `serviceAccount` if your transfer agent account is a service account, or `user` if your agents were installed with a user account.
     * TRANSFER_AGENT_ACCOUNT: The email of the account that installed your transfer agents. For example, `my-agent-sa@PROJECT_ID.iam.gserviceaccount.com` or `user@example.com`.
  3. Update the bucket policy via `curl`:
         
         curl -X PUT --data-binary @agent_sink_policy.json \
             -H "Authorization: Bearer OAUTH2_TOKEN" \
             -H "Content-Type: application/json" \
             "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Replace:

     * OAUTH2_TOKEN: The OAuth 2.0 access token generated in step 1.
     * BUCKET_NAME: The name of your destination bucket.



## Fine-grained permissions reference

Select your transfer type to view required roles and permissions.

### Agentless transfer

For agentless transfers, permissions must be granted to the Storage Transfer Service service agent:

Permission | Description  
---|---  
`storage.buckets.get` | Allows the service agent to inspect bucket metadata and location.  
`storage.objects.create` | Allows the service agent to write transferred objects to the destination bucket.  
`storage.objects.get` | Allows viewing existing objects and metadata. Required if your transfer is configured to [overwrite objects](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#OverwriteWhen) in the sink when different or never.  
`storage.objects.list` | Allows listing objects in the destination bucket. Required if checking whether objects already exist in the sink.  
`storage.objects.delete` | Allows deleting objects in the destination bucket. Required if overwrite or unique object deletion options are enabled.  
`storage.objects.setIamPolicy` | Allows setting object ACLs in the destination bucket. Required if object ACL preservation (`ACL_PRESERVE`) is enabled.  
`storage.folders.create`  
`storage.folders.get` | Allows creating and reading folders. Required when transferring to a destination bucket with hierarchical namespace enabled.  
  
### Agent-driven transfer

For agent-driven transfers to a Cloud Storage destination, permissions are split between two principals:

  * **Service agent:** Requires permissions to write transfer logs and verify object existence in the destination bucket.

  * **Transfer agent account:** The service account or user account running the transfer agents that writes files to Cloud Storage.




### Service agent permissions

Permission | Description  
---|---  
`storage.buckets.get` | Allows the service agent to inspect bucket metadata and location.  
`storage.objects.create` | Allows creating transfer logs in the bucket.  
`storage.objects.get` | Allows checking if objects have already been transferred.  
  
### Transfer agent account permissions

Permission | Description  
---|---  
`storage.objects.create` | Allows agents to write objects to the destination bucket during transfer.  
`storage.objects.get` | Allows agents to read object data and metadata in the destination bucket.  
`storage.objects.list` | Allows agents to list existing objects in the destination bucket.  
`storage.objects.delete` | Required if your transfer is configured to overwrite or delete objects in the sink.  
`storage.multipartUploads.create`  
`storage.multipartUploads.abort`  
`storage.multipartUploads.listParts`  
`storage.multipartUploads.list` | Allows agents to perform [multipart uploads](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices#multipart-uploads) for large files. Included automatically in `roles/storage.objectUser`.  
`storage.folders.create`  
`storage.folders.get` | Allows agents to create and read folders when transferring to a destination bucket with hierarchical namespace enabled.  
  
## What's next

  * Learn how to [Configure access to a source](https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks).
  * Learn how to [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).
  * Review the [Role and permission reference](https://docs.cloud.google.com/storage-transfer/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
