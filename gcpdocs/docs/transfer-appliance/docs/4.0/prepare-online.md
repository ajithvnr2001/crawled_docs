---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online/
title: Prepare for online transfer \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T23:41:26.373659+00:00
---

# Prepare for online transfer  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)



Send feedback 

#  Prepare for online transfer Stay organized with collections  Save and categorize content based on your preferences. 

Online transfer requires setup for the first time you use it. Subsequent transfers after initial setup don't require these steps.

The simplest way to complete this setup is to use the setup checklist in the Google Cloud console, as described in [Project setup and key download](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#project-setup-and-key-download). The checklist enables only the Transfer Appliance, Pub/Sub, and Storage Transfer APIs, creates the appliance service account, and grants roles to the service accounts.

Use the instructions on this page if you want to configure online transfer manually, for example to grant only the minimum required roles, or to use a service account that belongs to a different project.

## Service accounts used for online transfer

Online transfer uses the following two identities:

  * **Appliance service account** : a user-managed service account whose key (`key.json`) you upload to the appliance. The appliance uses this service account to create and run Storage Transfer Service jobs, to publish and receive Pub/Sub messages, and to upload your data to the destination bucket. The setup checklist creates this service account when you click **Create service account**. You can also create it yourself.

  * **Storage Transfer Service service agent of your project** : a Google-managed service agent with the following format:
        
        project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com
        

Replace `PROJECT_NUMBER` with the project number of the project that contains the destination bucket.


**Note:** The session service account (`SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com`) and the Storage Transfer Service service agent of the Google-managed tenant project aren't used for online transfer. You only need to authorize them for [offline transfer](/transfer-appliance/docs/4.0/prepare-permissions), for example if you switch the appliance to offline mode and ship it back to Google. The setup checklist might list these service accounts even if you use online mode.

## Enable the APIs

To complete first-time setup for online transfer, a Google Cloud administrator must enable the following APIs:

  * Google Storage Transfer API (`storagetransfer.googleapis.com`)
  * Pub/Sub API (`pubsub.googleapis.com`)
  * Cloud Storage API (`storage.googleapis.com`)



Optionally, if you'll enable [Cloud Monitoring](https://docs.cloud.google.com/transfer-appliance/docs/4.0/metrics-appliance), also enable the Cloud Monitoring API (`monitoring.googleapis.com`).

Enable the APIs in the following projects:

  * The project that you ordered the appliance from, which contains the destination bucket.
  * If the appliance service account belongs to a different project, also the project that contains the appliance service account. API requests from the appliance are checked against the project that owns the service account. If the APIs aren't enabled in that project, online transfer fails with an error similar to `Storage Transfer API has not been used in project PROJECT_NUMBER before or it is disabled`.



To enable the APIs in a project, do the following:

  1. Enable the Storage Transfer, Pub/Sub, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=storagetransfer.googleapis.com,pubsub.googleapis.com,storage.googleapis.com)

     1. Confirm the project you are enabling the APIs for, then click **Next**.

     2. Click **Enable**.




Alternatively, run the following command:
    
    
    gcloud services enable storagetransfer.googleapis.com pubsub.googleapis.com storage.googleapis.com --project=PROJECT_ID
    

Replace `PROJECT_ID` with the ID of the project to enable the APIs in.

## Configure the Storage Transfer Service service agent

Grant the following role to the Storage Transfer Service service agent of your project [on the project that you ordered the appliance from](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console):

  * **`Pub/Sub Editor`** (`roles/pubsub.editor`)



Grant one of the following roles to the Storage Transfer Service service agent [for the destination bucket](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add):

  * **`Storage Object Admin`** (`roles/storage.objectAdmin`), the minimum required role.
  * **`Storage Admin`** (`roles/storage.admin`), the role that the setup checklist grants.



## Create and configure a user-managed service account

  1. [Create a user-managed service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). This is the appliance service account.

The service account can be in the project that you ordered the appliance from, or in a different project, for example if your organization doesn't allow service account keys to be created in the order project. If you use a different project, enable the APIs in that project too.

  2. Grant roles to the user-managed service account [on the project that you ordered the appliance from](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console), and [for the destination bucket](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add). Grant these roles on the order project and the destination bucket even if the service account belongs to a different project.

The following table lists the minimum roles that online transfer requires, and the broader roles that the setup checklist grants:

Where to grant | Minimum roles | Roles granted by the setup checklist  
---|---|---  
Project | 
     * **`Storage Transfer Agent`** (`roles/storagetransfer.transferAgent`)
     * **`Storage Transfer User`** (`roles/storagetransfer.user`)
     * **`Pub/Sub Editor`** (`roles/pubsub.editor`)
     * **`Monitoring Metric Writer`** (`roles/monitoring.metricWriter`)
| 
     * **`Storage Transfer Admin`** (`roles/storagetransfer.admin`)
     * **`Pub/Sub Editor`** (`roles/pubsub.editor`)
     * **`Monitoring Metric Writer`** (`roles/monitoring.metricWriter`)
     * **`Storage Admin`** (`roles/storage.admin`)  
Destination bucket | 
     * **`Storage Object Admin`** (`roles/storage.objectAdmin`)
     * **`Storage Legacy Bucket Reader`** (`roles/storage.legacyBucketReader`)
|  None. The project-level **`Storage Admin`** (`roles/storage.admin`) role covers the bucket.   



Once the service account is configured, prepare a service account key:

  1. [Create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-console) for the user-managed service account. The key is downloaded when you create it, and you cannot download it again.

  2. Rename the key to `key.json`, and save it to a safe location.

  3. Once you've received your appliance, upload `key.json` to the `/tmp` directory on the appliance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
