---
url: https://docs.comfy.org/tutorials/partner-nodes/veed/veed-video/
title: VEED Video Nodes: Talking Photo, Lip Sync & Background Removal - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:30.145047+00:00
---

# VEED Video Nodes: Talking Photo, Lip Sync & Background Removal - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/veed/veed-video/

## On this page

  * Available workflows
    * Fabric 1.0: Talking Photo
    * Lipsync 2.0
    * Remove Video Background
  * Node controls
  * Tips
  * Get started



VEED

# VEED Video Nodes: Talking Photo, Lip Sync & Background Removal

Copy pageCopy page

Use VEED partner nodes in ComfyUI to make a photo talk, re-sync a speaker to new audio, and cut a subject out of a clip as an alpha matte.

Copy pageCopy page

The **VEED** video nodes cover the edit steps that usually need a second application: turning a still image into a talking portrait, replacing the speech in existing footage, and cutting a subject away from its background. In ComfyUI the provider runs through three partner nodes. **VEED Fabric 1.0** animates a photo from an audio track. **VEED Lipsync 2.0** re-syncs a speaker to new dialogue. **VEED Remove Video Background** returns the frames and an alpha mask instead of a flattened video, so the subject composites into anything. All three are cloud API nodes: they need a Comfy account with credits and download no model files locally. Each node bills per second or per frame of the clip you send. For speech cleanup on audio and video, see [VEED Clean Audio](https://docs.comfy.org/tutorials/partner-nodes/veed/veed-clean-audio).

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

Fabric 1.0: Talking Photo

Make a still image speak. The face in the photo is lip-synced to the audio you connect, and the clip keeps the image’s aspect ratio, so a portrait stays a portrait. It works on photos, illustrations, and mascots, which makes it a way to put a voice on artwork or on a character that was never filmed. ![VEED Fabric 1.0: Talking Photo workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_fabric_1_0-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “VEED Fabric 1.0: Talking Photo” in Template Library

**Input materials**

## black_fashion_portrait.png

Load into the `LoadImage` node. One clear, front-facing face

## audio_see_beyond_the_light.mp3

Load into the `LoadAudio` node. The speech sets the lip movement and the clip length

The audio runs up to 300 seconds and the video is exactly as long as the audio. Resolution is 480p or 720p: about 864x480 at 16:9 for 480p and 1312x736 for 720p.

### 

​

Lipsync 2.0

Keep footage you already shot and replace what the speaker says. The mouth is re-synced to the new audio while the rest of the frame stays as recorded, which is how a line gets rewritten or a clip gets dubbed without another shoot. ![VEED Lipsync 2.0 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_lipsync_2_0-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “VEED Lipsync 2.0: Lip Sync” in Template Library

**Input materials**

## rainbow_face_portrait_prism_video.mp4

Load into the `LoadVideo` node. One front-facing speaker

## veed_lipsync_rainbow_night_speech.wav

Load into the `LoadAudio` node. The new speech to sync to

The new speech runs up to 600 seconds and sets the output length. The video keeps its source resolution at 25 fps. When the footage is shorter than the audio, it plays forward and then backward until the audio ends, so send a clip that is long enough when the shot has to keep its direction.

### 

​

Remove Video Background

Cut the subject out of a clip. Instead of a flattened video, the node returns the frames plus a mask that marks what was background, so the subject composites over a new scene or exports as a transparent sequence. ![VEED Remove Video Background workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_remove_video_background-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “VEED Remove Video Background: Matte Export” in Template Library

**Input material**

## swimcap_glass_pop_video.mp4

Load into the `LoadVideo` node. Clips run up to 60 seconds

The template turns the mask into alpha for a PNG sequence. Add `Invert Mask` before `Image Composite Masked` when you want the subject as the compositing mask, or `Join Image with Alpha` followed by `Save WEBM` for a transparent video. Set the WEBM codec to `vp9`: it is the only option that writes the alpha channel, and `av1` drops it.

## 

​

Node controls

Control| Values| Applies to| Effect  
---|---|---|---  
`model`| `fabric-1.0`, `lipsync-2.0`, `standard`, `fast`, `green screen`| each node| The VEED model for that node  
`image`| image| Fabric 1.0| The face that speaks. Aspect ratio drives the output shape  
`video`| clip| Lipsync 2.0, Remove Video Background| Source footage. Up to 60 seconds on background removal  
`audio`| track| Fabric 1.0, Lipsync 2.0| The speech to sync to. Sets the output length  
`resolution`| `480p`, `720p`| Fabric 1.0| Output size class, 720p by default  
`seed`| integer| Lipsync 2.0| Rerun control only. Results stay non-deterministic  
`refine_foreground_edges`| on by default| Remove Video Background, standard and fast| Cleaner edges on hair and fur. Turning it off lowers the price  
`subject_is_person`| on by default| Remove Video Background, standard and fast| Turn it off when the subject is an object or an animal  
`spill_suppression_strength`| 0.0 to 1.0, default 0.8| Remove Video Background, green screen| How strongly green cast is removed. Raise it when green spots remain, lower it when colors shift  
  
Output resolution on background removal has no control: standard and green screen return up to 3840x2160, fast returns up to 1920x1080, and larger input is downscaled.

## 

​

Tips

  * **Send clean, front-facing footage.** Fabric wants one visible face, and Lipsync wants one speaker looking at the camera. Profiles and crowded frames are where either node gives up detail.
  * **Let the audio define the length.** Both talking nodes produce exactly as long a clip as the speech you connect, so cut the audio before the run rather than trimming video afterwards.
  * **Feed generated speech straight in.** Connect a text-to-speech node to `audio` and the portrait or the dubbed clip follows it without an export step.
  * **Only pay for edge refinement when you need it.** Turning `refine_foreground_edges` off on background removal lowers the per-frame rate, which is worth it on hard-edged subjects.
  * **Use green screen only on real green screen plates.** The green screen mode keys a backdrop and has no edge refinement or person detection, so a natural background belongs on standard or fast.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `VEED`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/veed/veed-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/veed/veed-video)

[Astra 2](https://docs.comfy.org/tutorials/partner-nodes/topaz/astra-2)[Vidu Q4 Preview](https://docs.comfy.org/tutorials/partner-nodes/vidu/vidu-q4-preview)
