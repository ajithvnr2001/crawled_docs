---
url: https://docs.cloud.google.com/chronicle/docs/onboard/provision-additional-instance/
title: Deploy an additional instance \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:45:36.943787+00:00
---

# Deploy an additional instance  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/onboard/provision-additional-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy an additional instance

Supported in:

Google SecOps 

This guide helps platform administrators and security engineers deploy additional Google SecOps instances within an existing unified subscription. It explains how to provision and link new instances using the self-service workflow in the Google Cloud console. By following this method, you scale multi-tenant security operations across business units, subsidiaries, or managed customers without waiting for manual support assistance. Successful deployment streamlines environment isolation while maintaining zero downtime for existing active instances.

## Common use cases

The following use cases describe how organizations deploy additional instances to isolate environments and scale operations:

### Business unit and subsidiary isolation

  * **Objective** : Deploy dedicated instances for distinct business units, subsidiaries, or operational environments (such as development, staging, and production) under a single contract.
  * **Value** : Enforce strict data boundaries and independent access controls while consolidating billing under one subscription.



### Managed security service provider customer onboarding

  * **Objective** : Provision separate Google SecOps instances for individual managed customers under an active managed security service provider (MSSP) subscription.
  * **Value** : Accelerate customer onboarding and maintain tenant isolation without manual support escalation.



## Key terminology

  * **Unified instance** : A Google SecOps tenant that combines SIEM and SOAR capabilities into a single environment linked to a Google Cloud project.
  * **Parent contract** : The active Google SecOps subscription agreement associated with your Cloud Billing account that governs regional residency, package tier, and default data retention settings across all linked instances.
  * **Administrative control project** : The dedicated Google Cloud project linked to an individual Google SecOps instance that controls (IAM) permissions, APIs, and resource settings for that tenant.



## Before you begin

Before you begin, confirm that you have the required permissions and environment setup:

  * **Permissions** : You must have the following roles: 
    * **Billing account permissions** : You need the `billing.resourceAssociations.list` permission or the [Billing Account User (`roles/billing.user`)](https://cloud.google.com/billing/docs/how-to/grant-access-to-billing#update-cloud-billing-permissions) role on the Cloud Billing account associated with your Google SecOps contract.
    * **Target project permissions** : On the target Google Cloud project that hosts the new instance, you need the following roles:
    * [Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin)
    * [Editor (`roles/editor`)](https://cloud.google.com/iam/docs/roles-overview#basic)
    * [Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin)
    * [Chronicle Service Admin (`roles/chroniclesm.admin`)](https://cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin)
    * **Identity provider configuration permissions** : If you use a third-party identity provider (IdP), you need the [IAM Workforce Pool Admin (`roles/iam.workforcePoolAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin) role at the organization level.
  * **Environment check** : You must link each Google SecOps instance to a dedicated Google Cloud project that uses the same Cloud Billing account as your Google SecOps subscription contract. For more information, see [Link an instance to Google Cloud](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).



### Limitations

Self-service additional instance provisioning is subject to the following supportability constraints:

  * **At least one active instance** : Your organization must have at least one existing Google SecOps instance that is already onboarded and active under your subscription contract. Self-service provisioning is disabled if no active instance exists.
  * **Maximum instance limit** : Self-service provisioning is available only when the total number of instances linked to your Cloud Billing account and subscription contract is fewer than 25. If 25 or more instances are linked, the **Add instance** button remains disabled.
  * **Active subscription** : Your Google SecOps subscription contract must be active and valid. You cannot provision additional instances if your subscription is expired or suspended.
  * **Standard, Enterprise, or Enterprise Plus tier** : The subscription must be an active registration for one of the supported Google SecOps packages.
  * **Unified instances only** : All existing instances under your contract must be unified instances. Self-service provisioning is not supported if any existing instance under the agreement is SIEM-only.
  * **Non-compliance instances only** : Self-service provisioning is available only for standard commercial environments. If any existing instance under your contract is configured with compliance controls or sovereign requirements (for example, FedRAMP, IL4, IL5, IL6, CMEK, or DRZ_Advanced), self-service provisioning is disabled. For compliance-controlled environments, contact your Google representative or reach out to [Google SecOps Support](https://console.cloud.google.com/support) for manual provisioning by the compliance engineering team.
  * **Data residency alignment** : All additional instances reside in the same geographic region (for example, `us` or `europe`) as your initial instance. The region selection is locked to match your parent contract and cannot be changed.
  * **Data retention inheritance** : Additional instances automatically inherit the contractual data retention duration of your parent subscription agreement.



## Prepare a Google Cloud project

Prepare the dedicated Google Cloud project that acts as the administrative control layer for the new instance:

  1. **Create or select a dedicated project** : We recommend creating a new, dedicated Google Cloud project for each new instance. Follow the steps in [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).
  2. **Verify billing account association** : The Google Cloud project must use the exact same Cloud Billing account as your Google SecOps subscription contract.
  3. **Verify project availability** : The Google Cloud project must not already be linked to another Google SecOps instance. Each project can host only one instance.
  4. **Configure VPC Service Controls (optional)** : If your organization uses [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), configure the ingress and egress rules documented in [Configure VPC Service Controls for Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops).

**Note:** If the project uses a different Cloud Billing account or is already linked to an existing instance, project selection fails during setup. Verify the billing association on the **Billing** page before starting the deployment.



## Deploy an additional instance

To deploy an additional Google SecOps instance using the Google Cloud console, complete the procedures in the following sections:

  1. Open the Google SecOps page
  2. Select the target project
  3. Add essential contacts
  4. Review deployment details and configure single sign-on
  5. Start the instance setup



### Open the Google SecOps page

Open the **Google SecOps** page in the Google Cloud console to initiate deployment:

  1. In the Google Cloud console, go to the **Google SecOps** page.
  2. The **Instances** table lists all existing Google SecOps instances associated with your billing account.
  3. Click **Add instance**.

**Note:** If the **Add instance** button is unavailable or disabled, your account either lacks billing permissions, has no initial onboarded instance, has 25 or more instances linked to the billing account and contract, or belongs to a compliance-controlled subscription. Review the Limitations section and verify your billing account roles before retrying.



### Select the target project

Link the prepared Google Cloud project to your new Google SecOps instance:

  1. On the **Link SecOps to a project** page, click **Select a project** to open the **Select a resource** dialog.
  2. Select your **Organization** from the drop-down list.
  3. From the **Projects and folders** list, select the Google Cloud project that you prepared for this instance.
  4. Click the name of the eligible Google Cloud project to select it.

**Note:** Google Cloud projects that cannot be selected display a warning warning icon. Hold the pointer over the warning icon to view the specific restriction (for example, billing account mismatch, insufficient permissions, or an existing Google SecOps instance association) and select a compliant project.



### Add essential contacts

Assign contacts to receive critical notifications about technical, security, legal, and billing topics:

  1. In the **Essential contacts** table, click **Add contact** (or click the edit icon next to an existing category).
  2. Enter the contact person's email address.
  3. Select one or more notification categories. You must assign at least one contact for each of the mandatory categories: 
     * **Technical**
     * **Security**
     * **Legal**
     * **Billing**
  4. Click **Save**.
  5. After assigning contacts to all mandatory categories, click **Next** to open the **Deployment** page.

**Note:** If any mandatory contact category remains unassigned, the **Next** button remains disabled. Assign at least one valid email address to each category to proceed.



### Review deployment details and configure single sign-on

Review the inherited contract settings and configure user authentication for the new instance:

  1. **Review deployment details** : Check the prefilled deployment configuration:

     * **Region** : Displays the geographic residency location. The region is locked to match your parent contract and can't be changed.
     * **Package tier** : Displays your Google SecOps package tier inherited from your subscription.
     * **Data retention duration** : Displays your retention duration inherited from your subscription.

Click **Next**.

  2. **Review service account** : Confirm the details of the service account created by the system for instance operations, and then click **Next**.

  3. **Configure single sign-on (SSO)** : Select the identity provider used to manage user authentication and access controls:

     * **Google Cloud Identity** : Select this option if you use Cloud Identity or Google Workspace. For details, see [Configure a Google Cloud identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication).
     * **Workforce identity federation** : Select this option if you use a third-party identity provider (such as Okta or Microsoft Entra ID). For details, see [Configure a third-party identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

Click **Next**.

  4. **Accept terms of service** : Read the terms of service and select the agreement checkbox.

**Note:** Verify that your chosen identity provider configuration is active before completing setup. Misconfigured workforce identity pools prevent users from signing in after deployment completes.



### Start the instance setup

Start the automated provisioning pipeline to deploy your instance:

  1. Click **Start setup** to initiate the deployment.
  2. The automated provisioning pipeline links the Google Cloud project to your contract, configures data storage, sets up service infrastructure, and activates your instance.
  3. When deployment completes, the new instance appears in the **Instances** table with an **Active** status. After you start setup, it might take between 30 minutes and 1 hour for the new instance to appear in the **Instances** table.

**Note:** If the deployment fails, verify that the Chronicle API is enabled in your target Google Cloud project. If the issue persists, contact your Google representative or reach out to [Google SecOps Support](https://console.cloud.google.com/support).



## Examples and reference information

Use the reference commands and links in this section to prepare your target project using the Google Cloud CLI (`gcloud` CLI) and complete post-deployment tasks.

### Enable the Chronicle API using the Google Cloud CLI

Run the following `gcloud` CLI command to enable the Chronicle API on your target Google Cloud project before starting deployment:
    
    
    gcloud services enable chronicle.googleapis.com \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with the project ID of your dedicated Google Cloud project.

### Grant project-level IAM roles using the Google Cloud CLI

Run the following `gcloud` CLI commands to grant the required project-level roles to the administrator performing the deployment:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ADMIN_EMAIL" \
        --role="roles/chroniclesm.admin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ADMIN_EMAIL" \
        --role="roles/serviceusage.serviceUsageAdmin"
    

Replace `PROJECT_ID` with your dedicated project ID and `ADMIN_EMAIL` with the email address of the administrator.

### Related documentation

After your new instance is deployed, complete the following setup tasks:

  * [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).
  * [Configure data RBAC for users](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users).
  * [Log in to your new instance](https://docs.cloud.google.com/chronicle/docs/onboard/log-in-to-new-instance).



## Troubleshooting

This section outlines performance expectations and provides self-service fixes for common deployment issues.

### Latency and limits

Provisioning an additional Google SecOps instance typically takes between 30 minutes and 1 hour for infrastructure allocation, storage linking, and tenant activation to complete, and for the new instance to appear in the **Instances** table after you trigger provisioning. During provisioning, existing active instances under your contract continue operating with zero downtime or session lockouts. Avoid refreshing the setup page or submitting duplicate setup requests during this period.

### Error remediation

Use the following table to diagnose and resolve issues during instance provisioning:

Issue | Description | Fix  
---|---|---  
**Add instance** button disabled | The **Add instance** button on the **Google SecOps** page is unavailable. | Verify that your contract subscription is active, at least one initial instance is already onboarded, fewer than 25 instances are linked to your billing account and contract, your account has the `roles/billing.user` role, and your subscription isn't compliance-controlled.  
Subscription configuration is invalid or has expired | The setup page displays the warning message _"Subscription configuration is invalid or has expired."_ and disables page interactions. | Verify that your Google SecOps subscription contract is active and hasn't expired or been suspended. If your contract onboarding token (valid for 30 days) has expired, contact your Google representative or [Google SecOps Support](https://console.cloud.google.com/support).  
Project selection warning warning icon | A warning warning icon appears next to a Google Cloud project in the **Select a resource** dialog. | Hold the pointer over the warning warning icon to view the restriction. Verify that the project uses the exact same Cloud Billing account as your subscription contract and isn't linked to another instance.  
**Next** button disabled on **Essential contacts** page | You can't proceed from the **Essential contacts** page to the **Deployment** page. | Assign at least one valid contact email address to each of the mandatory notification categories: **Technical** , **Security** , **Legal** , and **Billing**.  
Deployment setup failure | Provisioning fails after clicking **Start setup**. | Verify that `chronicle.googleapis.com` is enabled in the target Google Cloud project and that your account has the `roles/chroniclesm.admin` and `roles/serviceusage.serviceUsageAdmin` roles.  
  
### Validation and testing

To verify that your additional instance deployed successfully:

  1. In the Google Cloud console, go to the **Google SecOps** page.
  2. In the **Instances** table, confirm that the new instance displays an **Active** status.
  3. Select the target Google Cloud project that hosts the new instance, and then click the instance link to open the Google SecOps web interface and sign in using your configured identity provider.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
