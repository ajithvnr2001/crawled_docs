---
url: https://docs.comfy.org/built-in-nodes/PairConditioningSetProperties/
title: PairConditioningSetProperties - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:40.731778+00:00
---

# PairConditioningSetProperties - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PairConditioningSetProperties/

Cond Pair

# PairConditioningSetProperties - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PairConditioningSetProperties node allows you to modify properties of both positive and negative conditioning pairs at the same time.

Copy pageCopy page

The **PairConditioningSetProperties** node allows you to modify properties of both positive and negative conditioning pairs at the same time. It applies strength adjustments, conditioning area settings, and optional masking or timing controls to both conditioning inputs, returning the modified positive and negative conditioning data.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive_NEW`| The positive conditioning input to modify| CONDITIONING| Yes| -  
`negative_NEW`| The negative conditioning input to modify| CONDITIONING| Yes| -  
`strength`| The strength multiplier applied to the conditioning (default: 1.0)| FLOAT| Yes| 0.0 to 10.0  
`set_cond_area`| Determines how the conditioning area is calculated (default: “default”)| STRING| Yes| ”default"  
"mask bounds”  
`mask`| Optional mask to constrain the conditioning area| MASK| No| -  
`hooks`| Optional hook group for advanced conditioning modifications| HOOKS| No| -  
`timesteps`| Optional timestep range to limit when conditioning is applied| TIMESTEPS_RANGE| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The modified positive conditioning with applied properties| CONDITIONING  
`negative`| The modified negative conditioning with applied properties| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/en.md)

* * *

**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PairConditioningSetProperties.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PairConditioningSetProperties)

[PairConditioningSetDefaultAndCombine - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PairConditioningSetDefaultAndCombine)[PairConditioningSetPropertiesAndCombine - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PairConditioningSetPropertiesAndCombine)

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
