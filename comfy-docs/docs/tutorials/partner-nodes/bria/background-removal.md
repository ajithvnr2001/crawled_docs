---
url: https://docs.comfy.org/tutorials/partner-nodes/bria/background-removal/
title: Bria Background Removal in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-08T14:09:48.182607+00:00
---

# Bria Background Removal in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bria/background-removal/

## On this page

Back to top

  * What Bria Background Removal is good at
  * Example outputs
    * Bria: Remove Image Background
    * Bria: Guided Remove Background
  * Video Background Processing
    * Bria: Remove Video Background
    * Bria: Remove Video Background (Transparent)
    * Bria: Video Green Screen
    * Bria: Video Replace Background



Bria

# Bria Background Removal in ComfyUI

Copy pageCopy page

Remove backgrounds from images and video in ComfyUI with Bria Partner Nodes, including guided removal, transparent video, green screen, and replacement.

Copy pageCopy page

Bria’s AI background processing models are now available in ComfyUI through Partner Nodes. This page covers **Image Background Removal** , **Guided Image Background Removal** , **Video Background Removal** , **Transparent Video Background** , **Video Green Screen** , and **Video Background Replacement**.

## 

​

What Bria Background Removal is good at

  * **Image background removal** : Automatically removes an image’s background and returns the result with a transparent background
  * **Guided image background removal** : Keeps the subject a prompt describes and removes the rest, so one subject can be cut out of a busy scene instead of keeping everything that is not background
  * **Video background removal** : Replaces a video’s background with a solid color of your choice, or outputs the video with transparency
  * **Video green screen** : Applies a professional chroma-key green or blue screen effect, with presets including broadcast_green, chroma_green, and blue_screen
  * **Video background replacement** : Replaces a video’s background with a custom image or another video
  * **Short-form video support** : Video background processing accepts input videos up to 60 seconds



## 

​

Example outputs

Image background removal, returning the subject on a transparent background: ![Bria: Remove Image Background example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/utility_bria_remove_image_background.png)

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

### 

​

Bria: Remove Image Background

Upload an image to automatically remove its background using the Bria API. The result is returned as an image with a transparent background. ![Bria: Remove Image Background workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_bria_remove_image_background-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Remove Image Background” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## denim_girl.png

`LoadImage` node 26 · `denim_girl.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/denim_girl.png)![Bria: Remove Image Background example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/utility_bria_remove_image_background.png)

### 

​

Bria: Guided Remove Background

Remove an image’s background while keeping what a prompt describes. Instead of keeping everything that is not background, the node narrows the cutout to the subject you name, which is how one person or object comes out of a busy scene intact. The original pixels come back at full resolution with a new alpha channel. ![Bria: Guided Remove Background workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_guided_remove_background-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Guided Background Removal” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## bria_guided_person.png

Load into the `LoadImage` node

The `prompt` names what stays, for example `the man in the blue shirt` or `only the shoes`. A prompt that matches nothing returns a fully transparent image. `moderation` on exposes separate visual input and output toggles; off skips them. For a plain cutout with no guidance, use **Bria: Remove Image Background** above.

## 

​

Video Background Processing

Bria’s video background processing nodes let you remove, replace, or apply chroma-key effects to video backgrounds. The input video must be 60 seconds or shorter.

### 

​

Bria: Remove Video Background

Replace a video’s background with a solid color of your choice. ![Bria: Remove Video Background workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Remove Video Background” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## spear_warrior.mp4

`LoadVideo` node 4 · `spear_warrior.mp4`

### 

​

Bria: Remove Video Background (Transparent)

Remove the background from a video and output it with transparency. ![Bria: Remove Video Background \(Transparent\) workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background_transparent-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Remove Video Background (Transparent)” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## ad_video_demo.mp4

`LoadVideo` node 5 · `ad_video_demo.mp4`

### 

​

Bria: Video Green Screen

Apply a professional chroma-key green or blue screen effect to your video, with multiple preset options including broadcast_green, chroma_green, and blue_screen. ![Bria: Video Green Screen workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_green_screen-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Video Green Screen” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## investigator.mp4

`LoadVideo` node 5 · `investigator.mp4`

### 

​

Bria: Video Replace Background

Replace a video’s background with a custom image or another video. ![Bria: Video Replace Background workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_replace_background-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Video Replace Background” in Template Library

**Input materials** Upload these files to the matching `LoadVideo` and `LoadImage` nodes:

## stained_window_vintage_woman.mp4

`LoadVideo` node 4 · `stained_window_vintage_woman.mp4`

## gothic_hall_light_rays.png

`LoadImage` node 8 · `gothic_hall_light_rays.png`

![gothic_hall_light_rays.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/gothic_hall_light_rays.png)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bria/background-removal.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bria/background-removal)

[Image Editing](https://docs.comfy.org/tutorials/partner-nodes/bria/image-editing)[FIBO 2.0](https://docs.comfy.org/tutorials/partner-nodes/bria/fibo)
