---
url: https://docs.comfy.org/development/run-workflows/overview/
title: Running Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:55.993080+00:00
---

# Running Workflows - ComfyUI

> Source: https://docs.comfy.org/development/run-workflows/overview/

## On this page

  * Start here: the Comfy SDKs
  * What works against what
  * Which API should I use?
  * Getting started
  * Prerequisites



Run Workflows

# Running Workflows

Copy pageCopy page

How to run ComfyUI workflows against a live deployment, and which client works with which deployment

Copy pageCopy page

Once ComfyUI is [deployed somewhere](https://docs.comfy.org/development/deploy/overview), your application runs workflows against it: submit a workflow, wait for execution, download the outputs. This page maps out which client to use for which deployment.

## 

​

Start here: the Comfy SDKs

For a new integration, use the official **Comfy SDKs** (Python and TypeScript) and the [Comfy API v2](https://docs.comfy.org/api-reference/v2/overview) they call. The same code runs against every deployment target; only the base URL changes.

## Comfy SDKs

Install an SDK to submit workflows and download outputs from Python or TypeScript.

## 

​

What works against what

Deployment| Comfy SDKs / API v2| Notes  
---|---|---  
**Comfy API deployment**|  Yes| Point `COMFY_BASE_URL` at `https://<deployment>.run.comfy.app` with your API key  
**Comfy Cloud**|  Yes| The default base URL. Requires an API key and a paid subscription  
**Self-hosted**|  Yes, via the [API Proxy](https://docs.comfy.org/development/comfyui-server/api-proxy)| A small service alongside ComfyUI serves the v2 API  
  
Self-hosted instances can also skip the SDK entirely and use the raw [ComfyUI Server API](https://docs.comfy.org/development/comfyui-server/comms_overview) (REST + WebSocket). It exposes the full local surface, including the queue and node info, but has no compatibility guarantee across releases.

## 

​

Which API should I use?

| Comfy API v2 + SDKs| v1 Cloud API| ComfyUI Server API  
---|---|---|---  
**Where it runs**|  Comfy API deployments, Comfy Cloud, or self-hosted via the API Proxy| Comfy Cloud only| Self-hosted only  
**Compatibility**|  Versioned, additive changes only within v2| Deprecated, may change without notice| No guarantee across releases  
**Authentication**| `Authorization: Bearer` on Comfy Cloud and Comfy API deployments. Self-hosted: none by default, optional static bearer token| `X-API-Key` header (Comfy Cloud account)| None (local) or API key for Partner Nodes  
**Official clients**|  Python and TypeScript SDKs| None, call over HTTP| None, call over HTTP  
**Protocol**|  REST + SSE| REST + WebSocket| REST + WebSocket  
**Scope**|  Run a workflow and get results| Full Cloud surface, including models and account| Full local surface, including queue and node info  
**Best for**|  New integrations that should keep working| Existing integrations and Cloud features v2 does not cover yet| Full control, custom tooling against your own instance  
  
All of them accept the same workflow format ([API format](https://docs.comfy.org/development/api-development/workflow-api-format)), so you can develop and test workflows locally and move them to another deployment without changes.

## 

​

Getting started

## Comfy SDKs

Run workflows from Python or TypeScript, against any deployment target.

## API Proxy for Self-Hosted

Serve the v2 API in front of your own ComfyUI so the SDKs can reach it.

## Workflow API Format

Export workflows in the JSON format the APIs accept.

## ComfyUI Server API

The raw REST and WebSocket API of a self-hosted instance.

## 

​

Prerequisites

  * An [API key](https://docs.comfy.org/development/api-development/getting-an-api-key) for anything that touches Comfy Cloud, a Comfy API deployment, or Partner Nodes. A purely local ComfyUI does not need one.
  * A workflow exported in [API format](https://docs.comfy.org/development/api-development/workflow-api-format).



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/run-workflows/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/run-workflows/overview)

[ComfyUI Account API Key IntegrationPrevious](https://docs.comfy.org/development/comfyui-server/api-key-integration)[Run your first workflowNext](https://docs.comfy.org/development/api-development/quickstart)

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
