---
url: https://docs.comfy.org/built-in-nodes/ElevenLabsInstantVoiceClone/
title: ElevenLabsInstantVoiceClone - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:51.501841+00:00
---

# ElevenLabsInstantVoiceClone - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ElevenLabsInstantVoiceClone/

Elevenlabs

# ElevenLabsInstantVoiceClone - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ElevenLabs Instant Voice Clone node creates a new, unique voice model by analyzing 1 to 8 audio recordings of a person’s voice.

Copy pageCopy page

The ElevenLabs Instant Voice Clone node creates a new, unique voice model by analyzing 1 to 8 audio recordings of a person’s voice. It sends these samples to the ElevenLabs API, which processes them to generate a voice clone that can be used for text-to-speech synthesis.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio_*`| Audio recordings for voice cloning. You must provide between 1 and 8 audio files.| AUDIO| Yes| 1 to 8 files  
`remove_background_noise`| Remove background noise from voice samples using audio isolation. (default: False)| BOOLEAN| No| True / False  
  
**Note:** You must provide at least one audio file, and you can provide up to eight. The node will automatically create input slots for the audio files you add.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`voice`| The unique identifier for the newly created cloned voice model. This output can be connected to other ElevenLabs text-to-speech nodes.| ELEVENLABS_VOICE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/en.md)

* * *

**Source fingerprint (SHA-256):** `5b109dfff8cdbc51d9e2684b9508b0998aaa014459b973acf29c204835a8db95`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ElevenLabsInstantVoiceClone.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ElevenLabsInstantVoiceClone)

[ElevenLabsAudioIsolation - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ElevenLabsAudioIsolation)[ElevenLabsSpeechToSpeech - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ElevenLabsSpeechToSpeech)

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
