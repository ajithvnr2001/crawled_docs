---
url: https://docs.comfy.org/tutorials/video/ltx/ltx-2/
title: LTX-2 in ComfyUI: Synchronized Audio-Video Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:07.347506+00:00
---

# LTX-2 in ComfyUI: Synchronized Audio-Video Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/ltx/ltx-2/

## On this page

  * Key features
  * Model checkpoints
  * Getting started
  * Workflows
    * Text-to-video
    * Image-to-video
    * Control-to-video
  * Prompting tips
  * Resources



LTX

# LTX-2 in ComfyUI: Synchronized Audio-Video Workflows

Copy pageCopy page

Generate synchronized video and audio in ComfyUI with LTX-2: text-to-video, image-to-video, video-to-video control, keyframe interpolation, and 2x upscalers.

Copy pageCopy page

[LTX-2](https://huggingface.co/Lightricks/LTX-2) is a 19B parameter DiT-based audio-video foundation model by Lightricks. It generates synchronized video and audio in a single pass, creating cohesive experiences where motion, dialogue, background noise, and music are produced together.

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

Key features

  * **Synchronized audio-video generation** : Generates motion, dialogue, SFX, and music together in one pass
  * **Multiple generation modes** : Text-to-video, image-to-video, and video-to-video
  * **Control options** : Canny, Depth, and Pose video-to-video control via IC-LoRAs
  * **Keyframe-driven generation** : Interpolate between keyframe images
  * **Native upscaling** : Spatial (2x) and temporal (2x) upscalers for higher resolution and FPS
  * **Prompt enhancement** : Automatic prompt enhancement support



## 

​

Model checkpoints

Name| Description  
---|---  
ltx-2-19b-dev| Full model in bf16, flexible and trainable  
ltx-2-19b-dev-fp8| Full model in fp8 quantization  
ltx-2-19b-distilled| Distilled version, 8 steps, CFG=1  
ltx-2-spatial-upscaler-x2-1.0| 2x spatial upscaler for higher resolution  
ltx-2-temporal-upscaler-x2-1.0| 2x temporal upscaler for higher FPS  
  
## 

​

Getting started

LTX-2 is natively supported in ComfyUI. To get started:

  1. Update ComfyUI to the latest version
  2. Go to **Template Library** > **Video** > choose any LTX-2 workflow
  3. Follow the pop-up to download models and run the workflow



## 

​

Workflows

### 

​

Text-to-video

Generate videos from text prompts. ![ComfyUI Workflow - LTX-2 T2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_t2v-1.webp)

## Text-to-Video

Download workflow

## Run on Comfy Cloud

Open in cloud

**Distilled version** (faster, 8 steps): ![ComfyUI Workflow - LTX-2 T2V Distilled](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_t2v_distilled-1.webp)

## Text-to-Video Distilled

Download workflow

## Run on Comfy Cloud

Open in cloud

### 

​

Image-to-video

Generate videos from an input image. ![ComfyUI Workflow - LTX-2 I2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_i2v-1.webp)

## Image-to-Video

Download workflow

## Run on Comfy Cloud

Open in cloud

**Input materials**

## Input Image

Download the default input image, or use your own image.

**Distilled version** (faster, 8 steps): ![ComfyUI Workflow - LTX-2 I2V Distilled](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_i2v_distilled-1.webp)

## Image-to-Video Distilled

Download workflow

## Run on Comfy Cloud

Open in cloud

**Input materials**

## Input Image

Download the default input image, or use your own image.

### 

​

Control-to-video

Generate videos with structural control using IC-LoRAs. **Depth control:** ![ComfyUI Workflow - LTX-2 Depth to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_depth_to_video-1.webp)

## Depth-to-Video

Download workflow

## Run on Comfy Cloud

Open in cloud

**Input materials**

## Input Image

Download the default depth input image, or use your own.

## Input Video

Download the default input video, or use your own.

**Canny control:** ![ComfyUI Workflow - LTX-2 Canny to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_canny_to_video-1.webp)

## Canny-to-Video

Download workflow

## Run on Comfy Cloud

Open in cloud

**Input materials**

## Input Image

Download the default canny input image, or use your own.

## Input Video

Download the default input video, or use your own.

**Pose control:** ![ComfyUI Workflow - LTX-2 Pose to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_pose_to_video-1.webp)

## Pose-to-Video

Download workflow

## Run on Comfy Cloud

Open in cloud

**Input materials**

## Input Image

Download the default pose input image, or use your own.

## Input Video

Download the default input video, or use your own.

## 

​

Prompting tips

When writing prompts for LTX-2, focus on detailed, chronological descriptions of actions and scenes. Include specific movements, appearances, camera angles, and environmental details in a single flowing paragraph. Start directly with the action and keep descriptions literal and precise. Structure your prompts with:

  * Main action in a single sentence
  * Specific details about movements and gestures
  * Character/object appearances
  * Background and environment details
  * Camera angles and movements
  * Lighting and colors
  * Any changes or sudden events

Keep prompts within 200 words for best results.

## 

​

Resources

  * [GitHub Repository](https://github.com/Lightricks/LTX-2)
  * [Hugging Face Model](https://huggingface.co/Lightricks/LTX-2)
  * [LTX-2 Prompting Guide](https://ltx.video/blog/how-to-prompt-for-ltx-2)
  * [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/ltx/ltx-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/ltx/ltx-2)

[LTX-2.3: ComfyUI Workflow ExamplesPrevious](https://docs.comfy.org/tutorials/video/ltx/ltx-2-3)[LTX-Video 0.9.5 in ComfyUI: T2V, I2V, Multi-Frame ControlNext](https://docs.comfy.org/tutorials/video/ltxv)

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
