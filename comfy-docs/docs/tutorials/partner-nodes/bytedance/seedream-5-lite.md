---
url: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedream-5-lite/
title: ByteDance Seedream 5.0 Lite - Smart AI Image Creation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:28.056833+00:00
---

# ByteDance Seedream 5.0 Lite - Smart AI Image Creation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedream-5-lite/

## On this page

  * What Seedream 5.0 Lite is good at
  * Example outputs
  * Seedream 5.0 lite image edit workflow
    * Image edit showcase
    * Consistency showcase
  * Seedream 5.0 lite text to image workflow
    * World knowledge showcase
  * Get started



ByteDance

# ByteDance Seedream 5.0 Lite - Smart AI Image Creation

Copy pageCopy page

Generate images with web-connected retrieval and enhanced instruction following using Seedream 5.0 lite in ComfyUI

Copy pageCopy page

Seedream 5.0 lite is the latest image generation model from BytePlus. It is the first in the Seedream family to bring in web-connected retrieval, which means the model can draw on live online information when generating images.

## 

​

What Seedream 5.0 Lite is good at

  * **Web-connected retrieval** : The model pulls from live web data during generation, allowing creations to be tied to real-world trends, current events, and up-to-date knowledge
  * **Smarter instruction following** : Handles complex, multi-step instructional prompts far more reliably. Multi-image inputs, local editing instructions, and batch style requests all land closer to the intended output
  * **Stronger consistency** : Character identity, product appearance, style, and lighting all hold up much better across a set of generated images
  * **Deeper world knowledge** : Expanded knowledge base makes the model useful for technical illustration, educational diagrams, and knowledge-heavy creative work



## 

​

Example outputs

Multi-step local editing, following several boxed instructions in one pass: ![Instruction following example 1](https://substack-post-media.s3.amazonaws.com/public/images/9a770e2a-c0ed-4253-bd60-14c5beff150d_2048x2048.png) _Change the glasses in the green box to circular lenses, the orange purse in the blue box to a purple oval purse, and her shoes in the red box are patterned with leopard print._ Style transfer between two images: ![Style transfer example](https://substack-post-media.s3.amazonaws.com/public/images/dc08a07e-edf1-4864-b6a6-5a7b17b78cfa_1920x1080.png) _Refer to the second image and change the style of the first picture to match that of the second image._ Product consistency across a batch of generated photos: ![Product consistency](https://substack-post-media.s3.amazonaws.com/public/images/585cf84d-afe0-4277-b08a-7a0cddbd6a54_1620x1080.png) _Using the bottle from the reference image, generate six product photos in different seasonal settings. Consistent bottle design across all six._ Knowledge-heavy text-to-image generation: ![Gravity infographic](https://substack-post-media.s3.amazonaws.com/public/images/fac37b40-faaa-4360-b449-08da38322186_2562x1440.png) _Pixel art infographic for explaining gravity, rendered in crisp 16-bit style with a dark navy/charcoal background and bold cinematic palette tones._

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

Seedream 5.0 lite image edit workflow

![Seedream 5.0 Lite Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_lite_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Seedream 5.0 lite” in Template Library

### 

​

Image edit showcase

![Instruction following example 1](https://substack-post-media.s3.amazonaws.com/public/images/9a770e2a-c0ed-4253-bd60-14c5beff150d_2048x2048.png) _Change the glasses in the green box to circular lenses, the orange purse in the blue box to a purple oval purse, and her shoes in the red box are patterned with leopard print._ ![Instruction following example 2](https://substack-post-media.s3.amazonaws.com/public/images/6ec0976b-1cb0-45e0-a657-ab97efd4d915_2048x2048.png) _While maintaining the original composition, change the overall color tone to navy and white colors. Change “RTX PRO 6000” to “SEEDREAM 5.0 LITE” in the image, and change “2025” to “NOW LIVE”._ ![Style transfer example](https://substack-post-media.s3.amazonaws.com/public/images/dc08a07e-edf1-4864-b6a6-5a7b17b78cfa_1920x1080.png) _Refer to the second image and change the style of the first picture to match that of the second image._

### 

​

Consistency showcase

![Design consistency](https://substack-post-media.s3.amazonaws.com/public/images/cc7b80ef-418c-4376-95e2-38c9110c6456_1920x1080.png) _Refer to the design and layout style of Figure 2 and adapt the style of Figure 1 accordingly._ ![Character merge](https://substack-post-media.s3.amazonaws.com/public/images/22d1fa08-17f3-4113-86ee-ca0a324cbb3b_1920x1080.png) _Merge Figure 1 and Figure 2 into a high-angle top-down selfie of two people, compact composition with them close together._ ![Multi-reference composition](https://substack-post-media.s3.amazonaws.com/public/images/2d690f6d-fa30-4152-9dc4-c09341c4e887_1920x1080.png) _Use the flowers shown in Figure 1‑4 for flower arrangement. Arrange all the flowers in the vase shown in Figure 5, then place the vase on the table shown in Figure 6._ ![Product consistency](https://substack-post-media.s3.amazonaws.com/public/images/585cf84d-afe0-4277-b08a-7a0cddbd6a54_1620x1080.png) _Using the bottle from the reference image, generate six product photos in different seasonal settings. Consistent bottle design across all six._

## 

​

Seedream 5.0 lite text to image workflow

![Seedream 5.0 Lite Text-to-Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_lite_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Seedream 5.0 lite” in Template Library

### 

​

World knowledge showcase

![Gravity infographic](https://substack-post-media.s3.amazonaws.com/public/images/fac37b40-faaa-4360-b449-08da38322186_2562x1440.png) _Pixel art infographic for explaining gravity, rendered in crisp 16-bit style with a dark navy/charcoal background and bold cinematic palette tones._ ![Big Bang infographic](https://substack-post-media.s3.amazonaws.com/public/images/39e35082-3b26-41df-8e09-5cc1841d94c6_2562x1440.png) _Comic book style infographic for explaining the Big Bang and the age of dinosaurs, with a deep crimson and ink-black background and bold comic palette tones._

## 

​

Get started

  1. Update ComfyUI to the latest (0.15.0+)
  2. Go to Template Library, search for `Seedream 5.0 lite`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bytedance/seedream-5-lite.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bytedance/seedream-5-lite)

[ByteDance Seedream 5.0 Pro - Professional AI Image GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedream-5-pro)[Clarity AI Crystal Upscaler in ComfyUI: Faithful UpscalingNext](https://docs.comfy.org/tutorials/partner-nodes/clarityai/crystal-upscale)

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
