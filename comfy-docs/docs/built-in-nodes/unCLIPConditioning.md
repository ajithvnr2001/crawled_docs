---
url: https://docs.comfy.org/built-in-nodes/unCLIPConditioning/
title: unCLIPConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:53.289727+00:00
---

# unCLIPConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/unCLIPConditioning/

Conditioning

# unCLIPConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed to integrate CLIP vision outputs into the conditioning process

Copy pageCopy page

This node is designed to integrate CLIP vision outputs into the conditioning process, adjusting the influence of these outputs based on specified strength and noise augmentation parameters. It enriches the conditioning with visual context, enhancing the generation process.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning`| The base conditioning data to which the CLIP vision outputs are to be added, serving as the foundation for further modifications.| `CONDITIONING`  
`clip_vision_output`| The output from a CLIP vision model, providing visual context that is integrated into the conditioning.| `CLIP_VISION_OUTPUT`  
`strength`| Determines the intensity of the CLIP vision output’s influence on the conditioning.| `FLOAT`  
`noise_augmentation`| Specifies the level of noise augmentation to apply to the CLIP vision output before integrating it into the conditioning.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning`| The enriched conditioning data, now containing integrated CLIP vision outputs with applied strength and noise augmentation.| `CONDITIONING`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/unCLIPConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/unCLIPConditioning)

[T5TokenizerOptions](https://docs.comfy.org/built-in-nodes/T5TokenizerOptions)[MOSSImageControl](https://docs.comfy.org/built-in-nodes/MOSSImageControl)
