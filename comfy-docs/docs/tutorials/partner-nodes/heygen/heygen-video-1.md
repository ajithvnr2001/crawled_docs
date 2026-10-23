---
url: https://docs.comfy.org/tutorials/partner-nodes/heygen/heygen-video-1/
title: HeyGen Video 1.0 in ComfyUI: Text, Image, and Reference to Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:31.286513+00:00
---

# HeyGen Video 1.0 in ComfyUI: Text, Image, and Reference to Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/heygen/heygen-video-1/

## On this page

  * Available workflows
    * Text to Video
    * Image to Video
    * Reference to Video
  * Node controls
  * Prompting tips
  * Get started



HeyGen

# HeyGen Video 1.0 in ComfyUI: Text, Image, and Reference to Video

Copy pageCopy page

Generate 5 to 15 second clips with synced dialogue from a prompt, a first frame, or up to 12 reference images, videos, and audio clips in ComfyUI

Copy pageCopy page

**HeyGen Video 1.0** is a general-purpose video model from HeyGen that generates the picture, the spoken line, and the ambience in one pass. You describe the shot and the dialogue in the prompt, and the clip comes back with synchronized speech, so a talking-head or product video needs no shoot, no presenter, and no separate voice-over step. In ComfyUI the model runs through two partner nodes. **HeyGen Video 1.0 Reference to Video** handles text to video on its own and reference to video once images, videos, or audio are connected; **HeyGen Video 1.0 Image to Video** starts from a first frame. Both are cloud API nodes: they need a Comfy account with credits and download no local model. See [Partner Nodes pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the per-second rates. Every run returns a 5 to 15 second clip at 480p, 768p, or 2K, with the dialogue, room tone, and any music already in the video.

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

Available workflows

### 

​

Text to Video

Generate a clip from a prompt alone. The prompt carries the action, the spoken line, and the sound, so one node run returns a finished talking clip.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HeyGen Video 1.0: Text to Video” in Template Library

The text-to-video template runs the Reference to Video node with nothing connected, which is the text-to-video mode of that node.

### 

​

Image to Video

Animate one image. The image is the first frame of the clip, and the output keeps its aspect ratio, so crop the image when you need a different shape. The prompt drives what happens and what is said.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HeyGen Video 1.0: Image to Video” in Template Library

**Input material**

## model_red_curls_ring.png

Load into the `LoadImage` node that feeds the HeyGen Video 1.0 Image to Video node

### 

​

Reference to Video

Keep people, products, and places consistent across the shot by connecting them as references: up to 9 images, 3 videos, and 3 audio clips, 12 in total. The prompt then addresses them as `@Image1`, `@Video1`, and `@Audio1`, numbered per type in input order.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HeyGen Video 1.0: Reference to Video” in Template Library

**Input materials**

## model_black_blazer_red_earrings.png

Load into the first reference image slot · `@Image1`

## cognac_leather_handbag.png

Load into the second reference image slot · `@Image2`

## 

​

Node controls

Control| Values| Applies to| Effect  
---|---|---|---  
`prompt`| text, up to 32000 characters| both nodes| The shot, the spoken line, and the sound. Reference media is addressed as `@Image1`, `@Video1`, `@Audio1`  
`duration`| 5 to 15 seconds| both nodes| Slider, default 5  
`resolution`| `480p`, `768p`, `2K`| both nodes| Output resolution. On Reference to Video, `2K` requires a `16:9` or `9:16` `aspect_ratio`, and `auto` works at `2K` only when no reference media is connected  
`aspect_ratio`| `auto`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`| Reference to Video| `auto` is 16:9 with nothing connected. With references it follows the first reference image, or the first reference video when no images are connected  
`seed`| integer| both nodes| Results can still vary between runs with the same seed  
`reference_images`| up to 9| Reference to Video| One image per slot. A batched input on a single slot is rejected  
`reference_videos`| up to 3| Reference to Video| One video per slot  
`reference_audios`| up to 3| Reference to Video| Needs at least one reference image or video connected. A voice reference wants a few seconds of clean speech  
  
The Image to Video node takes the image, the prompt, the duration, the resolution, and the seed. It has no aspect ratio control, because the first frame sets the shape of the clip.

## 

​

Prompting tips

  * **Write the spoken line into the prompt**. Put the dialogue in quotes as part of the description of the shot, so the model speaks it and matches the lip movement. Both templates ship long example prompts that show the shape: the shot and the subject first, the line in quotes, then the sound and the camera language.
  * **Describe the sound with the picture**. Room tone, a piece of music, or the noise an action makes is written into the prompt rather than set with a control. The sample prompts end with the ambience, for example quiet room tone with a faint kettle whistle, or a soft glass clink as an object is set down.
  * **Keep a product or presenter consistent**. Connect the product or the person as a reference image and name it in the prompt, then describe how it must stay the same, such as keeping the exact color, proportions, and hardware of a bag from `@Image2`.
  * **Shape the shot with references**. With `aspect_ratio` set to `auto`, the framing follows the first reference image, so the reference you connect first decides the shape of the video.
  * **Expect variation between runs**. The seed does not lock the result; the same settings can still produce a different take.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `HeyGen Video 1.0`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/heygen/heygen-video-1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/heygen/heygen-video-1)

[HappyHorse 1.0 Video Generation in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/happyhorse/happyhorse1-0)[Higgsfield Genjutsu in ComfyUI: Video Motion TransferNext](https://docs.comfy.org/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer)

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
