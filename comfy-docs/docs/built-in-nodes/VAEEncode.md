---
url: https://docs.comfy.org/built-in-nodes/VAEEncode/
title: VAEEncode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:53.035616+00:00
---

# VAEEncode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEEncode/

Latent

# VAEEncode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed for encoding images into a latent space representation using a specified VAE model.

Copy pageCopy page

This node is designed for encoding images into a latent space representation using a specified VAE model. It abstracts the complexity of the encoding process, providing a straightforward way to transform images into their latent representations.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`pixels`| The ‘pixels’ parameter represents the image data to be encoded into the latent space. It plays a crucial role in determining the output latent representation by serving as the direct input for the encoding process.| `IMAGE`  
`vae`| The ‘vae’ parameter specifies the Variational Autoencoder model to be used for encoding the image data into latent space. It is essential for defining the encoding mechanism and characteristics of the generated latent representation.| VAE  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output is a latent space representation of the input image, encapsulating its essential features in a compressed form.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEEncode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEEncode)

[VAEDecodeTiled](https://docs.comfy.org/built-in-nodes/VAEDecodeTiled)[VAEEncodeAudio](https://docs.comfy.org/built-in-nodes/VAEEncodeAudio)
