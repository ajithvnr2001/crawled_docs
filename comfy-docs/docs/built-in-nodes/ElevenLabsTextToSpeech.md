---
url: https://docs.comfy.org/built-in-nodes/ElevenLabsTextToSpeech/
title: ElevenLabsTextToSpeech - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:51.997017+00:00
---

# ElevenLabsTextToSpeech - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ElevenLabsTextToSpeech/

Elevenlabs

# ElevenLabsTextToSpeech - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ElevenLabs Text to Speech node converts written text into spoken audio using the ElevenLabs API.

Copy pageCopy page

The ElevenLabs Text to Speech node converts written text into spoken audio using the ElevenLabs API. It allows you to select a specific voice and fine-tune various speech characteristics like stability, speed, and style to generate a customized audio output. The text must contain at least one character.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for text-to-speech. Selecting a model reveals its specific parameters.| DYNAMIC_COMBO| No| `"eleven_v4"`  
`"eleven_v4_turbo"`  
`"eleven_multilingual_v2"`  
`"eleven_v3"`  
`voice`| Voice to use for speech synthesis. Connect from Voice Selector or Instant Voice Clone.| CUSTOM| Yes| N/A  
`text`| The text to convert to speech. Must contain at least one character.| STRING| Yes| N/A  
`stability`| Voice stability. Lower values give broader emotional range, higher values produce more consistent but potentially monotonous speech (default: 0.5).| FLOAT| No| 0.0 - 1.0  
`apply_text_normalization`| Text normalization mode. ‘auto’ lets the system decide, ‘on’ always applies normalization, ‘off’ skips it.| COMBO| No| `"auto"`  
`"on"`  
`"off"`  
`language_code`| ISO 639-1 language code (e.g., ‘en’, ‘es’, ‘ja’). Leave empty for automatic detection (default: "").| STRING| No| N/A  
`seed`| Seed for reproducibility (determinism not guaranteed) (default: 1).| INT| No| 0 - 2147483647  
`output_format`| Audio output format.| COMBO| No| `"mp3_44100_192"`  
`"opus_48000_192"`  
  
### 

​

eleven_multilingual_v2 Inputs

These parameters become available when `model` is set to `"eleven_multilingual_v2"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`speed`| Speech speed. 1.0 is normal, <1.0 slower, >1.0 faster (default: 1.0).| FLOAT| No| 0.7 - 1.2  
`similarity_boost`| Similarity boost. Higher values make the voice more similar to the original (default: 0.75).| FLOAT| No| 0.0 - 1.0  
`use_speaker_boost`| Boost similarity to the original speaker voice (default: False).| BOOLEAN| No| True / False  
`style`| Style exaggeration. Higher values increase stylistic expression but may reduce stability (default: 0.0).| FLOAT| No| 0.0 - 0.2  
  
### 

​

eleven_v3 Inputs

These parameters become available when `model` is set to `"eleven_v3"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`speed`| Speech speed. 1.0 is normal, <1.0 slower, >1.0 faster (default: 1.0).| FLOAT| No| 0.7 - 1.3  
`similarity_boost`| Similarity boost. Higher values make the voice more similar to the original (default: 0.75).| FLOAT| No| 0.0 - 1.0  
  
### 

​

eleven_v4 and eleven_v4_turbo Inputs

These parameters become available when `model` is set to `"eleven_v4"` or `"eleven_v4_turbo"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`similarity_boost`| Similarity boost. Higher values make the voice more similar to the original (default: 0.75).| FLOAT| No| 0.0 - 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The generated audio from the text-to-speech conversion.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/en.md)

* * *

**Source fingerprint (SHA-256):** `2f8aadca9f4fee9614ce4488aa206119ecf714518b7c0c340b1bfa766f59672e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ElevenLabsTextToSpeech.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ElevenLabsTextToSpeech)

[ElevenLabsTextToSoundEffects - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ElevenLabsTextToSoundEffects)[ElevenLabsVoiceSelector - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ElevenLabsVoiceSelector)

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
