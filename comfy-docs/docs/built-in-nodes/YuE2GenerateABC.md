---
url: https://docs.comfy.org/built-in-nodes/YuE2GenerateABC/
title: YuE2GenerateABC - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:26.613040+00:00
---

# YuE2GenerateABC - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/YuE2GenerateABC/

Yue2

# YuE2GenerateABC - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates ABC notation for a song based on a style description and lyrics, using a YuE2 text-and-lyrics model.

Copy pageCopy page

This node generates ABC notation for a song based on a style description and lyrics, using a YuE2 text-and-lyrics model. The resulting `abc` output can be connected to the YuE2 Generate Music node to produce audio.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The YuE2 model used to tokenize the style and lyrics and generate the ABC notation.| CLIP| Yes| -  
`style`| Text describing the musical style of the song. Supports multiline input and dynamic prompts.| STRING| Yes| -  
`lyrics`| Text containing the lyrics of the song. Supports multiline input and dynamic prompts.| STRING| Yes| -  
`seed`| Random seed used for generation. Changing it produces different results. Default: 0.| INT| Yes| 0 to 18446744073709551615  
`mode`| full: generates melody and chords; melody: generates melody only, recommended for covers.| COMBO| Yes| ”full"  
"melody”  
`max_abc_tokens`| Maximum number of tokens generated for the ABC notation. Default: 8192. Advanced setting.| INT| Yes| 1 to 20000  
`temperature`| Controls the randomness of the generated tokens. Higher values produce more varied output. Default: 0.7. Advanced setting.| FLOAT| Yes| 0.0 to 5.0  
`top_p`| Nucleus sampling threshold; only tokens within this cumulative probability are considered. Default: 0.9. Advanced setting.| FLOAT| Yes| 0.01 to 1.0  
`top_k`| Limits token selection to the K most likely tokens. Default: 30. Advanced setting.| INT| Yes| 1 to 32768  
`repetition_penalty`| Penalty applied to repeated tokens during generation. Default: 1.005. Advanced setting.| FLOAT| Yes| 0.01 to 10.0  
`penalty_window`| Number of recent ABC tokens used to penalize repetition. Default: 100. Advanced setting.| INT| Yes| 1 to 20000  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`abc`| The generated ABC notation of the song, which can be connected to the YuE2 Generate Music node.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/en.md)

* * *

**Source fingerprint (SHA-256):** `2c1bf0841a044724ff0477f920972d70bbd97de49b56fbe6213a9ac134797130`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/YuE2GenerateABC.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/YuE2GenerateABC)

[SheetSage2AudioToABC - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SheetSage2AudioToABC)[YuE2GenerateMusic - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/YuE2GenerateMusic)

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
