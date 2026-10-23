---
url: https://docs.comfy.org/built-in-nodes/TextEncodeJoyImageEdit/
title: TextEncodeJoyImageEdit - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:09.141871+00:00
---

# TextEncodeJoyImageEdit - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeJoyImageEdit/

Joyimage

# TextEncodeJoyImageEdit - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node encodes a text prompt and optional images into conditioning data for use with JoyImage models.

Copy pageCopy page

This node encodes a text prompt and optional images into conditioning data for use with JoyImage models. It combines a CLIP text encoder with optional image inputs to create rich conditioning that can guide image generation or editing tasks.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used for encoding the text prompt| CLIP| Yes| -  
`prompt`| The text prompt to encode, supporting multiline input and dynamic prompts| STRING| Yes| -  
`vae`| A VAE model for encoding images into latent space| VAE| No| -  
`images`| Optional images to include in the conditioning, up to a maximum of 6 images. Each image connects as a separate input (image_0 to image_5)| IMAGE| No| 0 to 6 images  
  
The `images` input is an autogrow group that accepts between 0 and 6 images. When no images are connected, the conditioning is based on the text prompt alone.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The encoded conditioning data combining the text prompt and any provided images| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeJoyImageEdit/en.md)

* * *

**Source fingerprint (SHA-256):** `ef48523aa9fc990b2839d755cef272bcdfbacef5af8d961736fde5200c6f082d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeJoyImageEdit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeJoyImageEdit)

[InstructPixToPixConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/InstructPixToPixConditioning)[CLIPTextEncodeKandinsky5 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeKandinsky5)

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
