---
url: https://docs.comfy.org/built-in-nodes/SamplingPercentToSigma/
title: SamplingPercentToSigma - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:57.418310+00:00
---

# SamplingPercentToSigma - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplingPercentToSigma/

Sigmas

# SamplingPercentToSigma - ComfyUI Built-in Node Documentation

Copy pageCopy page

Converts a sampling percentage into the matching sigma value using the selected model’s sampling settings.

Copy pageCopy page

Converts a sampling percentage into the matching sigma value using the selected model’s sampling settings. It maps a percentage between 0.0 and 1.0 onto the model’s noise schedule, and can optionally return the model’s true maximum or minimum sigma at the two end points.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model containing the sampling parameters used for the conversion| MODEL| Yes| -  
`sampling_percent`| The sampling percentage to convert to a sigma value (default: 0.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.0001)  
`return_actual_sigma`| Return the actual sigma value instead of the value used for interval checks. This only affects results at 0.0 and 1.0. (default: False)| BOOLEAN| Yes| -  
  
When `return_actual_sigma` is enabled, a `sampling_percent` of 0.0 returns the model’s maximum sigma value (sigma_max), and a `sampling_percent` of 1.0 returns the minimum sigma value (sigma_min). For all other percentages, the result is the same whether or not this option is enabled.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sigma_value`| The sigma value corresponding to the input sampling percentage| FLOAT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/en.md)

* * *

**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplingPercentToSigma.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplingPercentToSigma)

[ManualSigmas - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ManualSigmas)[SetFirstSigma - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SetFirstSigma)

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
