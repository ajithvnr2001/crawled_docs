---
url: https://docs.comfy.org/built-in-nodes/SeedVR2PostProcessing/
title: SeedVR2PostProcessing - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:00.193140+00:00
---

# SeedVR2PostProcessing - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SeedVR2PostProcessing/

Post Processors

# SeedVR2PostProcessing - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node aligns the generated image with the original resized image and applies optional color correction.

Copy pageCopy page

This node aligns the generated image with the original resized image and applies optional color correction. It takes the output from a SeedVR2 upscaling process and adjusts it to match the colors and dimensions of the original reference image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The generated image to process.| IMAGE| Yes| -  
`original_resized_images`| The original resized image before pre-processing, used as reference.| IMAGE| Yes| -  
`color_correction_method`| Method to match the generated image colors to the original image. lab: transfer color in CIELAB space, preserving detail (most faithful). wavelet: transfer low-frequency color, keeping upscaled high-frequency detail. adain: match per-channel mean/std (fastest, global tint). none: skip color transfer (geometry alignment only). (default: “lab”)| COMBO| Yes| `"lab"`  
`"wavelet"`  
`"adain"`  
`"none"`  
  
**Note:** Both inputs may be 4-D (batch, height, width, channels) or 5-D (batch, frames, height, width, channels) tensors. The node crops both to the smallest batch, frame count, height, and width, so they do not need to match exactly. When a color correction method other than `none` is used, the reference image is resized to the output size first. Color correction is processed in memory-aware chunks, backing off to a smaller chunk size if memory runs out. Output height and width are rounded down to even numbers. If the reference image has an alpha channel (4 channels), that alpha channel is preserved and applied to the output.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The aligned, color-corrected image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/en.md)

* * *

**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SeedVR2PostProcessing.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SeedVR2PostProcessing)

[VOIDQuadmaskPreprocess - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VOIDQuadmaskPreprocess)[SeedVR2Preprocess - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SeedVR2Preprocess)

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
