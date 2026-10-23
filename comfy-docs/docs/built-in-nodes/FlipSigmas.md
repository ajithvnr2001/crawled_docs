---
url: https://docs.comfy.org/built-in-nodes/FlipSigmas/
title: FlipSigmas - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.869823+00:00
---

# FlipSigmas - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FlipSigmas/

Sigmas

# FlipSigmas - ComfyUI Built-in Node Documentation

Copy pageCopy page

The FlipSigmas node is designed to manipulate the sequence of sigma values used in diffusion models by reversing their order and ensuring the first value

Copy pageCopy page

The `FlipSigmas` node is designed to manipulate the sequence of sigma values used in diffusion models by reversing their order and ensuring the first value is non-zero if originally zero. This operation is crucial for adapting the noise levels in reverse order, facilitating the generation process in models that operate by gradually reducing noise from data.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`sigmas`| The ‘sigmas’ parameter represents the sequence of sigma values to be flipped. This sequence is crucial for controlling the noise levels applied during the diffusion process, and flipping it is essential for the reverse generation process.| `SIGMAS`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`sigmas`| The output is the modified sequence of sigma values, flipped and adjusted to ensure the first value is non-zero if originally zero, ready for use in subsequent diffusion model operations.| `SIGMAS`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FlipSigmas/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FlipSigmas.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FlipSigmas)

[ExtendIntermediateSigmas - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ExtendIntermediateSigmas)[ManualSigmas - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ManualSigmas)

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
