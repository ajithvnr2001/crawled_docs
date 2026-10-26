---
url: https://docs.comfy.org/tutorials/partner-nodes/kling/kling-3-0/
title: Kling 3.0 Video and Image Generation in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:10.134693+00:00
---

# Kling 3.0 Video and Image Generation in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/kling/kling-3-0/

## On this page

Back to top

  * What Kling 3.0 is good at
  * Example outputs
  * Available models
  * Learn more
  * Kling 3.0: Text to Image
  * Kling 3.0: Video Generation
  * Kling 3.0: First Last Frame to Video
  * Kling 3.0: Motion Control
  * Legacy Kling models (EOL)
    * Retired workflow templates and replacements



Kling

# Kling 3.0 Video and Image Generation in ComfyUI

Copy pageCopy page

Learn how to use Kling 3.0 models in ComfyUI for multi-shot video generation, subject consistency, multilingual audio, and native text rendering

Copy pageCopy page

Kling 3.0 is one of the most advanced multi-modal generation systems, now available in ComfyUI via Partner Nodes. This release includes **Kling Video 3.0** , **Kling Video 3.0 Omni** , **Kling Image 3.0** , and **Kling Image 3.0 Omni** , bringing video, image, audio-visual, and narrative generation capabilities directly into your node-based workflows.

## 

​

What Kling 3.0 is good at

  * **Multi-shot generation** : Generate multiple shots with duration control in a single generation
  * **Locked subject consistency** : Maintain character and object identity across camera motion and scene evolution
  * **Native audio with character awareness** : Multilingual dialogue with precise lip sync and facial expression alignment
  * **Native text rendering** : Clear, structured on-screen text for ads, UI scenes, and branded content



## 

​

Example outputs

Text-to-image generation with the Kling 3.0 model: ![Kling 3.0: Text to Image example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_kling_v3_t2i.png)

## 

​

Available models

Model| Type| Description  
---|---|---  
**Kling Video 3.0**|  Video| Standard video generation with multi-shot support  
**Kling Video 3.0 Omni**|  Video| Advanced video generation with audio-visual capabilities  
**Kling Image 3.0**|  Image| High-quality image generation  
**Kling Image 3.0 Omni**|  Image| Multi-modal image generation with enhanced features  
  
## 

​

Learn more

For detailed examples, prompts, and video demonstrations of Kling 3.0’s capabilities, check out our blog post:

## Kling 3.0 Models Are Now Available

Read the full announcement with video examples, prompt tips, and feature deep-dives.

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

Kling 3.0: Text to Image

Generate an image from a text prompt using the Kling 3.0 model. ![Kling 3.0: Text to Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 3.0: Text to Image” in Template Library

**Example output** ![Kling 3.0: Text to Image example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_kling_v3_t2i.png)

## 

​

Kling 3.0: Video Generation

Input text or image prompts to generate 15-second video sequences with multi-shot compositions, complex camera movements, and consistent subjects. ![Kling 3.0: Video Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 3.0: Video Generation” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## boxing.png

`LoadImage` node 1 · `boxing.png`

![boxing.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/boxing.png)

## 

​

Kling 3.0: First Last Frame to Video

Input a first and last frame image to generate a continuous video sequence with multi-shot generation and precise element control. ![Kling 3.0: First Last Frame to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_flf2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 3.0: First Last Frame to Video” in Template Library

**Input materials** Upload these files to the matching `LoadImage` nodes:

## goldenfish_in_bag.png

`LoadImage` node 1 · `goldenfish_in_bag.png`

## man_in_daydream.png

`LoadImage` node 13 · `man_in_daydream.png`

![goldenfish_in_bag.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/goldenfish_in_bag.png)![man_in_daydream.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/man_in_daydream.png)

## 

​

Kling 3.0: Motion Control

Apply the motion of a reference video to a character image. Upload a character image plus a motion reference video and the model drives your character through the action in the clip while keeping their identity. This workflow runs the Kling 3.0 model, which improves facial consistency over previous versions. ![Kling 3.0: Motion Control workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_motion_control3-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 3.0: Motion Control” in Template Library

**Input materials** Upload these files to the matching `LoadImage` and `LoadVideo` nodes:

## future_robot.png

`LoadImage` node 2 · `future_robot.png`

## boxing_man.mp4

`LoadVideo` node 3 · `boxing_man.mp4`

![future_robot.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/future_robot.png)

**Motion control settings** Set `character_orientation` to `video` when the camera and framing should follow the motion clip, which allows reference clips up to 30 seconds, or to `image` when the character keeps the framing of the still image, which limits the clip to 10 seconds. Keep `mode` on `pro` for final output and switch to `std` for cheaper tests. `keep_original_sound` carries the clip’s audio into the result, and `model` switches back to `kling-v2-6` for the previous generation. This workflow uses the same `Kling Motion Control` node as the [Kling 2.6 Motion Control](https://docs.comfy.org/tutorials/partner-nodes/kling/kling-motion-control) example, so the input tips on that page apply here too.

## 

​

Legacy Kling models (EOL)

**End of life (EOL)** : The following legacy Kling models and workflow templates are scheduled for retirement on **September 15, 2026** : Kling V1.5, V1.6, V2.1, V2.1 Master, and the Kolors Virtual Try-On API. Related Partner Nodes remain in ComfyUI but these model options will stop working after the retirement date.

### 

​

Retired workflow templates and replacements

Removed template| Suggested replacement  
---|---  
`api_kling_i2v` (V2.1 Master)| [`api_kling_o3_i2v`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_o3_i2v.json) or [`api_kling2_6_i2v`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling2_6_i2v.json)  
`api_kling_effects` (V1.6)| Kling 3.0 effect workflows (`api_kling_v3_*`)  
`api_kling_flf` (V1.6)| [`api_kling_v3_flf2v`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_v3_flf2v.json) or [`api_kling_o3_flf2v`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_o3_flf2v.json)  
`api_kling_dual_characters_effects` (V1.6)| Kling 3.0 effect workflows (`api_kling_v3_*`)  
  
For virtual try-on, use [Flux Virtual Try-On](https://docs.comfy.org/built-in-nodes/FluxVTONode) (`api_flux_vto`) or other supported alternatives. FLUX VTO and Gemini-based fashion templates are not affected by this retirement.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/kling/kling-3-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/kling/kling-3-0)

[HitPaw Video Enhance](https://docs.comfy.org/tutorials/partner-nodes/hitpaw/hitpaw-video-enhance)[Kling Virtual Try-On](https://docs.comfy.org/tutorials/partner-nodes/kling/kling-virtual-try-on)
