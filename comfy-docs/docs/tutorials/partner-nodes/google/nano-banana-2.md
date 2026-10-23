---
url: https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2/
title: Nano Banana 2 - Fast AI Image Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:29.642410+00:00
---

# Nano Banana 2 - Fast AI Image Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2/

## On this page

  * What Nano Banana 2 is good at
  * Example outputs
  * Use it
  * Nano Banana 2 image edit workflow
  * Character turnaround sheet workflow
  * Which model should you pick?
  * Get started



Google

# Nano Banana 2 - Fast AI Image Generation

Copy pageCopy page

Generate high-quality images with Pro-level quality at Flash speed using Nano Banana 2 in ComfyUI

Copy pageCopy page

Nano Banana 2 is now available in ComfyUI through Partner Nodes. This release fundamentally changes the default choice for most creators, delivering Pro-level quality at Flash speed.

## 

​

What Nano Banana 2 is good at

  * **Pro-level quality at Flash speed** : Richer textures, sharper detail, stronger lighting, and better prompt adherence without the latency tradeoff
  * **Search-grounded world knowledge** : Intelligently triggers Google Image Search grounding to improve factual accuracy for lesser-known landmarks, niche objects, or real-world details
  * **Subject consistency** : Maintain character resemblance of up to 5 characters and fidelity of up to 14 objects in a single workflow
  * **Configurable thinking levels** : Control how much the model “thinks” before generating (Minimal for fast exploration, High/Dynamic for complex layouts)
  * **Precision text rendering and translation** : Generate accurate, legible text for marketing mockups, greeting cards, and localized assets



## 

​

Example outputs

Text replacement in an existing image, keeping quality intact: ![Quality comparison](https://substack-post-media.s3.amazonaws.com/public/images/1f92ae2e-14d8-4a3b-9ed7-e57dacd2584f_1825x1696.png) _Replace the text from the input image with: Nano Banana 2 Available on ComfyUI Cheaper and Faster_ Search-grounded world knowledge for factually accurate infographics: ![Educational infographic](https://substack-post-media.s3.amazonaws.com/public/images/edfe3b6b-8942-472e-8772-a3700946fc23_1024x559.png) _Educational comic book style infographic explaining five lesser-known North American native species, with search-grounding to ensure accurate depictions of rare habitats and ecological roles._ ![Skateboard culture infographic](https://substack-post-media.s3.amazonaws.com/public/images/536b845b-b278-4924-b8e4-114e5e5defa9_2752x1536.png) _Comic book style infographic for American skateboard culture evolution from the 1970s to the 2020s._ Subject consistency across a storyboard sequence: ![Subject consistency](https://substack-post-media.s3.amazonaws.com/public/images/e38f7afb-9752-49a1-9e6c-1ea99dba42ff_4908x2626.png) _Maintain character resemblance and object fidelity across storyboard sequences._ Configurable thinking levels for different reasoning depth: ![Thinking levels comparison](https://substack-post-media.s3.amazonaws.com/public/images/6d0d4773-3ff5-4319-bc00-8afb62c2a1ad_4608x1332.png) _Cinematic portrait with different thinking levels: Minimal for quick iterations, High for detailed outputs._ ![Art Nouveau portrait](https://substack-post-media.s3.amazonaws.com/public/images/49e5f98a-b375-4fda-b280-7b695f535807_4608x1332.png) _Art Nouveau inspired portrait with configurable reasoning depth._ Text rendering and translation into localized variants: ![Text rendering](https://substack-post-media.s3.amazonaws.com/public/images/808ca8d0-acac-470d-a666-23e411254276_1376x768.png) _Amateur cellphone photograph with stylized graffiti text rendering._ ![Spanish translation](https://substack-post-media.s3.amazonaws.com/public/images/6af9b091-7bbe-49da-b70f-e766394039ef_2784x1536.png) _Translate text to Spanish._ ![Hindi translation](https://substack-post-media.s3.amazonaws.com/public/images/548d44f6-d43e-484f-a8d8-37638f9ff482_2784x1536.png) _Translate text to Hindi._ ![Mandarin translation](https://substack-post-media.s3.amazonaws.com/public/images/5f4a52f9-1995-440f-8394-245e43f3a9a2_2784x1536.png) _Translate text to Mandarin._

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

Nano Banana 2 image edit workflow

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Nano Banana 2” in Template Library

![Nano Banana 2 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana2_image_edit-1.webp)

## Download Sample Input Image

Get the example input image for this workflow

## 

​

Character turnaround sheet workflow

Generate a character turnaround sheet from a single reference image: front, side, and back views of the same subject on one sheet. The sheet feeds directly into the [Pixal3D Multi Views to 3D](https://docs.comfy.org/tutorials/3d/pixal3d#pixal3d-multi-views) workflow, or you can use it as a character reference sheet for video and image generation.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Character Turnaround Sheet Generator” in Template Library

![Character turnaround sheet workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana_create_turnaround_sheet-1.webp)

## Download Sample Input Image

Get the example input image for this workflow

## 

​

Which model should you pick?

Model| Best for  
---|---  
**Nano Banana 2**|  Most creators: fast enough to explore, smart enough to refine, polished enough to ship  
**Nano Banana Pro**|  Maximum factual precision and high-stakes edge cases  
  
## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Double-click the canvas and search for the “Nano Banana 2” node
  3. Or go to the Template Library to use the ready-to-go workflow
  4. Choose your resolution, set your aspect ratio, and decide whether the prompt needs deeper reasoning



The new model version has also been added to the previous “Nano Banana Pro” node. If you have old workflows with this node, you don’t need to rebuild them: just reselect the model version.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/google/nano-banana-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/google/nano-banana-2)

[Nano Banana Pro: Studio-Quality AI Image GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-pro)[Nano Banana 2 Lite: Fast AI Image GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-lite)

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
