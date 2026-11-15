---
url: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-text-to-video/
title: Luma Text to Video in ComfyUI: Retired Legacy Node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:56.077298+00:00
---

# Luma Text to Video in ComfyUI: Retired Legacy Node - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-text-to-video/

## On this page

Back to top

  * What Luma Text to Video is good at
  * Text to Video Workflow with Luma Partner Nodes
    * 1\. Download the Workflow
    * 2\. Additional Notes



Luma

# Luma Text to Video in ComfyUI: Retired Legacy Node

Copy pageCopy page

How the retired Luma Text to Video Partner node worked in ComfyUI, why it stopped working, and which node replaces it.

Copy pageCopy page

**Deprecated** : The legacy **Luma Text to Video** node is deprecated, and Luma removes the endpoints it uses on October 24, 2026. Use the [**Luma Ray 3.2 Text to Video** node](https://docs.comfy.org/built-in-nodes/LumaRay32TextToVideoNode) instead.

The Luma Text to Video node allows you to create high-quality, smooth videos from text descriptions using Luma AI’s innovative video generation technology.

## What Luma Text to Video is good at

  * **Text-to-video generation** : Creates high-quality, smooth videos from text descriptions of scenes, subjects, actions, and mood
  * **Camera control** : The Luma Concepts feature adds camera movements for professional video shots and cinematography
  * **Model selection** : Different video models with different features are selectable via the model parameter
  * **Adjustable output** : Video resolution and duration are adjustable (except with the Ray 1.6 model, where these parameters don’t apply)



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

## Text to Video Workflow with Luma Partner Nodes

The Luma Text to Video node requires text prompts to describe the video content. In this guide, we’ve created examples using `prompt` and `luma_concepts` to showcase Luma AI’s excellent video generation capabilities.

### 1\. Download the Workflow

This page documents the retired **Luma Text to Video** node and the example workflow it shipped, which selected `ray-2`. Luma stops serving that model on October 24, 2026, so neither the node nor the example can run. The example and its step guide stay in this page’s source as a comment. The replacement is a separate node. Its own guide:

## Luma Ray 3.2: Text to Video

See the replacement node and its inputs.

### 2\. Additional Notes

  * **Writing Prompts** : Describe scenes, subjects, actions, and mood in detail for best results
  * **Luma Concepts** : Mainly used for camera control to create professional video shots
  * **Seed Parameter** : Only determines if the node should rerun, doesn’t affect generation results
  * **Model Selection** : Different video models have different features, adjustable via the model parameter
  * **Resolution and Duration** : Adjust output video resolution and length using these parameters
  * **Ray 1.6 Model Note** : Duration and resolution parameters don’t work when using the Ray 1.6 model. Luma stopped serving Ray 1.6 in September 2026, so that option no longer runs.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/luma/luma-text-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/luma/luma-text-to-video)

[LTX Video VFX](https://docs.comfy.org/tutorials/partner-nodes/lightricks/ltx-video-vfx)[Luma Image to Video](https://docs.comfy.org/tutorials/partner-nodes/luma/luma-image-to-video)
