---
url: https://docs.cloud.google.com/gemini/enterprise/docs/delete-a-data-store/
title: Delete a data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T12:43:06.711214+00:00
---

# Delete a data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/delete-a-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Delete a data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete a data store.

Deletion is an asynchronous process that can take days. You can't reuse a data store ID until the original data store is completely deleted. To prevent this from blocking your workflow, we strongly recommend that you use a unique ID for every data store. 

## Before you begin

Before deleting a structured or unstructured data store, if your data store is connected to an app, you must do one of the following:

  * To keep the app and delete only the data store, unlink the data store from its connected app.
  * To delete both the app and the data store, first [Delete the app](https://docs.cloud.google.com/gemini/enterprise/docs/delete-app) that the data store is connected to.



The following rules also apply:

  * You can't delete a data store that a data connector created by using the `dataStores.delete` method; the request fails with the error `Connected data store can only be deleted by internal requests`. Delete the data connector instead, which deletes its data stores.
  * Before you delete a data connector whose actions are enabled in an app or custom agent, turn off those actions or unlink the data store from the app. Otherwise, the deletion fails with the error `Deleting Data Connector with linked assistant actions is not supported. Please unlink assistant actions first`. This applies to every connector that provides actions, such as Jira, Outlook, and custom MCP servers.
  * The assistant of an app uses a data store that is created together with the app. You can't delete that data store directly; the request fails with the error `DataStore … is managed by Engine … and cannot be deleted directly`. The data store is deleted when you delete the app.
  * If you don't unlink the data store first, the request fails with the error `DataStore … currently exists in list at index … of Engine …`.



## Procedure

### Console

To delete a data store, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page, and then click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gemini-enterprise/data-stores)

  2. For the data store that you want to delete, click more_vert, and then click **Delete**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
