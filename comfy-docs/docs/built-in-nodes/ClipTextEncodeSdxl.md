---
url: https://docs.comfy.org/built-in-nodes/ClipTextEncodeSdxl/
title: CLIPTextEncodeSDXL - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:51.244177+00:00
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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipTextEncodeSdxl.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipTextEncodeSdxl)

[CLIPTextEncodeSD3](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeSD3)[CLIPTextEncodeSDXLRefiner](https://docs.comfy.org/built-in-nodes/ClipTextEncodeSdxlRefiner)
