---
url: https://docs.comfy.org/built-in-nodes/FishAudioSpeechToText/
title: FishAudioSpeechToText - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.237761+00:00
---

# FishAudioSpeechToText - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FishAudioSpeechToText/

Fish Audio

# FishAudioSpeechToText - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node transcribes audio into text using the Fish Audio speech-to-text service.

Copy pageCopy page

This node transcribes audio into text using the Fish Audio speech-to-text service. It automatically detects the language of the audio and can optionally return word-level timestamped segments as JSON.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| Audio to transcribe.| AUDIO| Yes| —  
`language`| ISO 639-1 language hint (e.g. ‘en’, ‘zh’). The language is auto-detected regardless. Default: "" (empty string).| STRING| No| Any ISO 639-1 language code, e.g. `en`, `zh`; empty string for auto-detection  
`precise_timestamps`| Return word-level timestamped segments. Default: false.| BOOLEAN| No| true or false  
  
Note: The `language` parameter is only a hint — the language is always auto-detected from the audio. When `precise_timestamps` is false (the default), word-level timestamps are not returned; when true, the output segments include word-level timestamps.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`text`| The transcribed text.| STRING  
`language_code`| The ISO 639-1 language code detected for the audio.| STRING  
`segments_json`| JSON string containing the transcription segments. Includes word-level timestamps when `precise_timestamps` is enabled.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioSpeechToText/en.md)

* * *

**Source fingerprint (SHA-256):** `eaf1c9a9d2b90ec962a408615cc417b552864354c3f272144b8e239b23961920`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FishAudioSpeechToText.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FishAudioSpeechToText)

[FishAudioInstantVoiceClone - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FishAudioInstantVoiceClone)[FishAudioTextToSpeech - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FishAudioTextToSpeech)

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
