---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/
title: Set up a Miro data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:53:23.708472+00:00
---

# Set up a Miro data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/

[ Skip to main content ](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/)
  * [Deutsch](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/?hl=ko)


[ ![](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/gemini-spark-blue-192px.svg) ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#prereqs)
  * [Create the Miro data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#create-data-store)
  * [Data handling and query execution](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#data-handling-and-query-execution)
    * [Query execution](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#query-execution)
    * [Data handling](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#data-handling)
  * [What's next](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#whats-next)


**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)


Send feedback 
#  Set up a Miro data store Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#prereqs)
  * [Create the Miro data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#create-data-store)
  * [Data handling and query execution](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#data-handling-and-query-execution)
    * [Query execution](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#query-execution)
    * [Data handling](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#data-handling)
  * [What's next](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro/set-up-data-store/#whats-next)


This page describes how to create a data store and connect Miro to Gemini Enterprise.
## Before you begin
Before you set up your Miro connection, do the following:
  1. Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 
    1. In the Google Cloud console, go to the **IAM** page. 
[Go to IAM](https://console.cloud.google.com/iam-admin/iam)
    2. Locate the user account and click edit **Edit**.
    3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).


## Create the Miro data store
To create the Miro data store, perform the following steps:
  1. In the Google Cloud console, go to the Gemini Enterprise page.
[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)
  2. Select or [create](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.
  3. In the navigation menu, click **Data stores**.
  4. Click add**Create data store**.
  5. In the **Source** section, search for **Miro** , and click **Select**.
  6. In the **Data** section:
    1. In the **Entities to search** section, select **Diagram** , **Table** , and **Doc**.
  7. Click **Continue**.
  8. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress). 
  9. In the **Configuration** section: 
    1. From the **Multi-region** list, select the location for your data connector.
    2. In the **Your data connector name** field, enter a name for your connector.
    3. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 
       * Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see [Register a single-region key for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).
       * Select **Google-managed encryption key** or **Cloud KMS key**.
       * If you selected **Cloud KMS key** : 
         * In the **Key management type** list, select the appropriate type.
         * In the **Cloud KMS key** list, select the key.
For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek). 
  10. Click **Continue**.
  11. In the **Billing** section, select **General pricing** or **Configurable pricing**. For more information, see [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and [Licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses). 
  12. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page.


On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Miro data store is ready to be used.
After creating the data store, connect the data store you just created to an existing app or [create a new app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store) it to the new app, and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Miro before executing any queries.
## Data handling and query execution
This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.
### Query execution
After you authorize Miro and send a search query to Gemini Enterprise:
  * Gemini Enterprise sends your search query directly to the Miro API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.


### Data handling
When using third-party federated search, the following data handling rules apply:
  * Your query string is sent to the third-party search backend (Miro API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.


## What's next
  * To provide a user interface for querying your Miro data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Miro data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
