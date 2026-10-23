---
url: https://docs.comfy.org/built-in-nodes/ElevenLabsTextToDialogue/
title: ElevenLabsTextToDialogue - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:51.429282+00:00
---

# ElevenLabsTextToDialogue - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ElevenLabsTextToDialogue/

Elevenlabs

# ElevenLabsTextToDialogue - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ElevenLabs Text to Dialogue node generates a multi-speaker audio dialogue from text.

Copy pageCopy page

The ElevenLabs Text to Dialogue node generates a multi-speaker audio dialogue from text. It allows you to create a conversation by specifying different text lines and distinct voices for each participant. The node sends the dialogue request to the ElevenLabs API and returns the generated audio.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`stability`| Voice stability. Lower values give broader emotional range, higher values produce more consistent but potentially monotonous speech. (default: 0.5)| FLOAT| Yes| 0.0 - 1.0  
`apply_text_normalization`| Text normalization mode. ‘auto’ lets the system decide, ‘on’ always applies normalization, ‘off’ skips it.| COMBO| Yes| `"auto"`  
`"on"`  
`"off"`  
`model`| Model to use for dialogue generation (default: `"eleven_v4"`).| COMBO| Yes| `"eleven_v3"`  
`"eleven_v4"`  
`"eleven_v4_turbo"`  
`inputs`| Number of dialogue entries. Selecting a number creates that many text and voice input pairs.| DYNAMIC_COMBO| Yes| `"1"`  
`"2"`  
`"3"`  
`"4"`  
`"5"`  
`"6"`  
`"7"`  
`"8"`  
`"9"`  
`"10"`  
`language_code`| ISO 639-1 language code (e.g., ‘en’, ‘es’, ‘ja’). Leave empty for automatic detection. (default: empty)| STRING| Yes| -  
`seed`| Seed for reproducibility. (default: 1)| INT| Yes| 0 - 4294967295  
`output_format`| Audio output format.| COMBO| Yes| `"mp3_44100_192"`  
`"opus_48000_192"`  
  
### 

​

Dialogue Entry Inputs

Shared by all `inputs` options.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`text1` … `text10`| Text content for the corresponding dialogue entry. The node creates one `text` field for each selected dialogue entry. Each text value must contain at least one character.| STRING| Yes| -  
`voice1` … `voice10`| Voice for the corresponding dialogue entry. Connect from a Voice Selector or Instant Voice Clone node. The node creates one `voice` field for each selected dialogue entry.| ELEVENLABS_VOICE| Yes| -  
  
**Note:** The `inputs` selector can create up to 10 dialogue entries. Each entry requires both a `text` field and a `voice` field. The `text` value cannot be empty. The `voice` input expects a voice ID provided by a compatible ElevenLabs voice node.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The generated multi-speaker dialogue audio in the selected output format.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/en.md)

* * *

**Source fingerprint (SHA-256):** `bff737be0c828990d7286de4372e995295a4716febd388d7cc02c2a9987a6c80`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ElevenLabsTextToDialogue.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ElevenLabsTextToDialogue)

[ElevenLabsSpeechToText - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ElevenLabsSpeechToText)[ElevenLabsTextToSoundEffects - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ElevenLabsTextToSoundEffects)

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
