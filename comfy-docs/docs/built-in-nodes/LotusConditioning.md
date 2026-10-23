---
url: https://docs.comfy.org/built-in-nodes/LotusConditioning/
title: LotusConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:26.030968+00:00
---

# LotusConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LotusConditioning/

Lotus

# LotusConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LotusConditioning node supplies fixed, pre-computed conditioning embeddings for the Lotus model.

Copy pageCopy page

The LotusConditioning node supplies fixed, pre-computed conditioning embeddings for the Lotus model. Because Lotus uses a frozen encoder with null conditioning, the node inlines the resulting prompt embeddings directly instead of running inference or loading large tensor files, so its output never changes. The returned conditioning can be plugged straight into a generation pipeline that expects Lotus-compatible conditioning.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
 _No inputs_|  This node does not accept any input parameters.| -| -| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`conditioning`| The pre-computed conditioning embeddings for the Lotus model. Returned as a conditioning list holding the fixed prompt embeddings together with an empty dictionary.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LotusConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LotusConditioning)

[Kandinsky5ImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Kandinsky5ImageToVideo)[GetICLoRAParameters - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GetICLoRAParameters)

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
