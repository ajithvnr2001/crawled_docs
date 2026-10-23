---
url: https://docs.comfy.org/interface/job-history/
title: Job History - Queue and Past Runs - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:01.222419+00:00
---

# Job History - Queue and Past Runs - ComfyUI

> Source: https://docs.comfy.org/interface/job-history/

## On this page

  * Turn Job History on
  * Opening the panel
  * Tabs: All, Completed, Failed
  * Search, filter, and sort
  * Job list and actions
  * How this relates to Assets and Errors
  * Related pages



Left sidebar

# Job History - Queue and Past Runs

Copy pageCopy page

When Comfy.Queue.QPOV2 is on, the Job History sidebar shows active and past ComfyUI jobs with status badges, filters, and job actions.

Copy pageCopy page

**Job History** is a left-sidebar tab that appears when the setting **Docked job history/queue panel** (`Comfy.Queue.QPOV2`) is enabled. The frontend registers it at the **top** of the sidebar (`prepend`) so you can watch active jobs and browse past runs without using the floating queue overlay. When the setting is off, the tab is removed and the floating job-history overlay remains available instead (`Comfy.Queue.ToggleOverlay`). Run / queue controls in the top header still start jobs either way. This page is about the **sidebar** Job History surface. ![The Job History panel while a run is active: the status line, the Running group, completed jobs, and the All and Completed tabs](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/job-history/job_history_panel.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=12b96c86e3780d05edfc42ca322d6c2f) ![The Job History icon with the active job count badge while the tab is not open](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/job-history/job_history_badge.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=ca7132f25c4737f70b064eb5b610c6c5)

## 

​

Turn Job History on

  1. Open **Settings**.
  2. Under `Comfy` → `Queue` → `Layout`, enable **Docked job history/queue panel** (`Comfy.Queue.QPOV2`).
  3. The **Job History** icon appears at the top of the left sidebar.

The setting is experimental. On nightly builds it defaults to on; on other builds check the setting if you do not see the tab.

## 

​

Opening the panel

Click the **Job History** icon. While jobs are running or queued and this tab is **not** active, the icon shows a numeric badge with the active job count. Opening the tab clears the badge display for that view.

## 

​

Tabs: All, Completed, Failed

The panel header has status tabs:

  * **All** : every job in history for the current filters.
  * **Completed** : finished runs.
  * **Failed** : only appears when at least one failed job exists in the list.

Below the tabs, a summary line shows how many jobs are running and queued (or that there are no active jobs). A **Clear queue** control cancels all pending (queued, not yet running) jobs.

## 

​

Search, filter, and sort

Use the header tools to narrow the list:

  * **Search** : filter jobs by text.
  * **Filter** : **All workflows** or **Current workflow**.
  * **Sort** : **Most recent** or **Total generation time**.



## 

​

Job list and actions

Jobs are listed with status, progress when running, and preview thumbnails when outputs exist. From a job row or its context menu you can: **Running or queued**

  * Open as workflow in a new tab
  * Copy job ID
  * Cancel job

**Completed**

  * Inspect asset (when a preview exists)
  * Add the output to the current workflow as a loader node
  * Download the preview asset
  * Open as workflow in a new tab
  * Export workflow
  * Copy job ID

**Failed**

  * Open workflow in a new tab
  * Copy job ID
  * Copy error message
  * Report error
  * Remove job from the history list

The header actions menu includes **Clear history** , which opens a confirmation dialog. Clearing history removes queue history entries; read the dialog note about how that relates to stored assets on your install.

## 

​

How this relates to Assets and Errors

Outputs from completed runs also appear in [Assets](https://docs.comfy.org/interface/assets) when the assets system is enabled. Workflow failures and missing resources are listed in the [Right Side Panel](https://docs.comfy.org/interface/right-side-panel) **Errors** tab while you fix the graph.

## 

​

Related pages

  * [Interface Overview](https://docs.comfy.org/interface/overview)
  * [Assets](https://docs.comfy.org/interface/assets)
  * [Right Side Panel](https://docs.comfy.org/interface/right-side-panel)
  * [Comfy settings](https://docs.comfy.org/interface/settings/comfy)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/job-history.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/job-history)

[Apps Sidebar - Packaged Workflow AppsPrevious](https://docs.comfy.org/interface/apps)[Right Side Panel: Node Properties and ErrorsNext](https://docs.comfy.org/interface/right-side-panel)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
