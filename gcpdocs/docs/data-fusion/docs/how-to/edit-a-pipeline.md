---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/
title: Edit pipelines \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:00:13.905283+00:00
---

# Edit pipelines  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/

[ Skip to main content ](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/)
  * [Deutsch](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=de)
  * [Español](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=es-419)
  * [Français](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=id)
  * [Italiano](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=it)
  * [Português](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=ja)
  * [한국어](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdata-fusion%2Fdocs%2Fhow-to%2Fedit-a-pipeline%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#before_you_begin)
  * [Edit the pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#edit)
  * [View or restore a previous version of the pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#view-or-restore-version)
  * [Export an edited version of a deployed pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#export)
    * [Export the latest version](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#export-latest-version)
    * [Export a previous version](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#export-previous-version)
  * [Import an edited version of a deployed pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#import)
  * [Delete an edited version of a pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#delete)
  * [Statuses for edited pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#statuses)
  * [What's next](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)


Was this helpful?
Send feedback 
#  Edit pipelines Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#before_you_begin)
  * [Edit the pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#edit)
  * [View or restore a previous version of the pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#view-or-restore-version)
  * [Export an edited version of a deployed pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#export)
    * [Export the latest version](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#export-latest-version)
    * [Export a previous version](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#export-previous-version)
  * [Import an edited version of a deployed pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#import)
  * [Delete an edited version of a pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#delete)
  * [Statuses for edited pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#statuses)
  * [What's next](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/#whats_next)


This page describes how to edit deployed batch pipelines in Cloud Data Fusion.
Editing a pipeline lets you do the following:
  * Incrementally add features to a deployed pipeline without creating duplicates. For example, you can add, remove, or modify plugins, then redeploy the pipeline. Editing a pipeline creates a new version of the same pipeline, which prevents a proliferation of pipelines, allowing for better organization. Duplicating a pipeline creates a new pipeline with a different name.
  * Maintain a history of the edited versions.
  * View and restore old versions of a pipeline.
  * Edit any part of the pipeline, such as the pipeline structure, configuration, metadata, preferences, and comments.
  * Export an edited JSON file for a deployed pipeline.


When you edit the pipeline, Cloud Data Fusion creates a new draft, which becomes the _latest version_. The name of the pipeline remains the same. You develop the pipeline iteratively, without creating duplicate pipelines with unique names. The latest version retains the triggers, pipeline configurations, runtime arguments, metadata, comments, and schedules from the previous version. The latest version is the active version of the pipeline: it can be run or scheduled to run.
## Before you begin
  * Cloud Data Fusion supports editing deployed batch pipelines in version 6.9.1 and later. To upgrade to the latest version, see [Upgrade your Cloud Data Fusion environment](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).
  * Cloud Data Fusion doesn't support editing deployed real-time pipelines or replication jobs.


## Edit the pipeline
To edit a deployed batch pipeline in Cloud Data Fusion, follow these steps:
  1. Go to your instance: 
    1. In the Google Cloud console, go to the Cloud Data Fusion page.
    2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.
[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)
  2. Click **List > Deployed**.
  3. Go to the pipeline that you want to edit and click more_vert **More > Edit**.
A new draft of the pipeline appears on the **Studio** page.
  4. Edit your pipeline. For example, add a new analytics node, or edit the properties of a source.
  5. Optional: To finish editing the pipeline later, click **Save**.
  6. After you finish editing the pipeline, click **Deploy**.
  7. In the **Enter change summary** dialog, enter a description of the changes you made to the pipeline and click **Deploy**. The deployed pipeline opens on the **Pipeline** page.


## View or restore a previous version of the pipeline
To view or deploy a previous version of a batch pipeline, follow these steps:
  1. Open your instance in the Cloud Data Fusion interface.
  2. Click **List > Deployed**.
  3. Select a pipeline. The pipeline appears on the **Pipeline** page.
  4. Click history **History**.
A version history list appears.
  5. Optional: To view a previous version of a pipeline, click **View**.
  6. Optional: To restore an older version of the pipeline to the latest version, click **Restore**.
Cloud Data Fusion creates a new version of the pipeline and opens it on the **Pipeline** page. It's now the latest version.


## Export an edited version of a deployed pipeline
You can export the edited version of a deployed pipeline as a JSON file to share with other developers, add it to version control, or move it from a development environment to a test or production environment. For example, after you edit a pipeline during development and debugging phases, you export the JSON file, and then import and deploy it in a production environment.
### Export the latest version
To export the latest version of the pipeline, follow these steps:
  1. Open your instance in the Cloud Data Fusion interface.
  2. Click **List > Deployed**.
  3. Select the pipeline that you want to export and click more_vert **More > Export**.
A JSON file with the pipeline configurations from the latest version is saved locally.


### Export a previous version
To export previous versions of the pipeline, follow these steps:
  1. Open your instance in the Cloud Data Fusion interface.
  2. Click **List > Deployed**.
  3. Select the pipeline. The latest version opens on the **Pipelines** page.
  4. Click history **History**.
  5. Select the pipeline version that you want to export and click **View > Actions > Export**.


## Import an edited version of a deployed pipeline
All pipelines are exported in the `Draft` state. Edited versions of a deployed pipeline are also imported in the `Draft` state. For more information, see [Import a pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines#import).
## Delete an edited version of a pipeline
When you delete the latest version of a deployed pipeline, all versions of the deployed pipeline are deleted. Draft versions aren't deleted.
Instead, the draft pipeline version has the **Orphaned** status. To resolve this status, deploy the draft pipeline. Cloud Data Fusion creates a new pipeline, which is the latest version.
## Statuses for edited pipelines
When you edit pipelines, the following statuses might appear on the **Pipeline Drafts** page.  
| Status  | Description  |  
| --- | --- |  
| **In-Progress**  | You have saved edits to the pipeline.  |  
| **Orphaned**  | The latest version of the pipeline was deleted and associated drafts no longer belong to an existing pipeline. You might see this status if someone deletes the pipeline with the following endpoint: `DELETE/v3/namespaces/NAMESPACE_ID/apps/APP_ID       `.   |  
| **Obsolete**  | A newer version has been deployed while edits have been in progress. You might see this status if another developer deploys the pipeline before you finish editing. This is the same as **Draft Out of Date** that appears on the Pipeline page.  |  
When you edit pipelines, the following statuses might appear on the **Studio** page.  
| Status  | Description  |  
| --- | --- |  
| Editing in progress  | You're editing a draft pipeline.  |  
| Orphaned draft  | Someone deployed a newer version while you were editing the pipeline.   |  
## What's next
  * Learn how to [export and import pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
