---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/manage-data-agents/
title: Manage context sets in Bigtable Studio \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:58:49.708931+00:00
---

# Manage context sets in Bigtable Studio  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/manage-data-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Manage context sets in Bigtable Studio Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create context sets in Bigtable Studio using a context set file. Context set names must be unique within a project.

To learn about context sets, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/context-sets-overview). 

## Before you begin

Complete the following prerequisites before creating an agent.

### Enable required services

Enable the following services for your project: 

  * [Data Analytics API with Gemini](https://console.cloud.google.com/apis/library/geminidataanalytics.googleapis.com)
  * [Gemini for Google Cloud API](https://console.cloud.google.com/apis/library/cloudaicompanion.googleapis.com)
  * [Knowledge Catalog API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com)



### Prepare a Bigtable instance

Make sure that a Bigtable instance is available. For more information, see [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).

### Required roles and permissions

  * Grant the `bigtable.admin` role to the IAM user at the instance or project level. For more information, see [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).
  * Grant the `geminidataanalytics.queryDataUser` role to the IAM user at the project level. For more information, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).
  * To create, upload, and manage context sets, grant the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role to the IAM user at the project level. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).



## Create a context set

To create a context set, perform the following steps:

  1. In the Google Cloud console, go to the Bigtable page.

[Go to Bigtable](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  5. Click **Create context set**.

  6. In **Context set name** , provide a unique context set name. The context set name is case-sensitive and can contain letters, numbers, hyphens, and underscores. Names must be 4-30 characters.

The context set ID is derived from the context set name but is not necessarily identical. For the context set ID, the context set name is converted to lowercase and non-alphanumeric characters are replaced with the `-` character. For example, the context set name `querydata_e2e_test` has the context set ID `querydata-e2e-test`.

  7. Optional. In **Description** , add a description for your context set.

  8. Optional. To upload a context set file, click **Browse** in the **Upload context file** section, and select the context set file.

  9. Click **Create**.


**Note:** Creating the first context set in a project can take several minutes.

## Build context sets

After creating a context set, follow the steps in [Build context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/build-context-sets) to create a context set file. You can then edit your context set to upload the context set file.

## Edit a context set

To edit a context set, perform the following steps:

  1. In the Google Cloud console, go to the Bigtable page.

[Go to Bigtable](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**. 

  4. Click **View actions** next to the context set you want to edit.

  5. Click **Edit context set**. 

  6. Click **Browse** in the **Upload context file** section, and select the context set file.

  7. Click **Save**.




## Delete a context set

To delete a context set, perform the following steps:

  1. In the Google Cloud console, go to the Bigtable page.

[Go to Bigtable](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**. 

  4. Click **View actions** next to the context set you want to delete.

  5. Click **Delete context set**.

  6. In the **Delete context set** confirmation dialog, enter the ID of the context set.

  7. Click **Confirm** to delete the context set.




## What's next

  * Learn more about [context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/context-sets-overview).
  * Learn how to [test a context set](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/inspect-data-agent).
  * Learn how to [build context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/build-context-sets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
