---
url: https://docs.comfy.org/built-in-nodes/EmptyTrellis2LatentStructure/
title: EmptyTrellis2LatentStructure - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:44.235937+00:00
---

# EmptyTrellis2LatentStructure - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyTrellis2LatentStructure/

Trellis

# EmptyTrellis2LatentStructure - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates an empty latent structure for the Trellis2 model, where all values are set to zero.

Copy pageCopy page

This node creates an empty latent structure for the Trellis2 model, where all values are set to zero. It produces a blank 3D latent tensor with 32 channels at a resolution of 16×16×16, sized for the specified number of items in the batch.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`batch_size`| The number of latent images in the batch (default: 1).| INT| Yes| 1 to 4096  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| An empty Trellis2 latent structure. The samples are a zero-filled tensor with the shape (batch_size, 32, 16, 16, 16), and the latent type is set to “trellis2”.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/en.md)

* * *

**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyTrellis2LatentStructure.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyTrellis2LatentStructure)

[LatentRotate](https://docs.comfy.org/built-in-nodes/LatentRotate)[VaeDecodeShapeTrellis](https://docs.comfy.org/built-in-nodes/VaeDecodeShapeTrellis)
