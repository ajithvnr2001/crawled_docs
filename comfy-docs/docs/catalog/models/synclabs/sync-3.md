---
url: https://docs.comfy.org/catalog/models/synclabs/sync-3/
title: Sync 3 video generation model (synclabs/sync-3): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:24.014042+00:00
---

# Sync 3 video generation model (synclabs/sync-3): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/synclabs/sync-3/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Workflow templates
  * Nodes
  * Pricing



Catalog

# Sync 3 video generation model (synclabs/sync-3): where to run it and pricing

Copy pageCopy page

Sync 3 is a video generation model from Sync.so. Run it with Comfy Router and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: synclabs/sync-3 Provider: synclabs Product: router, cloud, workflows, nodes Input: video, image, audio, text Output: video License: closed Sync 3 is a video generation model from Sync.so. It takes video, image, audio and text as input and produces video. It has no open weights. It runs on Sync.so’s servers, so you use it through Comfy Router and Partner Nodes in ComfyUI and Comfy Cloud.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Sync 3 with Comfy Router](https://docs.comfy.org/development/comfy-router/models/synclabs/sync-3/code)| You call `synclabs/sync-3` from your own code with `COMFY_API_KEY`  
Comfy Cloud| [Open `api_sync_so_lip_sync_video` on Comfy Cloud](https://cloud.comfy.org/?template=api_sync_so_lip_sync_video)| You want to run a ready-made workflow without installing anything  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/synclabs/sync-3`. Live request schema: `GET /v2/models/synclabs/sync-3/openapi.json`.



## Workflow templates

Template| Title| Added  
---|---|---  
`api_sync_so_lip_sync_video`| Sync 3: Video Lip-Sync| 2026-07-15  
`api_sync_so_talking_image`| Sync 3: Talking Image| 2026-07-15  
  
## Nodes

  * [SyncLipSyncNode](https://docs.comfy.org/built-in-nodes/SyncLipSyncNode)
  * [SyncTalkingImageNode](https://docs.comfy.org/built-in-nodes/SyncTalkingImageNode)



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/synclabs/sync-3/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/synclabs/sync-3`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/synclabs/sync-3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/synclabs/sync-3)
