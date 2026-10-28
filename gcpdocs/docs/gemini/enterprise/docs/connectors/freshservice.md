---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:15:53.038799+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/

[ Skip to main content ](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/)
  * [Deutsch](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini%2Fenterprise%2Fdocs%2Fconnectors%2Ffreshservice%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/gemini-spark-blue-192px.svg) ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/#supported-actions)
  * [Limitations](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/#limitations)
  * [What's next](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/#whats-next)


**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)


Was this helpful?
Send feedback 
#  Overview Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/#supported-actions)
  * [Limitations](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/#limitations)
  * [What's next](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/#whats-next)


The Freshservice connector for Gemini Enterprise lets you search, read, and perform write operations on your Freshservice tickets using natural language.
## Supported actions
When the Freshservice connector is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.  
| Action  | Description  |  
| --- | --- |  
| Create ticket  | Creates a new ticket in Freshservice.  |  
| Create ticket note  | Adds a note (conversation) to an existing ticket in Freshservice.  |  
| Place service catalog item request  | Submits a request for a service catalog item.  |  
| Update ticket  | Updates an existing ticket in Freshservice.  |  
## Limitations
The Freshservice data store for Gemini Enterprise has the following limitations:
  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Freshservice data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Freshservice data store is supported only in the `global`, `us`, and `eu` locations.


## What's next
  * To create and configure a data store with Freshservice, see [Set up a Freshservice data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice/set-up-data-store).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
