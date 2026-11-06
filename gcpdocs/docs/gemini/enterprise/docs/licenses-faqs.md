---
url: https://docs.cloud.google.com/gemini/enterprise/docs/licenses-faqs/
title: Frequently asked questions about Gemini Enterprise subscriptions and licenses \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:06:04.396502+00:00
---

# Frequently asked questions about Gemini Enterprise subscriptions and licenses  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/licenses-faqs/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Frequently asked questions about Gemini Enterprise subscriptions and licenses Stay organized with collections  Save and categorize content based on your preferences. 

This page provides answers to common questions about managing and using the Gemini Enterprise licenses.

## Manage subscriptions

This section covers common questions related to managing your Gemini Enterprise subscriptions.

### Why can't I view and modify subscriptions, including reclaiming, and distributing licenses?

You must have the [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) role to manage subscriptions. You can also use a custom role with specific permissions. Verify that you have this role or the required permissions. If you don't have either, contact your billing account administrator.

For more information, see:

  * [Find a Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-administrator)
  * [Before you begin in Get subscriptions and assign licenses for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#before-you-begin).



### Can I update the subscription name?

No, you can't update the subscription name after the subscription is created.

If the subscription name is shown as `n/a`, it is a placeholder for a subscription purchased through a sales channel or an offline order form, and it doesn't mean the subscription is invalid.

### Can I reduce the license count?

No, you can't reduce the license count during an active subscription term. License reductions are only possible when the subscription term ends or is up for renewal.

### Why can't I modify or manage the subscription through Google Cloud console?

If you purchased your subscription through an offline order form, you can't modify or manage it directly within the Google Cloud console. Offline order forms are handled outside of the console's self-service interface. To make any changes or updates to your subscription, such as adjusting license counts or renewing, contact your Google Account Manager.

### Why is Edit turned off on the Manage Users page?

In the **Gemini Enterprise licenses** section on the **Manage Users** page, the **Edit** button is turned off.

You can't modify subscription settings directly on this page. Instead, to update settings like license counts, see [Update subscription settings](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#update-subscription).

### What does the `Subscription already exists` error mean when trying to purchase a new subscription?

This error means that your Cloud Billing account already has an active subscription for the same Gemini Enterprise edition, regardless of whether the subscription period is monthly or annual. A single Cloud Billing account can have only one active subscription per edition at a time.

To use your existing subscription in a different project or projects:

  1. [Update the existing subscription](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#update-subscription) to increase the license count.
  2. [Distribute the licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) to the new project.



### Can I change my subscription period between monthly and annual?

No, you can't directly change the billing period of an active Gemini Enterprise subscription in the Google Cloud console. You also can't purchase a second subscription for the same edition on the same Cloud Billing account while the current subscription is active.

To switch between a monthly and an annual billing period, choose one of the following options:

  * **Switch at the end of your current term**. [Cancel your current subscription](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#cancel-subscription) by clearing **Auto renewal**. Your subscription remains active until the end of the current billing term. After the term expires, purchase a new subscription with your preferred billing period and [distribute the licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) to your projects.
  * **Switch before your current term ends** : Contact [Cloud Billing Support](https://docs.cloud.google.com/support/billing) or your Google Cloud sales representative or account manager to request early cancellation of your active subscription. After the cancellation is complete, purchase a new subscription with your preferred billing period.



### Do free-trial licenses include the AI developer tools quota?

No. Free-trial subscriptions don't include access to [AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview) or [pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#pay-as-you-go-usage-above-quota). To use AI developer tools, you must have an active non-trial subscription.

For other Gemini Enterprise features, free-trial seats draw from the same project-level pooled quota allocation as paid seats. For details on weekly pool calculations, see [Quotas for Standard and Plus editions](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#quotas-standard-plus).

## Distribute and assign licenses

This section covers common questions related to distributing and assigning Gemini Enterprise licenses to projects and users.

### Can I use one Gemini Enterprise subscription across multiple projects?

Yes, the Gemini Enterprise subscription is managed at the billing account level. This means that any project associated with that billing account can be allocated licenses from your subscription. You can [distribute the licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) to multiple projects as needed, allowing flexibility in how you manage access across your different development or production environments.

**Note:** Billing-account-level license distribution applies to Gemini Enterprise subscriptions. Standalone [Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-licensing) subscriptions are purchased and managed at the individual project level and can't be distributed or shared across multiple projects.

### Can I distribute licenses to a project in a different organization or billing account?

Yes. License distribution rules depend on your subscription edition:

  * **Seat-based subscriptions (such as Gemini Enterprise Standard and Plus):** You can [distribute licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) to projects across different Google Cloud organizations and projects linked to different Cloud Billing accounts.
  * **Pay-as-you-go subscriptions:** You can distribute licenses to projects across different organizations, but the destination project **must** be linked to the same Cloud Billing account that owns the Pay-as-you-go subscription.



### How do I move or share licenses to a different project or location?

To move, share, or correct a license allocation to a different project or location under the same Cloud Billing account, follow these steps:

  1. **Unassign the licenses in the source project:** If the licenses are assigned to users in the source project and location, [remove the users from those licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#manage-licenses) on the **Manage users** page. You can only reclaim unassigned licenses (attempting to reclaim assigned seats returns a `Not enough licenses remaining` error).
  2. **Reclaim the unassigned licenses to the billing account:** [Reclaim the unassigned licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#reclaim-licenses) from the source project and location so they return to your Cloud Billing account's unallocated subscription pool. You can only perform this action once per calendar day.
  3. **Distribute the licenses to the target project or location:** [Distribute the available licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) from the subscription pool to the destination project or location using the Google Cloud console or the REST API.
  4. **Assign the licenses to users:** [Assign the distributed licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#license-assignment) to users in the destination project and location.



### How do I check the list of projects the licenses are allocated to?

To see which projects are allocated licenses from your Gemini Enterprise subscription, use the REST API. The [subscription details method](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#subscription-detail) provides the information you need, including how you distribute licenses across projects linked to your billing account.

### Can I use a license assigned to me in different projects?

No, a user's license for Gemini Enterprise is only valid within the specific project where you distributed it. While you manage subscriptions at the billing account level, you allocate licenses on a per-project basis. Therefore, if you need to use Gemini Enterprise features in multiple projects, you must explicitly distribute licenses to each of those projects.

### Can I transfer a subscription to a different Cloud Billing account, or what happens if I change a project's billing account?

No. Gemini Enterprise subscriptions are tied to the Cloud Billing account where they were purchased and can't be transferred to another Cloud Billing account.

If you need to move a project to a new Cloud Billing account:

  * **Existing subscription on the old billing account:** The original subscription remains on the old Cloud Billing account and continues to be billed there until it expires or is canceled. If you want to reuse that project's seats on other projects that remain linked to the old Cloud Billing account, [remove users from the licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#manage-licenses) and [reclaim the unassigned licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#reclaim-licenses) back to the old Cloud Billing account before changing the project's billing account.
  * **Licensing the project under the new billing account:**
    * **Seat-based subscriptions (such as Gemini Enterprise Standard and Plus):** Because seat-based licenses support cross-billing-account distribution, licenses previously distributed from the old Cloud Billing account continue working after the project moves to the new billing account, but subscription charges remain billed to the old account. If you want subscription billing to occur under the new Cloud Billing account, purchase a subscription on the new Cloud Billing account, distribute licenses to the project, and [transfer or assign users](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#transfer-users) to the new subscription.
    * **Pay-as-you-go subscriptions:** You can only [distribute licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) to projects that are linked to the Cloud Billing account that owns the subscription. If a project using Pay-as-you-go moves to a new Cloud Billing account, you must subscribe to the Pay-as-you-go edition on the new Cloud Billing account and distribute licenses from that account.



## Troubleshoot

This section covers common issues and their solutions related to Gemini Enterprise licenses.

### Why am I unable to distribute licenses?

Check the following details:

  * Verify that you have enabled the Discovery Engine API in the project you are distributing the licenses to. 
  * Verify you have the [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) role (`roles/billing.admin`) or a custom role with the required permissions. For more information, see [Before you begin in Get subscriptions and assign licenses for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#before-you-begin). 
  * The Google Cloud console does not support distributing licenses to multiple projects. Therefore, use the [REST API method](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) for this task. 



### What does the `Not enough licenses remaining` error mean?

This error means you are trying to reclaim more licenses than what is available and unassigned. You can only reclaim licenses that are not assigned to users. To resolve this, reduce the number of licenses you are attempting to reclaim, or unassign licenses from users.

### What does the `The quantity exceeds the maximum limit of seats for this account` error mean?

When you're purchasing or modifying licenses directly in the Google Cloud console, this error occurs if you try to buy more seats than the limit for your Cloud Billing account.

If you attempt to increase your seat count beyond this limit from the Google Cloud console, or if you attempt to add seats to an account that was previously provisioned above this limit using an offline order form, the operation fails with a maximum seat limit error.

To request seat counts above the online limits, contact your Google Cloud sales representative or account manager to update your order or apply an allowlist exception for your billing account.

### What does the `404 Error: License config not found` error mean?

This error means there is a problem with the request parameter. Before reclaiming or distributing any licenses, verify the subscription information on the [Subscription details page](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#subscription-detail) and the region (Current location) and license config ID (Subscription ID) in the [Manage Users page](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#view-licenses).

### Why can't users access Gemini Enterprise features even though they have licenses?

Common reasons why users might not be able to access features:

  * **Subscription type:** Check if the user's license is from a subscription type that includes the specific features they are trying to access. 
  * **IAM Roles:** Confirm the user has the [Gemini Enterprise User role](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`) for the Gemini Enterprise project. For more information, see [IAM roles and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control). 
  * **Workforce Identity Federation:** If you are using [Workforce Identity Federation](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider), verify that it is correctly configured, as misconfigurations can lead to access issues. 



### What does the `FAILED_PRECONDITION: Failed to allocate quota for agent creation` error mean?

When calling `AgentService.CreateAgent` (or creating a custom agent in the Google Cloud console), you might encounter the following error:

`400 FAILED_PRECONDITION: Failed to allocate quota for agent creation.`

This error means that the calling user or service account isn't entitled to create custom agents in the target project and location. Verify the following causes:

  * **No active license assigned to the calling user or service account:** Custom agent creation requires the calling principal to hold an active eligible license in the project and location where the agent is created. If you're creating agents using a service account (such as in a CI/CD pipeline or with Terraform), [assign an active license seat](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#license-assignment) to the service account's email address in that project and location.
  * **Frontline edition license:** Users holding a Gemini Enterprise Frontline license can interact with prebuilt agents published by administrators, but aren't eligible to create custom agents. Upgrade the user to a Gemini Enterprise Standard or Plus license to enable custom agent creation.
  * **License cache propagation delay:** If you recently distributed or assigned a license to the user or service account, allow 5 to 15 minutes for backend entitlement caches to synchronize before calling the agent creation API.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
