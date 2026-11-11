---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/imanage-platform/third-party-config/
title: iManage platform configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:55:03.113763+00:00
---

# iManage platform configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/imanage-platform/third-party-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  iManage platform configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how an iManage administrator configures iManage Control Center before you create the iManage platform data store in Gemini Enterprise.

**Note:** iManage platform uses Google-managed OAuth. You don't need to create your own OAuth application or provide a client ID and client secret. You authorize the connector with your iManage platform account when you enable connector in app.

## Configure iManage MCP Server

The iManage Model Context Protocol (MCP) Server accepts connections only from MCP clients that an iManage administrator has added to the allowlist. Before users can connect to iManage platform from Gemini Enterprise, an iManage administrator who belongs to the `NRTADMIN` group must enable the MCP applications, add Gemini Enterprise as an allowed MCP client, and assign an access policy in iManage Control Center.

For the full procedure in iManage Control Center, see the [iManage MCP Server Administration Guide](https://docs.imanage.com/ai/mcpserver-admin-help/en-US/) and [Requirements](https://docs.imanage.com/ai/mcpserver-admin-help/en-US/Requirements.html) in the iManage documentation.

### Add the iManage MCP applications

To enable the MCP server and its Control Center management interface, add both iManage MCP applications in iManage Control Center:

  1. Sign in to iManage Control Center as a member of the `NRTADMIN` group.
  2. Go to **Settings > Applications**.
  3. Add the **iManage MCP Control Center Extension** application.
  4. Add the **iManage MCP Service** application, and turn on **Allow Refresh Token** in its authentication settings so that Gemini Enterprise can maintain user sessions.



For detailed instructions, see [Adding the iManage MCP application in iManage Control Center](https://docs.imanage.com/ai/mcpserver-admin-help/en-US/Adding_the_iManage_MCP_application_in_iManage_Control_Center.html) in the iManage documentation.

### Allow Gemini Enterprise as an MCP client

To let Gemini Enterprise connect to your iManage MCP Server, add the Gemini Enterprise client URL to your allowed MCP clients list:

  1. In iManage Control Center, go to **Extensions > MCP Settings**.
  2. If prompted, read and accept the disclaimer.
  3. Select the **MCP Clients** tab.
  4. Add Gemini Enterprise to **Allowed MCP clients** by using one of the following methods: 
     * Enter the following client URL: `https://vertexaisearch.cloud.google.com`
     * If a user has already tried to connect from Gemini Enterprise, locate the request under **Pending approval** and approve it.



For detailed instructions, see [MCP Clients](https://docs.imanage.com/ai/mcpserver-admin-help/en-US/MCP_Clients.html) and [Selecting or adding MCP clients](https://docs.imanage.com/ai/mcpserver-admin-help/en-US/Selecting_or_adding_MCP_clients.html) in the iManage documentation.

### Assign an access policy to users

To grant users permission to use MCP tools with Gemini Enterprise, assign an access policy:

  1. In iManage Control Center, go to **Extensions > MCP Settings**.
  2. Select the **Assign Access Policy** tab.
  3. Assign an access policy to the users or groups who query iManage platform from Gemini Enterprise.



## What's next

  * To create and configure a data store with iManage platform, see [Set up an iManage platform data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/imanage-platform/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
