---
url: https://docs.cloud.google.com/looker/docs/admin-panel-authentication-oauth-clients/
title: Admin settings - Manage OAuth Clients \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:36:56.530945+00:00
---

# Admin settings - Manage OAuth Clients  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-authentication-oauth-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Manage OAuth Clients Stay organized with collections  Save and categorize content based on your preferences. 

In Looker, administrators can use the **Manage OAuth Clients** page to manage identity-based OAuth 2.0 access for external applications without creating API keys or using the API Explorer. This document describes how to enable pre-configured applications, register custom OAuth clients, and manage token revocation.

The **Manage OAuth Clients** page is located in the **Authentication** section of the Looker **Admin** panel. It provides a centralized interface for granting access to developer tools such as the Looker CLI, AI agent Model Context Protocol (MCP) clients, and business intelligence (BI) connectors.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Requirements

To access and manage the **Manage OAuth Clients** page, the following requirements must be met:

  * Your Looker instance must be Looker-hosted. [Customer-hosted Looker instances](https://docs.cloud.google.com/looker/docs/glossary#customer-hosted) aren't supported.
  * You must have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) on your Looker instance.



## Overview

The **Manage OAuth Clients** page organizes client applications into two tabs:

  * **Application Library** : A catalog of pre-configured, Looker-managed OAuth applications, including AI agent Model Context Protocol (MCP) clients, business intelligence (BI) connectors, and developer tools.
  * **Custom Clients** : A management interface for registering and configuring your own custom OAuth client applications with customizable callback redirect URIs and group access controls.



A search bar at the top of the page lets you filter applications across both tabs in real time.

## Application Library tab

The **Application Library** tab contains pre-configured OAuth clients that are maintained by Looker. We recommend that you check the **Application Library** tab first before creating a custom client. If the tool that you want to connect is already pre-configured in the library, you can enable it without registering a new custom client, unless you need a different redirect URI or port.

The Application Library includes pre-configured clients for the following integrations:

  * **AI agent MCP clients** : Cursor, VS Code, Claude Code, Claude Desktop, ChatGPT, Gemini CLI, Cline, Windsurf, Antigravity, and the Looker Extension for VS Code.
  * **BI connectors** : Connected Sheets, Data Studio, Tableau Desktop, Microsoft Power BI, and Microsoft Excel.
  * **Developer tools** : Looker CLI.



### Enabling and disabling library applications

Each pre-configured client application in the Application Library has an **Enable** switch:

  * **Enable** : Enable the switch to allow users to authenticate into Looker from that client application by using OAuth.
  * **Disable** : Disable the switch to block authorization requests from that client application. Disabling an application immediately revokes and invalidates all active OAuth tokens that were issued to users for that application.

**Note:** Pre-configured applications in the Application Library cannot be deleted. They can only be enabled or disabled.

The **Client ID** for each pre-configured client application is displayed on its row. You can copy the client ID for use in client-side configurations, but the client ID for library applications is immutable and cannot be modified.

### Synchronization with the BI Connectors page

The enablement status of BI connectors (including Connected Sheets, Data Studio, Tableau Desktop, Microsoft Power BI, and Microsoft Excel) is automatically synchronized between the **Manage OAuth Clients** page and the [**BI Connectors**](https://docs.cloud.google.com/looker/docs/bi-connectors) page:

  * Changing the enablement status of a BI connector switch on the **Manage OAuth Clients** page automatically updates the corresponding connector switch on the **BI Connectors** page.
  * Changing the enablement status of a BI connector switch on the **BI Connectors** page automatically updates its status on the **Manage OAuth Clients** page.

**Note:** The **BI Connectors** page remains available to for configuring the outbound **Enable Connected Sheets quick link** setting.

### Redirect URIs and dynamic port configurations

Looker requires OAuth redirect URIs to match registered values exactly and does not support wildcard redirect URIs.

  * **Standard BI connectors** : Use pre-configured, immutable redirect URIs that match the service's official authentication endpoints.
  * **AI agent and MCP clients** : Some AI tools use dynamic or ephemeral local ports by default when initiating an OAuth redirect (such as Claude Code or Cline). To accommodate these tools, Looker pre-registers a fixed default port for each library client (for example, port `8080` for Claude Code and Cline, or port `7777` for Gemini CLI).



To use a pre-configured library client that requires a fixed port, choose one of the following options:

  1. **Configure the client to use the pre-registered static port** : In your client application settings or startup flags, specify the pre-registered port (for example, run Claude Code with `--callback-port 8080`).
  2. **Register a custom client** : If you want to use a different port or custom callback URL, register a new client on the **Custom Clients** tab with your preferred redirect URI.



## Custom Clients tab

The **Custom Clients** tab lets you register and administer custom OAuth 2.0 client applications for internal tools, proprietary integrations, or third-party applications that are not available in the Application Library.

### Registering a custom OAuth client

To register a new custom OAuth client, follow these steps:

  1. In the **Admin** panel, navigate to the **Authentication** section and select **Manage OAuth Clients**.
  2. Select the **Custom Clients** tab.
  3. Click **Add New**.
  4. In the side panel, complete the following fields: 
     * **Client ID** : Enter a unique string identifier for your application. The client ID cannot start with `com.looker.`, which is reserved for Looker-managed applications.
     * **Client Name** : Enter a descriptive display name for the application.
     * **Description** (Optional): Enter a brief description explaining the application's purpose.
     * **Redirect URIs** : Enter one or more authorized callback URIs (for example, `https://mycompany.com/oauth/callback` or `http://localhost:8080/callback`). You can enter multiple redirect URIs to support different environments or ports.
     * **Restrict to Group ID** (Optional): Enter the [numeric ID](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#viewing_and_searching_groups) of a Looker user group. If a numeric ID is specified, only users who belong to that group can authorize and authenticate into Looker using this application.
  5. Click **Add** to create the custom client.



### Viewing client details

To view detailed information for any custom client application, follow these steps:

  1. On the **Custom Clients** tab, click the  chevron_right chevron icon on the client's row in the table.
  2. A side panel opens, displaying the client name, client ID, description, the complete list of authorized redirect URIs, and, if configured, the group ID restrictions.



### Editing a custom client

To update an existing custom OAuth client application, follow these steps:

  1. On the **Custom Clients** tab, locate the client application and click the edit **Edit** icon on its row.
  2. In the edit side panel, update the **Client Name** , **Description** , **Redirect URIs** , or **Restrict to Group ID** fields as needed.

**Note:** The **Client ID** field cannot be modified after registration. If you need to change the client ID, delete the client and register a new one.
  3. Click **Update** to save your changes.




### Deleting a custom client

To remove a custom OAuth client application, follow these steps:

  1. On the **Custom Clients** tab, locate the client application and click the delete **Delete** (trash) icon on its row.
  2. In the confirmation dialog, click **Delete**.

**Warning:** Deleting a custom client permanently removes the client registration from Looker and immediately invalidates all active OAuth authorization codes, access tokens, and refresh tokens that were issued for that application.

## Token invalidation and security

To maintain security across connected applications, Looker automatically enforces token revocation. When an administrator deletes a custom client application or disables an application in the **Application Library** or **Custom Clients** tab, Looker immediately revokes all active OAuth refresh tokens that were issued to all users for that application. Any authorization codes that were associated with that application are permanently invalidated.

**Note:** In the cases of deleting or disabling an application, no new access tokens can be generated, and any already-issued access tokens will expire within 60 minutes.

If a user or an application attempts to connect by using revoked credentials, Looker denies authorization and returns an error that indicates that the OAuth client was not found or is not enabled.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
