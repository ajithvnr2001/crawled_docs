---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration/
title: Salesforce configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T07:55:27.127429+00:00
---

# Salesforce configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Salesforce configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how a Salesforce administrator installs the [Gemini Enterprise - Salesforce Connector](https://appexchange.salesforce.com/appxListingDetail?listingId=ee18ab11-351b-4178-b6af-3573d35e2d29) managed package from Salesforce AppExchange, and enables the MCP server the connector calls. Both are prerequisites for connecting Salesforce to Gemini Enterprise.

## Why this is required

The Salesforce connector uses Google-managed OAuth. You don't create your own Salesforce connected app and you never enter a client ID or client secret into Gemini Enterprise. Instead, Google publishes a managed package that contains an external client app, and your Salesforce organization authorizes that app.

Because the OAuth flow runs against your organization's My Domain endpoints rather than a shared Salesforce login host, your organization must trust the Gemini Enterprise app before any user can authorize the connector. Installing the managed package is what establishes that trust. If the package isn't installed, the **Authorize** step in Gemini Enterprise fails.

## Before you begin

Before you install the package, make sure of the following:

  * You are signed in to Salesforce as a user with the **Download AppExchange Packages** permission. This permission is included in the **System Administrator** profile. Users without it can't install a package.

  * You know which organization you are connecting. Install the package in the same organization whose My Domain URL you plan to enter as the **Instance URI** when you create the data store.

  * Your organization has My Domain enabled and deployed. The connector authorizes against your My Domain host, for example `https://example.my.salesforce.com`.

  * Your organization uses a supported Salesforce edition. The package supports the **Professional** , **Enterprise** , and **Unlimited** editions.

  * The **SObject All** MCP server is active in your organization. The server isn't active by default. See Enable the MCP server in your organization.


**Note:** Sandbox and production are separate Salesforce organizations. If you plan to connect a sandbox organization, install the package into that sandbox as well as into production. See Install into a sandbox organization.

## Enable the MCP server in your organization

The connector calls the Salesforce-hosted **SObject All** MCP server, which exposes the create, read, update, and delete operations behind the connector's actions. The connector connects only to the **SObject All** MCP server endpoint; separate per-operation MCP servers aren't supported. Activating it is a separate administrator task from installing the managed package, and you must do both.

Because the server is inactive by default, an administrator must activate it in your organization.

To activate it, follow these steps:

  1. In Salesforce, go to **Setup**.

  2. Go to **Integrations > API Catalog > MCP Servers**.

  3. On the **Salesforce Servers** tab, find **SObject All** , described as _Creates, reads, updates, and deletes Salesforce records_.

  4. Set its **Server Status** to **Active**.




Activating the **SObject All** MCP server enables the server for your organization without requiring a separate MCP server user permission, and it doesn't grant users permission to create, update, or delete records on its own. Write and delete access is controlled at two layers:

  * **In Gemini Enterprise** : Read-only actions are enabled by default, and actions that create, update, or delete records are turned off by default. When setting up or managing the data store, the Google Cloud administrator chooses which create, update, or delete actions to enable—or leaves them all disabled so that the connector is read-only. See [Enable actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store#enable-actions).
  * **In Salesforce** : Every action runs under the authorizing user's own Salesforce account and respects that user's object-level permissions, field-level security, and sharing rules.



## Install the package

To install the managed package, follow these steps:

  1. Sign in to your Salesforce organization as an administrator.

  2. Go to the [Gemini Enterprise - Salesforce Connector](https://appexchange.salesforce.com/appxListingDetail?listingId=ee18ab11-351b-4178-b6af-3573d35e2d29) listing on Salesforce AppExchange.

  3. Click **Get It Now**.

  4. Choose the environment to install into:

     * **Install in Production** for your production organization.
     * **Install in Sandbox** for a sandbox organization.
  5. Choose which users get access to the app:

     * **Install for Admins Only** : only users with the System Administrator profile can use the app.
     * **Install for Specific Profiles** : only users with the profiles you select can use the app.
     * **Install for All Users** (recommended): every user in the organization can use the app without additional profile configuration.

The managed package already includes the required OAuth scopes (`mcp_api` and `refresh_token`). Every user who signs in to authorize the connector in Gemini Enterprise must have access to the app under the option you choose. A user whose profile doesn't have access can't complete the sign-in step.

  6. Approve third-party access if Salesforce prompts you to, then click **Install** or **Upgrade**.

  7. Wait for the installation to finish. For a large organization, Salesforce might complete the installation asynchronously and email you when it's done.




After installation, the app appears in Salesforce **Setup** as **Gemini Enterprise**.

## Set the login IP policy for the app

Per-data-store static IP addresses aren't supported for the Salesforce connector. Instead, IP validation is handled through the Google-managed AppExchange app:

  * **Authentication calls (OAuth token exchange and refresh)** : When a user authorizes the connector, Gemini Enterprise exchanges and refreshes that user's Salesforce tokens from Google's servers. Those requests don't come from your organization's IP addresses. If the app enforces IP restrictions and your users' profiles have login IP ranges, the requests are rejected and the **Authorize** step fails. Set the app's **IP Relaxation** policy to **Relax IP restrictions** : the Google-managed Gemini Enterprise app already restricts token requests to Google's own egress IP ranges, and that check applies regardless of the policy setting.
  * **Data calls** : Only sign-in and token requests are checked against IP restrictions. After a user authorizes the connector, Salesforce serves the connector's data requests based on the user's valid access token.



To set the policy:

  1. In Salesforce, go to **Setup**.

  2. Go to **Apps > External Client App Manager**, and click **Gemini Enterprise**.

  3. Select the **Policies** tab, and click **Edit**.

  4. In the **OAuth Policies** section, set **IP Relaxation** to **Relax IP restrictions**.

  5. Click **Save**.




## Install into a sandbox organization

A sandbox is a separate Salesforce organization with its own My Domain host and its own installed packages. Installing the package in production does not install it in your sandbox.

To connect a sandbox organization, install the package again from the sandbox, choosing **Install in Sandbox**. For the data store settings that a sandbox connection requires, see [Set up a Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store).

## What happens after you install

Installing the package doesn't connect anything on its own. It makes the Gemini Enterprise app available to your organization so that individual users can authorize it.

After a Google Cloud administrator creates the Salesforce data store in Gemini Enterprise and connects it to an app (see [Set up a Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store)), each end user (including administrators who use the web app) authorizes Gemini Enterprise to access Salesforce on their behalf using per-user End-User Authentication. When a user first queries Salesforce data in the Gemini Enterprise web app, they are redirected to your organization's Salesforce sign-in page, where they grant the Gemini Enterprise app the `mcp_api` and `refresh_token` scopes. For more information, see [Authorize the connector](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization).

Because each user authorizes individually, Gemini Enterprise accesses Salesforce records with that user's own permissions. A user only sees and modifies records they can already see and modify in Salesforce.

## Troubleshoot

Symptom | Likely cause  
---|---  
The **Authorize** step fails, or the Salesforce sign-in page reports an unknown or unauthorized client application. | The managed package isn't installed in the organization that the **Instance URI** points to. Verify that you installed the package in that exact organization, including when the organization is a sandbox.  
Some users can authorize and others can't. | The package was installed for admins only, or for a set of profiles that doesn't include those users. To grant access without reinstalling the package, go to **Setup > Apps > External Client App Manager**, click **Gemini Enterprise** , select the **Policies** tab, click **Edit** , and add the affected profiles or permission sets (or set **Permitted Users** to **All users may self-authorize**).  
Authorization succeeds, but queries or actions fail in the Gemini Enterprise web app. | The **SObject All** MCP server isn't active in the organization. Activate the server in Salesforce Setup. See Enable the MCP server in your organization.  
Authorization succeeds but no Salesforce data is returned. | The authorizing user might not have record-level access in Salesforce. The connector honors the user's own Salesforce permissions.  
  
## What's next

  * To create the data store, see [Set up a Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
