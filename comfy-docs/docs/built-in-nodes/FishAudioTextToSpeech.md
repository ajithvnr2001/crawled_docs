---
url: https://docs.comfy.org/built-in-nodes/FishAudioTextToSpeech/
title: FishAudioTextToSpeech - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.339838+00:00
---

# FishAudioTextToSpeech - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FishAudioTextToSpeech/

Fish Audio

# FishAudioTextToSpeech - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts written text into spoken audio using Fish Audio text-to-speech models.

Copy pageCopy page

This node converts written text into spoken audio using Fish Audio text-to-speech models. It supports cues embedded in the text: [happy] and [whispering] on s2.1-pro, (happy) on s1, and plain-language [directions] plus `<whisper>...</whisper>` word tags on drama-3. Multi-speaker dialogue uses @Voice1/@Voice2 tags when multiple voices are connected. Three models are available: drama-3 and s2.1-pro, which both support up to five voices and multi-speaker dialogue, and s1, which uses a single optional voice.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`text`| The text to convert to speech. With two or more voices connected, mark speaker changes with @Voice1, @Voice2, etc. (default: empty)| STRING| Yes| Any non-empty text  
`model`| Model to use for text-to-speech.| DYNAMIC_COMBO| Yes| ”drama-3"  
"s2.1-pro"  
"s1”  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 42)| INT| Yes| 0 to 2147483647  
  
### 

​

drama-3 and s2.1-pro Inputs

These inputs appear when the `drama-3` or `s2.1-pro` model is selected. The parameter sets are identical.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voices`| Growable slot: connect 0 to 5 voice items (`voice_1`, `voice_2`, …). Voices for synthesis. Leave empty for a random voice. With two or more voices, mark speaker changes in the text with @Voice1, @Voice2, etc.| FISHAUDIO_VOICE| No| 0 to 5 voices  
`temperature`| Expressiveness. Higher values are more varied, lower values are more consistent. (default: 0.7)| FLOAT| Yes| 0.0 to 1.0  
`top_p`| Diversity via nucleus sampling. (default: 0.7)| FLOAT| Yes| 0.01 to 1.0  
`speed`| Speaking rate. 1.0 is normal, <1.0 slower, >1.0 faster. (default: 1.0)| FLOAT| Yes| 0.5 to 2.0  
`volume`| Volume adjustment in decibels. 0 is no change. (default: 0.0)| FLOAT| Yes| -10.0 to 10.0  
`normalize`| Normalize numbers and text for English and Chinese, improving stability for numbers and dates. (default: true)| BOOLEAN| Yes| true / false  
  
### 

​

s1 Inputs

These inputs appear when the s1 model is selected.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voice`| Voice for synthesis. Leave unconnected for a random voice.| FISHAUDIO_VOICE| No| Optional single voice  
`temperature`| Expressiveness. Higher values are more varied, lower values are more consistent. (default: 0.7)| FLOAT| Yes| 0.0 to 1.0  
`top_p`| Diversity via nucleus sampling. (default: 0.7)| FLOAT| Yes| 0.01 to 1.0  
`speed`| Speaking rate. 1.0 is normal, <1.0 slower, >1.0 faster. (default: 1.0)| FLOAT| Yes| 0.5 to 2.0  
`volume`| Volume adjustment in decibels. 0 is no change. (default: 0.0)| FLOAT| Yes| -10.0 to 10.0  
`normalize`| Normalize numbers and text for English and Chinese, improving stability for numbers and dates. (default: true)| BOOLEAN| Yes| true / false  
  
**Note:** The `text` input must not be empty. Speaker tags (@Voice1, @Voice2, etc.) are case-insensitive and must refer to a connected voice; tagging a voice that is not connected raises an error. When two or more voices are connected, the text must reference every connected voice at least once, or the node reports the missing tags. On drama-3 and s2.1-pro, connecting 0 voices uses a random voice, 1 voice uses that voice alone, and 2 or more voices enable multi-speaker dialogue. On s1, a single optional voice is used and leaving it unconnected uses a random voice. Cues can be placed in the text: [happy] and [whispering] on s2.1-pro, (happy) on s1, and plain-language [directions] and `<whisper>...</whisper>` word tags on drama-3.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The generated speech as an audio file.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/en.md)

* * *

**Source fingerprint (SHA-256):** `adcfe8f994b8fbe07efb3dd3f86c8955ea3cec62cc3f0321efd2b63c0470b7a3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FishAudioTextToSpeech.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FishAudioTextToSpeech)

[FishAudioSpeechToText - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FishAudioSpeechToText)[FishAudioVoiceSelector - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FishAudioVoiceSelector)

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
