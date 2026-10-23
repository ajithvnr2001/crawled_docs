---
url: https://docs.comfy.org/built-in-nodes/TextEncodeMingImageEdit/
title: TextEncodeMingImageEdit - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:09.341441+00:00
---

# TextEncodeMingImageEdit - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeMingImageEdit/

Ming Image

# TextEncodeMingImageEdit - ComfyUI Built-in Node Documentation

Copy pageCopy page

Text Encode Ming Image Edit encodes a text prompt into conditioning for Ming image editing, optionally mixing in reference images.

Copy pageCopy page

Text Encode Ming Image Edit encodes a text prompt into conditioning for Ming image editing, optionally mixing in reference images. The prompt and the reference images are tokenized by a CLIP model, and when a VAE is connected the reference images are also encoded into latent frames that are appended to the conditioning.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used to tokenize the prompt and the reference images.| CLIP| Yes| -  
`vae`| Optional VAE that encodes the reference images into latent frames appended to the conditioning. Without a VAE the images only condition the text encoder through the vision tower.| VAE| No| -  
`prompt`| Text prompt to encode. Supports multiline input and dynamic prompts.| STRING| Yes| Multiline text  
`images`| Growable slot: optional reference images seen by the text encoder and appended to the latent sequence as clean frames. Connect 1..8 images (`image_1`, `image_2`, …); later images are resized to the first one and the sampled latent should match its size. Only the RGB channels are used.| IMAGE| No| 0 to 8  
  
**Note:** Reference images are read in numeric order of their slot names, and empty slots are ignored. Reference latents are only produced when both `vae` and at least one image are provided.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| Conditioning containing the encoded prompt, plus the reference latents when a VAE and reference images are provided.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMingImageEdit/en.md)

* * *

**Source fingerprint (SHA-256):** `675fb3cc0af006e1284fdb2a5ca2c268c540ee92e1ede90b2359f4e3fc8ba5ea`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeMingImageEdit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeMingImageEdit)

[TextEncodeMageFlowEdit - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TextEncodeMageFlowEdit)[MiniMaxH3AddGuide - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MiniMaxH3AddGuide)

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
