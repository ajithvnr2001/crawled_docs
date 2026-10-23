---
url: https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-1/
title: Nano Banana 2.1: AI Image Generation and Editing in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:29.379879+00:00
---

# Nano Banana 2.1: AI Image Generation and Editing in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-1/

## On this page

  * What Nano Banana 2.1 is good at
  * Example outputs
  * Use it
  * Workflows
    * Text to Image
    * Image Edit
  * Settings that matter
  * Which model should you pick?
  * Get started



Google

# Nano Banana 2.1: AI Image Generation and Editing in ComfyUI

Copy pageCopy page

Generate and edit images with Nano Banana 2.1 in ComfyUI, with 1K to 4K output, three thinking levels, and up to 14 reference images

Copy pageCopy page

Nano Banana 2.1 (`gemini-nano-banana-2.1`) is available in ComfyUI through Partner Nodes. One node covers both text-to-image generation and image editing: start from a prompt, or connect reference images and describe the change you want.

## 

​

What Nano Banana 2.1 is good at

  * **Generation and editing in one node** : the same node handles text-to-image and image editing, so you can iterate on a result without rebuilding the workflow
  * **1K, 2K and 4K output** : choose the resolution that fits the job, from quick drafts to large, detailed images
  * **Adjustable thinking level** : `MINIMAL`, `MEDIUM` and `HIGH` control how much the model reasons before it draws. Nano Banana 2.1 starts at `MEDIUM`, while the other two models start at `MINIMAL`
  * **Up to 14 reference images** : connect several images in one call to guide subject, style or layout
  * **Model switching without rewiring** : the model dropdown also runs Nano Banana 2 and Nano Banana 2 Lite in the same node



## 

​

Example outputs

Text to image, using the workflow’s default prompt: ![Poster with oversized white NANO BANANA 2.1 type over a yellow banana wrapped in translucent glass rings on a black background](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_1_t2i.png) Image edit, from one input image plus the instruction “Change the background to dark, and relight this portrait with dramatic blue light from the front and a warm amber rim light from behind”:

![Profile portrait of a bearded man wearing silver wrap-around sunglasses and a silver chain, against a pale grey sky](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/silver_frame_profile.png)![The same portrait against a dark background, lit by warm amber rim light from behind and cool blue light from the front](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_1_image_edit.png)

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

Download JSON or search “Nano Banana 2.1” in Template Library

Write the description of the image you want and run the workflow. No input files are needed: the prompt is the only input, `aspect_ratio` decides the shape (see below), and the result is saved as a PNG.

### 

​

Image Edit

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Nano Banana 2.1” in Template Library

## Download Sample Image

Get the example input image for this workflow

Load an image into the `Load Image` node and describe the edit in the prompt. The workflow wires the image into the model’s reference input and adds an `Image Compare` node, so you can check the original against the result in the same canvas.

## 

​

Settings that matter

Setting| What it does  
---|---  
`aspect_ratio`| `auto` matches the aspect ratio of the first reference image, and with no reference image it usually returns a 16:9 image. The other values are fixed ratios: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, `1:4`, `4:1`, `8:1`, `1:8`  
`resolution`| `1K`, `2K` or `4K` output. Higher resolutions cost more per image  
`thinking_level`| `MINIMAL` is the fastest and adds no reasoning cost; `MEDIUM` and `HIGH` spend more time and credits on the model’s reasoning before it draws. Nano Banana 2.1 starts at `MEDIUM`  
`response_modalities`| `IMAGE` returns the picture. `IMAGE+TEXT` also returns the model’s text, which appears on the `text` and `thought_image` outputs  
`seed`| Fix a value to make repeated runs as close to identical as the model allows  
  
`temperature` and `top_p` are exposed by the node, and Nano Banana 2.1 does not send them. They apply when you switch the model dropdown to Nano Banana 2 or Nano Banana 2 Lite.

## 

​

Which model should you pick?

Model| Output resolutions| Thinking levels| Best for  
---|---|---|---  
**Nano Banana 2.1**|  1K, 2K, 4K| MINIMAL, MEDIUM, HIGH| Editing and generation where layout and detail matter  
**[Nano Banana 2](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2)**|  1K, 2K, 4K| MINIMAL, HIGH| Balanced quality and speed at larger sizes  
**[Nano Banana 2 Lite](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-lite)**|  1K| MINIMAL, HIGH| The fastest and cheapest option for drafts and high-volume runs  
  
## 

​

Get started

  1. Update ComfyUI to 0.39.1 or newer: the workflows use the `Nano Banana 2.1` node
  2. Double-click the canvas and search for “Nano Banana 2.1”, or open the Template Library and pick Text to Image or Image Edit
  3. Enter a prompt. For editing, load an image into the `Load Image` node first
  4. Choose the resolution and thinking level, then run the workflow



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/google/nano-banana-2-1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/google/nano-banana-2-1)

[Nano Banana 2 Lite: Fast AI Image GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-lite)[Grok in ComfyUI: AI Image and Video GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-overview)

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
