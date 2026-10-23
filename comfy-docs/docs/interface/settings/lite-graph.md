---
url: https://docs.comfy.org/interface/settings/lite-graph/
title: ComfyUI LiteGraph (Canvas) Settings - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:02.938037+00:00
---

# ComfyUI LiteGraph (Canvas) Settings - ComfyUI

> Source: https://docs.comfy.org/interface/settings/lite-graph/

## On this page

  * Canvas
    * Show selection toolbox
    * Live selection
    * Zoom node level of detail (font size threshold)
    * Maximum FPS
    * Always snap to grid
    * Snap to grid size
    * Enable fast-zoom shortcut (Ctrl + Shift + Drag)
    * Show graph canvas menu
    * Canvas zoom speed
    * Show canvas info on bottom left corner (fps, etc.)
    * Auto-pan speed
  * Canvas Navigation
    * Navigation Mode
    * Left Mouse Click Behavior
    * Mouse Wheel Scroll
  * Context Menu
    * Scale node combo widget menus (lists) when zoomed in
  * Graph
    * Link Render Mode
  * Group
    * Double click group title to edit
    * Group selected nodes padding
    * Select group children on click
  * Link
    * Link midpoint markers
  * Link Release
    * Action on link release (Shift)
    * Action on link release (No modifier)
  * Node
    * Always shrink new nodes
    * Enable DOM element clipping (enabling may reduce performance)
    * Middle-click creates a new Reroute node
    * Keep all links when deleting nodes
    * Snap highlights node
    * Auto snap link to node slot
    * Enable Tooltips
    * Tooltip Delay
    * Node life cycle badge mode
    * Node ID badge mode
    * Node source badge mode
    * Double click node title to edit
  * Node Widget
    * Float widget rounding decimal places [0 = auto]
    * Disable default float widget rounding
    * Disable node widget sliders
    * Always show advanced widgets on all nodes
    * Preview image format
    * Show width × height below the image preview
  * Pointer
    * Enable trackpad gestures
    * Double click interval (maximum)
    * Pointer click drift (maximum distance)
  * Reroute
    * Reroute spline offset



ComfyUI Settings

# ComfyUI LiteGraph (Canvas) Settings

Copy pageCopy page

Detailed description of ComfyUI graphics rendering engine LiteGraph setting options

Copy pageCopy page

The settings described on this page are located in the **ComfyUI in-app settings menu**. You can open it by navigating to **Settings** (gear icon) or using the `Ctrl + ,` keyboard shortcut, then select the corresponding category to view and configure these options.

LiteGraph is the underlying graphics rendering engine of ComfyUI. The settings in this category mainly control the behavior and appearance of graphical interfaces such as canvas, nodes, and links.

## 

​

Canvas

### 

​

Show selection toolbox

  * **Default Value** : Enabled
  * **Function** : The selection toolbox is a floating quick action toolbar that appears on nodes after they are selected, providing common quick operations such as partial execution, pinning, deletion, color modification, etc.

![Show selection toolbox](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/lite-graph/selection-toolbox.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=477b7ea42f5c0d270240538fad73c60f)

### 

​

Live selection

  * **Default Value** : Enabled
  * **Function** : When enabled, nodes are selected and deselected in real time while you drag a selection rectangle, similar to other design tools



### 

​

Zoom node level of detail (font size threshold)

  * **Default Value** : 8
  * **Range** : 0 - 24
  * **Function** : Sets when nodes switch to simplified level of detail rendering while you zoom out, measured as a minimum font size in pixels. Higher values switch nodes to simplified rendering sooner, lower values keep full node quality longer, and 0 disables level of detail switching entirely. The different rendering modes are shown below

![Low quality rendering](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/lite-graph/render-mode.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=cd5b2cb2c03dc6ef09eb42350358f5b9)

### 

​

Maximum FPS

  * **Default Value** : 0 (use screen refresh rate)
  * **Range** : 0 - 120
  * **Function** : Limits the rendering frame rate of the canvas. 0 means using the screen refresh rate. Higher FPS will make the canvas rendering smoother, but will also consume more performance. Too low values will cause more obvious stuttering.



### 

​

Always snap to grid

  * **Default Value** : Disabled
  * **Function** : When this option is not enabled, you can hold the `Shift` key to align node edges with the grid. When enabled, node edges will automatically align with the grid without holding the `Shift` key.



### 

​

Snap to grid size

  * **Default Value** : 10
  * **Range** : 1 - 500
  * **Function** : When auto-snap is enabled or when moving nodes while holding the `Shift` key, this parameter determines the grid size for snapping. The default value is 10, and you can adjust it according to your needs.



### 

​

Enable fast-zoom shortcut (Ctrl + Shift + Drag)

  * **Default Value** : Enabled
  * **Function** : Enables the `Ctrl + Shift + Left Mouse Button Drag` fast zoom function, providing a faster zoom operation method



### 

​

Show graph canvas menu

  * **Default Value** : Enabled
  * **Function** : Controls whether to display the canvas menu in the bottom right corner

The canvas menu is located in the bottom right corner of the entire ComfyUI interface, containing operations such as canvas zooming, temporarily hiding all connections, quickly scaling the workflow to fit the canvas, etc., as shown in the image below ![Show graph canvas menu](https://mintcdn.com/dripart/A0ohfUGOp7aobXHn/images/interface/setting/lite-graph/canvas_menu.jpg?fit=max&auto=format&n=A0ohfUGOp7aobXHn&q=85&s=d4ae22081d9b4ecf741867f749360f6c)

### 

​

Canvas zoom speed

  * **Default Value** : 1.1
  * **Range** : 1.01 - 2.5
  * **Function** : Controls the speed of canvas zooming, adjusts the sensitivity of mouse wheel zooming



### 

​

Show canvas info on bottom left corner (fps, etc.)

  * **Default Value** : Enabled
  * **Function** : Controls whether to display canvas information in the bottom left corner, showing performance metrics like FPS

![Canvas info](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/lite-graph/canvas-info.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=7ecbaf0b57b8ab66d8df31779e5f5926)

### 

​

Auto-pan speed

  * **Default Value** : 15
  * **Range** : 0 - 30
  * **Function** : Sets the maximum speed used when the canvas pans automatically as you drag a node or a link against the canvas edge. Set it to 0 to disable auto-panning



## 

​

Canvas Navigation

### 

​

Navigation Mode

  * **Default Value** : Drag Navigation
  * **Options** : Standard (New), Drag Navigation, Custom
  * **Function** : Selects a preset for the two canvas navigation behaviors below. Standard (New) selects with the left mouse button and pans with the mouse wheel, Drag Navigation (the default) pans with the left mouse button and zooms with the mouse wheel, and Custom keeps whatever you set for each behavior individually. Changing either behavior away from its preset switches this setting to Custom



### 

​

Left Mouse Click Behavior

  * **Default Value** : Panning
  * **Options** : Panning, Select
  * **Function** : Sets what dragging with the left mouse button on an empty part of the canvas does: pan the canvas or draw a selection rectangle



### 

​

Mouse Wheel Scroll

  * **Default Value** : Zoom in/out
  * **Options** : Panning, Zoom in/out
  * **Function** : Sets what the mouse wheel does on the canvas: zoom in and out, or pan vertically



## 

​

Context Menu

### 

​

Scale node combo widget menus (lists) when zoomed in

  * **Default Value** : Disabled
  * **Function** : Controls whether to scale node combo widget menus (lists) when zoomed in, allowing users to select node combo widgets



## 

​

Graph

### 

​

Link Render Mode

  * **Default Value** : 2 (Spline)
  * **Options** : Straight, Linear, Spline, Hidden
  * **Function** : Sets the rendering style of connections, controlling the visual style of links between nodes

![Link Render Mode](https://mintcdn.com/dripart/EeFKEryMLH5667kk/images/interface/setting/lite-graph/link-render-mode.jpg?fit=max&auto=format&n=EeFKEryMLH5667kk&q=85&s=7e84452d1f5a5a71def87b3d27c95462)

## 

​

Group

This section of settings is mainly related to node group functionality ![Node Group](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=02765d28e1720e5cc0bc2f6a1f70ab02)

### 

​

Double click group title to edit

  * **Default Value** : Enabled
  * **Function** : Controls whether you can double-click the node title to edit it, allowing users to rename nodes, marked as part `1` in the image



### 

​

Group selected nodes padding

  * **Default Value** : 10
  * **Range** : 0 - 100
  * **Function** : Sets the inner padding when grouping selected nodes, controlling the spacing between the group frame and nodes, marked as the arrow annotation part `2` in the image



### 

​

Select group children on click

  * **Default Value** : Disabled
  * **Function** : When enabled, clicking a group selects all nodes and items inside it



## 

​

Link

### 

​

Link midpoint markers

  * **Default Value** : Circle
  * **Options** : None, Circle, Arrow
  * **Function** : Sets the marker style at link midpoints, displaying direction indicators at link midpoints

![Link midpoint markers](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/setting/lite-graph/link-midpoint.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=8657ef27abace2e70e48f25300bde988)

## 

​

Link Release

This menu section currently mainly controls related operations when link connections are released. The current two related operations are: **A node recommendation list related to the current input/output will appear after release** **A search box will be launched after release**

### 

​

Action on link release (Shift)

  * **Default Value** : search box
  * **Options** : context menu, search box, no action
  * **Function** : Sets the action when releasing links while holding the Shift key, special behavior when releasing links while holding Shift



### 

​

Action on link release (No modifier)

  * **Default Value** : context menu
  * **Options** : context menu, search box, no action
  * **Function** : Sets the default action when releasing links, controls the behavior after dragging and releasing links



## 

​

Node

### 

​

Always shrink new nodes

  * **Default Value** : Disabled
  * **Function** : Controls whether to automatically shrink when creating new nodes, so nodes can always display the minimum size, but may cause some text display to be truncated when adding, requiring manual adjustment of node size



### 

​

Enable DOM element clipping (enabling may reduce performance)

  * **Default Value** : Enabled
  * **Function** : Enables DOM element clipping (may affect performance), optimizes rendering but may reduce performance



### 

​

Middle-click creates a new Reroute node

  * **Default Value** : Enabled
  * **Function** : Creates a new reroute node when middle-clicking, quickly creates reroute nodes for organizing connections



### 

​

Keep all links when deleting nodes

  * **Default Value** : Enabled
  * **Function** : Automatically bypasses connections when deleting intermediate nodes, attempts to reconnect input and output links when deleting nodes



### 

​

Snap highlights node

  * **Default Value** : Enabled
  * **Function** : Highlights nodes when dragging links to them, provides visual feedback, shows connectable nodes. When enabled, the effect is as shown in the image below, the corresponding side of the link will display highlighted style

![Snap highlights node](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=242f3b88d95229d99744f720cf86c935)

### 

​

Auto snap link to node slot

  * **Default Value** : Enabled
  * **Function** : Automatically snaps to available slots when dragging links to nodes, simplifies connection operations, automatically finds suitable input slots



### 

​

Enable Tooltips

  * **Default Value** : Enabled
  * **Function** : Some node information will contain tooltips, including parameter descriptions, etc. When enabled, these tooltips will be displayed when hovering the mouse, as shown in the image below

![Enable Tooltips](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=df329458465d6f20efea955e638c9656)

### 

​

Tooltip Delay

  * **Default Value** : 500
  * **Range** : 100 - 3000
  * **Function** : Controls the delay before a tooltip appears, in milliseconds



### 

​

Node life cycle badge mode

  * **Default Value** : Show all
  * **Function** : Controls the display of node lifecycle markers, showing node status information



### 

​

Node ID badge mode

  * **Default Value** : None
  * **Function** : Controls the display of node ID markers, showing node unique identifiers

![Node ID badge mode](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ca8e1edfff6c7673f1432ba0ac2edde5)

### 

​

Node source badge mode

  * **Default Value** : Hide built-in
  * **Options** : 
    * None
    * Hide built-in
    * Show all
  * **Function** : Controls the display mode of node source markers, showing node source information. The corresponding display effect is shown in the image below. If show all is selected, it will display labels for both custom nodes and built-in nodes, making it convenient for you to determine the corresponding node source. The corresponding fox logo represents ComfyUI built-in nodes

![Node source badge mode](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=383afc337b63f52be2f8d3cb9e7c4ed7)

### 

​

Double click node title to edit

  * **Default Value** : Enabled
  * **Function** : Controls whether you can double-click the node title to edit it, allowing users to rename nodes



## 

​

Node Widget

### 

​

Float widget rounding decimal places [0 = auto]

  * **Default Value** : 0 (auto)
  * **Range** : 0 - 6
  * **Function** : Sets the decimal places for float widget rounding, 0 means auto, requires page reload



### 

​

Disable default float widget rounding

  * **Default Value** : Disabled
  * **Function** : Controls whether to disable default float widget rounding, requires page reload, cannot be disabled when the node backend has set rounding



### 

​

Disable node widget sliders

  * **Default Value** : Disabled
  * **Function** : Controls whether to disable slider controls in node widgets, forcing text input instead of sliders



### 

​

Always show advanced widgets on all nodes

  * **Default Value** : Disabled
  * **Function** : When enabled, advanced widgets are always visible on all nodes without expanding each node individually



### 

​

Preview image format

  * **Default Value** : Empty string (use original format)
  * **Function** : Sets the format for preview images in image widgets, converts to lightweight formats like webp, jpeg, etc.



### 

​

Show width × height below the image preview

  * **Default Value** : Enabled
  * **Function** : Displays width × height information below image previews, showing image dimension information

![Show width × height below the image preview](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e7fdfd5227158a413b5b0051a6e171bf)

## 

​

Pointer

### 

​

Enable trackpad gestures

  * **Default Value** : Enabled
  * **Function** : This setting enables trackpad mode for the canvas, allowing two-finger pinch zoom and drag.



### 

​

Double click interval (maximum)

  * **Default Value** : 300
  * **Function** : Maximum time (milliseconds) between two clicks of a double-click. Increasing this value helps solve issues where double-clicks are sometimes not recognized.



### 

​

Pointer click drift (maximum distance)

  * **Default Value** : 6
  * **Function** : If the pointer moves more than this distance while holding the button, it is considered a drag (rather than a click). Helps prevent accidental mouse movement when clicking.



## 

​

Reroute

### 

​

Reroute spline offset

  * **Default Value** : 20
  * **Function** : Used to determine the smoothness of curves on both sides of reroute nodes. Larger values make curves smoother, smaller values make curves sharper.

![Reroute spline offset](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a76bc935bc5e37fe1b3c99129c7b5fe3)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/settings/lite-graph.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/settings/lite-graph)

[Comfy SettingsPrevious](https://docs.comfy.org/interface/settings/comfy)[Customizing ComfyUI AppearanceNext](https://docs.comfy.org/interface/appearance)

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
