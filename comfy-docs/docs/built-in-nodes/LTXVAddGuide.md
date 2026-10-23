---
url: https://docs.comfy.org/built-in-nodes/LTXVAddGuide/
title: LTXVAddGuide - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:16.922129+00:00
---

# LTXVAddGuide - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVAddGuide/

Ltxv

# LTXVAddGuide - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXVAddGuide node encodes input images or videos through a VAE encoder and adds them as guide keyframes to a latent video sequence.

Copy pageCopy page

The LTXVAddGuide node encodes input images or videos through a VAE encoder and adds them as guide keyframes to a latent video sequence. It updates both positive and negative conditioning and returns the modified latent, with options to set the starting frame, conditioning strength, an optional attention mask, and optional IC-LoRA parameters.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning input to be modified with keyframe guidance.| CONDITIONING| Yes| -  
`negative`| Negative conditioning input to be modified with keyframe guidance.| CONDITIONING| Yes| -  
`vae`| VAE model used for encoding the input image/video frames.| VAE| Yes| -  
`latent`| Input latent sequence that will receive the conditioning frames.| LATENT| Yes| -  
`image`| Image or video to condition the latent video on. Must be 8 _n + 1 frames. If the video is not 8_ n + 1 frames, it will be cropped to the nearest 8*n + 1 frames.| IMAGE| Yes| -  
`frame_idx`| Frame index to start the conditioning at. For single-frame images or videos with 1-8 frames, any frame_idx value is acceptable. For videos with 9+ frames, frame_idx must be divisible by 8, otherwise it will be rounded down to the nearest multiple of 8. Negative values are counted from the end of the video. Default: 0.| INT| Yes| -9999 to 9999  
`strength`| Strength of the conditioning influence, where 1.0 applies full conditioning and 0.0 applies no conditioning. Default: 1.0.| FLOAT| Yes| 0.0 to 10.0  
`attention_mask`| Optional pixel-space spatial mask. Controls per-region conditioning influence via self-attention, multiplied by strength.| MASK| No| -  
`iclora_parameters`| Optional IC-LoRA parameters from a Get IC-LoRA Parameters node. Used for adjusting guide processing as required by certain IC-LoRAs (e.g., those with a reference_downscale_factor > 1). When chained, each LTXVAddGuide uses only the parameters connected to it.| IC_LORA_PARAMETERS| No| -  
  
**Note:** The input image/video must have a frame count following the 8*n + 1 pattern (e.g., 1, 9, 17, 25 frames). If the input exceeds this pattern, it will be automatically cropped to the nearest valid frame count. **Note on`iclora_parameters`:** When using IC-LoRA parameters with a `reference_downscale_factor` greater than 1, the latent spatial dimensions (width and height) must be divisible by that factor. The node will raise an error if this condition is not met. **Note:** The encoded guide frames must fit within the latent sequence at the selected frame position. If the conditioned frames exceed the length of the latent sequence, the node raises an error. **Note:** Adding a guide to a latent that combines audio and video channels is not supported and will raise an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning updated with keyframe guidance information.| CONDITIONING  
`negative`| Negative conditioning updated with keyframe guidance information.| CONDITIONING  
`latent`| Latent sequence with incorporated conditioning frames and updated noise mask.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/en.md)

* * *

**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVAddGuide.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVAddGuide)

[LTXVAddGeneratedKeyframes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVAddGeneratedKeyframes)[LTXVAddLatentGuide - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVAddLatentGuide)

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
