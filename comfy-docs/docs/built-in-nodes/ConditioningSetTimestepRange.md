---
url: https://docs.comfy.org/built-in-nodes/ConditioningSetTimestepRange/
title: ConditioningSetTimestepRange - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:52.049663+00:00
---

# ConditioningSetTimestepRange - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningSetTimestepRange/

Transform

# ConditioningSetTimestepRange - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed to adjust the temporal aspect of conditioning by setting a specific range of timesteps.

Copy pageCopy page

This node is designed to adjust the temporal aspect of conditioning by setting a specific range of timesteps. It allows for the precise control over the start and end points of the conditioning process, enabling more targeted and efficient generation.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`CONDITIONING`| The conditioning input represents the current state of the generation process, which this node modifies by setting a specific range of timesteps.| CONDITIONING  
`start`| The start parameter specifies the beginning of the timestep range as a percentage of the total generation process, allowing for fine-tuned control over when the conditioning effects begin.| `FLOAT`  
`end`| The end parameter defines the endpoint of the timestep range as a percentage, enabling precise control over the duration and conclusion of the conditioning effects.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`CONDITIONING`| The output is the modified conditioning with the specified timestep range applied, ready for further processing or generation.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetTimestepRange/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningSetTimestepRange.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningSetTimestepRange)

[ConditioningSetMask](https://docs.comfy.org/built-in-nodes/ConditioningSetMask)[ConditioningZeroOut](https://docs.comfy.org/built-in-nodes/ConditioningZeroOut)
