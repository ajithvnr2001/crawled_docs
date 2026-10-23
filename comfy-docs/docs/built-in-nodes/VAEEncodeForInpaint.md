---
url: https://docs.comfy.org/built-in-nodes/VAEEncodeForInpaint/
title: VAEEncodeForInpaint - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:17.040895+00:00
---

# VAEEncodeForInpaint - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEEncodeForInpaint/

Latent

# VAEEncodeForInpaint - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed for encoding images into a latent representation suitable for inpainting tasks

Copy pageCopy page

This node is designed for encoding images into a latent representation suitable for inpainting tasks, incorporating additional preprocessing steps to adjust the input image and mask for optimal encoding by the VAE model.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`pixels`| The input image to be encoded. This image undergoes preprocessing and resizing to match the VAE model’s expected input dimensions before encoding.| `IMAGE`  
`vae`| The VAE model used for encoding the image into its latent representation. It plays a crucial role in the transformation process, determining the quality and characteristics of the output latent space.| VAE  
`mask`| A mask indicating the regions of the input image to be inpainted. It is used to modify the image before encoding, ensuring that the VAE focuses on the relevant areas.| `MASK`  
`grow_mask_by`| Specifies how much to expand the inpainting mask to ensure seamless transitions in the latent space. A larger value increases the area affected by inpainting.| `INT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output includes the encoded latent representation of the image and a noise mask, both crucial for subsequent inpainting tasks.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeEncodeForInpaint/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEEncodeForInpaint.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEEncodeForInpaint)

[VAEEncodeAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEEncodeAudio)[VAEEncodeTiled - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAEEncodeTiled)

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
