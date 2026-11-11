---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/netdocuments/third-party-config/
title: NetDocuments configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:54:55.049069+00:00
---

# NetDocuments configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/netdocuments/third-party-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  NetDocuments configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how a NetDocuments administrator configures NetDocuments before you create the NetDocuments data store in Gemini Enterprise.

**Note:** NetDocuments uses Google-managed OAuth. You don't need to create your own OAuth application or provide a client ID and client secret. You authorize the connector with your NetDocuments account when you enable connector in app.

## Verify licensing and entitlements

Before configuring NetDocuments, verify the following prerequisites:

  * **Organization entitlement** : your NetDocuments repository must have **ndConnect** Model Context Protocol (MCP) access enabled.
  * **User licensing** : each user who connects to NetDocuments from Gemini Enterprise must have the required NetDocuments AI license, such as an **ndMAX Enterprise** subscription.



For more information about NetDocuments AI capabilities and licensing, see [Legal AI Integrations](https://www.netdocuments.com/legal-ai-integrations/) and [MCP via ndConnect](https://support.netdocuments.com/s/article/MCP-via-ndConnect) in the NetDocuments documentation.

## Enable ndConnect MCP for your repository

A NetDocuments **Repository Administrator** must enable **ndConnect** MCP for the repository in the NetDocuments Admin Console:

  1. Sign in to the NetDocuments Admin Console as a **Repository Administrator**.
  2. Go to **Security Center** , and then select **ndConnect**.
  3. Select **Enable MCP for this repository** , and then save your changes.
  4. If users save content to NetDocuments by using MCP actions, verify that each user has a primary cabinet assigned and that target cabinets are enabled for MCP.



For the full procedure in the NetDocuments Admin Console, see [MCP via ndConnect](https://support.netdocuments.com/s/article/MCP-via-ndConnect) in the NetDocuments documentation.

## What's next

  * To create and configure a data store with NetDocuments, see [Set up a NetDocuments data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/netdocuments/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
