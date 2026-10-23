---
url: https://docs.comfy.org/custom-nodes/help_page/
title: Add node docs for your ComfyUI custom node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:37.560438+00:00
---

# Add node docs for your ComfyUI custom node - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/help_page/

## On this page

  * Node Documentation with Markdown
  * Setup
  * Supported Markdown Features
  * Example Structure
  * Example Markdown File



Package & Publish

# Add node docs for your ComfyUI custom node

Copy pageCopy page

How to create rich documentation for your custom nodes

Copy pageCopy page

## 

​

Node Documentation with Markdown

Custom nodes can include rich markdown documentation that will be displayed in the UI instead of the generic node description. This provides users with detailed information about your node’s functionality, parameters, and usage examples. If you have already added tooltips for each parameter in the node definition, this basic information can be directly accessed via the node documentation panel. No additional node documentation needs to be added, and you can refer to the related implementation of [ContextWindowsManualNode](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_context_windows.py#L7)

## 

​

Setup

To add documentation for your custom nodes or multi-language support documentation:

  1. Create a `docs` folder inside your `WEB_DIRECTORY`
  2. Add markdown files named after your nodes (the names of your nodes are the dictionary keys in the `NODE_CLASS_MAPPINGS` dictionary used to register the nodes): 
     * `WEB_DIRECTORY/docs/NodeName.md` \- Default documentation
     * `WEB_DIRECTORY/docs/NodeName/en.md` \- English documentation
     * `WEB_DIRECTORY/docs/NodeName/zh.md` \- Chinese documentation
     * Add other locales as needed (e.g., `fr.md`, `de.md`, etc.)

The system will automatically load the appropriate documentation based on the user’s locale, falling back to `NodeName.md` if a localized version is not available.

## 

​

Supported Markdown Features

  * Standard markdown syntax (headings, lists, code blocks, etc.)
  * Images using markdown syntax: `![alt text](image.png)`
  * HTML media elements with specific attributes: 
    * `<video>` and `<source>` tags
    * Allowed attributes: `controls`, `autoplay`, `loop`, `muted`, `preload`, `poster`



## 

​

Example Structure
    
    
    my-custom-node/
    ├── __init__.py
    ├── web/              # WEB_DIRECTORY
    │   ├── js/
    │   │   └── my-node.js
    │   └── docs/
    │       ├── MyNode.md           # Fallback documentation
    │       └── MyNode/
    │           ├── en.md           # English version
    │           └── zh.md           # Chinese version
    

## 

​

Example Markdown File
    
    
    # My Custom Node
    
    This node processes images using advanced algorithms.
    
    ## Parameters
    
    - **image**: Input image to process
    - **strength**: Processing strength (0.0 - 1.0)
    
    ## Usage
    
    ![example usage](https://docs.comfy.org/custom-nodes/help_page/example.png)
    
    <video controls loop muted>
      <source src="demo.mp4" type="video/mp4">
    </video>
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/help_page.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/help_page)

[Node replacementPrevious](https://docs.comfy.org/custom-nodes/backend/node-replacement)[Workflow templatesNext](https://docs.comfy.org/custom-nodes/workflow_templates)

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
