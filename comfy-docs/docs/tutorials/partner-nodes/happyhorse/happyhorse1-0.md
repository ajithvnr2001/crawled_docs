---
url: https://docs.comfy.org/tutorials/partner-nodes/happyhorse/happyhorse1-0/
title: HappyHorse 1.0 Video Generation in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:30.904585+00:00
---

# HappyHorse 1.0 Video Generation in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/happyhorse/happyhorse1-0/

## On this page

  * What HappyHorse 1.0 is good at
  * Example outputs
  * HappyHorse 1.0 image-to-video
  * HappyHorse 1.0 text-to-video
  * HappyHorse 1.0 reference-to-video
  * HappyHorse 1.0 video edit



HappyHorse

# HappyHorse 1.0 Video Generation in ComfyUI

Copy pageCopy page

Generate cinematic video with Alibaba’s HappyHorse 1.0 in ComfyUI: image, text, and reference-driven clips, plus edit-style workflows.

Copy pageCopy page

HappyHorse 1.0 is a cinematic video generation model from Alibaba, now available in ComfyUI via Partner Nodes. It is designed for high-quality storytelling video and production-ready creative workflows. HappyHorse 1.0 focuses on strong aesthetics, multi-shot sequencing, and powerful edit-style workflows (generation + editing). It’s a great fit for creators building ads, e-commerce visuals, short-form content, and social marketing videos.

## 

​

What HappyHorse 1.0 is good at

  * **Multi-modal creation paths** : Text-to-Video (T2V), Image-to-Video (I2V), and Subject-to-Video (S2V)
  * **Cinematic aesthetics** : Wide-aperture framing, shallow depth of field, refined texture, and atmospheric mood
  * **Multi-shot output** : Up to **15s** at **1080p** , with an emphasis on multi-shot consistency across cut transitions
  * **Editing workflows** : V2V and SV2V for transforming footage or replacing/inserting subjects while preserving motion and composition



## 

​

Example outputs

Image-to-video generation with cinematic aesthetics and multi-shot consistency:

Text-to-video generation with multi-shot sequencing and refined visual atmosphere:

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

HappyHorse 1.0 image-to-video

Generate cinematic video from a single image with strong aesthetic control and multi-shot consistency.

## Run HappyHorse 1.0 I2V on Cloud

Try the Image-to-Video workflow instantly on Comfy Cloud.

## HappyHorse 1.0 I2V Workflow

Get the HappyHorse 1.0 Image-to-Video workflow file.

![HappyHorse 1.0 Image-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_i2v-1.webp)

## Download Sample Input Image

Get the example input image for this workflow.

## 

​

HappyHorse 1.0 text-to-video

Generate cinematic video from pure text prompts, with multi-shot sequencing and refined visual atmosphere.

## Run HappyHorse 1.0 T2V on Cloud

Try the Text-to-Video workflow instantly on Comfy Cloud.

## HappyHorse 1.0 T2V Workflow

Get the HappyHorse 1.0 Text-to-Video workflow file.

![HappyHorse 1.0 Text-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_t2v-1.webp)

## 

​

HappyHorse 1.0 reference-to-video

Use a reference subject to drive video generation, preserving identity across cinematic multi-shot sequences.

## Run HappyHorse 1.0 R2V on Cloud

Try the Reference-to-Video workflow instantly on Comfy Cloud.

## HappyHorse 1.0 R2V Workflow

Get the HappyHorse 1.0 Reference-to-Video workflow file.

![HappyHorse 1.0 Reference-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_r2v-1.webp)

## Download Car Reference Image

Get the example car reference image.

## Download Person Reference Image

Get the example person reference image.

## 

​

HappyHorse 1.0 video edit

Transform existing footage or replace/insert subjects while preserving motion and composition with V2V and SV2V editing workflows.

## Run HappyHorse 1.0 Video Edit on Cloud

Try the Video Edit workflow instantly on Comfy Cloud.

## HappyHorse 1.0 Video Edit Workflow

Get the HappyHorse 1.0 Video Edit workflow file.

![HappyHorse 1.0 Video Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_video_edit-1.webp)

## Download Sample Input Image

Get the example input image for the video edit workflow.

## Download Sample Input Video

Get the example input video for the video edit workflow.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/happyhorse/happyhorse1-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/happyhorse/happyhorse1-0)

[HappyHorse 1.1 Video Generation in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/happyhorse/happyhorse1-1)[HeyGen Video 1.0 in ComfyUI: Text, Image, and Reference to VideoNext](https://docs.comfy.org/tutorials/partner-nodes/heygen/heygen-video-1)

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
