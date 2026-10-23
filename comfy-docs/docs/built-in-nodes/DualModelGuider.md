---
url: https://docs.comfy.org/built-in-nodes/DualModelGuider/
title: DualModelGuider - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:51.130512+00:00
---

# DualModelGuider - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DualModelGuider/

Guiders

# DualModelGuider - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node allows you to use two different models during the guided CFG sampling process: one model for the positive (conditional) pass and a separate model

Copy pageCopy page

This node allows you to use two different models during the guided CFG sampling process: one model for the positive (conditional) pass and a separate model for the negative (unconditional) pass. When no negative model is provided, it behaves like a standard CFG guider using a single model.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model used for the positive (conditional) pass.| MODEL| Yes|   
`model_negative`| Model used for the negative (unconditional) pass. Use the same model for ordinary CFG.| MODEL| No|   
`positive`| The positive conditioning input.| CONDITIONING| Yes|   
`cfg`| The CFG scale value (default: 4.0).| FLOAT| Yes| 0.0 to 100.0 (step: 0.1)  
`negative`| Negative conditioning run on the negative model. Leave unconnected for a text-free (image-only) unconditional pass.| CONDITIONING| No|   
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`GUIDER`| A guider object configured with the specified models and conditioning for use in sampling.| GUIDER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualModelGuider/en.md)

* * *

**Source fingerprint (SHA-256):** `a60803156e98d2ffe975d39922dfbeacafd1a2155d88dd2e285ac1426a1e7a33`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DualModelGuider.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DualModelGuider)

[DualCFGGuider - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DualCFGGuider)[LTXVDualCFGGuider - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVDualCFGGuider)

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
