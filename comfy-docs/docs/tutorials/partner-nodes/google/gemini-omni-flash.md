---
url: https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash/
title: Gemini Omni Flash: Conversational Video Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:29.243883+00:00
---

# Gemini Omni Flash: Conversational Video Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash/

## On this page

  * What Gemini Omni Flash 1.1 is good at
  * Available workflows
    * Text to Video (Omni Flash)
    * Text to Video (Omni Flash 1.1)
    * Image to Video (Omni Flash 1.1)
    * Reference to Video (Omni Flash 1.1)
    * Video Edit (Omni Flash 1.1)
    * Video Extend (Omni Flash 1.1)
  * Get started



Google

# Gemini Omni Flash: Conversational Video Generation

Copy pageCopy page

Generate and edit videos through natural language using Gemini Omni Flash 1.1, Google’s multimodal video model, available in ComfyUI through Partner Nodes

Copy pageCopy page

Gemini Omni Flash is Google DeepMind’s conversational video generation and editing model, part of the Gemini Omni family first introduced at Google I/O 2026. It combines Gemini’s multimodal reasoning with native video creation: you describe what you want in plain language, attach reference images or videos, and the model generates a clip with synchronized audio. The current version, Gemini Omni Flash 1.1, reached general availability on August 27, 2026 and adds keyframe interpolation, 360p/4K output options, and scene extension.

## 

​

What Gemini Omni Flash 1.1 is good at

  * **Conversational video editing** : Refine and edit videos using natural language: swap characters, relight scenes, alter angles, add or remove objects while maintaining the original audio and video tracks
  * **Multimodal input** : Combine text, images (up to 14), and videos (up to 3, 10 seconds each) to guide generation. Every output carries a native audio track
  * **Keyframe interpolation** : With the `image_to_video` task, attach a starting frame and an optional ending frame, and the model generates the footage in between
  * **Reference to video** : Bind reference images to roles with tags like `<IMAGE_REF_0>` so characters, products, and objects from your images appear in a new scene without the image itself being used as a frame
  * **Scene extension** : The `extend` task appends up to 10 seconds of new footage to a clip, reading the last 10 seconds of context for character and motion consistency, up to about 40 seconds cumulatively
  * **Resolution control** : Draft at 360p (about one third of the 720p cost), then re-render at 720p, 1080p, or 4K. 16:9 and 9:16 aspect ratios are supported
  * **World knowledge and simulation** : Combines physics understanding with Gemini’s knowledge of history, science, and cultural context, enabling meaningful storytelling beyond photorealism
  * **Text and action synchronization** : Render legible text and graphics directly into video, syncing kinetic typography with on-screen movements



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

The Gemini Omni Flash 1.1 workflows require ComfyUI 0.34.2 or later. In the node, select **Omni Flash 1.1** from the model dropdown to use the GA model; the **Omni Flash** option runs the preview model, which is scheduled to retire on September 30, 2026.

## 

​

Available workflows

### 

​

Text to Video (Omni Flash)

Generate video from a single text prompt with the preview-tier Gemini Omni Flash model. Describe the scene, the length, and the aspect ratio in one prompt, and the model renders the clip with a native audio track. ![Gemini Omni Flash Text to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni” in Template Library

The preview Omni Flash model is scheduled to retire on September 30, 2026. Use the Omni Flash 1.1 workflows below for the GA model.

### 

​

Text to Video (Omni Flash 1.1)

Generate cinematic video from natural language prompts with Gemini Omni Flash 1.1. Describe the desired length (3 to 10 seconds) directly in the prompt, and pick the aspect ratio and output resolution in the node: 16:9 or 9:16, 360p for cheap drafts, up to 4K for final renders. Every clip includes a generated audio track. ![Gemini Omni Flash 1.1 Text to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.1” in Template Library

### 

​

Image to Video (Omni Flash 1.1)

Animate an image with Gemini Omni Flash 1.1. With the `image_to_video` task, the first attached image becomes the starting frame and an optional second image becomes the ending frame: the model generates the footage in between, which makes camera orbits, zoom transitions, and looping clips predictable. ![Gemini Omni Flash 1.1 Image to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_i2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.1” in Template Library

### 

​

Reference to Video (Omni Flash 1.1)

Generate video that incorporates specific subjects from up to 14 reference images. In reference mode, bind each image to a role with tags like `<IMAGE_REF_0>` and refer to the tags in your prompt: characters, products, and objects from your images appear in the scene while the image itself is never used as a frame. Combine character references with style references for brand-consistent content. ![Gemini Omni Flash 1.1 Reference to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_r2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.1” in Template Library

### 

​

Video Edit (Omni Flash 1.1)

Edit videos with natural language using Gemini Omni Flash 1.1. With the `edit` task, the node takes exactly one input video (10 seconds or less) and rewrites it based on your instructions: swap backgrounds, restyle scenes, add or remove elements. The `edit` and `extend` tasks keep the aspect ratio of the input video. Simple prompts work best; adding “keep everything else the same” maximizes consistency. ![Gemini Omni Flash 1.1 Video Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.1” in Template Library

### 

​

Video Extend (Omni Flash 1.1)

Extend an existing video by up to 10 seconds per step with the `extend` task, building stories up to about 40 seconds total. The model analyzes the last 10 seconds of context, keeping characters, motion, and audio coherent as the scene continues from where it left off. Optionally attach reference images to introduce new characters mid-story. Extension appends new content only at the end of the clip, but the model may revise the final source frames to make the transition seamless. ![Gemini Omni Flash 1.1 Video Extend workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_extend-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemini Omni 1.1” in Template Library

## 

​

Get started

  1. Update ComfyUI to the latest version (0.34.2 or later for the Omni Flash 1.1 workflows)
  2. Double-click the canvas and search for “Gemini Omni Flash” nodes
  3. Or go to the Template Library to use the ready-to-go workflows
  4. Choose the workflow that matches your input type (text, image, or video)
  5. Enter your prompt and generate



For the best results, combine Gemini Omni Flash with Nano Banana 2 Lite: generate images at high speed, then use Gemini Omni Flash to animate them into video.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/google/gemini-omni-flash.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/google/gemini-omni-flash)

[ByteDance vCube Video Enhance in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/bytedance/vcube)[Grok Imagine Video in ComfyUI: AI Video Generation, Editing, and ExtensionNext](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-video)

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
