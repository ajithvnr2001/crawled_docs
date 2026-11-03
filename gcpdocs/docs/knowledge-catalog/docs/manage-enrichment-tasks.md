---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-tasks/
title: Manage enrichment tasks \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T09:44:33.789955+00:00
---

# Manage enrichment tasks  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-tasks/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage enrichment tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can view, edit, manually run, and delete your enrichment tasks from the **Enrichments** page in Knowledge Studio. Managing your tasks lets you monitor job runs, update target resources and knowledge signals, trigger on-demand runs, and remove obsolete tasks.

## Before you begin

To view enrichment tasks, you must have the **Dataplex DataScan Viewer** (`roles/dataplex.dataScanViewer`) or **Dataplex Viewer** (`roles/dataplex.viewer`) role on the project. To edit, manually run, or delete enrichment tasks, you must have the **Dataplex DataScan Editor** (`roles/dataplex.dataScanEditor`) or **Dataplex Editor** (`roles/dataplex.editor`) role on the project. For more information, see the Grant required Identity and Access Management (IAM) roles to users section in [Configure prerequisites for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#grant-user-roles).

## View an enrichment task

To view the configuration and run history of an enrichment task, perform the following steps:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the navigation pane, select **Enrichments**.

  3. From the list of enrichment tasks, click the name of the task that you want to view.




The task details page opens and displays the following tabs:

  * **Jobs** (default): Displays a list of all historical runs (jobs) for the task, including each run's name, summary, status, last update time, duration, and tokens used.

  * **Details** : Displays the task's configuration, including its goal, context set, target resources, knowledge signals, evaluation settings, and run schedule.




**Note:** For tasks with auto-publishing enabled, the agent stages proposals as change requests and automatically approves them when the run meets your publishing criteria, leaving an audit record on the run report. Deletion proposals are always held for manual review.

## Edit an enrichment task

To modify an existing enrichment task, perform the following steps:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.
  2. In the navigation pane, select **Enrichments**.
  3. From the list of enrichment tasks, click the name of the task that you want to modify.
  4. Click **Edit**.
  5. Modify the task configuration as needed. You can update the task's goal, additional target resources, knowledge signals, evaluation settings, and run schedule, but you can't change the task's **Context set** or **Enrichment task region**.

If you remove target resources that were previously enriched by the task, the next enrichment run generates a **Deletions** change request card proposing to remove the stale context entries from the context set. Deletion proposals always require human review and approval.

  6. Click **Save** to apply your changes.




## Run an enrichment task manually

Although tasks can run automatically on a schedule, you can also trigger a run manually:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.
  2. In the navigation pane, select **Enrichments**.
  3. From the list of enrichment tasks, click the name of the task that you want to trigger.
  4. Click **Run now**.



Knowledge Studio initiates a new job run and lists the run in the **Jobs** tab.

## Delete an enrichment task

Deleting an enrichment task is permanent and can't be undone. When you delete an enrichment task, the following actions occur:

  * **Task and run history removal** : Knowledge Studio permanently deletes the task configuration, cancels any future scheduled runs, and removes all historical job runs (**Jobs**) and unapplied change proposals for the task.
  * **Runtime resource cleanup** : Knowledge Studio automatically deletes temporary runtime resources and Cloud Storage execution files provisioned for the task.
  * **Preserved context set metadata** : Deleting the task doesn't delete the associated context set or revert any entries, descriptions, aspects, or entry links that were already published to the context set.



To delete an enrichment task, perform the following steps:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.
  2. In the navigation pane, select **Enrichments**.
  3. Delete one or more tasks: 
     * **To delete a single task from its details page** : Click the name of the task that you want to delete, and then click **Delete**.
     * **To delete one or more tasks from the task list** : Select the checkbox next to each task that you want to delete, and then click **Delete** in the action bar.
  4. In the confirmation dialog, click **Delete** to confirm.



## What's next

  * [About enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks)
  * [Evaluate and approve enrichment proposals](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
