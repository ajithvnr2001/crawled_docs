---
url: https://docs.comfy.org/built-in-nodes/BreezeVoiceClone/
title: Breeze Voice Clone - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:53.404450+00:00
---

# Breeze Voice Clone - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BreezeVoiceClone/

Audio

# Breeze Voice Clone - ComfyUI Built-in Node Documentation

Copy pageCopy page

Creates a Breeze voice from a recording of one speaker.

Copy pageCopy page

Creates a Breeze voice from a recording of one speaker. The voice is saved to your account and returned as a voice handle, together with an audio preview of how it sounds.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| Recording of one speaker, at least 3 seconds long. Only the first 60 seconds are used.| AUDIO| Yes| -  
`remove_background_noise`| Cleans the recording up before cloning. Default: false.| BOOLEAN| No| true  
false  
`seed`| Controls whether the node re-runs; results are non-deterministic regardless of the seed. Default: 42.| INT| No| 0 to 2147483647  
  
## Outputs

Output Name| Description| Data Type  
---|---|---  
`voice`| The new Breeze voice, for Breeze Text to Speech.| BREEZE_VOICE  
`preview`| Audio preview of the cloned voice.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceClone/en.md)

* * *

**Source fingerprint (SHA-256):** `3c2e461a8e1a38bfa494a687f5b77a375e9e81c77964493181d7c622a682c56f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BreezeVoiceClone.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BreezeVoiceClone)

[Breeze Text to Speech](https://docs.comfy.org/built-in-nodes/BreezeTextToSpeech)[Breeze Voice Design](https://docs.comfy.org/built-in-nodes/BreezeVoiceDesign)
