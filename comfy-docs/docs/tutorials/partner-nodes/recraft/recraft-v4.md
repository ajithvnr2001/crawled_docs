---
url: https://docs.comfy.org/tutorials/partner-nodes/recraft/recraft-v4/
title: Recraft V4 & V4.1 Image & Vector Generation in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:37.467201+00:00
---

# Recraft V4 & V4.1 Image & Vector Generation in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/recraft/recraft-v4/

## On this page

  * What Recraft V4 is good at
  * Example outputs
  * Recraft V4 text to image workflow
    * Steps to run the workflow
    * Image showcase
  * Recraft V4 text to vector workflow
    * Vector showcase
  * Recraft V4.1 text to image workflow
    * Steps to run the workflow
  * Recraft V4.1 Flash text to image workflow
    * Steps to run the workflow
  * Recraft V4.1 text to vector workflow
  * Recraft V4 styles
    * Recraft V4 style reference workflow
  * Additional notes



Recraft

# Recraft V4 & V4.1 Image & Vector Generation in ComfyUI

Copy pageCopy page

Generate professional images and production-ready vectors with Recraft V4 and V4.1 in ComfyUI

Copy pageCopy page

Recraft V4 is an image generation model built for professional design work. It was developed in collaboration with designers and optimized for composition, lighting, color relationships, and material realism. Recraft V4.1 is the latest update to the model family, designed to interpret short prompts and produce natural photorealism across a range of output styles. Recraft V4.1 Flash is the fastest and lowest-cost model in the V4 family: it generates one image per run from a short prompt and does not support styles.

## 

​

What Recraft V4 is good at

  * **Raster + vector in one model** : photorealistic images, stylized illustrations, and production-ready SVGs from the same model
  * **Better detail** : cleaner textures, more accurate lighting, tighter geometry. Holds up in complex scenes
  * **Faces and anatomy that work** : reliable proportions and expressions, even with multiple subjects or action poses
  * **Text rendering** : legible text for signage, packaging, infographics. Handles short and mid-length phrases well
  * **SVG output** : editable vectors with clean lines and proper color segmentation. Production-quality vector output
  * **Prompt accuracy** : follows detailed creative direction closely, including spatial relationships, materials, and reflections
  * **V4 Pro** : same model, higher resolution. Outputs at 2048×2048 for print and large-format work



## 

​

Example outputs

Editorial photography from a detailed text prompt: ![Street photography example](https://substack-post-media.s3.amazonaws.com/public/images/9fe39ca3-b0ba-4f26-aa26-b3eaa11185de_1792x1024.png) Vector illustration output, ready for editing as SVG: ![Rooftop illustration](https://substack-post-media.s3.amazonaws.com/public/images/571c5214-5c7f-43f9-81c4-80cad1e5578b_1792x1024.png) Recraft V4.1 text-to-image, producing natural photorealism from a short prompt: ![Recraft V4.1 Text to Image output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_recraft_v4_1_t2i.png)

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

Recraft V4 text to image workflow

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Recraft V4 Text to Image” in Template Library

![Recraft V4 Text to Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_t2i-1.webp)

### 

​

Steps to run the workflow

  1. (Optional) Modify the `Recraft Style` node to control the visual style
  2. (Optional) Edit the `prompt` parameter in the `Recraft Text to Image` node
  3. (Optional) Change the `size` parameter for different output dimensions
  4. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to generate the image
  5. After the API returns the result, view the generated image in the `Save Image` node



### 

​

Image showcase

![Street photography example](https://substack-post-media.s3.amazonaws.com/public/images/9fe39ca3-b0ba-4f26-aa26-b3eaa11185de_1792x1024.png) _Full-body editorial street photo of a young person wearing an oversized vintage Fear of God flannel layered over a faded Pyrex Vision hoodie, distressed wide-leg denim, original Just Don python-brim snapback, and beat-up Nike Dunk Lows. Shot on a gritty Brooklyn sidewalk, golden hour, 35mm film grain._ ![Hypebeast editorial](https://substack-post-media.s3.amazonaws.com/public/images/9fd968f1-f5f9-42a9-973d-74bd163babde_2560x1664.png) _Full outfit shot: electric blue and coral camo hoodie, matching camo joggers, white G-Shock watch, matte black techwear crossbody harness bag, and New Balance 550s in a cream colorway. Concrete parking garage backdrop, harsh fluorescent overhead lighting casting sharp shadows._ ![Action shot](https://substack-post-media.s3.amazonaws.com/public/images/a8643f80-8cc4-4246-a95a-bed1f9ee10f1_2560x1664.png) _Fish-eye lens, shot from inside an empty concrete pool: a guy in a shearling bomber and transparent PVC shell is mid-kickflip at the lip of the pool directly above the camera, board separating from his feet, his layered outfit catching air and fanning open revealing the hockey jersey underneath._

## 

​

Recraft V4 text to vector workflow

Recraft V4 can generate production-ready SVG vector outputs directly. This is useful for logos, icons, brand assets, or anything that needs to scale. SVG outputs are compatible with Illustrator, Figma, and Sketch.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Recraft V4 Text to Vector” in Template Library

![Recraft V4 Text to Vector workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_text_to_vector-1.webp)

### 

​

Vector showcase

![Rooftop illustration](https://substack-post-media.s3.amazonaws.com/public/images/571c5214-5c7f-43f9-81c4-80cad1e5578b_1792x1024.png) _A group of friends lounging on a rooftop at sunset, string lights overhead, one person tending a small grill, another strumming a ukulele, a dog napping on a blanket beside a cooler: warm, relaxed, retro lifestyle illustration_ ![Boombox illustration](https://substack-post-media.s3.amazonaws.com/public/images/748f04c7-50b9-433d-93cb-c619984c8e89_1792x1024.png) _A giant neon boombox blasting music, with lightning bolts and sound waves exploding out of the speakers, melting cassette tapes swirling around it, and a pair of oversized headphones draped on top: bold, chaotic, and electrifying_ ![Kitten sticker](https://substack-post-media.s3.amazonaws.com/public/images/3ddce7b4-8f37-4256-bd93-2e5796dfacca_1024x1024.png) _Adorable kitten sticker, the kitten is using ComfyUI on a little tiny laptop_

## 

​

Recraft V4.1 text to image workflow

Generate photorealistic and illustrative images from text prompts using Recraft V4.1, producing one high-quality image per generation. The model interprets short prompts and outputs natural photorealistic results.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Recraft V4.1” in Template Library

![Recraft V4.1 Text to Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_t2i-1.webp) ![Recraft V4.1 Text to Image output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_recraft_v4_1_t2i.png)

### 

​

Steps to run the workflow

  1. (Optional) Modify the `Recraft Style` node to control the visual style
  2. (Optional) Edit the `prompt` parameter in the `Recraft Text to Image` node
  3. (Optional) Change the `size` parameter for different output dimensions
  4. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to generate the image
  5. After the API returns the result, view the generated image in the `Save Image` node



## 

​

Recraft V4.1 Flash text to image workflow

Generate one image per run with Recraft V4.1 Flash, the fastest and lowest-cost model in the V4 family. It supports the standard V4 size presets and no style controls, so it fits high-volume generation, rapid iteration, and quick concept exploration.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Recraft 4.1 flash” in Template Library

![Recraft V4.1 Flash text to image output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_recraft_v4_1_flash_t2i.png)

### 

​

Steps to run the workflow

  1. (Optional) Edit the `prompt` parameter in the `Recraft V4 Text to Image` node
  2. (Optional) Set `model` to `recraftv4_1_flash`
  3. (Optional) Change the `size` parameter for different output dimensions
  4. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to generate the image
  5. After the API returns the result, view the generated image in the `Save Image` node



## 

​

Recraft V4.1 text to vector workflow

Generate a clean, flat vector logo from a text prompt using Recraft V4.1, producing one scalable SVG output with no file input required. Ideal for branding and logo design, vector illustration projects, and consistent flat-color graphics.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Recraft V4.1” in Template Library

![Recraft V4.1 Text to Vector workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_text_to_vector-1.webp)

## 

​

Recraft V4 styles

Recraft V4 and V4.1 generation nodes can apply a reusable style. Pass a `style_id` or connect style reference images to keep every output consistent with the same look.

  * **Recraft V4 Create Style** : Creates a reusable style from 1 to 10 reference images and returns a `style_id`. The style works with every Recraft V4 and V4.1 model of the same output type (raster or vector), and total reference image size is limited to 10 MB
  * **Style-required models** : The `recraftv4_styles` and `recraftv4_styles_pro` models, plus their vector variants, always require a `style_id` or style reference images. Other V4 models accept styles as an optional input
  * **Style inputs** : `style_id` and `style_references` cannot be combined in one run. Style reference images are billed on top of the generation, and the node returns the created `style_id` for reuse
  * **Style match** : `precise` reproduces the style in detail, `flexible` matches the general look



### 

​

Recraft V4 style reference workflow

Generate images in the style of one or more reference images with Recraft V4 Styles. The template creates a reusable `style_id` from four reference images with the Recraft V4 Create Style node, then feeds it into a Recraft V4 Text to Image generation. No training or fine-tuning is required: the style captures texture, composition, and rendering from the references alone. ![Recraft V4 Style Reference workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_style_reference-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Recraft V4: Style-Reference Image Generation” in Template Library

## Style Reference 1: recraft_v4_style_ref_1.png

Style reference for the workflow, or use your own images.

## Style Reference 2: recraft_v4_style_ref_2.png

Style reference for the workflow, or use your own images.

## Style Reference 3: recraft_v4_style_ref_3.png

Style reference for the workflow, or use your own images.

## Style Reference 4: recraft_v4_style_ref_4.png

Style reference for the workflow, or use your own images.

The created style ID is saved to `ComfyUI/output/Recraft_Style_v4/`, and you can customize the output location with the save node’s `filename_prefix`. Reuse the same style ID in future generations to keep the look consistent across runs.

## 

​

Additional notes

  * **Recraft Style** : Offers various preset styles like realistic photos, digital art, and logo designs
  * **Seed Parameter** : Only used to determine if the node should run again; the actual generation result is not affected by the seed value



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/recraft/recraft-v4.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/recraft/recraft-v4)

[Qwen Image 3.0 Pro - Advanced AI Image GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/qwen/qwen-image-3-0-pro)[Recraft Text to Image Partner Nodes ComfyUI Official ExampleNext](https://docs.comfy.org/tutorials/partner-nodes/recraft/recraft-text-to-image)

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
