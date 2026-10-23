---
url: https://docs.comfy.org/tutorials/partner-nodes/bria/image-editing/
title: Bria Eraser, Expand Image, and GenFill in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:26.922587+00:00
---

# Bria Eraser, Expand Image, and GenFill in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bria/image-editing/

## On this page

  * What Bria Image Editing is good at
  * Example outputs
    * Bria: Eraser
    * Bria: Expand Image
    * Bria: Generative Fill
  * Prompt-driven editing (no mask)
    * Bria: Erase by Text
    * Bria: Add Object
    * Bria: Replace Object
    * Bria: Relight
    * Bria: Restore Photo
    * Bria: Reseason
    * Bria: Erase Foreground
    * Bria: Replace Image Background
  * Get started



Bria

# Bria Eraser, Expand Image, and GenFill in ComfyUI

Copy pageCopy page

Remove objects, expand images, and generate content inside masked regions with the Bria Eraser, Expand Image, and Generative Fill partner nodes in ComfyUI.

Copy pageCopy page

Bria’s image editing tools are available in ComfyUI as Partner Nodes. This page covers three mask-based editing workflows: **Bria Eraser** (remove objects), **Bria Expand Image** (outpaint beyond the borders), and **Bria Generative Fill** (generate content inside a masked region). All three keep everything outside the edited area pixel-perfect unchanged.

## 

​

What Bria Image Editing is good at

  * **Object removal** : Bria Eraser erases a masked object or region and fills it with surrounding context, no prompt needed
  * **Image expansion** : Bria Expand Image outpaints beyond the original borders, generating surroundings that match the image’s lighting, perspective, and texture
  * **Generative fill** : Bria Generative Fill regenerates a masked region from a prompt, art-directing new content into the scene
  * **Pixel-perfect preservation** : All three workflows keep everything outside the edited area unchanged



## 

​

Example outputs

Object removal with Bria Eraser, inpainting the background behind the erased region: ![Bria: Eraser example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Bria_Eraser.png) Image expansion with Bria Expand Image, extending the scene beyond its original borders: ![Bria: Expand Image example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Bria_Expand_Image.png) Generative fill, regenerating a masked region from a prompt: ![Bria: Generative Fill example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Bria_GenFill.png) Each workflow takes a single input image plus a mask. The **Painter** node in the templates provides a brush canvas for drawing the mask, and an **ImageCompare** node shows the before/after result side by side. The Painter node is only available under Nodes 2.0; if you only see “Painter: Node 2.0 only”, enable Nodes 2.0 via **Menu - > Nodes2.0**, or use the [Mask Editor](https://docs.comfy.org/interface/maskeditor) to create the mask instead.

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

### 

​

Bria: Eraser

Remove a specific object or region from an image. The masked area is erased and filled with surrounding context; everything outside the mask stays unchanged. ![Bria: Eraser workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_eraser-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria Eraser” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## vintage_girl_yellow_apple.png

Download sample input image

![Bria: Eraser input](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/vintage_girl_yellow_apple.png)![Bria: Eraser example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Bria_Eraser.png)

**How to use**

  1. **Load an image** : Upload your image in `LoadImage`. The Painter canvas and compare view auto-update.
  2. **Paint a mask** : Brush over the object or region you want to remove. Paint slightly beyond the object’s edge (hair, glass, fabric, contact points) so the model has room to blend cleanly.
  3. **Run`BriaEraser`**: No prompt needed. The node erases the masked area and inpaints the background. Enter your `api_key` if it is not already set.
  4. **Compare and save** : `ImageCompare` shows before/after, `SaveImageAdvanced` exports the result.



The masked area is fully regenerated from its surroundings, so the result blends seamlessly. The mask is binary: white (255) marks the region to erase, black (0) everywhere else, and it must match the image’s aspect ratio. For more precise results, use an automatic segmentation mask (SAM-style) if available: the API’s `mask_type` distinguishes `manual` (brush-drawn) from `automatic` (algorithm-generated) masks.

### 

​

Bria: Expand Image

Expand an image beyond its original borders. The original image stays untouched; the surrounding area is generated to match its lighting, perspective, and texture. ![Bria: Expand Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_expand_image-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria Expand Image” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## red_sports_car_night.png

Download sample input image

![Bria: Expand Image input](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/red_sports_car_night.png)![Bria: Expand Image example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Bria_Expand_Image.png)

**How to use**

  1. **Load an image** : Upload your image in `LoadImage` and connect it to `BriaExpandImage`.
  2. **Choose an expansion mode** in the `expand_mode` dropdown: 
     * **Preset aspect ratio** : Pick one of `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`. The image is centered and the edges are expanded to fit that ratio.
     * **Custom ratio** : Pick `custom_ratio` and set `ratio_width` / `ratio_height` (e.g. 21 and 9 for 21:9). Bria accepts width-to-height ratios between 0.5 and 3.0, so anything taller than 1:2 needs the manual mode.
     * **Manual** : Pick `manual` and place the original image on a canvas with `canvas_width` / `canvas_height` (max 5000 x 5000), `image_width` / `image_height`, and `image_x` / `image_y` (the image’s top-left corner; can be negative to crop).
  3. **Prompt (optional)** : Leave it empty and Bria automatically generates a prompt from the input image and expands to match its scene and style. Or write your own to guide the expansion direction explicitly, for example “the street continuing to the right”, “add a streetlamp”, “no other cars”. English only; special characters are not supported.
  4. **Optional** : `negative_prompt` to avoid unwanted content, `seed` to reproduce a result, `moderation` to enable content moderation.
  5. **Save** : Connect the image output to `SaveImage`.



The `prompt` output on the node shows the prompt actually used: your input, or the one auto-generated by Bria when the field is empty. If the target aspect ratio equals the image’s current ratio (e.g. a 1:1 image set to `1:1`), no changes are made and the image is returned as-is. Canvas area is limited to 5,000 x 5,000 pixels. Keep the main subject above 15% of the total canvas area for best results.

### 

​

Bria: Generative Fill

Regenerate a specific region of an image from a prompt. The masked area is fully regenerated; everything outside the mask stays pixel-perfect unchanged. ![Bria: Generative Fill workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_genfill-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Generative Fill” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## retro_girl_cinnamon_bun.png

Download sample input image

![Bria: Generative Fill input](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/retro_girl_cinnamon_bun.png)![Bria: Generative Fill example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Bria_GenFill.png)

**How to use**

  1. **Load an image** : Upload your image in `LoadImage`. The Painter canvas and compare view auto-update.
  2. **Paint a mask** : Brush over the region you want to regenerate. Blob-shaped, brush-drawn masks work best. Paint slightly beyond the object’s edge (hair, glass, fabric, contact points) so the model has room to blend.
  3. **Write the prompt** : In `BriaGenFill`, describe what should be generated inside the masked area, as if art-directing a cropped micro-scene: name the object, its material and size, how it interacts with the surface, and ask for a contact shadow. Around 90-110 words works best. Keep `refine_prompt` enabled.
  4. **Optional** : `negative_prompt` to avoid unwanted details. Use a fixed `seed` to iterate on the mask or wording, then randomize once the result looks right.
  5. **Compare and save** : `ImageCompare` shows before/after, `SaveImageAdvanced` exports the result.



Masks trigger generative replacement, not pixel retouching: the masked area means “regenerate this region”, not “touch up this region”.

## 

​

Prompt-driven editing (no mask)

The nodes below edit an image from a text instruction alone: no Painter canvas, no mask. Each node outputs the edited image plus a `structured_prompt` string that describes the edit, which you can feed into Bria FIBO Image Edit for follow-up edits. All of them cost 12.07 credits per run.

### 

​

Bria: Erase by Text

Remove an object by naming it. Enter the object’s name in `BriaEraseByText`, such as `the lamp`: several objects can be named and removed at once, and no mask is needed.

### 

​

Bria: Add Object

Add a new object to the scene from a prompt, such as `Place a red vase with flowers on the table`. Bria re-imagines the edit on each run, so repeated runs can differ. The node’s `seed` input is never sent to the API. It changes only the node’s cache key, so an otherwise identical graph runs the edit again instead of returning a cached result.

### 

​

Bria: Replace Object

Swap one object for another from a prompt, such as `Replace the red apple with a green pear`. Like Add Object, each run re-imagines the edit.

### 

​

Bria: Relight

Change the lighting of a scene with two dropdowns: `light_type` picks the atmosphere (13 options including midday, blue hour light, sunrise light, spotlight on subject, moonlight lighting, and harsh studio lighting), and `light_direction` picks where the light comes from: `front`, `side`, `bottom`, or `top-down`.

### 

​

Bria: Restore Photo

Repair and restore an old or degraded photo in one click: no prompt and no mask, just connect the image.

### 

​

Bria: Reseason

Change the season of an outdoor scene. Pick `spring`, `summer`, `autumn`, or `winter` in the `season` dropdown and Bria re-renders foliage, lighting, and atmosphere to match.

### 

​

Bria: Erase Foreground

Remove the entire foreground of an image and generate a background in its place.

### 

​

Bria: Replace Image Background

Replace the background of an image. Describe the new background with a prompt, or guide it with up to 10 reference images. The mode dropdown controls how closely the result follows the prompt: `high_control` follows it most closely, `base` is a balanced middle ground, and `fast` trades control for speed. Enable `keep_original_size` to return the input’s exact pixel size instead of scaling the result.

## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Bria Eraser`, `Bria Expand Image`, or `Bria Generative Fill`. The prompt-driven nodes in the section above are available on the node palette without a template.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bria/image-editing.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bria/image-editing)

[Bria FIBO in ComfyUI: JSON-Prompt Image Editing and OutpaintingPrevious](https://docs.comfy.org/tutorials/partner-nodes/bria/fibo)[ByteDance Seedream 5.0 Pro - Professional AI Image GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedream-5-pro)

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
