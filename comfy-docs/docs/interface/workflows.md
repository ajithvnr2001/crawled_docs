---
url: https://docs.comfy.org/interface/workflows/
title: Workflows Sidebar - Saved and Open Graphs - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:03.625560+00:00
---

# Workflows Sidebar - Saved and Open Graphs - ComfyUI

> Source: https://docs.comfy.org/interface/workflows/

## On this page

  * Opening the Workflows panel
  * Sections in the panel
    * Open
    * Bookmarks
    * Browse
  * Search
  * Actions on a workflow
  * How this relates to the top tab strip
  * Related pages



Left sidebar

# Workflows Sidebar - Saved and Open Graphs

Copy pageCopy page

Use the Workflows left-sidebar panel to open saved ComfyUI workflows, bookmark favorites, manage open tabs, and search your graph library.

Copy pageCopy page

The **Workflows** entry in the left sidebar lists workflows saved on this installation, bookmarked favorites, and (optionally) the graphs you currently have open. From here you open a graph, rename or delete saved files, bookmark favorites, insert one workflow into another, and duplicate a graph without leaving the editor. Templates live in a separate browse action (`Browse Templates` in the View menu, or the Templates control in the sidebar). See [Templates](https://docs.comfy.org/interface/features/template). Packaged app workflows (files ending in `.app.json`) also appear under [Apps](https://docs.comfy.org/interface/apps). ![The Workflows panel with the Open, Bookmarks, and Browse sections and the search box](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/workflows/workflows_panel.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=fb82c64988ffaf4439223bdc5ddb7f30)

## 

​

Opening the Workflows panel

Click the **Workflows** icon in the left sidebar (default shortcut: `w`). The panel title is **Workflows**. Use the refresh button in the header to resync the saved-workflow list from disk.

## 

​

Sections in the panel

When you are not searching, the panel is split into sections:

### 

​

Open

Shown only when **Opened workflows position** (`Comfy.Workflow.WorkflowTabsPosition`) is set to **Sidebar**. It lists every workflow currently open in the editor as a flat list. Modified or unsaved graphs show a `*` before the name. Click the close button on a row to close that tab. Hold `Shift` while closing to skip the unsaved-changes warning (the close button switches to a destructive style while Shift is held). When the setting is **Topbar** (the default), open workflows stay in the top tab strip instead, and this section is hidden. If the position is **Sidebar** , the sidebar icon also shows a badge with the open-workflow count when the count is greater than zero.

### 

​

Bookmarks

A flat list of workflows you bookmarked. Use the bookmark icon on a leaf in **Browse** (or here) to toggle the bookmark. The section is hidden when you have no bookmarks.

### 

​

Browse

Your persisted workflows as a folder tree under the workflow storage path for this install. Click a leaf to open it. Empty libraries show an empty-state message.

## 

​

Search

The search box filters all workflows (not only Browse) by path. While a query is active, the panel switches to a single search-results tree.

## 

​

Actions on a workflow

On a workflow leaf you can:

  * **Open** : click the leaf to load it as the active graph.
  * **Rename** : rename in place; the file is renamed on disk with the correct workflow suffix (`.json` or `.app.json`).
  * **Delete** : remove a persisted workflow (temporary graphs cannot be deleted this way).
  * **Bookmark** : toggle the bookmark from the leaf action button.
  * **Drag** : workflow leaves are draggable for drop targets that accept them.
  * **Context menu** : 
    * **Insert** : insert the workflow into the current graph (not offered in App Mode).
    * **Duplicate** : create a copy of the workflow.



## 

​

How this relates to the top tab strip

The top workflow tabs and this sidebar list the same open graphs when tabs live in the top bar. Moving **Opened workflows position** between **Topbar** and **Sidebar** only changes where the open list is shown, not where files are stored. Paths differ by install type (Desktop app user data, portable/self-hosted user directory, Cloud workspace storage), but the panel sections and actions are the same.

## 

​

Related pages

  * [Interface Overview](https://docs.comfy.org/interface/overview)
  * [Templates](https://docs.comfy.org/interface/features/template)
  * [Apps](https://docs.comfy.org/interface/apps)
  * [Share workflow](https://docs.comfy.org/cloud/share-workflow) (Cloud)
  * [App Mode](https://docs.comfy.org/interface/app-mode)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/workflows.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/workflows)

[Model Library - Browse Local ModelsPrevious](https://docs.comfy.org/interface/model-library)[Apps Sidebar - Packaged Workflow AppsNext](https://docs.comfy.org/interface/apps)

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
