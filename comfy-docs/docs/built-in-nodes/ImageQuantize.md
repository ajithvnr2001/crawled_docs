---
url: https://docs.comfy.org/built-in-nodes/ImageQuantize/
title: ImageQuantize - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:50.637200+00:00
---

# ImageQuantize - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageQuantize/

Filters

# ImageQuantize - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageQuantize node is designed to reduce the number of colors in an image to a specified number

Copy pageCopy page

The ImageQuantize node is designed to reduce the number of colors in an image to a specified number, optionally applying dithering techniques to maintain visual quality. This process is useful for creating palette-based images or reducing the color complexity for certain applications.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`image`| The input image tensor to be quantized. It affects the node’s execution by being the primary data upon which color reduction is performed.| `IMAGE`  
`colors`| Specifies the number of colors to reduce the image to. It directly influences the quantization process by determining the color palette size.| `INT`  
`dither`| Determines the dithering technique to be applied during quantization, affecting the visual quality and appearance of the output image.| COMBO[STRING]  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`image`| The quantized version of the input image, with reduced color complexity and optionally dithered to maintain visual quality.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageQuantize.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageQuantize)

[ImageBlur](https://docs.comfy.org/built-in-nodes/ImageBlur)[ImageSharpen](https://docs.comfy.org/built-in-nodes/ImageSharpen)
