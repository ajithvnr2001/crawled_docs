---
url: https://docs.comfy.org/built-in-nodes/MakeTrainingDataset/
title: MakeTrainingDataset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:29.034061+00:00
---

# MakeTrainingDataset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MakeTrainingDataset/

Training

# MakeTrainingDataset - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node prepares data for training by encoding images and text.

Copy pageCopy page

This node prepares data for training by encoding images and text. It takes a list of images and a corresponding list of text captions, then uses a VAE model to convert the images into latent representations and a CLIP model to convert the text into conditioning data. The resulting paired latents and conditioning are output as lists, ready for use in training workflows.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| List of images to encode.| IMAGE| Yes| N/A  
`vae`| VAE model for encoding images to latents.| VAE| Yes| N/A  
`clip`| CLIP model for encoding text to conditioning.| CLIP| Yes| N/A  
`texts`| List of text captions. Can be length n (matching images), 1 (repeated for all), or omitted (uses empty string).| STRING| No| 0, 1, or n items (n = number of images)  
  
**Parameter Constraints:**

  * This node uses list inputs: `images` and `texts` are processed as lists, while `vae` and `clip` accept a single model each (the first item of the supplied list is used).
  * The number of items in the `texts` list must be 0, 1, or exactly match the number of items in the `images` list. If it is 0 or omitted, an empty string is used for all images. If it is 1, that single text is repeated for all images. Any other length raises an error.
  * The output `latents` and `conditioning` lists always contain the same number of items as the `images` list, so each latent is paired with the conditioning for its corresponding caption.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latents`| List of latent dicts.| LATENT  
`conditioning`| List of conditioning lists.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/en.md)

* * *

**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MakeTrainingDataset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MakeTrainingDataset)

[LossGraphNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LossGraphNode)[ResolutionBucket - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ResolutionBucket)

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
