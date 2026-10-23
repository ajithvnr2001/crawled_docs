---
url: https://docs.comfy.org/built-in-nodes/MiniMaxMusic3TextEncode/
title: MiniMaxMusic3TextEncode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:32.836906+00:00
---

# MiniMaxMusic3TextEncode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MiniMaxMusic3TextEncode/

Minimax Music

# MiniMaxMusic3TextEncode - ComfyUI Built-in Node Documentation

Copy pageCopy page

MiniMax Music3 Text Encode uses a MiniMax Music3 CLIP model to convert text captions and lyrics into an acoustic conditioning sequence for music generation.

Copy pageCopy page

MiniMax Music3 Text Encode uses a MiniMax Music3 CLIP model to convert text captions and lyrics into an acoustic conditioning sequence for music generation. The node returns the resulting CONDITIONING data, along with the actual audio duration in seconds calculated from the input maximum duration.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The MiniMax Music3 CLIP model, used for text encoding and conditioning sequence generation.| CLIP| Yes| -  
`caption`| Text describing the music to generate. Supports multi-line text and dynamic prompts.| STRING| Yes| -  
`lyrics`| The lyrics text to be used for generating the music. Supports multi-line text and dynamic prompts.| STRING| Yes| -  
`seed`| Reproducible random seed for the generation process. Default: 0. A control-after-generate widget is provided.| INT| Yes| 0 to 18446744073709551615 (0xffffffffffffffff)  
`max_duration`| Maximum duration in seconds; the model can end the song earlier. Default: 120.0.| FLOAT| Yes| 0.04 to the model’s maximum audio duration (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04  
`cfg_scale`| Classifier-free guidance scale. Default: model constant CFG_SCALE. Advanced parameter.| FLOAT| Yes| 0.0 to 100.0, step 0.1 (keeps 2 decimal places)  
`top_k`| Top-k sampling value used for acoustic token selection. Default: model constant CFG_TOP_K. Advanced parameter.| INT| Yes| 1 to the model’s vocabulary size (C0_VOCAB_SIZE)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`conditioning`| The generated acoustic conditioning sequence, used to guide subsequent music generation.| CONDITIONING  
`seconds`| The actual duration of the conditioning sequence, in seconds.| FLOAT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/en.md)

* * *

**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MiniMaxMusic3TextEncode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MiniMaxMusic3TextEncode)

[MiniMaxH3ReferenceToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MiniMaxH3ReferenceToVideo)[PhotoMakerEncode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PhotoMakerEncode)

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
