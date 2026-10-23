---
url: https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-pro/
title: Nano Banana Pro: Studio-Quality AI Image Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:29.789905+00:00
---

# Nano Banana Pro: Studio-Quality AI Image Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-pro/

## On this page

  * What Nano Banana Pro is good at
  * Example outputs
  * Use it
  * Nano Banana Pro
  * Which model should you pick?
  * Get started



Google

# Nano Banana Pro: Studio-Quality AI Image Generation

Copy pageCopy page

Generate and edit production-ready 4K images with Nano Banana Pro (Gemini 3 Pro Image) in ComfyUI, with advanced text rendering and character consistency.

Copy pageCopy page

Nano Banana Pro is Google DeepMind’s flagship image model (Gemini 3 Pro Image) for studio-quality image generation and editing. It pushes beyond casual creation into production-ready visuals with advanced capabilities including native 4K resolution, precise text rendering in 10 languages, multi-image blending, and search-grounded world knowledge for accurate real-world depictions.

## 

​

What Nano Banana Pro is good at

  * **4K generation** : Create and edit images in native 4K resolution with studio-quality color grading, angle control, and focus adjustments
  * **World knowledge** : Generates accurate, real-world images by tapping into Google Search’s knowledge base for lesser-known landmarks, niche objects, and cultural details
  * **Text and translation** : Renders clean, legible text and supports detection and translation across 10 languages
  * **Multi-image blending** : Blend up to 14 images with precise compositional control
  * **Character and subject consistency** : Maintain character resemblance and object fidelity across complex multi-subject compositions
  * **Advanced reasoning** : Configurable thinking levels. Choose Minimal for fast exploration or High/Dynamic for complex layouts and precise control



## 

​

Example outputs

Multi-image blending, combining two reference images into one studio-quality result: ![Nano Banana Pro example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_pro.png)

## 

​

Use it

## Call it from code

Call it over HTTP through Comfy Router, with copy-paste Python, TypeScript, Swift and cURL snippets

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

Nano Banana Pro

Nano-banana Pro (Gemini 3.0 Pro Image) for studio-quality 4K image generation and editing with enhanced text rendering and character consistency. ![Nano Banana Pro workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_pro-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Nano Banana Pro” in Template Library

**Input materials** Upload these files to the matching `LoadImage` nodes:

## api_nano_banana_pro_input_image_1.png

`LoadImage` node 11 · `api_nano_banana_pro_input_image_1.png`

## api_nano_banana_pro_input_image_2.png

`LoadImage` node 12 · `api_nano_banana_pro_input_image_2.png`

**Example output** ![Nano Banana Pro example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_pro.png)

## 

​

Which model should you pick?

Model| Best for  
---|---  
**[Nano Banana 2 Lite](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-lite)**|  Speed and cost: rapid iteration, high-throughput pipelines, low-latency applications  
**[Nano Banana 2](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2)**|  Most creators: balanced quality and speed for general-purpose image generation and editing  
**Nano Banana Pro**|  Professional use cases: maximum quality, 4K generation, complex layouts and precise control  
  
## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Double-click the canvas and search for the “Nano Banana Pro” node
  3. Or go to the Template Library to use the ready-to-go workflow
  4. Upload your reference images, enter your prompt, and select the desired thinking level



Nano Banana Pro provides the highest quality output in the Nano Banana family. For faster generation at lower cost, consider [Nano Banana 2 Lite](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-lite) or [Nano Banana 2](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/google/nano-banana-pro.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/google/nano-banana-pro)

[Clarity AI Crystal Upscaler in ComfyUI: Faithful UpscalingPrevious](https://docs.comfy.org/tutorials/partner-nodes/clarityai/crystal-upscale)[Nano Banana 2 - Fast AI Image GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2)

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
