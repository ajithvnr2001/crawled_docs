---
url: https://docs.comfy.org/interface/right-side-panel/
title: Right Side Panel: Node Properties and Errors - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:02.511278+00:00
---

# Right Side Panel: Node Properties and Errors - ComfyUI

> Source: https://docs.comfy.org/interface/right-side-panel/

## On this page

  * Open and close the panel
  * The panel follows your selection
    * Parameters
    * Nodes
    * Info
    * Settings
    * Errors
  * Favoriting inputs
  * Related



Right side panel

# Right Side Panel: Node Properties and Errors

Copy pageCopy page

Use the ComfyUI right side panel to edit node parameters and settings, favorite inputs, change node state, and fix workflow errors.

Copy pageCopy page

The right side panel is the properties panel on the right edge of the ComfyUI workspace. It shows the parameters, info, and settings of whatever you have selected on the canvas, keeps the inputs you use most one click away, and lists workflow errors together with their fixes.

## 

​

Open and close the panel

Click the panel icon in the top right control area to open the panel. The button tooltip reads **Toggle properties panel** , and when the workflow has errors while the panel is closed, the button shows a red dot so you can open the panel straight into the error list. Close the panel from the icon in its own header. ![ComfyUI top-right control area with the properties panel button highlighted](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_button.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=54658426a24489c6a3fd458dc065428b) ComfyUI remembers the panel state between sessions.

## 

​

The panel follows your selection

The title and the available tabs change with what is selected on the canvas:

Selection| Panel title| Tabs  
---|---|---  
Nothing| Workflow Overview| Parameters, Nodes, Settings  
One node| The node name| Parameters, Info, Settings, plus Errors when relevant  
One subgraph node| The node name| Parameters, Settings, plus Errors when relevant and the Edit subgraph button  
Multiple items| The number of selected items| Nodes, Settings, plus Errors when relevant  
  
Click the pencil button next to the title to rename the selected node or group. For a subgraph node, the header also shows an **Edit subgraph** button that opens the subgraph editor inside the panel. The Errors tab appears only when the selection has relevant errors, or when nothing is selected and the workflow contains errors. You can hide the tab entirely with the **Show errors tab in side panel** setting under `Comfy` → `Error System`.

### 

​

Parameters

With one node selected, the **Parameters** tab lists its inputs under **INPUTS**. With several items selected, the same view is labelled **Nodes** and lists the inputs of every selected item. Both views have a search field at the top and a collapsible section per node. Inputs marked as advanced are collected in a separate **ADVANCED INPUTS** section. Every input has an actions menu with **Rename** , **Favorite** , and **Reset to default** , plus **Hide input** for inputs promoted from a subgraph. When multiple nodes are selected, each section also has a button to locate its nodes on the canvas. ![Right side panel with one node selected, showing the Parameters tab and its INPUTS list](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_parameters.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=aeded554ee84c0b44d7e44cc7fdcd9a9) With nothing selected, the same tab shows your favorited inputs instead, so you can adjust the values you change most often without selecting a node first.

### 

​

Nodes

The Nodes tab is shown when nothing is selected. It lists every node in the workflow with its inputs, searchable and collapsible, so you can review or edit any node from one place. It is also the label the parameters view uses when several items are selected.

### 

​

Info

The Info tab appears for a single selected node that is not a subgraph. It shows the same [Node docs](https://docs.comfy.org/interface/features/node-docs) help content you get from the selection toolbox docs icon and from the help button on Nodes 2.0.

### 

​

Settings

With a selection, the Settings tab covers the selected nodes and groups:

  * **Node state** : **Normal** , **Bypass** , or **Mute**.
  * **Node color** : pick a color for the node.
  * **Pinned** : pins the node so it stays fixed in place on the canvas.

![Right side panel Settings tab with node state, node color, and pinned controls](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_settings.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=dbaec8a4b6a018140394fddc4f40ab4d) Changes apply to every item in the selection, so you can set the same state or color for a whole group at once. Groups expose the color and pin controls only. With nothing selected, the tab is labelled **Global Settings** and gathers quick toggles that mirror the full settings dialog:

  * **Nodes** : Show advanced parameters, Show toolbox on selection, Nodes 2.0.
  * **Canvas** : Grid spacing, Snap nodes to grid.
  * **Connection links** : Link shape, Show connected links.
  * **View all settings** : opens the full settings dialog.



### 

​

Errors

The Errors tab groups the problems that block the workflow, so you can resolve them before running:

  * **Node errors** : the failing node, the error message, an **Expand** and **Collapse** control, and **Locate node on canvas**.
  * **Missing node packs** : **Install All** , **Apply Changes** , and **View in Manager** when ComfyUI Manager is available.
  * **Missing models** : **Download** for a single file or **Download all** , **Import** in Comfy Cloud for models you provide yourself, and a note when a model is gated on Hugging Face and needs a signed-in account with the license accepted.
  * **Missing inputs** : input media that the workflow expects but cannot find.
  * **Error log** and links to submit a GitHub issue or contact support.



## 

​

Favoriting inputs

Favorited inputs are the panel’s shortcuts. Open the Parameters tab, click the actions menu on any input, and choose **Favorite**. Favorited inputs then appear in the panel whenever nothing is selected, where you can search and reorder them. Use **Unfavorite** in the same menu to remove one. ![The right side panel on the Errors tab, listing a missing input for the Load Image node with the locate button](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_errors.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=076927960b2cf80d531b6f0b008d72a9) ![The Info tab showing the built-in documentation for the selected KSampler node](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_info.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=61fab494dd86b58e5f22fe89371a24db) ![The properties panel toggle button with the error indicator while the panel is closed](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_error_badge.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=e1b930304ab8bcb9b9f552e817897cd1)

## 

​

Related

  * [Interface Overview](https://docs.comfy.org/interface/overview) for the workspace areas.
  * [ComfyUI Settings](https://docs.comfy.org/interface/settings/overview) for the full settings dialog.
  * [Node Docs](https://docs.comfy.org/interface/features/node-docs) (same help content as the Info tab).
  * [Node Library](https://docs.comfy.org/interface/node-library).



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/right-side-panel.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/right-side-panel)

[Job History - Queue and Past RunsPrevious](https://docs.comfy.org/interface/job-history)[Canvas Controls - Minimap, Zoom, and Focus ModeNext](https://docs.comfy.org/interface/canvas-controls)

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
