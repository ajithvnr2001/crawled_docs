---
url: https://docs.comfy.org/built-in-nodes/BatchImagesMasksLatentsNode/
title: BatchImagesMasksLatentsNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.046989+00:00
---

# BatchImagesMasksLatentsNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BatchImagesMasksLatentsNode/

Utils

# BatchImagesMasksLatentsNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Batch Images/Masks/Latents node combines multiple inputs of the same type into a single batch.

Copy pageCopy page

The Batch Images/Masks/Latents node combines multiple inputs of the same type into a single batch. It automatically detects whether the inputs are images, masks, or latent representations and uses the appropriate batching method. This is useful for preparing multiple items for processing by nodes that accept batched inputs.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`inputs`| A dynamic list of inputs to be combined into a batch. You can add between 1 and 50 items. All items must be of the same type (all images, all masks, or all latents).| IMAGE, MASK, or LATENT| Yes| 1 to 50 inputs  
  
**Note:** The node automatically determines the data type (IMAGE, MASK, or LATENT) based on the first item in the `inputs` list. All subsequent items must match this type. The node will fail if you try to mix different data types. **Additional behavior based on input type:**

  * **Images** : When batching images, the node pads images with fewer color channels to match the maximum channel count among all inputs (padding value is 1.0). It also resizes all images to match the dimensions of the first image using bilinear interpolation.
  * **Masks** : When batching masks, the node resizes all masks to match the dimensions of the first mask using bilinear interpolation.
  * **Latents** : When batching latents, the node reshapes all latent tensors to match the dimensions of the first latent’s samples. It also combines the `batch_index` values from each latent, extending the list with sequential indices if a latent lacks a `batch_index`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| A single batched output. The data type matches the input type (batched IMAGE, batched MASK, or batched LATENT).| IMAGE, MASK, or LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9f82b036c99577ebcda6de647c662def572ae1f01bd78dca1a0ab32f4698e09e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BatchImagesMasksLatentsNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BatchImagesMasksLatentsNode)

[SeedNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SeedNode)[MarkdownNote - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MarkdownNote)

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
