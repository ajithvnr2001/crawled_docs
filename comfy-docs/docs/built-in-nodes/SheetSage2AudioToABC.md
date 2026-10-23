---
url: https://docs.comfy.org/built-in-nodes/SheetSage2AudioToABC/
title: SheetSage2AudioToABC - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.177312+00:00
---

# SheetSage2AudioToABC - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SheetSage2AudioToABC/

Yue2

# SheetSage2AudioToABC - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node transcribes vocal and instrumental melodies from music into ABC notation, a text-based format for writing down musical scores.

Copy pageCopy page

This node transcribes vocal and instrumental melodies from music into ABC notation, a text-based format for writing down musical scores. It analyzes the connected audio and returns the resulting notation as text, which can then be fed into the YuE2 Generate Music node using the matching mode.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio_encoder`| The audio encoder model used to analyze the audio and produce the ABC notation.| AUDIO_ENCODER| Yes| -  
`audio`| The music audio to transcribe into ABC notation.| AUDIO| Yes| -  
`mode`| Controls what is transcribed. “full” generates melody and chords; “melody” generates melody only, recommended for covers.| COMBO| Yes| `"melody"`  
`"full"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`abc`| The transcribed music in ABC notation, returned as a list of strings. Connect this to the YuE2 Generate Music node and use the matching mode.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SheetSage2AudioToABC/en.md)

* * *

**Source fingerprint (SHA-256):** `612d18dedd09b64210087c340b8f304ace8cd7b30b1a6e8e8ba7c749b355a497`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SheetSage2AudioToABC.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SheetSage2AudioToABC)

[WanImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanImageToVideo)[YuE2GenerateABC - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/YuE2GenerateABC)

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
