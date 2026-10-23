---
url: https://docs.comfy.org/built-in-nodes/LatentConcat/
title: LatentConcat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:20.625547+00:00
---

# LatentConcat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentConcat/

Advanced

# LatentConcat - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentConcat node combines two latent samples by joining them together along a chosen dimension.

Copy pageCopy page

The LatentConcat node combines two latent samples by joining them together along a chosen dimension. It takes two latent inputs and concatenates them along the x, y, or t axis, with the option to control which sample comes first. The node automatically adjusts the batch size of the second input to match the first before performing the concatenation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples1`| The first latent sample to concatenate| LATENT| Yes| -  
`samples2`| The second latent sample to concatenate| LATENT| Yes| -  
`dim`| The dimension along which to concatenate the latent samples. Positive values (x, y, t) place samples1 before samples2 in the result. Negative values (-x, -y, -t) place samples2 before samples1. The dimension mapping is: x = width, y = height, t = time/frames| COMBO| Yes| `"x"`  
`"-x"`  
`"y"`  
`"-y"`  
`"t"`  
`"-t"`  
  
**Note:** The second latent sample (`samples2`) is automatically repeated as needed to match the batch size of the first latent sample (`samples1`) before concatenation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The concatenated latent samples resulting from combining the two input samples along the specified dimension| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/en.md)

* * *

**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentConcat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentConcat)

[LatentBatchSeedBehavior - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentBatchSeedBehavior)[LatentCut - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentCut)

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
