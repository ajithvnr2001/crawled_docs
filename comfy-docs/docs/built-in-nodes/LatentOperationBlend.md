---
url: https://docs.comfy.org/built-in-nodes/LatentOperationBlend/
title: LatentOperationBlend - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:21.187344+00:00
---

# LatentOperationBlend - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentOperationBlend/

Operations

# LatentOperationBlend - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a latent operation that blends a latent toward a reference latent

Copy pageCopy page

This node creates a latent operation that blends a latent toward a reference latent, and returns that operation so it can be plugged into nodes such as Latent Apply Operation or Latent Apply Operation CFG. When the reference is a different spatial size, it is resized to the target latent with nearest-neighbor interpolation, and a reference with a smaller batch is repeated to match the target batch size. A strength of 0 leaves the latent unchanged. This node is marked as experimental.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference`| The latent to blend toward. Its samples are cast to the device and dtype of the latent being processed, then resized and repeated to match it.| LATENT| Yes| -  
`strength`| How far to blend toward the reference: 0 leaves the latent unchanged, 1 matches the resized reference latent (default: 1.0).| FLOAT| Yes| 0.0 to 1.0 (step 0.0001)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`operation`| A blend operation that can be applied to latent samples.| LATENT_OPERATION  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationBlend/en.md)

* * *

**Source fingerprint (SHA-256):** `5890089afddf83ddd4edd992606509b118aac9ef13eb89589f73fa75e0b9dd5a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentOperationBlend.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentOperationBlend)

[LatentApplyOperationCFG - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentApplyOperationCFG)[LatentOperationSharpen - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentOperationSharpen)

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
