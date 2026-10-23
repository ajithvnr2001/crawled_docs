---
url: https://docs.comfy.org/built-in-nodes/ConditioningSetPropertiesAndCombine/
title: ConditioningSetPropertiesAndCombine - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:42.074936+00:00
---

# ConditioningSetPropertiesAndCombine - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningSetPropertiesAndCombine/

Cond Single

# ConditioningSetPropertiesAndCombine - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ConditioningSetPropertiesAndCombine node modifies conditioning data by applying properties from a new conditioning input to an existing conditioning input.

Copy pageCopy page

The ConditioningSetPropertiesAndCombine node modifies conditioning data by applying properties from a new conditioning input to an existing conditioning input. It combines the two conditioning sets while controlling the strength of the new conditioning and specifying how the conditioning area should be applied.

## 

​

Inputs

Parameter| Description| Data Type| Input Type| Default| Range  
---|---|---|---|---|---  
`cond`| The original conditioning data to be modified| CONDITIONING| Required| -| -  
`cond_NEW`| The new conditioning data providing properties to apply| CONDITIONING| Required| -| -  
`strength`| Controls the intensity of the new conditioning properties| FLOAT| Required| 1.0| 0.0 - 10.0  
`set_cond_area`| Determines how the conditioning area is applied| STRING| Required| default| [“default”, “mask bounds”]  
`mask`| Optional mask to define specific areas for conditioning| MASK| Optional| -| -  
`hooks`| Optional hook functions for custom processing| HOOKS| Optional| -| -  
`timesteps`| Optional timestep range for controlling when conditioning is applied| TIMESTEPS_RANGE| Optional| -| -  
  
**Note:** When `mask` is provided, the `set_cond_area` parameter can use “mask bounds” to constrain the conditioning application to the masked regions.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The combined conditioning data with modified properties| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/en.md)

* * *

**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningSetPropertiesAndCombine.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningSetPropertiesAndCombine)

[ConditioningSetProperties - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningSetProperties)[CreateHookLora - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateHookLora)

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
