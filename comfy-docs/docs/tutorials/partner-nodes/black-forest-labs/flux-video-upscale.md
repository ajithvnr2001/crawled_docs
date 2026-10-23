---
url: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-video-upscale/
title: FLUX Video Upscale: AI video upscaling to 4K in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:26.722807+00:00
---

# FLUX Video Upscale: AI video upscaling to 4K in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-video-upscale/

## On this page

  * What FLUX Video Upscale is good at
  * Example outputs
  * Use it
  * FLUX Video Upscale workflow
  * Precise or creative mode
  * Prompt tips
  * Limits
  * Get started



Black Forest Labs

# FLUX Video Upscale: AI video upscaling to 4K in ComfyUI

Copy pageCopy page

Upscale video to 1080p, 2K, or 4K with the FLUX Video Upscale partner node in ComfyUI. Precise mode preserves the source; creative mode adds fine detail.

Copy pageCopy page

FLUX Video Upscale is Black Forest Labs’ FLUX 3 powered super-resolution tool for video, available in ComfyUI as a partner node. It upscales clips to 1080p, 2K, or 4K while keeping the source aspect ratio and its audio track.

## 

​

What FLUX Video Upscale is good at

  * **Upscale to 4K** : Raises video resolution to 1080p, 2K, or 4K in a single API call
  * **Two modes** : Precise mode preserves the source exactly; creative mode restores and invents fine detail
  * **Audio preserved** : The output keeps the source clip’s audio track
  * **Up to 20 seconds** : Accepts clips up to 20 seconds at up to 2560x1440 source resolution



## 

​

Example outputs

Upscaling an existing clip while keeping its aspect ratio and audio track:

## 

​

Use it

## Call it from code

Call it over HTTP through Comfy Router, with copy-paste Python, TypeScript, Swift and cURL snippets

This runs on the same Comfy account and is billed in the same credits as running it in ComfyUI below. See [Partner Nodes pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for per-model rates and [Concurrency limits](https://docs.comfy.org/tutorials/partner-nodes/concurrency-limits) for how many requests you can have in flight.

To use the Partner Nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the Partner Nodes.

  * Local users

  * Cloud users




Make sure your ComfyUI is updated.

  * [Download ComfyUI](https://www.comfy.org/download)
  * [Update Guide](https://docs.comfy.org/installation/update_comfyui)

Workflows in this guide can be found in the [Workflow Templates](https://docs.comfy.org/interface/features/template). If you can’t find them in the template, your ComfyUI may be outdated.If nodes are missing when loading a workflow, possible reasons:

  1. You are not using the latest ComfyUI version (Nightly version)
  2. Some nodes failed to import at startup



  * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.

## 

​

FLUX Video Upscale workflow

Upscale an existing video clip: load the video, choose a mode and upscale factor, then run. The workflow uses the FLUX Video Upscale partner node to process the clip through the Black Forest Labs API.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX Video Upscale” in Template Library

## 

​

Precise or creative mode

The node’s **mode** option selects how the upscaler treats your footage:

  * **Precise** : Sharpens the source without changing it. Use when identity matters: faces, products, brand assets, and footage of real people.
  * **Creative (default)** : Restores and invents fine detail. Best for generated footage, textures, crowds, and scenery. Identity is not preserved as strictly, so faces and products can drift.



## 

​

Prompt tips

  * Start from the least compressed source you have. Compression artifacts limit how much real detail the upscaler can recover.
  * Use creative mode for generated footage, landscapes, textures, and crowds; use precise mode when faces, products, or brand assets must stay exactly as they are.
  * A short prompt describing the clip’s content can steer creative mode toward the right kind of detail, for example “detailed armor plating and reptilian skin texture”. Leave it empty for a neutral upscale.
  * The prompt does not change the clip’s content. It only steers the enhanced detail, so no action chains, camera moves, or audio cues are needed.
  * Run upscaling as your final step, after editing and trimming, so you only pay for footage you keep.



## 

​

Limits

  * Input clips are limited to 1 to 20 seconds, at least 64px, with an aspect ratio between 1:4 and 4:1. Sources larger than 3840x2160 in area need **auto_downscale** enabled.
  * The upscale factor ranges from 1.5x to 3x, and the output keeps the source aspect ratio. Very large sources are upscaled by less than requested.
  * Output is 24 fps, capped at about 14.4 megapixels per frame, and keeps the source audio track.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `FLUX Video Upscale`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/black-forest-labs/flux-video-upscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/black-forest-labs/flux-video-upscale)

[FLUX Video Edit: Text-Prompt Video Editing in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-video-edit)[Seedance 2.5 - AI video generation with audioNext](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5)

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
