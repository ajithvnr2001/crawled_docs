---
url: https://docs.comfy.org/tutorials/partner-nodes/veed/veed-dubbing/
title: VEED Dubbing: Translate and Lip Sync Video Speech in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-28T13:54:25.272168+00:00
---

# VEED Dubbing: Translate and Lip Sync Video Speech in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/veed/veed-dubbing/

## On this page

Back to top

  * Available workflow
    * VEED Dubbing: video translation
  * Node controls
  * Tips
  * Get started



VEED

# VEED Dubbing: Translate and Lip Sync Video Speech in ComfyUI

Copy pageCopy page

Translate a video’s speech into another language in ComfyUI with VEED Dubbing: each speaker’s voice is cloned and the lips are re-synced to the translation.

Copy pageCopy page

VEED Dubbing translates the speech in a clip into another language. Every speaker’s voice is cloned and their lips are re-synced to the translation, so the result looks spoken in the target language instead of captioned. In ComfyUI the node is **VEED Dubbing** , with two model tiers. `standard` is the cheaper one: mono audio, 85 target languages, with Spanish as Latin American and Portuguese as Brazilian. `pro` adds regional accents and stereo audio, and reaches 101 target languages, including variants such as `English (UK)`, `Spanish (Mexico)` and `Chinese (Taiwan)`. It is a cloud API node. It needs a Comfy account with credits, downloads no model files, and bills per second of output. See [Partner node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for current rates.

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

Available workflow

### 

​

VEED Dubbing: video translation

Translate a clip you already have. The performance, the shot and the timing stay as recorded; what changes is the language the speaker is heard in. ![VEED Dubbing workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_dubbing-1.webp)

## Download Workflow

Download JSON or search “VEED Dubbing: Video Translation” in Template Library

**Input materials**

## api_veed_dubbing_input_video.mp4

Load into the `LoadVideo` node. One speaker facing the camera

The clip runs up to 599 seconds and the output is as long as its audio track, at 25 fps.

## 

​

Node controls

Control| Values| Effect  
---|---|---  
`model`| `standard`, `pro`| The dubbing tier. `standard` is mono with 85 target languages; `pro` adds regional accents and stereo audio with 101  
`video`| clip| The footage to dub. Up to 599 seconds, with a visible face and speech in the audio track  
`target_language`| language list| The language to dub into. The list depends on the tier, and `pro` carries the accent variants  
`source_language`| `auto` or a language| The language spoken in the video. `auto` is the default  
`seed`| integer| Rerun control only. Results stay non-deterministic  
  
## 

​

Tips

  * **Send footage with a visible speaker.** Dubbing works on what it can see, so a single person facing the camera is the reliable case. Backs of heads, hands, product shots and crowd scenes do not dub.
  * **Check that the audio actually has speech.** Narration, dialogue and interviews all work. Music, sound effects and silence give the model nothing to translate.
  * **Name the source language when auto mishears.** `auto` handles clean recordings, but a short clip or a strong accent dubs more accurately when you set `source_language` yourself.
  * **Pick`pro` when the accent matters.** The standard tier gives one variant per language, so requests for British English or Mexican Spanish only exist on `pro`.
  * **Cut to the length limit first.** The node accepts up to 599 seconds of video, and the output is as long as the audio track, so trim before the run rather than after.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `VEED Dubbing`
  3. Load a talking-head clip into the `LoadVideo` node
  4. Choose the tier in `model`, set `target_language`, then run the workflow



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/veed/veed-dubbing.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/veed/veed-dubbing)

[Astra 2](https://docs.comfy.org/tutorials/partner-nodes/topaz/astra-2)[Video Nodes](https://docs.comfy.org/tutorials/partner-nodes/veed/veed-video)
