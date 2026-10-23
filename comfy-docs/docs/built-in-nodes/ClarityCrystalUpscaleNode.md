---
url: https://docs.comfy.org/built-in-nodes/ClarityCrystalUpscaleNode/
title: ClarityCrystalUpscaleNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:35.012331+00:00
---

# ClarityCrystalUpscaleNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClarityCrystalUpscaleNode/

Clarity AI

# ClarityCrystalUpscaleNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Upscale an image with Clarity AI’s Crystal Upscaler, a high-fidelity upscaler that stays faithful to the original while restoring faces, skin, and fine texture.

Copy pageCopy page

Upscale an image with Clarity AI’s Crystal Upscaler, a high-fidelity upscaler that stays faithful to the original while restoring faces, skin, and fine texture. The image is sent to Clarity AI’s API and the upscaled result is returned as an image. Selecting a `model` reveals the parameters specific to that model.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use. Selecting a model reveals the parameters specific to it: `image`, `scale_factor`, and `creativity`.| DYNAMIC_COMBO| Yes| `"crystal-upscaler"`  
`image`| The image to upscale. Must contain exactly one image; image batches are not supported.| IMAGE| Yes| N/A  
`scale_factor`| Factor to multiply the image width and height by. The output is limited to 100 megapixels (default: 2.0).| FLOAT| Yes| 1.0 to 200.0 (step 0.1)  
`creativity`| Higher values let the model reconstruct more detail instead of strictly preserving the original. Has no effect on images whose shorter side is 256 pixels or less (default: 0).| INT| Yes| 0 to 10  
  
**Note:** The input image must be at least 2x2 pixels. The output is capped at 100 megapixels and 65535 pixels per side; a larger result raises an error, so use a smaller image or a lower `scale_factor`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The upscaled image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalUpscaleNode/en.md)

* * *

**Source fingerprint (SHA-256):** `38c90cf7054a93477ee63c356c3fdf8ba38c7edaf1a337da7ac366cd9d746d9e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClarityCrystalUpscaleNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClarityCrystalUpscaleNode)

[ByteDanceSeedreamNodeV3 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamNodeV3)[GeminiImage2Node - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GeminiImage2Node)

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
