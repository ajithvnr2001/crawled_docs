---
url: https://docs.comfy.org/development/comfyui-server/comms_overview/
title: ComfyUI Server Overview: REST and WebSocket APIs - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:58.197355+00:00
---

# ComfyUI Server Overview: REST and WebSocket APIs - ComfyUI

> Source: https://docs.comfy.org/development/comfyui-server/comms_overview/

## On this page

Back to top

  * Starting the Server
  * Key Pages in This Section
  * Using Partner Nodes
  * How the Server Works



Self-Hosted Server API

# ComfyUI Server Overview: REST and WebSocket APIs

Copy pageCopy page

Run ComfyUI as a headless HTTP server, then submit workflows, upload files, download outputs, and monitor progress over its REST and WebSocket APIs.

Copy pageCopy page

ComfyUI runs as an HTTP server on your machine by default. You can call it programmatically to submit workflows, upload files, download outputs, and monitor progress — all without opening the browser.

## Starting the Server

When you launch ComfyUI, it automatically starts an HTTP server at `http://127.0.0.1:8188`. To run ComfyUI as a headless server (no browser):
    
    
    # Run without opening the browser
    python main.py --disable-auto-launch
    
    
    
    # Specify a custom port
    python main.py --port 8288
    
    
    
    # Listen on all network interfaces (for remote access)
    python main.py --listen 0.0.0.0
    

For a full list of startup flags, run `python main.py --help` or see the [Startup Flags reference](https://docs.comfy.org/development/comfyui-server/startup-flags).

## Key Pages in This Section

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

## Using Partner Nodes

If your workflow contains paid Partner Nodes, you can include your API key in the payload. See the [Partner Node API Integration](https://docs.comfy.org/development/comfyui-server/api-key-integration) guide for details.

* * *

## How the Server Works

The Comfy server runs on top of the [aiohttp framework](https://docs.aiohttp.org/), which in turn uses [asyncio](https://pypi.org/project/asyncio/). Messages from the server to the client are sent by socket messages through the `send_sync` method of the server, which is an instance of `PromptServer` (defined in `server.py`). They are processed by a socket event listener registered in `api.js`. See [messages](https://docs.comfy.org/development/comfyui-server/comms_messages). Messages from the client to the server are sent by the `api.fetchApi()` method defined in `api.js`, and are handled by HTTP routes defined by the server. See [routes](https://docs.comfy.org/development/comfyui-server/comms_routes).

The client submits the whole workflow (widget values and all) when you queue a request. The server does not receive any changes you make after you send a request to the queue. If you want to modify server behavior during execution, you’ll need routes.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfyui-server/comms_overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfyui-server/comms_overview)

[Hosting options](https://docs.comfy.org/development/deploy/self-hosting)[API examples](https://docs.comfy.org/development/comfyui-server/api-examples)
