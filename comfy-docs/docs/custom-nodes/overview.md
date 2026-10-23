---
url: https://docs.comfy.org/custom-nodes/overview/
title: ComfyUI Custom Node Types and Architecture - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:40.612462+00:00
---

# ComfyUI Custom Node Types and Architecture - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/overview/

## On this page

  * Client-Server Model
    * Server side only
    * Client side only
    * Independent Client and Server
    * Connected Client and Server
  * Next Steps



Build Custom Nodes

# ComfyUI Custom Node Types and Architecture

Copy pageCopy page

Learn how ComfyUI custom nodes work, the client-server model, and the four node categories: server side only, client side only, independent, and connected.

Copy pageCopy page

Custom nodes allow you to implement new features and share them with the wider community. A custom node is like any Comfy node: it takes input, does something to it, and produces an output. While some custom nodes perform highly complex tasks, many just do one thing. Here’s an example of a simple node that takes an image and inverts it. ![Unique Images Node](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=8088073e29e8af1bc700937ecb3b77e9) Custom node examples：

  * [cookiecutter-comfy-extension](https://github.com/Comfy-Org/cookiecutter-comfy-extension)
  * [ComfyUI-React-Extension-Template](https://github.com/Comfy-Org/ComfyUI-React-Extension-Template)
  * [ComfyUI_frontend_vue_basic](https://github.com/jtydhr88/ComfyUI_frontend_vue_basic)

If you use Claude Code for development, the [ComfyUI Custom Node Skills](https://github.com/jtydhr88/comfyui-custom-node-skills) provide Claude with comprehensive knowledge of the ComfyUI node system, covering both the V3 and V1 APIs. Install it from the Claude Code marketplace or add the repository URL to get 9 skills covering node basics, inputs, outputs, datatypes, advanced patterns, frontend extensions, and packaging.

## 

​

Client-Server Model

Comfy runs in a client-server model. The server, written in Python, handles all the real work: data-processing, models, image diffusion etc. The client, written in Javascript, handles the user interface. Comfy can also be used in API mode, in which a workflow is sent to the server by a non-Comfy client (such as another UI, or a command line script). Custom nodes can be placed into one of four categories:

### 

​

Server side only

The majority of Custom Nodes run purely on the server side, by defining a Python class that specifies the input and output types, and provides a function that can be called to process inputs and produce an output.

### 

​

Client side only

A few Custom Nodes provide a modification to the client UI, but do not add core functionality. Despite the name, they may not even add new nodes to the system.

### 

​

Independent Client and Server

Custom nodes may provide additional server features, and additional (related) UI features (such as a new widget to deal with a new data type). In most cases, communication between the client and server can be handled by the Comfy data flow control.

### 

​

Connected Client and Server

In a small number of cases, the UI features and the server need to interact with each other directly.

Any node that requires Client-Server communication will not be compatible with use through the API.

## 

​

Next Steps

## Getting Started

Build and register a working custom node, step by step.

## Python (Backend)

The node class contract: properties, inputs, return types.

## JavaScript (UI)

Extend the ComfyUI frontend from your node package.

## Package & Publish

Ship your node to the Comfy Registry.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/overview)

[Custom NodesPrevious](https://docs.comfy.org/custom-nodes/intro)[Creating Custom Nodes in ComfyUINext](https://docs.comfy.org/custom-nodes/walkthrough)

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
