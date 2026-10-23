---
url: https://docs.comfy.org/built-in-nodes/BatchLatentsNode/
title: BatchLatentsNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:23.038754+00:00
---

# BatchLatentsNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BatchLatentsNode/

Batch

# BatchLatentsNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Batch Latents node combines multiple latent inputs into a single batch.

Copy pageCopy page

The Batch Latents node combines multiple latent inputs into a single batch. It takes a variable number of latent samples and merges them along the batch dimension so they can be processed together by subsequent nodes. The node also merges the batch index metadata of all inputs into the combined output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latents`| A set of latent samples to be combined into a single batch. You must provide at least one latent, and you can add up to 50. The node automatically creates input slots (`latent_1`, `latent_2`, and so on) as you connect more latents.| LATENT| Yes| 1 to 50 inputs  
  
**Note:** You must provide at least one latent input for the node to function. The node automatically creates input slots as you connect more latents, up to a maximum of 50. Each input latent is reshaped to match the sample shape of the first latent before being combined, and any latent without batch index metadata is assigned a sequential batch index. The input latents are joined along the batch dimension to produce the combined result.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| A single latent output containing all the input latents combined into one batch, together with their merged batch index metadata.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/en.md)

* * *

**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BatchLatentsNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BatchLatentsNode)

[EmptyARVideoLatent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyARVideoLatent)[LatentBatch - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentBatch)

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
