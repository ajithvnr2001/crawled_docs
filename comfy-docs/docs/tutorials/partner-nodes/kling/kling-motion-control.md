---
url: https://docs.comfy.org/tutorials/partner-nodes/kling/kling-motion-control/
title: Kling 2.6 Motion Control in ComfyUI: Reference Video Motion Transfer - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:31.865783+00:00
---

# Kling 2.6 Motion Control in ComfyUI: Reference Video Motion Transfer - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/kling/kling-motion-control/

## On this page

  * What Kling 2.6 Motion Control is good at
  * Character orientation modes
  * Model tiers
  * Kling2.6: Motion Control
  * Input requirements
  * Tips for better results



Kling

# Kling 2.6 Motion Control in ComfyUI: Reference Video Motion Transfer

Copy pageCopy page

Transfer motion from a reference video to a character image in ComfyUI with the Kling 2.6 Motion Control node, including orientation modes and tiers.

Copy pageCopy page

Kling 2.6 Motion Control is a specialized multimodal model developed by Kuaishou that enables precise motion transfer from reference videos to character images. By combining a **Reference Image** (your character) and a **Motion Reference Video** (the action), the AI applies the movement, expression, and pacing of the video to your static character while maintaining their identity. Unlike standard image-to-video generation that guesses motion from text prompts, Motion Control uses a reference video as the movement blueprint. The model acts as a digital puppeteer, extracting choreography from your reference video and applying it to your character with cinema-grade fidelity.

## 

​

What Kling 2.6 Motion Control is good at

  * **Complex motion handling** : Execute complicated sequences like dance routines, martial arts, or athletic movements without losing character coherence. The model understands weight transfer and momentum for realistic physical impact.
  * **Precision hand and finger performance** : Hands have traditionally been a weak point for AI video. This feature specifically improves finger articulation and hand movements by mimicking real footage, making it ideal for presentations and demonstrations.
  * **Scene and environment flexibility** : Use text prompts to change the environment while the character continues their referenced motion. You’re not limited to the reference video’s background.
  * **Advanced camera and perspective modes** : Granular control over how the camera interprets your reference with distinct orientation modes.
  * **30-second one-shot support** : Generate continuous actions up to 30 seconds in a single generation, enabling uninterrupted character motion for narrative scenes.



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

Character orientation modes

The `character_orientation` parameter determines how the model interprets spatial information and constrains output duration:

Mode| Description| Max Duration  
---|---|---  
`video`| Output character orientation matches the reference video. Best for complex full-body performances like dance sequences and elaborate choreography.| 30 seconds  
`image`| Output character orientation matches the reference image. Best for portrait animations with camera movement like pans, tilts, and tracking shots.| 10 seconds  
  
## 

​

Model tiers

Tier| Resolution| Best For  
---|---|---  
**Standard**|  720p| Simple animations, social media content, memes, and quick tests. Faster and more credit-efficient.  
**Pro**|  1080p| Complex choreography, intricate hand movements, professional marketing assets, and broadcast-quality content.  
  
## 

​

Kling2.6: Motion Control

Apply precise character actions and expressions from a reference video to your character image with synchronized motion control. ![Kling2.6: Motion Control workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_motion_control-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling2.6: Motion Control” in Template Library

**Input materials** Upload these files to the matching `LoadImage` and `LoadVideo` nodes:

## streetwear_fox.jpg

`LoadImage` node 11 · `streetwear_fox.jpg`

## street_dancer.mp4

`LoadVideo` node 2 · `street_dancer.mp4`

![streetwear_fox.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/streetwear_fox.jpg)

## 

​

Input requirements

  * **Image formats** : JPG, PNG, WEBP, GIF, AVIF (max 10MB)
  * **Video formats** : MP4, MOV, WEBM, M4V, GIF (max 100MB)
  * **Video duration** : 3-30 seconds depending on orientation mode
  * **Minimum resolution** : 720px width and height
  * **Subject visibility** : Character must clearly show head, shoulders, and torso



## 

​

Tips for better results

  * **Match aspect ratios** : Ensure your character image and reference video have similar aspect ratios (e.g., both 16:9 or both 9:16) to prevent awkward stretching or cropping.
  * **Clean backgrounds** : Use reference videos with simple or static backgrounds for best motion extraction. High-contrast videos where the actor’s silhouette is distinct work best.
  * **Clear character angles** : If your reference video shows rotation, use 3D-style characters or realistic photos that handle rotation better. Flat 2D cartoons may struggle with back views.
  * **Visible limbs** : Ensure the character’s limbs are visible in the source image. If a character has hands in pockets but the motion requires waving, the AI will hallucinate hands, often leading to artifacts.
  * **Leave breathing room** : Leave negative space around the subject. If the character will dance or move arms wide, they need space within the frame to avoid clipping.
  * **Framing alignment** : Match the framing between your image and reference video. Use a close-up reference for face animations, or a full-body reference for walking/dancing sequences.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/kling/kling-motion-control.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/kling/kling-motion-control)

[Kling 3.0 Video and Image Generation in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/kling/kling-3-0)[Kling Virtual Try-On in ComfyUI: Dress a Person in Any GarmentNext](https://docs.comfy.org/tutorials/partner-nodes/kling/kling-virtual-try-on)

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
