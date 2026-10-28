---
url: https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access/
title: Grant Service Account User for run-as service accounts \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T09:50:59.511930+00:00
---

# Grant Service Account User for run-as service accounts  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Grant Service Account User for run-as service accounts

This page lists the principals who require the Service Account User (`roles/iam.serviceAccountUser`) role for the upcoming [authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes), and explains how to grant it.

**Warning:** Grant the role before you [set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as). Setting a run-as service account requires you to publish the integration, and publishing requires this role. If you attempt to set the service account before granting the required role, the publish action fails.

## Who needs the Service Account User role

The following principals require the Service Account User role on the listed service account:

Principal | Service account  
---|---  
Users who publish or test the integration, including deployment automation. | The integration's run-as service account  
Users and automation that run the integration through the API or the Google Cloud console, synchronously or asynchronously. | The integration's run-as service account  
The service account that a trigger uses to start the integration. This includes the **Service account email** of a [Cloud Scheduler trigger](https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger), or the **Service account** of a [Cloud Pub/Sub trigger](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger), an [Eventarc trigger](https://docs.cloud.google.com/application-integration/docs/configure-eventarc-trigger), or an [Integration Connectors event trigger](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks#event_triggers). This is not required if the trigger account is the run-as service account itself. | The integration's run-as service account  
Users who approve or resume a suspended run. | The integration's run-as service account  
The principal that starts an integration that calls a sub-integration using the [Call Integration](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task) task. For an integration started by a trigger with a service account, this is the trigger's service account. | The sub-integration's run-as service account, in addition to the calling integration's run-as service account  
The calling integration's run-as service account, when it calls a sub-integration asynchronously. This is not required if both integrations use the same service account. | The sub-integration's run-as service account  
Users who create or edit an [authentication profile](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles) of type **Service account** or **OIDC token**. | The service account named in the profile  
Users who publish or test an integration that uses that profile, including deployment automation. | The service account named in the profile  
The principal that runs an integration that reaches a task using that profile. For an asynchronous or scheduled run, this is the integration's run-as service account, or the Application Integration service agent, `service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`, if the integration does not have one. Setting a run-as service account is the recommended fix in that case. | The service account named in the profile  
  
Saving a draft does not require the Service Account User role. The authorization checks on publishing, testing, and saving authentication profiles currently apply. The checks on running, approving, calling sub-integrations, and running tasks that use an authentication profile will take effect as the rollout proceeds. Grant these roles proactively to ensure your integrations continue to run successfully.

**Note:** The Application Integration roles, including `roles/integrations.integrationInvoker`, do not grant `iam.serviceAccounts.actAs`. The Service Account User role is always a separate grant.

## Grant the role

To grant the role to a principal, run the following command:
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT \
        --project=SERVICE_ACCOUNT_PROJECT_ID \
        --member='user:PRINCIPAL' \
        --role='roles/iam.serviceAccountUser'
    

Replace the following:

  * `SERVICE_ACCOUNT`: The email address of the run-as service account, or of the account named in an authentication profile.
  * `SERVICE_ACCOUNT_PROJECT_ID`: The ID of the project that _owns the service account_.
  * `PRINCIPAL`: The email address of the user.



For other principal types, use the corresponding `--member` prefix:

  * **Groups:** Use `group:`. We recommend using Google groups rather than individual user accounts to simplify access management as team members change.
  * **Service accounts:** Use `serviceAccount:` for automated processes, applications, and trigger service accounts.

**Caution:** The `--project` flag must specify the project that owns the service account. If your run-as service account resides in a different project from the integration, the grant belongs in the service account's project. Granting this role in the integration's project has no effect. A project-level grant is valid, provided it is applied to the project that owns the service account.

To grant the role in the Google Cloud console:

  1. Go to **IAM & Admin** > **Service Accounts**.
  2. Select the service account.
  3. Click **Permissions** > **Grant access**.



To grant this role, you need the `roles/iam.serviceAccountAdmin` role on the service account. Project Owners have this by default. For more information, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

## What's next

  * [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as) on integrations that run without a user identity.
  * If a grant does not seem to work, see [Troubleshoot authorization errors](https://docs.cloud.google.com/application-integration/docs/authorization-changes-troubleshoot).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
