---
url: https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-1/
title: OpenAI GPT-Image-1 in ComfyUI: Text-to-Image and Inpainting - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:06.778765+00:00
---

# OpenAI GPT-Image-1 in ComfyUI: Text-to-Image and Inpainting - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-1/

## On this page

  * What GPT-Image-1 is good at
  * Example outputs
  * Parameter Description
    * Required Parameters
    * Widget Parameters
    * Optional Parameters
  * Usage Examples
    * Text-to-Image Example
    * Image-to-Image Example
    * Multiple Image Input Example
    * Inpainting Workflow
  * FAQs



OpenAI

# OpenAI GPT-Image-1 in ComfyUI: Text-to-Image and Inpainting

Copy pageCopy page

Generate and edit images with OpenAI GPT-Image-1 in ComfyUI: text-to-image, image-to-image from a reference, masked inpainting, and multiple image inputs.

Copy pageCopy page

![OpenAI GPT-Image-1 Node Screenshot](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=243b4200a707b55f1c4fd88d4edf51a9) OpenAI GPT-Image-1 is part of the ComfyUI Partner nodes series that allows users to generate images through OpenAI’s **GPT-Image-1** model. This is the same model used for image generation in ChatGPT 4o. The **OpenAI GPT-Image-1** node synchronously generates images through OpenAI’s image generation API. It receives text prompts and returns images matching the description. GPT-Image-1 is OpenAI’s most advanced image generation model currently available, capable of creating highly detailed and realistic images.

## 

​

What GPT-Image-1 is good at

  * Text-to-image generation
  * Image editing functionality (inpainting through masks)
  * Image-to-image generation from a reference image
  * Multiple image input, batching several reference images into a single generation



## 

​

Example outputs

Text-to-image generation from a single text prompt: ![ComfyUI openai-gpt-image-1 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/text2image.png) Image-to-image generation from a reference image: ![ComfyUI openai-gpt-image-1 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/image2image.png) Multiple image input, combining several reference images into one generation: ![Multiple Image Input Example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/multiple_image_input.png) Inpainting, replacing a masked area of an input image: ![ComfyUI openai-gpt-image-1 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/inpaint.png)

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

Parameter Description

### 

​

Required Parameters

Parameter| Type| Description  
---|---|---  
`prompt`| Text| Text prompt describing the image content you want to generate  
  
### 

​

Widget Parameters

Parameter| Type| Options| Default| Description  
---|---|---|---|---  
`seed`| Integer| 0-2147483647| 0| Random seed used to control generation results  
`quality`| Option| low, medium, high| low| Image quality setting, affects cost and generation time  
`background`| Option| opaque, transparent| opaque| Whether the returned image has a background  
`size`| Option| auto, 1024x1024, 1024x1536, 1536x1024| auto| Size of the generated image  
`n`| Integer| 1-8| 1| Number of images to generate  
  
### 

​

Optional Parameters

Parameter| Type| Options| Default| Description  
---|---|---|---|---  
`image`| Image| Any image input| None| Optional reference image for image editing  
`mask`| Mask| Mask input| None| Optional mask for inpainting (white areas will be replaced)  
  
## 

​

Usage Examples

### 

​

Text-to-Image Example

The image below contains a simple text-to-image workflow. Please download the image and drag it into ComfyUI to load the corresponding workflow. ![ComfyUI openai-gpt-image-1 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/text2image.png) The corresponding workflow is very simple: ![ComfyUI openai-gpt-image-1 workflow example](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e7308997e027153d914a61418a9c0058) You only need to load the `OpenAI GPT-Image-1` node, input the description of the image you want to generate in the `prompt` node, connect a `Save Image` node, and then run the workflow.

### 

​

Image-to-Image Example

The image below contains a simple image-to-image workflow. Please download the image and drag it into ComfyUI to load the corresponding workflow. ![ComfyUI openai-gpt-image-1 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/image2image.png) We will use the image below as input: ![ComfyUI openai-gpt-image-1 workflow input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/input.webp) In this workflow, we use the `OpenAI GPT-Image-1` node to generate images and the `Load Image` node to load the input image, then connect it to the `image` input of the `OpenAI GPT-Image-1` node. ![ComfyUI openai-gpt-image-1 workflow example](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=05cab30de9ab5bc2e0865c0a367f82fc)

### 

​

Multiple Image Input Example

Please download the image below and drag it into ComfyUI to load the corresponding workflow. ![Multiple Image Input Example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/multiple_image_input.png) Use the hat image below as an additional input image. ![Hat](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/hat.webp) The corresponding workflow is shown in the image below: ![Multiple Image Input Example](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=125236ed762b17ae1e711fa702663f74) The `Batch Images` node is used to load multiple images into the `OpenAI GPT-Image-1` node.

### 

​

Inpainting Workflow

GPT-Image-1 also supports image editing functionality, allowing you to specify areas to replace using a mask. Below is a simple inpainting workflow example: Download the image below and drag it into ComfyUI to load the corresponding workflow. We will continue to use the input image from the image-to-image workflow section. ![ComfyUI openai-gpt-image-1 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/inpaint.png) The corresponding workflow is shown in the image ![ComfyUI openai-gpt-image-1 workflow example](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=12d74944bf8905025606740b820918a8) Compared to the image-to-image workflow, we use the MaskEditor in the `Load Image` node through the right-click menu to draw a mask, then connect it to the `mask` input of the `OpenAI GPT-Image-1` node to complete the workflow. **Notes**

  * The mask and image must be the same size
  * When inputting large images, the node will automatically resize the image to an appropriate size



## 

​

FAQs

Why can't I find the Partner Nodes?

Please update your ComfyUI to the latest version (the latest commit or the latest [desktop version](https://www.comfy.org/download)). We may add more API support in the future, and the corresponding nodes will be updated, so please keep your ComfyUI up to date.

Please note that you need to distinguish between the nightly version and the release version. In some cases, the latest `release` version may not be updated in time compared to the `nightly` version. Since we are still iterating quickly, please ensure you are using the latest version when you cannot find the corresponding node.

Why can't I use / log in to the Partner Nodes?

API access requires that your current request is based on a secure network environment. The current requirements for API access are as follows:

  * The local network only allows access from `127.0.0.1` or `localhost`, which may mean that you cannot use the Partner Nodes in a ComfyUI service started with the `--listen` parameter in a LAN environment.
  * Able to access our API service normally (a proxy service may be required in some regions).
  * Your account does not have enough [credits](https://docs.comfy.org/interface/credits).



Why can't I use Partner Node even after logging in, or why does it keep asking me to log in while using?

  * Currently, only `127.0.0.1` or `localhost` access is supported.
  * Ensure your account has enough credits.



Can Partner Nodes be used for free?

Partner Nodes require credits for API calls to closed-source models, so they do not support free usage.

How to purchase credits?

Please refer to the following documentation:

  1. [Comfy Account](https://docs.comfy.org/interface/user): Find the `User` section in the settings menu to log in.
  2. [Credits](https://docs.comfy.org/interface/credits): After logging in, the settings interface will show the credits menu. You can purchase credits in `Settings` → `Credits`. We use a prepaid system, so there will be no unexpected charges.
  3. Complete the payment through Stripe.
  4. Check if the credits have been updated. If not, try restarting or refreshing the page.



Are unused credits refundable?

Currently, we do not support refunds for credits. If you believe there is an error resulting in unused balance due to technical issues, please [contact support](mailto:support@comfy.org).

Can credits go negative?

Credits are not intended to be used as a negative balance or credit line. However, due to race conditions where partner nodes don’t always report costs before execution, a single execution may consume more credits than your remaining balance and temporarily result in a negative balance after completion. When your balance is negative, you will not be able to run Partner Nodes until you top up and restore a positive balance. Please ensure you have enough credits before making API calls.

Where can I check usage and expenses?

Please visit the [Credits](https://docs.comfy.org/interface/credits) menu after logging in to check the corresponding credits.

Is it possible to use my own API Key?

Currently, the Partner Nodes are still in the testing phase and do not support this feature yet, but we have considered adding it.

Do credits expire?

Yes, the expiration depends on the type of credits:

  * **Monthly credits** : Expire at the end of your billing period
  * **Top-up credits** : Expire 1 year from the date of purchase



Can credits be transferred or shared?

No, your credits cannot be transferred to other users and are limited to the currently logged-in account, but we do not restrict the number of devices that can log in.

Can I use the same account on different devices?

We do not limit the number of devices that can log in; you can use your account anywhere you want.

How can I request for my account or information to be deleted??

Email a request to [support@comfy.org](mailto:support@comfy.org) and we will delete your information

Is there content moderation for Partner Nodes?

Partner Nodes send your inputs (prompts, images, and other content) to third-party providers for processing. These providers enforce their own content moderation policies. Please do not submit NSFW or other prohibited content to API nodes.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/openai/gpt-image-1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/openai/gpt-image-1)

[OpenAI GPT-Image-2 in ComfyUI: Reasoning Image GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2)[Qwen Image 3.0 Pro - Advanced AI Image GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/qwen/qwen-image-3-0-pro)

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
