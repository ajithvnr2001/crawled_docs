---
url: https://docs.comfy.org/built-in-nodes/BreezeTextToSpeech/
title: Breeze Text to Speech - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:53.541753+00:00
---

# Breeze Text to Speech - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BreezeTextToSpeech/

Audio

# Breeze Text to Speech - ComfyUI Built-in Node Documentation

Copy pageCopy page

Converts text into speech with Breeze TTS 2.

Copy pageCopy page

Converts text into speech with Breeze TTS 2. Pick a Breeze voice, choose the language of the text, and optionally direct how the line is performed. English and Chinese can use either Breeze TTS 2 model; every other language uses Breeze TTS 2 Multilingual.

## Inputs

### Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voice`| Breeze voice to speak with, from Breeze Voice Selector or one of the Breeze voice creation nodes.| BREEZE_VOICE| Yes| -  
`text`| Text to speak, 1 to 1000 characters. Audio tags such as `(laughs)` or `(sighs)` are performed instead of read. Default: empty.| STRING| Yes| 1 to 1000 characters  
`language`| Language of the text. English and Chinese can use either model; other languages use Breeze TTS 2 Multilingual. A voice sounds best in its own language, so for another language use a copy made with Breeze Voice Localize.| DYNAMIC_COMBO| Yes| Multiple options available  
`delivery`| How the line is performed: `neutral` keeps the voice as it is, `directed` follows written instructions. Default: `"neutral"`.| DYNAMIC_COMBO| Yes| `"neutral"`  
`"directed"`  
`speed`| Tempo multiplier that leaves the pitch unchanged. Default: 1.0.| FLOAT| No| 0.5 to 2.0 (step 0.05)  
`seed`| Controls whether the node re-runs; results are non-deterministic regardless of the seed. Default: 42.| INT| No| 0 to 2147483647  
  
### Language “English” and “Chinese” Inputs

These appear only when `language` is English or Chinese.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| `Breeze TTS 2` or `Breeze TTS 2 Multilingual`. Default: `"Breeze TTS 2"`.| COMBO| Yes| `"Breeze TTS 2"`  
`"Breeze TTS 2 Multilingual"`  
  
### Delivery “neutral” Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`speaker_boost`| Keeps the voice closer to its original sound. Default: false.| BOOLEAN| No| true  
false  
  
### Delivery “directed” Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`instructions`| How to perform the text, written in the same language as the text. Default: empty.| STRING| No| Multiline text  
`strength`| How strongly the voice follows the instructions. Default: 4.0.| FLOAT| No| 1.0 to 10.0 (step 0.1)  
  
## Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The generated speech as WAV audio.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeTextToSpeech/en.md)

* * *

**Source fingerprint (SHA-256):** `e5e5201e8c951a878ef9e764db31e494285ddded6ec66d8e818ec132342bbe5c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BreezeTextToSpeech.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BreezeTextToSpeech)

[Sonilo Video to Music](https://docs.comfy.org/built-in-nodes/SoniloVideoToMusic)[Breeze Voice Clone](https://docs.comfy.org/built-in-nodes/BreezeVoiceClone)
