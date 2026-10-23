---
url: https://docs.comfy.org/tutorials/basic/upscale/
title: ComfyUI Image Upscale Workflow - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:18.370337+00:00
---

# ComfyUI Image Upscale Workflow - ComfyUI

> Source: https://docs.comfy.org/tutorials/basic/upscale/

## On this page

  * What is Image Upscaling?
  * Upscaling Workflow
    * Model Installation
    * Workflow and Assets
    * Complete the Workflow Step by Step
  * Text-to-Image Combined Workflow
  * Additional Tips



Basic Examples

# ComfyUI Image Upscale Workflow

Copy pageCopy page

Upscale images in ComfyUI: load an upscale model, build the workflow, and chain it after text-to-image for higher resolution outputs.

Copy pageCopy page

## 

​

What is Image Upscaling?

Image Upscaling is the process of converting low-resolution images to high-resolution using algorithms. Unlike traditional interpolation methods, AI upscaling models (like ESRGAN) can intelligently reconstruct details while maintaining image quality. For instance, the default SD1.5 model often struggles with large-size image generation. To achieve high-resolution results,we typically generate smaller images first and then use upscaling techniques. This article covers one of many upscaling methods in ComfyUI. In this tutorial, we’ll guide you through:

  1. Downloading and installing upscaling models
  2. Performing basic image upscaling
  3. Combining text-to-image workflows with upscaling



Looking for more advanced upscaling options? Check out our comprehensive [Image Upscaling Guide](https://docs.comfy.org/tutorials/utility/image-upscale) which covers various models and use cases including portrait enhancement, product photography, and more.

## 

​

Upscaling Workflow

### 

​

Model Installation

Required ESRGAN models download:

1

Visit OpenModelDB

Visit [OpenModelDB](https://openmodeldb.info/) to search and download upscaling models (e.g., RealESRGAN)![openmodeldb](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e5a63a5efe9b72af78d7331179cef6ba)As shown:

  1. Filter models by image type using the category selector
  2. The model’s magnification factor is indicated in the top-right corner (e.g., 2x in the screenshot)

We’ll use the [4x-ESRGAN](https://openmodeldb.info/models/4x-ESRGAN) model for this tutorial. Click the `Download` button on the model detail page.![OpenModelDB_download](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=678b9869dfcf612056bdc38fcec2f8f4)

2

Save Model Files in Directory

Save the model file (.pth) in `ComfyUI/models/upscale_models` directory

### 

​

Workflow and Assets

Download and drag the following image into ComfyUI to load the basic upscaling workflow: ![Upscale workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/upscale_workflow.png)

Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.

Use this image in smaller size as input: ![Upscale-input](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ce8c5f3cd94c0cbde5ded50f09204d5b)

### 

​

Complete the Workflow Step by Step

Follow the steps in the diagram below to ensure the workflow runs correctly. ![Upscale workflow](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=632d1202982e8e7c59974a4152304967)

  1. Ensure `Load Upscale Model` loads `4x-ESRGAN.pth`
  2. Upload the input image to the `Load Image` node
  3. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to generate the image

The core components are the `Load Upscale Model` and `Upscale Image (Using Model)` nodes, which receive an image input and upscale it using the selected model.

## 

​

Text-to-Image Combined Workflow

After mastering basic upscaling, we can combine it with the [text-to-image](https://docs.comfy.org/tutorials/basic/text-to-image) workflow. For text-to-image basics, refer to the [text-to-image tutorial](https://docs.comfy.org/tutorials/basic/text-to-image). Download and drag this image into ComfyUI to load the combined workflow: ![Text-to-image upscale workflow](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=98c8d536f0a76025092f8fec157002f8) This workflow connects the text-to-image output image directly to the upscaling nodes for final processing.

## 

​

Additional Tips

Model characteristics:

  * **RealESRGAN** : General-purpose upscaling
  * **BSRGAN** : Excels with text and sharp edges
  * **SwinIR** : Preserves natural textures, ideal for landscapes



  1. **Chained Upscaling** : Combine multiple upscale nodes (e.g., 2x → 4x) for ultra-high magnification
  2. **Hybrid Workflow** : Connect upscale nodes after generation for “generate+enhance” pipelines
  3. **Comparative Testing** : Different models perform better on specific image types - test multiple options



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/basic/upscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/basic/upscale)

[Outpainting Workflow ExamplePrevious](https://docs.comfy.org/tutorials/basic/outpaint)[ComfyUI LoRA ExampleNext](https://docs.comfy.org/tutorials/basic/lora)

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
