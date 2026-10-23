---
url: https://docs.comfy.org/built-in-nodes/EmptyLatentImage/
title: EmptyLatentImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:53.591137+00:00
---

# EmptyLatentImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyLatentImage/

Latent

# EmptyLatentImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyLatentImage node is designed to generate a blank latent space representation with specified dimensions and batch size.

Copy pageCopy page

The `EmptyLatentImage` node is designed to generate a blank latent space representation with specified dimensions and batch size. This node serves as a foundational step in generating or manipulating images in latent space, providing a starting point for further image synthesis or modification processes.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`width`| Specifies the width of the latent image to be generated. This parameter directly influences the spatial dimensions of the resulting latent representation.| `INT`  
`height`| Determines the height of the latent image to be generated. This parameter is crucial for defining the spatial dimensions of the latent space representation.| `INT`  
`batch_size`| Controls the number of latent images to be generated in a single batch. This allows for the generation of multiple latent representations simultaneously, facilitating batch processing.| `INT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output is a tensor representing a batch of blank latent images, serving as a base for further image generation or manipulation in latent space.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyLatentImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyLatentImage)

[EmptyLatentAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyLatentAudio)[GetAudioLatentSize - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GetAudioLatentSize)

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
