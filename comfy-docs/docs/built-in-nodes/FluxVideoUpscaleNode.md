---
url: https://docs.comfy.org/built-in-nodes/FluxVideoUpscaleNode/
title: FluxVideoUpscaleNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:57.830832+00:00
---

# FluxVideoUpscaleNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxVideoUpscaleNode/

BFL

# FluxVideoUpscaleNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Flux Video Upscale upscales a video clip by 1.5 to 3 times using FLUX super-resolution.

Copy pageCopy page

Flux Video Upscale upscales a video clip by 1.5 to 3 times using FLUX super-resolution. In creative mode it restores and invents fine detail; in precise mode it sharpens the source without changing it.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Source clip of 1 to 20 seconds with an aspect ratio between 1:4 and 4:1. The output is rendered at 24 fps and capped at about 14.4 megapixels per frame.| VIDEO| Yes| 1 to 20 seconds duration; aspect ratio between 1:4 and 4:1; minimum 64x64 pixels  
`upscale_factor`| Output size relative to the source. Very large sources are upscaled by less than the requested factor because of the per-frame cap. (default: 2.0)| FLOAT| Yes| 1.5 to 3.0 (step 0.1)  
`mode`| ’creative’ restores and invents fine detail, best for generated footage, textures and scenery. ‘precise’ sharpens the source without changing it, for faces, products and real footage. (default: “creative”)| COMBO| Yes| ”creative"  
"precise”  
`prompt`| Optional description of the clip that steers the enhanced detail. Leave empty for a neutral upscale. (default: empty)| STRING| Yes| Multiline text  
`auto_downscale`| Automatically downscale sources larger than 3840x2160 pixels in area to fit the input limit. Aspect ratio is preserved; smaller videos are untouched. (default: true)| BOOLEAN| Yes| true  
false  
`safety_tolerance`| Moderation tolerance, 0 is the strictest. (default: 2, advanced parameter)| INT| Yes| 0 to 4  
`seed`| Seed to determine if node should re-run; FLUX picks its own seed, so actual results are nondeterministic regardless of this value. (default: 42)| INT| Yes| 0 to 4294967295  
  
Note: The source video must be between 1 and 20 seconds long, at least 64x64 pixels in size, and have an aspect ratio between 1:4 and 4:1. If `auto_downscale` is disabled and the video area exceeds 3840x2160 pixels, the node raises an error. The output video is rendered at 24 fps and capped at about 14.4 megapixels per frame, so very large sources may be upscaled by less than the requested factor.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The upscaled video clip.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/en.md)

* * *

**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxVideoUpscaleNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxVideoUpscaleNode)

[FluxVideoEditNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxVideoEditNode)[BriaRemoveVideoBackground - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaRemoveVideoBackground)

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
