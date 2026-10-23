---
url: https://docs.comfy.org/tutorials/partner-nodes/wan/wan2-7/
title: Wan2.7 in ComfyUI: T2V, I2V, R2V, and Video Editing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:06.870392+00:00
---

# Wan2.7 in ComfyUI: T2V, I2V, R2V, and Video Editing - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/wan/wan2-7/

## On this page

  * What Wan2.7 is good at
  * Highlights
  * Wan2.7 image-to-video
  * Wan2.7 text-to-video
  * Wan2.7 reference-to-video
  * Wan2.7 video edit



Wan

# Wan2.7 in ComfyUI: T2V, I2V, R2V, and Video Editing

Copy pageCopy page

Generate video with Wan2.7 through ComfyUI Partner Nodes: image-to-video, text-to-video, reference-to-video, video continuation, and prompt-guided editing.

Copy pageCopy page

Wan2.7 is Alibaba’s latest video generation model, now available in ComfyUI via Partner Nodes. It is a comprehensive upgrade over version 2.6 with significant improvements across image quality, audio, motion dynamics, stylization, and consistency. This release brings a fully upgraded multimodal video pipeline directly into your node graph, supporting text, image, audio, and video inputs across five task types.

## 

​

What Wan2.7 is good at

  * **Image-to-video** : First-frame, first+last-frame, and audio-driven generation
  * **Text-to-video** : Pure text prompts with optional audio input and multi-shot narration
  * **Video continuation** : Extend an existing clip with new content guided by a text prompt
  * **Reference-to-video** : Reference both a subject’s visual appearance and vocal timbre; supports up to 5 real-person inputs and multi-character interactions
  * **Video edit** : Edit or replicate videos via text prompts, reference image, or style transfer



## 

​

Highlights

  * Supports up to **5 real-person image inputs** for multi-character scenes
  * Vocal timbre reference for consistent audio-visual identity
  * 3x3 grid-based image generation
  * Significant improvements in motion dynamics, stylization, and consistency over Wan2.6



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

Wan2.7 image-to-video

Generate video from image inputs. Supports first-frame, first+last-frame, and audio-driven generation modes. ![Wan2.7 I2V workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_i2v-1.webp)

## Wan2.7 I2V Workflow

Get the Wan2.7 Image-to-Video workflow file.

## Run Wan2.7 I2V on Cloud

Try the Image-to-Video workflow instantly on Comfy Cloud.

## 

​

Wan2.7 text-to-video

Generate video from pure text prompts. Optionally include audio input and multi-shot narration for richer storytelling. ![Wan2.7 T2V workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_t2v-1.webp)

## Wan2.7 T2V Workflow

Get the Wan2.7 Text-to-Video workflow file.

## Run Wan2.7 T2V on Cloud

Try the Text-to-Video workflow instantly on Comfy Cloud.

## 

​

Wan2.7 reference-to-video

Use reference images of a subject’s visual appearance along with an optional vocal timbre reference. Supports up to 5 real-person inputs for multi-character interaction scenes. ![Wan2.7 R2V workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_r2v-1.webp)

## Wan2.7 R2V Workflow

Get the Wan2.7 Reference-to-Video workflow file.

## Run Wan2.7 R2V on Cloud

Try the Reference-to-Video workflow instantly on Comfy Cloud.

## 

​

Wan2.7 video edit

Edit or replicate existing videos using text prompts, a reference image, or style transfer. ![Wan2.7 Video Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_video_edit-1.webp)

## Wan2.7 Video Edit Workflow

Get the Wan2.7 Video Edit workflow file.

## Run Wan2.7 Video Edit on Cloud

Try the Video Edit workflow instantly on Comfy Cloud.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/wan/wan2-7.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/wan/wan2-7)

[Wan 3.0 in ComfyUI: Video Generation with Synchronized AudioPrevious](https://docs.comfy.org/tutorials/partner-nodes/wan/wan3-0)[3D Models in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/3d/overview)

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
