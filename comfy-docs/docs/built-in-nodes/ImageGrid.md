---
url: https://docs.comfy.org/built-in-nodes/ImageGrid/
title: ImageGrid - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.382333+00:00
---

# ImageGrid - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageGrid/

Batch

# ImageGrid - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Image Grid node combines multiple images into a single, organized grid or collage.

Copy pageCopy page

The Image Grid node combines multiple images into a single, organized grid or collage. It takes a list of images and arranges them into a specified number of columns, resizing each image to fit a defined cell size and adding optional padding between them. The result is a single, new image containing all the input images in a grid layout.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| A list of images to be arranged into the grid. The node requires at least one image to function.| IMAGE| Yes| -  
`columns`| The number of columns in the grid (default: 4).| INT| No| 1 - 20  
`cell_width`| The width, in pixels, of each cell in the grid (default: 256).| INT| No| 32 - 2048  
`cell_height`| The height, in pixels, of each cell in the grid (default: 256).| INT| No| 32 - 2048  
`padding`| The amount of padding, in pixels, to place between images in the grid (default: 4).| INT| No| 0 - 50  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The single output image containing all the input images arranged in a grid.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/en.md)

* * *

**Source fingerprint (SHA-256):** `87bc0af8af33a0fd703f13fec782075502c9562847fa3887a2273afa5b28c47e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageGrid.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageGrid)

[ImageFromBatch - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageFromBatch)[ImageMergeTileList - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageMergeTileList)

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
