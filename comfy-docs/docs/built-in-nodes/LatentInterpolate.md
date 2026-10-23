---
url: https://docs.comfy.org/built-in-nodes/LatentInterpolate/
title: LatentInterpolate - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:20.978397+00:00
---

# LatentInterpolate - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentInterpolate/

Advanced

# LatentInterpolate - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentInterpolate node is designed to perform interpolation between two sets of latent samples based on a specified ratio

Copy pageCopy page

The LatentInterpolate node is designed to perform interpolation between two sets of latent samples based on a specified ratio, blending the characteristics of both sets to produce a new, intermediate set of latent samples.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`samples1`| The first set of latent samples to be interpolated. It serves as the starting point for the interpolation process.| `LATENT`  
`samples2`| The second set of latent samples to be interpolated. It serves as the endpoint for the interpolation process.| `LATENT`  
`ratio`| A floating-point value that determines the weight of each set of samples in the interpolated output. A ratio of 0 produces a copy of the first set, while a ratio of 1 produces a copy of the second set.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output is a new set of latent samples that represent an interpolated state between the two input sets, based on the specified ratio.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentInterpolate.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentInterpolate)

[LatentCutToBatch - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentCutToBatch)[LatentMultiply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentMultiply)

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
