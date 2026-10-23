---
url: https://docs.comfy.org/built-in-nodes/VAEDecodeTripoSplat/
title: VAEDecodeTripoSplat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:16.428009+00:00
---

# VAEDecodeTripoSplat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEDecodeTripoSplat/

Triposplat

# VAEDecodeTripoSplat - ComfyUI Built-in Node Documentation

Copy pageCopy page

Decode a TripoSplat latent representation into a 3D gaussian splat.

Copy pageCopy page

Decode a TripoSplat latent representation into a 3D gaussian splat. This node takes the sampled latent from a TripoSplat model and reconstructs it as a set of 3D gaussians, which can be adjusted in density by modifying the number of gaussians produced.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The latent samples to decode. If the samples contain a nested camera stream alongside the latent, only the latent stream is decoded.| LATENT| Yes| -  
`vae`| TripoSplat VAE decoder| VAE| Yes| -  
`num_gaussians`| Number of gaussians to produce (rounded to a multiple of 32). 262144 matches the octree’s point density; higher oversamples the same points (denser, but no new detail) and costs proportionally more VRAM/time. Default: 262144| INT| Yes| 32 to 1048576 (step: 32)  
`seed`| Seeds the octree point sampler (global RNG) for deterministic decodes. Default: 0| INT| Yes| 0 to 18446744073709551615  
  
**Note:** The `num_gaussians` value is automatically clamped to the allowed range and rounded to a multiple of the VAE decoder’s gaussians-per-point setting. The actual number used may differ slightly from the input value.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`splat`| The decoded 3D gaussian splat containing positions, scales, rotations, opacities, and spherical harmonics coefficients| SPLAT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/en.md)

* * *

**Source fingerprint (SHA-256):** `5c2b21cee31c68a6440ab4c7156e0d5c041ce7264f6467a508dc41e2eb0dc598`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEDecodeTripoSplat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEDecodeTripoSplat)

[TripoSplatSamplingPreview - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoSplatSamplingPreview)[VOIDWarpedNoise - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VOIDWarpedNoise)

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
