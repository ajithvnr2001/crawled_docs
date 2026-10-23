---
url: https://docs.comfy.org/built-in-nodes/FishAudioInstantVoiceClone/
title: FishAudioInstantVoiceClone - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.131043+00:00
---

# FishAudioInstantVoiceClone - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FishAudioInstantVoiceClone/

Fish Audio

# FishAudioInstantVoiceClone - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a private cloned voice from your audio recordings using the Fish Audio API.

Copy pageCopy page

This node creates a private cloned voice from your audio recordings using the Fish Audio API. You provide one or more audio samples, and the node builds a custom voice that can be immediately used for text-to-speech. It accepts 1 to 20 recordings, with a recommended length of 10 to 30 seconds each and a total limit of 270 seconds.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`files`| Audio recordings for voice cloning. This is a growable input: connect one or more audio items (for example `audio_1`, `audio_2`, …) to provide the voice samples.| AUDIO| Yes| 1 to 20 recordings  
`enhance_audio_quality`| Enhance reference audio quality before training (default: True).| BOOLEAN| Yes| True  
False  
  
**Note:** The total duration of all reference audio combined must be under 270 seconds. If the combined duration reaches or exceeds 270 seconds, the node returns an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`voice`| The newly created cloned voice, identified by a unique voice ID returned by the Fish Audio API. This voice can be used for text-to-speech.| FISHAUDIO_VOICE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioInstantVoiceClone/en.md)

* * *

**Source fingerprint (SHA-256):** `6c4f011a4611a076b2488152591efeb61c029d6dfae2b079ba74689891c84803`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FishAudioInstantVoiceClone.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FishAudioInstantVoiceClone)

[ElevenLabsVoiceSelector - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ElevenLabsVoiceSelector)[FishAudioSpeechToText - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FishAudioSpeechToText)

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
