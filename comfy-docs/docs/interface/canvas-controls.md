---
url: https://docs.comfy.org/interface/canvas-controls/
title: Canvas Controls - Minimap, Zoom, and Focus Mode - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:00.925078+00:00
---

# Canvas Controls - Minimap, Zoom, and Focus Mode - ComfyUI

> Source: https://docs.comfy.org/interface/canvas-controls/

## On this page

  * Canvas toolbar
  * View menu
  * Focus Mode
  * Minimap options
  * Links and canvas globals
  * Related pages



Canvas

# Canvas Controls - Minimap, Zoom, and Focus Mode

Copy pageCopy page

Use ComfyUI canvas controls and the View menu for minimap, link visibility, canvas info, zoom, fit view, Select/Hand modes, and Focus Mode.

Copy pageCopy page

The bottom-right canvas toolbar and the **View** menu control how you move around the graph. Core View commands include toggle bottom panel, browse templates, **Focus Mode** , canvas performance info, minimap, link visibility, zoom in/out, and fit view. ![The bottom-right canvas toolbar with the minimap open](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/canvas-controls/canvas_toolbar.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=cd8c2ef1bdec81bd8c730b3a3c0159a4) ![Focus Mode on: the workspace chrome is hidden and a hamburger control is shown](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/canvas-controls/canvas_focus_mode.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=fe9f3b0f77c39731e2d77a5147c16b2d) ![Link visibility on: the connected nodes are joined by wires](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/canvas-controls/canvas_links_visible.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=4e20906792a1924523e3da25bdd920ac) ![Link visibility off: the nodes stay on the canvas but the connection wires are hidden](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/canvas-controls/canvas_links_hidden.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=2fb86dd45ba7907910bfdc0cfcf4e3b9)

## 

​

Canvas toolbar

When **Show graph canvas menu** (`Comfy.Graph.CanvasMenu`) is on (default), a floating toolbar sits at the bottom-right of the canvas:

Control| What it does  
---|---  
**Canvas mode**|  Menu to switch between **Select** (edit nodes) and **Hand** (pan-only / read-only canvas). Defaults: `v` unlocks Select, `h` locks Hand.  
**Fit view**|  Frames the graph in the viewport (`Comfy.Canvas.FitView`, default `.`).  
**Zoom**|  Opens a popover with Zoom in, Zoom out, Zoom to fit, and a percentage field (1-1000%). Default shortcuts include `Alt` \+ `=` / `Alt` \+ `-` for zoom in/out.  
**Minimap**|  Toggles the overview map (`Comfy.Canvas.ToggleMinimap`, default `Alt` \+ `Shift` \+ `M`). Persisted as `Comfy.Minimap.Visible`.  
**Link visibility**|  Hides or shows connection wires by toggling hidden link render mode (`Comfy.Canvas.ToggleLinkVisibility`).  
  
You can hide the whole toolbar with **Show graph canvas menu** in Lite Graph / Canvas settings.

## 

​

View menu

The **View** menu registers the same navigation commands so you can run them from the menu bar or the command palette:

  * Toggle Bottom Panel
  * Browse Templates
  * Focus Mode
  * Canvas Performance (`Comfy.ToggleCanvasInfo`, toggles `Comfy.Graph.CanvasInfo`)
  * Toggle Minimap
  * Toggle Link Visibility
  * Zoom In / Zoom Out / Fit View



## 

​

Focus Mode

**Focus Mode** (`Workspace.ToggleFocusMode`) hides workspace chrome so you can concentrate on the graph. While it is on:

  * The top menu section is hidden (new menu).
  * Left/right sidebar panels and the bottom panel are not rendered in the splitter layout.
  * A hamburger control appears so you can exit Focus Mode (**Show menu**).

Toggle Focus Mode again, or use the hamburger control, to restore the full workspace.

## 

​

Minimap options

Beyond show/hide, Settings under Minimap control what the map draws (node colors, links, groups, bypass state, error state). See [Lite Graph settings](https://docs.comfy.org/interface/settings/lite-graph) and related Appearance entries when present.

## 

​

Links and canvas globals

Link shape and whether connected links are shown are also available as quick toggles in the [Right Side Panel](https://docs.comfy.org/interface/right-side-panel) **Global Settings** when nothing is selected, and in full under Lite Graph settings (`Comfy.LinkRenderMode` and related options). Grid spacing and snap-to-grid live in the same Global Settings / Lite Graph areas.

## 

​

Related pages

  * [Interface Overview](https://docs.comfy.org/interface/overview)
  * [Shortcuts](https://docs.comfy.org/interface/shortcuts)
  * [Lite Graph settings](https://docs.comfy.org/interface/settings/lite-graph)
  * [Right Side Panel](https://docs.comfy.org/interface/right-side-panel) (Global Settings quick toggles)
  * [Bottom Panel](https://docs.comfy.org/interface/bottom-panel)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/canvas-controls.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/canvas-controls)

[Right Side Panel: Node Properties and ErrorsPrevious](https://docs.comfy.org/interface/right-side-panel)[ComfyUI Nodes 2.0Next](https://docs.comfy.org/interface/nodes-2)

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
