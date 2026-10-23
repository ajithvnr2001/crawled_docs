---
url: https://docs.comfy.org/interface/settings/comfy/
title: Comfy Settings - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:02.952363+00:00
---

# Comfy Settings - ComfyUI

> Source: https://docs.comfy.org/interface/settings/comfy/

## On this page

  * Partner Nodes
    * Show Partner Node pricing badge
  * Dev Mode
    * Enable dev mode options (API save, etc.)
  * Edit Token Weight
    * Ctrl+up/down precision
  * Error System
    * Show errors tab in side panel
    * Show missing nodes in the issues tab
    * Show missing models in the issues tab
    * Show missing media in the issues tab
  * Execution
    * Live preview method
  * Locale
    * Language
  * Menu
    * Use new menu
  * Model Library
    * What name to display in the model library tree view
    * Automatically load all model folders
  * Node
    * Show deprecated nodes in search
    * Show experimental nodes in search
  * Node Library
    * New Node Library Design
  * Node Search Box
    * Number of nodes suggestions
    * Show node frequency in search results
    * Show node id name in search results
    * Show node category in search results
    * Node preview
    * Node search box implementation
    * Added nodes follow the cursor
  * Node Widget
    * Widget control mode
    * Textarea widget spellcheck
  * Notification Preferences
    * Show version updates
  * Queue
    * Queue history size
    * Docked job history/queue panel
  * Queue Button
    * Batch count limit
  * Validation
    * Validate workflows
  * Window
    * Show confirmation when closing window
  * Workflow
    * Persist workflow state and restore on page (re)load
    * Auto Save
    * Auto Save Delay (ms)
    * Show confirmation when deleting workflows
    * Save and restore canvas position and zoom level in workflows
    * Opened workflows position
    * Prompt for filename when saving workflow
    * Sort node IDs when saving workflow
    * Require confirmation when clearing workflow
    * Enable node replacement suggestions
    * Require confirmation to overwrite an existing subgraph blueprint
    * Restore widget values by name



ComfyUI Settings

# Comfy Settings

Copy pageCopy page

Detailed description of ComfyUI core setting options

Copy pageCopy page

The settings described on this page are located in the **ComfyUI in-app settings menu**. You can open it by navigating to **Settings** (gear icon) or using the `Ctrl + ,` keyboard shortcut, then select the corresponding category to view and configure these options.

## 

​

Partner Nodes

### 

​

Show Partner Node pricing badge

  * **Default Value** : Enabled
  * **Function** : Controls whether to display pricing badges on Partner Nodes, helping users identify the usage cost of Partner Nodes

![Show Partner Node pricing badge](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/comfy/api_node_pricing_badge.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d930d2fdabb096a91d6df9bb8c2b26bb)

> For more information about Partner Nodes, please refer to [Partner Nodes](https://docs.comfy.org/tutorials/partner-nodes/overview)

## 

​

Dev Mode

### 

​

Enable dev mode options (API save, etc.)

  * **Default Value** : Disabled
  * **Function** : Enables development mode options (such as API save, etc.)



## 

​

Edit Token Weight

### 

​

Ctrl+up/down precision

  * **Default Value** : 0.01
  * **Function** : When using CLIPTextEncode type nodes or text input node widgets, use Ctrl+up/down to quickly adjust weights. This option changes the weight value for each adjustment



## 

​

Error System

### 

​

Show errors tab in side panel

  * **Default Value** : Enabled
  * **Function** : Displays an Issues tab in the right side panel that lists blocking errors and missing resources that need setup, such as missing node packs, model files, and input media. Disabling it hides the tab and the error overlay; runtime and prompt execution errors still appear in dialogs



### 

​

Show missing nodes in the issues tab

  * **Default Value** : Enabled
  * **Function** : Controls whether missing node packs are listed in the Issues tab and highlighted on the canvas. Hiding them does not make the workflow runnable: the nodes still have to be installed before it can run



### 

​

Show missing models in the issues tab

  * **Default Value** : Enabled
  * **Function** : Controls whether model files that cannot be found are listed in the Issues tab and highlighted on the canvas



### 

​

Show missing media in the issues tab

  * **Default Value** : Enabled
  * **Function** : Controls whether input images, videos, and audio that cannot be found are listed in the Issues tab and highlighted on the canvas



## 

​

Execution

### 

​

Live preview method

  * **Default Value** : default
  * **Options** : default, none, auto, latent2rgb, taesd
  * **Function** : Sets how an image in progress is previewed while a prompt runs. `default` uses the preview method configured on the ComfyUI server, and `none` turns live previews off



## 

​

Locale

### 

​

Language

  * **Options** : English, 中文 (Chinese),日本語 (Japanese), 한국어 (Korean), Русский (Russian), Español (Spanish), Français (French)
  * **Default Value** : Auto-detect browser language
  * **Function** : Modify the display language of ComfyUI interface



## 

​

Menu

### 

​

Use new menu

  * **Default Value** : Top
  * **Function** : Select menu interface and position; currently supports Top and Bottom



  * Top

  * Bottom




The menu interface will be displayed at the top of the workspace![Top Menu](https://mintcdn.com/dripart/A0ohfUGOp7aobXHn/images/interface/setting/comfy/UseNewMenu_top.jpg?fit=max&auto=format&n=A0ohfUGOp7aobXHn&q=85&s=6581ad8f565a37b79bb227066c6a9a3e)

The menu bar interface will be displayed at the bottom of the workspace![Bottom Menu](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/comfy/UseNewMenu_bottom.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f32277b0016b128cf57783fc09b2ec18)

## 

​

Model Library

Model Library refers to the model management function in the ComfyUI sidebar menu. You can use this function to view models in your `ComfyUI/models` and additionally configured model folders. ![Model Library](https://mintcdn.com/dripart/EeFKEryMLH5667kk/images/interface/sidepanel/model_library.jpg?fit=max&auto=format&n=EeFKEryMLH5667kk&q=85&s=e0a688e26a545ebf5db465119bc14f06)

### 

​

What name to display in the model library tree view

  * **Default Value** : title
  * **Function** : Select the name format to display in the model library tree view, currently only supports filename and title



### 

​

Automatically load all model folders

  * **Default Value** : Disabled
  * **Function** : Whether to automatically detect model files in all folders when clicking the model library. Enabling may cause loading delays (requires traversing all folders). When disabled, files in the corresponding folder will only be loaded when clicking the folder name.



## 

​

Node

During the iteration process of ComfyUI, we will adjust some nodes and enable some nodes. These nodes may undergo major changes or be removed in future versions. However, to ensure compatibility, deprecated nodes have not been removed. You can use the settings below to enable whether to display **experimental nodes** and **deprecated nodes**.

### 

​

Show deprecated nodes in search

  * **Default Value** : Disabled
  * **Function** : Controls whether to display deprecated nodes in search. Deprecated nodes are hidden by default in the UI, but remain effective in existing workflows.

![Show deprecated nodes in search](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/comfy/depr_node.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=be33ca36eb10dc84a8f83aa8955738e4)

### 

​

Show experimental nodes in search

  * **Default Value** : Enabled
  * **Function** : Controls whether to display experimental nodes in search. Experimental nodes are some new feature support, but are not fully stable and may change or be removed in future versions.

![Show experimental nodes in search](https://mintcdn.com/dripart/A0ohfUGOp7aobXHn/images/interface/setting/comfy/beta_node.jpg?fit=max&auto=format&n=A0ohfUGOp7aobXHn&q=85&s=e77212e5d08039e65ace1f6dfcccc34b)

## 

​

Node Library

### 

​

New Node Library Design

  * **Default Value** : Enabled
  * **Function** : Uses the redesigned node library sidebar with the Essential, All, and Custom tabs, improved search, and hover previews



## 

​

Node Search Box

### 

​

Number of nodes suggestions

  * **Default Value** : 5
  * **Function** : Used to modify the number of recommended nodes in the related node context menu. The larger the value, the more related recommended nodes are displayed.

![Number of nodes suggestions](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/comfy/node_suggestions.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=5dc8c7cc67b5ac49fd5a0d733cb73c04)

### 

​

Show node frequency in search results

  * **Default Value** : Disabled
  * **Function** : Controls whether to display node usage frequency in search results

![Show node frequency in search results](https://mintcdn.com/dripart/A0ohfUGOp7aobXHn/images/interface/setting/comfy/node_frequency.png?fit=max&auto=format&n=A0ohfUGOp7aobXHn&q=85&s=a41b74a30294a7b2d4b82a83c63ae1cc)

### 

​

Show node id name in search results

  * **Default Value** : Disabled
  * **Function** : Controls whether to display node ID names in search results

![Show node id name in search results](https://mintcdn.com/dripart/A0ohfUGOp7aobXHn/images/interface/setting/comfy/node_id_name.jpg?fit=max&auto=format&n=A0ohfUGOp7aobXHn&q=85&s=d346ef21812e3bea8f4f81197be66dcc)

### 

​

Show node category in search results

  * **Default Value** : Enabled
  * **Function** : Controls whether to display node categories in search results, helping users understand node classification information



### 

​

Node preview

  * **Default Value** : Enabled
  * **Function** : Controls whether to display node previews in search results, making it convenient for you to quickly preview nodes



### 

​

Node search box implementation

  * **Default Value** : default
  * **Function** : Select the implementation method of the node search box (experimental feature). If you select `litegraph (legacy)`, it will switch to the early ComfyUI search box



### 

​

Added nodes follow the cursor

  * **Default Value** : Enabled
  * **Function** : When enabled, a node added from the search box follows the pointer until you click to place it. Only applies to the default node search box implementation



## 

​

Node Widget

### 

​

Widget control mode

  * **Options** : before, after
  * **Default Value** : after
  * **Function** : Controls whether the timing of node widget value updates is before or after workflow execution, such as updating seed values



### 

​

Textarea widget spellcheck

  * **Default Value** : Disabled
  * **Function** : Controls whether text area widgets enable spellcheck, providing spellcheck functionality during text input. This functionality is implemented through the browser’s spellcheck attribute



## 

​

Notification Preferences

### 

​

Show version updates

  * **Default Value** : Enabled
  * **Function** : Shows notifications about new models and major new features in the interface



## 

​

Queue

### 

​

Queue history size

  * **Default Value** : 64
  * **Range** : 2 - 256
  * **Function** : Controls the queue history size recorded in the sidebar queue history panel. The larger the value, the more queue history is recorded. When the number is large, loading the page will also consume more memory



### 

​

Docked job history/queue panel

  * **Default Value** : Disabled in stable releases, enabled in nightly builds
  * **Function** : Replaces the floating job queue panel with the same job queue docked in the job history side panel. Disable it to return to the floating panel layout



## 

​

Queue Button

### 

​

Batch count limit

  * **Default Value** : 100
  * **Function** : Sets the maximum number of tasks added to the queue in a single click, preventing accidentally adding too many tasks to the queue



## 

​

Validation

### 

​

Validate workflows

  * **Default Value** : Disabled
  * **Function** : Ensures the structural and connection correctness of workflows. If enabled, the system will call `useWorkflowValidation().validateWorkflow()` to validate workflow data
  * **Validation Process** : The validation process includes two steps: 
    * Schema validation: Use Zod schemas to validate workflow structure
    * Link repair: Check and repair connection issues between nodes
  * **Error Handling** : When validation fails, error prompts will be displayed, but workflow loading will not be blocked



## 

​

Window

### 

​

Show confirmation when closing window

  * **Default Value** : Enabled
  * **Function** : When there are modified but unsaved workflows, controls whether to display confirmation when closing the browser window or tab, preventing accidental window closure that leads to loss of unsaved workflows



## 

​

Workflow

### 

​

Persist workflow state and restore on page (re)load

  * **Default Value** : Enabled
  * **Function** : Controls whether to restore workflow state on page (re)load, maintaining workflow content after page refresh



### 

​

Auto Save

  * **Default Value** : off
  * **Function** : Controls the auto-save behavior of workflows, automatically saving workflow changes to avoid data loss



### 

​

Auto Save Delay (ms)

  * **Default Value** : 1000
  * **Function** : Sets the delay time for auto-save, only effective when auto-save is set to “after delay”



### 

​

Show confirmation when deleting workflows

  * **Default Value** : Enabled
  * **Function** : Controls whether to display a confirmation dialog when deleting workflows in the sidebar, preventing accidental deletion of important workflows



### 

​

Save and restore canvas position and zoom level in workflows

  * **Default Value** : Enabled
  * **Function** : Controls whether to save and restore canvas position and zoom level in workflows, restoring the previous view state when reopening workflows



### 

​

Opened workflows position

  * **Options** : Sidebar, Topbar, Topbar (Second Row)
  * **Default Value** : Topbar
  * **Function** : Controls the display position of opened workflow tabs, currently only supports Sidebar, Topbar, Topbar (Second Row)



### 

​

Prompt for filename when saving workflow

  * **Default Value** : Enabled
  * **Function** : Controls whether to prompt for filename input when saving workflows, allowing users to customize workflow filenames



### 

​

Sort node IDs when saving workflow

  * **Default Value** : Disabled
  * **Function** : Determines whether to sort node IDs when saving workflows, making workflow file format more standardized and convenient for version control



### 

​

Require confirmation when clearing workflow

  * **Default Value** : Enabled
  * **Function** : Controls whether to display a confirmation dialog when clearing workflows, preventing accidental clearing of workflow content



### 

​

Enable node replacement suggestions

  * **Default Value** : Enabled
  * **Function** : Missing nodes with a known replacement are listed as replaceable in the missing nodes dialog, so you can review and apply the replacement instead of installing the original node pack



### 

​

Require confirmation to overwrite an existing subgraph blueprint

  * **Default Value** : Enabled
  * **Function** : Asks for confirmation before an existing subgraph blueprint is overwritten when you save a subgraph with the same name



### 

​

Restore widget values by name

  * **Default Value** : Disabled
  * **Function** : Loads widget values by widget name instead of by their position in the widget list. This is a transitional setting that is planned to become the default in a future release



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/settings/comfy.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/settings/comfy)

[ComfyUI Settings OverviewPrevious](https://docs.comfy.org/interface/settings/overview)[ComfyUI LiteGraph (Canvas) SettingsNext](https://docs.comfy.org/interface/settings/lite-graph)

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
