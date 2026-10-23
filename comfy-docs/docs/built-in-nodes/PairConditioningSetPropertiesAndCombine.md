---
url: https://docs.comfy.org/built-in-nodes/PairConditioningSetPropertiesAndCombine/
title: PairConditioningSetPropertiesAndCombine - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:40.834740+00:00
---

# PairConditioningSetPropertiesAndCombine - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PairConditioningSetPropertiesAndCombine/

Cond Pair

# PairConditioningSetPropertiesAndCombine - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PairConditioningSetPropertiesAndCombine node modifies and combines conditioning pairs by applying new conditioning data to existing positive and negative

Copy pageCopy page

The PairConditioningSetPropertiesAndCombine node modifies and combines conditioning pairs by applying new conditioning data to existing positive and negative conditioning inputs. It allows you to adjust the strength of the applied conditioning and control how the conditioning area is set. This node is particularly useful for advanced conditioning manipulation workflows where you need to blend multiple conditioning sources together.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The original positive conditioning input| CONDITIONING| Yes| -  
`negative`| The original negative conditioning input| CONDITIONING| Yes| -  
`positive_NEW`| The new positive conditioning to apply| CONDITIONING| Yes| -  
`negative_NEW`| The new negative conditioning to apply| CONDITIONING| Yes| -  
`strength`| The strength factor for applying the new conditioning (default: 1.0)| FLOAT| Yes| 0.0 to 10.0  
`set_cond_area`| Controls how the conditioning area is applied (default: “default”)| STRING| Yes| ”default"  
"mask bounds”  
`mask`| Optional mask to constrain the conditioning application area| MASK| No| -  
`hooks`| Optional hook group for advanced control| HOOKS| No| -  
`timesteps`| Optional timestep range specification| TIMESTEPS_RANGE| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The combined positive conditioning output| CONDITIONING  
`negative`| The combined negative conditioning output| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/en.md)

* * *

**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PairConditioningSetPropertiesAndCombine.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PairConditioningSetPropertiesAndCombine)

[PairConditioningSetProperties - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PairConditioningSetProperties)[ConditioningSetDefaultAndCombine - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningSetDefaultAndCombine)

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
