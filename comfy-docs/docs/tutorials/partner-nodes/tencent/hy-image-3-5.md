---
url: https://docs.comfy.org/tutorials/partner-nodes/tencent/hy-image-3-5/
title: Tencent Hunyuan Image 3.5 Preview in ComfyUI: Text to Image and Edit Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:38.365301+00:00
---

# Tencent Hunyuan Image 3.5 Preview in ComfyUI: Text to Image and Edit Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/tencent/hy-image-3-5/

## On this page

  * What HY Image 3.5 Preview is good at
  * Tencent HY Image 3.5 Preview text to image workflow
    * Steps to run the workflow
  * Tencent HY Image 3.5 Preview image edit workflow
    * Steps to run the workflow
    * Prompting tips
  * Get started



Tencent

# Tencent Hunyuan Image 3.5 Preview in ComfyUI: Text to Image and Edit Workflows

Copy pageCopy page

Generate and edit images with Tencent Hunyuan Image 3.5 Preview in ComfyUI: multilingual text rendering, 5 reference images, and 4K output upscaled from 2K.

Copy pageCopy page

Tencent Hunyuan Image 3.5 Preview is Tencent’s preview image model, available in ComfyUI through Partner Nodes. It generates images from text and edits existing images from an instruction, with a focus on multilingual text rendering, photorealism, and consistency between a reference image and the edited result. Compared with earlier Hunyuan image models, HY Image 3.5 Preview strengthens three areas: multilingual text rendering and typesetting for advertising, infographics, and UI design; photorealism and stylistic range across cinematic, comic, commercial photography, and illustration; and editing consistency that preserves the key traits of people and products across background, outfit, and style changes. Two workflows are available. `Tencent HY Image: Text to Image` generates an image from a prompt, and `Tencent HY Image: Edit` edits or combines up to five reference images. Both run on Tencent’s servers through Comfy API, so no model downloads or local GPU are required.

## 

​

What HY Image 3.5 Preview is good at

  * **Multilingual text and typesetting** : renders legible text for posters, infographics, and UI mockups instead of plain scene images
  * **Photorealistic range** : covers cinematic stills, comic art, commercial photography, and illustration from short prompts
  * **Editing consistency** : keeps the defining traits of people and products stable when you change the background, outfit, or style
  * **Up to 5 reference images** : combine several images in one edit and reference each one in the prompt
  * **Output up to 4K** : renders up to 2K natively and upscales 4K output from a 2K render



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

Tencent HY Image 3.5 Preview text to image workflow

Generate one image from a text prompt. The model rewrites and expands the prompt before rendering, so short prompts work.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HY Image 3.5” in Template Library

![Poster reading HY Image 3.5 Preview in white capitals over a glossy liquid-metal shape with iridescent highlights on a dark background](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_tencent_hy_image_3_5_preview_t2i.png)

### 

​

Steps to run the workflow

  1. Edit the `prompt` in the `Tencent HY Image: Text to Image` node
  2. (Optional) Set `aspect_ratio` to control the output shape. With `auto` the model picks the aspect ratio from the prompt, and `auto` is not available at 4K
  3. (Optional) Change `resolution` from the default `2K`. `1K` is about 1024x1024 and `2K` is about 2048x2048 pixels. `4K` output is rendered at 2K and then upscaled by the model
  4. (Optional) Switch `resolution` to `custom` to set an exact `width` and `height` instead. Both must be multiples of 16 and the total area can be up to 4096x4096. Above roughly a 6:1 ratio the model starts repeating the subject
  5. Click `Run` or press `Ctrl(cmd) + Enter` to generate the image
  6. View the result in the `Save Image` node



## 

​

Tencent HY Image 3.5 Preview image edit workflow

Edit or combine up to five reference images from a text instruction. Use it to change a background, swap an outfit, restyle a product shot, or merge several references into one image while keeping the subject’s defining traits. ![Tencent HY Image 3.5 Preview image edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tencent_hy_image_3_5_preview_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HY Image 3.5” in Template Library

![Angular matte black concept motorcycle on an orange paddock stand against a deep red background](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/futuristic_brutalist_motorcycle.png)

### 

​

Steps to run the workflow

  1. Upload the sample image into the `Load Image` node that is already connected to the `Tencent HY Image: Edit` node. The downloaded workflow refers to the file by name (`futuristic_brutalist_motorcycle.png`), so that node stays empty until you upload it. To edit your own images instead, connect 1 to 5 images to the `images` input of the `Tencent HY Image: Edit` node
  2. Write the editing instruction in `prompt`. Reference the inputs in order as `@Image1`, `@Image2`, and so on. A batched input counts once per image
  3. (Optional) Set `aspect_ratio` and `resolution`. With `auto`, the output follows the aspect ratio of the first reference image. `4K` output is rendered at 2K and then upscaled by the model
  4. (Optional) Set `reference_detail` to `high` to let the model see references at up to 2048x2048 pixels instead of 1024x1024. This preserves small text and fine detail better but takes longer
  5. Click `Run` or press `Ctrl(cmd) + Enter` to generate the image
  6. View the result in the `Save Image` node



### 

​

Prompting tips

  * Describe the edit and the parts that must stay unchanged separately, for example `@Image1 change the background to a night market, keep the subject and jacket unchanged`
  * Number references in the order they are connected. The numbering in the prompt has to match the input order
  * `watermark` sits in the node’s advanced options and is off by default. Turn it on to add an AI-generated watermark to the output



## 

​

Get started

  1. Update ComfyUI to the latest version, or use [Comfy Cloud](https://cloud.comfy.org/?utm_source=docs&utm_medium=referral&utm_campaign=hy-image-3-5)
  2. Go to Template Library and search for `HY Image 3.5`
  3. Open the text to image or image edit workflow and run it



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/tencent/hy-image-3-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/tencent/hy-image-3-5)

[Runway Image Generation in ComfyUI: Text-to-Image and Reference ImagesPrevious](https://docs.comfy.org/tutorials/partner-nodes/runway/image-generation)[Topaz Image Enhance Wonder 3.5 - AI image enhancementNext](https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5)

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
