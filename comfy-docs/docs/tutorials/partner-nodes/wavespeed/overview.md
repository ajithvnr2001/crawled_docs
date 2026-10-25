---
url: https://docs.comfy.org/tutorials/partner-nodes/wavespeed/overview/
title: Image & Video Enhancement with WaveSpeed - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:50.851092+00:00
---

# Image & Video Enhancement with WaveSpeed - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/wavespeed/overview/

## On this page

  * Key capabilities
  * Models



WaveSpeed

# Image & Video Enhancement with WaveSpeed

Copy pageCopy page

Upscale video and images, and restore old photos using WaveSpeed AI models — FLSH-VSR video upscaling, SeedVR2 image restoration, and general image upscaling, all within ComfyUI.

Copy pageCopy page

WaveSpeed is a high-performance AI media enhancement platform, now available as native workflow nodes in ComfyUI. It offers **image upscaling** and **SeedVR2 AI image fix** for photos, plus **FLSH-VSR video upscaling** — all powered by ComfyCloud with no local GPU needed.

## 

​

Key capabilities

  * **FLSH-VSR video upscaling** — Temporal-coherent AI video super-resolution that maintains consistent detail across frames, ideal for archiving, AI video enhancement, and SD-to-HD conversion.
  * **General image upscaling** — Multi-purpose image enlargement and quality improvement covering photographs, digital art, renders, and screenshots.
  * **SeedVR2 AI image fix** — Diffusion-based restoration model for recovering damaged, degraded, or low-quality images, including old photo repair, noise and artifact removal, and lost detail reconstruction.
  * **No local GPU required** — All processing runs on ComfyCloud’s infrastructure, keeping your local hardware free for generation and composition.
  * **Easy pipeline integration** — Simple drop-in nodes that work as a final enhancement step or intermediate preprocessing stage in any ComfyUI workflow.
  * **Broad content compatibility** — Models handle diverse input types including photographs, AI art, video frames, and compressed web images.



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

Models

WaveSpeed offers two model groups in ComfyUI. The **Upscale** group covers general image upscaling and SeedVR2 restoration, while **FlashVSR** provides temporal-aware video super-resolution.

## WaveSpeed Upscale

General image upscaling and SeedVR2 AI image restoration.

## WaveSpeed FlashVSR

Temporal-coherent AI video upscaling.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/wavespeed/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/wavespeed/overview)

[Wan2 7](https://docs.comfy.org/tutorials/partner-nodes/wan/wan2-7)[WaveSpeed Upscale](https://docs.comfy.org/tutorials/partner-nodes/wavespeed/wavespeed-upscale)
