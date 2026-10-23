---
url: https://docs.comfy.org/built-in-nodes/ResizeAndPadImage/
title: ResizeAndPadImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:51.700424+00:00
---

# ResizeAndPadImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ResizeAndPadImage/

Transform

# ResizeAndPadImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ResizeAndPadImage node resizes an image to fit within specified dimensions while maintaining its original aspect ratio.

Copy pageCopy page

The ResizeAndPadImage node resizes an image to fit within specified dimensions while maintaining its original aspect ratio. It scales the image down proportionally to fit within the target width and height, then adds padding around the edges to fill any remaining space. The padding color and interpolation method can be customized to control the appearance of the padded areas and the quality of the resizing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be resized and padded| IMAGE| Yes| -  
`target_width`| The desired width of the output image (default: 512)| INT| Yes| 1 to MAX_RESOLUTION  
`target_height`| The desired height of the output image (default: 512)| INT| Yes| 1 to MAX_RESOLUTION  
`padding_color`| The color to use for padding areas around the resized image (default: “white”)| COMBO| Yes| ”white"  
"black”  
`interpolation`| The interpolation method used for resizing the image (default: “area”)| COMBO| Yes| ”area"  
"bicubic"  
"nearest-exact"  
"bilinear"  
"lanczos”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resized and padded output image| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/en.md)

* * *

**Source fingerprint (SHA-256):** `cc516caee9f466d557e1c8e3c7fcef25acc1e33d181bc4b100302dc93530cb95`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ResizeAndPadImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ResizeAndPadImage)

[RandomCropImages - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RandomCropImages)[ResizeImagesByLongerEdge - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ResizeImagesByLongerEdge)

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
