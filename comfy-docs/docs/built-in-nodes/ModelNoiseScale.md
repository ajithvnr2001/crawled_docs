---
url: https://docs.comfy.org/built-in-nodes/ModelNoiseScale/
title: ModelNoiseScale - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:49.700126+00:00
---

# ModelNoiseScale - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelNoiseScale/

Patch

# ModelNoiseScale - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node adjusts the noise scale used during model sampling.

Copy pageCopy page

This node adjusts the noise scale used during model sampling. It creates a copy of the input model, applies the specified noise scale to its sampling configuration, and returns the modified model.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply the noise scale adjustment to.| MODEL| Yes| -  
`noise_scale`| Absolute training noise scale. For example HiDream-O1 base: 8.0, dev: 7.5. (default: 1.0)| FLOAT| Yes| 0.0 to 64.0 (step: 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The modified model with the new noise scale applied.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/en.md)

* * *

**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelNoiseScale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelNoiseScale)

[ModelAttentionBackend](https://docs.comfy.org/built-in-nodes/ModelAttentionBackend)[ModelSamplingAuraFlow](https://docs.comfy.org/built-in-nodes/ModelSamplingAuraFlow)
