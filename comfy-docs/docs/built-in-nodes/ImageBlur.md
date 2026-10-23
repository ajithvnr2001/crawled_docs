---
url: https://docs.comfy.org/built-in-nodes/ImageBlur/
title: ImageBlur - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:07.327175+00:00
---

# ImageBlur - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageBlur/

Filters

# ImageBlur - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageBlur node applies a Gaussian blur to an image, allowing for the softening of edges and reduction of detail and noise.

Copy pageCopy page

The `ImageBlur` node applies a Gaussian blur to an image, allowing for the softening of edges and reduction of detail and noise. It provides control over the intensity and spread of the blur through parameters.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`image`| The input image to be blurred. This is the primary target for the blur effect.| `IMAGE`  
`blur_radius`| Determines the radius of the blur effect. A larger radius results in a more pronounced blur.| `INT`  
`sigma`| Controls the spread of the blur. A higher sigma value means the blur will affect a wider area around each pixel.| `FLOAT`  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`image`| The output is the blurred version of the input image, with the degree of blur determined by the input parameters.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageBlur.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageBlur)

[ImageBlend - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageBlend)[ImageQuantize - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageQuantize)

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
