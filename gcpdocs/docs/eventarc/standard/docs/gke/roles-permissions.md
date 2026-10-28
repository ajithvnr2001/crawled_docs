---
url: https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/
title: Roles and permissions for Google Kubernetes Engine (GKE) targets \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:54:55.830220+00:00
---

# Roles and permissions for Google Kubernetes Engine (GKE) targets  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/

[ Skip to main content ](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/)
  * [Deutsch](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=de)
  * [Español](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=es-419)
  * [Français](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=id)
  * [Italiano](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=it)
  * [Português](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=ja)
  * [한국어](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Grant project-wide permissions](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#project-perms)
  * [Grant permissions to Google service agents](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#agent-perms)
  * [What's next](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)


Send feedback 
#  Roles and permissions for Google Kubernetes Engine (GKE) targets Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Grant project-wide permissions](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#project-perms)
  * [Grant permissions to Google service agents](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#agent-perms)
  * [What's next](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#whats_next)


[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)
This document shows you how to grant Identity and Access Management (IAM) roles and permissions to support routing events using Eventarc from Google Cloud and other sources to GKE destinations, including the public endpoints of private and public services running in a GKE cluster.
  1. [Grant project-wide permissions to the principal invoking the Eventarc APIs](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#project-perms) (for example, the Eventarc trigger creator):
    1. The **Eventarc Admin** role allows you full control over all Eventarc resources, including specifying a service account for the trigger when you create it.
    2. The **Service Account User** role allows a principal to impersonate and use a service account. The service account is associated with an Eventarc trigger and represents the identity of the trigger.
  2. [Grant Eventarc trigger permissions to the trigger service account](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#sa-perms):
    1. The **Eventarc Event Receiver** role allows your Eventarc trigger to receive events from event providers. You don't need to grant the role if you are routing direct events from Cloud Pub/Sub.
    2. The **Pub/Sub Subscriber** role allows your Eventarc trigger to consume messages from Pub/Sub and to attach subscriptions to a topic.
    3. The **Monitoring Metric Writer** role allows Eventarc's event forwarder to write metrics using Cloud Monitoring and other systems that provide metrics.
  3. [Grant permissions to Google service agents](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions/#agent-perms):
    1. If you are creating a trigger for direct events from Cloud Storage, grant the **Pub/Sub Publisher** role.
    2. If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, grant the **Service Account Token Creator** role.


For more information about granting IAM roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).
## Grant project-wide permissions
If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this role includes the permissions necessary for full access to most Google Cloud resources. Otherwise, required roles must be granted by an administrator on the appropriate resource to the appropriate _principal_ (also known as a member).
For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). Each principal has its own identifier, which is typically an email address.
  1. The [Eventarc Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`) allows you full control over all Eventarc resources.
Grant the role on the project:

```
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=PRINCIPAL \
    --role=roles/eventarc.admin
```

Replace the following:
     * `PROJECT_ID`: your Google Cloud project ID.
     * `PRINCIPAL`: an identifier for the trigger creator which usually has the following form: `PRINCIPAL_TYPE:ID`. For example, `user:my-user@example.com`. For a full list of the possible `PRINCIPAL_TYPE` values, see the [Policy Binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding).
  2. The [Service Account User role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) allows a principal to run operations as a service account.
When creating an Eventarc trigger, you need this role so that you can associate a user-managed service account with the trigger and which represents its identity. For more information, see [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions).
You can either grant the role on the project to allow the principal to impersonate multiple service accounts or grant the role on the service account to allow the principal to impersonate only a specific service account.
Grant the role on the project:

```
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=PRINCIPAL \
    --role=roles/iam.serviceAccountUser
```

Or, grant the role on the service account:

```
gcloud iam service-accounts add-iam-policy-binding \
    projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
    --member=PRINCIPAL \
    --role=roles/iam.serviceAccountUser
```

Replace the following:
     * `SERVICE_ACCOUNT_PROJECT_ID`: the Google Cloud project ID that contains the service account.
     * `SERVICE_ACCOUNT_NAME`: the name of the service account. ## Grant Eventarc trigger permissions


Every Eventarc trigger is associated with an IAM service account at the time the trigger is created. You can specify a user-managed service account that the trigger uses as its default identity. If you don't specify a service account during the trigger's creation, the trigger uses the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) for its identity.
We recommend that you [create your own user-managed service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) to give you greater control and flexibility when managing your trigger.
  1. Create a service account and note its name:

```
gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
    --description="DESCRIPTION" \
    --display-name="DISPLAY_NAME"

```

Replace the following:
     * `SERVICE_ACCOUNT_NAME`: the name of the service account. This name appears in the email address that identifies the service account.
     * `DESCRIPTION`: an optional description of the service account
     * `DISPLAY_NAME`: a service account name to display in the Google Cloud console
  2. Grant the [Eventarc Event Receiver role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) (`roles/eventarc.eventReceiver`) on the project to the service account associated with your Eventarc trigger so that it can receive events from event providers.
Note that you don't need to grant the Eventarc Event Receiver role if you are routing [direct events from Cloud Pub/Sub](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-pubsub).

```
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
    --role=roles/eventarc.eventReceiver
```

Replace `SERVICE_ACCOUNT_NAME` with the name of your service account that you noted in the previous step.
  3. Grant the [Pub/Sub Subscriber role](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber) (`roles/pubsub.subscriber`) on the project to the service account associated with your Eventarc trigger so that it can consume messages from Pub/Sub and attach subscriptions to a topic.

```
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
    --role=roles/pubsub.subscriber
```

Replace `SERVICE_ACCOUNT_NAME` with the name of your service account that you noted previously.
  4. Grant the [Monitoring Metric Writer role](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) on the project to the service account associated with your Eventarc trigger so that Eventarc's event forwarder can write metrics using Cloud Monitoring and other systems that provide metrics.

```
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
    --role=roles/monitoring.metricWriter
```

## Grant permissions to Google service agents


Some Google Cloud services have [_service agents_](https://docs.cloud.google.com/iam/docs/service-agents) that allow the services to access your resources. If an API requires a service agent, then Google creates the service agent after you activate and use the API.
  1. **If you are creating a trigger for direct events from Cloud Storage** , to support publishing messages to a topic, grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) on the project to the Cloud Storage service agent:

```
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com \
    --role=roles/pubsub.publisher
```

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:

```
gcloud projects describe PROJECT_ID --format='value(projectNumber)'
```

  2. **If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021** , to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) on the project to the Pub/Sub service agent. Otherwise, this role is granted by default:

```
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
    --role=roles/iam.serviceAccountTokenCreator
```

## What's next


  * Learn about [access control options in Eventarc](https://docs.cloud.google.com/eventarc/docs/access-control).
  * Learn about [creating IAM policies for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam).
  * Learn about [best practices for using service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).
  * Learn how to [describe a trigger and verify its associated service account](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-describe).


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
