---
url: https://docs.cloud.google.com/application-integration/docs/authorization-changes-find-affected/
title: Find integrations that need a run-as service account \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T11:12:26.445003+00:00
---

# Find integrations that need a run-as service account  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/authorization-changes-find-affected/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Find integrations that need a run-as service account

This page helps you find the integrations that require a run-as service account before the [authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes) take effect.

## Determine if an integration needs a run-as service account

You only need a run-as service account when user credentials are not available for the whole run. This occurs in the following situations: 

Execution type | User credentials available? | Run-as service account required?  
---|---|---  
**Synchronous** — A user triggers the integration and waits for the result. | Yes, for the entire execution. | **No**  
**Asynchronous** — The integration is queued and completes later. | Yes, but only when triggered. | **Yes**  
**Unattended** — A schedule or an event triggers the integration. | No, a user is never present. | **Yes**  
**Note:** Asynchronous runs require a run-as service account even if a user triggers them. Queued work does not retain the user's credentials, meaning no identity is available to authorize the integration when it eventually runs. An integration that only runs synchronously does not need a run-as service account unless it calls another integration asynchronously. In that case, the sub-integration requires its own run-as service account.

## Identify affected integrations

An integration runs without a user identity if any of the following conditions are met:

  * It has any trigger other than an [API](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger) or [Private](https://docs.cloud.google.com/application-integration/docs/configure-private-trigger) trigger, for example a [Schedule](https://docs.cloud.google.com/application-integration/docs/configure-schedule-trigger), [Cloud Scheduler](https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger), [Cloud Pub/Sub](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger), [Salesforce](https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger), [Integration Connectors event](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks#event_triggers), or [Eventarc](https://docs.cloud.google.com/application-integration/docs/configure-eventarc-trigger) trigger.
  * It is scheduled through the API using `scheduleIntegrations`.
  * Another integration calls it as an asynchronous sub-integration, using the [Call Integration](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task) task. The sub-integration needs its own run-as service account even if the calling integration has one.
  * It uses the [Suspend](https://docs.cloud.google.com/application-integration/docs/configure-suspend-task) or [Approval](https://docs.cloud.google.com/application-integration/docs/configure-approval-task) task, where a run can sit waiting and then expire on its own.



**Check the run-as service account status**

To list all published versions in a region alongside their run-as service accounts, run the following command:
    
    
    curl -s -G -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      --data-urlencode "filter=state=ACTIVE" \
      --data-urlencode "pageSize=1000" \
      "https://REGION-integrations.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/integrations/-/versions" \
    | jq -r '.integrationVersions[]
             | [ .name, (.runAsServiceAccount // "NONE") ]
             | @tsv'
    

Replace the following:

  * `REGION`: the region of your integration. For the list of supported regions, see [Locations](https://docs.cloud.google.com/application-integration/docs/locations).
  * `PROJECT_ID`: the ID of your Google Cloud project



If the output shows `NONE` for an integration, you only need to take action if the integration meets any of the conditions listed previously.

To check an integration manually, open it in the integration editor and click settings **Integration settings** in the editor toolbar. The **Service account** field displays the run-as service account. It is empty if a service account is not assigned.

**Caution:** Keep `filter=state=ACTIVE` in the request rather than filtering the output afterward. The `-` wildcard returns only the most recently modified version of each integration. If you fetch everything and filter later, an integration whose newest version is an unpublished draft will be omitted from the results, even if an older published version is still running. If the response contains a `nextPageToken`, repeat the request using `pageToken=TOKEN` until the token is no longer returned.**Warning:** Don't rely solely on warnings in the Google Cloud console. An integration on an infrequent schedule, or one that has not been triggered recently, might require action without displaying a warning. Always check your scheduled and event-driven integrations using the steps outlined on this page.

## What's next

  * [Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) on the run-as service accounts you already use.
  * [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as) on each integration you found.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
