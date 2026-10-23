---
url: https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-lite/
title: Nano Banana 2 Lite: Fast AI Image Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:29.960937+00:00
---

# Nano Banana 2 Lite: Fast AI Image Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-lite/

## On this page

  * What Nano Banana 2 Lite is good at
  * Example outputs
  * Use it
  * Workflows
    * Text to Image
    * Image Edit
  * Which model should you pick?
  * Get started



Google

# Nano Banana 2 Lite: Fast AI Image Generation

Copy pageCopy page

Generate images at Google’s fastest speed and lowest cost using Nano Banana 2 Lite, the Gemini 3.1 Flash-Lite Image model in ComfyUI

Copy pageCopy page

Nano Banana 2 Lite is Google DeepMind’s fastest and most cost-efficient Gemini Image model, designed for rapid ideation and high-volume workflows. Powered by `gemini-3.1-flash-lite-image`, it delivers text-to-image generation in approximately 4 seconds at $0.041 per image, making it ideal for quick concept visualization, rapid prototyping, and iterative design exploration.

## 

​

What Nano Banana 2 Lite is good at

  * **Ultra-fast generation** : Text-to-image outputs in as little as 4 seconds, built for interactive prototyping and rapid visual drafting
  * **Cost-efficient** : Priced at $0.041 per 1K-resolution image, the most affordable option in the Nano Banana family
  * **Character consistency** : Maintain character identities and object fidelity across multiple rapid generations
  * **In-image text rendering** : Draft copy and render legible text directly into generated images for localized ad variations
  * **Configurable model selection** : Choose between Nano Banana 2 Lite, Nano Banana 2, and Nano Banana Pro within the same node



## 

​

Example outputs

Text-to-image generation from a single prompt: ![Nano Banana 2 Lite Text to Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_lite_t2i.png) Image editing from a text instruction: ![Nano Banana 2 Lite Image Edit - Output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_lite_image_edit.png)

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

Workflows

### 

​

Text to Image

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Nano Banana 2 Lite” in Template Library

Generate images from text descriptions. No file inputs required — just enter your prompt and the workflow produces one or more generated images with support for interleaved text and image inputs. ![Nano Banana 2 Lite Text to Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_lite_t2i.png)

### 

​

Image Edit

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Nano Banana 2 Lite” in Template Library

## Download Sample Image

Get the example input image for this workflow

Upload an image and provide a text instruction to edit it. The workflow produces a side-by-side comparison of the original and edited result.

![Nano Banana 2 Lite Image Edit - Input](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/red_f1_track_car.png)![Nano Banana 2 Lite Image Edit - Output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_lite_image_edit.png)

## 

​

Which model should you pick?

Model| Best for  
---|---  
**Nano Banana 2 Lite**|  Speed and cost — rapid iteration, high-throughput pipelines, low-latency applications  
**[Nano Banana 2](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2)**|  Most creators — balanced quality and speed for general-purpose image generation and editing  
**[Nano Banana Pro](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-pro)**|  Professional use cases — maximum quality, 4K generation, complex layouts and precise control  
  
## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Double-click the canvas and search for the “Nano Banana 2” node (it includes Nano Banana 2 Lite as a model option)
  3. Or go to the Template Library to use the ready-to-go workflow
  4. Select “Nano Banana 2 Lite” from the model dropdown for fastest generation



Nano Banana 2 Lite is available within the existing Nano Banana 2 node. If you have old workflows using this node, you can select “Nano Banana 2 Lite” from the model version dropdown without rebuilding your workflow.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/google/nano-banana-2-lite.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/google/nano-banana-2-lite)

[Nano Banana 2 - Fast AI Image GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2)[Nano Banana 2.1: AI Image Generation and Editing in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-1)

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
