---
url: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-image-to-video/
title: Luma Image to Video in ComfyUI: Retired Legacy Node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:56.021299+00:00
---

# Luma Image to Video in ComfyUI: Retired Legacy Node - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-image-to-video/

## On this page

Back to top

  * What Luma Image to Video is good at
  * Image to Video Workflow with Luma Partner Nodes
    * 1\. Download the Workflow
    * 2\. Additional Notes



Luma

# Luma Image to Video in ComfyUI: Retired Legacy Node

Copy pageCopy page

How the retired Luma Image to Video Partner node worked in ComfyUI, why it stopped working, and which node replaces it.

Copy pageCopy page

**Deprecated** : The legacy **Luma Image to Video** node is deprecated, and Luma removes the endpoints it uses on October 24, 2026. Use the [**Luma Ray 3.2 Image to Video** node](https://docs.comfy.org/built-in-nodes/LumaRay32ImageToVideoNode) instead.

The Luma Image to Video node allows you to convert static images into smooth, dynamic videos using Luma AI’s advanced technology, bringing life and motion to your images.

## What Luma Image to Video is good at

  * **Image animation** : Converts static images into smooth, dynamic videos, bringing life and motion to your images
  * **Prompt-guided motion** : Text prompts determine the video’s motion effects
  * **Camera control** : The Luma Concepts feature controls camera movement for professional cinematography
  * **Flexible image inputs** : Works from a `first_image`, a `last_image`, or both
  * **Adjustable output** : Video resolution and duration are adjustable, and different video generation models can be selected via the model parameter



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

## Image to Video Workflow with Luma Partner Nodes

The Luma Image to Video node requires at least one image input (`first_image` or `last_image`) along with text prompts to determine the video’s motion effects. In this guide, we’ve created an example using `first_image` and `luma_concepts` to showcase Luma AI’s video generation capabilities.

### 1\. Download the Workflow

This page documents the retired **Luma Image to Video** node and the example workflow it shipped, which selected `ray-2`. Luma stops serving that model on October 24, 2026, so neither the node nor the example can run. The example and its step guide stay in this page’s source as a comment. The replacement is a separate node. Its own guide:

## Luma Ray 3.2: Image to Video

See the replacement node and its inputs.

### 2\. Additional Notes

  * **Image Input Requirements** : At least one of `first_image` or `last_image` is required, with a maximum of 1 image per input
  * **Luma Concepts** : Controls camera movement for professional video effects
  * **Seed Parameter** : Only determines if the node should rerun, doesn’t affect generation results
  * **Enable Input Nodes** : Right-click on purple “Bypass” mode nodes and set “mode” to “always” to enable inputs
  * **Model Selection** : Different video generation models have unique characteristics, adjustable via the model parameter
  * **Resolution and Duration** : Adjust output video resolution and length using resolution and duration parameters



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/luma/luma-image-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/luma/luma-image-to-video)

[Luma Text to Video](https://docs.comfy.org/tutorials/partner-nodes/luma/luma-text-to-video)[MiniMax (Hailuo)](https://docs.comfy.org/tutorials/partner-nodes/minimax/overview)
