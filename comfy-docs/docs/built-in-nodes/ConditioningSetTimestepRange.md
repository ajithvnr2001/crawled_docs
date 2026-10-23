---
url: https://docs.comfy.org/built-in-nodes/ConditioningSetTimestepRange/
title: ConditioningSetTimestepRange - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:43.180237+00:00
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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSettimestepRange/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningSetTimestepRange.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningSetTimestepRange)

[ConditioningSetMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningSetMask)[ConditioningZeroOut - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningZeroOut)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
