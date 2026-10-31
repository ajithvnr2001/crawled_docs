---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration/
title: Salesforce configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:50:30.759523+00:00
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

This page describes how a Salesforce administrator enables the MCP server that the Salesforce connector calls, and configures OAuth 2.0 authentication in Salesforce. Both are prerequisites for connecting Salesforce to Gemini Enterprise.

## Choose an authentication method

Because the OAuth 2.0 flow runs against your organization's My Domain endpoints rather than a shared Salesforce login host, your Salesforce organization must trust an OAuth client app before any user can authorize the connector. You can configure authentication in one of two ways:

  * **Google-managed OAuth** (**OAuth 2.0 (Google Managed)** , default): Google publishes the [Gemini Enterprise - Salesforce Connector](https://appexchange.salesforce.com/appxListingDetail?listingId=ee18ab11-351b-4178-b6af-3573d35e2d29) managed package on Salesforce AppExchange. When you install the package in your Salesforce organization, you don't create your own Salesforce app or enter a client ID or client secret into Gemini Enterprise. See Install the Google-managed package.
  * **Bring your own app** (**OAuth 2.0 (Bring Your Own App)**): If your organization can't install AppExchange packages or wants to manage its own OAuth application and security policies directly, you can create your own external client app in Salesforce and enter its client ID (consumer key) and client secret (consumer secret) in Gemini Enterprise. See Create your own OAuth app.



## Before you begin

Before you configure Salesforce, make sure of the following:

  * You're signed in to Salesforce as an administrator:

    * To install the Google-managed package, your user profile must include the **Download AppExchange Packages** permission (included in the **System Administrator** profile).
    * To bring your own app, your user profile must have permission to create and manage external client apps in Salesforce **Setup**.
  * You know which organization you're connecting. Complete the setup in the same organization whose My Domain URL you plan to enter as the **Instance URI** when you create the data store.

  * Your organization has My Domain enabled and deployed. The connector authorizes against your My Domain host, for example `https://example.my.salesforce.com`.

  * Your organization uses a supported Salesforce edition. The connector supports the **Professional** , **Enterprise** , **Unlimited** , and **Developer** editions.

  * The **SObject All** MCP server is active in your organization. The server isn't active by default. See Enable the MCP server in your organization.


**Note:** Sandbox and production are separate Salesforce organizations. If you plan to connect a sandbox organization, complete the configuration in that sandbox as well as in production. See Connect a sandbox organization.

## Enable the MCP server in your organization

The connector calls the Salesforce-hosted **SObject All** MCP server, which exposes the create, read, update, and delete operations behind the connector's actions. The connector connects only to the **SObject All** MCP server endpoint; separate per-operation MCP servers aren't supported. Activating it is required for both **OAuth 2.0 (Google Managed)** and **OAuth 2.0 (Bring Your Own App)**.

Because the server is inactive by default, an administrator must activate it in your organization.

To activate it, follow these steps:

  1. In Salesforce, go to **Setup**.

  2. Go to **Integrations > API Catalog > MCP Servers**.

  3. On the **Salesforce Servers** tab, find **SObject All** , described as _Creates, reads, updates, and deletes Salesforce records_.

  4. Set its **Server Status** to **Active**.




Activating the **SObject All** MCP server enables the server for your organization without requiring a separate MCP server user permission, and it doesn't grant users permission to create, update, or delete records on its own. Write and delete access is controlled at two layers:

  * **In Gemini Enterprise** : Read-only actions are enabled by default, and actions that create, update, or delete records are turned off by default. When setting up or managing the data store, the Google Cloud administrator chooses which create, update, or delete actions to enable—or leaves them all disabled so that the connector is read-only. See [Enable actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store#enable-actions).
  * **In Salesforce** : Every action runs under the authorizing user's own Salesforce account and respects that user's object-level permissions, field-level security, and sharing rules.



## Install the Google-managed package

If you plan to use **OAuth 2.0 (Google Managed)** , install the Gemini Enterprise managed package from Salesforce AppExchange:

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




After installation, the app appears in Salesforce **Setup** as **Gemini Enterprise**. Next, set the login IP policy for the app.

## Create your own OAuth app

If you plan to use **OAuth 2.0 (Bring Your Own App)** , create and configure an external client app in Salesforce to obtain a consumer key (**Client ID**) and consumer secret (**Client Secret**):

  1. Sign in to your Salesforce organization as an administrator and go to **Setup**.

  2. In the **Quick Find** field, enter `External Client App Manager` and select **External Client App Manager**.

  3. Click **New External Client App** , and under **Basic Information** , enter the required information (**External Client App Name** , **API Name** , and **Contact Email**).

  4. In the **API (Enable OAuth Settings)** section, select **Enable OAuth** and configure the following settings:

     1. Under **App Settings** , for **Callback URL** , enter:
            
            https://vertexaisearch.cloud.google.com/oauth-redirect
            

     2. For **OAuth Scopes** , add both of the following scopes:

        * **Access the Salesforce API Platform MCP servers (mcp_api)**
        * **Perform requests at any time (refresh_token, offline_access)**

These grant the `mcp_api` and `refresh_token` scopes required by the connector.

     3. Under **Security** , make sure the following options are selected:

        * **Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows**
        * **Issue JSON Web Token (JWT)-based access tokens for named users**
  5. Click **Create**.

  6. Configure the app's OAuth policies:

     1. In **Setup** , go to **Apps > External Client App Manager**, click your external client app, select the **Policies** tab, and click **Edit**.

     2. For **Permitted Users** , select **All users may self-authorize** (recommended), or select **Admin approved users are pre-authorized** and assign the profiles or permission sets for all users who will authorize the connector (including the administrator who verifies authentication during data store creation).

     3. For **IP Relaxation** , select **Relax IP restrictions**. For details on why this setting is required, see Set the login IP policy for the app.

     4. Click **Save**.

  7. Copy the app's OAuth credentials:

     1. Select the **Settings** tab, expand **OAuth Settings** , and click **Consumer Key and Secret**.
     2. Copy and save the **Consumer Key** and **Consumer Secret**. You enter these values as the **Client ID** and **Client Secret** when you create the data store in Gemini Enterprise.



## Set the login IP policy for the app

Per-data-store static IP addresses aren't supported for the Salesforce connector. Instead, the external client app in Salesforce governs login IP validation:

  * **Authentication calls (OAuth token exchange and refresh)** : When a user authorizes the connector, Gemini Enterprise exchanges and refreshes that user's Salesforce tokens from Google's servers. Those requests don't come from your organization's IP addresses. If the app enforces IP restrictions and your users' profiles have login IP ranges, the requests are rejected and the **Verify Auth** or **Authorize** step fails. Set the app's **IP Relaxation** policy to **Relax IP restrictions**. For the Google-managed **Gemini Enterprise** app, Google already restricts token requests to Google's own egress IP ranges, and that check applies regardless of the policy setting.
  * **Data calls** : Only sign-in and token requests are checked against IP restrictions. After a user authorizes the connector, Salesforce serves the connector's data requests based on the user's valid access token.



To set the policy for the Google-managed app (or your own external client app):

  1. In Salesforce, go to **Setup**.

  2. Go to **Apps > External Client App Manager**, and click **Gemini Enterprise** (or the name of your custom external client app).

  3. Select the **Policies** tab, and click **Edit**.

  4. In the **OAuth Policies** section, set **IP Relaxation** to **Relax IP restrictions**.

  5. Click **Save**.




## Connect a sandbox organization

A sandbox is a separate Salesforce organization with its own My Domain host and its own installed packages and apps. Configuring production doesn't configure your sandbox.

To connect a sandbox organization, activate the **SObject All** MCP server in the sandbox, and then either install the AppExchange package into the sandbox (choosing **Install in Sandbox**) or create your external client app in the sandbox. For the data store settings that a sandbox connection requires, see [Set up a Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store).

## What happens after you configure Salesforce

Configuring the app in Salesforce doesn't connect anything on its own. It makes the OAuth app available to your organization so that individual users can authorize it.

After a Google Cloud administrator creates the Salesforce data store in Gemini Enterprise and connects it to an app (see [Set up a Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store)), each end user (including administrators who use the web app) authorizes Gemini Enterprise to access Salesforce on their behalf using per-user End-User Authentication. When a user first queries Salesforce data in the Gemini Enterprise web app, they are redirected to your organization's Salesforce sign-in page, where they grant the app the `mcp_api` and `refresh_token` scopes. For more information, see [Authorize the connector](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization).

Because each user authorizes individually, Gemini Enterprise accesses Salesforce records with that user's own permissions. A user only sees and modifies records they can already see and modify in Salesforce.

## Troubleshoot

Symptom | Likely cause  
---|---  
The **Verify Auth** or **Authorize** step fails, or the Salesforce sign-in page reports an unknown, invalid, or unauthorized client application. | If you use **OAuth 2.0 (Google Managed)** , verify that the managed package is installed in the exact organization (including a sandbox) that the **Instance URI** points to. If you use **OAuth 2.0 (Bring Your Own App)** , verify that the **Client ID** and **Client Secret** match the app in that organization, the callback URL is set to `https://vertexaisearch.cloud.google.com/oauth-redirect`, the `mcp_api` and `refresh_token` scopes are selected, and **Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows** is enabled.  
Some users can authorize and others can't. | The app's **Permitted Users** policy restricts access to specific profiles or permission sets that don't include those users, or **IP Relaxation** isn't set to **Relax IP restrictions**. In **Setup** , open the app's **Policies** tab, click **Edit** , add the affected profiles or permission sets (or set **Permitted Users** to **All users may self-authorize**), and verify that **IP Relaxation** is set to **Relax IP restrictions**.  
Authorization succeeds, but queries or actions fail in the Gemini Enterprise web app. | The **SObject All** MCP server isn't active in the organization, or **Issue JSON Web Token (JWT)-based access tokens for named users** isn't selected on your external client app. Activate the server in Salesforce Setup (see Enable the MCP server in your organization) and verify that your external client app issues JWT-based access tokens.  
Authorization succeeds but no Salesforce data is returned. | The authorizing user might not have record-level access in Salesforce. The connector honors the user's own Salesforce permissions.  
  
## What's next

  * To create the data store, see [Set up a Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
