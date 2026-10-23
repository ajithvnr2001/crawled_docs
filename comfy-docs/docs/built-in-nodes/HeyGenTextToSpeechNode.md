---
url: https://docs.comfy.org/built-in-nodes/HeyGenTextToSpeechNode/
title: HeyGenTextToSpeechNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:03.692166+00:00
---

# HeyGenTextToSpeechNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HeyGenTextToSpeechNode/

Heygen

# HeyGenTextToSpeechNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Synthesize speech audio from text using HeyGen’s Starfish TTS engine.

Copy pageCopy page

Synthesize speech audio from text using HeyGen’s Starfish TTS engine. This node includes HeyGen’s most popular voices across 17 languages.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`text`| Text to synthesize (up to 5000 characters). The generated speech must be at least 1 second long.| STRING| Yes| 1 to 5000 characters  
`voice`| Voice to use (curated from HeyGen’s most popular Starfish-compatible voices).| STRING| Yes| Multiple options available  
`custom_voice_id`| Optional HeyGen voice ID. When set, overrides the voice selected above. The voice must support the Starfish engine (default: empty).| STRING| No| Any valid HeyGen voice ID  
`speed`| Speech speed multiplier (default: 1.0).| FLOAT| No| 0.5 to 2.0 (step: 0.05)  
`ssml`| Treat the text as SSML markup (for pauses, emphasis, and pronunciation control) (default: False).| BOOLEAN| No| True / False  
`seed`| Not sent to HeyGen; change it to force a re-run (default: 42).| INT| No| 0 to 2147483647  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`AUDIO`| The synthesized speech audio generated from the input text.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTextToSpeechNode/en.md)

* * *

**Source fingerprint (SHA-256):** `82300626657db8ab16e96ae96b7dfe3291b77bf75efec35971dc772e5123cce7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HeyGenTextToSpeechNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HeyGenTextToSpeechNode)

[FishAudioVoiceSelector - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FishAudioVoiceSelector)[SoniloTextToMusic - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SoniloTextToMusic)

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
