---
url: https://docs.comfy.org/built-in-nodes/ShuffleImageTextDataset/
title: ShuffleImageTextDataset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.310834+00:00
---

# ShuffleImageTextDataset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ShuffleImageTextDataset/

Batch

# ShuffleImageTextDataset - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node shuffles a list of images and a list of texts together, keeping their pairings intact.

Copy pageCopy page

This node shuffles a list of images and a list of texts together, keeping their pairings intact. It uses a random seed to determine the shuffle order, ensuring the same input lists will be shuffled in the same way each time the seed is reused.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| List of images to shuffle.| IMAGE| Yes| -  
`texts`| List of texts to shuffle.| STRING| Yes| -  
`seed`| Random seed. The shuffle order is determined by this value (default: 0).| INT| No| 0 to 18446744073709551615  
  
**Note:** The `images` and `texts` inputs must be lists of the same length. The node will pair the first image with the first text, the second image with the second text, and so on, before shuffling these pairs together.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The shuffled list of images.| IMAGE  
`texts`| The shuffled list of texts, maintaining their original pairings with the images.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/en.md)

* * *

**Source fingerprint (SHA-256):** `77050e9f7255e64b07bd394908b679acef399d78ec9be7c1346d6f297c109968`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ShuffleImageTextDataset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ShuffleImageTextDataset)

[ShuffleDataset - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ShuffleDataset)[SplitImageToTileList - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SplitImageToTileList)

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
