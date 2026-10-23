---
url: https://docs.comfy.org/built-in-nodes/CLIPTextEncodeControlnet/
title: CLIPTextEncodeControlnet - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:33.069930+00:00
---

# CLIPTextEncodeControlnet - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CLIPTextEncodeControlnet/

Conditioning

# CLIPTextEncodeControlnet - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CLIP Text Encode (Controlnet) node encodes a text prompt with a CLIP model and adds the resulting text encoding to existing conditioning data.

Copy pageCopy page

The CLIP Text Encode (Controlnet) node encodes a text prompt with a CLIP model and adds the resulting text encoding to existing conditioning data. It stores the text embeddings as controlnet cross-attention parameters inside each conditioning entry, so the returned conditioning carries that extra controlnet information.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used for text tokenization and encoding| CLIP| Yes| -  
`conditioning`| Existing conditioning data to be combined with the CLIP text encoding| CONDITIONING| Yes| -  
`text`| The text prompt to be processed by the CLIP model. Supports multiline text and dynamic prompts| STRING| Yes| -  
  
**Note:** All three inputs (`clip`, `conditioning`, and `text`) are required for this node to function. The `text` input supports multiline text and dynamic prompts for flexible text processing. This node is marked as experimental in the source code.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| Enhanced conditioning data with the added controlnet cross-attention parameters (`cross_attn_controlnet` and `pooled_output_controlnet`) derived from the CLIP text encoding| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/en.md)

* * *

**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CLIPTextEncodeControlnet.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CLIPTextEncodeControlnet)

[CLIPTextEncode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClipTextEncode)[CLIPVisionEncode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ClipVisionEncode)

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
