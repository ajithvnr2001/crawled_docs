---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/
title: About saved queries \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:51:19.251673+00:00
---

# About saved queries  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/

[ Skip to main content ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/)
  * [Deutsch](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=de)
  * [Español](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=it)
  * [Português](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Ffirestore%2Fmongodb-compatibility%2Fdocs%2Fsaved-queries%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Storage location](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/#storage-location)
  * [Limitations](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/#limitations)
  * [Pricing](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/#pricing)
  * [What's next](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview)


Was this helpful?
Send feedback 
  * On this page
  * [Storage location](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/#storage-location)
  * [Limitations](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/#limitations)
  * [Pricing](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/#pricing)
  * [What's next](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/saved-queries/#whats-next)


# About saved queries Stay organized with collections  Save and categorize content based on your preferences.
To store, reuse, and share frequently run database statements without rewriting them for each session, you can use saved queries in Firestore with MongoDB compatibility.
You can use Firestore Studio to create, save, and manage queries. The saved queries capability is available only in the console; you cannot run or manage saved queries through an API or other means.
Saved queries have the following characteristics:
  * Google-owned and Google-managed encryption keys encrypt all queries at rest.
  * A saved query is a child of a project.
  * Saved queries are deleted when the project is deleted. If you delete the instance or database, you can still access saved queries in the project using the [**Saved queries** page](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-manage-saved-queries) in the Google Cloud console.
  * You must have the correct [Identity and Access Management (IAM) role or permissions](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-manage-saved-queries#required-roles) to view and manage saved queries.
  * You can only access saved queries using Firestore Studio or by navigating to the **Saved queries** page in the Google Cloud console. Saved queries aren't accessible through the API.


## Storage location
Firestore with MongoDB compatibility attempts to store queries in the same location as the database. However, storage for saved queries is available in a limited number of locations, so it might select another region by default. To view and update the location where your saved queries are stored, first click **Show Advanced Options** from the save subtask. Then, from the **Region** list, select an available location.
## Limitations
Saved queries has the following limitations:
  * There is a rate limit of 20 queries per second (QPS) per user per project, including both read and write. This quota is not trackable or overridable.
  * You can't create more than 10,000 saved queries in a project—including saved queries for other Google Cloud products. For more information, see [Quotas and limits](https://docs.cloud.google.com/firestore/mongodb-compatibility/quotas) .
  * You can't use [customer-managed encryption keys](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/cmek) for instances with saved queries .


## Pricing
There is no additional charge for using or storing saved queries.
## What's next
  * Learn how to [create and manage saved queries](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-manage-saved-queries) . 
  * Learn how to [manage Firestore with the Google Cloud console](https://docs.cloud.google.com/firestore/native/docs/using-console). 


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
