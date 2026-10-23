---
url: https://docs.comfy.org/development/comfyui-server/comms_overview/
title: Server Overview - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:54.869010+00:00
---

# Server Overview - ComfyUI

> Source: https://docs.comfy.org/development/comfyui-server/comms_overview/

## On this page

  * Starting the Server
  * Key Pages in This Section
  * Using Partner Nodes
  * How the Server Works



Self-Hosted Server API

# Server Overview

Copy pageCopy page

Run ComfyUI as a server and interact with it programmatically via REST and WebSocket APIs

Copy pageCopy page

ComfyUI runs as an HTTP server on your machine by default. You can call it programmatically to submit workflows, upload files, download outputs, and monitor progress — all without opening the browser.

## 

​

Starting the Server

When you launch ComfyUI, it automatically starts an HTTP server at `http://127.0.0.1:8188`. To run ComfyUI as a headless server (no browser):
    
    
    # Run without opening the browser
    python main.py --disable-auto-launch
    
    
    
    # Specify a custom port
    python main.py --port 8288
    
    
    
    # Listen on all network interfaces (for remote access)
    python main.py --listen 0.0.0.0
    

For a full list of startup flags, run `python main.py --help` or see the [Startup Flags reference](https://docs.comfy.org/development/comfyui-server/startup-flags).

## 

​

Key Pages in This Section

## Startup Flags

Complete reference for all main.py command-line arguments.

## API Routes

Available HTTP endpoints for submitting workflows, uploading files, and querying status.

## API Examples

Code examples for calling the API: HTTP-only, WebSocket + History, and SaveImageWebsocket.

## Server Messages

WebSocket message types the server sends to the client during execution.

## Execution Model Inversion

Advanced: invert execution for custom control flows.

## 

​

Using Partner Nodes

If your workflow contains paid Partner Nodes, you can include your API key in the payload. See the [Partner Node API Integration](https://docs.comfy.org/development/comfyui-server/api-key-integration) guide for details.

* * *

## 

​

How the Server Works

The Comfy server runs on top of the [aiohttp framework](https://docs.aiohttp.org/), which in turn uses [asyncio](https://pypi.org/project/asyncio/). Messages from the server to the client are sent by socket messages through the `send_sync` method of the server, which is an instance of `PromptServer` (defined in `server.py`). They are processed by a socket event listener registered in `api.js`. See [messages](https://docs.comfy.org/development/comfyui-server/comms_messages). Messages from the client to the server are sent by the `api.fetchApi()` method defined in `api.js`, and are handled by HTTP routes defined by the server. See [routes](https://docs.comfy.org/development/comfyui-server/comms_routes).

The client submits the whole workflow (widget values and all) when you queue a request. The server does not receive any changes you make after you send a request to the queue. If you want to modify server behavior during execution, you’ll need routes.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfyui-server/comms_overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfyui-server/comms_overview)

[Self-Hosting OptionsPrevious](https://docs.comfy.org/development/deploy/self-hosting)[API ExamplesNext](https://docs.comfy.org/development/comfyui-server/api-examples)

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
