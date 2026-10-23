---
url: https://docs.comfy.org/built-in-nodes/LTXVDualCFGGuider/
title: LTXVDualCFGGuider - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:17.991342+00:00
---

# LTXVDualCFGGuider - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVDualCFGGuider/

Guiders

# LTXVDualCFGGuider - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a guided sampling object (CFG guider) for LTXV-AV models.

Copy pageCopy page

This node creates a guided sampling object (CFG guider) for LTXV-AV models. It applies a separate guidance scale to the video part and the audio part of a packed LTXV-AV latent, letting you control the influence of conditioning on each modality independently. If the two scales are equal, or if the latent does not contain separate video and audio components, a single overall scale is used instead.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to use when sampling.| MODEL| Yes| -  
`positive`| Positive conditioning to guide generation toward.| CONDITIONING| Yes| -  
`negative`| Negative conditioning to steer generation away from.| CONDITIONING| Yes| -  
`video_cfg`| Guidance strength applied to the video modality of the latent (default: 3.0).| FLOAT| Yes| 0.0 to 100.0  
`audio_cfg`| Guidance strength applied to the audio modality of the latent (default: 7.0).| FLOAT| Yes| 0.0 to 100.0  
  
Note: When `video_cfg` and `audio_cfg` are equal (or very close in value), the guider uses that value as a single CFG scale for the whole latent. If the latent is not a packed LTXV-AV latent, only the `video_cfg` value is used.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`guider`| The configured CFG guider to be passed to a sampler node.| GUIDER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/en.md)

* * *

**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVDualCFGGuider.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVDualCFGGuider)

[DualModelGuider - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DualModelGuider)[VideoLinearCFGGuidance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VideoLinearCFGGuidance)

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
