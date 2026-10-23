---
url: https://docs.comfy.org/built-in-nodes/ResolutionBucket/
title: ResolutionBucket - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:51.608677+00:00
---

# ResolutionBucket - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ResolutionBucket/

Training

# ResolutionBucket - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node organizes a list of latent images and their corresponding conditioning data by their resolution.

Copy pageCopy page

This node organizes a list of latent images and their corresponding conditioning data by their resolution. It groups together items that share the same height and width, creating separate batches for each unique resolution. This process is useful for preparing data for efficient training, as it allows models to process multiple items of the same size together.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latents`| List of latent dicts to bucket by resolution.| LATENT| Yes| N/A  
`conditioning`| List of conditioning lists (must match latents length).| CONDITIONING| Yes| N/A  
  
**Note:** Both inputs are list-type inputs, meaning the node receives a list of items for each. The number of items in the `latents` list must exactly match the number of items in the `conditioning` list; if the counts do not match, the node raises an error. Each latent dictionary can contain a batch of samples, and the corresponding conditioning list must contain a matching number of conditioning items for that batch, since each sample in the batch is paired with its own conditioning entry. Latent samples may have a shape of (B, C, H, W) for images or (B, T, C, H, W) for videos; the node groups them by height and width only.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latents`| List of batched latent dicts, one per resolution bucket.| LATENT  
`conditioning`| List of condition lists, one per resolution bucket.| CONDITIONING  
  
**Note:** Both outputs are list-type outputs. Each output list contains one entry per unique resolution (height and width) found in the input, in the order the resolutions were first encountered. Latents within each bucket are stacked along a new batch dimension.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/en.md)

* * *

**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ResolutionBucket.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ResolutionBucket)

[MakeTrainingDataset - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MakeTrainingDataset)[SaveTrainingDataset - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveTrainingDataset)

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
