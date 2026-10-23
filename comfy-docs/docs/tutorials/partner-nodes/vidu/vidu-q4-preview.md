---
url: https://docs.comfy.org/tutorials/partner-nodes/vidu/vidu-q4-preview/
title: Vidu Q4 Preview in ComfyUI: Image and Reference to Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:39.636901+00:00
---

# Vidu Q4 Preview in ComfyUI: Image and Reference to Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/vidu/vidu-q4-preview/

## On this page

  * Available workflows
    * Image to Video
    * Reference to Video
    * Workflow overview
    * Steps to run
  * Node controls
  * Prompting tips
  * Get started



Vidu

# Vidu Q4 Preview in ComfyUI: Image and Reference to Video

Copy pageCopy page

Generate 3 to 16 second videos with native audio from a first frame or up to 15 reference images using the Vidu Q4 Preview partner nodes in ComfyUI.

Copy pageCopy page

**Vidu Q4 Preview** is a video generation model from Vidu, available in ComfyUI through two partner nodes. It generates clips from 3 to 16 seconds with native audio, so the picture, the dialogue, and the sound effects all come from the model in a single pass. Output runs from 540p up to 4K. In ComfyUI, **Vidu Q4 Image-to-Video Generation** animates a single first frame with an optional prompt, and **Vidu Q4 Reference-to-Video Generation** builds a clip from up to 15 reference images, optional reference audio, and a prompt. Both are cloud API nodes: they need a Comfy account with credits and download no local model. See [Partner Node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the per-second rates. Image-to-video keeps the aspect ratio of the input image. Reference-to-video takes an explicit `aspect_ratio`, and both nodes expose `duration`, `resolution`, and an `audio` toggle.

## 

​

Available workflows

### 

​

Image to Video

Animate one image. The image is the first frame of the clip and the output keeps its aspect ratio, so crop the image when you need a different shape. The prompt is optional and describes what happens in the shot. ![Vidu Q4 Preview Image to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q4_preview_i2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Vidu Q4 Preview: Image to Video” in Template Library

**Input material**

## model_turquoise_yellow_outfit.png

Load into the `LoadImage` node that feeds the Vidu Q4 Image-to-Video node

### 

​

Reference to Video

Build a clip from reference images, optional reference audio, and a prompt. Connect up to 15 reference images and up to 3 audio clips, then address them in the prompt by order: `image 1`, `image 2`, and so on. The template uses two reference images to keep a character and a prop consistent across the shot. ![Vidu Q4 Preview Reference to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q4_preview_r2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Vidu Q4 Preview: Reference to Video” in Template Library

**Input materials**

## clay_man_smiley_sweater.png

Load into the second reference image slot · `image 2`

## yellow_fuzzy_smiley.png

Load into the first reference image slot · `image 1`

### 

​

Workflow overview

Both templates use a small graph:

  * **LoadImage** : provides the first frame (image to video) or the reference images (reference to video)
  * **Vidu4ImageToVideoNode** / **Vidu4ReferenceVideoNode** : the core nodes, configured with the `Vidu Q4 Preview` model
  * **SaveVideo** : writes the finished clip



### 

​

Steps to run

  1. **Load the input** : set the first frame for image to video, or the reference images for reference to video
  2. **Select the model** : keep `Vidu Q4 Preview` on the node
  3. **Choose a resolution and duration** : from `540p` to `4K`, and 3 to 16 seconds
  4. **Toggle audio** : leave it on to keep dialogue and sound effects, off for a silent clip
  5. **Click Queue** or press `Ctrl+Enter` to generate



## 

​

Node controls

Control| Values| Applies to| Effect  
---|---|---|---  
`image`| one image| Image to Video| First frame of the clip. Aspect ratio must be between 1:5 and 5:1  
`reference_images`| up to 15| Reference to Video| One image per slot; a batch on a single slot counts per image. Address them in the prompt by order as `image 1`, `image 2`  
`reference_audios`| up to 3, 3 to 12 seconds each| Reference to Video| Voice references. Only the voice is used, not the words. Requires `audio` to be on. Assign a voice in the prompt, for example `image 1 says "Hello!" in the voice from audio 1`  
`prompt`| text, up to 5000 characters| both nodes| Optional for image to video, required for reference to video  
`aspect_ratio`| `16:9`, `9:16`, `1:1`, `3:4`, `4:3`| Reference to Video| Output aspect ratio. Image to video follows the input image instead  
`resolution`| `540p`, `720p`, `1080p`, `2K`, `4K`| both nodes| Output resolution, default `720p`  
`duration`| 3 to 16 seconds| both nodes| Slider, default 5  
`audio`| on (default), off| both nodes| Keeps native audio, including dialogue and sound effects  
`seed`| integer| both nodes| Results can still vary between runs with the same seed  
  
## 

​

Prompting tips

  * **Describe the shot, the line, and the sound**. The model renders picture and audio together, so write the action, the spoken line in quotes, and the ambience in the same prompt.
  * **Label references by their order**. Reference images are addressed as `image 1`, `image 2`. Say what each one should keep, for example keeping a character’s face and outfit from `image 1`.
  * **Write dialogue for a voice reference**. Reference audio carries the voice, not the words, so write the line in the prompt and point it at a voice, such as `image 1 says "Welcome back!" in the voice from audio 1`.
  * **Keep the aspect ratio inside the allowed range**. Reference images must sit between 1:5 and 5:1.
  * **Expect variation between runs**. The seed does not lock the result; the same settings can still produce a different take.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Vidu Q4 Preview`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/vidu/vidu-q4-preview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/vidu/vidu-q4-preview)

[Astra 2 - Creative diffusion video upscalingPrevious](https://docs.comfy.org/tutorials/partner-nodes/topaz/astra-2)[Wan 3.0 Video Generation in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/wan/wan3-0)

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
