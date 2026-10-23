---
url: https://docs.comfy.org/built-in-nodes/TripoSplatSamplingPreview/
title: TripoSplatSamplingPreview - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:14.502160+00:00
---

# TripoSplatSamplingPreview - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoSplatSamplingPreview/

Triposplat

# TripoSplatSamplingPreview - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node patches a TripoSplat model so that when used with the standard KSampler node

Copy pageCopy page

This node patches a TripoSplat model so that when used with the standard KSampler node, a live preview of the decoded gaussian splat is shown at each sampling step. It works by wrapping the sampler’s callback to decode the model’s output into a preview image after every step.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The TripoSplat model to patch for live preview (provides the conditioning token length used to estimate memory needs)| MODEL| Yes|   
`vae`| TripoSplat VAE decoder| VAE| Yes|   
`octree_level`| Octree depth for the preview decode (lower = cheaper/coarser). Default: 5| INT| No| 2 to 8  
`num_gaussians`| Number of gaussians to produce for the preview (rounded to a multiple of 32). Default: 16384| INT| No| 1024 to 262144 (step: 32)  
`yaw`| Preview camera yaw in degrees. Default: 90.0| FLOAT| No| -360.0 to 360.0 (step: 1.0)  
`pitch`| Preview camera pitch in degrees. Default: 15.0| FLOAT| No| -89.0 to 89.0 (step: 1.0)  
`point_size`| Maximum splat radius in pixels. Each gaussian is sized from its scale and capped here; lower = finer/pointier, higher = chunkier. Default: 3| INT| No| 1 to 16  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The patched TripoSplat model with live preview functionality added| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/en.md)

* * *

**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoSplatSamplingPreview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoSplatSamplingPreview)

[VaeDecodeTextureTrellis - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VaeDecodeTextureTrellis)[VAEDecodeTripoSplat - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAEDecodeTripoSplat)

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
