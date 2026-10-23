---
url: https://docs.comfy.org/built-in-nodes/ConditioningSetProperties/
title: ConditioningSetProperties - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:42.599096+00:00
---

# ConditioningSetProperties - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningSetProperties/

Cond Single

# ConditioningSetProperties - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ConditioningSetProperties node modifies the properties of conditioning data by adjusting strength, area settings, and applying optional masks, hooks

Copy pageCopy page

The ConditioningSetProperties node modifies the properties of conditioning data by adjusting strength, area settings, and applying optional masks, hooks, or timestep ranges. It allows you to control how conditioning influences the generation process by setting specific parameters that affect the application of conditioning data during image generation.

## 

​

Inputs

Parameter| Description| Data Type| Input Type| Default| Range  
---|---|---|---|---|---  
`cond_NEW`| The conditioning data to modify| CONDITIONING| Required| -| -  
`strength`| Controls the intensity of the conditioning effect| FLOAT| Required| 1.0| 0.0 - 10.0 (step: 0.01)  
`set_cond_area`| Determines how the conditioning area is applied. Choose “default” for standard behavior or “mask bounds” to restrict to the mask region| STRING| Required| default| [“default”, “mask bounds”]  
`mask`| Optional mask to restrict where conditioning is applied| MASK| Optional| -| -  
`hooks`| Optional hook functions for custom processing| HOOKS| Optional| -| -  
`timesteps`| Optional timestep range to limit when conditioning is active| TIMESTEPS_RANGE| Optional| -| -  
  
**Note:** When a `mask` is provided, the `set_cond_area` parameter can be set to “mask bounds” to restrict conditioning application to the masked region only. The `hooks` parameter allows for custom processing via hook functions, and `timesteps` limits the conditioning effect to a specific range of timesteps during generation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The modified conditioning data with updated properties| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/en.md)

* * *

**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningSetProperties.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningSetProperties)

[ConditioningSetDefaultAndCombine - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningSetDefaultAndCombine)[ConditioningSetPropertiesAndCombine - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningSetPropertiesAndCombine)

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
