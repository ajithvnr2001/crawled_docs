---
url: https://docs.comfy.org/built-in-nodes/ElevenLabsSpeechToSpeech/
title: ElevenLabsSpeechToSpeech - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:51.759803+00:00
---

# ElevenLabsSpeechToSpeech - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ElevenLabsSpeechToSpeech/

Elevenlabs

# ElevenLabsSpeechToSpeech - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ElevenLabs Speech to Speech node transforms an input audio file from one voice to another.

Copy pageCopy page

The ElevenLabs Speech to Speech node transforms an input audio file from one voice to another. It uses the ElevenLabs API to convert speech while preserving the original content and emotional tone of the audio.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for speech-to-speech transformation. The selected model determines the available voice settings listed below.| DYNAMIC_COMBO| Yes| `eleven_multilingual_sts_v2`  
`eleven_english_sts_v2`  
`voice`| Target voice for the transformation. Connect from Voice Selector or Instant Voice Clone.| CUSTOM| Yes| -  
`audio`| Source audio to transform.| AUDIO| Yes| -  
`stability`| Voice stability. Lower values give broader emotional range, higher values produce more consistent but potentially monotonous speech (default: 0.5).| FLOAT| Yes| 0.0 - 1.0  
`output_format`| Audio output format.| COMBO| Yes| `"mp3_44100_192"`  
`"opus_48000_192"`  
`seed`| Seed for reproducibility (default: 0).| INT| Yes| 0 - 4294967295  
`remove_background_noise`| Remove background noise from input audio using audio isolation (default: False).| BOOLEAN| Yes| -  
  
### 

​

eleven_multilingual_sts_v2 and eleven_english_sts_v2 Inputs

Both models provide the same set of voice settings below.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`speed`| Speech speed. 1.0 is normal, <1.0 slower, >1.0 faster (default: 1.0).| FLOAT| Yes| 0.7 - 1.3  
`similarity_boost`| Similarity boost. Higher values make the voice more similar to the original (default: 0.75).| FLOAT| Yes| 0.0 - 1.0  
`use_speaker_boost`| Boost similarity to the original speaker voice (default: False).| BOOLEAN| Yes| -  
`style`| Style exaggeration. Higher values increase stylistic expression but may reduce stability (default: 0.0).| FLOAT| Yes| 0.0 - 0.2  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The transformed audio file in the specified output format.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/en.md)

* * *

**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ElevenLabsSpeechToSpeech.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ElevenLabsSpeechToSpeech)

[ElevenLabsInstantVoiceClone - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ElevenLabsInstantVoiceClone)[ElevenLabsSpeechToText - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ElevenLabsSpeechToText)

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
