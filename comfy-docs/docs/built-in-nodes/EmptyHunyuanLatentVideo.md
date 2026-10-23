---
url: https://docs.comfy.org/built-in-nodes/EmptyHunyuanLatentVideo/
title: EmptyHunyuanLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:52.765723+00:00
---

# EmptyHunyuanLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyHunyuanLatentVideo/

Hunyuan Video

# EmptyHunyuanLatentVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyHunyuanLatentVideo node is similar to the EmptyLatentImage node.

Copy pageCopy page

The `EmptyHunyuanLatentVideo` node is similar to the `EmptyLatentImage` node. You can consider it as a blank canvas for video generation, where width, height, and length define the properties of the canvas, and the batch size determines the number of canvases to create. This node creates empty canvases ready for subsequent video generation tasks.

## 

​

Inputs

Parameter| Description| Comfy Type  
---|---|---  
`width`| Video width, default 848, minimum 16, maximum `nodes.MAX_RESOLUTION`, step size 16.| `INT`  
`height`| Video height, default 480, minimum 16, maximum `nodes.MAX_RESOLUTION`, step size 16.| `INT`  
`length`| Video length, default 25, minimum 1, maximum `nodes.MAX_RESOLUTION`, step size 4.| `INT`  
`batch_size`| Batch size, default 1, minimum 1, maximum 4096.| `INT`  
  
## 

​

Outputs

Parameter| Description| Comfy Type  
---|---|---  
`samples`| Generated latent video samples containing zero tensors, ready for processing and generation tasks.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyHunyuanLatentVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyHunyuanLatentVideo)

[EmptyHunyuanImageLatent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyHunyuanImageLatent)[EmptyHunyuanVideo15Latent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyHunyuanVideo15Latent)

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
