---
url: https://docs.comfy.org/built-in-nodes/Mahiro/
title: Mahiro - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:29.098359+00:00
---

# Mahiro - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Mahiro/

Experimental

# Mahiro - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Mahiro node modifies the guidance function to focus more on the direction of the positive prompt rather than the difference between positive and negative

Copy pageCopy page

The Mahiro node modifies the guidance function to focus more on the direction of the positive prompt rather than the difference between positive and negative prompts. It creates a patched model that applies a custom guidance scaling approach using cosine similarity between normalized conditional and unconditional denoised outputs. This experimental node helps steer the generation more strongly toward the positive prompt’s intended direction.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to be patched with the modified guidance function| MODEL| Yes|   
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`patched_model`| The modified model with the Mahiro guidance function applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/en.md)

* * *

**Source fingerprint (SHA-256):** `56f13cd14ffde21ab980850b62e07bdd4db6733a545f9329bf908c6030147981`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Mahiro.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Mahiro)

[LoraSave - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoraSave)[PerpNeg - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PerpNeg)

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
