---
url: https://docs.comfy.org/built-in-nodes/ModelSamplingFlux/
title: ModelSamplingFlux - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:21.353968+00:00
---

# ModelSamplingFlux - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelSamplingFlux/

FLUX

# ModelSamplingFlux - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelSamplingFlux node applies Flux model sampling to a given model by calculating a shift parameter based on image dimensions.

Copy pageCopy page

The ModelSamplingFlux node applies Flux model sampling to a given model by calculating a shift parameter based on image dimensions. It creates a specialized sampling configuration that adjusts the model’s behavior according to the specified width, height, and shift parameters, then returns the modified model with the new sampling settings applied.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply Flux sampling to| MODEL| Yes| -  
`max_shift`| Maximum shift value for sampling calculation (default: 1.15)| FLOAT| Yes| 0.0 - 100.0 (step 0.01)  
`base_shift`| Base shift value for sampling calculation (default: 0.5)| FLOAT| Yes| 0.0 - 100.0 (step 0.01)  
`width`| Width of the target image in pixels (default: 1024)| INT| Yes| 16 - MAX_RESOLUTION (step 8)  
`height`| Height of the target image in pixels (default: 1024)| INT| Yes| 16 - MAX_RESOLUTION (step 8)  
  
`max_shift` and `base_shift` are advanced parameters. The shift applied to the sampling configuration is calculated from the image dimensions: the latent resolution is computed as `width × height / 256`, and the shift value is interpolated between `base_shift` at a latent resolution of 256 and `max_shift` at a latent resolution of 4096.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with Flux sampling configuration applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/en.md)

* * *

**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelSamplingFlux.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelSamplingFlux)

[ChromaRadianceOptions](https://docs.comfy.org/built-in-nodes/ChromaRadianceOptions)[Apply USO Style Reference](https://docs.comfy.org/built-in-nodes/USOStyleReference)
