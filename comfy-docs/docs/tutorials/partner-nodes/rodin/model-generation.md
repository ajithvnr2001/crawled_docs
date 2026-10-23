---
url: https://docs.comfy.org/tutorials/partner-nodes/rodin/model-generation/
title: Hyper3D Rodin in ComfyUI: Single and Multi-View 3D Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:37.614921+00:00
---

# Hyper3D Rodin in ComfyUI: Single and Multi-View 3D Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/rodin/model-generation/

## On this page

  * What Rodin Model Generation is good at
  * Single-view Model Generation Workflow
    * 2\. Complete the Workflow Execution Step by Step
  * Multi-view Model Generation Workflow
    * 1\. Workflow File Download
    * 2\. Complete the Workflow Execution Step by Step
  * Other Related Nodes



Rodin

# Hyper3D Rodin in ComfyUI: Single and Multi-View 3D Generation

Copy pageCopy page

Generate production-ready 3D models in ComfyUI with the Hyper3D Rodin partner node from a single image or up to five multi-view images.

Copy pageCopy page

Hyper3D Rodin (hyper3d.ai) is a platform focused on rapidly generating high-quality, production-ready 3D models and materials through artificial intelligence. ComfyUI has now natively integrated the corresponding Rodin model generation API, allowing you to conveniently use the related nodes in ComfyUI for model generation.

## 

​

What Rodin Model Generation is good at

  * **Single-view model generation** : Generates a 3D model from a single image input
  * **Multi-view model generation** : Generates a 3D model from up to 5 image inputs, such as front, back, and left views
  * **Different levels of detail** : Supports model generation with adjustable detail, including different polygon counts for smoother, more detailed models
  * **Direct export** : Generated models are saved to the `ComfyUI/output/Rodin` directory and can be exported from the `Preview 3D` node



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

Single-view Model Generation Workflow

Generate a 3D model from a single image input with Rodin. ![Rodin Single-view Model Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_image_to_model-1.webp)

## Download Workflow File

Single-view Model Generation (Json Format)

## Run on Comfy Cloud

Open in Comfy Cloud

![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/doll.jpg)

### 

​

2\. Complete the Workflow Execution Step by Step

![ComfyUI Rodin Image to Model Step Guide](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ed79f1fb8546ed41a3d157cece818ee9) You can refer to the numbers in the image to complete the basic text-to-image workflow execution:

  1. In the `Load Image` node, load the provided input image
  2. (Optional) In `Rodin 3D Generate - Regular Generate` adjust the corresponding parameters 
     * polygon_count: You can set different polygon counts, the higher the value, the smoother and more detailed the model
  3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/Rodin` directory
  4. In the `Preview 3D` node, click to expand the menu
  5. Select `Export` to directly export the corresponding model



## 

​

Multi-view Model Generation Workflow

The corresponding `Rodin 3D Generate - Regular Generate` allows up to 5 image inputs

### 

​

1\. Workflow File Download

You can modify the single-view workflow to a multi-view workflow, or directly download the workflow file below ![Rodin Multi-view Model Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_multiview_to_model-1.webp)

## Download Workflow File

Multi-view Model Generation (Json Format)

## Run on Comfy Cloud

Open in Comfy Cloud

![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/front.jpg) ![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/back.jpg) ![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/left.jpg)

### 

​

2\. Complete the Workflow Execution Step by Step

![ComfyUI Rodin Image to Model Step Guide](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6241527775e83bd480811631ef4d88ed) You can refer to the numbers in the image to complete the basic text-to-image workflow execution:

  1. In the `Load Image` node, load the provided input images
  2. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/Rodin` directory
  3. In the `Preview 3D` node, click to expand the menu
  4. Select `Export` to directly export the corresponding model



## 

​

Other Related Nodes

Currently, Rodin provides different types of model generation nodes in ComfyUI, since the corresponding input conditions are the same as the workflow introduced in this article, you can enable them as needed. In addition, we have provided corresponding nodes in the corresponding templates, you can also modify the corresponding node mode as needed to enable them ![Rodin Other Related Nodes](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7caf60a6b994156e71476564c856fc15)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/rodin/model-generation.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/rodin/model-generation)

[Meshy 6 in ComfyUI: Text, Image, and Multi-View to 3DPrevious](https://docs.comfy.org/tutorials/partner-nodes/meshy/meshy-6)[Tripo P2: Quad Topology 3D Model Generation in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p2)

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
