---
url: https://docs.comfy.org/interface/bottom-panel/
title: Bottom Panel - Shortcuts, Logs, and Terminal - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:02.621588+00:00
---

# Bottom Panel - Shortcuts, Logs, and Terminal - ComfyUI

> Source: https://docs.comfy.org/interface/bottom-panel/

## On this page

  * Opening the panel
  * Shortcuts tabs
  * Logs (self-hosted and Desktop)
  * Terminal (Desktop only)
  * Related pages



Bottom & help

# Bottom Panel - Shortcuts, Logs, and Terminal

Copy pageCopy page

The ComfyUI bottom panel hosts Shortcuts (Essentials and View Controls), runtime logs on non-Cloud builds, and a command terminal on Desktop only.

Copy pageCopy page

The bottom panel is a docked workspace strip under the canvas. It hosts keyboard shortcut reference tabs on every build, a **Logs** stream on self-hosted and Desktop builds, and a **Terminal** on the Desktop app only. Comfy Cloud does not register terminal tabs; Shortcuts still work. ![The bottom panel open on the Shortcuts tab, showing the Essentials list](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/bottom-panel/bottom_panel_shortcuts.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=9f77fbce04f73687e6be12b1b82a12d9) ![The Logs tab streaming runtime output from the ComfyUI process on a self-hosted install](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/bottom-panel/bottom_panel_logs.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=18ba948694f1bb8e6a75f43bfe657206)

## 

​

Opening the panel

You can open the bottom panel in several ways:

  * **Shortcuts** : click the keyboard icon near the bottom of the left sidebar (`Workspace.ToggleBottomPanel.Shortcuts`, default `Ctrl` \+ `Shift` \+ `K`). That toggles the shortcuts panel specifically.
  * **Console / terminal panel** (non-Cloud): click the terminal icon near the bottom of the left sidebar. That runs **Toggle Bottom Panel** , which prefers the terminal panel when Logs/Terminal tabs are loaded, otherwise falls back to Shortcuts.
  * **View** menu: **Bottom Panel** (`Workspace.ToggleBottomPanel`).
  * **Logs shortcut** (non-Cloud): default `Ctrl` \+ ``` toggles the Logs tab (`Workspace.ToggleBottomPanelTab.logs-terminal`).

The panel is hidden while [Focus Mode](https://docs.comfy.org/interface/canvas-controls) is on.

## 

​

Shortcuts tabs

Shortcuts register two tabs on the **shortcuts** panel:

  * **Essentials** : common editing and queue shortcuts.
  * **View Controls** : navigation and view-related shortcuts.

These panels mirror the same command/keybinding data you can customize under Settings → Keybinding. For the full editable list, see [Shortcuts](https://docs.comfy.org/interface/shortcuts).

## 

​

Logs (self-hosted and Desktop)

On non-Cloud builds, a **Logs** tab streams runtime log output from the ComfyUI process. Use it when debugging custom nodes, server errors, or backend messages without switching to an external terminal. Default shortcut: `Ctrl` \+ ```.

## 

​

Terminal (Desktop only)

On the **Desktop** app, a **Terminal** (command terminal) tab is registered next to Logs. It provides an in-app shell for Desktop users. It is not registered on pure browser self-hosted sessions or on Comfy Cloud. ![The Terminal tab on Desktop, showing an in-app shell next to Logs](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/bottom-panel/bottom_panel_terminal.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=90f43833f6f52001db479d6cac56f88e) Cloud builds skip both Logs and Terminal registration entirely; only Shortcuts remains.

## 

​

Related pages

  * [Shortcuts](https://docs.comfy.org/interface/shortcuts)
  * [Canvas Controls](https://docs.comfy.org/interface/canvas-controls) (Focus Mode hides this panel)
  * [Help Center](https://docs.comfy.org/interface/help-center)
  * [Interface Overview](https://docs.comfy.org/interface/overview)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/bottom-panel.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/bottom-panel)

[ComfyUI Nodes 2.0Previous](https://docs.comfy.org/interface/nodes-2)[ComfyUI Help Center: Release Notes, Support, and FeedbackNext](https://docs.comfy.org/interface/help-center)

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
