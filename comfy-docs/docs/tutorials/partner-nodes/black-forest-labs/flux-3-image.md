---
url: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-image/
title: FLUX 3 Image in ComfyUI: Text to Image and Image Edit - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:26.116028+00:00
---

# FLUX 3 Image in ComfyUI: Text to Image and Image Edit - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-image/

## On this page

  * What FLUX 3 Image is good at
  * Use it
  * FLUX 3 Image text-to-image workflow
    * Text to image steps
  * FLUX 3 Image edit workflow
    * Image edit steps
  * FLUX 3 Image bounding box edit workflow
    * Bounding box edit steps
  * Get started



Black Forest Labs

# FLUX 3 Image in ComfyUI: Text to Image and Image Edit

Copy pageCopy page

Run FLUX 3 Image in ComfyUI for text-to-image generation, multi-reference edits, and bounding-box layout control, at up to 4K with web search grounding.

Copy pageCopy page

FLUX 3 is Black Forest Labs’ multimodal foundation model, announced July 23, 2026 and in Early Access. It learns from images, video, and audio in a single architecture built on Self-Flow, their approach to aligning multimodal generation and understanding in one model. FLUX 3 Image is the part of it that generates and edits still images. Capabilities and limits may change during the Early Access rollout. FLUX 3 Image turns a text prompt into an image, or edits and combines up to 10 reference images. You refer to the references in the prompt as `image 1`, `image 2`, and so on, and the model interprets and expands the prompt before generating. Web and image search grounding is on by default, so it can look up the subjects you name. It returns a single image at any of sixteen aspect ratios and at one of five resolution tiers, from 0.75K (about 0.6 megapixels) up to 4K (about 16.8 megapixels). In ComfyUI, FLUX 3 Image runs through the **FLUX 3 Image** Partner Node and is billed in credits per generated image, by resolution. Three templates cover text-to-image, multi-reference editing, and bounding-box layout control.

## 

​

What FLUX 3 Image is good at

  * **Text to image** : generates one image from a prompt, which the model interprets and expands first
  * **Multi-reference editing** : edits or combines up to 10 reference images, addressed as `image 1` to `image 10` in the prompt
  * **Bounding-box layout control** : places objects and text where you want them with boxes from the Create Bounding Boxes node
  * **Search grounding** : web and image search are on by default, so the model can research named subjects before it draws
  * **Flexible output** : sixteen aspect ratios and five resolution tiers, from 0.75K to 4K
  * **Typography and layout** : suited to posters, headlines, captions, and layout-driven design work



## 

​

Use it

## Call it from code

Call it over HTTP through Comfy Router, with copy-paste Python, TypeScript, Swift and cURL snippets

This runs on the same Comfy account and is billed in the same credits as running it in ComfyUI below. See [Partner Nodes pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for per-resolution rates and [Concurrency limits](https://docs.comfy.org/tutorials/partner-nodes/concurrency-limits) for how many requests you can have in flight.

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

FLUX 3 Image text-to-image workflow

Generate an image from a text prompt. FLUX 3 Image interprets and expands the prompt, then renders it at the resolution you choose. No input files are required. ![FLUX 3 Image text to image workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX 3 Image: Text to Image” in Template Library

### 

​

Text to image steps

  1. Enter a prompt in the **FLUX 3 Image** node
  2. Set `resolution` (0.75K to 4K) and, if you want, an `aspect_ratio` other than `auto`
  3. Leave `grounding` on to let the model search the web and images for the subjects you name
  4. Click **Queue** to generate the image



## 

​

FLUX 3 Image edit workflow

Edit an image, or combine several, from a text instruction. Connect up to 10 reference images and name them in the prompt as `image 1`, `image 2`, and so on. ![FLUX 3 Image edit workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX.3 Image: Image Edit” in Template Library

### 

​

Image edit steps

  1. Upload your reference images to the **Load Image** node, adding more with the Autogrow slots, up to 10
  2. Describe the edit in the **FLUX 3 Image** node, naming each reference as `image 1`, `image 2`, and so on
  3. Set `resolution` and `aspect_ratio` for the output
  4. Click **Queue** to generate the edited image



## 

​

FLUX 3 Image bounding box edit workflow

Place objects and text at exact positions by feeding boxes from the **Create Bounding Boxes** node into the **FLUX 3 Image** node. Boxes are relative to the canvas, so set the output to the same aspect ratio. Each box carries its own description, which joins the prompt. ![FLUX 3 Image bounding box edit workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_image_bboxes-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX 3 Image: Bounding Box Edit” in Template Library

### 

​

Bounding box edit steps

  1. Upload the image to the **Load Image** node
  2. Draw boxes with **Create Bounding Boxes** and give each one a description
  3. Write the overall instruction in the **FLUX 3 Image** node
  4. Set `aspect_ratio` to match the canvas the boxes were drawn on
  5. Click **Queue** to generate the image



## 

​

Get started

  1. Update ComfyUI to the latest version (0.38.2 or later)
  2. Open Template Library and search for `FLUX 3 Image`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/black-forest-labs/flux-3-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/black-forest-labs/flux-3-image)

[FLUX.1 Kontext in ComfyUI: Pro and Max Image EditingPrevious](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-kontext)[Beeble SwitchX in ComfyUI: Relighting and Environment EditingNext](https://docs.comfy.org/tutorials/partner-nodes/beeble/beeble-switchx)

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
