---
url: https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/
title: Support a cross-project service account \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:59:06.236145+00:00
---

# Support a cross-project service account  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/

[ Skip to main content ](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/)
  * [Deutsch](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=de)
  * [Español](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=es-419)
  * [Français](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=id)
  * [Italiano](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=it)
  * [Português](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=ja)
  * [한국어](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Feventarc%2Fdocs%2Fuse-cross-project-service-account%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Enable cross-project service account usage](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#enable)
  * [Grant permissions for service account authentication](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#grant)
  * [Grant permissions to support event routing](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#grant-events)
  * [What's next](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)


Was this helpful?
Send feedback 
#  Support a cross-project service account Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Enable cross-project service account usage](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#enable)
  * [Grant permissions for service account authentication](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#grant)
  * [Grant permissions to support event routing](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#grant-events)
  * [What's next](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#whats_next)


[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)
Every Eventarc trigger is associated with an Identity and Access Management (IAM) service account at the time the trigger is created. The trigger uses the service account as its default identity.
By default, you can't create an IAM service account in one Google Cloud project and attach it to a resource in another project. However, you might have centralized the service accounts for your organization in separate projects, which can make the service accounts easier to manage. This document outlines the steps required to support attaching a service account in one project to an Eventarc trigger in another project.
If you don't have the permissions to perform these steps, ask an administrator to complete them.
## Enable cross-project service account usage
Complete the following steps in the service account project.
  1. In the Google Cloud console, go to the **Organization policies** page.
[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)
  2. If the **Disable Cross-Project Service Account Usage** policy is enforced, you must [disable it](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).
For more information, see [Enable service accounts to be attached across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).
  3. [Create your service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) and note its name.


## Grant permissions for service account authentication
Principals can use service accounts to authenticate in a few different ways. Each type of authentication requires the principal to have specific IAM permissions on the service account. For more information, see [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions).
  1. Grant the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) IAM role to the Eventarc service agent of the Google Cloud project that contains the trigger. This permits the service agent to manage the cross-project access for the service account. A service agent is the identity of a given Google Cloud service for a particular project. For more information, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents).
[Console](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#console)[gcloud](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#gcloud) More
    1. In the Google Cloud console, go to the **Service accounts** page.
[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
    2. Select the project that owns the service account that you will attach to the Eventarc trigger.
    3. Click the email address of the service account that you previously created.
    4. Click the **Principals with access** tab.
    5. Click person_add **Grant access**.
    6. In the **New principals** field, enter the email address of the Eventarc service agent:

```
service-EVENTARC_PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com
```

Replace `EVENTARC_PROJECT_NUMBER` with the Google Cloud project number of the project that contains the trigger.
    7. Click **Add another role**.
    8. In the **Select a role** list, filter for **Service Account Token Creator** , and then select the role.
    9. Click **Save**.
Run the [`gcloud iam service-accounts add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command:

```
gcloud iam service-accounts add-iam-policy-binding \
    SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
    --member='serviceAccount:service-EVENTARC_PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com' \
    --role='roles/iam.serviceAccountTokenCreator'
```

Replace the following:
     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `SERVICE_ACCOUNT_PROJECT_ID`: the Google Cloud project ID of the project that owns the service account
     * `EVENTARC_PROJECT_NUMBER`: the Google Cloud project number of the project that contains the trigger
  2. Grant the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) IAM role to all principals who create triggers—for example, the Eventarc service agent of the Google Cloud project that contains the trigger. This predefined role contains the `iam.serviceAccounts.actAs` permission, which is required to attach a service account to a resource.
[Console](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#console)[gcloud](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/#gcloud) More
Grant the role on the project to allow the principal to impersonate multiple service accounts:
    1. In the Google Cloud console, go to the **IAM** page.
[Go to IAM](https://console.cloud.google.com/iam-admin/iam)
    2. Select the project that owns the service account.
    3. Click person_add **Grant access**.
    4. In the **New principals** field, enter the email address of the principal.
    5. In the **Select a role** list, filter for **Service Account User** , and then select the role.
    6. Click **Save**.
Or, grant the role on the service account to allow the principal to impersonate only a specific service account:
    1. In the Google Cloud console, go to the **Service accounts** page.
[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
    2. Select the project that owns the service account.
    3. Click the email address of the service account that you previously created.
    4. Click the **Permissions** tab.
    5. In the **Principals with access to this service account** section, click person_add **Grant access**.
    6. In the **New principals** field, enter the email address of the principal.
    7. Click **Add another role**.
    8. In the **Select a role** list, filter for **Service Account User** , and then select the role.
    9. Click **Save**.
Run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command and grant the role on the project to allow the principal to impersonate multiple service accounts:

```
gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
    --member=PRINCIPAL \
    --role='roles/iam.serviceAccountUser'
```

Or, run the [`gcloud iam service-accounts add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command and grant the role on the service account to allow the principal to impersonate only a specific service account:

```
gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_RESOURCE_NAME \
    --member=PRINCIPAL \
    --role='roles/iam.serviceAccountUser'
```

Replace the following:
     * `SERVICE_ACCOUNT_PROJECT_ID`: the Google Cloud project ID of the project that owns the service account
     * `PRINCIPAL`: an identifier for the trigger creator in the format `user|group|serviceAccount:email` or `domain:domain`. For example: 
       * `user:test-user@gmail.com`
       * `group:admins@example.com`
       * `serviceAccount:test123@example.domain.com`
       * `domain:example.domain.com` m
     * `SERVICE_ACCOUNT_RESOURCE_NAME`: the full resource name of the service account. For example:
`projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com`
Where:
       * `SERVICE_ACCOUNT_PROJECT_ID` is the Google Cloud project ID that owns the service account
       * `SERVICE_ACCOUNT_NAME` is the name of your service account


## Grant permissions to support event routing
Before creating an Eventarc trigger, you must grant other IAM permissions to support routing events using Eventarc.
  1. Grant the appropriate permissions based on what resources the Eventarc trigger must access to do its work, and the event provider and destination. For more information see [All roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions).
  2. [Create your trigger](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) using the cross-project service account.


## What's next
  * [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview)
  * [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
