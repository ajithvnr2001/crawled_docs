---
url: https://docs.comfy.org/built-in-nodes/LatentOperationTonemapReinhard/
title: LatentOperationTonemapReinhard - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:21.743905+00:00
---

# LatentOperationTonemapReinhard - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentOperationTonemapReinhard/

Operations

# LatentOperationTonemapReinhard - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a latent operation that applies Reinhard tonemapping to latent vectors.

Copy pageCopy page

This node creates a latent operation that applies Reinhard tonemapping to latent vectors. It normalizes each latent vector, measures the overall magnitude distribution (mean and standard deviation), and then compresses extreme magnitudes using the Reinhard curve, with the overall strength controlled by a multiplier. The node is marked as experimental (also searchable as “hdr latent”).

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`multiplier`| Controls the intensity of the tonemapping effect (default: 1.0)| FLOAT| Yes| 0.0 to 100.0 (step 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`operation`| Returns a tonemapping operation that can be applied to latent vectors| LATENT_OPERATION  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/en.md)

* * *

**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentOperationTonemapReinhard.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentOperationTonemapReinhard)

[LatentOperationSharpen - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentOperationSharpen)[LatentAdd - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentAdd)

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
