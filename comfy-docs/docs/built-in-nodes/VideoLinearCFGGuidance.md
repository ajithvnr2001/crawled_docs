---
url: https://docs.comfy.org/built-in-nodes/VideoLinearCFGGuidance/
title: VideoLinearCFGGuidance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:53.174845+00:00
---

# VideoLinearCFGGuidance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VideoLinearCFGGuidance/

Guiders

# VideoLinearCFGGuidance - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VideoLinearCFGGuidance node applies a linear conditioning guidance scale to a video model

Copy pageCopy page

The VideoLinearCFGGuidance node applies a linear conditioning guidance scale to a video model, adjusting the influence of conditioned and unconditioned components over a specified range. This enables dynamic control over the generation process, allowing for fine-tuning of the model’s output based on the desired level of conditioning.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model`| The model parameter represents the video model to which the linear CFG guidance will be applied. It is crucial for defining the base model that will be modified with the guidance scale.| MODEL  
`min_cfg`| The min_cfg parameter specifies the minimum conditioning guidance scale to be applied, serving as the starting point for the linear scale adjustment. It plays a key role in determining the lower bound of the guidance scale, influencing the model’s output.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`model`| The output is a modified version of the input model, with the linear CFG guidance scale applied. This adjusted model is capable of generating outputs with varying degrees of conditioning, based on the specified guidance scale.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCFGGuidance/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VideoLinearCFGGuidance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VideoLinearCFGGuidance)

[LTXVDualCFGGuider](https://docs.comfy.org/built-in-nodes/LTXVDualCFGGuider)[VideoTriangleCFGGuidance](https://docs.comfy.org/built-in-nodes/VideoTriangleCFGGuidance)
