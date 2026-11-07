---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs/
title: Evaluate and approve enrichment proposals \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:53:32.453788+00:00
---

# Evaluate and approve enrichment proposals  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Evaluate and approve enrichment proposals Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Enrichment runs let you evaluate and approve AI-generated metadata proposals before they are published to your context set. Every time an enrichment task runs, it analyzes your target assets against your knowledge signals, computes evaluation metrics, and drafts proposed metadata updates. You can then inspect run performance, audit agent reasoning traces, and approve or deny the proposed changes.

## Before you begin

To get the permissions that you need to evaluate and approve enrichment runs, ask your administrator to grant you the following IAM roles:

  * On the target context set (or project): 
    * **Dataplex Content User** (`roles/dataplex.contentUser`) to view context set entries and proposals
    * **Dataplex Content Editor** (`roles/dataplex.contentEditor`) or **Dataplex Content Admin** (`roles/dataplex.contentAdmin`) to edit proposals and apply approved changes to the context set
  * On the project: 
    * **Dataplex Workflow Approver** (`roles/dataplex.workflowApprover`) to approve or deny change request batches
    * **Dataplex DataScan Viewer** (`roles/dataplex.dataScanViewer`) or **Dataplex Viewer** (`roles/dataplex.viewer`) to view enrichment tasks and run reports
    * **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`) to view catalog entries and aspects
    * **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`) or **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`) to apply approved proposals to catalog entries



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/grant-role-console).

You must also have run an active enrichment task in your project. For more information, see [Create enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks).

## Evaluation workflow

You can review an enrichment run in three phases:

  1. **Assess overall viability:** Check the aggregate scores on the **Overview** and **Evaluation** tabs. Those scores tell you if the run is broadly successful or needs closer inspection before you examine individual proposals.

  2. **Scrutinize individual proposals:** Filter the **Overview** tab for `Low` confidence proposals. If a proposal's decision is unclear, use the **Artifacts** tab to audit the raw conversation traces to understand why the agent made its suggestion.

  3. **Approve or deny the run:** Conduct a final check. If the majority of proposals are sound and properly grounded, approve the change request batch to merge the metadata into your context set. If the batch is heavily flawed, deny the batch, improve your context set or knowledge signals, and run the task again.




## Open an enrichment run

To view the details of an enrichment run, perform the following steps:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the navigation pane, select **Enrichments**.

The **Enrichments** page opens and displays a list of enrichment tasks. The task list includes the task name, status, run summary, trigger, and the date it was last modified.

  3. From the list of tasks, click the name of the enrichment task that you want to investigate.

The task details page opens to the **Jobs** tab by default and lists all historical runs for the task. Each run displays one of the following statuses: `Pending`, `Running`, `Needs review`, `Partially approved`, `Approved`, `Rejected`, `Succeeded`, `Succeeded with errors`, `Failed`, or `Cancelled`.

  4. In the list of jobs, click the linked **Name** (ID) of the run that you want to view. Alternatively, click more_vert **Actions** next to a run, and select **Result** (or select **Activity log** to jump directly to the run's execution logs).




The **Enrichment run details** page opens and organizes your results into the following tabs:

Tab | Use this tab to...  
---|---  
**Overview** | Assess the high-level health and confidence, and review and approve the generated metadata proposals. Answers the questions: _Is this run mostly good?_ and _What exactly will be published to the catalog?_  
**Evaluation** | Check quantitative scoring and pass/fail metrics. Answers the question: _Did the enrichment logic actually improve the data's usability?_  
**Artifacts** | Inspect diagnostics, tacit learning, and grounding scores. Answers the question: _Why did the agent make this decision and is the logic trustworthy?_  
**Logs** | Troubleshoot system execution traces. Answers the question: _Did the job fail technically?_  
  
## Assess overall run viability

The **Overview** tab is your starting point. Visit this tab to gauge the overall success of the run, browse the high-level metrics, and review or approve the specific metadata changes proposed by the AI.

To review the run summary:

  1. On the **Enrichment run details** page, select the **Overview** tab.

  2. Review the **Enrichment report**. This section displays the overall health of the run, including the aggregate score, status (for example, `Needs review`), duration, total tokens used, and a summary describing the overall confidence of the proposals.

**What to look for:** Review the aggregate score and summary to gauge whether the run succeeded at a macroscopic level before digging into individual proposals. For example, a score of 80% or higher generally indicates a high-confidence run, whereas lower scores might require you to review the proposals more carefully.

  3. Review the **End-to-end evaluation** section. This section displays the baseline and projected pass rates for your evaluation cases. An acceptable run typically results in a positive **Delta** (for example, +5%), indicating that the proposed metadata improves overall data usability compared to the baseline.

  4. Review the **Proposals** section. Each **Proposals** card displays a high-level summary of proposed changes (such as the total number of creations, updates, or deletions), followed by proposals grouped into the following collapsible categories:

     * **BigQuery tables** : Proposed table overview descriptions, column metadata, and glossary links.
     * **Knowledge base documents** : Proposed domain concepts, metric definitions, self-learning rules, and query templates.
     * **Knowledge base index** : Proposed navigation index entries (marked with an `Index` chip and an `N/A` confidence score) that map how context set entries relate to one another.
     * **Other changes** : Additional entry or aspect updates.

You can filter the proposals by confidence level (`High`, `Medium`, `Low`, `N/A`) and expand each category to view specific entries.

**What to look for:** Look for `Low` confidence proposals in particular, because those proposals typically indicate missing context or hallucinations that must be edited or removed.




## Scrutinize individual proposals

Unless you enabled auto-publish on the task, enrichment runs don't modify your metadata automatically. The run generates _proposed changes_ that you must review and approve.

When you review proposals, filter by confidence score and review the `Low` confidence proposals first, because they require the most scrutiny and are most likely to need manual adjustments or removal. Verify that the generated Markdown, tags, or descriptions accurately represent your business logic in **Preview** mode, and look for any unintended attribute overrides in the **Changes** view.

To review and act on the proposals generated by the run:

  1. On the **Enrichment run details** page, in the **Proposals** section, locate the proposal that you want to review.

  2. Click **View proposal** for the entry. A **Proposed changes** side panel opens.

  3. In the side panel, review and optionally edit the AI's generated metadata:

     * Under the specific resource being modified (for example, the **Overview** aspect), use the view toggle to switch between views.

The **Changes** view lets you inspect the exact diff being pushed to the context set. The diff is computed dynamically against the live entry while proposals are pending review; after you approve the batch, the proposed changes become the live version and the diff view is no longer displayed.

The **Preview** view displays the human-friendly formatting of the generated documents and tables.

     * To manually adjust the AI's proposal, click edit **Edit** next to the resource name, make your changes in the text editor, and then click **Save**.

  4. If an individual proposal is inaccurate, click **Remove from request** in the side panel, and then click **Remove** to confirm. Removing a proposal omits the proposed change from the change request batch so that it isn't applied when you approve the remaining proposals; it doesn't delete existing entries from the catalog or increment the deletions counter.

  5. Alternatively, to act on multiple proposals at once from the **Proposals** list, select the checkboxes next to the proposals (or use **Select all shown entries** , **Invert selection** , or **Clear**), and then click **Approve selected** to publish only the selected proposals or **Remove selected** to omit them from the batch.

  6. After you review all proposals in the batch, click **Approve** in the **Proposals** card header to merge all remaining proposals in the batch into your context set, or click **Deny** to reject the entire batch.




### Chained batch approvals, deletions, and superseded runs

Depending on the size of your task and changes to your task scope, the **Overview** tab can display specialized change request cards:

  * **Chained batch approvals for large runs** : When an enrichment run generates more than 250 metadata changes, Knowledge Studio automatically splits the proposals into sequential **Proposals** cards. You must review and approve batches in numerical order; subsequent batches remain locked until the preceding batch is approved. If you approve some batches and leave others pending or rejected, the run status shows `Partially approved`.
  * **Deletion proposals (`Deletions` card)**: When you remove target data assets from an enrichment task's scope, the next run generates a dedicated **Deletions** card proposing to remove the stale context entries from your context set. Deletion proposals always require manual human review and approval, even when **Auto-publish** is enabled on the task.
  * **Superseded runs** : If a later run of the same enrichment task completes while an earlier run still has pending proposals, Knowledge Studio locks the earlier run's pending proposals and displays a banner with a **View latest run** link so that you don't overwrite new metadata with stale proposals.



## View end-to-end evaluation metrics

The **Evaluation** tab measures the effect of the enrichment run. This tab compares how well your data answers test questions _with_ the proposed metadata versus _without_ it, helping you determine whether to approve the run or adjust your context sets.

When you evaluate results, use the **Why** column to understand the reasoning. The agent provides detailed reasoning comparing its logic to the reference. You can use this feedback to understand why the agent failed (for example, missing a critical table join). You can then use that information to improve your source data or clarify your context set.

To interpret the evaluation results:

  1. On the **Enrichment run details** page, click the **Evaluation** tab.
  2. Review the scores at the top of the tab. Focus on the **Delta** , which shows the overall percentage change in the pass rate, indicating the high-level value added by the enrichment proposals.
  3. Review the **Summary metrics** to see statistical changes (such as Average or Maximum) across specific criteria, like _Data result accuracy_.
  4. Use the **Per-case results** table to debug specific cognitive gaps. This table lists every test question evaluated during the run. 
     * Filter the list to locate **Fail** results or `Still failing` entries in the **Change** column.
     * Read the explanation in the **Why** column to understand AI failures.



## Audit run artifacts

The **Artifacts** tab contains detailed diagnostics and evidence supporting the AI's decisions. Visit this tab when you need to understand _why_ a proposal received a low confidence score. You can also use the **Artifacts** tab to audit raw conversation traces and learned rules extracted by the agent.

When you view the **Learnings** tab, check the **Applied** versus **Needs attention** counts. The **Applied** count shows how many new facts were successfully added to the system, whereas **Needs attention** flags contradictory or ambiguous findings that require manual cleanup. A count of `0` means no new knowledge was extracted this round, which is a normal outcome. If items are flagged as _ambiguous_ or _conflicts_ , the agent found contradictory information in your sources that you need to resolve in your context set.

When you view the **Confidence scores** tab, read the summary sentence (for example, _What held most proposals back_). Go to the **Changes proposed** section to isolate the lowest-rated changes. If a change is listed in that section, it likely failed grounding checks or lacked sufficient evidence. Use this list to prioritize which proposals to remove.

To view run artifacts:

  1. On the **Enrichment run details** page, click the **Artifacts** tab.

  2. Review the following sub-tabs to inspect diagnostic data:

     * **Learnings** : Displays whether the agent mined new _tacit knowledge_ (for example, from conversation logs or chat histories). You can also view the conversation traces that led to specific proposals.

     * **Confidence scores** : Breaks down the AI's confidence rating across three dimensions: **Grounding** , **Corroboration** , and **Source quality**. You can also access the raw `dynamic_eval.json` dataset from this section if you need to audit the evaluations.




## Troubleshoot failed runs

The **Logs** tab contains detailed system execution traces. Visit this tab to troubleshoot backend errors or investigate why an enrichment job failed to run to completion.

**Note:** Enrichment runs typically take 20 to 60 minutes to complete, or several hours when curation and evaluation sets are enabled. Execution logs can take 20 to 30 minutes to begin populating while the agent initializes and extracts signals.

Common issues and resolutions include the following:

  * **Changes failed to apply when approving a batch** : If a **Proposals** batch card displays an error banner stating that changes failed to apply, open the flagged proposal in the batch, edit and save the entry to fix the validation or formatting issue, or click **Remove from request**. Saving the fix returns the batch to the `Needs review` state so that you can click **Approve** again.

  * **Task scope exceeds 500 resources** : An enrichment task supports up to 500 total resources across default context set resources and added resources. If a task fails because of resource limits, edit the task scope to reduce the number of target tables or split your tables across multiple context sets and enrichment tasks.




To troubleshoot a failed run or inspect execution details:

  1. On the **Enrichment run details** page, click the **Logs** tab.
  2. Use the **Severity** menu or the **Filter** bar to narrow the log results.
  3. Review the execution traces and system logging. 
     * **What to look for:** Look for red `ERROR` or `FATAL` severity entries that indicate backend failures, such as quota exhaustion, missing execution service account permissions, or API timeouts.



Alternatively, if log routing is enabled for your project, you can query diagnostic logs directly using **Cloud Logging**. Detailed execution logs from the enrichment agent are routed to Cloud Logging with sensitive system instructions and raw data redacted.

Use the following queries in the Logs Explorer to filter logs:

  * **View all logs for enrichment tasks** :
        
        resource.type="dataplex.googleapis.com/EnrichmentTask"
        

  * **Filter logs for a specific task** :
        
        resource.type="dataplex.googleapis.com/EnrichmentTask"
        resource.labels.enrichment_task_id="TASK_ID"
        

  * **Filter logs for a specific run execution** :
        
        resource.type="dataplex.googleapis.com/EnrichmentTask"
        resource.labels.enrichment_task_id="TASK_ID"
        jsonPayload.runMetadata.enrichmentRun:"RUN_ID"
        

  * **Filter for warnings and errors** :
        
        severity>=WARNING
        




You can also use these queries to configure **Cloud Monitoring alert policies** based on your Cloud Logging metrics. For example, you can proactively route an alert to Slack, PagerDuty, or an email distribution list whenever an enrichment run fails (`severity>=ERROR`).

## Iterate on an enrichment task

If an enrichment run generates inaccurate proposals or fails grounding checks (reporting `Low` confidence), don't approve the run. Instead, improve the information given to the agent and run the task again:

  1. On the **Overview** tab, in the **Proposals** section, click **Deny**.

  2. If the agent misinterpreted your data schemas, go to the source definitions in Knowledge Catalog and improve the schema descriptions.

  3. If the agent lacked sufficient business logic or query patterns, go to the task's target **Context set** to add manual document entries or verified query templates, or remove outdated entries that confused the agent.

  4. Go to the **Enrichments** page, select your task, and click **Edit** to update the task configuration:

     * **Scope** : Add missing related tables to the target assets.
     * **Improve** : Attach missing knowledge signals (such as Cloud Storage documents, external connectors, or business glossaries) or update your evaluation sets.
  5. Save your changes, and then click **Run now** to generate a new set of proposals.




## What's next

  * [Manage context sets](https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
