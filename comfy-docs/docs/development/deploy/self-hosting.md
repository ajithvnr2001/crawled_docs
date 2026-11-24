---
url: https://docs.comfy.org/development/deploy/self-hosting/
title: Self-Hosting ComfyUI: Bare Metal, GPU Cloud, and Docker - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:37.014593+00:00
---

# Self-Hosting ComfyUI: Bare Metal, GPU Cloud, and Docker - ComfyUI

> Source: https://docs.comfy.org/development/deploy/self-hosting/

## On this page

Back to top

  * Your own hardware
  * GPU cloud providers
  * Community Docker images
  * Next step: run workflows against it



Self-Hosting

# Self-Hosting ComfyUI: Bare Metal, GPU Cloud, and Docker

Copy pageCopy page

Run ComfyUI yourself and call it as an API: your own hardware, rented GPU pods from Runpod or Vast.ai, or community Docker images.

Copy pageCopy page

Self-hosting means running ComfyUI yourself and calling it as an API. You manage the hardware, the models, and the custom nodes, and in return you get full control: any GPU, any model, any node pack, and your data never leaves your infrastructure. ComfyUI runs as an HTTP server by default, so any working install is already an API endpoint. The options below differ only in where that install lives.

## Your own hardware

The simplest deployment is the machine in front of you. Install ComfyUI and it serves `http://127.0.0.1:8188` out of the box:

  * [Manual install](https://docs.comfy.org/installation/manual_install) for Linux, macOS, and Windows, and the standard choice for servers
  * [Comfy Desktop](https://docs.comfy.org/installation/desktop/overview) or the [portable Windows build](https://docs.comfy.org/installation/comfyui_portable_windows) for local development

To run it headless (no browser) or listen on a non-default address, see the [server startup flags](https://docs.comfy.org/development/comfyui-server/startup-flags). For example:
    
    
    python main.py --listen 0.0.0.0 --port 8188
    

The ComfyUI server has no authentication by default. Only bind to a non-loopback address on a network you trust, or put a reverse proxy with authentication in front of it.

## GPU cloud providers

If you do not own a GPU, you can rent one and run ComfyUI on it. Providers commonly used by the community include:

  * **[Runpod](https://www.runpod.io)** : GPU pods with community ComfyUI templates that come pre-configured.
  * **[Vast.ai](https://vast.ai)** : a GPU marketplace; community ComfyUI templates are available here too.

On these providers you typically start from a community template or image, then add your models and custom nodes. The result is a normal self-hosted ComfyUI with a public URL or an SSH tunnel in front of it.

These templates are community-maintained, not published or supported by the ComfyUI team. Review what a template installs before putting credentials or private models on it.

If you want a managed version of this workflow, follow [Custom Builds](https://docs.comfy.org/development/deploy/cloud-custom-builds) to build and deploy it on Comfy Cloud.

## Community Docker images

**Docker:** ComfyUI does not provide an official Docker image. If you want to run ComfyUI in a container, you can use community-maintained images from [Docker Hub](https://hub.docker.com/search?q=comfyui). These images are **not officially maintained by Comfy-Org** and are not supported by the ComfyUI team. Use them at your own risk.

A containerized ComfyUI behaves like any other self-hosted install: expose the server port and call it as usual.

## Next step: run workflows against it

A self-hosted deployment can be called in two ways:

## Comfy SDKs + API Proxy

Use the official SDKs against your instance. The API Proxy, a small service that runs alongside ComfyUI, serves Comfy API v2.

## ComfyUI Server API

Call the raw REST and WebSocket API directly, with no extra service. Full local surface, but no compatibility guarantee across releases.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/deploy/self-hosting.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/deploy/self-hosting)

[Usage and Limits](https://docs.comfy.org/development/deploy/cloud-usage)[Hosting options](https://docs.comfy.org/development/deploy/self-hosting)
