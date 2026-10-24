---
url: https://docs.comfy.org/built-in-nodes/RecraftVectorizeImageNode/
title: RecraftVectorizeImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:51.569291+00:00
---

# RecraftVectorizeImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftVectorizeImageNode/

Recraft

# RecraftVectorizeImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates SVG vector graphics from an input image.

Copy pageCopy page

Generates SVG vector graphics from an input image. This node converts raster images into scalable vector format by sending each image to the Recraft API and combining the results into a single SVG output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to convert to SVG format. Supports batch processing of multiple images.| IMAGE| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SVG`| The generated vector graphics output combining all processed images into a single SVG document.| SVG  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `bda74d9f11cc79217c61ecb8ba597a671133baa4380386428c4d9e9b68006713`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftVectorizeImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftVectorizeImageNode)

[RecraftV4TextToVectorNode](https://docs.comfy.org/built-in-nodes/RecraftV4TextToVectorNode)[ReveImageCreateNode](https://docs.comfy.org/built-in-nodes/ReveImageCreateNode)
