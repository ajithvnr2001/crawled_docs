---
url: https://docs.comfy.org/built-in-nodes/SolidMask/
title: SolidMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:53.111278+00:00
---

# SolidMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SolidMask/

Mask

# SolidMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SolidMask node generates a uniform mask with a specified value across its entire area.

Copy pageCopy page

The SolidMask node generates a uniform mask with a specified value across its entire area. It’s designed to create masks of specific dimensions and intensity, useful in various image processing and masking tasks.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`value`| Specifies the intensity value of the mask, affecting its overall appearance and utility in subsequent operations.| FLOAT  
`width`| Determines the width of the generated mask, directly influencing its size and aspect ratio.| INT  
`height`| Sets the height of the generated mask, affecting its size and aspect ratio.| INT  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`mask`| Outputs a uniform mask with the specified dimensions and value.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SolidMask/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SolidMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SolidMask)

[MaskToImage](https://docs.comfy.org/built-in-nodes/MaskToImage)[ThresholdMask](https://docs.comfy.org/built-in-nodes/ThresholdMask)
