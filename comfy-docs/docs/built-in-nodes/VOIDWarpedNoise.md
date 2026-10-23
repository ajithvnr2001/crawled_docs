---
url: https://docs.comfy.org/built-in-nodes/VOIDWarpedNoise/
title: VOIDWarpedNoise - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:18.337016+00:00
---

# VOIDWarpedNoise - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VOIDWarpedNoise/

Void

# VOIDWarpedNoise - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates temporally-correlated noise for the second pass of the VOID video refinement process.

Copy pageCopy page

Generates temporally-correlated noise for the second pass of the VOID video refinement process. It takes the Pass 1 output video and warps Gaussian noise along optical flow vectors, so the noise moves consistently with the video content. The resulting warped noise is used as the starting latent for Pass 2, which improves temporal consistency in the final output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`optical_flow`| Optical flow model from OpticalFlowLoader (RAFT-large).| OPTICAL_FLOW| Yes| -  
`video`| Pass 1 output video frames [T, H, W, 3].| IMAGE| Yes| -  
`width`| Target width in pixels (default: 672). The input video is scaled to this width before the noise is generated, and the latent width is derived as width ÷ 8.| INT| Yes| 16 to MAX_RESOLUTION (step 8)  
`height`| Target height in pixels (default: 384). The input video is scaled to this height before the noise is generated, and the latent height is derived as height ÷ 8.| INT| Yes| 16 to MAX_RESOLUTION (step 8)  
`length`| Number of pixel frames. Rounded down to make latent_t even (patch_size_t=2 requirement), e.g. 49 to 45 (default: 45).| INT| Yes| 1 to MAX_RESOLUTION (step 1)  
`batch_size`| Number of identical warped noise sequences to produce (default: 1). The generated noise is repeated this many times along the batch dimension.| INT| Yes| 1 to 64  
  
**Note on the`length` parameter:** The `length` value is automatically rounded down to the nearest value that produces an even `latent_t` dimension, as required by the CogVideoX-Fun-V1.5 model’s `patch_size_t=2` constraint (for example, 49 becomes 45). The node logs a warning when this rounding occurs. Frames beyond the adjusted `length` are ignored, and the noise is resampled to the resulting latent frame count. **Note on`width` and `height`:** These values are used both to resize the incoming video frames (bilinear, center crop) and to determine the final latent resolution (divided by 8). If the generated noise does not match the requested latent size, it is resized to fit.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`warped_noise`| A 5D tensor (B, C, T, H, W) containing optical-flow warped Gaussian noise, ready for use as the initial latent in VOID Pass 2.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/en.md)

* * *

**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VOIDWarpedNoise.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VOIDWarpedNoise)

[VAEDecodeTripoSplat - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEDecodeTripoSplat)[VOIDWarpedNoiseSource - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VOIDWarpedNoiseSource)

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
