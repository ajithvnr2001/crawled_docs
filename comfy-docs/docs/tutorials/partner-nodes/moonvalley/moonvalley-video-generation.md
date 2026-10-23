---
url: https://docs.comfy.org/tutorials/partner-nodes/moonvalley/moonvalley-video-generation/
title: Moonvalley Marey in ComfyUI: Video Generation (Deprecated) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:35.000407+00:00
---

# Moonvalley Marey in ComfyUI: Video Generation (Deprecated) - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/moonvalley/moonvalley-video-generation/

## On this page

  * What Moonvalley is good at
  * Moonvalley Text-to-Video Workflow
    * 1\. Download the Workflow File
    * 2\. Follow the Steps to Run the Workflow
  * Moonvalley Image-to-Video Workflow
    * 1\. Download the Workflow File
    * 2\. Follow the Steps to Run the Workflow
  * Moonvalley Video-to-Video Workflow
    * 1\. Download the Workflow File
    * 2\. Follow the Steps to Run the Workflow



Moonvalley

# Moonvalley Marey in ComfyUI: Video Generation (Deprecated)

Copy pageCopy page

Deprecated Moonvalley Marey partner nodes in ComfyUI for text-to-video, image-to-video, and video-to-video generation. The API is no longer available.

Copy pageCopy page

**Service unavailable** : The Moonvalley API service is no longer available. These nodes have been deprecated and may not function as expected.

Moonvalley Marey Realism v1.5 is an AI video generation model designed for cinematic-level creation. The model is **trained entirely with commercially licensed content** , ensuring **copyright compliance and commercial safety**.

## 

​

What Moonvalley is good at

  * Exceptional prompt comprehension: Accurately interprets complex prompt instructions.
  * Native 1080p HD quality: The training dataset is based on **1080P** videos, resulting in fine and detailed output.
  * Realistic physics and dynamic performance: Precisely simulates physical motion models and natural dynamics, delivering professional-grade realism.
  * Complex scene layering and advanced lighting effects: Supports foreground, midground, and background layering in complex scenes, with intelligent spatial relationship understanding.
  * Production-level control features such as motion and pose transfer: Automatically generates realistic lighting for composite scenes.

Currently, Moonvalley-related Partner nodes are natively supported in ComfyUI. You can use the corresponding text-to-video, image-to-video, and video-to-video capabilities directly in ComfyUI.

**Service unavailable** : The Moonvalley API service is no longer available. These nodes have been deprecated and may not function as expected.

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

Moonvalley Text-to-Video Workflow

### 

​

1\. Download the Workflow File

[Download the workflow file in JSON format](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_text_to_video.json)

### 

​

2\. Follow the Steps to Run the Workflow

![Text-to-Video Workflow](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=75dc005efbab705ab95cea22b36f7a24)

  1. Enter the positive prompt (content you want to appear in the video)
  2. Enter the negative prompt (content you do not want to appear in the video)
  3. Modify the video output resolution
  4. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to start video generation
  5. After the API returns the result, you can view the generated video in the `Save Video` node. The video will also be saved in the `ComfyUI/output/` directory



## 

​

Moonvalley Image-to-Video Workflow

### 

​

1\. Download the Workflow File

[Download the workflow file in JSON format](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video.json) Download the image below as the input image ![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video_input.webp)

### 

​

2\. Follow the Steps to Run the Workflow

![Image-to-Video Workflow](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9467e0f19d709f9b77cc4778a97f04a8)

  1. Load the input image in the `Load Image` node
  2. Enter the positive prompt (content you want to appear in the video)
  3. Enter the negative prompt (content you do not want to appear in the video)
  4. Modify the video output resolution
  5. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to start video generation
  6. After the API returns the result, you can view the generated video in the `Save Video` node. The video will also be saved in the `ComfyUI/output/` directory



## 

​

Moonvalley Video-to-Video Workflow

The `Moonvalley Marey Video to Video` node allows you to input a reference video for video re-drawing. You can use the reference video’s motion or character poses for video generation.

### 

​

1\. Download the Workflow File

[Download the workflow file in JSON format](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_video_to_video.json) Download the video below as the input video:

### 

​

2\. Follow the Steps to Run the Workflow

![Video-to-Video Workflow](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ee9e202bdc9a3b39c8dc6ba5b10577b5)

  1. Load the reference video (or your own material) in the `Load Video` node 
     * If the final video duration is 5s, the input video must be longer than 5s
     * If the final video duration is 10s, the input video must be longer than 10s
  2. Enter the positive prompt (content you want to appear in the video)
  3. Enter the negative prompt (content you do not want to appear in the video)
  4. Set the `control_type` parameter to choose the reference type for video re-drawing 
     * `Motion Transfer`: Generate based on the motion in the reference video
     * `Pose Transfer`: Generate based on the character poses in the reference video
  5. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to start video generation
  6. After the API returns the result, you can view the generated video in the `Save Video` node. The video will also be saved in the `ComfyUI/output/` directory



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/moonvalley/moonvalley-video-generation.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/moonvalley/moonvalley-video-generation)

[MiniMax H3 API Video Generation in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/minimax/minimax-h3)[Pruna P-Video-2: Text and Image to Video in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/pruna/p-video-2)

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
