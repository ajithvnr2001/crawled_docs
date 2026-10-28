---
url: https://docs.cloud.google.com/alloydb/docs/user-grant-access/
title: Grant access to other users \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T18:46:11.095599+00:00
---

# Grant access to other users  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/user-grant-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Grant access to other users Stay organized with collections  Save and categorize content based on your preferences. 

To allow a Google Cloud user account or service account to manage, view, or connect to AlloyDB for PostgreSQL resources in a project, you can grant the account predefined Identity and Access Management (IAM) roles.

Depending on the scope of control you want the account to have, you grant it one of these predefined IAM roles:

  * AlloyDB Admin (`roles/alloydb.admin`) to grant full control for all AlloyDB resources

  * AlloyDB Editor (`roles/alloydb.editor`) to grant read-write access to create, modify, and delete AlloyDB resources, without permission to manage tag bindings or Backup and DR Service backup plans

  * AlloyDB Client (`roles/alloydb.client`) and Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`) to grant connectivity access to AlloyDB instances from clients connecting with the AlloyDB Auth Proxy or AlloyDB Language Connectors

  * AlloyDB Database User (`roles/alloydb.databaseUser`) to grant IAM-based database user login access and AlloyDB Studio query access to AlloyDB instances

  * AlloyDB Viewer (`roles/alloydb.viewer`) to grant read-only access to all AlloyDB resources

  * AlloyDB Admin for BackupDR (`roles/alloydb.backupDrAdmin`) to grant access to manage AlloyDB cluster backups and restores using Backup and DR




For detailed information about the specific IAM permissions these roles provide, see [Predefined AlloyDB IAM roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles).

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have the Owner (`roles/owner`) basic IAM role in the Google Cloud project you are using, or a role that grants these permissions: 
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.getIamPolicy`
    * `resourcemanager.projects.setIamPolicy`

To gain these permissions while following the principle of least privilege, ask your administrator to grant you the Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) role.

  * Enable the Cloud Resource Manager API in the Google Cloud project you are using.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com)




## Procedure

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select the project enabled to access AlloyDB.
  3. Select a principal (user or service account) to grant access to: 
     * To grant a role to a principal who already has other roles on the project, find the row containing the principal's email address, click edit **Edit principal** in that row, and click add **Add another role**. 
     * To grant a role to a principal who doesn't already have other roles on the project, click person_add **Grant access** , then enter the principal's email address. 
  4. From the drop-down list, select one of these roles: 
     * **AlloyDB Admin**
     * **AlloyDB Editor**
     * **AlloyDB Viewer**
     * **AlloyDB Client** and **Service Usage Consumer**
     * **AlloyDB Database User**
     * **AlloyDB Admin for BackupDR**
  5. Click **Save**. The principal is granted the role.

**Note:** In general, policy changes take effect within 60 seconds. However, under certain circumstances, it can take up to 7 minutes for changes to fully propagate across the system. 

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the `add-iam-policy-binding` command to grant an AlloyDB predefined role to an IAM principal (user account or service account).
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=PRINCIPAL \
        --role=ALLOYDB_ROLE
    

Replace the following:

  * `PROJECT_ID`: the ID of the project enabled to access AlloyDB.
  * `PRINCIPAL`: the type and email ID (email address) of the principal: 
    * For user accounts: `user:EMAIL_ID`
    * For service accounts: `serviceAccount:EMAIL_ID`
  * `ALLOYDB_ROLE`: the role that you want to grant the principal. The value must be one of the following:

    * `roles/alloydb.admin`
    * `roles/alloydb.editor`
    * `roles/alloydb.viewer`
    * `roles/alloydb.client`. Also grant `roles/serviceusage.serviceUsageConsumer` in a separate command.
    * `roles/alloydb.databaseUser`
    * `roles/alloydb.backupDrAdmin`

For details about the permissions these roles grant, see [Predefined AlloyDB IAM roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles).


**Note:** In general, policy changes take effect within 60 seconds. However, under certain circumstances, it can take up to 7 minutes for changes to fully propagate across the system. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
