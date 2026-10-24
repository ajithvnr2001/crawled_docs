---
url: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-video/
title: FLUX 3 Video - AI video generation with native audio - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:47.314521+00:00
---

# FLUX 3 Video - AI video generation with native audio - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-video/

## On this page

  * What FLUX 3 Video is good at
  * Example outputs
  * Use it
  * FLUX 3 text-to-video workflow
  * FLUX 3 image-to-video workflow
  * Get started



Black Forest Labs

# FLUX 3 Video - AI video generation with native audio

Copy pageCopy page

Generate videos with synchronized audio using FLUX 3 in ComfyUI, from text or images, with up to 20 seconds of footage in a single pass

Copy pageCopy page

FLUX 3 is Black Forest Labs’ multimodal foundation model, announced July 23, 2026 and currently in Early Access. It jointly learns from images, videos, and audio within a unified architecture built on Self-Flow, their approach for aligning multimodal generation and understanding in the same model. Instead of treating each modality in isolation, FLUX 3 learns a shared representation of the world: how objects hold together, how things move, and how events sound. Capabilities and limits may change during the Early Access rollout. For video, FLUX 3 creates highly diverse clips with native audio up to 20 seconds long in a single generation. All outputs come with synchronized audio generation, including ambient sound, speech, and effects. It supports text-to-video and image-to-video generation, with multi-shot output that chains individual clips into longer sequences and flexible aspect ratios.

## 

​

What FLUX 3 Video is good at

  * **Native audio** : Every video comes with synchronized audio, including ambient sound, speech, and effects
  * **Up to 20 seconds** : Generates long clips in a single pass
  * **Text and image input** : Generates video from a text prompt, or continues from a starting frame image
  * **Flexible formats** : 720p, 1080p, 1440p, or 2160p resolution, 24fps, aspect ratios from 9:16 to 21:9
  * **Multi-shot output** : Chains individual clips into longer sequences for extended storytelling



## 

​

Example outputs

Text-to-video generation from a single prompt, with synchronized audio, motion, and physics: Image-to-video generation from a starting frame and a text prompt:

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

FLUX 3 text-to-video workflow

Generate a full video from a single text prompt. FLUX 3 expands natural language into a complete scene with synchronized audio, motion, and physics, without needing reference images or complex settings.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX 3 Video” in Template Library

## 

​

FLUX 3 image-to-video workflow

Generate a full video from a text prompt and a starting frame image. FLUX 3 automatically expands your description into a cohesive scene with synchronized audio, motion, and physics.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX 3 Video” in Template Library

![FLUX 3 image to video input](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/space_caravan.png)

## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `FLUX 3 Video`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/black-forest-labs/flux-3-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/black-forest-labs/flux-3-video)

[Flux 3 Max](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-max)[Flux Video Edit](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-video-edit)
