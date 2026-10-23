---
url: https://docs.comfy.org/tutorials/partner-nodes/recraft/recraft-text-to-image/
title: Recraft Text to Image in ComfyUI: Images with Preset Styles - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:07.044330+00:00
---

# Recraft Text to Image in ComfyUI: Images with Preset Styles - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/recraft/recraft-text-to-image/

## On this page

  * What Recraft Text to Image is good at
  * Recraft Text to Image Partner Nodes Workflow
    * 1\. Download the Workflow File
    * 2\. Follow the Steps to Run the Workflow
    * 3\. Additional Notes



Recraft

# Recraft Text to Image in ComfyUI: Images with Preset Styles

Copy pageCopy page

Generate images from text in ComfyUI with the Recraft Text to Image partner node, using preset styles, RGB color control, and optional SVG vectorization.

Copy pageCopy page

The Recraft Text to Image node allows you to create high-quality images in various styles using Recraft AI’s image generation technology based on text descriptions.

## 

​

What Recraft Text to Image is good at

  * **High-quality generation** : Creates images from text descriptions using Recraft AI’s image generation technology
  * **Style control** : Preset styles such as digital art, realistic photos, and logo designs via the `Recraft Style` node
  * **Color control** : Set a desired color with the `Recraft Color RGB` node
  * **Adjustable output size** : Change the `size` parameter to control output dimensions
  * **SVG conversion** : An optional `Recraft Vectorize Image` node converts the generated image to SVG format



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

Recraft Text to Image Partner Nodes Workflow

### 

​

1\. Download the Workflow File

The workflow information is included in the metadata of the image below. Download and drag it into ComfyUI to load the workflow. ![Recraft Text to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/recraft/t2i/recraft_t2i.png)

### 

​

2\. Follow the Steps to Run the Workflow

![Recraft Text to Image Workflow Steps](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=26e3744a4e7c44a1d72840e8ffef5c3c) Follow these numbered steps to run the basic workflow:

  1. (Optional) Change the `Recraft Color RGB` in the `Color` node to your desired color
  2. (Optional) Modify the `Recraft Style` node to control the visual style, such as digital art, realistic photo, or logo design. This group includes other style nodes you can enable as needed
  3. (Optional) Edit the `prompt` parameter in the `Recraft Text to Image` node. You can also change the `size` parameter
  4. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to generate the image
  5. After the API returns the result, you can view the generated image in the `Save Image` node. The image will also be saved to the `ComfyUI/output/` directory



> (Optional) We’ve included a **Convert to SVG** group in the workflow. Since the `Recraft Vectorize Image` node in this group consumes additional credits, enable it only when you need to convert the generated image to SVG format

### 

​

3\. Additional Notes

  * **Recraft Style** : Offers various preset styles like realistic photos, digital art, and logo designs
  * **Seed Parameter** : Only used to determine if the node should run again, the actual generation result is not affected by the seed value



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/recraft/recraft-text-to-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/recraft/recraft-text-to-image)

[Recraft V4 & V4.1 Image & Vector Generation in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/recraft/recraft-v4)[Reve Image in ComfyUI: Retired Partner Node ReferenceNext](https://docs.comfy.org/tutorials/partner-nodes/reve/reve-image)

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
