---
url: https://docs.comfy.org/tutorials/audio/yue2/yue2/
title: ComfyUI YuE2 Music Generation Guide - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:05.436754+00:00
---

# ComfyUI YuE2 Music Generation Guide - ComfyUI

> Source: https://docs.comfy.org/tutorials/audio/yue2/yue2/

## On this page

  * Text to Music
    * 1\. Steps to Run
    * 2\. Model Download
    * 3\. Writing the Style
    * 4\. Writing the Lyrics
    * 5\. ABC Planning
    * 6\. Max Duration
    * 7\. Guidance Scale
  * Music Cover
    * 1\. Steps to Run
    * 2\. Model Downloads
    * 3\. How the Cover Works
    * 4\. Writing the Style and Lyrics



YuE2

# ComfyUI YuE2 Music Generation Guide

Copy pageCopy page

Generate complete songs with vocals in ComfyUI using the open-source YuE2 model: text to music with ABC planning, and melody-preserving covers with SheetSage2.

Copy pageCopy page

YuE2 is an open-source music generation model from Multimodal Art Projection (m-a-p) that turns a style prompt and lyrics into a complete song with vocals and instrumental accompaniment. A 3B-parameter model, it generates full song structures with sections such as intro, verse, chorus, bridge, and outro, and supports multiple singing languages including English, Chinese, and Japanese. What sets YuE2 apart from most text-to-music systems is its editable composition step. Before generating audio, YuE2 can first write a symbolic music plan in ABC notation: a melody, optionally with chords, that you can inspect and edit. The final song is then rendered from that plan. This makes results easier to steer than one-shot audio generation, and it also powers the cover workflow below, where a reference song is transcribed into the same notation and re-sung with new style and lyrics. YuE2 is supported natively in ComfyUI. Update to the latest version of [ComfyUI](https://github.com/comfyanonymous/ComfyUI) before starting. ComfyUI v0.35.0 or later is required, and v0.35.1 or later is recommended on AMD GPUs.

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

YuE2 is not available on Comfy Cloud yet. Both workflows on this page run in a local ComfyUI installation, so there is no Cloud template to open for them.

## 

​

Text to Music

Generate a complete song from a music style description and your own lyrics. With ABC planning enabled, YuE2 first creates an editable symbolic music plan (melody and optionally chords), then generates the final audio from that plan. ![YuE2 text to music workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_yue2_text2music-1.webp)

## Download Workflow

Download JSON or search “YuE2: Text to Music” in Template Library

### 

​

1\. Steps to Run

  1. Write a description of the music you want in **Style**
  2. Enter your song lyrics in **Lyrics** using section tags such as `[Verse]` and `[Chorus]`
  3. Choose a planning **Mode** : `full` generates melody and chords, `melody` generates the melody only
  4. Set the **Max Duration** of the song
  5. Queue the workflow to generate the song



### 

​

2\. Model Download

## YuE2 checkpoint

yue2_3b_int8_convrot.safetensors

Place the file in the following directory:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 checkpoints/
    │       └── yue2_3b_int8_convrot.safetensors
    

### 

​

3\. Writing the Style

Describe the main musical characteristics. Useful elements include:

  * **Genre** : pop, jazz, rock, electronic, folk
  * **Vocals** : warm female vocal, expressive male vocal, soft vocals
  * **Language** : English, Chinese, Japanese, and more
  * **Tempo** : 90 BPM, slow, upbeat
  * **Instruments** : piano, electric guitar, bass, drums, synths

Example:

> English, warm female vocal, contemporary pop, 96 BPM, piano, rounded electric bass, restrained drums, clear diction

Keep musical instructions in **Style** rather than in the lyrics.

### 

​

4\. Writing the Lyrics

Use section tags to describe the song structure:
    
    
    [Verse]
    Morning light across the window
    City waking down below
    
    [Chorus]
    Run with me into the sunlight
    Leave the shadows far behind
    

You can structure the song with sections such as `[Verse]`, `[Chorus]`, `[Bridge]`, and `[Outro]`. Put only the words intended to be sung in the lyrics field.

### 

​

5\. ABC Planning

The **Mode** option controls the symbolic planning step:

  * **full** : creates a plan with melody and chords before generating the song. Recommended for general text-to-music generation.
  * **melody** : creates a melody-only plan and lets the accompaniment be generated more freely.

Leaving the **abc** input empty disables planning and generates music directly from Style and Lyrics.

### 

​

6\. Max Duration

**Max Duration** sets the maximum length of the generated song in seconds, up to 900. The generation budget is 25 semantic tokens per second of requested duration, and sampling stops as soon as the model writes the song’s end token, so a song whose structure finishes early can end well before the limit. The Text to Music template sets this to 120 seconds, and Music Cover keeps the node’s 360-second default. The requested duration is capped by the model’s context. When the style, lyrics, and ABC plan claim more of the context than the run can spare, ComfyUI lowers the budget to what is left and reports it in the console: `YuE2 music budget reduced to ... tokens (... seconds) to fit the prompt.` A long prompt therefore shortens the song instead of failing the run. When nothing is left at all, the run stops with `YuE2 prompt leaves no room for music; shorten the style, lyrics, or ABC.` When the console reports a `YuE2 semantic reached its token budget before the end token.` warning, the model ran out of budget before it wrote the song’s end token, and the rendered audio can stop abruptly instead of finishing the song, because those semantic tokens are the song content the audio stage renders. Raise **Max Duration** to give the song more room. If the same run also logged a budget reduction, the prompt is already using the available context, so shorten the style, lyrics, or ABC plan instead. The notation phase reports the same warning as `YuE2 abc reached its token budget before the end token.`, where the score itself is cut short and the YuE2 Generate ABC node’s `max_abc_tokens` is the budget to raise.

### 

​

7\. Guidance Scale

The **YuE2 Generate Music** node has an advanced `cfg_scale` option (0 to 100, default 1.0) that sets autoregressive guidance on style and lyrics:

  * `1.0` disables guidance, which matches the ABC workflow. The included templates keep this default
  * `1.01` matches the guidance scale the model used before this option was added, for runs where planning is disabled (`abc` left empty)



## 

​

Music Cover

Create a new version of an existing song. This workflow uses SheetSage2 to transcribe the melody from a reference audio into an editable ABC score, then uses YuE2 to regenerate the song with a new style and lyrics. ![YuE2 music cover workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_yue2_music_cover-1.webp)

## Download Workflow

Download JSON or search “YuE2: Music Cover” in Template Library

**Input materials** Upload this file to the matching `LoadAudio` node:

## yue2_reference_song.flac

`LoadAudio` node · `yue2_reference_song.flac`

### 

​

1\. Steps to Run

  1. Load a reference song in **Audio**
  2. Describe the new musical direction in **Style**
  3. Enter the lyrics you want to sing in **Lyrics**
  4. Queue the workflow to generate a new cover version

The reference audio provides the melody, while YuE2 creates a new performance and arrangement based on your Style and Lyrics.

### 

​

2\. Model Downloads

## YuE2 checkpoint

yue2_3b_int8_convrot.safetensors

## SheetSage2 audio encoder

sheetsage2_bf16.safetensors

Place the files in the following directories:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── yue2_3b_int8_convrot.safetensors
    │   └── 📂 audio_encoders/
    │       └── sheetsage2_bf16.safetensors
    

### 

​

3\. How the Cover Works

The workflow does not feed the reference audio to YuE2 directly. Instead:
    
    
    Reference Audio
        ↓
    SheetSage2 (transcription)
        ↓
    Melody ABC score
        ↓
    YuE2 (generation with new Style and Lyrics)
    

Because the connection to the original song is the melody, covers work best when the new lyrics stay reasonably close to the original phrasing and syllable count.

### 

​

4\. Writing the Style and Lyrics

Describe the target musical style clearly. Useful elements include genre, vocal type, language, tempo, instruments, and mood:

> English, soulful jazz-pop, expressive male vocal, relaxed 88 BPM, Rhodes piano, upright bass, brushed drums, warm saxophone, intimate late-night atmosphere

Use the same `[Verse]` / `[Chorus]` / `[Bridge]` / `[Outro]` section tags as the text-to-music workflow. For better melody matching, keep the new lyrics close in length to the original lines.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/audio/yue2/yue2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/audio/yue2/yue2)

[ComfyUI SCAIL-2 Character Replacement Workflow TutorialPrevious](https://docs.comfy.org/tutorials/video/zai/scail2)[MiniMax Music 3 in ComfyUI: AI Music GenerationNext](https://docs.comfy.org/tutorials/audio/minimax/minimax-music-3)

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
