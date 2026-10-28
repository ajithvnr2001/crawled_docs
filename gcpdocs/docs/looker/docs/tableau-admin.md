---
url: https://docs.cloud.google.com/looker/docs/tableau-admin/
title: Administering Tableau to Looker connections \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:55.713958+00:00
---

# Administering Tableau to Looker connections  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/tableau-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Administering Tableau to Looker connections Stay organized with collections  Save and categorize content based on your preferences. 

The Looker–Tableau BI Connector lets you use a Looker Explore as a data source in Tableau Desktop, Tableau Cloud, and Tableau Server. The Looker–Tableau BI Connector is built upon the Looker [Open SQL Interface](https://docs.cloud.google.com/looker/docs/sql-interface), which allows access to LookML models and Explores for applications that use Java Database Connectivity (JDBC) to connect to data sources.

See the following sections for information on the administration steps required for connecting to Looker from these Tableau products:

  * Tableau Desktop
  * Tableau Cloud
  * Tableau Server



## Tableau Desktop

To set up your Looker instance as a data source for [Tableau Desktop](https://docs.cloud.google.com/looker/docs/tableau-connector#desktop), a Looker admin can enable the pre-configured **Tableau Desktop** client from the **Application Library** tab on the [**Manage OAuth Clients**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-oauth-clients#application-library) page (**Admin > Authentication > Manage OAuth clients**), or enable the [**Tableau Desktop**](https://docs.cloud.google.com/looker/docs/bi-connectors#tableau_desktop) switch on the Looker [**BI Connectors**](https://docs.cloud.google.com/looker/docs/bi-connectors) page.

In addition, for [Looker (Google Cloud core) instances that are configured for private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) and [customer-hosted Looker instances](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps), your instance must meet the following requirements:

  * The instance must be running Looker 25.16 or later.
  * Your network administrator must configure your network so that traffic from Tableau Desktop can reach your Looker instance.



## Tableau Cloud

To set up your Looker instance as a data source for [Tableau Cloud](https://docs.cloud.google.com/looker/docs/tableau-connector#cloud), the following tasks are required:

  * A Looker admin must set up OAuth for Tableau Cloud.
  * A Tableau admin must register the OAuth client ID on Tableau Cloud.
  * A Tableau user with [permissions to add data sources](https://help.tableau.com/current/online/en-us/permission_license_siterole.htm) must add **Looker by Google** as a data source.
  * For [Looker (Google Cloud core) instances that are configured for private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) and [customer-hosted Looker instances](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps), a network administrator must configure your network so that traffic from the Looker–Tableau BI Connector can reach your Looker instance.



### Set up OAuth for Tableau Cloud

To use the Looker–Tableau BI Connector for Tableau Cloud, a Looker admin must register a custom OAuth client application on your Looker instance.

You can register the client on the [**Manage OAuth Clients**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-oauth-clients) page in the Looker **Admin** panel (**Admin > Authentication > Manage OAuth clients**). On the **Custom Clients** tab, click **Add New** and enter the following information:

  * **Client ID** : Enter a unique client ID for the application (suggested value: `tableau-cloud`). Custom client IDs cannot start with `com.looker.`.
  * **Client Name** : Enter a descriptive name (for example, `Looker-Tableau-Cloud`).
  * **Description** : Enter a description (for example, `Client for Looker-Tableau Cloud integration`).
  * **Redirect URIs** : Enter `TABLEAU_CLOUD_URL/auth/add_oauth_token`, replacing `TABLEAU_CLOUD_URL` with your Tableau Cloud site URL.
  * **Restrict to Group ID** (Optional): Enter a numeric group ID if you want to restrict access to members of a specific Looker user group.



For step-by-step instructions on registering custom OAuth clients, see the [Admin settings - Manage OAuth Clients](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-oauth-clients#custom-clients) documentation page.

**Important:** After the client has been registered, you must enable the client's switch on the Looker **Manage OAuth Clients** page.

Alternatively, administrators can register the OAuth client programmatically by calling the ['register_oauth_client_app'](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/register_oauth_client_app) API endpoint directly or by using the [Looker API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) under the **Auth** method.

### Register the OAuth client ID on Tableau Cloud

After you set up OAuth for Tableau Cloud on your Looker instance, you need to register the custom OAuth client on Tableau Cloud by following these steps:

  1. Sign in to Tableau Cloud using your admin credentials, and then navigate to the **Settings** page.
  2. In the **General** tab of the **Settings** page, scroll to **OAuth Clients Registry** and click **Add OAuth Client**.
  3. In the **Create OAuth Client** dialog, enter the following information:

     * **Connection Type** : Select **Looker by Google** from the drop-down menu.
     * **OAuth Provider** : Select **Default IDP** from the drop-down menu.
     * **OAuth instance URL** : Enter your Looker instance URL with the `https://`. For example: `https://example.cloud.looker.com`:
           
           https://LOOKER_INSTANCE_URL
           

     * **Client ID** : Enter the **client_guid** value that you used when you set up OAuth for Tableau Cloud on your Looker instance:
           
           client_guid
           

     * **Client Secret** : Leave this field blank.

     * **Redirect URL** : Enter the **redirect_uri** value that you used when you set up OAuth for Tableau Cloud on your Looker instance:
           
           TABLEAU_CLOUD_URL/auth/add_oauth_token
           

  4. Click the **Add OAuth Client** button to register the OAuth client ID and return to the **Settings** page.

  5. Click the **Save** button at the bottom or top of the **Settings** page to save your changes.




### Add **Looker by Google** as a data source

A Tableau Cloud user who has a [Tableau role](https://help.tableau.com/current/online/en-us/permission_license_siterole.htm) that allows for creating data sources must add **Looker by Google** as a data source on your Tableau Cloud instance. If **Looker by Google** isn't added as a data source, it won't be visible or available to users who lack permission to add new data sources.

See the [Connecting to Looker data from Tableau Cloud](https://docs.cloud.google.com/looker/docs/tableau-connector#connecting-cloud) section in the Looker documentation for the procedure on adding Looker as a data source in Tableau Cloud.

## Tableau Server

To use Looker data for [Tableau Server](https://docs.cloud.google.com/looker/docs/tableau-connector#server), the following tasks are required:

  * A Looker admin must set up OAuth for Tableau Server.
  * A Tableau admin must install the Looker–Tableau BI Connector on Tableau Server
  * A Tableau admin must register the OAuth client ID on Tableau Server.
  * For [Looker (Google Cloud core) instances that are configured for private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) and [customer-hosted Looker instances](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps), a network administrator must configure your network so that traffic from the Looker–Tableau BI Connector can reach your Looker instance.



### Set up OAuth for Tableau Server

To use the Looker–Tableau BI Connector for Tableau Server, a Looker admin must register a custom OAuth client application on your Looker instance.

You can register the client on the [**Manage OAuth Clients**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-oauth-clients) page in the Looker **Admin** panel (**Admin > Authentication > Manage OAuth clients**). On the **Custom Clients** tab, click **Add New** and enter the following information:

  * **Client ID** : Enter a unique client ID for the application (suggested value: `tableau-server`). Custom client IDs cannot start with `com.looker.`.
  * **Client Name** : Enter a descriptive name (for example, `Looker-Tableau-Server`).
  * **Description** : Enter a description (for example, `Client for Looker-Tableau Server integration`).
  * **Redirect URIs** : Enter `TABLEAU_SERVER_URL/auth/add_oauth_token`, replacing `TABLEAU_SERVER_URL` with your Tableau Server URL.
  * **Restrict to Group ID** (Optional): Enter a numeric group ID if you want to restrict access to members of a specific Looker user group.



For step-by-step instructions on registering custom OAuth clients, see the [Admin settings - Manage OAuth Clients](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-oauth-clients#custom-clients) documentation page.

**Important:** After the client has been registered, you must enable the client's switch on the Looker **Manage OAuth Clients** page.

Alternatively, administrators can register the OAuth client programmatically by calling the ['register_oauth_client_app'](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/register_oauth_client_app) API endpoint directly or by using the [Looker API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) under the **Auth** method.

### Install the Looker–Tableau BI Connector on Tableau Server

To install Looker–Tableau BI Connector on Tableau Server, perform the following steps:

  1. Download the latest version of the `avatica-<release_number>-looker.jar` file from <https://github.com/looker-open-source/calcite-avatica/releases>.
  2. Install the JAR file on your Tableau Server host machine. The default Tableau installation path for the file depends on the server's operating system:

     * Linux server: `/opt/tableau/tableau_driver/jdbc`
     * Windows server: `C:\Program Files\Tableau\Drivers`



### Register the OAuth client ID on Tableau Server

After you set up OAuth for Tableau Server on your Looker instance, you need to register the custom OAuth client on Tableau Server by following these steps:

  1. Sign in to Tableau Server using your admin credentials, and then navigate to the **Settings** page.
  2. In the **General** tab of the **Settings** page, scroll to **OAuth Clients Registry** , and click **Add OAuth Client**.
  3. In the **Create OAuth Client** dialog, enter the following information:

     * **Connection Type** : Select **Looker by Google** from the drop-down menu.
     * **OAuth Provider** : Select **Default IDP** from the drop-down menu.
     * **OAuth instance URL** : Enter your Looker instance URL with the `https://`. For example: `https://example.cloud.looker.com`:
           
           https://LOOKER_INSTANCE_URL
           

     * **Client ID** : Enter the **client_guid** value that you used when you set up OAuth for Tableau Server on your Looker instance:
           
           client_guid_server
           

     * **Client Secret** : Leave this field blank.

     * **Redirect URL** : Enter the **redirect_uri** value that you used when you set up OAuth for Tableau Server on your Looker instance:
           
           TABLEAU_SERVER_URL/auth/add_oauth_token
           

  4. Click the **Add OAuth Client** button to register the OAuth client ID and return to the **Settings** page.

  5. Click the **Save** button at the bottom or top of the **Settings** page to save your changes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
