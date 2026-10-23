---
url: https://docs.comfy.org/built-in-nodes/T5TokenizerOptions/
title: T5TokenizerOptions - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.313130+00:00
---

# T5TokenizerOptions - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/T5TokenizerOptions/

Conditioning

# T5TokenizerOptions - ComfyUI Built-in Node Documentation

Copy pageCopy page

The T5TokenizerOptions node configures tokenizer settings for various T5 model types.

Copy pageCopy page

## 

​

Overview

The T5TokenizerOptions node configures tokenizer settings for various T5 model types. It sets minimum padding and minimum length parameters for multiple T5 model variants including t5xxl, pile_t5xl, t5base, mt5xl, and umt5xxl. The node takes a CLIP input, applies the settings to a copy of it, and returns the modified CLIP.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model to configure tokenizer options for| CLIP| Yes| -  
`min_padding`| Minimum padding value to set for all T5 model types (default: 0)| INT| Yes| 0 to 10000  
`min_length`| Minimum length value to set for all T5 model types (default: 0)| INT| Yes| 0 to 10000  
  
Note: This node is marked as experimental in ComfyUI. The settings are applied to all supported T5 variants at once: t5xxl, pile_t5xl, t5base, mt5xl, and umt5xxl. The input `clip` is cloned before modification, so the original CLIP is not altered.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The modified CLIP model with updated tokenizer options applied to all T5 variants| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/en.md)

* * *

**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/T5TokenizerOptions.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/T5TokenizerOptions)

[StyleModelApply - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StyleModelApply)[unCLIPConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/unCLIPConditioning)

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
