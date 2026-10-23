---
url: https://docs.comfy.org/built-in-nodes/WanAnimate2Cache/
title: WanAnimate2Cache - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:22.346990+00:00
---

# WanAnimate2Cache - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanAnimate2Cache/

Animate

# WanAnimate2Cache - ComfyUI Built-in Node Documentation

Copy pageCopy page

Caches the pose-video’s per-block activations once so they do not need to be recomputed on every sampling step, which roughly halves generation time.

Copy pageCopy page

Caches the pose-video’s per-block activations once so they do not need to be recomputed on every sampling step, which roughly halves generation time. The tradeoff is extra memory usage: about 12.5 GB of system RAM at 480x832 resolution with 81 frames in bf16, scaling with resolution and video length.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Wan Animate2 model to attach the cache to.| MODEL| Yes|   
`device`| Where to keep the cache. cpu (RAM) is the safe choice, the cache will not fit in VRAM alongside the model at typical sizes. gpu (VRAM) can be faster if it fits. (default: “cpu”)| STRING| Yes| ”cpu"  
"gpu”  
`dtype`| Storage precision. default stores the activations in the model’s compute dtype. int8 halves the cache, int4 quarters it, convrot is used to retain accuracy. (default: “default”)| STRING| Yes| ”default"  
"int8"  
"int4”  
  
Note: When context windows are used, each window is cached separately, so memory usage scales with the window count. The static_standard schedule should be used, because uniform schedules shift the windows on every step and the cache is never reused.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The cloned model with the pose-video activation cache attached. The cache is automatically freed when generation finishes.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2Cache/en.md)

* * *

**Source fingerprint (SHA-256):** `06305432601afd7c797ef29ef4be3f2bb1aa660e05edde270499e94ccdd54f84`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanAnimate2Cache.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanAnimate2Cache)

[VOIDInpaintConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VOIDInpaintConditioning)[WanAnimate2ToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanAnimate2ToVideo)

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
