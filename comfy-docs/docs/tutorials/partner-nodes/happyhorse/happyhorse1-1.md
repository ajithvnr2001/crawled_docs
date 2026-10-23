---
url: https://docs.comfy.org/tutorials/partner-nodes/happyhorse/happyhorse1-1/
title: HappyHorse 1.1 Video Generation in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:30.619103+00:00
---

# HappyHorse 1.1 Video Generation in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/happyhorse/happyhorse1-1/

## On this page

  * What HappyHorse 1.1 is good at
  * HappyHorse 1.1 text-to-video
  * HappyHorse 1.1 image-to-video
  * HappyHorse 1.1 reference-to-video
  * Getting started



HappyHorse

# HappyHorse 1.1 Video Generation in ComfyUI

Copy pageCopy page

Use HappyHorse 1.1 via ComfyUI Partner Nodes for image-to-video, text-to-video, and reference-to-video with native synchronized audio and multi-shot scenes.

Copy pageCopy page

HappyHorse 1.1 is the latest release of Alibaba’s production-grade video generation model, now available in ComfyUI as a Partner Node. It is engineered for real-world creative production: short episodic series, e-commerce commercials, brand marketing content, and game cutscenes. A standout feature is **native synchronized audio generation** : HappyHorse 1.1 produces dialogue, sound effects, and background music in a single render pass, with audio tightly bound to the visual timeline. There are no extra audio steps. Version 1.1 targets five core production-critical capabilities: dynamic expressive motion, consistent character rendering, reliable prompt adherence, stable text rendering, and authentic cinematic framing.

## 

​

What HappyHorse 1.1 is good at

  * **Native audio-video sync** : Dialogue, SFX, and background music in one pass (no extra steps)
  * **Three creation paths** : Text-to-Video (T2V), Image-to-Video (I2V), Reference-to-Video (R2V)
  * **Multi-image R2V** : Up to **9 reference images** per generation with preserved identity
  * **Multi-character consistency** : Multiple character references stay distinct with no visual cross-contamination
  * **Character × scene separation** : Feed characters and scenes as independent references; characters stay consistent as the background changes
  * **Long-context prompts** : Handles prompts beyond 2,500 characters; a single prompt can describe 6–8 consecutive scenes with the model autonomously allocating time and switching camera angles
  * **Cinematic language** : Full support for shot-reverse-shot, tracking shot, and cohesive transitions/pacing between shots
  * **Flexible output** : 720p and 1080p, 3–15 seconds, aspect ratios 16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 and more
  * **Production-ready visuals** : Fixes shiny skin and over-sharpening issues from v1.0 for natural-looking close-ups and series content



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

HappyHorse 1.1 text-to-video

Build a complete scene from scratch. You control style, shot size, lighting, action, and audio entirely through the prompt. HappyHorse 1.1 returns a single video with dialogue, sound effects, and music baked in.

## Run HappyHorse 1.1 T2V on Cloud

Try the Text-to-Video workflow instantly on Comfy Cloud.

## Download HappyHorse 1.1 T2V Workflow

Download the workflow JSON or search “HappyHorse 1.1” in Template Library.

![HappyHorse 1.1 Text-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_t2v-1.webp)

## 

​

HappyHorse 1.1 image-to-video

Animate a static first frame. The image already carries the look, so you describe the motion and the camera move. HappyHorse 1.1 returns a video with audio baked in.

## Run HappyHorse 1.1 I2V on Cloud

Try the Image-to-Video workflow instantly on Comfy Cloud.

## Download HappyHorse 1.1 I2V Workflow

Download the workflow JSON or search “HappyHorse 1.1” in Template Library.

## Download Sample Image

Get the example input image for this workflow.

![HappyHorse 1.1 Image-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_i2v-1.webp)

## 

​

HappyHorse 1.1 reference-to-video

Orchestrate a multi-character stage play. Map characters and scenes to reference images, then direct them through a timestamped storyboard with per-character dialogue. Up to 9 reference images per generation, with character and scene references separated so characters stay consistent across background changes.

## Run HappyHorse 1.1 R2V on Cloud

Try the Reference-to-Video workflow instantly on Comfy Cloud.

## Download HappyHorse 1.1 R2V Workflow

Download the workflow JSON or search “HappyHorse 1.1” in Template Library.

## Download Character Reference

Get the example character reference image.

## Download Scene Reference

Get the example scene reference image.

![HappyHorse 1.1 Reference-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_r2v-1.webp)

## 

​

Getting started

  1. Update ComfyUI to the latest version
  2. Find the HappyHorse nodes via the Node Library (search “HappyHorse”) or load a ready-made template from the Templates Library
  3. Pick your mode: Text-to-Video, Image-to-Video, or Reference-to-Video
  4. Wire in your prompt and any reference images, then run
  5. Output arrives with audio baked in at 720p or 1080p



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/happyhorse/happyhorse1-1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/happyhorse/happyhorse1-1)

[Grok Imagine Video 1.5 in ComfyUI: Image and Text to VideoPrevious](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-imagine-video-1-5)[HappyHorse 1.0 Video Generation in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/happyhorse/happyhorse1-0)

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
