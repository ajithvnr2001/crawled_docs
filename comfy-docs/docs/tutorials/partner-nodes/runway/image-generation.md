---
url: https://docs.comfy.org/tutorials/partner-nodes/runway/image-generation/
title: Runway Image Generation in ComfyUI: Text-to-Image and Reference Images - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:38.045958+00:00
---

# Runway Image Generation in ComfyUI: Text-to-Image and Reference Images - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/runway/image-generation/

## On this page

  * What Runway Image Generation is good at
  * Runway Image Text-to-Image Workflow
    * 1\. Workflow File Download
    * 2\. Complete the Workflow Execution Step by Step
  * Runway Image Reference-to-Image Workflow
    * 1\. Workflow and Input Image Download
    * 2\. Complete the Workflow Execution Step by Step



Runway

# Runway Image Generation in ComfyUI: Text-to-Image and Reference Images

Copy pageCopy page

Run Runway image partner nodes in ComfyUI to generate images from a text prompt or a reference image, with adjustable output aspect ratios.

Copy pageCopy page

Runway is a company focused on generative AI, providing powerful image generation capabilities. Its models support features such as style transfer, image extension, and detail control. Currently, ComfyUI has integrated the Runway API, allowing you to directly use the related nodes in ComfyUI for image generation.

## 

​

What Runway Image Generation is good at

  * **Text-to-image generation** : Generates images from a text prompt with the `Runway Text to Image` node, with adjustable output aspect ratios
  * **Reference-to-image generation** : Generates images guided by an input reference image plus a text prompt
  * **Style transfer, image extension, and detail control** : Runway’s models support these features for image generation



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

Runway Image Text-to-Image Workflow

### 

​

1\. Workflow File Download

The image below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow. ![ComfyUI Runway Image Text to Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/text_to_image.png)

### 

​

2\. Complete the Workflow Execution Step by Step

![ComfyUI Runway Image Text to Image Step Guide](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66f4bf5de975a5f0302d930e352605ff) You can refer to the numbers in the image to complete the basic text-to-image workflow execution:

  1. In the `Runway Text to Image` node, input your prompt in the `prompt` field
  2. (Optional) Adjust the `ratio` setting to set different output aspect ratios
  3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute image generation.
  4. After waiting for the API to return results, you can view the generated image in the `Save Image` node (right-click to save). The corresponding image will also be saved to the `ComfyUI/output/` directory.



## 

​

Runway Image Reference-to-Image Workflow

### 

​

1\. Workflow and Input Image Download

The image below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow. ![ComfyUI Runway Image Reference to Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/reference_to_image/runway_reference_to_image.png) Download the image below for input ![ComfyUI Runway Image Reference to Image Input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/reference_to_image/input.png)

### 

​

2\. Complete the Workflow Execution Step by Step

![ComfyUI Runway Image Reference to Image Step Guide](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f0ce702cc2a6a03d887072416d78c241) You can refer to the numbers in the image to complete the basic reference-to-image workflow execution:

  1. In the `Load Image` node, load the provided input image
  2. In the `Runway Text to Image` node, input your prompt in the `prompt` field and adjust dimensions
  3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute image generation.
  4. After waiting for the API to return results, you can view the generated image in the `Save Image` node (right-click to save). The corresponding image will also be saved to the `ComfyUI/output/` directory.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/runway/image-generation.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/runway/image-generation)

[Reve Image Create, Edit, and Remix in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/reve/reve-image)[Tencent Hunyuan Image 3.5 Preview in ComfyUI: Text to Image and Edit WorkflowsNext](https://docs.comfy.org/tutorials/partner-nodes/tencent/hy-image-3-5)

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
