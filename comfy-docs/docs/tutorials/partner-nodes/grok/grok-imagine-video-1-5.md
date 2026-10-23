---
url: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-imagine-video-1-5/
title: Grok Imagine Video 1.5 in ComfyUI: Image and Text to Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:30.402430+00:00
---

# Grok Imagine Video 1.5 in ComfyUI: Image and Text to Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-imagine-video-1-5/

## On this page

  * What Grok Imagine Video 1.5 is good at
  * Grok Imagine Video 1.5: Image to Video
    * Workflow Overview
    * Steps to Run
    * Output
    * Tips
  * Grok Imagine Video 1.5 Lite
    * Lite text-to-video workflow
    * Lite image-to-video workflow



Grok

# Grok Imagine Video 1.5 in ComfyUI: Image and Text to Video

Copy pageCopy page

Use the Grok Imagine Video 1.5 partner node in ComfyUI to generate video from an image or a text prompt with native audio, including the Lite workflows.

Copy pageCopy page

The [Grok Imagine Video 1.5](https://docs.comfy.org/built-in-nodes/GrokVideoNode) Partner Node enables high-quality video generation with native audio from an image or a text prompt. Powered by xAI’s latest Grok model, it produces realistic motion with synchronized audio and supports up to **1080p** resolution. The node supports three model variants selected via its `model` parameter:

  * **`grok-imagine-video`** : the previous generation model, supports optional image input
  * **`grok-imagine-video-1.5`** : the full-quality 1.5 model, supports 1080p output
  * **`grok-imagine-video-1.5-lite`** : a faster, lower-cost variant of 1.5 that generates from a text prompt or an image, with 480p, 720p, and 1080p output

All variants generate **native audio** : sound effects, ambience, and dialogue are synthesized in the same pass, with no separate audio pipeline needed. Video duration ranges from **1 to 15 seconds**.

## 

​

What Grok Imagine Video 1.5 is good at

  * **Image-to-video generation** : produces high-quality video from a single input image
  * **Text-to-video generation** : the `grok-imagine-video-1.5-lite` variant also generates from a text prompt alone
  * **Faster, lower-cost option** : `grok-imagine-video-1.5-lite` runs at a lower per-second rate than 1.5
  * **Native audio** : sound effects, ambience, and dialogue are synthesized in the same pass, with no separate audio pipeline needed
  * **Realistic motion** : motion stays synchronized with the generated audio
  * **Up to 1080p output** : the 1.5 models support 1080p resolution
  * **Flexible duration** : video length from 1 to 15 seconds



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

Grok Imagine Video 1.5: Image to Video

![Grok Imagine Video 1.5 Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_video_1_5-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine Video 1.5” in Template Library

## Download Sample Input Image

Get the example input image for this workflow.

### 

​

Workflow Overview

This workflow uses three nodes:

  * **LoadImage** : provides the starting image frame
  * **GrokVideoNode** : the core node configured with the `grok-imagine-video-1.5` model
  * **SaveVideo** : saves the generated video with native audio



### 

​

Steps to Run

  1. **Upload a starting image** : use the **LoadImage** node to load your reference image
  2. **Enter your prompt** : describe the motion, atmosphere, and scene dynamics in the **GrokVideoNode** node
  3. **Select model** : ensure `grok-imagine-video-1.5` is selected
  4. **Set resolution** : choose output resolution (`720p` recommended)
  5. **Set duration** : choose the video length in seconds
  6. **Set seed** : control whether the node re-runs; outputs are not reproducible regardless of seed
  7. **Click Queue** : press `Ctrl+Enter` to generate



### 

​

Output

The generated video includes **native audio** synchronized with the motion, saved automatically via the **SaveVideo** node.

### 

​

Tips

  * Use high-quality input images for best results
  * The prompt works best when it describes both the **visual scene** and the **motion dynamics**
  * For different results, try varying the seed value



## 

​

Grok Imagine Video 1.5 Lite

`grok-imagine-video-1.5-lite` is the faster, lower-cost variant of 1.5. It generates from a text prompt or a starting image and supports 480p, 720p, and 1080p output. Two templates cover it.

### 

​

Lite text-to-video workflow

![Grok Imagine Video 1.5 Lite text to video workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_video_1_5_lite_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine Video 1.5 Lite: Text to Video” in Template Library

  1. Select `grok-imagine-video-1.5-lite` as the `model` in the **GrokVideoNode** node
  2. Enter a prompt describing the scene, motion, and sound
  3. Set `resolution` (480p, 720p, or 1080p) and `duration` (1 to 15 seconds)
  4. Click **Queue** to generate the video



### 

​

Lite image-to-video workflow

![Grok Imagine Video 1.5 Lite image to video workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_video_1_5_lite_i2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine Video 1.5 Lite: Image to Video” in Template Library

## Download Sample Input Image

Get the example input image for this workflow.

  1. Upload a starting image to the **LoadImage** node
  2. Select `grok-imagine-video-1.5-lite` as the `model` in the **GrokVideoNode** node
  3. Describe the motion in the prompt, then set `resolution` and `duration`
  4. Click **Queue** to generate the video



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/grok/grok-imagine-video-1-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/grok/grok-imagine-video-1-5)

[Grok Imagine Video in ComfyUI: AI Video Generation, Editing, and ExtensionPrevious](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-video)[HappyHorse 1.1 Video Generation in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/happyhorse/happyhorse1-1)

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
