---
url: https://docs.comfy.org/interface/apps/
title: Apps Sidebar - Packaged Workflow Apps - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:00.062962+00:00
---

# Apps Sidebar - Packaged Workflow Apps - ComfyUI

> Source: https://docs.comfy.org/interface/apps/

## On this page

  * Opening the Apps panel
  * Empty state and Create
  * Working with apps
  * How Apps relates to Workflows and Templates
  * Related pages



Left sidebar

# Apps Sidebar - Packaged Workflow Apps

Copy pageCopy page

The Apps left-sidebar tab lists packaged workflow apps (.app.json). For the linear run UI, see App Mode.

Copy pageCopy page

The **Apps** entry is registered in the left sidebar after Assets, Node Library, Model Library, and Workflows. It lists packaged workflow apps: saved workflows whose file suffix is `.app.json`. The tab title includes a **Beta** badge. This sidebar catalog is not the same as [App Mode](https://docs.comfy.org/interface/app-mode). App Mode is the linear, simplified run UI for a workflow. The Apps sidebar is where you find and open packaged apps, create a blank workflow to start a new one, and manage those `.app.json` files the same way you manage ordinary workflows. ![The Apps panel with the Beta badge, the Create button, and the saved apps under Browse](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/apps/apps_panel.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=5c19665329960a9e62c1c8f3ec78f807)

## 

​

Opening the Apps panel

Click the **Apps** icon in the left sidebar. The panel reuses the same layout as [Workflows](https://docs.comfy.org/interface/workflows): search, optional **Open** section (when opened workflows are set to Sidebar), **Bookmarks** , and **Browse** , but every list is filtered to `.app.json` files only.

## 

​

Empty state and Create

When no apps are saved yet, the Browse area shows an empty state with a short message and a **Create app** button. When the Browse list has results, a **Create** button also appears in the panel header. Both actions run **New Blank Workflow** (`Comfy.NewBlankWorkflow`), which opens a blank graph you can configure for App Mode and save as an app.

## 

​

Working with apps

Actions match the Workflows panel for the filtered list:

  * Click an app to open it.
  * Bookmark, rename, delete, duplicate, and drag leaves the same way as ordinary workflows.
  * In the context menu, **Duplicate** is always available. **Insert** is available outside App Mode.

To actually run an app in the simplified linear UI, open it and enter App Mode. See [App Mode](https://docs.comfy.org/interface/app-mode) for building inputs and outputs, previewing the layout, and switching between graph editing and the app-style view.

## 

​

How Apps relates to Workflows and Templates

Surface| What it lists  
---|---  
[Workflows](https://docs.comfy.org/interface/workflows)| Ordinary saved graphs (and open tabs), typically `.json`  
**Apps** (this page)| Packaged apps ending in `.app.json`  
[Templates](https://docs.comfy.org/interface/features/template)| Official and community starter graphs from **Browse Templates** , not your local app library  
  
## 

​

Related pages

  * [App Mode](https://docs.comfy.org/interface/app-mode)
  * [Workflows](https://docs.comfy.org/interface/workflows)
  * [Templates](https://docs.comfy.org/interface/features/template)
  * [Interface Overview](https://docs.comfy.org/interface/overview)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/apps.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/apps)

[Workflows Sidebar - Saved and Open GraphsPrevious](https://docs.comfy.org/interface/workflows)[Job History - Queue and Past RunsNext](https://docs.comfy.org/interface/job-history)

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
