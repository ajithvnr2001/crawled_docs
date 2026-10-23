---
url: https://docs.comfy.org/built-in-nodes/SaveAudioOpus/
title: SaveAudioOpus - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:58.407713+00:00
---

# SaveAudioOpus - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveAudioOpus/

Audio

# SaveAudioOpus - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SaveAudioOpus node saves audio data to a file in the Opus format

Copy pageCopy page

The SaveAudioOpus node saves audio data to a file in the Opus format, letting you choose the encoding quality (bitrate) and the filename prefix for the exported file. This node is deprecated and may be removed in future versions.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The audio data to be saved as an Opus file. A ValueError is raised if this is None (for example, when the source video has no audio track).| AUDIO| Yes| -  
`filename_prefix`| The prefix used for the output filename (default: “audio/ComfyUI”).| STRING| No| -  
`quality`| The bitrate used to encode the Opus file; higher values produce better quality but larger files (default: “128k”).| COMBO| No| `"64k"`  
`"96k"`  
`"128k"`  
`"192k"`  
`"320k"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The audio data that was saved to the Opus file.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/en.md)

* * *

**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveAudioOpus.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveAudioOpus)

[SaveAudioMP3 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveAudioMP3)[SplitAudioChannels - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SplitAudioChannels)

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
