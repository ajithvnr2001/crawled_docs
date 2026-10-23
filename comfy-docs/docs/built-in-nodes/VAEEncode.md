---
url: https://docs.comfy.org/built-in-nodes/VAEEncode/
title: VAEEncode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:17.144521+00:00
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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeEncode/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEEncode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEEncode)

[VAEDecodeTiled - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEDecodeTiled)[VAEEncodeAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAEEncodeAudio)

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
