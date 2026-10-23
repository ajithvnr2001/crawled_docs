---
url: https://docs.comfy.org/built-in-nodes/HunyuanVideo15SuperResolution/
title: HunyuanVideo15SuperResolution - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:05.487325+00:00
---

# HunyuanVideo15SuperResolution - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HunyuanVideo15SuperResolution/

Hunyuan Video

# HunyuanVideo15SuperResolution - ComfyUI Built-in Node Documentation

Copy pageCopy page

The HunyuanVideo15SuperResolution node prepares conditioning data for a video super-resolution process.

Copy pageCopy page

The HunyuanVideo15SuperResolution node prepares conditioning data for a video super-resolution process. It takes a latent representation of a video and, optionally, a starting image, and packages them along with noise augmentation and CLIP vision data into a format that can be used by a model to generate a higher-resolution output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning input to be modified with latent and augmentation data.| CONDITIONING| Yes| N/A  
`negative`| The negative conditioning input to be modified with latent and augmentation data.| CONDITIONING| Yes| N/A  
`vae`| The VAE used to encode the optional `start_image`. Required if `start_image` is provided.| VAE| No| N/A  
`start_image`| An optional starting image to guide the super-resolution. If provided, it is upscaled and encoded into the conditioning latent.| IMAGE| No| N/A  
`clip_vision_output`| Optional CLIP vision embeddings to add to the conditioning.| CLIP_VISION_OUTPUT| No| N/A  
`latent`| The input latent video representation that is incorporated into the conditioning.| LATENT| Yes| N/A  
`noise_augmentation`| The strength of noise augmentation to apply to the conditioning (default: 0.70). This is an advanced parameter; a value is always supplied by the default.| FLOAT| Yes| 0.0 - 1.0 (step 0.01)  
  
**Note:** If you provide a `start_image`, you must also connect a `vae` so it can be encoded. The `start_image` is automatically upscaled to 16 times the spatial dimensions (width and height) of the input `latent`, then encoded and placed into the conditioning latent. Only the RGB channels of the `start_image` are used for encoding.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The modified positive conditioning, now containing the concatenated latent, noise augmentation, and optional CLIP vision data.| CONDITIONING  
`negative`| The modified negative conditioning, now containing the concatenated latent, noise augmentation, and optional CLIP vision data.| CONDITIONING  
`latent`| The input latent is passed through unchanged.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/en.md)

* * *

**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HunyuanVideo15SuperResolution.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HunyuanVideo15SuperResolution)

[HunyuanVideo15ImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HunyuanVideo15ImageToVideo)[TextEncodeHunyuanVideo_ImageToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextEncodeHunyuanVideo_ImageToVideo)

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
