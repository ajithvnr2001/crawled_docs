---
url: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-text-to-image/
title: Luma Text to Image in ComfyUI: Style and Character References - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:33.866470+00:00
---

# Luma Text to Image in ComfyUI: Style and Character References - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-text-to-image/

## On this page

  * What Luma Text to Image is good at
  * Example outputs
  * Luma Text to Image Partner Nodes Workflow
    * 1\. Download Workflow Files
    * 2\. Follow Steps to Run the Workflow
    * 3\. Additional Notes



Luma

# Luma Text to Image in ComfyUI: Style and Character References

Copy pageCopy page

Generate images from text with the Luma Text to Image node in ComfyUI: style images, style weight control, and up to four reference or character images.

Copy pageCopy page

The Luma Text to Image node allows you to generate high-quality images from text prompts using Luma AI’s advanced technology, capable of creating photorealistic content and artistic style images.

## 

​

What Luma Text to Image is good at

  * **High-quality text-to-image generation** : Creates photorealistic content and artistic style images from text prompts
  * **Style references** : A `style_image` input guides the look of the result, with `style_image_weight` controlling the style reference image’s influence
  * **Image and character references** : The `image_luma_ref` input supports reference-guided generation, with up to 4 reference images and character references usable simultaneously



## 

​

Example outputs

Style-guided generation at different `style_image_weight` values, showing the style reference image’s influence: ![Style Image Weight Comparison](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7f47d2d3a6acdde87df046460afa393f)

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

Luma Text to Image Partner Nodes Workflow

When the `Luma Text to Image` node is used without any image inputs, it functions as a text-to-image workflow. In this guide, we’ve created examples using `style_image` and `image_luma_ref` to showcase Luma AI’s excellent image processing capabilities.

### 

​

1\. Download Workflow Files

The workflow information is included in the metadata of the image below. Download and drag it into ComfyUI to load the workflow. ![Luma Text to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/luma_t2i.png) Please download these images for input: ![Input Image - Reference](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/input_ref.png) ![Input Image - Style](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/input_style.png)

### 

​

2\. Follow Steps to Run the Workflow

![Luma Text to Image Workflow Steps](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3122c711034e8270d086ae8c139cb64) Follow the numbered steps in the image to complete the basic workflow:

  1. Upload the reference image in the `Load image` node
  2. Upload the style reference image in the `Load image (renamed to styleref)` node
  3. (Optional) Modify the prompts in the `Luma Text to Image` node
  4. (Optional) Adjust the `style_image_weight` to control the style reference image’s influence
  5. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to generate the image
  6. After the API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory

![Style Image Weight Comparison](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7f47d2d3a6acdde87df046460afa393f)

### 

​

3\. Additional Notes

  * The node allows up to 4 reference images and character references simultaneously.
  * To enable multiple image inputs, right-click on the purple “Bypassed” nodes and set their `mode` to `always`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/luma/luma-text-to-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/luma/luma-text-to-image)

[Luma Uni-1 GuidePrevious](https://docs.comfy.org/tutorials/partner-nodes/luma/luma-uni-1)[Luma Image to Image in ComfyUI: Prompt-Driven Image EditingNext](https://docs.comfy.org/tutorials/partner-nodes/luma/luma-image-to-image)

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
