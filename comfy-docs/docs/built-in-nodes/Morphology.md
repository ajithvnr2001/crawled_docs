---
url: https://docs.comfy.org/built-in-nodes/Morphology/
title: Morphology - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:38.317276+00:00
---

# Morphology - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Morphology/

Filters

# Morphology - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Morphology node applies various morphological operations to images, which are mathematical operations used to process and analyze shapes in images.

Copy pageCopy page

The Morphology node applies various morphological operations to images, which are mathematical operations used to process and analyze shapes in images. It can perform operations like erosion, dilation, opening, closing, and more using a customizable kernel size to control the effect strength.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to process| IMAGE| Yes| -  
`operation`| The morphological operation to apply (default: “erode”)| STRING| Yes| `"erode"`  
`"dilate"`  
`"open"`  
`"close"`  
`"gradient"`  
`"bottom_hat"`  
`"top_hat"`  
`kernel_size`| The size of the structuring element kernel (default: 3). Must be an odd number.| INT| Yes| 3-999  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The processed image after applying the morphological operation| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/en.md)

* * *

**Source fingerprint (SHA-256):** `ea596f8d30975f153fccbc5651eec0fbbf308ef1c616313d996c200cddf748e3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Morphology.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Morphology)

[ImageSharpen - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageSharpen)[DA3GeometryToMesh - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DA3GeometryToMesh)

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
