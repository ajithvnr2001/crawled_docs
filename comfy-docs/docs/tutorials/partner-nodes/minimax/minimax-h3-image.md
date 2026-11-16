---
url: https://docs.comfy.org/tutorials/partner-nodes/minimax/minimax-h3-image/
title: MiniMax H3 Image API: Text to Image and Image Edit in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:58.245305+00:00
---

# MiniMax H3 Image API: Text to Image and Image Edit in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/minimax/minimax-h3-image/

## On this page

Back to top

  * What MiniMax H3 Image is good at
  * Text to image
  * Image edit
  * Options
  * Get started



MiniMax

# MiniMax H3 Image API: Text to Image and Image Edit in ComfyUI

Copy pageCopy page

Generate 2K or 4K images from a prompt, or edit up to 16 reference images with MiniMax H3 Image through the ComfyUI partner API.

Copy pageCopy page

MiniMax H3 Image is MiniMax’s image model, available in ComfyUI through the **MiniMax H3 Image** partner node. Text to image and image editing use the same node: with no reference images connected it generates from your prompt, and with references connected it edits or combines them. The workflows run on MiniMax’s servers through your Comfy API account, so there are no model downloads and no local GPU to manage.

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

## What MiniMax H3 Image is good at

  * **2K and 4K output** : pick a size tier and an aspect ratio, or set an exact width and height
  * **Image editing** : edit or combine up to 16 reference images, addressed in the prompt as `@Image1` to `@Image16`
  * **Prompt rewriting** : MiniMax expands a short prompt into a detailed scene description by default and returns the rewritten prompt with the image
  * **Poster-grade detail** : suited to posters, packaging, and editorial images that need legible text and dense detail



## Text to image

Generate an image from a prompt at 2K or 4K. ![MiniMax H3 Image text to image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_image_t2i-1.webp)

## Download Workflow

Download JSON or search “MiniMax-H3-Image: Text to Image (API)” in Template Library

## Image edit

Connect a source image, describe the change, and only what the prompt asks for is rewritten. The template adds a woman to a finished render and keeps the rest of the frame. ![MiniMax H3 Image edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_image_image_edit-1.webp)

## Download Workflow

Download JSON or search “MiniMax-H3-Image: Image Edit (API)” in Template Library

**Input materials**

## surreal_rendering_modern.png

`LoadImage` · `surreal_rendering_modern.png`

## Options

Input| Values| Notes  
---|---|---  
`model`| `MiniMax-H3-Image`, `MiniMax-H3-Image-Highspeed`| In the template, change the `model` dropdown to switch  
`size`| `2K`, `4K`, `custom`| 2K and 4K derive width and height from the aspect ratio. `custom` takes a width and height from 512 to 7680 px each, with 655,360 to 20,000,000 px in total and an aspect ratio of at most 3:1  
`aspect_ratio`| `auto` plus 15 fixed ratios| `auto` follows the prompt, or the reference image when one is connected  
`enhance_prompt`| on by default| MiniMax rewrites the prompt into a detailed scene description first. Edits are always enhanced, so turning it off only affects text to image, which then needs a fixed ratio or a custom size  
`images`| up to 16| Reference images for editing and combining. Refer to them in the prompt as `@Image1`, `@Image2`, and so on, in connection order  
  
Prompts can be up to 8,000 characters when reference images are connected. The node also returns the rewritten `revised_prompt` next to the image.

## Get started

  1. Update ComfyUI to 0.45.1 or later
  2. In the Template Library, search for `MiniMax-H3-Image`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/minimax/minimax-h3-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/minimax/minimax-h3-image)

[Muse Image](https://docs.comfy.org/tutorials/partner-nodes/meta/muse-image)[GPT Image 2.6](https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2-6)
