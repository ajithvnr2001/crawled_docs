---
url: https://docs.comfy.org/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer/
title: Higgsfield Genjutsu in ComfyUI: Video Motion Transfer - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:31.150361+00:00
---

# Higgsfield Genjutsu in ComfyUI: Video Motion Transfer - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer/

## On this page

  * Higgsfield Genjutsu: Motion Transfer
  * Node controls
  * Prompting tips
  * Get started



Higgsfield

# Higgsfield Genjutsu in ComfyUI: Video Motion Transfer

Copy pageCopy page

Recast a video in ComfyUI with Higgsfield Genjutsu: 1 to 8 reference images rebuild its cast, while the source clip keeps its motion, camera, and audio.

Copy pageCopy page

**Higgsfield Genjutsu Motion Transfer** rebuilds an existing video instead of generating a new one. The source clip keeps its motion, camera movement, timing, and audio, while the cast, location, wardrobe, and style are rebuilt from 1 to 8 reference images. You describe what should be different, and the rest of the shot stays as it was filmed. Higgsfield ships Genjutsu in two modes, Motion Transfer and Object Swap. ComfyUI exposes Motion Transfer through the `HiggsfieldMotionTransferNode` in the `partner/video/Higgsfield` category. It is a cloud API node: it needs a Comfy account with credits, downloads no model, and bills per output second, because the length of the result follows the source clip. The node is useful when the performance already exists and only the look has to change. Recast a phone clip with a different character, move a shoot to a location that was never available, restyle footage for another market, or produce several variants of one take without filming each one separately.

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

Higgsfield Genjutsu: Motion Transfer

Recast a video from reference images while the source clip keeps its motion, camera movement, timing, and audio.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Higgsfield Genjutsu: Motion Transfer” in Template Library

**Input materials** Upload these files to the matching `LoadVideo` and `LoadImage` nodes:

## rooftop_dancer.mp4

`LoadVideo` · source motion clip

## snow_queen_ref.png

`LoadImage` · character reference · `image_1`

## ice_palace_ref.png

`LoadImage` · scene reference · `image_2`

## 

​

Node controls

Control| Values| Effect  
---|---|---  
`model`| `genjutsu-v1.0`| The Genjutsu model. Selecting it reveals the inputs below  
`video`| 4 to 30 seconds| Source clip whose motion, camera movement, timing, and audio are kept. A shorter clip is rejected, and a longer one is trimmed to its first 30 seconds  
`reference_images`| 1 to 8 images| The characters, locations, or styles to use. Connect one image per slot (`image_1`, `image_2`, and so on); a batched input counts once per image, and the total across all slots cannot exceed 8  
`prompt`| text, optional| Describes the result, for example which reference replaces which person, or a new setting  
`resolution`| `480p`, `720p`, `1080p`| Output resolution, default `720p`  
`seed`| integer| Only controls whether the node re-runs. Results can still vary between runs with the same seed  
  
The output length follows the prepared source clip, so a 12-second clip returns a 12-second video.

## 

​

Prompting tips

  * **Name what each reference replaces.** The prompt is optional, but it is the only place to say which image belongs to which person or object. Write it as a short instruction, such as recasting the dancer as the character in the first reference image and using the second one for the new setting.
  * **Keep the reference set narrow.** One image per element is usually enough: a character, a location, a wardrobe change, or a style. Adding more images gives the model more to blend, which makes the result less predictable.
  * **Match the framing you want.** The output keeps the motion and camera of the source clip, so choose a source video whose framing already suits the result. A close-up performance stays a close-up.
  * **Describe the change, not the whole scene.** Everything not mentioned in the prompt is rebuilt from the references, so there is no need to restate the motion, the pacing, or the audio.
  * **Expect variation between runs.** The seed does not lock the result; the same settings can produce a different take.



## 

​

Get started

  1. Update ComfyUI to version 0.40.0 or later
  2. Go to **Template Library** , search for `Higgsfield Genjutsu`
  3. Load the source clip in the `LoadVideo` node and the reference images in the `LoadImage` nodes
  4. Write the prompt, pick a `resolution`, then run the workflow



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer)

[HeyGen Video 1.0 in ComfyUI: Text, Image, and Reference to VideoPrevious](https://docs.comfy.org/tutorials/partner-nodes/heygen/heygen-video-1)[Kling 3.0 Video and Image Generation in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/kling/kling-3-0)

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
