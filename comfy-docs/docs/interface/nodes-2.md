---
url: https://docs.comfy.org/interface/nodes-2/
title: ComfyUI Nodes 2.0 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:02.259416+00:00
---

# ComfyUI Nodes 2.0 - ComfyUI

> Source: https://docs.comfy.org/interface/nodes-2/

## On this page

  * Why this change?
  * Current status and known issues
  * How to try it
    * Enable Nodes 2.0
    * What to test
  * How to provide feedback
  * Switching back



Canvas

# ComfyUI Nodes 2.0

Copy pageCopy page

Nodes 2.0 moves ComfyUI node rendering from LiteGraph Canvas to a Vue-based system for faster iteration: what changed and how to enable it.

Copy pageCopy page

Nodes 2.0 is now available in Comfy Desktop, portable, and stable releases. This update transitions the node system from LiteGraph.js Canvas rendering to a Vue-based architecture, unlocking faster iteration and richer interactions.

## 

​

Why this change?

The previous Canvas rendering system had become a development bottleneck. Even small UI changes often required deep modifications and could take days to implement. This slowed the ability to respond to community feedback and made node customization difficult for developers. The new Vue-based system enables:

  * **Faster feature development** \- UI changes can be implemented more quickly
  * **Richer interactions** \- Dynamic widgets, expandable nodes, and better components
  * **A more flexible foundation** \- Better support for future tools and customization



## 

​

Current status and known issues

We’re actively working on improvements and want to be transparent about current limitations:

Area| Status  
---|---  
**Performance**|  Still optimizing toward Canvas-level performance. Certain scenarios may behave differently.  
**Compatibility**|  Some custom nodes may require updates to be fully supported.  
**Edge cases**|  At extreme zoom levels or within very large workflows, minor visual issues may appear.  
  
We’re gathering feedback to prioritize improvements. The LiteGraph.js rendering system remains available, and you can toggle between systems at any time.

## 

​

How to try it

### 

​

Enable Nodes 2.0

  1. Visit [cloud.comfy.org](https://cloud.comfy.org) or update to the latest version of Comfy Desktop, portable, or stable release
  2. Click **Try it out** on the top banner when you launch ComfyUI



### 

​

What to test

Use Nodes 2.0 in your daily workflows and share feedback with us:

  * **Basic interactions** \- Dragging, resizing, selecting
  * **Daily workflows** \- Execution, parameters, custom nodes
  * **Performance** \- Especially with complex workflows



## 

​

How to provide feedback

Encountered issues or have suggestions for interaction improvements?

  * **Support center** \- [ComfyUI Help Center](https://support.comfy.org)
  * **GitHub issues** \- [Create an issue in ComfyUI_frontend](https://github.com/Comfy-Org/ComfyUI_frontend/issues)



Including reproduction steps, screenshots, and system info is extremely helpful when reporting issues.

## 

​

Switching back

If you encounter issues:

  1. Click on the **ComfyUI logo** to open the menu
  2. Toggle **Nodes 2.0** to switch back to the previous interface

![Nodes 2.0 toggle location in ComfyUI menu](https://mintcdn.com/dripart/qbw4z6UfFGJ-L3Cc/images/interface/nodes_2.0.jpg?fit=max&auto=format&n=qbw4z6UfFGJ-L3Cc&q=85&s=859a3a5b4faefd96adb24044ced72f72) Your feedback helps us prioritize improvements. Enable Nodes 2.0 in settings and start exploring the new node design!

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/nodes-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/nodes-2)

[Canvas Controls - Minimap, Zoom, and Focus ModePrevious](https://docs.comfy.org/interface/canvas-controls)[Bottom Panel - Shortcuts, Logs, and TerminalNext](https://docs.comfy.org/interface/bottom-panel)

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
