---
url: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seed-audio-1-0/
title: ByteDance Seed Audio 1.0 - Universal Audio Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:27.041196+00:00
---

# ByteDance Seed Audio 1.0 - Universal Audio Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seed-audio-1-0/

## On this page

  * What Seed Audio 1.0 is good at
  * Available workflows
    * Seed Audio 1.0: Text to Audio
    * Seed Audio 1.0: Text + Audio to Audio
    * Seed Audio 1.0: Text + Image to Audio
  * How to use Seed Audio 1.0 in ComfyUI
    * Choosing a reference mode
    * Prompt structure
    * Parameter tuning
    * Edge cases and limitations
  * Get started



ByteDance

# ByteDance Seed Audio 1.0 - Universal Audio Generation

Copy pageCopy page

Generate speech, music, sound effects, and multi-speaker dialogue from one prompt with voice cloning and preset voices using Seed Audio 1.0 in ComfyUI

Copy pageCopy page

Seed Audio 1.0 is ByteDance’s universal audio generation model, now available as a built-in node in ComfyUI. Unlike traditional text-to-speech systems that only read words aloud, Seed Audio understands the full spectrum of sound. It can generate speech, music, sound effects, ambient atmospheres, and multi-speaker dialogue from a single text prompt.

## 

​

What Seed Audio 1.0 is good at

  * **Multi-modal audio generation** : Speech, music, sound effects, and ambient audio from one prompt. Describe what you hear, and Seed Audio produces it
  * **Voice cloning** : Clone voices from up to 3 reference clips (tagged `@Audio1`, `@Audio2`, `@Audio3` in the prompt) for multi-character dialogue or consistent narration
  * **Preset voices** : Pick from built-in TTS 2.0 voices when you need reliable, high-quality narration without a reference clip
  * **Image-driven voice** : Derive a voice from a character image, matching the tone and style to the visual subject
  * **Fine-grained control** : Adjust speech rate, pitch, loudness, and sample rate independently for each generation
  * **Multi-speaker dialogue** : Name characters inline in the prompt and Seed Audio handles voice assignment, turn-taking, and emotional delivery
  * **Up to 2 minutes per run** : Generate extended audio clips suitable for narration, podcast clips, video dubbing, and sound design

With these capabilities, Seed Audio 1.0 fits a wide range of use cases including video voiceovers, multi-character audio dramas, product demos, e-learning narration, game audio prototyping, and accessibility content.

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

Seed Audio 1.0: Text to Audio

Input a text prompt to generate speech, dialogue, background music, and sound effects in one audio file. ![Seed Audio 1.0: Text to Audio workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_t2a-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Seed Audio 1.0: Text to Audio” in Template Library

### 

​

Seed Audio 1.0: Text + Audio to Audio

Upload a reference audio clip and write a text prompt to clone the voice into a new scene. ![Seed Audio 1.0: Text + Audio to Audio workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_ta2a-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Seed Audio 1.0: Text + Audio to Audio” in Template Library

**Input materials** Upload this file to the matching `LoadAudio` node:

## seed_audio_ref_audio1.mp3

`LoadAudio` node 8 · `seed_audio_ref_audio1.mp3`

### 

​

Seed Audio 1.0: Text + Image to Audio

Upload a character image and write a text prompt to generate audio with a voice style matching the visual subject. ![Seed Audio 1.0: Text + Image to Audio workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_ti2a-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Seed Audio 1.0: Text + Image to Audio” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## girl_and_fish.png

`LoadImage` node 6 · `girl_and_fish.png`

![girl_and_fish.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/girl_and_fish.png)

## 

​

How to use Seed Audio 1.0 in ComfyUI

Seed Audio 1.0 ships as the **ByteDanceSeedAudio** built-in node. You can find it in the node menu under ByteDance.

### 

​

Choosing a reference mode

The node offers four reference modes that determine how the generated voice is conditioned:

Mode| Description| When to use  
---|---|---  
**Text only**|  Describe everything (voice style, emotion, ambience, and dialogue) in the prompt| Quick generation with no reference material  
**Audio reference**|  Connect up to 3 reference audio clips (30s max each) and tag them as `@Audio1`, `@Audio2`, `@Audio3` in the prompt| Cloning specific voices or creating multi-character dialogue  
**Image reference**|  Connect one character image; the model derives a voice from it| Deriving a voice from a visual character design  
**Preset voice**|  Select a built-in TTS 2.0 voice from the dropdown| Reliable narration without cloning  
  
### 

​

Prompt structure

For best results, structure your prompt to describe the audio scene:

  * **Voice and emotion** : Describe the tone, age, gender, accent, or emotional delivery
  * **Ambience and background** : Describe the acoustic environment (quiet studio, busy street, concert hall)
  * **Sound effects** : Describe specific sounds at the right moment in the timeline
  * **Dialogue lines** : Write the lines to speak, naming characters for multi-speaker scenes

**Example: narration with ambience**

> A calm, warm male voice speaks confidently. Soft rain falls in the background, with occasional distant thunder. “Seed Audio 1.0 generates natural speech with full control over pacing, pitch, and presence.”

**Example: multi-speaker dialogue with audio references**

> @Audio1 says nervously in a low, fast whisper: “Did you see that?” @Audio2 replies in a calm, slow drawl: “See what? It’s just the wind.” Light wind ambience throughout.

### 

​

Parameter tuning

After connecting your inputs, tune these parameters for the desired output:

  * **Speech rate** : Default 0 (normal). Range -50 (0.5x) to 100 (2.0x). Use negative values for relaxed narration, positive for energetic voiceovers
  * **Pitch** : Shift in semitones (-12 to +12). Useful for character voices or matching a specific vocal range
  * **Loudness** : Default 0 (normal). Range -50 (0.5x) to 100 (2.0x). Adjust for consistent volume across different source materials
  * **Sample rate** : Choose from 8kHz to 48kHz. 24kHz is a good default for speech; 44.1kHz or 48kHz for music
  * **Seed** : Controls whether the node reruns; results are non-deterministic regardless of seed value



### 

​

Edge cases and limitations

  * **Reference clip duration** : Audio reference clips are limited to 30 seconds each. For longer reference material, trim or edit the clip before connecting
  * **Audio reference ordering** : Reference inputs must be connected sequentially (1, 2, 3) without gaps
  * **Tag limit** : A maximum of 3 `@AudioN` tags are supported in a single prompt
  * **Character limit** : Prompts are limited to 3000 characters
  * **Duration limit** : Maximum 2 minutes of audio per run



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Add the **ByteDanceSeedAudio** node from the node menu, or open one of the workflow templates above
  3. Choose your reference mode and connect inputs
  4. Write your prompt describing the audio scene and dialogue
  5. Run the workflow



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bytedance/seed-audio-1-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bytedance/seed-audio-1-0)

[Fish Audio Prompt Guide: writing prompts for Fish Audio TTS in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/fishaudio/prompt-guide)[Sonilo in ComfyUI: Video to Music and Text to Audio GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/sonilo/video-to-music)

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
