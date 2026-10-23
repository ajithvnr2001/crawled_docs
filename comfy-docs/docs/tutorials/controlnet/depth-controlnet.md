---
url: https://docs.comfy.org/tutorials/controlnet/depth-controlnet/
title: Depth ControlNet in ComfyUI: Control Scene Structure - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:05.142131+00:00
---

# Depth ControlNet in ComfyUI: Control Scene Structure - ComfyUI

> Source: https://docs.comfy.org/tutorials/controlnet/depth-controlnet/

## On this page

  * Introduction to Depth Maps and Depth ControlNet
    * Application Scenarios for Depth Maps with ControlNet
  * ComfyUI ControlNet Workflow Example Explanation
    * 1\. ControlNet Workflow Assets
    * 2\. Model Installation
    * 3\. Step-by-Step Workflow Execution
  * Combining Depth Control with Other Techniques



ControlNet

# Depth ControlNet in ComfyUI: Control Scene Structure

Copy pageCopy page

Read a depth map, wire it into ControlNet, and keep architecture, portraits, and product shots in the spatial layout you specify.

Copy pageCopy page

## 

​

Introduction to Depth Maps and Depth ControlNet

A depth map is a special type of image that uses grayscale values to represent the distance between objects in a scene and the observer or camera. In a depth map, the grayscale value is inversely proportional to distance: brighter areas (closer to white) indicate objects that are closer, while darker areas (closer to black) indicate objects that are farther away. ![Depth Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth_input.png) Depth ControlNet is a ControlNet model specifically trained to understand and utilize depth map information. It helps AI correctly interpret spatial relationships, ensuring that generated images conform to the spatial structure specified by the depth map, thereby enabling precise control over three-dimensional spatial layouts.

### 

​

Application Scenarios for Depth Maps with ControlNet

Depth maps have numerous applications in various scenarios:

  1. **Portrait Scenes** : Control the spatial relationship between subjects and backgrounds, avoiding distortion in critical areas such as faces
  2. **Landscape Scenes** : Control the hierarchical relationships between foreground, middle ground, and background
  3. **Architectural Scenes** : Control the spatial structure and perspective relationships of buildings
  4. **Product Showcase** : Control the separation and spatial positioning of products against their backgrounds

In this example, we will use a depth map to generate an architectural visualization scene.

## 

​

ComfyUI ControlNet Workflow Example Explanation

### 

​

1\. ControlNet Workflow Assets

Please download the workflow image below and drag it into ComfyUI to load the workflow: ![Depth Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth_controlnet.png)

Images with workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`. This image already includes download links for the corresponding models, and dragging it into ComfyUI will automatically prompt for downloads.

Please download the image below, which we will use as input: ![Depth Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth_input.png)

### 

​

2\. Model Installation

If your network cannot successfully complete the automatic download of the corresponding models, please try manually downloading the models below and placing them in the specified directories:

  * [architecturerealmix_v11.safetensors](https://civitai.com/api/download/models/431755?type=Model&format=SafeTensor&size=full&fp=fp16)
  * [control_v11f1p_sd15_depth_fp16.safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11f1p_sd15_depth_fp16.safetensors?download=true)


    
    
    ComfyUI/
    ├── models/
    │   ├── checkpoints/
    │   │   └── architecturerealmix_v11.safetensors
    │   └── controlnet/
    │       └── control_v11f1p_sd15_depth_fp16.safetensors
    

### 

​

3\. Step-by-Step Workflow Execution

![ComfyUI Workflow - Depth ControlNet Flow Diagram](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_depth.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7bcb7a518e96e88c6ccb73c1a7eb7087)

  1. Ensure that `Load Checkpoint` can load **architecturerealmix_v11.safetensors**
  2. Ensure that `Load ControlNet` can load **control_v11f1p_sd15_depth_fp16.safetensors**
  3. Click `Upload` in the `Load Image` node to upload the depth image provided earlier
  4. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation



## 

​

Combining Depth Control with Other Techniques

Based on different creative needs, you can combine Depth ControlNet with other types of ControlNet to achieve better results:

  1. **Depth + Lineart** : Maintain spatial relationships while reinforcing outlines, suitable for architecture, products, and character design
  2. **Depth + Pose** : Control character posture while maintaining correct spatial relationships, suitable for character scenes

For more information on using multiple ControlNet models together, please refer to the [Mixing ControlNet](https://docs.comfy.org/tutorials/controlnet/mixing-controlnets) example.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/controlnet/depth-controlnet.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/controlnet/depth-controlnet)

[Pose ControlNet in ComfyUI: OpenPose and Two-Pass WorkflowsPrevious](https://docs.comfy.org/tutorials/controlnet/pose-controlnet-2-pass)[Depth T2I Adapter in ComfyUI: Depth-Map Image ControlNext](https://docs.comfy.org/tutorials/controlnet/depth-t2i-adapter)

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
