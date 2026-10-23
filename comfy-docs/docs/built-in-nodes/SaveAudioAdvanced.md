---
url: https://docs.comfy.org/built-in-nodes/SaveAudioAdvanced/
title: SaveAudioAdvanced - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:58.245386+00:00
---

# SaveAudioAdvanced - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveAudioAdvanced/

Audio

# SaveAudioAdvanced - ComfyUI Built-in Node Documentation

Copy pageCopy page

Saves the input audio to your ComfyUI output directory.

Copy pageCopy page

Saves the input audio to your ComfyUI output directory. This node allows you to export audio in various formats including FLAC, MP3, and Opus with configurable quality settings.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The audio to save.| AUDIO| Yes| -  
`filename_prefix`| The prefix for the file to save. May include formatting tokens such as %date:yyyy-MM-dd%. (default: “audio/ComfyUI”)| STRING| Yes| -  
`format`| The file format in which to save the audio.| DYNAMIC_COMBO| Yes| ”flac"  
"mp3"  
"opus”  
  
### 

​

MP3 Inputs

When “mp3” is selected as the format, the following setting becomes available.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`quality`| The encoding quality of the output MP3 file. (default: “V0”)| COMBO| No| ”V0"  
"128k"  
"320k”  
  
### 

​

Opus Inputs

When “opus” is selected as the format, the following setting becomes available.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`quality`| The encoding quality of the output Opus file. (default: “128k”)| COMBO| No| ”64k"  
"96k"  
"128k"  
"192k"  
"320k”  
  
Note: The `quality` setting is only available when the matching format is selected. When “flac” is selected, no additional quality setting is available.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The input audio, passed through unchanged after being saved.| AUDIO  
  
The node also returns UI information containing the saved audio file information.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/en.md)

* * *

**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveAudioAdvanced.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveAudioAdvanced)

[SaveAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveAudio)[SaveAudioMP3 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveAudioMP3)

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
