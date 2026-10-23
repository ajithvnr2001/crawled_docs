---
url: https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-4-5/
title: Ideogram 4.5 in ComfyUI: Text to Image and Edit - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:32.190953+00:00
---

# Ideogram 4.5 in ComfyUI: Text to Image and Edit - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-4-5/

## On this page

  * Text to Image
  * Image Edit
  * Precise Edit



Ideogram

# Ideogram 4.5 in ComfyUI: Text to Image and Edit

Copy pageCopy page

Run the Ideogram 4.5 partner nodes in ComfyUI for text to image, image edit, and precise edit that keeps untouched pixels identical

Copy pageCopy page

**Ideogram 4.5** is the newer model in the family and Ideogram’s most precise edit model: it changes only what the prompt asks for, so repeated edits keep colors, textures, and details in place. It ships in ComfyUI as three partner nodes that are billed per image through the same Comfy account as the rest of the partner nodes. Ideogram 4.0 keeps its own page: [Ideogram 4.0 in ComfyUI](https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-v4).

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

Text to Image

Generate an image from a text prompt, at a canvas size and quality tier you choose. ![Ideogram 4.5 text to image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Ideogram 4.5: Text to Image” in Template Library

![Ideogram 4.5 text to image example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_ideogram_v4_5_t2i.png) The **Ideogram 4.5 Text to Image** node takes:

Input| Values| Effect  
---|---|---  
`prompt`| up to 10000 characters| The image description. A structured JSON caption works here too, for example a `final_prompt` from an earlier run  
`size`| `auto` or a 1K or 2K preset| `auto` lets the model pick a canvas that suits the prompt. Presets cover both 1K and 2K and run from `1:1` to `23:9`, for example `(2K) 2048x2048 (1:1)` and `(1K) 1280x720 (16:9)`  
`quality`| `low`, `medium` (default), `high`| Higher tiers cost more and take longer  
`magic_prompt`| `auto` (default), `on`, `off`| Rewrites the prompt into a detailed structured caption before generating. `off` keeps your wording as literal as possible  
`seed`| integer| Text to image is not reproducible from the seed alone, because the prompt is rewritten on every run  
  
The node also outputs `final_prompt`, the structured caption the image was generated from. To reproduce an image, feed that caption back with `magic_prompt` set to `off` and the same seed.

## 

​

Image Edit

Edit or combine up to five images with one instruction. `image_1` is the image being edited; images 2 to 5 supply design, material, or color references. Address them in the prompt as `@Image1`, `@Image2`, and so on. ![Ideogram 4.5 image edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Ideogram 4.5: Image Edit” in Template Library

**Input material**

## interior_orange_sofa.png

Load into the `image_1` slot on the Ideogram 4.5 Edit node

The template builds its instruction with a **Build JSON Prompt** node, so you can mark a region of the image and caption it, for example “remove it”. Turn on [Nodes 2.0](https://docs.comfy.org/interface/nodes-2) if the editor does not appear. The **Ideogram 4.5 Edit** node adds:

Input| Values| Effect  
---|---|---  
`size`| `auto` (default), `source`, a preset, or `custom`| `auto` picks a canvas of about 2K from the images and the prompt. `source` keeps the size of `image_1`. A preset with a different aspect ratio recomposes the scene. `custom` uses the `width` and `height` below  
`width`, `height`| 256 to 4608, step 32| Used only when `size` is `custom`. The two dimensions together must stay within 4194304 pixels (2048x2048) and within an aspect ratio of 6:1  
`quality`| `very_low`, `low`, `medium` (default), `high`| Higher tiers cost more and take longer  
`seed`| integer| The same images, prompt, settings, and seed give the same result  
  
Up to five images can be connected in total. Inputs above roughly 4 MP are scaled down before they are uploaded, and each image must sit between 1:6 and 6:1. Edit re-renders the whole image, so it can shift the framing and the untouched areas along with the edit. Use Precise Edit when the rest of the picture has to stay exactly as it is.

## 

​

Precise Edit

Change only what the prompt asks for. Untouched pixels stay identical and the output keeps the size of `image_1`. Accepts up to four reference images beyond the image being edited. ![Ideogram 4.5 precise edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_precise_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Ideogram 4.5: Precise Edit” in Template Library

**Input material**

## redhair_girl_portrait.png

Load into the `image_1` slot on the Ideogram 4.5 Precise Edit node

Precise Edit shares the reference slots, `@Image1` addressing, `quality`, and `seed` controls with Edit. It has no size control, because the output always matches the size of `image_1`. The template draws its instruction with the **Build JSON Prompt** node as well. Use it for product recolors, material swaps, and touch-ups that must leave the lighting, background, and framing of the rest of the photo alone.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/ideogram/ideogram-4-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/ideogram/ideogram-4-5)

[ComfyUI Ideogram 4.0 Partner Node TutorialPrevious](https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-v4)[Ideogram P-Image - fast text-to-imageNext](https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-p-image)

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
