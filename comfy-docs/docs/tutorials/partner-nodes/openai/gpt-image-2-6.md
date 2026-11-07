---
url: https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2-6/
title: OpenAI GPT Image 2.6: Flare and Sunburst Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-07T13:48:27.246309+00:00
---

# OpenAI GPT Image 2.6: Flare and Sunburst Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2-6/

## On this page

Back to top

  * Getting started
  * Node settings
  * GPT Image 2.6 Flare: Text to Image
  * GPT Image 2.6 Flare: Image Edit
  * GPT Image 2.6 Sunburst: Text to Image
  * GPT Image 2.6 Sunburst: Image Edit



OpenAI

# OpenAI GPT Image 2.6: Flare and Sunburst Workflows

Copy pageCopy page

Generate and edit images in ComfyUI with the OpenAI GPT Image 2.6 Flare and Sunburst partner nodes: fast drafts, detail-first renders, four templates.

Copy pageCopy page

GPT Image 2.6 is OpenAI’s image model family, available in ComfyUI on the **OpenAI GPT Image 2.6** partner node. It comes in two variants:

  * **Flare** (`gpt-image-2.6-flare`): returns a draft in seconds and holds the layout together on dense posters and product shots. Use it for concept passes, mood boards and typography-heavy drafts
  * **Sunburst** (`gpt-image-2.6-sunburst`): spends its render budget on fine texture, small type and materials, and keeps subjects and lighting consistent across passes. Use it for finished visuals and dense layouts where detail has to hold up

Both variants do text to image and image edit, with up to 16 reference images, an optional mask for inpainting, quality levels from `low` to `max`, and a `complexity` control that sets how much the model plans the image before rendering. The node also still offers GPT Image 2.5, GPT Image 2 and GPT Image 1.5.

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

Getting started

  1. Update ComfyUI to 0.44.1 or later
  2. In the Node Library, search for **OpenAI GPT Image 2.6** and add the node
  3. Set `model` to `gpt-image-2.6-flare` or `gpt-image-2.6-sunburst`
  4. Connect the node’s image output to a Save Image node, or open one of the four templates below



## 

​

Node settings

  * **model** : `gpt-image-2.6-flare` for fast iteration, `gpt-image-2.6-sunburst` for detail-first renders
  * **prompt** : what to generate, or the edit instruction when reference images are connected
  * **size** : `auto`, a preset such as `1024x1024` or `3840x2160`, or `Custom`
  * **custom_width / custom_height** : used only when `size` is `Custom`, from 480 to 3840 in steps of 16
  * **background** : `auto`, `opaque`, or `transparent`
  * **quality** : `low`, `medium`, `high`, `xhigh`, or `max`. Affects cost and generation time
  * **complexity** : `low`, `medium`, or `high` (default). How much the model plans the image before rendering
  * **images** : optional reference images for editing, up to 16
  * **mask** : optional mask for inpainting, white areas are replaced. Requires exactly one reference image
  * **n** : how many images to generate, 1 to 8
  * **seed** : kept for API compatibility, the backend does not use it yet

Flare is the cheaper way to find a prompt that works. Run it at `low` or `medium` quality until the composition holds, then re-run the winning prompt on Sunburst for the final image.

## 

​

GPT Image 2.6 Flare: Text to Image

Generate a poster from a text prompt. The template asks for rendered text and a dense layout, which is where Flare’s speed matters: you can iterate on the wording without paying for final quality each time.

## Download Workflow

Download JSON or search “GPT Image 2.6 Flare” in Template Library

![GPT Image 2.6 Flare Text to Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_flare_t2i-1.webp)

## 

​

GPT Image 2.6 Flare: Image Edit

Change one detail of a photo and leave the rest alone: keep the face, pose, framing and lighting, then change the outfit, the hair or a single object.

## Download Workflow

Download JSON or search “GPT Image 2.6 Flare” in Template Library

![GPT Image 2.6 Flare Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_flare_image_edit-1.webp) Upload this file to the `Load Image` node:

## Input image: young_man_windblown.png

The example input image, or use your own

## 

​

GPT Image 2.6 Sunburst: Text to Image

Generate a finished poster with rendered type and fine texture. The template prompt describes one layer at a time: scene, subject, typography, small graphic elements, then the palette and render style.

## Download Workflow

Download JSON or search “GPT Image 2.6 Sunburst” in Template Library

![GPT Image 2.6 Sunburst Text to Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_sunburst_t2i-1.webp)

## 

​

GPT Image 2.6 Sunburst: Image Edit

Edit a photo while the camera angle, framing, subject position and light stay identical. Sunburst renders fine texture and small type, so posters and dense scenes hold up on the second or third pass.

## Download Workflow

Download JSON or search “GPT Image 2.6 Sunburst” in Template Library

![GPT Image 2.6 Sunburst Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_sunburst_image_edit-1.webp) Upload this file to the `Load Image` node:

## Input image: api_openai_gpt_image_26_sunburst_image_edit_input.png

The example input image, or use your own

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/openai/gpt-image-2-6.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/openai/gpt-image-2-6)

[Muse Image](https://docs.comfy.org/tutorials/partner-nodes/meta/muse-image)[GPT Image 2.5](https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2-5)
