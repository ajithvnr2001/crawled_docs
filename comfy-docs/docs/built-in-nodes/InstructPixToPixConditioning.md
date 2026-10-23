---
url: https://docs.comfy.org/built-in-nodes/InstructPixToPixConditioning/
title: InstructPixToPixConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:12.398810+00:00
---

# InstructPixToPixConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/InstructPixToPixConditioning/

Instructpix2pix

# InstructPixToPixConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The InstructPixToPixConditioning node prepares conditioning data for InstructPix2Pix image editing by combining positive and negative text prompts with image

Copy pageCopy page

The InstructPixToPixConditioning node prepares conditioning data for InstructPix2Pix image editing by combining positive and negative text prompts with image data. It encodes the input image through a VAE into a latent representation and attaches that latent to both the positive and negative conditioning, while also returning a matching empty latent. Image dimensions are automatically cropped to multiples of 8 pixels so the VAE can process them.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning data containing text prompts and settings for desired image characteristics| CONDITIONING| Yes| -  
`negative`| Negative conditioning data containing text prompts and settings for undesired image characteristics| CONDITIONING| Yes| -  
`vae`| VAE model used for encoding input images into latent representations| VAE| Yes| -  
`pixels`| Input image to be processed and encoded into latent space| IMAGE| Yes| -  
  
**Note:** The input image dimensions are automatically adjusted by center-cropping to multiples of 8 pixels in both width and height to ensure compatibility with the VAE encoding process.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning data with the encoded image latent attached as `concat_latent_image`| CONDITIONING  
`negative`| Negative conditioning data with the encoded image latent attached as `concat_latent_image`| CONDITIONING  
`latent`| Latent tensor of zeros with the same dimensions as the encoded image| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/InstructPixToPixConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/InstructPixToPixConditioning)

[TextEncodeHunyuanVideo_ImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TextEncodeHunyuanVideo_ImageToVideo)[TextEncodeJoyImageEdit - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextEncodeJoyImageEdit)

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
