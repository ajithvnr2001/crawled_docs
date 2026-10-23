---
url: https://docs.comfy.org/built-in-nodes/ShuffleVideoDataset/
title: ShuffleVideoDataset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.670374+00:00
---

# ShuffleVideoDataset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ShuffleVideoDataset/

Batch

# ShuffleVideoDataset - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node takes a list of videos and randomly reorders them.

Copy pageCopy page

This node takes a list of videos and randomly reorders them. It uses a random seed to make the shuffle reproducible, so the same seed always produces the same output order.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`videos`| List of videos to shuffle.| VIDEO| Yes| List of video inputs  
`seed`| Random seed for shuffling (default: 0).| INT| No| 0 to 18446744073709551615  
  
Note: The seed value is reduced modulo 4294967295 (2^32 - 1) before being used. As a result, seeds that differ by a multiple of 4294967295 produce the same output order.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`videos`| Shuffled list of videos in random order.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoDataset/en.md)

* * *

**Source fingerprint (SHA-256):** `0bd32b664197d3bbd4c53f65e29ef38fba836579f07f05cb7fb85f3b8a1024ac`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ShuffleVideoDataset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ShuffleVideoDataset)

[wanBlockSwap - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/wanBlockSwap)[ShuffleVideoTextDataset - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ShuffleVideoTextDataset)

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
