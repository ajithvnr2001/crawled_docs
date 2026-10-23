---
url: https://docs.comfy.org/interface/overview/
title: Interface Overview - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:34:59.239244+00:00
---

# Interface Overview - ComfyUI

> Source: https://docs.comfy.org/interface/overview/

## On this page

  * Localization
  * Workspace map
    * Left sidebar
    * Right side panel
    * Canvas
    * Run bar
    * Bottom and help
  * Feature components
  * Settings
  * Account and credits
  * Cloud exclusive



Interface Guide

# Interface Overview

Copy pageCopy page

Map of the ComfyUI workspace: workspace regions, feature components, settings, account and credits, and Cloud exclusives, with links to each guide page.

Copy pageCopy page

The visual interface is how most people drive the [ComfyUI Server](https://docs.comfy.org/development/comfyui-server/comms_overview). Use this page as a map of the UI, then open the linked guides for each region and component. ![ComfyUI Basic Interface](https://mintcdn.com/dripart/EeFKEryMLH5667kk/images/interface/overview/comfyui_new_interface.jpg?fit=max&auto=format&n=EeFKEryMLH5667kk&q=85&s=4d18b1d3d8044ca37fc71f7e89d143e7) The [ComfyUI frontend](https://github.com/Comfy-Org/ComfyUI_frontend) is maintained as its own project. Contributions go to that repository.

## 

​

Localization

ComfyUI supports English, Chinese, Russian, French, Japanese, and Korean. Open **Settings** , then under `Comfy` → `Locale` pick your language. ![ComfyUI Localization Support](https://mintcdn.com/dripart/eWfBNjjL5jL2h2ib/images/interface/overview/locale.jpg?fit=max&auto=format&n=eWfBNjjL5jL2h2ib&q=85&s=f7bdc0a03f437ea74bd9c69e3b9bc6d7)

## 

​

Workspace map

![ComfyUI Workspace with numbered regions 1–6](https://mintcdn.com/dripart/Bf4DeDZgTg4kdJMV/images/interface/overview/comfyui-new-interface-main.png?fit=max&auto=format&n=Bf4DeDZgTg4kdJMV&q=85&s=a9b74b0809cce523bf37bfcefbfd68b5) Numbers in the screenshot match the regions below:

#| Area| What it is  
---|---|---  
**1**| **Left sidebar**|  Assets, Node Library, Model Library, Workflows, Apps, and (when enabled) Job History  
**2**| **Canvas**|  The graph where you place and connect nodes, plus canvas controls  
**3**| **Right side panel**|  Parameters, node info, settings, and errors for the current selection (opens from the top-bar properties toggle)  
**4**| **Top bar**|  Open workflows, Run / queue controls, login, and the properties panel toggle  
**5**| **Bottom left**|  Help Center, bottom panel (logs / shortcuts), and Settings  
**6**| **Bottom right**|  Canvas controls: pan, minimap, link visibility, zoom, fit  
  
### 

​

Left sidebar

The left rail icons, top to bottom. **Job History** appears at the top only when `Comfy.Queue.QPOV2` is enabled: ![Left sidebar icon order: Job History \(when enabled\), Assets, Nodes, Models, Workflows, Apps](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/overview/sidebar_order.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=660e8ca23ca81dbf9a3daf5c8a518f0d)

## Assets

Generated and imported media: preview, reuse, download, delete

## Node Library

Essentials grid and full node list, bookmarks, search

## Model Library

Models detected under your models folder

## Workflows

Locally saved workflows and recent files

## Apps

Sidebar Apps entry; see also App Mode under Feature components

## Job History

Queue / job history when QPOV2 is enabled

### 

​

Right side panel

## Right Side Panel

Parameters, Info (node docs), Settings, Errors

### 

​

Canvas

## Canvas Controls

Minimap, links, canvas info, zoom, fit, Focus Mode

## Nodes 2.0

Node chrome, headers, and selection behavior

### 

​

Run bar

The floating run bar sits at the top of the canvas and holds everything needed to start and supervise a run: batch count, Run, queue mode, cancel, and the active job count. ![Run bar: 1 drag handle, 2 batch count, 3 Run, 4 queue mode, 5 cancel, 6 active jobs](https://mintcdn.com/dripart/eWJdujtoaBSEH32O/images/interface/overview/run_bar.png?fit=max&auto=format&n=eWJdujtoaBSEH32O&q=85&s=a667c6a1008fdb6963c8c84fdfe5faa6)

#| Control| What it does  
---|---|---  
**1**| **Drag handle**|  Move the bar anywhere on the canvas. While you drag, a **Dock to top** zone appears to pin it back to the top edge.  
**2**| **Batch count**|  How many times the workflow is queued per run (default `1`). Type a value or use the up and down arrows.  
**3**| **Run**|  Queue the workflow. Hold `Shift` to queue it at the front of the queue instead of the end.  
**4**| **Queue mode menu**|  Choose when the workflow queues itself: **Run** (only when you click), **Run (On Change)** (queues again whenever the workflow changes), or **Run (Instant)** (queues again as soon as the current run finishes).  
**5**| **Cancel**|  Stop the run that is executing now. Disabled while the queue is idle.  
**6**| **Active jobs**|  Number of queued and running jobs. Click to open the queue, right-click to clear it.  
  
### 

​

Bottom and help

## Bottom Panel

Shortcuts, logs, and (desktop) command terminal

## Help Center

Release notes, docs, support, feedback

## 

​

Feature components

Reusable UI capabilities that are not tied to a single workspace chrome region.

## Templates

Built-in workflow templates

## App Mode

Linear / app-style UI for running workflows

## Subgraph

Collapse graphs into reusable subgraph nodes

## Partial Execution

Run only part of a workflow

## Node Docs

In-app node help (also on the RSP Info tab)

## Dynamic Inputs

Dynamic inputs that grow as you connect them

## Mask Editor

Paint and edit masks on the canvas

## 

​

Settings

## Settings

Full settings dialog by category

## 

​

Account and credits

## User

Account and profile settings

## Plan & Credits

Balance, top-up, usage activity, and Cloud invoices

## 

​

Cloud exclusive

## Workspaces

Team workspaces on Comfy Cloud

## Share Workflow

Share workflows from Cloud

## Import Models

Upload your own models to Cloud

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/overview)

[DependenciesPrevious](https://docs.comfy.org/basic-concepts/dependencies)[Assets - ComfyUI Media Asset LibraryNext](https://docs.comfy.org/interface/assets)

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
