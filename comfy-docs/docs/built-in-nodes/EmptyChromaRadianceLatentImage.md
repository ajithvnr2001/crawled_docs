---
url: https://docs.comfy.org/built-in-nodes/EmptyChromaRadianceLatentImage/
title: EmptyChromaRadianceLatentImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:53.841714+00:00
---

# EmptyChromaRadianceLatentImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyChromaRadianceLatentImage/

Chroma Radiance

# EmptyChromaRadianceLatentImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyChromaRadianceLatentImage node creates a blank latent image with the dimensions you specify, for use in chroma radiance workflows.

Copy pageCopy page

The EmptyChromaRadianceLatentImage node creates a blank latent image with the dimensions you specify, for use in chroma radiance workflows. It produces a tensor filled with zeros that acts as the starting point for latent space operations, letting you define the width, height, and batch size of the empty latent image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent image in pixels (default: 1024)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| The height of the latent image in pixels (default: 1024)| INT| Yes| 16 to MAX_RESOLUTION  
`batch_size`| The number of latent images to generate in a batch (default: 1)| INT| Yes| 1 to 4096  
  
Note: `width` and `height` are defined with a step of 16, so the values are adjusted in multiples of 16.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| The generated empty latent image tensor filled with zeros, with the shape batch_size x 3 x height x width| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/en.md)

* * *

**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyChromaRadianceLatentImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyChromaRadianceLatentImage)

[ReplaceVideoLatentFrames](https://docs.comfy.org/built-in-nodes/ReplaceVideoLatentFrames)[EmptyCosmosLatentVideo](https://docs.comfy.org/built-in-nodes/EmptyCosmosLatentVideo)
