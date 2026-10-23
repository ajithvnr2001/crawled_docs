---
url: https://docs.comfy.org/built-in-nodes/RepeatLatentBatch/
title: RepeatLatentBatch - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:51.096123+00:00
---

# RepeatLatentBatch - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RepeatLatentBatch/

Batch

# RepeatLatentBatch - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RepeatLatentBatch node is designed to replicate a given batch of latent representations a specified number of times

Copy pageCopy page

The RepeatLatentBatch node is designed to replicate a given batch of latent representations a specified number of times, potentially including additional data like noise masks and batch indices. This functionality is crucial for operations that require multiple instances of the same latent data, such as data augmentation or specific generative tasks.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`samples`| The ‘samples’ parameter represents the latent representations to be replicated. It is essential for defining the data that will undergo repetition.| `LATENT`  
`amount`| The ‘amount’ parameter specifies the number of times the input samples should be repeated. It directly influences the size of the output batch, thereby affecting the computational load and the diversity of the generated data.| `INT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output is a modified version of the input latent representations, replicated according to the specified ‘amount’. It may include replicated noise masks and adjusted batch indices, if applicable.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RepeatLatentBatch.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RepeatLatentBatch)

[RebatchLatents - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RebatchLatents)[ReplaceVideoLatentFrames - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ReplaceVideoLatentFrames)

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
