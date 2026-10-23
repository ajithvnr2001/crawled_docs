---
url: https://docs.comfy.org/tutorials/utility/pose-detection-sdpose/
title: SDPose: Pose Detection in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:41.210887+00:00
---

# SDPose: Pose Detection in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/pose-detection-sdpose/

## On this page

  * Key strengths
  * SDPose Workflows
    * 1\. Download Workflows
    * SDPose: Image Multi-Person Detection
    * SDPose: Video Multi-Person Detection
    * SDPose-OOD: Image to Pose Map
    * SDPose-OOD: Video to Pose Map
    * 2\. Download Models
    * 3\. Using the Workflows
    * Multi-Person (Image)
    * Multi-Person (Video)
    * OOD Image to Pose
    * OOD Video to Pose Map
  * Additional Notes



Pose & Detection

# SDPose: Pose Detection in ComfyUI

Copy pageCopy page

Learn how to extract pose keypoints and maps from images and videos using SDPose, natively supported in ComfyUI

Copy pageCopy page

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

SDPose is a whole-body pose detection model that extracts human keypoints from images and videos. Combined with the RT-DETRv4 object detector, it supports multi-person detection and out-of-domain (OOD) pose estimation, making it a versatile tool for animation pipelines, pose-driven generation, and motion tracking workflows. SDPose + RT-DETRv4 are natively supported in ComfyUI (PR [#12748](https://github.com/Comfy-Org/ComfyUI/pull/12748)). The model weights are available on Hugging Face. [SDPose Model on Hugging Face](https://huggingface.co/Comfy-Org/SDPose) | [RT-DETRv4 Paper (arXiv)](https://arxiv.org/abs/2510.25257) | [SDPose Paper (arXiv)](https://arxiv.org/abs/2509.24980)

### 

​

Key strengths

  * **Whole-body keypoints** : detects body, hands, face, and feet keypoints in a unified model
  * **Multi-person support** : detects and labels multiple people in a single image or video
  * **Configurable outputs** : choose which body parts to visualize (body, hands, face, feet) and control stick/font size
  * **Bounding box detection** : includes object detection with tunable thresholds and class selection
  * **Image and video support** : dedicated workflows for single images, videos, and OOD pose estimation



> **Limitations:** Detection accuracy depends on image resolution and subject visibility. Extremely occluded or very small subjects may produce fewer keypoints.

## 

​

SDPose Workflows

Four workflows are available depending on your use case:

Workflow| Input| Output| Use Case  
---|---|---|---  
Multi-Person (Image)| Single image| Pose map + BBoxes| Photos with multiple people  
Multi-Person (Video)| Video| Per-frame pose map + BBoxes| Video pose tracking  
OOD Image to Pose| Single image| Pose map| Style transfer / image-to-pose  
OOD Video to Pose Map| Video| Per-frame pose map| Video-to-pose animation  
  
### 

​

1\. Download Workflows

Update your ComfyUI to the latest version, then go to `Workflow` -> `Browse Templates` and find SDPose workflows under the Utility category.

### 

​

SDPose: Image Multi-Person Detection

Upload an image to detect human poses. Supports detection for both single individuals and multiple people within the same scene. ![SDPose image multi-person detection workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sdpose_multi_person-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SDPose: Image Multi-Person Detection” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## group_photo.png

`LoadImage` node 679 · `group_photo.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/group_photo.png)

### 

​

SDPose: Video Multi-Person Detection

Upload a video to detect human poses. Supports detection for both single individuals and multiple people within the same scene. ![SDPose video multi-person detection workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sdpose_multi_person_video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SDPose: Video Multi-Person Detection” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## man_playing_violin.mp4

`LoadVideo` node 694 · `man_playing_violin.mp4`

### 

​

SDPose-OOD: Image to Pose Map

Upload an image to extract pose keypoints and generate a corresponding pose map using the SDPose-OOD model. ![SDPose-OOD image to pose map workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sdpose_ood_image_to_pose-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SDPose-OOD: Image to Pose Map” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## dancer.png

`LoadImage` node 667 · `dancer.png`

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/dancer.png)![SDPose-OOD image to pose map example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/utility_sdpose_ood_image_to_pose.png)

### 

​

SDPose-OOD: Video to Pose Map

Upload a video to extract pose keypoints and generate a pose map. The workflow supports multiple person detection and uses an enhanced SDPose model for accurate whole-body feature extraction. ![SDPose-OOD video to pose map workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sdpose_ood_video_to_pose_map-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SDPose-OOD: Video to Pose Map” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## man_in_the_rain.mp4

`LoadVideo` node 679 · `man_in_the_rain.mp4`

**Example output**

### 

​

2\. Download Models

The SDPose and RT-DETRv4 model checkpoints are hosted on the [Comfy-Org SDPose model repository](https://huggingface.co/Comfy-Org/SDPose). **checkpoints** (SDPose model):

  * [sdpose_wholebody_fp16.safetensors](https://huggingface.co/Comfy-Org/SDPose/blob/main/checkpoints/sdpose_wholebody_fp16.safetensors)

**diffusion_models** (RT-DETRv4 detector):

  * [rt_detr_v4-x-hgnet_fp16.safetensors](https://huggingface.co/Comfy-Org/SDPose/blob/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) (recommended)
  * [rt_detr_v4-x-hgnet_fp32.safetensors](https://huggingface.co/Comfy-Org/SDPose/blob/main/diffusion_models/rt_detr_v4-x-hgnet_fp32.safetensors) (full precision, larger)

Place them in the following directory structure:
    
    
    📂 ComfyUI/
    └── 📂 models/
        ├── 📂 checkpoints/
        │   └── sdpose_wholebody_fp16.safetensors
        └── 📂 diffusion_models/
            ├── rt_detr_v4-x-hgnet_fp16.safetensors
            └── rt_detr_v4-x-hgnet_fp32.safetensors
    

### 

​

3\. Using the Workflows

#### 

​

Multi-Person (Image)

  * **Input** : Load an image via the `Load Image` node. Use an image with one or more people (example: `group_photo.png`).
  * **Detection** : The `Image to Pose Map (SDPose Multi-Person)` subgraph processes the image and outputs: 
    * **IMAGE** : pose skeleton visualization overlaid on the image
    * **keypoints** : raw whole-body keypoint data
    * **bboxes** : bounding box coordinates
  * **Drawing Options** : Configure which body parts to draw: 
    * `draw_body`, `draw_hands`, `draw_face`, `draw_feet`: toggle visibility
    * `stick_width`, `face_point_size`: adjust visual style
    * `score_threshold`: minimum confidence for displaying keypoints
  * **Detection Options** : 
    * `resize_type.longer_size`: scale the longer dimension before detection
    * `max_detections`: maximum number of people to detect
    * `detect_threshold`: detection confidence threshold
    * `detect_class`: object class to detect (default: person)



#### 

​

Multi-Person (Video)

Same as the image workflow but processes video frames sequentially. Use `Load Video` to input a video file and `Save Video` to export the result.

#### 

​

OOD Image to Pose

Uses the SDPose model to generate a clean pose map from an image, without bounding box visualization. This is useful for style transfer where you want to extract the skeleton pose from one image and apply it to another.

#### 

​

OOD Video to Pose Map

Generates per-frame pose maps from a video. The output is a video file where each frame contains the extracted pose skeleton, suitable for downstream animation or ControlNet workflows.

## Learn about Subgraph

These workflows use Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflows.

## 

​

Additional Notes

  * **Model directory** : the SDPose checkpoint goes in `models/checkpoints/`, and the RT-DETRv4 detector goes in `models/diffusion_models/`
  * **Input image example** : the `group_photo.png` file is available in the workflow template’s `input/` directory for testing
  * **Keypoint output** : the POSE_KEYPOINT type can be connected to downstream nodes that accept pose data for conditional generation
  * **Update required** : SDPose + RT-DETRv4 support is available in recent ComfyUI versions. Make sure your ComfyUI is up to date.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/pose-detection-sdpose.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/pose-detection-sdpose)

[BiRefNet: Remove Image Background in ComfyUIPrevious](https://docs.comfy.org/tutorials/utility/remove-background-birefnet)[MediaPipe: Face Detection in ComfyUINext](https://docs.comfy.org/tutorials/utility/face-detection/mediapipe)

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
