---
url: https://docs.comfy.org/built-in-nodes/LTXVAddLatentGuide/
title: LTXVAddLatentGuide - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:17.504052+00:00
---

# LTXVAddLatentGuide - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVAddLatentGuide/

Ltxv

# LTXVAddLatentGuide - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Add Latent Guide node pins an already-encoded latent as a guide, for when the guide comes out of an earlier stage rather than an image.

Copy pageCopy page

The LTXV Add Latent Guide node pins an already-encoded latent as a guide, for when the guide comes out of an earlier stage rather than an image. It has the same effect as LTXV Add Guide without the VAE decode/encode round trip. A guide that is spatially smaller than the target (an IC-LoRA or detailing reference) is dilated onto a sparse grid, and its RoPE end positions are expanded by the same ratio so it covers the target canvas instead of addressing only the top-left corner of it.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning input.| CONDITIONING| Yes| N/A  
`negative`| Negative conditioning input.| CONDITIONING| Yes| N/A  
`vae`| The VAE model used to read the downscale index formula for frame placement.| VAE| Yes| N/A  
`latent`| Target video latent the guide is pinned onto.| LATENT| Yes| N/A  
`guiding_latent`| Guide latent. Its spatial size must divide the target’s by the same whole number on both axes; equal size pins it as-is, half size is treated as an x2 IC-LoRA reference.| LATENT| Yes| N/A  
`latent_idx`| Latent frame index to start the guide at, counted in latent frames rather than pixel frames. Negative values place the guide on frames before the start of the latent, not counted back from its end. Default: 0.| INT| Yes| -9999 to 9999  
`strength`| Capped at 1.0. A dilated guide marks its padding positions with a negative denoise mask so the model drops them; above 1.0 the kept positions would go negative too and the whole guide would be dropped. Amplify beyond 1.0 with attention_mask instead. Default: 1.0.| FLOAT| Yes| 0.0 to 1.0, step 0.01  
`attention_mask`| Optional pixel-space spatial mask. Controls per-region conditioning influence via self-attention, multiplied by strength.| MASK| No| N/A  
  
### 

​

Notes

  * Both `latent` and `guiding_latent` must be 5D video latents shaped (batch, channels, frames, height, width).
  * The guide must fit inside the target latent: the guide’s frame count added to `latent_idx` must not run past the end of the target latent. Negative `latent_idx` values are allowed and place the guide before the start of the latent.
  * The guide’s spatial size must divide the target’s spatial size by a whole number on both the height and width axes.
  * The height ratio and the width ratio must be the same value (a square ratio). A non-square ratio raises an error, because the dilation and RoPE placement use a single downscale factor for both axes.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with the guide attached.| CONDITIONING  
`negative`| Negative conditioning with the guide attached.| CONDITIONING  
`latent`| Latent output with the guide applied, including the updated `noise_mask`.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/en.md)

* * *

**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVAddLatentGuide.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVAddLatentGuide)

[LTXVAddGuide - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVAddGuide)[LTXVConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVConditioning)

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
