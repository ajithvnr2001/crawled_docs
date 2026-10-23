---
url: https://docs.comfy.org/built-in-nodes/AddNoise/
title: AddNoise - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:18.994658+00:00
---

# AddNoise - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AddNoise/

Noise

# AddNoise - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node adds controlled noise to a latent image using a specified noise generator and sigma values.

Copy pageCopy page

This node adds controlled noise to a latent image using a specified noise generator and sigma values. It processes the input through the model’s sampling system to apply noise scaling appropriate for the given sigma range, returning a new latent representation with the noise applied. This node is currently marked as experimental.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model containing sampling parameters and processing functions| MODEL| Yes| -  
`noise`| The noise generator that produces the base noise pattern| NOISE| Yes| -  
`sigmas`| Sigma values controlling the noise scaling intensity. If empty, the node returns the original latent image unchanged. When multiple sigmas are provided, the noise scale is calculated as the absolute difference between the first and last sigma values. When only one sigma is provided, that value is used directly as the scale.| SIGMAS| Yes| -  
`latent_image`| The input latent representation to which noise will be added. Empty latent images (containing only zeros) are not shifted during processing.| LATENT| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| The modified latent representation with added noise. Any NaN or infinite values in the output are converted to zeros for stability.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/en.md)

* * *

**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AddNoise.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AddNoise)

[VideoTriangleCFGGuidance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VideoTriangleCFGGuidance)[DisableNoise - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DisableNoise)

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
