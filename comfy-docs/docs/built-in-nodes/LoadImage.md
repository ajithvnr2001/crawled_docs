---
url: https://docs.comfy.org/built-in-nodes/LoadImage/
title: LoadImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:23.059799+00:00
---

# LoadImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadImage/

Image

# LoadImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LoadImage node is designed to load and preprocess images from a specified path.

Copy pageCopy page

The LoadImage node is designed to load and preprocess images from a specified path. It handles image formats with multiple frames, applies necessary transformations such as rotation based on EXIF data, normalizes pixel values, and optionally generates a mask for images with an alpha channel. This node is essential for preparing images for further processing or analysis within a pipeline.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`image`| The ‘image’ parameter specifies the identifier of the image to be loaded and processed. It is crucial for determining the path to the image file and subsequently loading the image for transformation and normalization.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`image`| The processed image, with pixel values normalized and transformations applied as necessary. It is ready for further processing or analysis.| `IMAGE`  
`mask`| An optional output providing a mask for the image, useful in scenarios where the image includes an alpha channel for transparency.| `MASK`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadImage)

[LayersFromBoundingBoxes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LayersFromBoundingBoxes)[LoadImageDataSetFromFolder - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadImageDataSetFromFolder)

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
