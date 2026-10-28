---
url: https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/
title: Set up multi-project cost view access to Cloud Billing accounts \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:06:53.867019+00:00
---

# Set up multi-project cost view access to Cloud Billing accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/

[ Skip to main content ](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/)
  * [Deutsch](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=es-419)
  * [Français](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=id)
  * [Italiano](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=ja)
  * [한국어](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/developer-tools-color.svg) ](https://docs.cloud.google.com/billing/docs)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Get started](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#get-started)
  * [Permissions required to get multi-project cost view access](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#required-permissions)
    * [Project permissions](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#project-permissions)
    * [Cloud Billing account permissions](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#billing-account-permissions)
  * [Grant permissions](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#grant-permissions)
    * [Project-scoped Cloud Billing account permissions](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#grant-scoped-billing-role)
  * [What's next](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)


Send feedback 
#  Set up multi-project cost view access to Cloud Billing accounts Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Get started](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#get-started)
  * [Permissions required to get multi-project cost view access](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#required-permissions)
    * [Project permissions](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#project-permissions)
    * [Cloud Billing account permissions](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#billing-account-permissions)
  * [Grant permissions](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#grant-permissions)
    * [Project-scoped Cloud Billing account permissions](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#grant-scoped-billing-role)
  * [What's next](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#whats_next)


In Cloud Billing accounts, multi-project access to usage costs lets solution owners see the cost data for all their projects in a single view in the Cloud Billing console. The multi-project view uses a combination of Cloud Billing account permissions and project permissions that let Cloud Billing administrators and organization administrators jointly control access to project-level cost data.
Using project-scoped Cloud Billing account permissions, Cloud Billing administrators can control which solution owners can view aggregated cost data in the Cloud Billing console.
## Get started
  1. Read this document to learn about the permissions required to get multi-project cost view access.
  2. Give project-scoped billing account permissions to solution owners.


## Permissions required to get multi-project cost view access
To get multi-project access to costs views in the Cloud Billing console, which enables project owners, solution owners, developers, and other non-billing admins to view aggregated costs for their authorized projects, you need the following permissions:
  * **Google Cloud project permissions** : To view the costs accrued in a project, you need _billing-specific_ project-side permissions granted on each of your authorized **Google Cloud projects**. Project permissions are typically managed by project owners.
  * **Cloud Billing account permissions** : You need _project-scoped_ billing account permissions on the [**Cloud Billing account** that is linked to your authorized projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked). Cloud Billing permissions are typically managed by a [`Billing Account Administrator`](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-administrator).


### Project permissions
_Project permissions_ are granted with roles on the Google Cloud project or folder. You can grant project permissions using a custom role, or with a [predefined role](https://docs.cloud.google.com/iam/docs/choose-predefined-roles). To view costs for a project, and access other billing tools for the project such as budgets and cost anomalies, you need a role on each project that includes the following permissions:  
| Permissions  | Purpose  | Predefined roles  |  
| --- | --- | --- |  
| 
  * `resourcemanager.projects.get`

 | To browse or retrieve details about a project, including the name and ID of the Cloud Billing account that is linked to the project.  | 
  * [Project Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)
  * [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)
  * [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)

 |  
| 
  * `billing.resourceCosts.get`

 | To view costs for a project in Cloud Billing reports.  | 
  * [Project Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)
  * [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)
  * [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)

 |  
| 
  * `billing.resourcebudgets.read`
  * `billing.resourcebudgets.write`

 | To view and manage budgets for a project in the Cloud Billing console.  | 
  * [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)
  * [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)

 |  
| 
  * `billing.resourcebudgets.configureSpendCap`

 | To configure, edit, and lift _spend cap_ budgets for a project in the Cloud Billing console.  | 
  * [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)
  * [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)

 |  
| 
  * `billing.anomalies.get`
  * `billing.anomalies.list`

 | To view cost anomalies for a project in the Cloud Billing console.  | 
  * [Project Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)
  * [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)
  * [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)

 |  
### Cloud Billing account permissions
_Cloud Billing account permissions_ are granted with roles on the Cloud Billing account. To view the aggregated costs for all of your authorized Google Cloud projects that are linked to a Cloud Billing account, you need a role on the billing account that includes the following [permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.projectCostsManager):  
| Permissions  | Purpose  | Predefined role (recommended)  |  
| --- | --- | --- |  
| `billing.accounts.get`  | View the basic properties and metadata of a Cloud Billing account.  |  [ Project Billing Costs Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.projectCostsManager) `roles/billing.projectCostsManager`  |  
| `billing.accounts.getIamPolicy`  | Lets users view the IAM assignments to a billing account, such as principals who are Billing Account Administrators and Billing Account Viewers.  |  
| `billing.accounts.getSpendingInformationScoped`  | View costs and usage for a billing account, scoped to the projects that the current authenticated user has permission to view.  |  
| `billing.costRecommendations.listScoped`  | Access the FinOps hub in the Cloud Billing console to view cost recommendations scoped to the projects that the current authenticated user has permission to view.  |  
You can grant the billing account permissions using a custom role, or with the project-scoped [predefined billing account role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#ba-project-costs):
  * Name: `billing.projectCostsManager`
  * Title: [Project Billing Costs Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.projectCostsManager)

  
|  For more information about **Google Cloud project** permissions, see:
  * [ Access control for projects with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-proj)
  * [ IAM basic and predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview)

 |  For more information about **Cloud Billing account** permissions, see:
  * [ Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [ Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles)
  * [ Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)

 |  
| --- | --- |  
## Grant permissions
**Project administrators** can [grant the project permissions](https://docs.cloud.google.com/iam/docs/grant-role-console). Many solution owners in your organization might already have the required billing-specific project permissions, because they are the same as those needed to access the single-project view in the Cloud Billing console.
**Billing Account Administrators** can grant the [required billing account permissions](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access/#grant-scoped-billing-role).
After your users are granted _both_ the project-side and the billing account permissions, they can access cost data in the relevant billing account for their projects.
### Project-scoped _Cloud Billing account_ permissions
To provide the required _Cloud Billing account permissions_ for multi-project access to the Cloud Billing console, we recommend you use the predefined billing role `Project Billing Costs Manager`.
To grant multi-project _billing account_ permissions to solution owners, in the Google Cloud console, follow this process:
  1. Ensure that you have the [permissions required to manage user access on a billing account](https://docs.cloud.google.com/billing/docs/how-to/grant-access-to-billing#required-permissions).
  2. In the Google Cloud console, go to the **Account management** page for the Cloud Billing account:
[Go to Account Management in Cloud Billing](https://console.cloud.google.com/billing/manage)
  3. At the prompt, choose the **Cloud Billing account** that you want to manage.
The **Account management** page for that account opens.
You can also open this page by clicking the **Account management** menu item in the billing account navigation menu.
  4. In the **Info** panel, review and edit the **Principals** and **Permissions** for the selected Cloud Billing account. If the panel isn't already visible, click **Show info panel** to open it.
  5. To add new principals and assign permissions, click **Add principal**.
  6. In the **New principals** field, enter the principals you want to add. You can add individual users' email addresses, groups, domains, or service accounts as principals.
  7. In the **Assign roles** section, from the **Select a role** drop-down list, select **Project Billing Costs Manager**.
  8. Click **Save**.


## What's next
Learn more about the [Cloud Billing tools that are available to Google Cloud project owners](https://docs.cloud.google.com/billing/docs/how-to/project-owners/overview).
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
