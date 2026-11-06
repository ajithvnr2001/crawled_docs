---
url: https://docs.cloud.google.com/managed-lustre/docs/maintenance-notifications/
title: Maintenance notifications and logs \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:24:24.530563+00:00
---

# Maintenance notifications and logs  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/maintenance-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Maintenance notifications and logs Stay organized with collections  Save and categorize content based on your preferences. 

Managed Lustre provides email notifications, [Cloud Hub](https://docs.cloud.google.com/hub/docs/maintenance) integration, and Cloud Logging records to help you track automated maintenance events across your instances.

## Email notifications

You can subscribe to email notifications for upcoming automated maintenance events to plan for potential disruption. Subscriptions to maintenance notifications are managed through your Google Cloud console Communication page:

[Go to the **Communication** page](https://console.cloud.google.com/user-preferences/communication)

Once subscribed, email notifications are sent based on whether a [maintenance policy](https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies) is configured for the instance.

Instances with a maintenance policy receive the following notifications:

  * **Advance notification** : Sent 7 to 14 days before a scheduled maintenance event, or after a maintenance event has been rescheduled.
  * **Canceled** : Sent if a scheduled maintenance event is canceled by Google, rescheduled, or automatically canceled following a successful self-service upgrade.
  * **In progress** : Sent when a scheduled maintenance event starts.
  * **Completed** : Sent when a scheduled maintenance event is completed.



Instances without a maintenance policy receive **In progress** and **Completed** notifications when automated maintenance occurs.

[Self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance) doesn't send email notifications or write maintenance logs. See [Track maintenance progress](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance#track_maintenance_progress) for how to monitor self-service maintenance progress.

## View maintenance in Cloud Hub

[Cloud Hub](https://docs.cloud.google.com/hub/docs/maintenance) lets you track automated maintenance activities across your Managed Lustre instances and other supported Google Cloud services. You do not need to configure anything on your Managed Lustre instances. For Cloud Hub setup requirements and required IAM roles, see [Before you begin](https://docs.cloud.google.com/hub/docs/maintenance#before-you-begin).

Instances without a maintenance policy report ongoing and completed activities during automated maintenance. Instances with a maintenance policy also report advance scheduled activities and canceled activities. User-initiated self-service maintenance is not tracked in Cloud Hub.

The Cloud Hub Maintenance page displays the following:

  * Scheduled and ongoing maintenance activities in the **Maintenance** table.
  * Completed and canceled maintenance activities from the past 30 days in the **Maintenance history** table.
  * Maintenance activity details, including event descriptions, timelines, affected instance names, locations, and progress states.



[Go to Maintenance](https://console.cloud.google.com/cloud-hub/maintenance)

## View maintenance logs

Cloud Logging records maintenance events for Managed Lustre across two log streams: unified maintenance event logs and instance maintenance logs.

  * Unified maintenance event logs: Standardized maintenance lifecycle events from Unified Maintenance with the log ID `maintenance.googleapis.com/maintenance_events`. These logs support log-based alerting across notification channels such as Pub/Sub, Slack, PagerDuty, and webhooks.
  * Instance maintenance logs: Service-specific activity records with the log ID `lustre.googleapis.com/maintenance`.



### Unified maintenance event logs

Unified Maintenance logs maintenance lifecycle events for Managed Lustre instances using the [`ResourceMaintenance`](https://docs.cloud.google.com/unified-maintenance/docs/log-schema) schema.

Event states in `jsonPayload.state` include the following values:

  * `SCHEDULED`: Maintenance is scheduled for a future window.
  * `STARTED`: Maintenance is in progress.
  * `SUCCEEDED`: Maintenance completed successfully.
  * `CANCELLED`: Maintenance was canceled or superseded by a self-service upgrade.



You can view unified maintenance logs using Logs Explorer or the gcloud CLI.

###  Logs Explorer 

To view unified maintenance logs using Logs Explorer, do the following:

  1. In the Google Cloud console, go to the **Cloud Logging** > **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer)

  2. Enter the following filter into the query editor and click **Run query** :
         
         log_id("maintenance.googleapis.com/maintenance_events")
         jsonPayload.resource.type="lustre.googleapis.com/Instance"
         

To filter by a specific maintenance state, add the `jsonPayload.state` field:
         
         log_id("maintenance.googleapis.com/maintenance_events")
         jsonPayload.resource.type="lustre.googleapis.com/Instance"
         jsonPayload.state="STATE"
         

Replace STATE with `SCHEDULED`, `STARTED`, `SUCCEEDED`, or `CANCELLED`.




###  gcloud CLI 

To view unified maintenance logs with the gcloud CLI, run the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command:
    
    
    gcloud logging read 'log_id("maintenance.googleapis.com/maintenance_events") AND jsonPayload.resource.type="lustre.googleapis.com/Instance"' --project=PROJECT_ID
    

Replace `PROJECT_ID` with your Google Cloud project ID.

To configure alerts and route notifications for scheduled maintenance events to channels such as email, Pub/Sub, PagerDuty, Slack, or ServiceNow, see [Configure alerts and notifications](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications). For details on log fields and event structures, see the [Unified Maintenance log schema](https://docs.cloud.google.com/unified-maintenance/docs/log-schema).

### Instance maintenance logs

Managed Lustre writes service-specific maintenance records with the log ID `lustre.googleapis.com/maintenance`. These logs record the following activity types:

  * `LustreAdvancedNotification`: Maintenance has been scheduled for the instance. Sent only for instances with a maintenance policy.
  * `LustreOngoingNotification`: Maintenance has started on the instance. Once complete, another `LustreOngoingNotification` event is logged with `is_completed=true`.
  * `LustreCancelledNotification`: Maintenance has been canceled. Sent only for instances with a maintenance policy.



You can view instance maintenance logs using Logs Explorer or the gcloud CLI.

###  Logs Explorer 

To view Managed Lustre instance maintenance logs using Logs Explorer, do the following:

  1. In the Google Cloud console, go to the **Cloud Logging** > **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer)

  2. Enter the following filter into the query editor and click **Run query** :
         
         resource.type="lustre.googleapis.com/Instance"
         resource.labels.instance_id="INSTANCE_ID"
         resource.labels.location="LOCATION"
         logName="projects/PROJECT_ID/logs/lustre.googleapis.com%2Fmaintenance"
         

Replace the following:

     * INSTANCE_ID: The ID of your Managed Lustre instance.
     * LOCATION: The location of your Managed Lustre instance.
     * PROJECT_ID: The ID of your Google Cloud project.



###  gcloud CLI 

To view instance maintenance logs with the gcloud CLI, run the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command:
    
    
    gcloud logging read 'resource.type="lustre.googleapis.com/Instance" resource.labels.instance_id="INSTANCE_ID" resource.labels.location="LOCATION" logName="projects/PROJECT_ID/logs/lustre.googleapis.com%2Fmaintenance"' --project=PROJECT_ID
    

Replace the following:

  * `INSTANCE_ID`: The ID of the Managed Lustre instance.
  * `LOCATION`: The zone where the instance is located.
  * `PROJECT_ID`: The project ID of the project where the instance is located.



## What's next

  * [Maintenance overview](https://docs.cloud.google.com/managed-lustre/docs/maintenance)
  * [Configure maintenance policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies)
  * [Perform self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance)
  * [Configure alerts and notifications for maintenance events](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications)
  * [View maintenance in Cloud Hub](https://docs.cloud.google.com/hub/docs/maintenance)
  * [Review the Unified Maintenance log schema](https://docs.cloud.google.com/unified-maintenance/docs/log-schema)
  * [Learn about Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
