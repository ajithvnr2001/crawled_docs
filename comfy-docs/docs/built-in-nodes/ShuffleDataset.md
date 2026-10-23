---
url: https://docs.comfy.org/built-in-nodes/ShuffleDataset/
title: ShuffleDataset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.773539+00:00
---

# ShuffleDataset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ShuffleDataset/

Batch

# ShuffleDataset - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Shuffle Dataset node takes a list of images and randomly changes their order.

Copy pageCopy page

The Shuffle Dataset node takes a list of images and randomly changes their order. It uses a seed value to control the randomness, ensuring the same shuffle order can be reproduced. This is useful for randomizing the sequence of images in a dataset before processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The list of images to be shuffled.| IMAGE| Yes| -  
`seed`| Random seed. (default: 0)| INT| No| 0 to 18446744073709551615  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The same list of images, but in a new, randomly shuffled order.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/en.md)

* * *

**Source fingerprint (SHA-256):** `6cde5dcf15817ab98f35f7b2e40fe79a5451c86dba93c0e3cd2622d1cec76c36`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ShuffleDataset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ShuffleDataset)

[RepeatImageBatch - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RepeatImageBatch)[ShuffleImageTextDataset - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ShuffleImageTextDataset)

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
