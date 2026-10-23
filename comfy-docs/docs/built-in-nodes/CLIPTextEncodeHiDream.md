---
url: https://docs.comfy.org/built-in-nodes/CLIPTextEncodeHiDream/
title: CLIPTextEncodeHiDream - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:32.725667+00:00
---

# CLIPTextEncodeHiDream - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CLIPTextEncodeHiDream/

Hidream

# CLIPTextEncodeHiDream - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CLIPTextEncodeHiDream node processes four separate text inputs using different language models (CLIP-L, CLIP-G, T5-XXL

Copy pageCopy page

The CLIPTextEncodeHiDream node processes four separate text inputs using different language models (CLIP-L, CLIP-G, T5-XXL, and LLaMA) and combines them into a single conditioning output. It tokenizes each text input with its corresponding model and encodes them together using a scheduled encoding approach, enabling more sophisticated text conditioning by leveraging multiple language models simultaneously.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used for tokenization and encoding| CLIP| Yes| -  
`clip_l`| Text input for CLIP-L model processing. Supports multiline text and dynamic prompts.| STRING| Yes| -  
`clip_g`| Text input for CLIP-G model processing. Supports multiline text and dynamic prompts.| STRING| Yes| -  
`t5xxl`| Text input for T5-XXL model processing. Supports multiline text and dynamic prompts.| STRING| Yes| -  
`llama`| Text input for LLaMA model processing. Supports multiline text and dynamic prompts.| STRING| Yes| -  
  
**Note:** All four text inputs (`clip_l`, `clip_g`, `t5xxl`, and `llama`) are required for proper functioning, as each contributes to the final conditioning output through the scheduled encoding process.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The combined conditioning output from all processed text inputs, encoded using the scheduled encoding method| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/en.md)

* * *

**Source fingerprint (SHA-256):** `c5e269c17bd2dd7d7171c02598a87983a988d953dd7df285978fc25a9c896e46`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CLIPTextEncodeHiDream.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CLIPTextEncodeHiDream)

[GLIGENTextBoxApply - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GLIGENTextBoxApply)[HiDreamO1ReferenceImages - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HiDreamO1ReferenceImages)

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
