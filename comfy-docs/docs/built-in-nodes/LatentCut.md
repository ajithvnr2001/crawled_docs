---
url: https://docs.comfy.org/built-in-nodes/LatentCut/
title: LatentCut - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:21.394016+00:00
---

# LatentCut - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentCut/

Advanced

# LatentCut - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentCut node extracts a specific section from latent samples along a chosen dimension.

Copy pageCopy page

The LatentCut node extracts a specific section from latent samples along a chosen dimension. It cuts out a portion of the latent representation by specifying the dimension (x, y, or t), the starting position, and how much to extract. The node supports both positive and negative indexing and automatically adjusts the extraction amount so it stays within the available bounds.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The input latent samples to extract from| LATENT| Yes| -  
`dim`| The dimension along which to cut the latent samples. “x” cuts along the last axis (typically width), “y” along the second-to-last axis (typically height), and “t” along the third-to-last axis (typically frames in video latents)| COMBO| Yes| ”x"  
"y"  
"t”  
`index`| The starting position for the cut (default: 0). Positive values count from the start, negative values count from the end. The node clamps the index to stay within the valid range of the latent samples| INT| Yes| -16384 to 16384  
`amount`| The number of elements to extract along the specified dimension (default: 1). Must be at least 1. The node automatically reduces this value if it would exceed the available data beyond the starting index| INT| Yes| 1 to 16384  
  
Note: The `index` and `amount` values are adjusted to fit the actual size of the latent along the selected dimension. If `index` is larger than the dimension size, it is clamped to the last valid position. If `index` is negative, it is clamped to the dimension size in absolute terms, and `amount` is limited so it does not go past the end of the data.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The extracted portion of the latent samples| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/en.md)

* * *

**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentCut.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentCut)

[LatentConcat - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentConcat)[LatentCutToBatch - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentCutToBatch)

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
