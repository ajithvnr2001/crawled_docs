---
url: https://docs.comfy.org/built-in-nodes/TextEncodeBooguEdit/
title: TextEncodeBooguEdit - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:08.706088+00:00
---

# TextEncodeBooguEdit - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeBooguEdit/

Boogu

# TextEncodeBooguEdit - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node prepares conditioning for image editing with Boogu.

Copy pageCopy page

This node prepares conditioning for image editing with Boogu. It processes reference images to create both positive and negative conditioning outputs. The reference image is used twice: vision tokens from the image are added only to the positive conditioning to amplify the edit instruction, while a VAE reference latent is added to both positive and negative conditioning so it cancels out under CFG, preserving the original image identity; the tokenizer automatically selects the appropriate system prompt based on the presence of images and empty negative prompts.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used for text encoding| CLIP| Yes|   
`prompt`| The text prompt describing the desired edit. Supports multiline text and dynamic prompts.| STRING| Yes|   
`negative_prompt`| The text prompt describing what to avoid in the edit. Can be left empty to drop negative conditioning. Advanced parameter.| STRING| Yes|   
`vae`| The VAE model used to encode reference images into latent space. Needed to add reference latents to the conditioning outputs.| VAE| No|   
`images`| Reference image(s) to edit. Boogu focuses on one reference per sample; more are allowed.| IMAGE| No| Up to 16 images  
  
Reference latents are added to both conditioning outputs only when `vae` is provided together with at least one reference `image`. If `vae` is omitted, the positive output still receives vision tokens from the reference images, but neither output includes reference latents.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Conditioning containing both the text prompt with vision tokens and the reference latents| CONDITIONING  
`negative`| Conditioning containing the negative text prompt and the reference latents| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/en.md)

* * *

**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeBooguEdit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeBooguEdit)

[BerniniConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BerniniConditioning)[ControlNetApply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ControlNetApply)

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
