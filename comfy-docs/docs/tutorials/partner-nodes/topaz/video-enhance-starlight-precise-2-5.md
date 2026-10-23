---
url: https://docs.comfy.org/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5/
title: Topaz Starlight Precise 2.5 - AI video upscaling - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:39.171318+00:00
---

# Topaz Starlight Precise 2.5 - AI video upscaling - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5/

## On this page

  * What Topaz Starlight Precise 2.5 is good at
  * Example outputs
  * Topaz Starlight Precise 2.5
    * Workflow overview
    * Steps to run
  * Get started



Topaz

# Topaz Starlight Precise 2.5 - AI video upscaling

Copy pageCopy page

Upscale videos with Topaz Starlight Precise 2.5 in ComfyUI: sharper 4K output with reduced artifacts for live-action footage

Copy pageCopy page

Topaz Starlight Precise 2.5 is a video upscaling model available in ComfyUI through the Topaz partner nodes. It upscales MP4 videos up to 4K resolution with sharper output and fewer artifacts.

## 

​

What Topaz Starlight Precise 2.5 is good at

  * **4K upscaling** : Upscales MP4 videos up to 4K resolution
  * **Sharper results** : Sharper output with fewer artifacts
  * **Live-action footage** : Reduced artifacts make it a good fit for live-action video
  * **Resolution options** : Output at FullHD (1080p) or 4K (2160p)



## 

​

Example outputs

Video upscaling with the Starlight Precise 2.5 model, showing the sharper enhanced result:

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

Topaz Starlight Precise 2.5

Upscale a video to sharper, higher-resolution output with the Starlight Precise 2.5 model. This workflow upscales MP4 videos up to 4K with sharper output and fewer artifacts.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Topaz Starlight Precise 2.5” in Template Library

### 

​

Workflow overview

This workflow uses three nodes:

  * **LoadVideo** : provides the source video
  * **TopazVideoEnhanceV2** : the core node, configured with the `Starlight Precise 2.5` upscaler model
  * **SaveVideo** : saves the enhanced video



### 

​

Steps to run

  1. **Load a video** : connect your MP4 video to the **LoadVideo** node
  2. **Select the upscaler** : keep `Starlight Precise 2.5` on the **TopazVideoEnhanceV2** node
  3. **Set resolution** : `FullHD (1080p)` or `4K (2160p)`
  4. **Click Queue** : press `Ctrl+Enter` to generate



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Topaz Starlight Precise 2.5`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5)

[Runway Gen4 Turbo in ComfyUI: Image-to-Video WorkflowPrevious](https://docs.comfy.org/tutorials/partner-nodes/runway/video-generation)[Topaz Astra Video Creative Upscale - AI video upscalingNext](https://docs.comfy.org/tutorials/partner-nodes/topaz/video-enhance-astra)

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
