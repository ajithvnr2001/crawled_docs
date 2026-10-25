---
url: https://docs.comfy.org/built-in-nodes/EmptyLTXVLatentVideo/
title: EmptyLTXVLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:54.814134+00:00
---

# EmptyLTXVLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyLTXVLatentVideo/

Ltxv

# EmptyLTXVLatentVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyLTXVLatentVideo node creates an empty (zero-filled) latent video tensor using the width, height, length, and batch size you specify.

Copy pageCopy page

The EmptyLTXVLatentVideo node creates an empty (zero-filled) latent video tensor using the width, height, length, and batch size you specify. It provides a blank starting point for LTXV video generation workflows, with the latent dimensions automatically compressed relative to the requested video size.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent video tensor (default: 768, step: 32)| INT| Yes| 64 to MAX_RESOLUTION  
`height`| The height of the latent video tensor (default: 512, step: 32)| INT| Yes| 64 to MAX_RESOLUTION  
`length`| The number of frames in the latent video (default: 97, step: 8)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| The number of latent videos to generate in a batch (default: 1)| INT| Yes| 1 to 4096  
  
Note: The latent video is compressed compared to the requested dimensions: the spatial dimensions (width and height) are divided by 32, and the frame count (length) is divided by 8 and rounded up to the nearest whole number. The step values for width, height, and length help keep these divisions even.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| The generated empty latent tensor with zero values in the specified dimensions, along with a spatial downscale ratio of 32| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyLTXVLatentVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyLTXVLatentVideo)

[HunyuanVideo15LatentUpscaleWithModel](https://docs.comfy.org/built-in-nodes/HunyuanVideo15LatentUpscaleWithModel)[LTXVAudioVAEDecode](https://docs.comfy.org/built-in-nodes/LTXVAudioVAEDecode)
