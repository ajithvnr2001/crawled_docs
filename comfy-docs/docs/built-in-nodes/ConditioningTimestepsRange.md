---
url: https://docs.comfy.org/built-in-nodes/ConditioningTimestepsRange/
title: ConditioningTimestepsRange - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:42.496976+00:00
---

# ConditioningTimestepsRange - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningTimestepsRange/

Hooks

# ConditioningTimestepsRange - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ConditioningTimestepsRange node creates three distinct timestep ranges for controlling when conditioning effects are applied during the generation process.

Copy pageCopy page

The ConditioningTimestepsRange node creates three distinct timestep ranges for controlling when conditioning effects are applied during the generation process. It takes start and end percentage values and divides the entire timestep range (0.0 to 1.0) into three segments: the main range between the specified percentages, the range before the start percentage, and the range after the end percentage.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`start_percent`| The starting percentage of the timestep range (default: 0.0)| FLOAT| Yes| 0.0 - 1.0  
`end_percent`| The ending percentage of the timestep range (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`TIMESTEPS_RANGE`| The main timestep range defined by start_percent and end_percent| TIMESTEPS_RANGE  
`BEFORE_RANGE`| The timestep range from 0.0 to start_percent| TIMESTEPS_RANGE  
`AFTER_RANGE`| The timestep range from end_percent to 1.0| TIMESTEPS_RANGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/en.md)

* * *

**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningTimestepsRange.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningTimestepsRange)

[SetHookKeyframes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SetHookKeyframes)[DeprecatedCheckpointLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DeprecatedCheckpointLoader)

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
