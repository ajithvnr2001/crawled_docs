---
url: https://docs.comfy.org/built-in-nodes/ImageColorToMask/
title: ImageColorToMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:07.585546+00:00
---

# ImageColorToMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageColorToMask/

Mask

# ImageColorToMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageColorToMask node is designed to convert a specified color in an image to a mask.

Copy pageCopy page

The `ImageColorToMask` node is designed to convert a specified color in an image to a mask. It processes an image and a target color, generating a mask where the specified color is highlighted, facilitating operations like color-based segmentation or object isolation.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`image`| The ‘image’ parameter represents the input image to be processed. It is crucial for determining the areas of the image that match the specified color to be converted into a mask.| `IMAGE`  
`color`| The ‘color’ parameter specifies the target color in the image to be converted into a mask. It plays a key role in identifying the specific color areas to be highlighted in the resulting mask.| `INT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`mask`| The output is a mask highlighting the areas of the input image that match the specified color. This mask can be used for further image processing tasks, such as segmentation or object isolation.| `MASK`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorToMask/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageColorToMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageColorToMask)

[GrowMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GrowMask)[ImageToMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageToMask)

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
