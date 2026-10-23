---
url: https://docs.comfy.org/built-in-nodes/SplitSigmasDenoise/
title: SplitSigmasDenoise - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:03.944309+00:00
---

# SplitSigmasDenoise - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SplitSigmasDenoise/

Sigmas

# SplitSigmasDenoise - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SplitSigmasDenoise node divides a sequence of sigma values into two parts based on a denoising strength parameter.

Copy pageCopy page

The SplitSigmasDenoise node divides a sequence of sigma values into two parts based on a denoising strength parameter. It splits the input sigmas into high and low sigma sequences, where the split point is determined by multiplying the total steps (one less than the number of sigma values) by the denoise factor. This allows for separating the noise schedule into different intensity ranges for specialized processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`sigmas`| The input sequence of sigma values representing the noise schedule| SIGMAS| Yes| -  
`denoise`| The denoising strength factor that determines where to split the sigma sequence (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`high_sigmas`| The first portion of the sigma sequence, containing the higher sigma values up to the split point| SIGMAS  
`low_sigmas`| The second portion of the sigma sequence, containing the lower sigma values from the split point onward| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/en.md)

* * *

**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SplitSigmasDenoise.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SplitSigmasDenoise)

[SplitSigmas - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SplitSigmas)[KSampler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KSampler)

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
