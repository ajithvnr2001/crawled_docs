---
url: https://docs.comfy.org/built-in-nodes/ReferenceMultiLatent/
title: ReferenceMultiLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:49.605860+00:00
---

# ReferenceMultiLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ReferenceMultiLatent/

Conditioning

# ReferenceMultiLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node encodes one or more reference images and appends their latents to the conditioning that an edit model consumes.

Copy pageCopy page

This node encodes one or more reference images and appends their latents to the conditioning that an edit model consumes. It is the multi-image counterpart of Set Reference Latent: you connect a VAE plus a set of reference images, and the node attaches every encoded latent to the positive conditioning and, when one is connected, to the negative conditioning as well. Use it when a model expects several reference images at once instead of a single latent.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning to modify with the reference latents.| CONDITIONING| Yes| -  
`negative`| Optional negative conditioning that receives the same reference latents. Leave it unconnected to reuse the modified positive conditioning on the `negative` output.| CONDITIONING| No| -  
`vae`| The VAE used to encode the connected reference images. When no VAE is connected the reference images are ignored.| VAE| No| -  
`resolution`| How each reference image is prepared before encoding. `"keep resolution"` encodes it at its incoming size; `"resize"` scales it to a target megapixel count while preserving the aspect ratio, which reveals `megapixels`. (default: “keep resolution”)| DYNAMIC_COMBO| Yes| `"keep resolution"`  
`"resize"`  
`images`| Growable slot: connect one or more reference images (`image_1`, `image_2`, …) to use as references. Images are encoded in slot order and appended to the conditioning in that order.| IMAGE| No| 1 to 100  
  
### 

​

Resize Inputs

These options appear when `resolution` is set to `"resize"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`megapixels`| Target size of each reference image, preserving aspect ratio. 1.0 is about 1024 x 1024 pixels. (default: 1.0)| FLOAT| Yes| 0.01 to 16.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning with the encoded reference latents appended.| CONDITIONING  
`negative`| The negative conditioning with the same reference latents appended. Returns the positive output when no negative conditioning is connected.| CONDITIONING  
`empty_latent`| The first reference latent multiplied by 0.0, ready to seed a sampler. Empty when no reference image is connected.| LATENT  
  
## 

​

Notes

  * The latents are appended rather than replaced, so chaining several Set Reference Multi Latent nodes accumulates references.
  * Each connected image is encoded on its own, so the reference images do not have to share a size.
  * Without any connected image, `positive` and `negative` are returned unchanged and `empty_latent` is empty.



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceMultiLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `06f98e7c21e8750a2bdf365cb80fac990bcf01246f183c60ef83bd195fc1225b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ReferenceMultiLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ReferenceMultiLatent)

[ReferenceLatent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ReferenceLatent)[ReferenceTimbreAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ReferenceTimbreAudio)

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
