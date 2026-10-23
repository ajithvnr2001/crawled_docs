---
url: https://docs.comfy.org/built-in-nodes/SplitImageWithAlpha/
title: SplitImageWithAlpha - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:03.267519+00:00
---

# SplitImageWithAlpha - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SplitImageWithAlpha/

Compositing

# SplitImageWithAlpha - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SplitImageWithAlpha node is designed to separate the color and alpha components of an image.

Copy pageCopy page

The SplitImageWithAlpha node is designed to separate the color and alpha components of an image. It processes an input image tensor, extracting the RGB channels as the color component and the alpha channel as the transparency component, facilitating operations that require manipulation of these distinct image aspects.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`image`| The ‘image’ parameter represents the input image tensor from which the RGB and alpha channels are to be separated. It is crucial for the operation as it provides the source data for the split.| `IMAGE`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`image`| The ‘image’ output represents the separated RGB channels of the input image, providing the color component without the transparency information.| `IMAGE`  
`mask`| The ‘mask’ output represents the separated alpha channel of the input image, providing the transparency information.| `MASK`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SplitImageWithAlpha.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SplitImageWithAlpha)

[PorterDuffImageComposite - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PorterDuffImageComposite)[DrawBBoxes - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DrawBBoxes)

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
