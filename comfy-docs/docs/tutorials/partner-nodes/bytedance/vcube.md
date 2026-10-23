---
url: https://docs.comfy.org/tutorials/partner-nodes/bytedance/vcube/
title: ByteDance vCube Video Enhance in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:27.898542+00:00
---

# ByteDance vCube Video Enhance in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bytedance/vcube/

## On this page

  * What vCube Video Enhance is good at
  * ByteDance vCube video enhance workflow
    * Node options



ByteDance

# ByteDance vCube Video Enhance in ComfyUI

Copy pageCopy page

Upscale and restore video with ByteDance vCube in ComfyUI: super-resolution up to 8K, artifact removal, color enhancement, and frame interpolation.

Copy pageCopy page

ByteDance vCube is ByteDance’s AI video enhancement technology. It upscales low-resolution video with super-resolution up to 8K while removing compression artifacts and noise, enhancing color and sharpness, and optionally interpolating frames for a higher frame rate. In ComfyUI, the ByteDance vCube Video Enhance node takes a video, upscales it to a target resolution preset, and restores its quality. The source video must be at most 2560x1440, and the output size is set by the resolution input.

## 

​

What vCube Video Enhance is good at

  * **Super-resolution up to 8K** : Upscales low-resolution video to output presets from 720P to 8K, or a custom short side from 128 to 4320 pixels
  * **Artifact and noise removal** : Cleans up compression artifacts and noise while restoring video quality
  * **Color and sharpness enhancement** : Improves color and sharpness, with a natural high-definition look or a softer result
  * **AI frame interpolation** : Raises the frame rate above the source, up to 120 fps
  * **Scene-aware presets** : Tuned modes for AI-generated footage, general video, compressed phone clips, drama with faces, and scratched or flickering archive footage



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

ByteDance vCube video enhance workflow

Upload a video, choose the target resolution and frame rate, and run the workflow to get an upscaled, restored video.

## Run on Comfy Cloud

Run the video enhance workflow instantly on Comfy Cloud.

## Download Workflow

Download the workflow JSON file for local use.

![ByteDance vCube Video Enhance workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_vcube_video_enhance-1.webp)

## Download Sample Input Video

Get the example input video for this workflow.

### 

​

Node options

  * **Scene preset** : Tuned to the content, with `aigc` for AI-generated footage, `common` for general video, `ugc` for compressed phone clips, `short_series` for drama with faces, and `old_film` for scratched or flickering archive footage
  * **Enhancement style** : `hd` for a natural high-definition look, or `natural` for a softer result
  * **Resolution** : Output presets from 720P to 8K, `source` to keep the source size, or a custom short side from 128 to 4320 pixels
  * **Frame rate** : `source`, or 24, 25, 30, 48, 50, 60, and 120 fps. Rates above the source enable AI frame interpolation; rates above 30 fps cost 2x, above 60 fps 4x
  * **Smoothness** : `low`, `medium`, or `high` bitrate level for the delivered file



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bytedance/vcube.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bytedance/vcube)

[Seedance 2.0 Real Human - Verified real person video generationPrevious](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0-real-human)[Gemini Omni Flash: Conversational Video GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash)

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
