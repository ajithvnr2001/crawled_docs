---
url: https://docs.comfy.org/built-in-nodes/FishAudioVoiceSelector/
title: FishAudioVoiceSelector - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.621245+00:00
---

# FishAudioVoiceSelector - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FishAudioVoiceSelector/

Fish Audio

# FishAudioVoiceSelector - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Fish Audio Voice Selector node selects a voice from the Fish Audio library for text-to-speech generation.

Copy pageCopy page

The Fish Audio Voice Selector node selects a voice from the Fish Audio library for text-to-speech generation. You can pick one of the built-in preset voices, or choose “custom” to enter any voice model ID from fish.audio.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voice`| Choose a voice, or ‘custom’ to enter any fish.audio voice model ID.| DYNAMIC_COMBO| Yes| ”Energetic Male (en)"  
"Friendly Women (en)"  
"Sarah (en)"  
"Verity (en)"  
"Polo (en)"  
"Adrian (en)"  
"E-girl (en)"  
"Narrator (en)"  
"Warm Conversational Voice (en)"  
"Warm Storyteller (en)"  
"Dramatic Character Male (en)"  
"News Narrator (zh)"  
"Lively Female (zh)"  
"Gentle Female (zh)"  
"Energetic Female (ja)"  
"Calm Female (ja)"  
"Calm Male (ja)"  
"custom”  
  
The preset voice options cover English (en), Chinese (zh), and Japanese (ja) voices and do not require any additional inputs.

### 

​

Custom Inputs

These inputs appear when `voice` is set to “custom”.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voice_id`| Voice model ID from fish.audio, e.g. the ID in [https://fish.audio/m/&lt;id>/](https://fish.audio/m/&lt;id%3E/). Default: empty string.| STRING| Yes| Any valid Fish Audio voice model ID  
  
Note: When `voice` is set to “custom”, `voice_id` must not be empty after whitespace is trimmed; otherwise the node raises a “Custom voice ID is empty.” error. If an unrecognized voice option is passed, the node raises an “Unknown voice” error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`voice`| The selected Fish Audio voice model ID. For a preset voice, the corresponding voice ID from the Fish Audio library is returned; for “custom”, the entered `voice_id` value is returned.| FISHAUDIO_VOICE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/en.md)

* * *

**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FishAudioVoiceSelector.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FishAudioVoiceSelector)

[FishAudioTextToSpeech - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FishAudioTextToSpeech)[HeyGenTextToSpeechNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HeyGenTextToSpeechNode)

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
