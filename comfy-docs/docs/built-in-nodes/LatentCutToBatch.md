---
url: https://docs.comfy.org/built-in-nodes/LatentCutToBatch/
title: LatentCutToBatch - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:20.763805+00:00
---

# LatentCutToBatch - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentCutToBatch/

Advanced

# LatentCutToBatch - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentCutToBatch node splits a latent representation along a chosen dimension (time, width

Copy pageCopy page

The LatentCutToBatch node splits a latent representation along a chosen dimension (time, width, or height) into slices of a specified size and stacks those slices into a new batch. Each slice becomes a separate item in the batch, so different parts of a latent sample can be processed independently.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The latent representation to be split and batched.| LATENT| Yes| -  
`dim`| The dimension along which to cut the latent samples. `"t"` refers to the temporal (frame) dimension, `"x"` to the width, and `"y"` to the height.| COMBO| Yes| `"t"`  
`"x"`  
`"y"`  
`slice_size`| The size of each slice to cut from the specified dimension. If the dimension’s size is not perfectly divisible by this value, the remainder is discarded. (default: 1)| INT| Yes| 1 to 16384 (max resolution)  
  
Note: The `"t"` option only takes effect when the latent includes a temporal dimension. If the chosen dimension maps to the batch or channel position, or does not exist (for example, selecting `"t"` on a latent without frames), the node returns the input unchanged. If `slice_size` is larger than the size of the chosen dimension, the entire dimension is used as a single slice. When the dimension size is not evenly divisible by `slice_size`, the leftover portion at the end is discarded. The output batch size is the input batch size multiplied by the number of slices, and the sliced dimension itself is reduced to `slice_size`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| The resulting latent batch, containing the sliced and stacked samples.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/en.md)

* * *

**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentCutToBatch.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentCutToBatch)

[LatentCut - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentCut)[LatentInterpolate - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentInterpolate)

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
