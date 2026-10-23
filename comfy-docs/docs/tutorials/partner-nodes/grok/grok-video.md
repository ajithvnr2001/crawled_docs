---
url: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-video/
title: Grok Imagine Video in ComfyUI: AI Video Generation, Editing, and Extension - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:31.549997+00:00
---

# Grok Imagine Video in ComfyUI: AI Video Generation, Editing, and Extension - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-video/

## On this page

  * What Grok Imagine Video is good at
  * Example outputs
  * Grok: Video Generation
    * Workflow overview
    * Steps to run
  * Grok: Video Edit
    * Workflow overview
    * Steps to run
  * Grok: Video Extend
    * Workflow overview
    * Steps to run
  * Grok: Reference to Video
    * Workflow overview
    * Steps to run



Grok

# Grok Imagine Video in ComfyUI: AI Video Generation, Editing, and Extension

Copy pageCopy page

Generate, edit, and extend videos with Grok Imagine in ComfyUI: text/image to video, video editing, video extension, and reference-to-video workflows

Copy pageCopy page

Grok Imagine Video is xAI’s video generation family, available in ComfyUI through the Grok partner nodes. It covers video generation from text or an image, video editing, seamless video extension, and reference-to-video generation guided by character or style images. For the latest model, see [Grok Imagine Video 1.5](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-imagine-video-1-5).

## 

​

What Grok Imagine Video is good at

  * **Video generation with audio** : produces up to 15-second clips with synchronized audio from a text prompt, with an optional starting image
  * **Natural-language video editing** : restyles footage, changes the setting, or applies a new aesthetic while keeping the original motion and content
  * **Seamless video extension** : continues a short video with a new clip that follows on from the original footage, based on a natural-language description of the next scene
  * **Reference-to-video** : generates video guided by up to 7 reference images, keeping characters, products, or styles consistent
  * **Resolution options** : outputs at 480p or 720p



## 

​

Example outputs

Video generation from a text prompt with synchronized audio: Video editing with natural-language instructions, keeping the original motion: Video extension, continuing a short clip with a new scene: Reference-to-video, keeping the subject consistent from reference images:

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

Grok: Video Generation

Generate a short video from a text prompt, with an optional starting image. This workflow uses the `grok-imagine-video` model to produce up to 15-second clips with synchronized audio.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine” in Template Library

### 

​

Workflow overview

This workflow uses three nodes:

  * **LoadImage** : provides the optional starting image frame
  * **GrokVideoNode** : the core node, configured with the `grok-imagine-video` model
  * **SaveVideo** : saves the generated video with audio



### 

​

Steps to run

  1. **Enter your prompt** : describe the motion, atmosphere, and scene dynamics in the **GrokVideoNode**
  2. **Optionally load a starting image** : connect an image to the **LoadImage** node
  3. **Set resolution** : `480p` or `720p`
  4. **Set duration** : choose a length from 1 to 15 seconds
  5. **Set seed** : control whether the node re-runs; outputs are not reproducible regardless of seed
  6. **Click Queue** : press `Ctrl+Enter` to generate



## 

​

Grok: Video Edit

Edit an uploaded video with natural-language instructions. Restyle the footage, change the setting, or apply a new aesthetic while keeping the original motion and content.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine” in Template Library

### 

​

Workflow overview

This workflow uses three nodes:

  * **LoadVideo** : provides the source video to edit
  * **GrokVideoEditNode** : the core node, configured with the `grok-imagine-video` model
  * **SaveVideo** : saves the edited video



### 

​

Steps to run

  1. **Load a video** : connect your video to the **LoadVideo** node (1 to 8.7 seconds, up to 50MB)
  2. **Describe the edit** : tell the model how to transform the footage in the **GrokVideoEditNode** prompt
  3. **Click Queue** : press `Ctrl+Enter` to generate



## 

​

Grok: Video Extend

Extend a short video with a seamless continuation. Describe the next scene in natural language, and the model generates a new clip that follows on from the original footage.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine” in Template Library

### 

​

Workflow overview

This workflow uses three nodes:

  * **LoadVideo** : provides the source video to extend
  * **GrokVideoExtendNode** : the core node, configured with the `grok-imagine-video` model
  * **SaveVideo** : saves the extended video



### 

​

Steps to run

  1. **Load a video** : connect your video to the **LoadVideo** node (MP4, 2 to 15 seconds, up to 50MB)
  2. **Describe the next scene** : tell the model what should happen next in the **GrokVideoExtendNode** prompt
  3. **Set duration** : choose the extension length (2 to 10 seconds)
  4. **Click Queue** : press `Ctrl+Enter` to generate



## 

​

Grok: Reference to Video

Generate a video guided by up to 7 reference images. Use character, product, or style references to keep the subject consistent while the prompt describes the motion and scene.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine” in Template Library

### 

​

Workflow overview

This workflow uses four nodes:

  * **LoadImage** x2: provide the character and object reference images
  * **GrokVideoReferenceNode** : the core node, configured with the `grok-imagine-video` model and reference images
  * **SaveVideo** : saves the generated video



### 

​

Steps to run

  1. **Load your references** : connect up to 7 reference images to the **LoadImage** nodes
  2. **Enter your prompt** : describe the scene, motion, and how the references appear in the **GrokVideoReferenceNode**
  3. **Set resolution** : `480p` or `720p`
  4. **Set aspect ratio** : pick from `16:9` down to `9:16`
  5. **Set duration** : choose a length from 2 to 10 seconds
  6. **Click Queue** : press `Ctrl+Enter` to generate



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/grok/grok-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/grok/grok-video)

[Gemini Omni Flash: Conversational Video GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash)[Grok Imagine Video 1.5 in ComfyUI: Image and Text to VideoNext](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-imagine-video-1-5)

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
