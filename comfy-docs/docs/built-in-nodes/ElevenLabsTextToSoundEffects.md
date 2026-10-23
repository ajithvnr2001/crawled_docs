---
url: https://docs.comfy.org/built-in-nodes/ElevenLabsTextToSoundEffects/
title: ElevenLabsTextToSoundEffects - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:51.673238+00:00
---

# ElevenLabsTextToSoundEffects - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ElevenLabsTextToSoundEffects/

Elevenlabs

# ElevenLabsTextToSoundEffects - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ElevenLabs Text to Sound Effects node generates audio sound effects from a text description.

Copy pageCopy page

The ElevenLabs Text to Sound Effects node generates audio sound effects from a text description. It uses the ElevenLabs API to create sound effects based on your prompt, allowing you to control the duration, looping behavior, and how closely the sound follows the text.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for sound effect generation. Only one model is currently available: `eleven_sfx_v2`.| DYNAMIC_COMBO| Yes| `"eleven_sfx_v2"`  
`text`| Text description of the sound effect to generate. (default: empty)| STRING| Yes| N/A  
`output_format`| Audio output format.| COMBO| Yes| `"mp3_44100_192"`  
`"opus_48000_192"`  
  
### 

​

eleven_sfx_v2 Inputs

These parameters are shown when the `eleven_sfx_v2` model is selected.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`duration`| Duration of generated sound in seconds. (default: 5.0)| FLOAT| Yes| 0.5 to 30.0  
`loop`| Create a smoothly looping sound effect. (default: False)| BOOLEAN| No| True  
False  
`prompt_influence`| How closely generation follows the prompt. Higher values make the sound follow the text more closely. (default: 0.3)| FLOAT| Yes| 0.0 to 1.0  
  
**Note:** The `text` parameter must not be empty; it is validated before the sound generation request is sent.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The generated sound effect audio file.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/en.md)

* * *

**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ElevenLabsTextToSoundEffects.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ElevenLabsTextToSoundEffects)

[ElevenLabsTextToDialogue - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ElevenLabsTextToDialogue)[ElevenLabsTextToSpeech - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ElevenLabsTextToSpeech)

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
