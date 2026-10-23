---
url: https://docs.comfy.org/tutorials/utility/image-upscale/
title: Image upscaling in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:40.924487+00:00
---

# Image upscaling in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/image-upscale/

## On this page

  * Why upscaling matters
  * Key concepts
    * Upscaling vs. enhancement
    * Creative vs. conservative upscale
  * Use cases
    * Portrait and skin enhancement
    * Product photography
    * Landscape and environments
    * Stylized art and illustration
    * AI-generated images
  * Available models
    * Local models (ESRGAN)
    * General creative upscaling
    * Partner nodes
  * Benchmark: 1K to 4K upscale time
  * Tips



Upscale & Restore

# Image upscaling in ComfyUI

Copy pageCopy page

Learn how to upscale images in ComfyUI using local models and partner nodes for different use cases

Copy pageCopy page

This guide covers image upscaling workflows in ComfyUI, including local models and partner node options for various use cases.

## The Complete AI Upscaling Handbook

For a comprehensive deep-dive with benchmarks and visual comparisons, read the full article on the ComfyUI Blog.

## 

​

Why upscaling matters

  * **Industry requirements for resolutions** : 4K/8K end results are widely required across VFX & Film, Marketing, E-commerce, Gaming, and Design industries, and requirements keep moving up.
  * **Reframing** : When assets ship across different aspect ratios and placements, extra resolution headroom prevents quality loss after cropping or recomposition.
  * **The AI content problem** : Generative AI has dramatically increased the speed of visual creation, but most AI assets today are still generated at 480–720p, and not production-ready at the pixel level: edges, micro-texture, faces/hands, compression artifacts, etc. This creates a new pipeline: Generation → Refinement/Fix → Upscale → Delivery.
  * **Cost/time efficiency** : Generate or render smaller → upscale at the end. This is a standard efficiency move in pipelines under budget/time pressure.



## 

​

Key concepts

### 

​

Upscaling vs. enhancement

  * **Upscaling** increases resolution while reconstructing detail.
  * **Enhancement** improves perceived quality (denoise, sharpen, restore, color, faces, etc.).

The best practice in AI pipelines usually combines both steps.

### 

​

Creative vs. conservative upscale

Diffusion models and generative AI changed what “upscaling” means. Traditionally, super-resolution aimed to **preserve the original signal**. Today, some models can **re-imagine details that never existed**. And there are models approaching different balances between the two.

| Conservative| Creative  
---|---|---  
**Approach**|  Preserve the original| Reimagine and enhance  
**Strengths**|  High accuracy, consistency, production-safe| Rich details, sharper, more visually striking  
**Limits**|  Can appear flat, limited improvement on poor input| Possible hallucinations or structural drift  
**Models**|  Magnific Precise, SeedVR2, FlashVSR, Topaz Fast, HitPaw| Wan 2.2, Magnific Creative, Topaz Astra, HitPaw Creative  
  
## 

​

Use cases

**TL;DR**

  * **Portraits** : Magnific Skin Enhancer
  * **Product photography** : Magnific Precise, WaveSpeed SeedVR2, or Nano Banana Pro
  * **Landscapes & illustrations**: Model choice depends on your specific needs
  * **AI artifacts** : Do not rely on upscaling to fix common AI artifacts
  * **SeedVR2 tip** : Downscale the image to 0.35 megapixels with the `ImageScaleToTotalPixels` node before upscaling for better results



### 

​

Portrait and skin enhancement

When it comes to upscaling portraits of realistic subjects, achieving realistic skin details while maintaining character consistency is key. The best upscale models for fixing plastic skin need to add texture, pores and natural skin imperfections. In this domain, Magnific Image Skin Enhancer far outperforms the rest. **Recommended** : Magnific Image Skin Enhancer

## Magnific Skin Enhancer

Try on Comfy Cloud or download workflow

### 

​

Product photography

Maintaining a faithful representation of materials, product label edges, and small text is a must when upscaling product images. Therefore, conservative upscaling models are necessary. **Recommended** : HitPaw, Magnific Precise, WaveSpeed SeedVR2, Nano Banana Pro

## HitPaw

Try on Comfy Cloud or download workflow

## Nano Banana Pro Product

Try on Comfy Cloud or download workflow

## SeedVR2 (Open Source)

Try on Comfy Cloud or download workflow

### 

​

Landscape and environments

For this use case, the upscale model you select really depends on your needs. Have an environmental shot that you want to pop with details and set a mood? Use a creative upscale model. Have an establishing shot where a building needs to stay consistent? Use a conservative upscale model. It’s worth noting that if your input image has artifacts, creative upscale models may be able to reimagine the artifact while conservative upscale models will not.

## Topaz Landscape

Try on Comfy Cloud or download workflow

## Recraft Creative

Try on Comfy Cloud or download workflow

## Recraft Crisp

Try on Comfy Cloud or download workflow

### 

​

Stylized art and illustration

This is another use case where the correct upscale model depends on your needs. A rule of thumb is that if your input has a very distinct/unique style, the best model will be conservative. Creative models may add too many details and stray away from the desired illustrated style. However, if your input image has room for detail, a creative model works well and can even improve the style. We recommend playing around with the ‘creativity’ parameters for Magnific Creative and Topaz Image Enhance to find values that meet your needs! Nano Banana Pro can also work well for more common styles and adding details (but may rely on ‘seed luck’). **Recommended** : Magnific Creative, Topaz Image Enhance, Nano Banana Pro

## Topaz Illustration

Try on Comfy Cloud or download workflow

## Topaz Creative

Try on Comfy Cloud or download workflow

## Nano Banana Pro Styled Art

Try on Comfy Cloud or download workflow

## Nano Banana Pro Portrait

Try on Comfy Cloud or download workflow

### 

​

AI-generated images

When it comes to upscaling images that have typical AI issues such as too many fingers, artifacts, incorrect anatomy, and morphing, the assumption is that creative upscales can fix it. Sometimes that’s true, but other times not so much. Best practice is to resolve these issues prior to upscaling with image-edit models or traditional tools (or generate a new image entirely).

## 

​

Available models

### 

​

Local models (ESRGAN)

For basic local upscaling using ESRGAN models, see the [basic upscale tutorial](https://docs.comfy.org/tutorials/basic/upscale).

Model| Best for  
---|---  
RealESRGAN| General-purpose upscaling  
BSRGAN| Text and sharp edges  
SwinIR| Natural textures, landscapes  
  
## Traditional Non-AI Upscaling

Try on Comfy Cloud or download workflow

### 

​

General creative upscaling

For general creative upscaling across various use cases:

## HitPaw Creative

Try on Comfy Cloud or download workflow

## Recraft Creative

Try on Comfy Cloud or download workflow

## Recraft Crisp

Try on Comfy Cloud or download workflow

### 

​

Partner nodes

Partner nodes provide access to advanced upscaling models via API.

Model| Type| Features  
---|---|---  
Topaz Image Enhance (Bloom)| Creative| Subject detection, face enhancement, color preservation, up to 8K  
Magnific Precise| Conservative| High accuracy, production-safe  
Magnific Creative| Creative| Detail reimagination  
Magnific Skin Enhancer| Creative| Portrait-specific, adds realistic skin texture  
Nano Banana Pro| Conservative| Fast, good for product photography  
WaveSpeed SeedVR2| Conservative| High fidelity  
HitPaw| Both| Conservative and creative modes  
Recraft| Both| Creative and crisp modes  
  
## 

​

Benchmark: 1K to 4K upscale time

Model| Time  
---|---  
Magnific Precise| ~40s  
WaveSpeed SeedVR2| ~40s  
Magnific Creative| ~50s  
Magnific Skin Enhancer| ~60s  
HitPaw| ~60s  
Nano Banana Pro| ~80s  
Topaz Image Enhance| ~100s  
  
## 

​

Tips

  * For SeedVR2, downscale the image to 0.35 megapixels with the `ImageScaleToTotalPixels` node before upscaling for better results.
  * Chain multiple upscale nodes (e.g., 2x → 4x) for ultra-high magnification.
  * Connect upscale nodes after generation for “generate + enhance” pipelines.
  * Test multiple models on your specific image type to find the best fit.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/image-upscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/image-upscale)

[ComfyUI preprocessor workflowsPrevious](https://docs.comfy.org/tutorials/utility/preprocessors)[Video Upscaling in ComfyUI: Models and Use CasesNext](https://docs.comfy.org/tutorials/utility/video-upscale)

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
