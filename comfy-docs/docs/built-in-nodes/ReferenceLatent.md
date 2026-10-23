---
url: https://docs.comfy.org/built-in-nodes/ReferenceLatent/
title: ReferenceLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:49.396339+00:00
---

# ReferenceLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ReferenceLatent/

Conditioning

# ReferenceLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node sets the guiding latent for an edit model.

Copy pageCopy page

This node sets the guiding latent for an edit model. It takes conditioning data and an optional latent input, then modifies the conditioning to include reference latent information. If the model supports it, you can chain multiple Set Reference Latent nodes to set multiple reference images.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`conditioning`| The conditioning data to be modified with reference latent information| CONDITIONING| Yes| -  
`latent`| Optional latent data to use as reference for the edit model. If not provided, the conditioning is returned unchanged| LATENT| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The modified conditioning data containing reference latent information| CONDITIONING  
  
## 

​

Notes

  * The reference latent is stored as a list of sample tensors, so connecting several Set Reference Latent nodes in sequence appends additional references rather than replacing the previous one.
  * When no `latent` is connected, the node passes the incoming `conditioning` through without changes.



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ReferenceLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ReferenceLatent)

[PiDConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PiDConditioning)[ReferenceMultiLatent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ReferenceMultiLatent)

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
