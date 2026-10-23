---
url: https://docs.comfy.org/built-in-nodes/LoadImageOutput/
title: LoadImageOutput - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:45.226039+00:00
---

# LoadImageOutput - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadImageOutput/

Image

# LoadImageOutput - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LoadImageOutput node loads images from the output folder.

Copy pageCopy page

The LoadImageOutput node loads images from the output folder. When you click the refresh button, it updates the list of available images and automatically selects the first one, making it easy to iterate through your generated images.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Load an image from the output folder. Includes an upload option and refresh button to update the image list. When the refresh button is clicked, the node will update the image list and automatically select the first image, allowing for easy iteration.| COMBO| Yes| Multiple options available  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The loaded image from the output folder| IMAGE  
`mask`| The mask associated with the loaded image| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/en.md)

* * *

**Source fingerprint (SHA-256):** `d1de0140765c9d5dd393715faa84dc5c3f0e49117391b8823a51b176bcb568d8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadImageOutput.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadImageOutput)

[LoadImageMask](https://docs.comfy.org/built-in-nodes/LoadImageMask)[LoadImageSetFromFolderNode](https://docs.comfy.org/built-in-nodes/LoadImageSetFromFolderNode)
