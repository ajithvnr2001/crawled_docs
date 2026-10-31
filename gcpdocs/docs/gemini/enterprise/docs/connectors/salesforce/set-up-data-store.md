---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store/
title: Set up a Salesforce data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:51:23.886648+00:00
---

# Set up a Salesforce data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Salesforce data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Salesforce to Gemini Enterprise. The data store searches your Salesforce records in real time and lets end users act on them using natural language.

## Before you begin

Before you set up your Salesforce connection, do the following:

  1. Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Locate the user account and click edit **Edit**.
     3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  2. Have your Salesforce administrator enable the **SObject All** MCP server in the Salesforce organization you're connecting, and configure your chosen authentication method:

     * **OAuth 2.0 (Google Managed)** (default): Install the [Gemini Enterprise - Salesforce Connector](https://appexchange.salesforce.com/appxListingDetail?listingId=ee18ab11-351b-4178-b6af-3573d35e2d29) managed package from Salesforce AppExchange into that organization. You don't need a client ID or client secret.
     * **OAuth 2.0 (Bring Your Own App)** : Create an external client app in that organization and obtain its consumer key (**Client ID**) and consumer secret (**Client Secret**).

Until the OAuth app is configured, users can't authorize the connector; until the **SObject All** MCP server is active, no actions are available. See [Salesforce configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration).

  3. Note your organization's My Domain URL, for example `https://example.my.salesforce.com`. You enter this as the **Instance URI**. For a sandbox organization, use the sandbox My Domain, for example `https://example--sandbox.sandbox.my.salesforce.com`.




### Find your My Domain URL

To find the My Domain URL to enter as the **Instance URI** :

  1. In Salesforce, go to **Setup**.
  2. In the **Quick Find** box, search for and select **My Domain**.
  3. Under **Current My Domain URL** , copy the URL, for example `https://example.my.salesforce.com`.



For a sandbox organization, do this in the sandbox. Its My Domain URL looks like `https://example--sandbox.sandbox.my.salesforce.com`.

## Create the Salesforce data store

To create the Salesforce data store, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add**Create data store**.

  5. In the **Source** section, search for **Salesforce** , and click **Select**.

  6. In the **Data** section:

     1. Under **Authentication settings** , for **Select your authentication method** , choose one of the following options:

        * **OAuth 2.0 (Google Managed)** (default): 
          1. For **Instance URI** , enter the My Domain URL of your Salesforce site, for example `https://example.my.salesforce.com`. For a sandbox organization, enter your sandbox My Domain, for example `https://example--sandbox.sandbox.my.salesforce.com`.
        * **OAuth 2.0 (Bring Your Own App)** : 
          1. For **Instance URI** , enter the My Domain URL of your Salesforce site, for example `https://example.my.salesforce.com`. For a sandbox organization, enter your sandbox My Domain, for example `https://example--sandbox.sandbox.my.salesforce.com`.
          2. For **Client ID** , enter the consumer key of your Salesforce external client app.
          3. For **Client Secret** , enter the consumer secret of your Salesforce external client app.
          4. Click **Verify Auth** and complete the Salesforce sign-in to verify your OAuth credentials.
     2. Under **Advanced options** , if you're connecting a sandbox organization, select **Use Sandbox**. Salesforce then serves actions from your sandbox organization.

     3. Click **Continue**.

     4. In the **Entities to search** section, select the entities that you want Gemini Enterprise to search. For Salesforce, select **Salesforce MCP**.

  7. Click **Continue**.

  8. Optional: In the **Actions** section, select the create, update, and delete actions that you want to enable for your users, or leave them unselected to keep the connector read-only (read-only actions are enabled by default). You can also enable or disable these actions after creating the data store; see Enable actions.

  9. Click **Continue**.

  10. In the **Configuration** section: 

     1. From the **Multi-region** list, select the location for your data connector.
     2. In the **Your data connector name** field, enter a name for your connector.
     3. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 
        * Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see [Register a single-region key for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).
        * Select **Google-managed encryption key** or **Cloud KMS key**.
        * If you selected **Cloud KMS key** : 
          * In the **Key management type** list, select the appropriate type.
          * In the **Cloud KMS key** list, select the key.
For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek). 
  11. Click **Continue**.

  12. In the **Billing** section, select **General pricing** or **Configurable pricing**. For more information, see [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and [Licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses). 

  13. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page.




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Salesforce data store is ready to be used.

After creating the data store, connect the data store you just created to an existing app or [create a new app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store) it to the new app, and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Salesforce before executing any queries.

**Note:** The **Authorize** step sends each user to your organization's Salesforce sign-in page to grant the OAuth app the `mcp_api` and `refresh_token` scopes. This step fails if the Gemini Enterprise managed package (for **OAuth 2.0 (Google Managed)**) or your custom OAuth app (for **OAuth 2.0 (Bring Your Own App)**) isn't configured in that organization, or if the user's profile doesn't have access to the app. Per-data-store static IP configuration isn't supported; login IP policy for authentication and token refresh calls is configured on the app in Salesforce, and data calls are authorized using the user's valid access token. See [Set the login IP policy for the app](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration#ip-policy).

## Enable actions

When you create a Salesforce data store, its actions are pre-populated in the data store. Read-only actions (**Soql Query** , **Find** , **Get Object Schema** , **Get Related Records** , **List Recent Sobject Records** , and **Get User Info**) are enabled by default and always available. Actions that create, update, or delete records (**Create Sobject Record** , **Update Sobject Record** , **Update Related Record** , **Delete Sobject Record** , and **Delete Related Record**) are turned off by default.

If you didn't enable create, update, or delete actions during data store creation, you can enable them at any time by following these steps:

  1. In the Google Cloud console, go to your Salesforce data store.

  2. Select the **Actions** tab.

  3. Select the actions that you want to enable (**Create Sobject Record** , **Update Sobject Record** , **Update Related Record** , **Delete Sobject Record** , or **Delete Related Record**). To keep the connector read-only, leave these actions unselected.

  4. Click **Enable actions**.




For the list of actions, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce#supported-actions).

## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Salesforce and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Salesforce MCP server.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Salesforce MCP server).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Salesforce. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Salesforce MCP server.

## What's next

  * To provide a user interface for querying your Salesforce data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
