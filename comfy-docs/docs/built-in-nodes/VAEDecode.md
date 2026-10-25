---
url: https://docs.comfy.org/built-in-nodes/VAEDecode/
title: VAEDecode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:52.996545+00:00
---

# VAEDecode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEDecode/

Latent

# VAEDecode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VAEDecode node is designed for decoding latent representations into images using a specified Variational Autoencoder (VAE).

Copy pageCopy page

The VAEDecode node is designed for decoding latent representations into images using a specified Variational Autoencoder (VAE). It serves the purpose of generating images from compressed data representations, facilitating the reconstruction of images from their latent space encodings.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`samples`| The ‘samples’ parameter represents the latent representations to be decoded into images. It is crucial for the decoding process as it provides the compressed data from which the images are reconstructed.| `LATENT`  
`vae`| The ‘vae’ parameter specifies the Variational Autoencoder model to be used for decoding the latent representations into images. It is essential for determining the decoding mechanism and the quality of the reconstructed images.| VAE  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`image`| The output is an image reconstructed from the provided latent representation using the specified VAE model.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEDecode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEDecode)

[TrimVideoLatent](https://docs.comfy.org/built-in-nodes/TrimVideoLatent)[VAEDecodeAudio](https://docs.comfy.org/built-in-nodes/VAEDecodeAudio)
