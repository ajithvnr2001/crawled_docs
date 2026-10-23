---
url: https://docs.comfy.org/built-in-nodes/LTXVImgToVideoInplace/
title: LTXVImgToVideoInplace - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:19.130519+00:00
---

# LTXVImgToVideoInplace - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVImgToVideoInplace/

Ltxv

# LTXVImgToVideoInplace - ComfyUI Built-in Node Documentation

Copy pageCopy page

LTXVImgToVideoInplace encodes an input image into the latent space and places those encoded frames at the start of an existing latent video.

Copy pageCopy page

LTXVImgToVideoInplace encodes an input image into the latent space and places those encoded frames at the start of an existing latent video. The `strength` value controls how strongly the encoded image conditions those initial frames, and when `bypass` is enabled, the input latent is returned unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`vae`| The VAE model used to encode the input image into the latent space.| VAE| Yes| -  
`image`| The input image to be encoded and used to condition the video latent.| IMAGE| Yes| -  
`latent`| The target latent video representation to be modified.| LATENT| Yes| -  
`strength`| Controls how strongly the encoded image conditions the initial frames of the latent. A value of 1.0 fully conditions the initial frames with the encoded image, while lower values condition them less strongly. The noise mask for the initial frames is set to `1.0 - strength`. (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`bypass`| Bypass the conditioning. When enabled, the node returns the input latent unchanged. (default: False)| BOOLEAN| Yes| True or False  
  
**Note:** The `image` will be automatically resized to match the spatial dimensions required by the `vae` for encoding, based on the `latent` input’s width and height. Only the RGB channels of the `image` are used for encoding.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latent`| The resulting latent video representation. When bypass is disabled, it contains the updated `samples` and a `noise_mask` that applies the conditioning strength to the initial frames. When bypass is enabled, it is the input latent returned unchanged.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/en.md)

* * *

**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVImgToVideoInplace.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVImgToVideoInplace)

[LTXVImgToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVImgToVideo)[LTXVReferenceAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVReferenceAudio)

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
