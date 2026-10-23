---
url: https://docs.comfy.org/tutorials/partner-nodes/mirelo/mirelo-sfx/
title: Mirelo SFX 2.0 in ComfyUI: Video to SFX and Text to SFX - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:29.569733+00:00
---

# Mirelo SFX 2.0 in ComfyUI: Video to SFX and Text to SFX - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/mirelo/mirelo-sfx/

## On this page

  * Available workflows
    * Video to SFX
    * Text to SFX
  * Node controls
  * Prompting tips
  * Get started



Mirelo

# Mirelo SFX 2.0 in ComfyUI: Video to SFX and Text to SFX

Copy pageCopy page

Generate sound effects in ComfyUI with Mirelo sfx-2.0: Foley timed to your video, or sound design from a text prompt, plus a separate speech track.

Copy pageCopy page

**Mirelo SFX 2.0** generates sound effects. It works in two directions: it watches a clip and produces Foley timed to what happens on screen, or it takes a text description of a sound and builds it from nothing. In ComfyUI the model runs through two partner nodes. **Mirelo Video to SFX** takes a clip and returns the mixed soundtrack plus the dialogue on its own output. **Mirelo Text to SFX** takes a prompt and a duration and returns one audio clip. Both are cloud API nodes: they need a Comfy account with credits and download no model files locally. Output is 48 kHz audio. A video run covers 1 to 600 seconds, and text to SFX covers 0.1 to 600 seconds. Video to SFX bills by the duration of the clip you send, and Text to SFX bills by the duration you set.

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

Video to SFX

Add sound to a finished cut. The model reads the picture and times each sound to the action in frame, so footsteps, impacts, and ambience land on the movement instead of on a guessed timeline. ![Mirelo SFX 2.0: Video to SFX workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_mirelo_video_to_sfx-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Mirelo SFX 2.0: Video to SFX” in Template Library

**Input material**

## mage_crash_discovery_video.mp4

Load into the `LoadVideo` node

The node has two audio outputs. `audio` carries the finished mix, and `speech` carries the dialogue separated from the generated effects. When the clip has no speech, the `speech` output is silent.

### 

​

Text to SFX

Build a sound from a description. The prompt and the duration are the only inputs, so this is the mode for a sound you cannot record or for filling an effects library. ![Mirelo SFX 2.0: Text to SFX workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_mirelo_text_to_sfx-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Mirelo SFX 2.0: Text to SFX” in Template Library

**Example prompts**

  * `Heavy rain on a tin roof with distant thunder`
  * `Soft footsteps on wood floor in a small quiet room`
  * `Sharp knife chop on a wooden cutting board, close mic`
  * `Metal door slam in a concrete hallway with short echo`



## 

​

Node controls

Control| Values| Applies to| Effect  
---|---|---|---  
`model`| `sfx-2.0`| both nodes| The Mirelo SFX model release  
`video`| clip, 1 to 600 seconds| Video to SFX| The cut the effects are timed to. Silent or with sound both work  
`audio`| optional track| Video to SFX| Dialogue to carry through instead of the clip’s own soundtrack. Leave unconnected when the video already holds the audio you want  
`prompt`| text, up to 2000 characters| both nodes| A short description of the sound. Required on Text to SFX, optional on Video to SFX  
`negative_prompt`| text, up to 1000 characters| both nodes| Sounds to leave out, as a comma-separated list  
`preserve_speech`| on by default| Video to SFX| Keeps the dialogue and mixes the effects under it. Turn it off for effects only  
`duration`| 0.1 to 600 seconds, default 5| Text to SFX| Length of the generated sound  
`seed`| integer| both nodes| Change it to explore variations of the same prompt  
  
## 

​

Prompting tips

  * **Name the sound, not the story.** Source, material, space, and intensity in one line: `boots on gravel, metal settling, soft cavern wind`. Concrete nouns you can hear beat abstract mood words.
  * **Start Video to SFX with an empty prompt.** The picture already carries the timing. Add one line only for off-screen sound, such as `distant church bells, a dog barking two streets away`, or to push a single layer.
  * **Use the negative prompt to strip layers.** `music, wind, crowd` removes a score from an AI-generated clip. Keep `speech` out of the negative list when you want the dialogue kept.
  * **Match the duration to the event.** A single impact does not need 30 seconds of rain.
  * **Audition a few variants.** Re-run with a different seed and change one dimension at a time: material first, then space, then intensity.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Mirelo`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/mirelo/mirelo-sfx.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/mirelo/mirelo-sfx)

[Video To Music](https://docs.comfy.org/tutorials/partner-nodes/sonilo/video-to-music)[Clean Audio](https://docs.comfy.org/tutorials/partner-nodes/veed/veed-clean-audio)
