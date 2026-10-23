---
url: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image/
title: FLUX 1.1 Pro Ultra in ComfyUI: 4 MP Text-to-Image and Image Remix - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:26.009096+00:00
---

# FLUX 1.1 Pro Ultra in ComfyUI: 4 MP Text-to-Image and Image Remix - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image/

## On this page

  * What FLUX 1.1 Pro Ultra Image is good at
  * Example outputs
  * Use it
  * FLUX 1.1 Pro Ultra Image Node Documentation
  * FLUX 1.1 [pro] Text-to-Image Tutorial
    * 1\. Download Workflow File
    * 2\. Complete the Workflow Steps
  * FLUX 1.1[pro] Image-to-Image Tutorial
    * 1\. Download Workflow File
    * 2\. Complete the Workflow Steps



Black Forest Labs

# FLUX 1.1 Pro Ultra in ComfyUI: 4 MP Text-to-Image and Image Remix

Copy pageCopy page

Use the FLUX 1.1 Pro Ultra partner node in ComfyUI for 4 MP text-to-image generation in Ultra or Raw mode, plus image-to-image remixing.

Copy pageCopy page

FLUX 1.1 Pro Ultra is a high-performance AI image generation tool by BlackForestLabs, featuring ultra-high resolution and efficient generation capabilities. It supports up to 4MP resolution (4x the standard version) while keeping single image generation time under 10 seconds - 2.5x faster than similar high-resolution models. The tool offers two core modes:

  * **Ultra Mode** : Designed for high-resolution needs, perfect for advertising and e-commerce where detail magnification is important. It accurately reflects prompts while maintaining generation speed.
  * **Raw Mode** : Focuses on natural realism, optimizing skin tones, lighting, and landscape details. Reduces the “AI look” and is ideal for photography and realistic style creation.



## 

​

What FLUX 1.1 Pro Ultra Image is good at

  * **Ultra-high resolution** : Generates images up to 4MP, 4x the standard version’s resolution
  * **Fast generation** : Keeps single image generation time under 10 seconds, 2.5x faster than similar high-resolution models
  * **Prompt accuracy at scale** : Ultra Mode reflects prompts accurately while maintaining generation speed, suited to advertising and e-commerce work
  * **Natural realism** : Raw Mode optimizes skin tones, lighting, and landscape details to reduce the “AI look”
  * **Image-to-image remixing** : An `image_prompt` input blends features from an input image, with `image_prompt_strength` controlling the blend ratio



## 

​

Example outputs

Text-to-image generation with the Flux 1.1 [pro] Ultra Image node: ![FLUX 1.1 pro Text-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_t2i.png) Image-to-image remixing, blending features from an input image into the output: ![FLUX 1.1 pro Image-to-Image Remix](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_i2i.png)

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

FLUX 1.1 Pro Ultra Image Node Documentation

Check the following documentation for detailed node parameter settings:

  * [FLUX 1.1 Pro Ultra Image](https://docs.comfy.org/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg)



## 

​

FLUX 1.1 [pro] Text-to-Image Tutorial

### 

​

1\. Download Workflow File

Download and drag the following file into ComfyUI to load the workflow: ![FLUX 1.1 pro Text-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_t2i.png)

### 

​

2\. Complete the Workflow Steps

![Workflow Steps](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b9403dd3baf434686961672addef2a39) Follow the numbered steps to complete the basic workflow:

  1. (Optional) Modify the prompt in the `Flux 1.1 [pro] Ultra Image` node
  2. (Optional) Set `raw` parameter to `false` for more realistic output
  3. Click `Run` or use shortcut `Ctrl(cmd) + Enter` to generate the image
  4. After the API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory



## 

​

FLUX 1.1[pro] Image-to-Image Tutorial

When adding an `image_prompt` to the node input, the output will blend features from the input image (Remix). The `image_prompt_strength` value affects the blend ratio: higher values make the output more similar to the input image.

### 

​

1\. Download Workflow File

Download and drag the following file into ComfyUI, or right-click the purple node in the Text-to-Image workflow and set `mode` to `always` to enable `image_prompt` input: ![FLUX 1.1 pro Image-to-Image Remix](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_i2i.png) We’ll use this image as input: ![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-3/text2image.png)

### 

​

2\. Complete the Workflow Steps

![Workflow Steps](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0217606be6c3f599e3d6ebd2fb14829a) Follow these numbered steps:

  1. Click **Upload** on the `Load Image` node to upload your input image
  2. (Optional) Adjust `image_prompt_strength` in `Flux 1.1 [pro] Ultra Image` to change the blend ratio
  3. Click `Run` or use shortcut `Ctrl(cmd) + Enter` to generate the image
  4. After the API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory

Here’s a comparison of outputs with different `image_prompt_strength` values: ![Comparison](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=eea7014b92e63f0b8d1bb50d5dae11c3)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image)

[Image ModelsPrevious](https://docs.comfy.org/tutorials/partner-nodes/image/overview)[FLUX.1 Kontext in ComfyUI: Pro and Max Image EditingNext](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-kontext)

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
