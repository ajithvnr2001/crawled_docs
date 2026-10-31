---
url: https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers/
title: Create triggers from Pub/Sub events \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:16.411753+00:00
---

# Create triggers from Pub/Sub events  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Create triggers from Pub/Sub events Stay organized with collections  Save and categorize content based on your preferences. 

You can invoke Cloud Run services and functions by setting up a Pub/Sub trigger.

When configuring the trigger, you link the trigger to a specific Pub/Sub topic. This ensures your service or function is called automatically whenever a message is published to that topic.

You can configure this trigger in two ways:

  * **Direct Pub/Sub trigger (Recommended)** : Route messages directly to your service or function using Pub/Sub. You manage the subscription directly, and your service or function receives the standard Pub/Sub push request. Use this if you need simpler configuration and lower latency.
  * **Eventarc-based trigger** : Route Pub/Sub messages to your service or function using Eventarc. You manage Pub/Sub triggers the same way as [other Eventarc sources](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events), and your service or function receives events as CloudEvents. Use this if you need Eventarc's advanced filtering or routing features.



## Before you begin

  1. Make sure you have set up a new project for Cloud Run as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page.

  2. Enable the Artifact Registry, Cloud Build, Cloud Run Admin API, Cloud Logging, and Pub/Sub APIs:

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,run.googleapis.com,logging.googleapis.com,pubsub.googleapis.com)

If you are configuring an Eventarc-based trigger, you must also enable the Eventarc API:

[Enable the Eventarc API](https://console.cloud.google.com/apis/enableflow;apiid=eventarc.googleapis.com)




### Required roles

Grant the required IAM roles and permissions. If you are configuring an Eventarc-based trigger, see the [required IAM roles and permissions for Eventarc](https://docs.cloud.google.com/eventarc/docs/roles-permissions). 

#### Required roles for the deployer account

To get the permissions that you need to trigger from Pub/Sub events, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Note that by default, [Cloud Build permissions include permissions to upload and download Artifact Registry artifacts](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp).

## Create a Pub/Sub trigger

###  Console 

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service or function you want to create a Pub/Sub trigger for.

  3. Select the **Triggers** tab.

Select the tab for your selected trigger configuration:

### Direct (recommended)

     1. Click add **Add trigger** , and select **Pub/Sub trigger > Direct**.
     2. In the **Direct Pub/Sub subscription** panel: 
        * In the **Cloud Pub/Sub topic** field, select the topic if you have already created one, or click **Create new topic** to create a new topic.
        * In the **Service account** field, select the service account that the subscription uses to invoke your service. If the console lists missing roles, click **Grant all**.
        * For the **Service URL path** , enter the path on your service that should receive messages, such as `/` (default) or `/pubsub`. The console adds this path to your service's URL.
     3. Click **Save**.

### Eventarc

In the **Eventarc trigger** pane, modify the trigger details as follows:

     1. Enter a name for the trigger in the **Trigger name** field, or use the default name.

     2. Select a **Trigger type** from the list:

        * **Google Sources** to specify triggers for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.

        * **Third-party** to integrate with non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview).

     3. Select **Pub/Sub** from the **Event provider** list, to select a product that provides the type of event for triggering your function. For the list of event providers, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).

     4. Select **google.cloud.pubsub.topic.v1.messagePublished** from the **Event type** list. Your trigger configuration varies depending on the supported event type. For more information, see [Event types](https://docs.cloud.google.com/eventarc/docs/event-types).

     5. From the **Select a Cloud Pub/Sub topic** list, choose a topic for the trigger to monitor. Messages you publish to this topic trigger calls to your function.

     6. If the **Region** field is enabled, select a [location](https://docs.cloud.google.com/eventarc/docs/overview#trigger-location) for the Eventarc trigger. In general, the location of an Eventarc trigger should match the location of the Google Cloud resource that you want to monitor for events. In most scenarios, you should also deploy your function in the same region. See [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations) for more details about Eventarc trigger locations.

     7. In the **Service account** field, select a service account. Eventarc triggers are linked to service accounts to use as an identity when invoking your function. Your Eventarc trigger's service account must have the permission to invoke your function. By default, Cloud Run uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

     8. Optionally, specify the **Service URL path** to send the incoming request to. This is the relative path on the destination service to which the events for the trigger should be sent. For example: `/`, `/route`, `route`, and `route/subroute`.

     9. Optionally, to enable retries if the delivery attempt fails, select the **Enable retry on failure** checkbox; otherwise, the default behavior is a single delivery attempt with no retries. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events).

     10. After you've completed the required fields, click **Save trigger**.




###  gcloud 

To create a trigger for your service or function using the gcloud CLI:

  1. [Deploy your service or function](https://docs.cloud.google.com/run/docs/deployment-options-for-services) if you haven't already done so.

  2. If you have an existing Pub/Sub topic, skip this step. Otherwise, create a Pub/Sub topic:
         
         gcloud pubsub topics create TOPIC_NAME

  3. Select the tab for your selected trigger configuration:

### Direct

     1. Configure the required roles for the Pub/Sub service agent:

#### Required roles for the Pub/Sub service agent

**Important:** If your project was created on or before April 8, 2021, you must grant the [ `iam.serviceAccountTokenCreator`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) role to the [service agent](https://docs.cloud.google.com/iam/docs/service-agents) `service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com` on the project in order to allow Pub/Sub to create tokens. However, if your project was created after that date, you do not need to grant it this role because it has the [ `roles/pubsub.serviceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.serviceAgent) role with identical permissions.

The following steps describe how to create and use a service account that can be used by the Pub/Sub subscription to invoke your service or function. These steps are required when using the Google Cloud CLI to create a Pub/Sub trigger command. If you are using the Google Cloud console to create the trigger, you can skip these steps.

        1. Create or select a service account to represent the Pub/Sub subscription identity.
               
               gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
                       --display-name "Cloud Run Pub/Sub Invoker"

Replace `SERVICE_ACCOUNT_NAME` with a name unique for your service account.

        2. Give the invoker service account permission to invoke your service:
               
               gcloud run services add-iam-policy-binding SERVICE_NAME \
                    --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
                    --role=roles/run.invoker

It can take several minutes for the IAM changes to propagate. In the meantime, you might see `HTTP 403` errors in the service logs.

        3. Allow Pub/Sub to create authentication tokens in your project:
               
               gcloud projects add-iam-policy-binding PROJECT_ID \
                    --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
                    --role=roles/iam.serviceAccountTokenCreator

Replace the following:

           * `PROJECT_ID`: your Google Cloud project ID.
           * `PROJECT_NUMBER`: your Google Cloud project number.

Project ID and project number are listed in the _Project info_ panel in the [Google Cloud console](https://console.cloud.google.com/) for your project.

     2. Create a Pub/Sub subscription with the service account:
            
            gcloud pubsub subscriptions create SUBSCRIPTION_NAME \
              --topic TOPIC_NAME \
              --ack-deadline=600 \
              --push-endpoint=SERVICE_URL/ \
              --push-auth-service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace the following:

        * `SUBSCRIPTION_NAME`: the name of the subscription you want to create.
        * `TOPIC_NAME`: the name of the topic you previously created.
        * `SERVICE_URL`: the HTTPS URL provided on deploying the service. This URL works even if you have also [added a domain mapping](https://docs.cloud.google.com/run/docs/mapping-custom-domains).
        * `SERVICE_ACCOUNT_NAME`: the name of the service account you created earlier.
        * `PROJECT_ID`: your Google Cloud project ID.

Notes:

        * The `--push-auth-service-account` flag activates the Pub/Sub push functionality for [Authentication and authorization](https://docs.cloud.google.com/pubsub/docs/authenticate-push-subscriptions).

        * Your Cloud Run service domain is automatically registered for use with Pub/Sub subscriptions.

        * For Cloud Run only, there is a built-in authentication check that the token is valid and an authorization check that the service account has permission to invoke the Cloud Run service.

### Eventarc

Run the following command to create a trigger that filters and routes events:
    
    gcloud eventarc triggers create TRIGGER_NAME  \
       --location=LOCATION \
       --destination-run-service=DESTINATION_RUN_SERVICE  \
       --destination-run-region=DESTINATION_RUN_REGION \
       --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
       --transport-topic=projects/PROJECT_ID/topics/TOPIC_NAME \
       --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace the following:

     * `TRIGGER_NAME`: the ID of the trigger or a fully qualified identifier. 
     * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`. 

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

     * `DESTINATION_RUN_SERVICE`: the name of the deployed service or Cloud Run function that receives the events for the trigger.
     * `DESTINATION_RUN_REGION`: (optional) the [Cloud Run location](https://docs.cloud.google.com/run/docs/locations) in which the destination Cloud Run function can be found. If not specified, it is assumed that the function is in the same region as the trigger.
     * `--event-filters="type=google.cloud.pubsub.topic.v1.messagePublished"` flag is required and can't be changed. For a different event type, you must create a new trigger.
     * `TOPIC_NAME`: the ID of the existing Pub/Sub topic. The topic must be in the same project as the trigger. 
     * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
     * `PROJECT_ID`: your Google Cloud project ID. 

Notes:

     * Optionally, to specify a single event delivery attempt with no retries, use the `--max-retry-attempts` flag. The only valid value is `1`. If you omit the flag, the standard retry behavior applies. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events). 
     * Other flags are available. For more information, see [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create). 




###  Terraform 

To create an Eventarc trigger for a Cloud Run function, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).

## Next steps

  * Learn how to [trigger services from Pub/Sub](https://docs.cloud.google.com/run/docs/tutorials/pubsub).
  * Learn how to [configure retries](https://docs.cloud.google.com/run/docs/tips/function-retries). 
  * Learn how to [trigger with events](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-31 UTC."],[],[]] 
