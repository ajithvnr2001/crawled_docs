---
url: https://docs.comfy.org/built-in-nodes/ManualSigmas/
title: ManualSigmas - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:29.414494+00:00
---

# ManualSigmas - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ManualSigmas/

Sigmas

# ManualSigmas - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ManualSigmas node allows you to manually define a custom sequence of noise levels (sigmas) for the sampling process.

Copy pageCopy page

The ManualSigmas node allows you to manually define a custom sequence of noise levels (sigmas) for the sampling process. You input a list of numbers as a string, and the node converts them into a SIGMAS tensor that can be used by other sampling nodes. This is useful for testing or creating specific noise schedules.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`sigmas`| A string containing the sigma values. The node extracts all numbers from this string, including decimals and negative values. For example, “1, 0.5, 0.1” or “1 0.5 0.1”. Default: “1, 0.5”.| STRING| Yes| Any comma- or space-separated numeric values  
  
Note: This node is marked as experimental.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sigmas`| A tensor containing the sequence of sigma values extracted from the input string.| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/en.md)

* * *

**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ManualSigmas.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ManualSigmas)

[FlipSigmas - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FlipSigmas)[SamplingPercentToSigma - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplingPercentToSigma)

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
