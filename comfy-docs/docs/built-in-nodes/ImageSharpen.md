---
url: https://docs.comfy.org/built-in-nodes/ImageSharpen/
title: ImageSharpen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:11.492098+00:00
---

# ImageSharpen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageSharpen/

Filters

# ImageSharpen - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageSharpen node enhances the clarity of an image by accentuating its edges and details.

Copy pageCopy page

The ImageSharpen node enhances the clarity of an image by accentuating its edges and details. It applies a sharpening filter to the image, which can be adjusted in intensity and radius, thereby making the image appear more defined and crisp.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`image`| The input image to be sharpened. This parameter is crucial as it determines the base image on which the sharpening effect will be applied.| `IMAGE`  
`sharpen_radius`| Defines the radius of the sharpening effect. A larger radius means that more pixels around the edge will be affected, leading to a more pronounced sharpening effect.| `INT`  
`sigma`| Controls the spread of the sharpening effect. A higher sigma value results in a smoother transition at the edges, while a lower sigma makes the sharpening more localized.| `FLOAT`  
`alpha`| Adjusts the intensity of the sharpening effect. Higher alpha values result in a stronger sharpening effect.| `FLOAT`  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`image`| The sharpened image, with enhanced edges and details, ready for further processing or display.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageSharpen.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageSharpen)

[ImageQuantize - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageQuantize)[Morphology - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Morphology)

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
