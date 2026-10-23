---
url: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-image-to-image/
title: Luma Image to Image in ComfyUI: Prompt-Driven Image Editing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:33.297038+00:00
---

# Luma Image to Image in ComfyUI: Prompt-Driven Image Editing - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-image-to-image/

## On this page

  * What Luma Image to Image is good at
  * Example outputs
  * Luma Image to Image Partner Nodes Workflow
    * 1\. Download Workflow File
    * 2\. Complete the Workflow Steps
    * 3\. Results with Different image_weight Values



Luma

# Luma Image to Image in ComfyUI: Prompt-Driven Image Editing

Copy pageCopy page

Edit existing images with the Luma Image to Image node in ComfyUI: prompt-driven changes to objects and shapes, with image weight control over the input.

Copy pageCopy page

The Luma Image to Image node allows you to modify existing images based on text prompts using Luma AI technology, while preserving certain features and structures from the original image.

## 

​

What Luma Image to Image is good at

  * **Prompt-driven image editing** : Modifies existing images based on text prompts while preserving certain features and structures from the original
  * **Changing objects and shapes** : The node works well for changing objects and shapes, though it may not be ideal for color changes
  * **Adjustable input influence** : The `image_weight` parameter controls how strongly the input image shapes the result, with lower values staying closer to the original



## 

​

Example outputs

Results at different `image_weight` values, showing how strongly the input image influences the generated output: ![Weight Comparison](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d6fc32e5bdbf4f1368f73cfac583643d)

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

Luma Image to Image Partner Nodes Workflow

This feature works well for changing objects and shapes. However, it may not be ideal for color changes. We recommend using lower weight values, around 0.0 to 0.1.

### 

​

1\. Download Workflow File

Download and drag the following image into ComfyUI to load the workflow (workflow information is included in the image metadata): ![Luma Image to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2i/luma_i2i.png) Download this image to use as input: ![Luma Image to Image Workflow Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2i/input.png)

### 

​

2\. Complete the Workflow Steps

![Luma Image to Image Workflow Steps](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0169a042868519a3cd76ef832fdc714a) Follow these numbered steps:

  1. Click **Upload** on the `Load Image` node to upload your input image
  2. (Optional) Modify the workflow prompts
  3. (Optional) Adjust `image_weight` to change input image influence (lower values stay closer to original)
  4. Click `Run` or use shortcut `Ctrl(cmd) + Enter` to generate the image
  5. After API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory



### 

​

3\. Results with Different `image_weight` Values

![Weight Comparison](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d6fc32e5bdbf4f1368f73cfac583643d)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/luma/luma-image-to-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/luma/luma-image-to-image)

[Luma Text to Image in ComfyUI: Style and Character ReferencesPrevious](https://docs.comfy.org/tutorials/partner-nodes/luma/luma-text-to-image)[Meta Muse Image in ComfyUI: Text to Image and Image EditNext](https://docs.comfy.org/tutorials/partner-nodes/meta/muse-image)

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
