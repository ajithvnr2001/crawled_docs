---
url: https://docs.comfy.org/built-in-nodes/SeedVR2Preprocess/
title: SeedVR2Preprocess - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:00.835534+00:00
---

# SeedVR2Preprocess - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SeedVR2Preprocess/

Pre Processors

# SeedVR2Preprocess - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node prepares a resized image or video for the SeedVR2 model by padding it to the shape the model expects.

Copy pageCopy page

This node prepares a resized image or video for the SeedVR2 model by padding it to the shape the model expects. Pixel values are clamped to the 0-1 range, the height and width are padded to multiples of 16, and the frame count is padded by repeating the last frame until it follows a 4n+1 pattern (1, 5, 9, 13, …). The alpha channel is dropped during processing; the companion Post-Process SeedVR2 Output node restores it later from the original resized image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`resized_images`| The resized image to process.| IMAGE| Yes| -  
  
Note: The input can be a single frame, a sequence of frames, or a batch of videos (4-D or 5-D IMAGE tensors). If it has more than 3 channels, the alpha channel is dropped and only RGB is kept. The shorter edge of the input must be at least 2 pixels. Spatial padding is filled with black (value 0), and valid frame counts follow a 4n+1 pattern (1, 5, 9, 13, …).

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The padded image for VAE encoding.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/en.md)

* * *

**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SeedVR2Preprocess.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SeedVR2Preprocess)

[SeedVR2PostProcessing - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SeedVR2PostProcessing)[GLSLShader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GLSLShader)

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
