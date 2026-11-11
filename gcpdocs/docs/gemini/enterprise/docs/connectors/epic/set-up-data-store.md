---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/set-up-data-store/
title: Set up an Epic EHR data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:55:18.925734+00:00
---

# Set up an Epic EHR data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up an Epic EHR data store Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to create a data store and connect Epic EHR to Gemini Enterprise.

## Before you begin

Before you set up your Epic EHR connection, do the following:

  1. Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Locate the user account and click edit **Edit**.
     3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  2. Have your Epic analyst register and configure an Epic app for Gemini Enterprise. For more information, see [Epic EHR configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/epic-configuration).

  3. Get the following values for the Epic environment that you want to connect:

     * FHIR R4 base URL
     * Authorize URL
     * Token URL
     * Client ID and client secret of the Epic app

For more information, see [Find your Epic endpoints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/epic-configuration#find-endpoints).




## Create the Epic EHR data store

To create the Epic EHR data store, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add**Create data store**.

  5. In the **Source** section, search for **Epic EHR** , and click **Select**.

  6. In the **Data** section:

     1. In the **Authentication settings** section, enter the following details. Enter each URL with `https://` and without a trailing slash.

        * **Epic FHIR R4 Audience URI (instance_uri)** : Your FHIR R4 base URL, for example `https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4`.
        * **Epic OAuth 2.0 Authorize URL** : Your authorize URL.
        * **Epic OAuth 2.0 Token URL** : Your token URL.
        * **Epic Connection Hub Client ID** : The client ID of your Epic app.
        * **Epic Connection Hub Client Secret** : The client secret of your Epic app.
     2. Click **Verify Auth** , and complete the Epic sign-in.

     3. Click **Continue**.

     4. In the **Destinations** section, in the **Host** field under **Epic FHIR R4 Base Endpoint URL (host_url)** , enter your FHIR R4 base URL with `https://` and without a trailing slash. Use the same value as **Epic FHIR R4 Audience URI (instance_uri)**.

     5. Click **Continue**.

     6. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

     7. Click **Continue**.

     8. In the **Entities to search** section, select all entities.

  7. Click **Continue**.

  8. In the **Actions** section, keep all actions selected. All Epic EHR actions are read-only.

  9. Click **Continue**.

  10. In the **Configuration** section, do the following:

     1. From the **Multi-region** list, select the location for your data connector.
     2. In the **Your data connector name** field, enter a name for your connector.
     3. If you selected `us` as the location, configure the **Encryption settings** :

        * Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see [Register a single-region key for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).
        * Select **Google-managed encryption key** or **Cloud KMS key**.
        * If you selected **Cloud KMS key** , do the following: 
          * In the **Key management type** list, select the appropriate type.
          * In the **Cloud KMS key** list, select the key.

For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek).

  11. Click **Continue**.

  12. In the **Billing** section, select **General pricing** or **Configurable pricing**. For more information, see [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and [Licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses). 

  13. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data stores** page.




On the **Data stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Epic EHR data store is ready to use.

After creating the data store, connect the data store you just created to an existing app or [create a new app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store) it to the new app, and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Epic EHR before executing any queries. Each user authorizes the connector with their own Epic account on your organization's Epic sign-in page.

## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Epic EHR and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Epic FHIR API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Epic FHIR API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Epic EHR. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Epic FHIR API.

## What's next

  * To provide a user interface for querying your Epic EHR data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Epic EHR data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
