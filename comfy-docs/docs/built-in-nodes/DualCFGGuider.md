---
url: https://docs.comfy.org/built-in-nodes/DualCFGGuider/
title: DualCFGGuider - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:51.290335+00:00
---

# DualCFGGuider - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DualCFGGuider/

Guiders

# DualCFGGuider - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Dual CFG Guider node creates a guidance system for sampling that uses two conditioning inputs together with one negative conditioning input.

Copy pageCopy page

The Dual CFG Guider node creates a guidance system for sampling that uses two conditioning inputs together with one negative conditioning input. It applies two separate guidance scales to control how strongly each conditioning influences the generated result, and it supports two ways of combining those scales: “regular” and “nested”.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to use for guidance| MODEL| Yes| -  
`cond1`| The first positive conditioning input| CONDITIONING| Yes| -  
`cond2`| The second conditioning input, used as the reference between the first positive conditioning and the negative conditioning| CONDITIONING| Yes| -  
`negative`| The negative conditioning input| CONDITIONING| Yes| -  
`cfg_conds`| Guidance scale applied to the first positive conditioning (default: 8.0)| FLOAT| Yes| 0.0 - 100.0  
`cfg_cond2_negative`| Guidance scale applied between the second conditioning and the negative conditioning (default: 8.0)| FLOAT| Yes| 0.0 - 100.0  
`style`| The guidance style to apply (default: “regular”). When set to “nested”, the guidance is applied in a nested fashion| COMBO| Yes| ”regular"  
"nested”  
  
Note: In `regular` style, `cfg_cond2_negative` is applied between `cond2` and `negative`, and `cfg_conds` is applied between `cond1` and `cond2`. In `nested` style, `cfg_conds` is applied first between `cond1` and `cond2`, and the resulting prediction is then guided away from `negative` using `cfg_cond2_negative`. Note: In `regular` style, when `cfg_cond2_negative` is equal to 1.0 the negative conditioning is skipped, and when `cfg_conds` is also equal to 1.0 the second conditioning is skipped as well. This reduces the number of model evaluations performed.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`GUIDER`| A configured guidance system ready for use with sampling| GUIDER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/en.md)

* * *

**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DualCFGGuider.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DualCFGGuider)

[CFGOverride - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CFGOverride)[DualModelGuider - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DualModelGuider)

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
