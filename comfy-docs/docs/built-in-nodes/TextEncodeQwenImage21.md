---
url: https://docs.comfy.org/built-in-nodes/TextEncodeQwenImage21/
title: TextEncodeQwenImage21 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:09.525380+00:00
---

# TextEncodeQwenImage21 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeQwenImage21/

Qwen Image

# TextEncodeQwenImage21 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TextEncodeQwenImage21 node encodes a prompt and a negative prompt for the Qwen-Image 2.1 model, optionally attaching reference images.

Copy pageCopy page

The TextEncodeQwenImage21 node encodes a prompt and a negative prompt for the Qwen-Image 2.1 model, optionally attaching reference images. Reference images are seen by the text encoder and, when a VAE is connected, are also encoded as latents that are spliced into the sequence, so the conditioning carries both the text instruction and the visual reference. The node returns positive and negative conditioning together with an empty latent sized to the first reference image, ready to be sampled.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The Qwen-Image 2.1 text encoder used to tokenize and encode the prompts.| CLIP| Yes| -  
`prompt`| Text prompt describing the image to generate or the edit to apply. Supports multiline input and dynamic prompts.| STRING| Yes| Any text  
`negative_prompt`| Text prompt describing what the result should avoid. Supports multiline input and dynamic prompts.| STRING| Yes| Any text  
`vae`| VAE used to encode the reference images into reference latents. When omitted, the reference images condition the result through the text encoder only.| VAE| No| -  
`resolution`| Reference images are resized to about `resolution` x `resolution` pixels, at multiples of 32, preserving aspect ratio. 0 keeps each reference at its own size, rounded to a multiple of 32 (default: 1024).| INT| Yes| 0 to 4096 (step 32)  
`images`| Reference images, seen by the text encoder and spliced into the sequence as VAE latents. Growable slot: connect up to 16 images (`image_1` … `image_16`).| IMAGE| No| 0 to 16 images  
  
The empty latent output is sized to the first connected reference image, or to `resolution` when no reference image is connected. Sample at the latent this node returns: any other size shifts the edit. When a VAE is connected, the same reference latents are attached to both the positive and the negative conditioning, so a single sampler step can denoise both.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Encoded conditioning for the prompt, carrying the reference latents when a VAE is connected.| CONDITIONING  
`negative`| Encoded conditioning for the negative prompt, with the same reference latents.| CONDITIONING  
`latent`| Empty latent on the first reference image’s size, or 1024 x 1024 when no reference image is connected.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImage21/en.md)

* * *

**Source fingerprint (SHA-256):** `3870f04597d12b593498c12ca139428af2d717b65aa40c889de9373ae9eb475e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeQwenImage21.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeQwenImage21)

[QwenImage21Cache - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/QwenImage21Cache)[TextEncodeQwenImageEdit - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextEncodeQwenImageEdit)

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
