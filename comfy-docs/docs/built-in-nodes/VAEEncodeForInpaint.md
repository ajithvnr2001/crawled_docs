---
url: https://docs.comfy.org/built-in-nodes/VAEEncodeForInpaint/
title: VAEEncodeForInpaint - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:53.118596+00:00
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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeForInpaint/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEEncodeForInpaint.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEEncodeForInpaint)

[VAEEncodeAudio](https://docs.comfy.org/built-in-nodes/VAEEncodeAudio)[VAEEncodeTiled](https://docs.comfy.org/built-in-nodes/VAEEncodeTiled)
