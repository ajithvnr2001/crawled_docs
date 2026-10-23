---
url: https://docs.comfy.org/built-in-nodes/RebatchLatents/
title: RebatchLatents - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:47.077510+00:00
---

# RebatchLatents - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RebatchLatents/

Batch

# RebatchLatents - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RebatchLatents node is designed to reorganize a batch of latent representations into a new batch configuration, based on a specified batch size.

Copy pageCopy page

The RebatchLatents node is designed to reorganize a batch of latent representations into a new batch configuration, based on a specified batch size. It ensures that the latent samples are grouped appropriately, handling variations in dimensions and sizes, to facilitate further processing or model inference.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`latents`| The ‘latents’ parameter represents the input latent representations to be rebatched. It is crucial for determining the structure and content of the output batch.| `LATENT`  
`batch_size`| The ‘batch_size’ parameter specifies the desired number of samples per batch in the output. It directly influences the grouping and division of the input latents into new batches.| `INT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output is a reorganized batch of latent representations, adjusted according to the specified batch size. It facilitates further processing or analysis.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RebatchLatents.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RebatchLatents)

[LatentFromBatch - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentFromBatch)[RepeatLatentBatch - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RepeatLatentBatch)

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
