---
url: https://docs.comfy.org/tutorials/basic/outpaint/
title: Outpainting in ComfyUI: Extend an Image Beyond Its Borders - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:05.475827+00:00
---

# Outpainting in ComfyUI: Extend an Image Beyond Its Borders - ComfyUI

> Source: https://docs.comfy.org/tutorials/basic/outpaint/

## On this page

  * About Outpainting
  * ComfyUI Outpainting Workflow Example Explanation
    * Preparation
    * 1\. Model Installation
    * 2\. Input Image
    * 3\. Outpainting Workflow
    * Outpainting Workflow Usage Explanation
    * Pad Image for outpainting Node
    * Input Parameters
    * Output Parameters
    * Node Output Content



Basic Examples

# Outpainting in ComfyUI: Extend an Image Beyond Its Borders

Copy pageCopy page

Use the Pad Image for Outpainting node with an inpainting model to grow the canvas, keeping the new edges consistent with the original image.

Copy pageCopy page

This guide will introduce you to the concept of outpainting in AI image generation and how to create an outpainting workflow in ComfyUI. We will cover:

  * Using outpainting workflow to extend an image
  * Understanding and using outpainting-related nodes in ComfyUI
  * Mastering the basic outpainting process



## 

​

About Outpainting

In AI image generation, we often encounter situations where an existing image has good composition but the canvas area is too small, requiring us to extend the canvas to get a larger scene. This is where outpainting comes in. Basically, it requires similar content to [Inpainting](https://docs.comfy.org/tutorials/basic/inpaint), but we use different nodes to **build the mask**. Outpainting applications include:

  * **Scene Extension:** Expand the scene range of the original image to show a more complete environment
  * **Composition Adjustment:** Optimize the overall composition by extending the canvas
  * **Content Addition:** Add more related scene elements to the original image



## 

​

ComfyUI Outpainting Workflow Example Explanation

### 

​

Preparation

#### 

​

1\. Model Installation

Download the following model file and save it to `ComfyUI/models/checkpoints` directory:

  * [512-inpainting-ema.safetensors](https://huggingface.co/Comfy-Org/stable_diffusion_2.1_repackaged/blob/main/512-inpainting-ema.safetensors)



#### 

​

2\. Input Image

Prepare an image you want to extend. In this example, we will use the following image: ![ComfyUI Outpainting Input Image](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/input.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=70f072d92be155e740f8763e0265240f)

#### 

​

3\. Outpainting Workflow

Download the image below and **drag it into ComfyUI** to load the workflow: ![ComfyUI Outpainting Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/outpaint.png)

Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.

### 

​

Outpainting Workflow Usage Explanation

![ComfyUI Outpainting Workflow Diagram](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/outpainting_workflow.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b56842f634fedc85c66bccd0ead52bb6) The key steps of the outpainting workflow are as follows:

  1. Load the locally installed model file in the `Load Checkpoint` node
  2. Click the `Upload` button in the `Load Image` node to upload your image
  3. Click the `Queue` button or use the shortcut `Ctrl + Enter` to execute the image generation

In this workflow, we mainly use the `Pad Image for outpainting` node to control the direction and range of image extension. This is actually an [Inpaint](https://docs.comfy.org/tutorials/basic/inpaint) workflow, but we use different nodes to build the mask.

### 

​

Pad Image for outpainting Node

![Pad Image for outpainting Node](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/pad_image_for_outpainting.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9a9eaf8b01a18692b50a684cbff5d8e1) This node accepts an input image and outputs an extended image with a corresponding mask, where the mask is built based on the node parameters.

#### 

​

Input Parameters

Parameter Name| Function  
---|---  
`image`| Input image  
`left`| Left padding amount  
`top`| Top padding amount  
`right`| Right padding amount  
`bottom`| Bottom padding amount  
`feathering`| Controls the smoothness of the transition between the original image and the added padding, higher values create smoother transitions  
  
#### 

​

Output Parameters

Parameter Name| Function  
---|---  
`image`| Output `image` represents the padded image  
`mask`| Output `mask` indicates the original image area and the added padding area  
  
#### 

​

Node Output Content

After processing by the `Pad Image for outpainting` node, the output image and mask preview are as follows: ![Pad Image for outpainting Node Results](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=cc8fd3e8159dca0e8abf9def1bfe6d39) You can see the corresponding output results:

  * The `Image` output is the extended image
  * The `Mask` output is the mask marking the extension areas



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/basic/outpaint.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/basic/outpaint)

[ComfyUI Inpainting WorkflowPrevious](https://docs.comfy.org/tutorials/basic/inpaint)[ComfyUI Image Upscale WorkflowNext](https://docs.comfy.org/tutorials/basic/upscale)

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
