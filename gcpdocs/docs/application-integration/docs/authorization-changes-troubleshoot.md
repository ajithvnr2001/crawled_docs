---
url: https://docs.cloud.google.com/application-integration/docs/authorization-changes-troubleshoot/
title: Troubleshoot authorization errors \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T11:12:27.744700+00:00
---

# Troubleshoot authorization errors  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/authorization-changes-troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot authorization errors

This page explains the authorization errors you might encounter after the [authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes), and how to resolve them.

Denied actions typically occur for one of two reasons:

  * **Run-as service account permissions** : Either the caller lacks permission to act as the service account, or the service account lacks the required resource permissions. See Run-as service account errors.
  * **Caller IAM roles** : The caller does not have the required IAM role to perform the action. See IAM role errors.



Because Application Integration checks both requirements, resolving an issue with one does not automatically resolve issues with the other.

## Run-as service account errors

Because some of these authorization checks are still rolling out, you might not encounter all of these errors immediately. In the error messages, `PRINCIPAL` is the account evaluated by the system. The message displays `The caller` if the account identity cannot be determined.

Condition | Error or behavior | Resolution  
---|---|---  
A principal (user, automation, or trigger) starts an integration but lacks permission to act as the integration's run-as service account. | The execution is rejected with the following error: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to run this integration.`

  * An API call returns the error directly, and no entry appears in your execution logs.
  * A Cloud Pub/Sub, Eventarc, or Integration Connectors event trigger records a failed execution in your execution logs, and the event is not redelivered.
  * A Cloud Scheduler job reports a `PERMISSION_DENIED` error.

| [Grant the Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) role to the principal starting the integration. For a trigger, grant this to the trigger's service account.  
An integration created on or after October 15, 2026, using a trigger other than API or Private, does not have a run-as service account. | Publishing and testing fail with the following error: `Set a run-as service account. These triggers run with no caller: TRIGGERS. Required for integrations created on or after October 15, 2026 (UTC).` | [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as).  
An execution triggered without user credentials does not have a run-as service account. | If integration governance is enabled for the region, publishing and testing fail with the following error, regardless of the integration's creation date: `Your project requires a run-as service account. Set one before publish or test.` Governance refers to the **Enable governance** setting described in [Edit region](https://docs.cloud.google.com/application-integration/docs/enable-new-region#edit-region).   
  
For regions without governance, the system does not reject these executions starting October 15, 2026. However, the following are planned to fail in a future release: 

  * Tasks lacking an identity, such as Connectors, Call REST Endpoint, or Cloud Run functions tasks.
  * Asynchronous executions, which will fail with the following error: `Integration NAME needs a run-as service account to run asynchronously via trigger TRIGGER_ID.`

| [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as).  
A Call Integration task cannot start its sub-integration. | The calling integration's Call Integration task fails for one of the following reasons: 

  * The sub-integration is called asynchronously and has no run-as service account, even if the calling integration has one: `Integration NAME needs a run-as service account to run asynchronously via trigger TRIGGER_ID.`
  * The principal that started the calling integration, or the calling integration's run-as service account, lacks permission to act as the sub-integration's run-as service account: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to run this integration.`

| [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as) on the sub-integration, or configure the call to run synchronously. Then, [grant the Service Account User role](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access#who_needs_it) on the sub-integration's service account.  
A principal publishes or tests an integration that uses an authentication profile without permission to act as its service account, or an execution reaches a task that uses that profile. | Publishing or testing fails, or the task fails, with the following error: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to use auth config "AUTH_PROFILE_NAME".` Whether the execution continues depends on how the task is configured to handle errors. | [Grant the Service Account User role](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) on the service account specified in the profile.  
A principal creates or edits a **Service account** or **OIDC token** authentication profile without permission to act as the specified service account. | Saving the profile fails with the following error: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to save this auth config.` | [Grant the Service Account User role](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) on the account named in the profile to the principal managing it.  
An approver lacks permission to act as the run-as service account. | Approving or resuming the execution fails with the following error: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to resume this execution.` The execution remains paused until it expires, which can make approvals appear as if they have stopped working. | [Grant the Service Account User role](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) to all potential approvers.  
A principal publishes or tests an integration without permission to act as its run-as service account. | `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to publish or test this integration.` Previously published versions continue running. If you use automation to publish, this error surfaces in your deployment pipeline logs rather than in the Google Cloud console. | [Grant the Service Account User role](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) to publishers, testers, and automated deployment service accounts.  
A task runs using the credentials of the principal who triggered it, and that principal lacks access to the target resource. In a new integration, and starting October 15, 2026, in a test of any integration, the [JavaScript](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task), [Data Transformer Script](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task), and [Data Mapping](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task) tasks operate this way. | The execution starts normally, but a task fails referencing a resource, even if no changes were made to the integration. | Grant the principal access to the resource, or assign the integration a run-as service account that already possesses the required access. Using a run-as service account is the recommended approach, as it ensures the integration's access remains consistent regardless of who triggers it.  
  
For the full list of Application Integration error codes, see [Error codes](https://docs.cloud.google.com/application-integration/docs/error-codes).

## IAM role errors

In addition to verifying the run-as service account, Application Integration verifies the caller's IAM permissions for each action. If you encounter a `PERMISSION_DENIED` error when interacting with an integration, or if execution logs fail to load, ensure you possess a role that grants the required permissions: 

Action | Required roles  
---|---  
View and open integrations | `roles/integrations.integrationViewer`  
View execution logs and details | `roles/integrations.integrationViewer` or `roles/integrations.integrationInvoker`  
Run an integration | `roles/integrations.integrationInvoker` or `roles/integrations.integrationEditor`  
Create and edit integrations | `roles/integrations.integrationEditor`  
Publish an integration | `roles/integrations.integrationDeployer` or `roles/integrations.integrationEditor`  
Approve or resume a suspended run | `roles/integrations.suspensionResolver` or `roles/integrations.integrationAdmin`  
Gain full access to all integrations | `roles/integrations.integrationAdmin`  
**Note:** Approving or resuming a suspended execution requires the `integrations.suspensions.resolve` permission, which the `roles/integrations.integrationEditor` role does not include. Approvers require the `roles/integrations.suspensionResolver` role, as well as the Service Account User role (`roles/iam.serviceAccountUser`) on the run-as service account.**Note:** The roles listed above do not allow you to modify access permissions. Granting the roles and permissions described on this page requires a separate administrative role: 

  * `roles/iam.serviceAccountAdmin` to grant the Service Account User role on a service account.
  * `roles/resourcemanager.projectIamAdmin` to grant project-level Application Integration roles.

Project Owners hold both roles by default. If you cannot assign a grant yourself, contact an administrator who has the required permissions.

To grant a role, run the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='user:PRINCIPAL' \
        --role='ROLE'
    

For more information, see the following resources:

  * [Predefined IAM roles](https://docs.cloud.google.com/application-integration/docs/predefined-iam-roles-permissions) for the complete list of roles and the specific permissions they contain.
  * [Access control](https://docs.cloud.google.com/application-integration/docs/access-control) for details on how Application Integration uses IAM.

**Caution:** If your organization scopes roles to individual integrations using [IAM conditions](https://docs.cloud.google.com/application-integration/docs/add-iam-conditions), the condition must match the specific integration you are accessing. A role binding that grants access to one integration might not grant access to another. If you encounter permission errors despite having the correct role, verify the conditions attached to your role binding.

## Troubleshoot ineffective grants

  * **Grant applied to the wrong project:** The grant must be made in the project that owns the _service account_ , which is not necessarily the project that owns the integration.
  * **Propagation delay:** Authorization decisions are cached briefly, in addition to standard IAM propagation delays. Wait a few minutes before retrying.
  * **Multiple service accounts involved:** The run-as service account, each authentication profile's service account, and each sub-integration's run-as service account are evaluated separately. Each requires its own explicit grant.
  * **Grant applied to the wrong principal:** For a Cloud Scheduler, Cloud Pub/Sub, Eventarc, or Integration Connectors event trigger, the principal that requires the grant is the trigger's service account, not your user account. See [Who needs the Service Account User role](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access#who_needs_it).
  * **Blocked by caller roles:** The Service Account User role determines if you can act _as_ the run-as service account. However, a separate IAM role governs whether you are permitted to perform the integration action itself. See IAM role errors.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
