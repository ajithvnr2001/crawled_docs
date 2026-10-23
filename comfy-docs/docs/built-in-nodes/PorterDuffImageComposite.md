---
url: https://docs.comfy.org/built-in-nodes/PorterDuffImageComposite/
title: PorterDuffImageComposite - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:43.795697+00:00
---

# PorterDuffImageComposite - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PorterDuffImageComposite/

Compositing

# PorterDuffImageComposite - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PorterDuffImageComposite node is designed to perform image compositing using the Porter-Duff compositing operators.

Copy pageCopy page

The PorterDuffImageComposite node is designed to perform image compositing using the Porter-Duff compositing operators. It allows for the combination of source and destination images according to various blending modes, enabling the creation of complex visual effects by manipulating image transparency and overlaying images in creative ways.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`source`| The source image tensor to be composited over the destination image. It plays a crucial role in determining the final visual outcome based on the selected compositing mode.| `IMAGE`  
`source_alpha`| The alpha channel of the source image, which specifies the transparency of each pixel in the source image. It affects how the source image blends with the destination image.| `MASK`  
`destination`| The destination image tensor that serves as the backdrop over which the source image is composited. It contributes to the final composited image based on the blending mode.| `IMAGE`  
`destination_alpha`| The alpha channel of the destination image, defining the transparency of the destination image’s pixels. It influences the blending of the source and destination images.| `MASK`  
`mode`| The Porter-Duff compositing mode to apply, which determines how the source and destination images are blended together. Each mode creates different visual effects.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`image`| The composited image resulting from the application of the specified Porter-Duff mode.| `IMAGE`  
`mask`| The alpha channel of the composited image, indicating the transparency of each pixel.| `MASK`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PorterDuffImageComposite.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PorterDuffImageComposite)

[JoinImageWithAlpha - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/JoinImageWithAlpha)[SplitImageWithAlpha - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SplitImageWithAlpha)

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
