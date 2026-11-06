---
url: https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage/
title: Configure access to a source: Cloud Storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:53:06.448976+00:00
---

# Configure access to a source: Cloud Storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a source: Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service can use a Cloud Storage source bucket in two transfer types:

  * **Agentless transfers:** Cloud-to-cloud transfers such as Cloud Storage to Cloud Storage, Cloud Storage to AWS S3, or Cloud Storage to Azure Blob Storage. Permissions are granted to the Storage Transfer Service service agent.

  * **Agent-driven transfers:** Transfers involving file systems or on-premises storage that use transfer agents and agent pools. Permissions must be granted to both the service agent and the transfer agent account.




## Auto-granting permissions in the Google Cloud console

If you're using the Google Cloud console to create an agentless transfer and have the required user permissions, the service agent will automatically be granted the required permissions on your source bucket.

You can skip the steps on this page. If required, [configure access to your destination](https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks), then [create a transfer](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).

## Prerequisites

  * **User account permissions:** To grant the required IAM roles listed on this page, your user account (or user-managed service account) must have permissions to modify IAM policies on your source bucket and agent pool project. For details on user account requirements, see [User account permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-user#resource-permissions).

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

The following predefined roles grant the required permissions on the source bucket to the service agent:

  * **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)
  * Plus one of the following: 
    * **Storage Object Viewer** (`roles/storage.objectViewer`) if source objects are retained.
    * **Storage Object User** (`roles/storage.objectUser`) if deleting source objects after transfer (`deleteObjectsFromSourceAfterTransfer`).
    * **Storage Object Admin** (`roles/storage.objectAdmin`) if preserving object ACLs (`ACL_PRESERVE`). Also supports deleting source objects after transfer.



Add the service agent to the source bucket IAM policy:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **Bucket overflow** menu (more_vert) for the source bucket.
  3. Choose **Edit access**.
  4. Click **\+ Add principal**.
  5. In **New principals** , enter your service agent email.
  6. Select `Storage Legacy Bucket Reader` from the **Select a role** drop-down menu.
  7. Click **Add another role** and select one of the following: 
     * `Storage Object Viewer`
     * `Storage Object User`
     * `Storage Object Admin`
  8. Click **Save**.



### gcloud

Run the following `gcloud storage` commands:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
    --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.legacyBucketReader
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
    --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.OBJECT_ROLE

Replace:

  * BUCKET_NAME: The name of your source bucket.
  * SERVICE_AGENT_EMAIL: The service agent email.
  * OBJECT_ROLE: Choose one of the following based on your transfer options:
  * `objectViewer`: If retaining source objects.
  * `objectUser`: If deleting source objects after transfer.
  * `objectAdmin`: If preserving object ACLs. Also supports deleting source objects after transfer.



### REST API

  1. Generate an access token to authenticate your request. If you are using the `gcloud` CLI, run:
         
         gcloud auth print-access-token

  2. Retrieve the existing bucket IAM policy (`GET https://storage.googleapis.com/storage/v1/b/<var>BUCKET_NAME</var>/iam`), append the following bindings to its `bindings` array, and save the merged policy as `source_policy.json`:
         
         {
         "bindings": [
           {
             "role": "roles/storage.legacyBucketReader",
             "members": ["serviceAccount:SERVICE_AGENT_EMAIL"]
           },
           {
             "role": "roles/storage.OBJECT_ROLE",
             "members": ["serviceAccount:SERVICE_AGENT_EMAIL"]
           }
         ]
         }

Replace:

     * SERVICE_AGENT_EMAIL: The service agent email.
     * OBJECT_ROLE: Choose `objectViewer` if retaining source objects, `objectUser` if deleting source objects, or `objectAdmin` if preserving object ACLs.
  3. Submit a `PUT` request using `curl`:
         
         curl -X PUT --data-binary @source_policy.json \
           -H "Authorization: Bearer OAUTH2_TOKEN" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Replace:

     * OAUTH2_TOKEN: The OAuth 2.0 access token generated in step 1.
     * BUCKET_NAME: The name of your source bucket.



### Agent-driven transfer

The following predefined roles grant the required access on the source bucket to the service agent:

  * **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)
  * **Storage Object Creator** (`roles/storage.objectCreator`)



The following role grants the required access on the source bucket to the transfer agent account:

  * **Storage Object Viewer** (`roles/storage.objectViewer`) if retaining source objects, or **Storage Object User** (`roles/storage.objectUser`) if deleting source objects after transfer.



Grant these roles on the source bucket.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **Bucket overflow** menu (more_vert) for the source bucket and select **Edit access**.
  3. Click **\+ Add principal**.
  4. In **New principals** , enter your service agent email.
  5. Select `Storage Legacy Bucket Reader` and `Storage Object Creator` from the **Select a role** drop-down menus.
  6. Click **\+ Add principal** again.
  7. Enter your **transfer agent account** email. This is the user or service account used when installing transfer agents. For example, `my-agent-sa@PROJECT_ID.iam.gserviceaccount.com` or `user@example.com`.
  8. Select `Storage Object Viewer` if retaining source objects, or `Storage Object User` if deleting source objects after transfer.
  9. Click **Save**.



### gcloud

  1. Grant bucket metadata read and transfer log write roles to the **service agent** :
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.legacyBucketReader
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/storage.objectCreator

  2. Grant object access roles to the **transfer agent account** :
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount_OR_user:TRANSFER_AGENT_ACCOUNT --role=roles/storage.OBJECT_ROLE

Replace:

     * BUCKET_NAME: The name of your source bucket.
     * SERVICE_AGENT_EMAIL: The service agent email.
     * serviceAccount_OR_user: Specify either `serviceAccount` if your transfer agent account is a service account, or `user` if your agents were installed with a user account.
     * TRANSFER_AGENT_ACCOUNT: The email of the account that installed your transfer agents. For example, `my-agent-sa@PROJECT_ID.iam.gserviceaccount.com` or `user@example.com`.
     * OBJECT_ROLE: Specify `objectViewer` if retaining source objects, or `objectUser` if deleting source objects after transfer.



### REST API

  1. Generate an access token to authenticate your request. If you are using the `gcloud` CLI, run:
         
         gcloud auth print-access-token

  2. Retrieve the existing bucket IAM policy (`GET https://storage.googleapis.com/storage/v1/b/<var>BUCKET_NAME</var>/iam`), append the following bindings to its `bindings` array, and save the merged policy as `agent_source_policy.json`:
         
         {
           "bindings": [
             {
               "role": "roles/storage.legacyBucketReader",
               "members": ["serviceAccount:SERVICE_AGENT_EMAIL"]
             },
             {
               "role": "roles/storage.objectCreator",
               "members": ["serviceAccount:SERVICE_AGENT_EMAIL"]
             },
             {
               "role": "roles/storage.OBJECT_ROLE",
               "members": ["serviceAccount_OR_user:TRANSFER_AGENT_ACCOUNT"]
             }
           ]
         }

Replace:

     * SERVICE_AGENT_EMAIL: The service agent email.
     * serviceAccount_OR_user: Specify either `serviceAccount` if your transfer agent account is a service account, or `user` if your agents were installed with a user account.
     * TRANSFER_AGENT_ACCOUNT: The email of the account that installed your transfer agents. For example, `my-agent-sa@PROJECT_ID.iam.gserviceaccount.com` or `user@example.com`.
     * OBJECT_ROLE: Specify `objectViewer` if retaining source objects, or `objectUser` if deleting source objects after transfer.
  3. Update the bucket policy via `curl`:
         
         curl -X PUT --data-binary @agent_source_policy.json \
             -H "Authorization: Bearer OAUTH2_TOKEN" \
             -H "Content-Type: application/json" \
             "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Replace:

     * OAUTH2_TOKEN: The OAuth 2.0 access token generated in step 1.
     * BUCKET_NAME: The name of your source bucket.



## Cross-project Cloud Storage transfers

To transfer objects between Cloud Storage buckets in different Google Cloud projects, you must grant permissions to the **service agent of the project creating the transfer** on both the source bucket and the destination bucket.

The [user account or user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/iam-user) creating the transfer only needs permissions on the project from which the transfer job is created.

To grant roles for cross-project transfers:

  1. Obtain the service agent email for the project that will run the transfer. See Find the service agent's email.
  2. On the **source bucket** , grant the following roles to that service agent: 
     * **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)
     * Plus one of the following object roles: 
       * **Storage Object Viewer** (`roles/storage.objectViewer`) if retaining source objects.
       * **Storage Object User** (`roles/storage.objectUser`) if deleting source objects after transfer (`deleteObjectsFromSourceAfterTransfer`).
       * **Storage Object Admin** (`roles/storage.objectAdmin`) if preserving object ACLs (`ACL_PRESERVE`). Also supports deleting source objects after transfer.
  3. On the **destination bucket** , grant the following roles to the **same** service agent: 
     * **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)
     * **Storage Object User** (`roles/storage.objectUser`), or **Storage Object Admin** (`roles/storage.objectAdmin`) if preserving object ACLs (`ACL_PRESERVE`).



For step-by-step instructions on granting destination bucket access, see [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).

### Organizational restrictions

If your organization has applied [Organization Policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy) constraints, ensure they permit cross-project service agent access:

  * **Domain restricted sharing (`constraints/iam.allowedPolicyMemberDomains`):** The policy on the project hosting the bucket must permit member domains containing the service agent. See [Restricting domains](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).
  * **Disabling cross-project service account usage (`constraints/iam.disableCrossProjectServiceAccountUsage`):** Ensure this constraint does not block cross-project service account access. See [Restricting service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts).
  * **VPC Service Controls:** If buckets belong to different service perimeters, configure ingress and egress rules to allow transfer communication. See [Configure VPC Service Controls for cloud object storage transfers](https://docs.cloud.google.com/storage-transfer/docs/transfer-with-vpc-sc).



## Fine-grained permissions reference

Select your transfer type to view required roles and permissions.

### Agentless transfer

For agentless transfers, permissions must be granted to the Storage Transfer Service service agent:

Permission | Description  
---|---  
`storage.buckets.get` | Allows the service agent to get the location of the bucket.  
`storage.objects.list` | Allows the service agent to list objects in the bucket.  
`storage.objects.get` | Allows the service agent to read objects in the bucket.  
`storage.objects.delete` | Allows the service agent to delete objects in the bucket. Required if `deleteObjectsFromSourceAfterTransfer` is `true`.  
`storage.objects.getIamPolicy` | Allows reading ACLs on source objects. Required if object ACL preservation (`ACL_PRESERVE`) is enabled.  
`storage.folders.list`  
`storage.folders.get` | Allows listing and reading folders. Required when transferring from a bucket with hierarchical namespace enabled.  
  
### Agent-driven transfer

For agent-driven transfers from a Cloud Storage source, permissions are split between two principals:

  * **Service agent:** Requires bucket-level read access to resolve bucket metadata and location, plus object creation access to write agent transfer logs.

  * **Transfer agent account:** The service account or user account used to create the transfer agents.




### Service agent permissions

Permission | Description  
---|---  
`storage.buckets.get` | Allows the service agent to inspect bucket metadata and location.  
`storage.objects.create` | Allows the service agent to write agent transfer logs to the source bucket when transferring from Cloud Storage to a file system.  
  
### Transfer agent account permissions

Permission | Description  
---|---  
`storage.objects.list` | Allows agents to list objects in the source bucket.  
`storage.objects.get` | Allows agents to read objects from the source bucket.  
`storage.objects.delete` | Allows agents to delete source objects if `deleteObjectsFromSourceAfterTransfer` is enabled.  
`storage.folders.list`  
`storage.folders.get` | Allows agents to list and read folders when transferring from a bucket with hierarchical namespace enabled.  
  
## What's next

You must configure access to your destination:

  * [Configure access to a Cloud Storage sink](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage)
  * [Configure access to a file system sink](https://docs.cloud.google.com/storage-transfer/docs/sink-filesystem)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
