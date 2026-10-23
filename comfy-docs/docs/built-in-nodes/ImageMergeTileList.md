---
url: https://docs.comfy.org/built-in-nodes/ImageMergeTileList/
title: ImageMergeTileList - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:09.557614+00:00
---

# ImageMergeTileList - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageMergeTileList/

Batch

# ImageMergeTileList - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node takes a list of image tiles and merges them back into a single, larger image.

Copy pageCopy page

This node takes a list of image tiles and merges them back into a single, larger image. It is designed to reconstruct an image that was previously split into a grid of overlapping tiles, using a weighted blending technique to create a seamless final result.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image_list`| A list of image tiles to be merged. The first tile in the list is used to determine the tile dimensions and data type for the entire process.| IMAGE| Yes| N/A  
`final_width`| The width of the final merged image in pixels (default: 1024).| INT| Yes| 64 - 32768  
`final_height`| The height of the final merged image in pixels (default: 1024).| INT| Yes| 64 - 32768  
`overlap`| The amount of overlap between adjacent tiles in pixels. A value greater than 0 enables a smooth blending effect at the tile seams (default: 128).| INT| Yes| 0 - 4096  
  
**Note:** The `image_list` is a dynamic input list. The node will process tiles in the order they are provided, up to the number required to fill the grid defined by the `final_width`, `final_height`, and the dimensions of the first tile. If the list contains more tiles than needed, the extra tiles are ignored.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The final merged image, reconstructed from the input tiles.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/en.md)

* * *

**Source fingerprint (SHA-256):** `41b570bf758093f3693c015e7976b946b9d93ca56db2bf66617149f259ae8c06`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageMergeTileList.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageMergeTileList)

[ImageGrid - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageGrid)[MergeImageLists - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MergeImageLists)

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
