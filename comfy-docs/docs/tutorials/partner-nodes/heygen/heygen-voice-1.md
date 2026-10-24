---
url: https://docs.comfy.org/tutorials/partner-nodes/heygen/heygen-voice-1/
title: HeyGen Voice 1.0 in ComfyUI: Voice Cloning and Text to Speech - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:42.016265+00:00
---

# HeyGen Voice 1.0 in ComfyUI: Voice Cloning and Text to Speech - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/heygen/heygen-voice-1/

## On this page

  * What HeyGen Voice 1.0 is good at
  * Example output
  * Use it
  * HeyGen Voice 1.0 workflow
    * Steps to run
  * Node controls
    * HeyGen Voice 1.0 Instant Clone
    * HeyGen Voice 1.0 Text to Speech
  * Limits
  * Get started



HeyGen

# HeyGen Voice 1.0 in ComfyUI: Voice Cloning and Text to Speech

Copy pageCopy page

Clone a voice from one recording and speak any script with HeyGen Voice 1.0 in ComfyUI: the Instant Clone and Text to Speech partner nodes.

Copy pageCopy page

**HeyGen Voice 1.0** turns a short recording of one speaker into a reusable voice, then speaks any script in that voice. There is no training wait: the clone is created from the clip you connect, and the returned `voice_id` is all the text-to-speech node needs. It is built for narration in your own voice, character dialogue, and multilingual voiceover. In ComfyUI the feature runs through two partner nodes: **HeyGen Voice 1.0 Instant Clone** takes the recording and returns a `voice_id`, and **HeyGen Voice 1.0 Text to Speech** speaks written text in that voice. Both are cloud API nodes: they need a Comfy account with credits and download no local model. Cloning is free and text to speech is billed per 1K characters. See [Partner Node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the rates. The template wires the two nodes together and saves both outputs: the spoken audio, and a text file with the `voice_id` so the same voice can be reused in a later session without cloning again.

## 

​

What HeyGen Voice 1.0 is good at

  * **Clone from a short recording** : 10 seconds of clear speech is enough, and up to 3 minutes of the clip is used
  * **Reuse the voice** : the `voice_id` output plugs into text to speech, or into `custom_voice_id` on HeyGen Avatar Video and HeyGen Talking Photo
  * **Two speeds** : `heygen-voice-1-turbo` is faster and costs half as much as `heygen-voice-1`
  * **Expressiveness control** : `expressiveness_boost` stays close to the recording at low values and adds emotion at high values



## 

​

Example output

Cloning a voice from one recording, then speaking a script in that voice: ![HeyGen Voice 1.0 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_voice_1-1.webp)

## 

​

Use it

This runs on the same Comfy account and is billed in the same credits as running it in ComfyUI below. See [Partner Nodes pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for per-model rates and [Concurrency limits](https://docs.comfy.org/tutorials/partner-nodes/concurrency-limits) for how many requests you can have in flight.

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

HeyGen Voice 1.0 workflow

Clone the voice, write the script, and run. The template keeps both nodes in one graph so the `voice_id` is passed straight from the clone to the text-to-speech node.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HeyGen Voice 1.0” in Template Library

**Input material**

## long_demo.mp3

Load into the `LoadAudio` node that feeds HeyGen Voice 1.0 Instant Clone

### 

​

Steps to run

  1. **Load a recording** : connect one speaker, at least 10 seconds of clear speech, in the **LoadAudio** node. Only the first 3 minutes are used
  2. **Clone the voice** : on **HeyGen Voice 1.0 Instant Clone** , set `language` to the language spoken in the recording and pick `similarity`. Change `seed` to clone again and get a slightly different voice
  3. **Write the script** : on **HeyGen Voice 1.0 Text to Speech** , enter up to 5000 characters of plain prose in `text`, and connect the `voice_id` output of the clone node to its `voice_id` input
  4. **Set the delivery** : `expressiveness_boost` from 0 to 1. `0` stays closest to the recording, `1` adds the most emotion
  5. **Click Queue** or press `Ctrl+Enter` to generate
  6. **Save the result** : the template writes the audio with **SaveAudioAdvanced** and the voice ID with **SaveText** , under `output/HeyGen_Voice_id/`



## 

​

Node controls

### 

​

HeyGen Voice 1.0 Instant Clone

Control| Values| Effect  
---|---|---  
`audio`| one audio clip| Recording of one speaker. At least 10 seconds is recommended; only the first 3 minutes are used  
`language`| `auto` or a language| Language spoken in the recording  
`similarity`| `medium`, `high`, `extra_high`, `max` (default)| How closely the cloned voice follows the recording  
`remove_background_noise`| on by default| Cleans the recording before cloning  
`seed`| default 42| Change it to clone again; each clone is a slightly different voice  
  
### 

​

HeyGen Voice 1.0 Text to Speech

Control| Values| Effect  
---|---|---  
`model`| `heygen-voice-1`, `heygen-voice-1-turbo`| Turbo is faster and costs half as much  
`voice_id`| a cloned voice ID| Output of the Instant Clone node  
`text`| 1 to 5000 characters| The script to speak. Speech longer than about 12 minutes fails, so split very long Chinese or Japanese text  
`language`| `auto` or a language| Set it for closely related languages such as Serbian or Malay, which auto-detection can confuse  
`expressiveness_boost`| 0.0 to 1.0, default 0.5| Higher values are more expressive; lower values stay closer to the original voice  
  
## 

​

Limits

  * The clone uses the first 3 minutes of the recording, and 10 seconds of clear speech is the practical minimum.
  * Text is limited to 5000 characters, about 12 minutes of speech. Plain prose only; anything else is rejected.
  * Instant voices ignore `seed`, `speed`, and `pitch` in text to speech. `expressiveness_boost` is the only delivery control.
  * The `voice_id` must come from a clone. An empty ID fails with an error.
  * Cloning is free; text to speech bills per 1K characters at the model’s rate.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `HeyGen Voice 1.0`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/heygen/heygen-voice-1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/heygen/heygen-voice-1)

[Video To Music](https://docs.comfy.org/tutorials/partner-nodes/sonilo/video-to-music)[SFX 2.0](https://docs.comfy.org/tutorials/partner-nodes/mirelo/mirelo-sfx)
