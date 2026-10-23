---
url: https://docs.comfy.org/tutorials/partner-nodes/runway/video-generation/
title: Runway Gen4 Turbo in ComfyUI: Image-to-Video Workflow - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:37.952043+00:00
---

# Runway Gen4 Turbo in ComfyUI: Image-to-Video Workflow - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/runway/video-generation/

## On this page

  * What Runway Video Generation is good at
    * Retired workflows and replacements
  * Gen4 turbo Image-to-Video Workflow
    * 1\. Workflow File Download
    * 2\. Complete the Workflow Execution Step by Step



Runway

# Runway Gen4 Turbo in ComfyUI: Image-to-Video Workflow

Copy pageCopy page

Generate video from a still image in ComfyUI with the Runway Gen4 Turbo partner node, with adjustable duration and aspect ratio.

Copy pageCopy page

Runway is a company focused on generative AI, providing powerful video generation capabilities. Currently, ComfyUI has integrated the Runway API, allowing you to directly use the related nodes in ComfyUI for video generation. Currently, ComfyUI natively integrates the following Runway video generation model:

  * Runway Gen4 turbo



**End of life (EOL)** : **Runway Gen3a Turbo** and **Runway First-Last-Frame to Video** reached end of life on **July 30, 2026**. Runway retired Gen-3 Alpha Turbo on that date. The related Partner Nodes (`RunwayImageToVideoNodeGen3a`, `RunwayFirstLastFrameNode`) and workflow templates are deprecated and no longer supported.

## 

​

What Runway Video Generation is good at

  * **Image-to-video generation** : The `Runway Gen4 turbo` node generates a video from an input image and a text prompt describing the video content
  * **Adjustable video length** : Modify the `duration` parameter to set the video length
  * **Adjustable aspect ratio** : Modify the `ratio` parameter to set the video aspect ratio



**End of life (EOL)** : **Runway Gen3a Turbo** and **Runway First-Last-Frame to Video** reached end of life on **July 30, 2026**. Runway retired Gen-3 Alpha Turbo on that date. The related Partner Nodes (`RunwayImageToVideoNodeGen3a`, `RunwayFirstLastFrameNode`) and workflow templates are deprecated and no longer supported.

### 

​

Retired workflows and replacements

Removed template| Suggested replacement  
---|---  
`api_runway_gen3a_turbo_image_to_video`| [`api_runway_gen4_turbo_image_to_video`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_runway_gen4_turbo_image_to_video.json) (Gen4 Turbo)  
`api_runway_first_last_frame`| [Kling 3.0 FLF2V](https://docs.comfy.org/tutorials/partner-nodes/kling/kling-3-0) (`api_kling_v3_flf2v`) or other first-last-frame templates  
  
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

Gen4 turbo Image-to-Video Workflow

### 

​

1\. Workflow File Download

The video below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow. [Download Json Format Workflow File](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/runway_gen4_turo_image_to_video.json) Download the image below as input image ![ComfyUI Runway gen4 turbo image to video Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/godfather.jpg)

### 

​

2\. Complete the Workflow Execution Step by Step

![ComfyUI Runway gen4 turbo image to video Step Guide](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1c2df6f00cd1a0fc221a058621cd1449) You can refer to the numbers in the image to complete the basic image-to-video workflow execution:

  1. In the `Load Image` node, load the provided input image
  2. In the `Runway Gen4 turbo` node, set the `prompt` to describe video content, modify the `duration` parameter to set video length, modify the `ratio` parameter to set video aspect ratio
  3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.
  4. After waiting for the API to return results, you can view the generated video in the `Save Video` node (right-click to save). The corresponding video will also be saved to the `ComfyUI/output/` directory.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/runway/video-generation.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/runway/video-generation)

[Pruna P-Video-2: Text and Image to Video in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/pruna/p-video-2)[Topaz Starlight Precise 2.5 - AI video upscalingNext](https://docs.comfy.org/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5)

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
