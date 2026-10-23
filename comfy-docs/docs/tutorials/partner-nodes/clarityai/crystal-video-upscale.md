---
url: https://docs.comfy.org/tutorials/partner-nodes/clarityai/crystal-video-upscale/
title: Clarity AI Crystal Video Upscaler in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:29.897630+00:00
---

# Clarity AI Crystal Video Upscaler in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/clarityai/crystal-video-upscale/

## On this page

  * What Crystal Video Upscaler is good at
  * Example output
  * Use it
  * Crystal Video Upscaler workflow
    * Steps to run
  * Node controls
  * Limits
  * Get started



Clarity AI

# Clarity AI Crystal Video Upscaler in ComfyUI

Copy pageCopy page

Upscale video with the Clarity AI Crystal Video Upscaler partner node in ComfyUI: raise the frame size while keeping the source frame rate and audio.

Copy pageCopy page

**Clarity AI Crystal Video Upscaler** raises the resolution of an existing clip instead of generating a new scene. It re-renders every frame at a larger size while staying close to the source, so faces, edges, and fine texture come back sharper rather than being replaced by invented detail. It is built for restoring compressed or soft AI video, upscaling generated clips for large screens, and giving edited footage a cleaner finish. In ComfyUI the model runs through the **Clarity AI Crystal Video Upscale** partner node. It is a cloud API node: it needs a Comfy account with credits and downloads no local model. You connect one video and get one upscaled video out, with the source frame rate and audio track carried over. See [Partner Node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the per-second rate. The node has a single control, `scale_factor`, which multiplies the width and height of every frame. The output is capped at 9 megapixels per frame and 360 megapixel-seconds per clip, so a long clip or a frame that is already large comes back upscaled by less than the factor you asked for instead of failing.

## 

​

What Crystal Video Upscaler is good at

  * **Faithful detail** : re-renders frames larger while staying close to the source, instead of generating new content
  * **Keeps the clip intact** : the source frame rate and audio track carry over
  * **One control** : `scale_factor` sets how much larger the output is
  * **Graceful limits** : oversized or long clips are upscaled by a smaller factor rather than rejected



## 

​

Example output

Upscaling a road clip at 2x, with the frame rate and the audio track preserved: ![Clarity AI Crystal Video Upscaler workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_video_upscale-1.webp)

## 

​

Use it

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

Crystal Video Upscaler workflow

Load a clip, set the upscale factor, and run. The workflow sends the video to the Clarity AI Crystal Video Upscale node and saves the upscaled result.

## Download Workflow

Download JSON or search “Clarity AI: Crystal Video Upscaler” in Template Library

**Input material**

## desert_highway_encounter.mp4

Load into the `LoadVideo` node that feeds the Clarity AI Crystal Video Upscale node

### 

​

Steps to run

  1. **Load a video** : upload or select your source clip in the **Load Video** node
  2. **Set the scale factor** : enter a value on the **Clarity AI Crystal Video Upscale** node. `2.0` doubles the width and height
  3. **Click Queue** or press `Ctrl+Enter` to generate



## 

​

Node controls

Control| Values| Effect  
---|---|---  
`video`| one video| Source clip. The output keeps its frame rate and audio track  
`model`| `crystal-video-upscaler`| The model the node calls  
`scale_factor`| 1.0 to 200.0, default 2.0| Multiplies the source width and height. Lowered automatically when the result would pass the frame or clip limit  
  
## 

​

Limits

  * The output is capped at **9 megapixels per frame** and **360 megapixel-seconds per clip**. Long clips and frames that are already large are upscaled by less than the requested factor.
  * Each side of the source video is limited to 5120 pixels, and the scale factor is lowered to fit that limit.
  * Clips above 30 fps cost 2x, above 60 fps 3x, and so on.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Clarity AI: Crystal Video Upscaler`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/clarityai/crystal-video-upscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/clarityai/crystal-video-upscale)

[Vcube](https://docs.comfy.org/tutorials/partner-nodes/bytedance/vcube)[Gemini Omni Flash](https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash)
