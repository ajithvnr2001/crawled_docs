---
url: https://docs.comfy.org/built-in-nodes/BreezeVoiceSelector/
title: Breeze Voice Selector - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:53.301205+00:00
---

# Breeze Voice Selector - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BreezeVoiceSelector/

Audio

# Breeze Voice Selector - ComfyUI Built-in Node Documentation

Copy pageCopy page

Picks a featured Breeze voice, or any Breeze voice id, and passes it to Breeze Text to Speech.

Copy pageCopy page

Picks a featured Breeze voice, or any Breeze voice id, and passes it to Breeze Text to Speech. The node only resolves an id and makes no API call.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`language`| Language group of the featured voices, or `custom` to enter an id. Default: `"English"`.| DYNAMIC_COMBO| Yes| `"English"`  
`"Chinese"`  
`"Japanese"`  
`"custom"`  
  
### Language “English”, “Chinese” and “Japanese” Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voice`| Featured voice in that language.| COMBO| Yes| Multiple options available  
  
### Language “custom” Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voice_id`| Any Breeze voice id, such as a voice created by the other Breeze nodes. Letters, digits, `_` and `-` only. Default: empty.| STRING| Yes| Breeze voice id  
  
## Outputs

Output Name| Description| Data Type  
---|---|---  
`voice`| The selected Breeze voice.| BREEZE_VOICE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceSelector/en.md)

* * *

**Source fingerprint (SHA-256):** `0bded8f1b6ec92abaec514ed843b3c138d804e3736758f5df3a2faf52e89a8b0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BreezeVoiceSelector.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BreezeVoiceSelector)

[Breeze Voice Remix](https://docs.comfy.org/built-in-nodes/BreezeVoiceRemix)[HeyGen Voice 1.0 Instant Clone](https://docs.comfy.org/built-in-nodes/HeyGenVoiceCloneNode)
