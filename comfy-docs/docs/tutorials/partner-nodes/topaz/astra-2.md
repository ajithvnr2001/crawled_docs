---
url: https://docs.comfy.org/tutorials/partner-nodes/topaz/astra-2/
title: Astra 2 - Creative diffusion video upscaling - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:38.244677+00:00
---

# Astra 2 - Creative diffusion video upscaling - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/topaz/astra-2/

## On this page

  * What is Astra 2?
  * Model overview
  * What Astra 2 is good at
  * Related
  * In ComfyUI
  * Example workflow



Topaz

# Astra 2 - Creative diffusion video upscaling

Copy pageCopy page

What Astra 2 does for your videos in ComfyUI, plus creative upscaling with control over detail and style.

Copy pageCopy page

Enhanced creative upscaling for GenAI video, with advanced control over detail and style.

## 

​

What is Astra 2?

**If you’re new here:** Astra 2 targets **AI-generated and stylized video**. Plain upscaling mostly enlarges and sharpens existing pixels; Astra 2 can **add plausible new detail and texture** where the source is soft, so the clip feels richer, not only bigger.

## 

​

Model overview

It builds on Astra 1 with clearer control over how detail and stylization are produced (creativity, sharpness, optional **descriptive** prompts, not step lists). Strong fits: stylized/GenAI footage, wides and sparse-detail scenes, and footage that looks overly smooth until texture is restored.

## 

​

What Astra 2 is good at

  * **Adds texture and detail** : Not only sharpening.
  * **Steerable look** : Creativity, sharpness, optional prompt guidance.
  * **Stylized & wides**: Where inferred detail matters.



## 

​

Related

  * [Video upscaling in ComfyUI](https://docs.comfy.org/tutorials/utility/video-upscale): guidance on choosing an upscaling approach.



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

In ComfyUI

Use **Topaz Video Enhance**. **Topaz Video Enhance (Legacy)** does not offer **Astra 2**. Set upscaler to **Astra 2** , resolution to **FullHD** or **4K** ; input must be **MP4**. Optional **Prompt** : max **450** frames (~15 s @ 30 fps). Empty prompt: up to **9000** frames. Expand advanced controls for **Sharp** and **Realism** when needed.

## 

​

Example workflow

**Load Video** → **Topaz Video Enhance** → **Save Video**. After opening the template, pick **Astra 2** on the upscaler if another preset is selected. ![Astra 2 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_astra2-1.webp)

## Run on Comfy Cloud

Open the workflow instantly on Comfy Cloud.

## Download workflow

Download the workflow JSON for local ComfyUI.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/topaz/astra-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/topaz/astra-2)

[Topaz Astra Video Creative Upscale - AI video upscalingPrevious](https://docs.comfy.org/tutorials/partner-nodes/topaz/video-enhance-astra)[Vidu Q4 Preview in ComfyUI: Image and Reference to VideoNext](https://docs.comfy.org/tutorials/partner-nodes/vidu/vidu-q4-preview)

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
