---
url: https://docs.cloud.google.com/storage-transfer/docs/iam-agent-based/
title: Agent-based project-level permissions \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:44:21.588776+00:00
---

# Agent-based project-level permissions  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/iam-agent-based/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Agent-based project-level permissions Stay organized with collections  Save and categorize content based on your preferences. 

Agent-based transfers require project-level IAM permissions for two distinct entities: a service agent and a transfer agent account.

Configure the permissions on this page only if your transfer involves a file system, HDFS, or S3-compatible storage. If your transfer is agentless, do not configure the roles on this page; proceed directly to [Configure access to your source and destination](https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks).

Agent-based transfers use the following identities:

  * **Service agent** : A Google-managed service account used by Storage Transfer Service to coordinate tasks with transfer agents.
  * **Transfer agent account** : The Google Cloud user account or user-managed service account used to authenticate and run transfer agents on your client machines or instances.



For general information on granting IAM roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Service agent permissions

Storage Transfer Service uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) to coordinate agent-driven transfers.

To enable Storage Transfer Service to coordinate work between Google Cloud and your transfer agents, grant the following role to the service agent on the project running Storage Transfer Service:

  * **Storage Transfer Service Agent** (`roles/storagetransfer.serviceAgent`)



### Obtain the service agent email address

Granting a role to the service agent requires the service agent's email address identifier. The service agent is created automatically when you first create a transfer job, run `gcloud transfer` setup commands, visit the **Storage Transfer** page in the Google Cloud console, or call [`googleServiceAccounts.get`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get).

To obtain the service agent email address:

  1. Go to the [`googleServiceAccounts.get` reference page](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get). An interactive panel opens, titled **Try this method**.
  2. Under **Request parameters** , enter your project ID.
  3. Click **Execute**.



Copy the value of `accountEmail`. The email address uses the following format: `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.

### Grant the service agent role

To grant the **Storage Transfer Service Agent** role:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **IAM** page for the project running Storage Transfer Service.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Grant access**.

  3. In the **New principals** field, enter your service agent email address.

  4. In the **Select a role** drop-down list, search for and select **Storage Transfer Service Agent** (`roles/storagetransfer.serviceAgent`).

  5. Click **Save**.




###  `gcloud`

Run `gcloud projects add-iam-policy-binding`:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:SERVICE_AGENT_EMAIL" \
    --role="roles/storagetransfer.serviceAgent"
    

Replace the following:

  * PROJECT_ID: The project running Storage Transfer Service.
  * SERVICE_AGENT_EMAIL: The service agent email address.



## Transfer agent account permissions

Transfer agents run on your client machines using the credentials of either a user account or a user-managed service account:

  * A user account uses the credentials of an authenticated user.
  * A user-managed service account uses service account keys or identity federation. To create a service account, see [Create and manage service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).



To authorize transfer agents to connect to Storage Transfer Service, receive tasks, and log status, assign the following role on the Google Cloud project hosting your agent pool:

  * **Storage Transfer Agent** (`roles/storagetransfer.transferAgent`)



To grant this role:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Ensure you have selected the project containing your agent pool.

  3. Click **Grant access**.

  4. In the **New principals** field, enter the email address of your user account or user-managed service account.

  5. In the **Select a role** drop-down list, search for and select **Storage Transfer Agent** (`roles/storagetransfer.transferAgent`).

  6. Click **Save**.




###  `gcloud`

Run `gcloud projects add-iam-policy-binding`:
    
    
    gcloud projects add-iam-policy-binding AGENT_POOL_PROJECT_ID \
    --member="serviceAccount_OR_user:TRANSFER_AGENT_ACCOUNT" \
    --role="roles/storagetransfer.transferAgent"
    

Replace the following:

  * AGENT_POOL_PROJECT_ID: The project containing your agent pool.
  * serviceAccount_OR_user: Specify either `serviceAccount` if your transfer agent account is a service account, or `user` if your agents were installed with a user account.
  * TRANSFER_AGENT_ACCOUNT: The email address of the account running the transfer agents.



## What's next

After configuring project permissions, proceed with the following setup steps in order:

  1. [Create an agent pool](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools).
  2. [Install transfer agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents) in your pool.
  3. Configure access permissions for your storage systems: 
     * [Configure access to a source: file system](https://docs.cloud.google.com/storage-transfer/docs/source-filesystem)
     * [Configure access to a source: S3-compatible storage](https://docs.cloud.google.com/storage-transfer/docs/source-s3-compatible)
     * [Configure access to a source: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage)
     * [Configure access to a sink: file system](https://docs.cloud.google.com/storage-transfer/docs/sink-filesystem)
     * [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage)
  4. Review the complete [Role and permission reference](https://docs.cloud.google.com/storage-transfer/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
