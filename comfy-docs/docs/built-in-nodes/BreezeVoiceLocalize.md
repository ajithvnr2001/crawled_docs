---
url: https://docs.comfy.org/built-in-nodes/BreezeVoiceLocalize/
title: Breeze Voice Localize - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:53.353865+00:00
---

# Breeze Voice Localize - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BreezeVoiceLocalize/

Audio

# Breeze Voice Localize - ComfyUI Built-in Node Documentation

Copy pageCopy page

Creates a copy of a voice that speaks another language natively, instead of reading a foreign language with its original accent.

Copy pageCopy page

Creates a copy of a voice that speaks another language natively, instead of reading a foreign language with its original accent. The copy is saved to your account and returned with an audio preview.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voice`| Breeze voice to copy.| BREEZE_VOICE| Yes| -  
`language`| Language the new voice speaks. Default: `"English"`.| COMBO| Yes| Multiple options available  
`seed`| Controls whether the node re-runs; results are non-deterministic regardless of the seed. Default: 42.| INT| No| 0 to 2147483647  
  
## Outputs

Output Name| Description| Data Type  
---|---|---  
`voice`| The localized copy of the voice, named after the original voice and the language.| BREEZE_VOICE  
`preview`| Audio preview of the localized voice.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceLocalize/en.md)

* * *

**Source fingerprint (SHA-256):** `a997fbc3426669f6e5725c455f49f3e16d5e14806ea3fac26657459f63e99db1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BreezeVoiceLocalize.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BreezeVoiceLocalize)

[Breeze Voice Design](https://docs.comfy.org/built-in-nodes/BreezeVoiceDesign)[Breeze Voice Remix](https://docs.comfy.org/built-in-nodes/BreezeVoiceRemix)
