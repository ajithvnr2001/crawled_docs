---
url: https://docs.cloud.google.com/resource-manager/docs/project-suspension-guidelines/
title: Project suspension guidelines \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-09T06:57:46.672468+00:00
---

# Project suspension guidelines  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/project-suspension-guidelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/resource-manager/docs/resources)



Send feedback 

#  Project suspension guidelines Stay organized with collections  Save and categorize content based on your preferences. 

Google treats policy and Terms of Service (ToS) violations very seriously in order to protect users, resources, and data. If Google Cloud suspends your project because it violates policy or ToS, you can use built-in safeguard and recovery tools to regain access to your resources. By learning how suspensions affect your project, you can fix issues more quickly and avoid future disruptions.

## Suspended versus orphaned project resources

A project resource or user can be suspended by Google due to ToS violations. If the user is the sole owner of a project resource, that project will also be suspended. When this happens, existing workloads are shut down, and users lose access to the suspended project resource. Project owners will receive an email notification informing them of the suspension, and how to appeal the suspension. If a project resource is suspended for more than nine months, it is marked for deletion. See the [Policy Violations FAQ](https://support.google.com/cloud/answer/7002354?hl=en) for more information on appeal best practices in case of a project resource suspension. 

A project resource becomes orphaned if it doesn't have an owner, regardless of whether they are active or suspended. This might come about if the Google accounts belonging to all owners or users associated with the project resource are deleted. A project resource isn't considered orphaned if the owners are suspended.

Orphaned project resources are inaccessible. To recover access to an orphaned project, see Recover lost access to projects and organizations. A project resource that is orphaned will immediately be marked for deletion unless one of the following criteria is met:

  1. It has some API activity that is reflected in the logs.
  2. It is associated with a [Google Workspace](https://gsuite.google.com) customer domain.
  3. It has a live [App Engine](https://cloud.google.com/appengine) app.
  4. It has any active or future Variable Term Quota.
  5. It is linked to a Cloud Billing account.
  6. It is owned by an [Organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) resource.



Projects that are marked for deletion are not usable, and will be fully deleted after approximately 30 days. Some resources, such as Cloud Storage resources, are deleted much sooner. For more information about the project deletion process, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).

## How to avoid orphaned projects

In order to prevent a project from becoming orphaned, we recommend that more than one owner be associated with the project at all times.

If a project belongs to an [Organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations), then it will always have at least the Organization as an owner and as such will not be orphaned. The Organization administrator has full control over each project in the Organization. To eliminate the risk of a project resource becoming orphaned, we recommend [obtaining an Organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) and migrating all production projects under it.

## Recover lost access to projects and organizations

If you lose access to a Google Cloud project or organization resource, the recovery process depends on whether the resource belongs to an organization resource or is a standalone project.

### Recover access to a project in an organization

If a project belongs to an [organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations), you can recover access without contacting Cloud Customer Care. Organization Administrators (`roles/resourcemanager.organizationAdmin`) have full control over all projects in the organization resource and can grant the Owner role (`roles/owner`) or reassign project ownership directly.

To recover access to a project in an organization resource, do one of the following:

  * Ask an Organization Administrator in your organization to grant you the Owner role (`roles/owner`) or another appropriate Identity and Access Management (IAM) role on the project. For instructions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * If your organization doesn't have an active Organization Administrator, ask your Google Workspace or Cloud Identity super administrator to assign the Organization Administrator role (`roles/resourcemanager.organizationAdmin`), and then grant access to the project. For instructions, see [Grant access to an organization resource](https://docs.cloud.google.com/resource-manager/docs/access-control-org#grant-access).



### Recover access to an organization resource

Customer Care can't directly grant access to a Google Cloud organization resource. If you lose access to your organization resource, recover access through your Google Workspace or Cloud Identity domain account:

  1. Sign in to the Google Admin console using a Google Workspace or Cloud Identity super administrator account and grant the Organization Administrator role (`roles/resourcemanager.organizationAdmin`) on the organization resource.
  2. If you don't have access to a super administrator account, follow the [administrator account recovery process](https://support.google.com/a/answer/33561) to regain access to your Google Workspace or Cloud Identity account. If automated recovery isn't available and you can modify your domain's DNS records, you can verify domain ownership through [administrator access recovery](https://support.google.com/a/answer/7579987).



### Recover access to a standalone project

A standalone project is a project that doesn't belong to an organization resource. Before you contact Customer Care to recover access to a standalone project, you must exhaust all self-service recovery options.

#### Try self-service recovery options first

Before you open a support case, attempt all of the following self-service recovery methods:

  * **Contact existing project owners** : reach out to all current project owners and ask them to grant you the Owner role (`roles/owner`) in the Google Cloud console.
  * **Recover an existing owner account** : if you no longer have the credentials for an existing owner account, try to recover the account: 
    * **Managed Google Workspace or Cloud Identity account** : ask your domain administrator to reset the user's password or [restore a recently deleted user account](https://support.google.com/a/answer/1397578), which is available within 20 days of deletion.
    * **Personal Google Account** : use the [Google Account recovery page](https://accounts.google.com/signin/recovery) to recover the account through its configured recovery email address or phone number. If the account has an alternate email address, you can also sign in using that alternate email address and password.
    * **Conflicting account ending in`@gtempaccount.com`**: if an owner's email address ends in `@gtempaccount.com`, ask the user to sign in and resolve the account conflict by using the [conflicting accounts troubleshooter](https://support.google.com/accounts/troubleshooter/1699308).
  * **Accept a pending owner invitation** : if an active user in your company has a pending invitation to become a project owner, ask that user to sign in with the invited email address and accept the invitation in the Google Cloud console.
  * **Impersonate an owner service account** : if a service account has the Owner role (`roles/owner`) on the project, any principal with the Service Account User role (`roles/iam.serviceAccountUser`) on that service account can impersonate the service account and grant project access.



#### Request access recovery from Customer Care

If you have exhausted all self-service recovery options and still can't access a standalone project, you can contact [Customer Care](https://console.cloud.google.com/support) to request project access recovery. Customer Care can evaluate access recovery requests only for orphaned standalone projects, which are standalone projects that have no active human owners or whose registered owners are all unresponsive.

When you submit a recovery request, Customer Care follows a mandatory verification and notification process:

  1. **Owner notification and response window** : even if you have already tried to contact the existing project owners, Customer Care is legally required to contact all registered project owners at their primary, secondary, and alternate email addresses. Confirm that Customer Care has your permission to notify the registered owners of your request: 
     * Customer Care waits at least three business days, or 72 hours, for a response to each notification attempt, up to one week in total, before declaring the project orphaned.
     * If an existing owner responds and approves the request, that owner can grant you access directly.
     * If an existing owner responds and denies the request, Customer Care can't grant you access.
  2. **Verifiable data justification** : if the registered owners don't respond within the mandatory response window, you must provide verifiable data that proves your legitimate ownership of the project and its workloads before Customer Care can evaluate granting access. Depending on your access level, Customer Care might require several of the following data points:

     * Approval from the Billing Account Administrator (`roles/billing.admin`) of the Cloud Billing account linked to the project, along with the billing account ID and most recent billed amount. If your only goal is to stop charges on an orphaned project, the Billing Account Administrator can [disable billing on the project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#how-to-disable-billing) instead of recovering project access.
     * Domain ownership verification through a DNS `TXT` record or approval from at least two domain administrators, if all existing owner accounts belong to your domain.
     * Project creation date, original project creator, and current or previous project owners.
     * Specific project configuration details and resource identifiers, such as user-created service accounts, OAuth 2.0 client IDs and authorized domains, API keys, or active resource names.

Approval from a Google representative, such as an account manager or customer engineer, isn't accepted as data justification because Google representatives don't have visibility into project data or legal ownership. If you can't provide sufficient verifiable data to prove ownership, Customer Care can't grant access to the project.




#### Projects ineligible for Customer Care

Customer Care can't grant access to the following types of projects:

  * **Projects in an organization resource** : recover access through your organization administrator or super administrator account.
  * **Google-owned internal projects** : projects under the `google.com` organization aren't eligible for external support recovery.
  * **Firebase-only projects** : projects that use only Firebase APIs are handled by [Firebase support](https://firebase.google.com/support) through the Firebase project ownership process.
  * **Google Cloud Marketplace billing projects** : billing projects managed by Google for Cloud Marketplace services aren't eligible for customer access.
  * **Resold customer projects** : resellers can't be granted access to projects linked to resold billing accounts, even if the reseller is a Billing Account Administrator. To stop charges on a project, a reseller can [disable billing on the project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#how-to-disable-billing).
  * **Default Google Apps Script projects** : Customer Care can't grant access to default projects created automatically for Apps Script, which have project names starting with `sys-`. For more information, see [Google Cloud projects in Apps Script](https://developers.google.com/apps-script/guides/cloud-platform-projects).



## Effect of ToS violations

### Google-wide disabled account

In some cases a Google-wide account (which covers access to a variety of Google products like Google Photos, Google Play, Google Drive, and Google Cloud) will be disabled for violations of a Google ToS, egregious policy violations, or as required by law. Owners of disabled Google accounts will not be able to access their Google Cloud resources until the account is reinstated. If an account is disabled, a notification is sent to the secondary email address provided during the signup process, if available. If a phone number is available, the user is notified via text message. The notification includes a link for appeal and recovery, where applicable.

In order to regain access to their Google Cloud resources, owners of disabled Google accounts will need to contact Google support and have their account re-enabled. To contact Google support, [log in to your Google account](https://accounts.google.com/Login).

To minimize the effect of an account being disabled on Google Cloud resources, we recommend that you add more than one owner to all resources. As long as there is at least one active owner, Google Cloud resources will not be suspended due to the one of the owners being disabled.

### Google Cloud account suspension

In certain circumstances when a Google Cloud user is consistently violating ToS or [Google Cloud Acceptable Use Policy](https://cloud.google.com/terms/aup) (AUP) through their projects, their access to Google Cloud may be suspended. When that happens, the developer will not be able to access their Cloud projects. They will continue to have access to other Google services like Gmail.

When a Google Cloud account is suspended and the developer has at least one active project, they will get an email informing them about the project being suspended. The developer can go to the Console, fill out the form and reach out to Google to resolve the issue.

See the [Policy Violations FAQ](https://support.google.com/cloud/answer/7002354?hl=en) for more information on appeal best practices in case of a project resource suspension. 

### Google Cloud project suspension

Google Cloud projects may be suspended due to violations of the Google Cloud ToS, including the Google Cloud Acceptable Use Policy (Google Cloud AUP). When activities that violate the Google Cloud AUP or ToS are detected in a project, the project owner has an obligation to fix the violation immediately. If the violation is not fixed, Google may take action to suspend the project. It is important that Google Cloud developers check the project owner email account regularly. If Google suspends a Google Cloud project then all the associated Google Cloud workloads will be suspended as well. The owner of a suspended project will receive a notification email from google-cloud-compliance@google.com with resources to appeal.

If a suspended project resource has at least one owner, whether active or suspended, it is not considered orphaned and will not marked be for deletion. However, a project resource that has been suspended for nine months will be marked for deletion even if it is not orphaned.

To recover a suspended project fix the issue and follow the link in the notification email or contact Google Support. To contact Google support, [log in to your Google account](https://accounts.google.com/Login). See the [Policy Violations FAQ](https://support.google.com/cloud/answer/7002354?hl=en) for more information on appeal best practices in case of a project resource suspension.

## Cloud Billing account suspension

Google Cloud Cloud Billing accounts may be suspended due to violations of Google Cloud ToS, missed payments, or for suspected fraud. If a Cloud Billing account is suspended then all Google Cloud resources attached to that Cloud Billing account are suspended as well.

If your Cloud Billing account remains invalid for a protracted period, some resources might be removed from the projects associated with your account. **Removed resources are not recoverable.** See the [Resolve Cloud Billing issues](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues) page for more information.

To recover a suspended Cloud Billing account, owners can use one of these options:

  * **Submit documents or request a verification code** : Use [Google payments center](https://payments.google.com) to see if you need to submit documents or get a verification code.

[Learn about verifying an account in Google payments center](https://support.google.com/googlepay/answer/7644078#zippy=%2Crequest-a-verification-code%2Cupload-documents).

  * **Make a manual payment** : In the Google Cloud console, sign in to the **Payment overview** page for your Cloud Billing account, and click **Make a payment**.

[Go to Payment overview](https://console.cloud.google.com/billing/payment)

[Learn about making manual payments to your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manual-payment).




You might need to manually restart services that were shut down while the Cloud Billing account was suspended. See [Restarting Google Cloud services](https://docs.cloud.google.com/billing/docs/how-to/restart-services) for information on restarting your services.

Cloud resources linked to a suspended Cloud Billing account are not considered orphaned, as long as they have at least one active owner.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
