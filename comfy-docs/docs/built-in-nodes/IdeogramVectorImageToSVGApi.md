---
url: https://docs.comfy.org/built-in-nodes/IdeogramVectorImageToSVGApi/
title: IdeogramVectorImageToSVGApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:47.228239+00:00
---

# IdeogramVectorImageToSVGApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/IdeogramVectorImageToSVGApi/

Image

# IdeogramVectorImageToSVGApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts an image into an editable SVG with Ideogram Vector.

Copy pageCopy page

This node converts an image into an editable SVG with Ideogram Vector. The result is vector markup rather than a raster image, so the traced shapes stay editable in a vector editor. Transparent areas of an image with alpha stay transparent.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use. Default: `"ideogram-vector-1"`.| DYNAMIC_COMBO| Yes| `"ideogram-vector-1"`  
`image`| The image to convert. A batched input is converted image by image and the resulting SVGs are returned together.| IMAGE| Yes| -  
`mode`| `"simple"` traces fewer, larger shapes; `"default"` keeps finer detail. Default: `"default"`.| COMBO| Yes| `"simple"`  
`"default"`  
  
**Constraints:**

  * Images whose longest side is above 2048 pixels are downscaled before upload.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SVG`| The converted image as editable vector markup.| SVG  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorImageToSVGApi/en.md)

* * *

**Source fingerprint (SHA-256):** `6553291e9d887b31485b9cbf8f6ced4186470eb47e8621ebb0f4e5df6542123e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/IdeogramVectorImageToSVGApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/IdeogramVectorImageToSVGApi)

[IdeogramVectorGenerateApi](https://docs.comfy.org/built-in-nodes/IdeogramVectorGenerateApi)[ClaudeNode](https://docs.comfy.org/built-in-nodes/ClaudeNode)
