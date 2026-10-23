---
url: https://docs.comfy.org/built-in-nodes/ElevenLabsSpeechToText/
title: ElevenLabsSpeechToText - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:51.607386+00:00
---

# ElevenLabsSpeechToText - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ElevenLabsSpeechToText/

Elevenlabs

# ElevenLabsSpeechToText - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ElevenLabs Speech to Text node transcribes audio into text using the ElevenLabs API.

Copy pageCopy page

The ElevenLabs Speech to Text node transcribes audio into text using the ElevenLabs API. It supports automatic language detection, speaker diarization (identifying different speakers), and audio event tagging (annotating sounds like laughter or music in the transcript).

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for transcription. Selecting this model reveals additional parameters.| DYNAMIC_COMBO| Yes| `"scribe_v2"`  
`audio`| Audio to transcribe.| AUDIO| Yes| -  
`language_code`| ISO-639-1 or ISO-639-3 language code (e.g., ‘en’, ‘es’, ‘fra’). Leave empty for automatic detection. (default: "")| STRING| No| -  
`num_speakers`| Maximum number of speakers to predict. Set to 0 for automatic detection. (default: 0)| INT| No| 0 - 32  
`seed`| Seed for reproducibility (determinism not guaranteed). (default: 1)| INT| No| 0 - 2147483647  
  
### 

​

Scribe v2 Inputs

These parameters are shown when the `"scribe_v2"` model is selected.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`tag_audio_events`| Annotate sounds like (laughter), (music), etc. in transcript. (default: False)| BOOLEAN| No| -  
`diarize`| Annotate which speaker is talking. (default: False)| BOOLEAN| No| -  
`diarization_threshold`| Speaker separation sensitivity. Lower values are more sensitive to speaker changes. Only used when `diarize` is enabled. (default: 0.22)| FLOAT| No| 0.1 - 0.4  
`temperature`| Randomness control. 0.0 uses model default. Higher values increase randomness. (default: 0.0)| FLOAT| No| 0.0 - 2.0  
`timestamps_granularity`| Timing precision for transcript words. (default: “word”)| COMBO| No| `"word"`  
`"character"`  
`"none"`  
  
**Note:** `num_speakers` cannot be set to a value greater than 0 when `diarize` is enabled. You must either disable `diarize` or set `num_speakers` to 0.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`text`| The transcribed text from the audio.| STRING  
`language_code`| The detected language code of the audio.| STRING  
`words_json`| A JSON-formatted string containing detailed word-level information, including timestamps and speaker labels if enabled.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/en.md)

* * *

**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ElevenLabsSpeechToText.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ElevenLabsSpeechToText)

[ElevenLabsSpeechToSpeech - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ElevenLabsSpeechToSpeech)[ElevenLabsTextToDialogue - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ElevenLabsTextToDialogue)

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
