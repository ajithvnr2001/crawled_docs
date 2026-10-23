---
url: https://docs.comfy.org/built-in-nodes/ExtendIntermediateSigmas/
title: ExtendIntermediateSigmas - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:54.585986+00:00
---

# ExtendIntermediateSigmas - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ExtendIntermediateSigmas/

Sigmas

# ExtendIntermediateSigmas - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ExtendIntermediateSigmas node takes an existing sequence of sigma values and inserts additional intermediate sigma values between them.

Copy pageCopy page

The ExtendIntermediateSigmas node takes an existing sequence of sigma values and inserts additional intermediate sigma values between them. It allows you to specify how many extra steps to add, the spacing method for interpolation, and optional start and end sigma boundaries to control where the extension occurs within the sigma sequence.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`sigmas`| The input sigma sequence to extend with intermediate values| SIGMAS| Yes| -  
`steps`| Controls the number of intermediate sigma values inserted between each pair of existing sigmas. The interval between two sigmas is divided into `steps` parts, producing `steps - 1` new values per pair (default: 2, which inserts one value per pair)| INT| Yes| 1 to 100  
`start_at_sigma`| Upper sigma boundary for extension. Only sigma intervals whose starting sigma is less than or equal to this value are extended. When set to -1.0, it is treated as infinity, meaning no upper limit is applied. Default: -1.0| FLOAT| Yes| -1.0 to 20000.0  
`end_at_sigma`| Lower sigma boundary for extension. Only sigma intervals whose starting sigma is greater than or equal to this value are extended. Default: 12.0| FLOAT| Yes| 0.0 to 20000.0  
`spacing`| The interpolation method for spacing the intermediate sigma values (default: “linear”)| COMBO| Yes| `"linear"`  
`"cosine"`  
`"sine"`  
  
**Note:** The node only inserts intermediate sigmas for sigma intervals where the starting sigma is less than or equal to `start_at_sigma` and greater than or equal to `end_at_sigma`. When `start_at_sigma` is set to -1.0, it is treated as infinity, so only the `end_at_sigma` lower boundary applies.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sigmas`| The extended sigma sequence with additional intermediate values inserted| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/en.md)

* * *

**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ExtendIntermediateSigmas.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ExtendIntermediateSigmas)

[VPScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VPScheduler)[FlipSigmas - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FlipSigmas)

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
