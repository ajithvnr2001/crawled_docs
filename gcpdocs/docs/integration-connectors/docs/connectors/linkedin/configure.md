---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/
title: LinkedIn \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:54:15.778741+00:00
---

# LinkedIn  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/

[ Skip to main content ](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/)
  * [Deutsch](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=de)
  * [Español](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=es-419)
  * [Français](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=id)
  * [Italiano](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=it)
  * [Português](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=ja)
  * [한국어](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fintegration-connectors%2Fdocs%2Fconnectors%2Flinkedin%2Fconfigure%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#before-you-begin)
  * [Configure the connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#configure-the-connector)
  * [System limitations](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#system-limitations)
  * [Use the LinkedIn connection in an integration](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#use-the-linkedin-connection-in-an-integration)
  * [Entities](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#entities)
  * [Entity operation examples](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#entityexamples-exp)
    * [Example - List all the Comments from the LinkedIn profile page.](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#example---list-all-the-comments-from-the-linkedin-profile-page.)
    * [Example - Get Profiles from a specific ID](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#example---get-profiles-from-a-specific-id)
  * [Get help from the Google Cloud community](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#get-help-from-the-google-cloud-community)
  * [What's next](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)


Was this helpful?
Send feedback 
  * On this page
  * [Before you begin](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#before-you-begin)
  * [Configure the connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#configure-the-connector)
  * [System limitations](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#system-limitations)
  * [Use the LinkedIn connection in an integration](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#use-the-linkedin-connection-in-an-integration)
  * [Entities](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#entities)
  * [Entity operation examples](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#entityexamples-exp)
    * [Example - List all the Comments from the LinkedIn profile page.](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#example---list-all-the-comments-from-the-linkedin-profile-page.)
    * [Example - Get Profiles from a specific ID](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#example---get-profiles-from-a-specific-id)
  * [Get help from the Google Cloud community](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#get-help-from-the-google-cloud-community)
  * [What's next](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#whats-next)


# LinkedIn Stay organized with collections  Save and categorize content based on your preferences.
The LinkedIn connector lets you perform read operations on LinkedIn data.
## Before you begin
In your Google Cloud project, do the following tasks:
  * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private).
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant the `roles/secretmanager.viewer` and `roles/secretmanager.secretAccessor` IAM roles to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector. 
  * Enable the following services: 
    * `secretmanager.googleapis.com` (Secret Manager API)
    * `connectors.googleapis.com` (Connectors API)
To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). If these services or permissions have not been enabled for your project previously, you are prompted to enable them when you configure the connector.


## Configure the connector
A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:
  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 
[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)
  2. Click **+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
    1. **Region** : Select a location from the drop-down list. 
For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).
    2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
    1. **Connector** : Select **LinkedIn** from the drop down list of available Connectors.
    2. **Connector version** : Select the Connector version from the drop down list of available versions. 
    3. In the **Connection Name** field, enter a name for the Connection instance. 
Connection names must meet the following criteria: 
       * Connection names can use letters, numbers, or hyphens.
       * Letters must be lower-case.
       * Connection names must begin with a letter and end with a letter or number.
       * Connection names cannot exceed 49 characters.
    4. Optionally, enter a **Description** for the connection instance.
    5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
    6. **Service Account** : Select a service account that has the [required roles](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#before-you-begin).
    7. Optionally, configure the **Connection node settings** : 
       * **Minimum number of nodes** : Enter the minimum number of connection nodes.
       * **Maximum number of nodes** : Enter the maximum number of connection nodes.
A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.
    8. **Company Id** : The LinkedIn company ID that is unique to your organization. If you specify the Company ID in the query, use the following format: `urn:li:organization:COMPANY_ID`.
    9. Click **NEXT**.
    10. In the **Authorization** section, enter details of the client ID and client secret. 
       * **Client ID** : The client ID used for requesting access tokens. 
       * **Scope** : A comma-separated list of desired scopes from the LinkedIn developer account. 
       * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created. 
       * **Secret version** : Secret version for the secret selected. 
    11. Click **NEXT**. 
    12. **Review** : Review your connection and authentication details.
    13. Click **Create**.
## System limitations
The LinkedIn connector can process a maximum of 5 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit LinkedIn enforces a limit of 10k requests per user every 24 hours. 
By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 
For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).
## Use the LinkedIn connection in an integration
After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.
     * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
     * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).
Entities
The LinkedIn connector supports entities, such as Comments and Profiles. To understand how to configure the entities, see [Entity examples](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure/#entityexamples-exp).
Entity operation examples
### Example - List all the Comments from the LinkedIn profile page.
This example lists all the Comments from the Posts in the Organization Pages that you administer
    1. In the `Configure connector task` dialog, click `Entities`.
    2. Select Comments from the `Entity` list.
    3. Select the `LIST` operation, and then click **Done**.
### Example - Get Profiles from a specific ID
This example gets the profiles based on the ID from the `Profiles` entity.
    1. In the `Configure connector task` dialog, click `Entities`.
    2. Select `Profiles` from the `Entity` list.
    3. Select the `GET` operation, and then click **Done**.
    4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `2t7k5s4fgC` in the **Default Value** field. 
Here, `Id [KEY]` is the primary key value of the `Profiles` entity.
    5. Click **Done**.
## Get help from the Google Cloud community
You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 
## What's next
     * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
     * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
     * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
