---
url: https://docs.comfy.org/built-in-nodes/BerniniConditioning/
title: BerniniConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:24.035747+00:00
---

# BerniniConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BerniniConditioning/

Bernini

# BerniniConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The BerniniConditioning node prepares video and image conditioning data for the Wan2.2-A14B model.

Copy pageCopy page

The BerniniConditioning node prepares video and image conditioning data for the Wan2.2-A14B model. It encodes source videos, reference videos, and reference images using the provided VAE, then attaches them to the conditioning data as in-context tokens. The task is automatically inferred from which inputs are connected.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning data| CONDITIONING| Yes| -  
`negative`| Negative conditioning data| CONDITIONING| Yes| -  
`vae`| VAE model used to encode video and image inputs| VAE| Yes| -  
`width`| Width of the output latent (default: 832)| INT| Yes| 16 to 8192 (step: 16)  
`height`| Height of the output latent (default: 480)| INT| Yes| 16 to 8192 (step: 16)  
`length`| Number of frames in the output latent (default: 81)| INT| Yes| 1 to 8192 (step: 4)  
`batch_size`| Number of videos to generate in a single batch (default: 1)| INT| Yes| 1 to 4096  
`source_video`| Source video to edit or restyle (v2v, rv2v). Resized to width/height and trimmed to length.| IMAGE| No| -  
`reference_video`| Video to insert into the source video (ads2v). Trimmed to length and resized with preserved aspect ratio (long edge capped at ref_max_size).| IMAGE| No| -  
`reference_images`| Reference images injected as in-context tokens (r2v, rv2v). Each image is encoded independently at its own native aspect ratio (long edge capped at ref_max_size). Up to 8 images can be provided.| IMAGE| No| 0 to 8 images  
`ref_max_size`| Max size for the long edge of reference_video and reference_images. Resized with preserved aspect ratio and snapped to 16px (default: 848).| INT| No| 16 to 8192 (step: 16)  
  
**Note:** The task is inferred from which inputs are connected:

  * No inputs connected → text-to-video (t2v)
  * `source_video` only → video-to-video (v2v)
  * `source_video` \+ `reference_images` → reference-guided video editing (rv2v)
  * `reference_images` only → reference-to-video (r2v)
  * `source_video` \+ `reference_video` → insert image/video into video (ads2v)

Context streams are attached in a fixed order: `source_video` (source ID 1), then `reference_video` (source ID 2), then each reference image (source IDs 3, 4, …). A reference image input containing multiple images contributes one stream per image.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with context latents attached| CONDITIONING  
`negative`| Negative conditioning with context latents attached| CONDITIONING  
`latent`| Empty latent tensor with dimensions matching the specified width, height, length, and batch size| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BerniniConditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `70b5026f9479249bc5d1fe4695583193216e34e1b092764ac30e0ec3b7eba670`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BerniniConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BerniniConditioning)

[ARVideoI2V - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ARVideoI2V)[TextEncodeBooguEdit - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextEncodeBooguEdit)

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
