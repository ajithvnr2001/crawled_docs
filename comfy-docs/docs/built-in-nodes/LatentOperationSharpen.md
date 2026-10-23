---
url: https://docs.comfy.org/built-in-nodes/LatentOperationSharpen/
title: LatentOperationSharpen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:21.303485+00:00
---

# LatentOperationSharpen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentOperationSharpen/

Operations

# LatentOperationSharpen - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentOperationSharpen node creates a sharpening operation for latent representations using a Gaussian-based kernel.

Copy pageCopy page

The LatentOperationSharpen node creates a sharpening operation for latent representations using a Gaussian-based kernel. It normalizes the latent data, applies a custom sharpening kernel through convolution, and then restores the original luminance, which enhances details and edges in the latent space representation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`sharpen_radius`| The radius of the sharpening kernel, which controls the size of the area used for sharpening (default: 9)| INT| Yes| 1-31  
`sigma`| The standard deviation of the Gaussian kernel used to build the sharpening kernel (default: 1.0)| FLOAT| Yes| 0.1-10.0  
`alpha`| The sharpening intensity factor; higher values produce a stronger sharpening effect (default: 0.1)| FLOAT| Yes| 0.0-5.0  
  
All three inputs are advanced parameters and have default values, so the node can be used without changing them. This node is marked as experimental.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`operation`| Returns a sharpening operation that can be applied to latent data| LATENT_OPERATION  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/en.md)

* * *

**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentOperationSharpen.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentOperationSharpen)

[LatentOperationBlend - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentOperationBlend)[LatentOperationTonemapReinhard - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentOperationTonemapReinhard)

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
