---
url: https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash-1-2/
title: Gemini Omni Flash 1.2: Conversational Video Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:32.608281+00:00
---

# Gemini Omni Flash 1.2: Conversational Video Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash-1-2/

## On this page

Back to top

  * What Gemini Omni Flash 1.2 is good at
  * Available workflows
    * Text to Video (Omni Flash 1.2)
    * Image to Video (Omni Flash 1.2)
    * Reference to Video (Omni Flash 1.2)
    * Video Edit (Omni Flash 1.2)
    * Video Extend (Omni Flash 1.2)
  * Get started



Google

# Gemini Omni Flash 1.2: Conversational Video Generation

Copy pageCopy page

Generate and edit video with Gemini Omni Flash 1.2 in ComfyUI: text, image, reference, edit and extend workflows, with native audio on every clip.

Copy pageCopy page

Gemini Omni Flash 1.2 is Google’s conversational video model, available in ComfyUI through the **Google Gemini Omni (Video)** partner node. Describe the shot in plain language, attach reference images or a clip, and the node returns video with synchronized audio. Version 1.2 renders clips from 3 to 15 seconds at 360p, 720p, 1080p or 4K, in 16:9 or 9:16. It takes up to 14 reference images and 3 reference videos, and extends a clip to 30 seconds. Omni Flash 1.1 and the older preview model stay selectable in the node.

## 

​

What Gemini Omni Flash 1.2 is good at

  * **Conversational editing** : change a character, relight a scene, alter the camera angle, or add and remove objects while the rest of the shot keeps its framing and audio
  * **Multimodal input** : combine text, up to 14 images, and up to 3 reference videos of 15 seconds each
  * **Keyframe interpolation** : with the `image_to_video` task, attach a starting frame and an optional ending frame, and the model generates the footage between them
  * **Reference to video** : tag each reference image as `<IMAGE_REF_0>` and name it in the prompt, so a character or product appears in a new scene instead of being used as a frame
  * **Scene extension** : the `extend` task continues a clip from its last frames, up to a 30-second result, without a visible seam
  * **Resolution control** : draft at 360p, then render the final clip at up to 4K



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

The Gemini Omni Flash 1.2 workflows require ComfyUI 0.44.1 or later. Select **Omni Flash 1.2** in the node’s model dropdown.

## 

​

Available workflows

### 

​

Text to Video (Omni Flash 1.2)

Write the scene, the length (3 to 15 seconds), and the motion into one prompt. The node returns the clip with a generated audio track. ![Gemini Omni Flash 1.2 Text to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.2” in Template Library

### 

​

Image to Video (Omni Flash 1.2)

Animate a still with the `image_to_video` task. The first image is the opening frame, an optional second image is the closing frame, and the prompt carries the motion and the sound. ![Gemini Omni Flash 1.2 Image to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_i2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.2” in Template Library

### 

​

Reference to Video (Omni Flash 1.2)

Keep a subject consistent across a new scene. Tag each reference image as `<IMAGE_REF_0>` and name the tag in the prompt: the character or product appears in the clip, while the image itself is never used as a frame. ![Gemini Omni Flash 1.2 Reference to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_r2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.2” in Template Library

### 

​

Video Edit (Omni Flash 1.2)

Change one thing in a finished clip with the `edit` task: swap a background, restyle a scene, add or remove an element, while the cut, timing and audio stay. Attach exactly one video of up to 15 seconds, keep the prompt to the change you want, and add “keep everything else the same” for maximum consistency. ![Gemini Omni Flash 1.2 Video Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.2” in Template Library

### 

​

Video Extend (Omni Flash 1.2)

Continue a finished clip instead of re-shooting it. The `extend` task reads the last frames and keeps the subject, framing and audio running for the next stretch: a 5-second input becomes a 10-second output. Input videos can be up to 25 seconds, and the result can reach 30 seconds. ![Gemini Omni Flash 1.2 Video Extend workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_extend-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.2” in Template Library

## 

​

Get started

  1. Update ComfyUI to 0.44.1 or later
  2. Double-click the canvas and search for “Google Gemini Omni (Video)”, or open a workflow from the Template Library
  3. Select **Omni Flash 1.2** in the model dropdown
  4. Pick the task that matches your input, write the prompt, and run



For the best results, pair Gemini Omni Flash with Nano Banana 2 Lite: generate images at high speed, then animate them into video.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/google/gemini-omni-flash-1-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/google/gemini-omni-flash-1-2)

[Crystal Video Upscale](https://docs.comfy.org/tutorials/partner-nodes/clarityai/crystal-video-upscale)[Gemini Omni Flash](https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash)
