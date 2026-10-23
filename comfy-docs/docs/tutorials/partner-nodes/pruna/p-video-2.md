---
url: https://docs.comfy.org/tutorials/partner-nodes/pruna/p-video-2/
title: Pruna P-Video-2: Text and Image to Video in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:37.071623+00:00
---

# Pruna P-Video-2: Text and Image to Video in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/pruna/p-video-2/

## On this page

  * What P-Video-2 is good at
  * P-Video-2: Text to Video
    * Steps to Run
    * Tips
  * P-Video-2: Image to Video
    * Steps to Run
    * Input asset
  * Node options reference



Pruna

# Pruna P-Video-2: Text and Image to Video in ComfyUI

Copy pageCopy page

Generate video from text or a starting image with Pruna P-Video-2 partner nodes in ComfyUI: 1 to 20 second clips, 720p or 1080p, native audio, draft mode.

Copy pageCopy page

Pruna P-Video-2 is Pruna’s quality-focused video generation model, available in ComfyUI through two partner nodes: **Pruna P-Video-2 Text to Video** and **Pruna P-Video-2 Image to Video**. It produces clips from 1 to 20 seconds at 720p or 1080p, at 24 or 48 fps, in seven aspect ratios (16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 1:1), with native audio: ambience, sound effects, and lip-synced dialogue generated from the prompt. The image-to-video node animates a first frame with an optional last frame, and both nodes accept an optional audio input that drives the motion and becomes the soundtrack. A draft mode renders faster, less detailed previews billed at 60% of the standard rate, so you can iterate on composition before committing to a full-quality render. The nodes run entirely on Pruna’s servers through the Comfy API. No model downloads or local GPU are required; you need a Comfy API account with credits.

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

What P-Video-2 is good at

  * **Native audio** : generates a soundtrack with ambience, sound effects, and lip-synced dialogue, or follows a connected audio track
  * **Flexible output** : 720p or 1080p at 24 or 48 fps, 1 to 20 seconds (or `auto` duration chosen from the prompt), seven aspect ratios
  * **Draft mode** : faster, less detailed previews at 60% of the standard rate
  * **First and last frame** : image-to-video animates between two images with closely matched aspect ratios

Pricing depends on resolution and draft mode, billed per second. See [Pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for details.

## 

​

P-Video-2: Text to Video

Generate a video from a text prompt. ![Pruna P-Video-2 Text to Video Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Prune P-Video 2: Text to Video” in Template Library

### 

​

Steps to Run

  1. **Enter your prompt** : describe the scene, its motion, and its sound in the **Pruna P-Video-2 Text to Video** node (up to 5000 characters)
  2. **Set duration and resolution** : pick 1 to 20 seconds or `auto`, then 720p (about 0.9 megapixels) or 1080p (about 2 megapixels)
  3. **Choose the frame rate** : 24 or 48 fps. 48 fps is not available with draft at 1080p
  4. **Optional: connect audio** : an audio input drives the motion and sets the video length instead of `duration` (1 to 20 seconds; longer audio is truncated)
  5. **Click Queue** : press `Ctrl+Enter` to generate



### 

​

Tips

  * `enhance_prompt` (on by default) rewrites short prompts with more detail. Turn it off to reproduce a result exactly with the same seed
  * `generate_audio` can be turned off for a silent clip



## 

​

P-Video-2: Image to Video

Animate an image into a video, with an optional last frame. ![Pruna P-Video-2 Image to Video Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_i2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Prune P-Video 2: Image to Video” in Template Library

### 

​

Steps to Run

  1. **Upload a first frame** : connect a **LoadImage** node. The output keeps the aspect ratio of this image
  2. **Optional: upload a last frame** : the video ends on this image. Its aspect ratio must be close to the first frame’s
  3. **Describe the motion and sound** : write how the scene moves and sounds in the prompt (up to 5000 characters)
  4. **Set duration, resolution, and frame rate** : same options as text to video
  5. **Click Queue** : press `Ctrl+Enter` to generate



### 

​

Input asset

The example workflow uses this sample image:

  * [alien_mothership_foggy_megacity.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/alien_mothership_foggy_megacity.png)



## 

​

Node options reference

Option| Values| Default| Notes  
---|---|---|---  
`duration`| 1 to 20, or auto| 5| Ignored when audio is connected; the video then follows the audio length  
`resolution`| 720p / 1080p| 720p| 720p is about 0.9 MP, 1080p about 2 MP at 16:9  
`fps`| 24 / 48| 24| 48 fps unavailable with draft at 1080p  
`draft`| on / off| off| Faster, less detailed render at 60% of the standard rate  
`generate_audio`| on / off| on| Ignored when audio is connected  
`enhance_prompt`| on / off| on| Advanced. Turn off for exact seed reproducibility  
`seed`| 0 to 2147483647| 42| Exact reproducibility requires enhance_prompt off  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/pruna/p-video-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/pruna/p-video-2)

[Moonvalley Marey in ComfyUI: Video Generation (Deprecated)Previous](https://docs.comfy.org/tutorials/partner-nodes/moonvalley/moonvalley-video-generation)[Runway Gen4 Turbo in ComfyUI: Image-to-Video WorkflowNext](https://docs.comfy.org/tutorials/partner-nodes/runway/video-generation)

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
