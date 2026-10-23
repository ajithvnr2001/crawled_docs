---
url: https://docs.comfy.org/tutorials/partner-nodes/veed/veed-clean-audio/
title: VEED Clean Audio: Speech Cleanup for Audio and Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:30.827027+00:00
---

# VEED Clean Audio: Speech Cleanup for Audio and Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/veed/veed-clean-audio/

## On this page

  * Available workflows
    * Clean Audio
    * Clean Audio (in Video)
  * Node controls
  * Tips
  * Get started



VEED

# VEED Clean Audio: Speech Cleanup for Audio and Video

Copy pageCopy page

Remove background noise from speech with VEED Clean Audio in ComfyUI, on a recording or a video soundtrack, with optional loudness normalization.

Copy pageCopy page

**VEED Clean Audio** isolates the voice in a recording. It strips background noise, and because it is built for speech, music and sound effects go with the noise: what comes back is the dialogue on its own, cleaned and ready to use. In ComfyUI the model runs through two partner nodes. **VEED Clean Audio** takes a standalone recording and returns cleaned audio. **VEED Clean Audio (in Video)** takes a clip, cleans only its soundtrack, and returns the video with the picture untouched. Both are cloud API nodes: they need a Comfy account with credits and download no model files locally. The two nodes return different things. **Clean Audio** returns 48 kHz mono audio. **Clean Audio (in Video)** returns the video itself, with the picture untouched and its soundtrack replaced by that cleaned 48 kHz mono speech. Both accept runs up to 1799 seconds, just under 30 minutes. For lip sync, talking portraits, and background removal, see [VEED Video Nodes](https://docs.comfy.org/tutorials/partner-nodes/veed/veed-video).

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

Clean Audio

Clean a voice recording before it goes anywhere else. The node is the first step of a voice pipeline: send the cleaned speech to a lip sync node, a transcription step, or a mix, and the noise floor of the original never reaches them. ![VEED Clean Audio: Speech Cleanup workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_clean_audio-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “VEED Clean Audio: Speech Cleanup” in Template Library

**Input material**

## veed_clean_audio_noisy_input.wav

Load into the `LoadAudio` node

### 

​

Clean Audio (in Video)

Clean the speech inside a clip without touching the picture. Only the soundtrack is replaced, with the cleaned 48 kHz mono speech, so the result is the same edit with a usable voice track. ![VEED Clean Audio: Video Speech Cleanup workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_clean_audio_video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “VEED Clean Audio: Video Speech Cleanup” in Template Library

**Input material**

## veed_clean_audio_input_h3_omniref_person_dialogue_plus_noise.mp4

Load into the `LoadVideo` node. The clip needs an audio track

A clip with no audio track stops with an error instead of returning a silent video. Only the first audio track is kept: extra audio tracks and embedded subtitles are dropped, so export those first when the clip carries more than one.

## 

​

Node controls

Control| Values| Applies to| Effect  
---|---|---|---  
`audio`| recording, up to 1799 seconds| Clean Audio| The speech to clean  
`video`| clip with audio, up to 1799 seconds| Clean Audio (in Video)| The clip whose soundtrack is cleaned. The picture is not re-encoded by the clean step  
`strength`| 0.0 to 1.0, default 0.874| both nodes| How much noise is removed under the speech. Lower keeps more room tone behind the voice  
`loudness`| `normalize`, `keep input level`| both nodes| Whether the output is normalized to a target loudness  
`target_lufs`| -40 to -8, default -19| both nodes, `normalize` only| Integrated loudness of the output  
  
Pauses between words are always cleaned completely, whatever `strength` is set to, and values above the default change little. Peaks are capped at -1.1 dBTP, so a loud target stops early: typical speech settles near -15 LUFS.

## 

​

Tips

  * **Leave`strength` at the default first.** It is tuned for speech. Lower it only when the room tone behind the voice is part of the sound you want to keep.
  * **Normalize when the cleaned audio has to match other clips.** A shared `target_lufs` is what makes a series of recordings sit at the same level.
  * **Do not expect music back.** Music and effects are removed along with the noise, so this node cleans dialogue, not a full mix. Run it on the voice stem when a soundtrack has to survive.
  * **Cut long recordings before the run.** The cap is 1799 seconds, and a shorter file is cheaper at the per-minute rate.
  * **Chain it into the talking nodes.** Cleaned speech makes a better input for lip sync and talking portraits than the raw recording.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `VEED`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/veed/veed-clean-audio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/veed/veed-clean-audio)

[SFX 2.0](https://docs.comfy.org/tutorials/partner-nodes/mirelo/mirelo-sfx)[Overview](https://docs.comfy.org/tutorials/partner-nodes/language/overview)
