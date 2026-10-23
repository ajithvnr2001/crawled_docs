---
url: https://docs.comfy.org/built-in-nodes/SamplerARVideo/
title: SamplerARVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:55.818740+00:00
---

# SamplerARVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerARVideo/

Samplers

# SamplerARVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Sampler AR Video node provides a specialized sampling method for autoregressive video models, such as those using Causal Forcing or Self-Forcing techniques.

Copy pageCopy page

The Sampler AR Video node provides a specialized sampling method for autoregressive video models, such as those using Causal Forcing or Self-Forcing techniques. It manages all parameters related to the autoregressive (AR) loop directly within the workflow, making it easy to configure how the model generates video frames one step at a time.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`num_frame_per_block`| Frames per autoregressive block. A value of 1 means the model generates one frame at a time (framewise), while a value of 3 means it generates three frames together (chunkwise). This setting must match the checkpoint’s training mode. Default: 1.| INT| Yes| 1 to 64  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SAMPLER`| A configured sampler object that uses the “ar_video” sampling function with the specified autoregressive parameters.| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerARVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerARVideo)

[KSamplerSelect - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KSamplerSelect)[SamplerDPMAdaptative - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerDPMAdaptative)

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
