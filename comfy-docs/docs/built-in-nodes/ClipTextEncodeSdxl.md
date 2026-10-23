---
url: https://docs.comfy.org/built-in-nodes/ClipTextEncodeSdxl/
title: CLIPTextEncodeSDXL - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:36.417199+00:00
---

# CLIPTextEncodeSDXL - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipTextEncodeSdxl/

Stable Diffusion

# CLIPTextEncodeSDXL - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed to encode text input using a CLIP model specifically customized for the SDXL architecture.

Copy pageCopy page

This node is designed to encode text input using a CLIP model specifically customized for the SDXL architecture. It uses a dual encoder system (CLIP-L and CLIP-G) to process text descriptions, resulting in more accurate image generation.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`clip`| CLIP model instance used for text encoding.| CLIP  
`width`| Specifies the image width in pixels, default 1024.| INT  
`height`| Specifies the image height in pixels, default 1024.| INT  
`crop_w`| Width of the crop area in pixels, default 0.| INT  
`crop_h`| Height of the crop area in pixels, default 0.| INT  
`target_width`| Target width for the output image, default 1024.| INT  
`target_height`| Target height for the output image, default 1024.| INT  
`text_g`| Global text description for overall scene description.| STRING  
`text_l`| Local text description for detail description.| STRING  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`CONDITIONING`| Contains encoded text and conditional information needed for image generation.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeSdxl/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipTextEncodeSdxl.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipTextEncodeSdxl)

[CLIPTextEncodeSD3 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeSD3)[CLIPTextEncodeSDXLRefiner - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ClipTextEncodeSdxlRefiner)

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
