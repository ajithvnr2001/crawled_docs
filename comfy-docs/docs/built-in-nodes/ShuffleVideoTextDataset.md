---
url: https://docs.comfy.org/built-in-nodes/ShuffleVideoTextDataset/
title: ShuffleVideoTextDataset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.385230+00:00
---

# ShuffleVideoTextDataset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ShuffleVideoTextDataset/

Batch

# ShuffleVideoTextDataset - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node randomly shuffles the order of pairs of video-text in a list, keeping each video paired with its corresponding text.

Copy pageCopy page

This node randomly shuffles the order of pairs of video-text in a list, keeping each video paired with its corresponding text. It takes two lists of equal length and applies the same random permutation to both, ensuring that the original pairings are preserved after shuffling. A seed value controls the shuffle order so results can be reproduced.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`videos`| List of videos to shuffle.| VIDEO| Yes| List of video items  
`texts`| List of texts to shuffle (the captions paired with the videos).| STRING| Yes| List of text strings  
`seed`| Random seed that determines the shuffle order (default: 0).| INT| Yes| 0 to 18446744073709551615  
  
Note: `videos` and `texts` must have the same length, since the node pairs each video with the text at the same position and preserves those pairings when shuffling. Internally, the `seed` value is reduced using modulo 4294967295 (2^32 - 1) before the random order is generated, so very large seed values may produce the same shuffle as smaller ones.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`videos`| Shuffled videos in the new random order.| VIDEO  
`texts`| Shuffled texts in the same new order as the videos.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/en.md)

* * *

**Source fingerprint (SHA-256):** `834305718cd53a86211363750e887ffccdb54bc3b628dc17f049e546c234f9cb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ShuffleVideoTextDataset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ShuffleVideoTextDataset)

[ShuffleVideoDataset - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ShuffleVideoDataset)[LTXVPreprocess - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVPreprocess)

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
