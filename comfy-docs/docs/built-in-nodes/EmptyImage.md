---
url: https://docs.comfy.org/built-in-nodes/EmptyImage/
title: EmptyImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:26.906448+00:00
---

# EmptyImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyImage/

Image

# EmptyImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyImage node is used to create blank images with specified dimensions and colors.

Copy pageCopy page

## 

​

Function Description

The EmptyImage node is used to create blank images with specified dimensions and colors. It can generate solid-color background images, commonly used as starting points or background images for image processing workflows.

## 

​

Working Principle

Just like a painter preparing a blank canvas before starting to create, the EmptyImage node provides you with a “digital canvas”. You can specify the canvas size (width and height), choose the base color of the canvas, and even prepare multiple canvases of the same specifications at once. This node is like an intelligent art supply store that can create standardized canvases that perfectly meet your size and color requirements.

## 

​

Inputs

Parameter Name| Description| Data Type  
---|---|---  
`width`| Sets the width of the generated image (in pixels), determining the horizontal dimensions of the canvas| INT  
`height`| Sets the height of the generated image (in pixels), determining the vertical dimensions of the canvas| INT  
`batch_size`| The number of images to generate at once, used for batch creation of images with the same specifications| INT  
`color`| The background color of the image. You can input hexadecimal color settings, which will be automatically converted to decimal| INT  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated blank image tensor, formatted as [batch_size, height, width, 3], containing RGB three color channels| IMAGE  
  
## 

​

Common Color Reference Values

Since the current color input for this node is not user-friendly, with all color values being converted to decimal, here are some common color values that can be used directly for quick application.

Color Name| Hexadecimal Value  
---|---  
Black| 0x000000  
White| 0xFFFFFF  
Red| 0xFF0000  
Green| 0x00FF00  
Blue| 0x0000FF  
Yellow| 0xFFFF00  
Cyan| 0x00FFFF  
Magenta| 0xFF00FF  
Orange| 0xFF8000  
Purple| 0x8000FF  
Pink| 0xFF80C0  
Brown| 0x8B4513  
Dark Gray| 0x404040  
Light Gray| 0xC0C0C0  
Navy Blue| 0x000080  
Dark Green| 0x008000  
Dark Red| 0x800000  
Gold| 0xFFD700  
Silver| 0xC0C0C0  
Beige| 0xF5F5DC  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyImage/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyImage)

[ConditioningCombine - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningCombine)[GetImageSize - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GetImageSize)

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
