---
url: https://docs.comfy.org/built-in-nodes/SaveAudioMP3/
title: SaveAudioMP3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:57.863480+00:00
---

# SaveAudioMP3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveAudioMP3/

Audio

# SaveAudioMP3 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SaveAudioMP3 node saves audio data as an MP3 file.

Copy pageCopy page

The SaveAudioMP3 node saves audio data as an MP3 file. It takes an audio input and exports it to the output directory with a customizable filename and quality setting, handling file naming and MP3 format conversion automatically. **This node is deprecated and may be removed in future versions.**

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The audio data to be saved as an MP3 file| AUDIO| Yes| -  
`filename_prefix`| The prefix for the output filename (default: “audio/ComfyUI”)| STRING| No| -  
`quality`| The audio quality setting for the MP3 file (default: “V0”)| COMBO| No| `"V0"`  
`"128k"`  
`"320k"`  
`prompt`| Internal prompt data, automatically provided by the system| PROMPT| No| -  
`extra_pnginfo`| Additional PNG information, automatically provided by the system| EXTRA_PNGINFO| No| -  
  
**Note:** If the input `audio` is None (for example, when the source video has no audio track), the node raises a ValueError.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The audio data that was saved to an MP3 file| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/en.md)

* * *

**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveAudioMP3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveAudioMP3)

[SaveAudioAdvanced - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveAudioAdvanced)[SaveAudioOpus - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveAudioOpus)

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
