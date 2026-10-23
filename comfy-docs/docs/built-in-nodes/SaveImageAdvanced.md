---
url: https://docs.comfy.org/built-in-nodes/SaveImageAdvanced/
title: SaveImageAdvanced - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:58.919959+00:00
---

# SaveImageAdvanced - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveImageAdvanced/

Image

# SaveImageAdvanced - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Save Image (Advanced) node saves the input images to your ComfyUI output directory with advanced control over file format, bit depth, and color space.

Copy pageCopy page

The **Save Image (Advanced)** node saves the input images to your ComfyUI output directory with advanced control over file format, bit depth, and color space. It supports saving as PNG, EXR, or AVIF files (including animated AVIF) and can embed workflow metadata into the saved files.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The images to save.| IMAGE| Yes| -  
`filename_prefix`| The prefix for the file to save. May include formatting tokens such as `%date:yyyy-MM-dd%` or `%Empty Latent Image.width%`. (default: “ComfyUI”)| STRING| Yes| -  
`format`| The file format in which to save the image. Selecting a format reveals additional options for that format.| DYNAMIC_COMBO| Yes| `"png"`  
`"exr"`  
`"avif"`  
  
### 

​

PNG Inputs

These options appear when `format` is set to `"png"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`bit_depth`| The bit depth for the saved PNG file. (default: “8-bit”)| COMBO| Yes (conditional)| `"8-bit"`  
`"16-bit"`  
`input_color_space`| Colorspace of the input tensor. Only sRGB is available for PNG format. (default: “sRGB”)| COMBO| Yes (conditional)| `"sRGB"`  
  
### 

​

EXR Inputs

These options appear when `format` is set to `"exr"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`bit_depth`| The bit depth for the saved EXR file. (default: “16-bit float”)| COMBO| Yes (conditional)| `"16-bit float"`  
`"32-bit float"`  
`input_color_space`| Colorspace of the input tensor. The EXR is always written as scene-linear in the matching gamut.  
`"sRGB"` — input is sRGB-encoded Rec.709; the inverse sRGB EOTF is applied.  
`"HDR"` — input is HLG-encoded Rec.2020 (BT.2100); the inverse HLG OETF is applied to get scene-linear light.  
`"linear"` — input is already scene-linear (Rec.709 primaries); written through unchanged. Use this for renderer/compositor output. (default: “sRGB”)| COMBO| Yes (conditional)| `"sRGB"`  
`"HDR"`  
`"linear"`  
  
### 

​

AVIF Inputs

These options appear when `format` is set to `"avif"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`bit_depth`| The bit depth for the saved AVIF file. Auto uses 8-bit YUV420 for sRGB and 10-bit YUV420 for HDR. (default: “auto”)| COMBO| Yes (conditional)| `"auto"`  
`"8-bit YUV420"`  
`"10-bit YUV420"`  
`input_color_space`| Colorspace of the input images. HDR selects BT.2020/HLG and HDR PQ selects BT.2020/PQ. (default: “sRGB”)| COMBO| Yes (conditional)| `"sRGB"`  
`"HDR"`  
`"HDR PQ"`  
`crf`| Lower values produce higher quality and larger files. (default: 18)| INT| Yes (conditional)| 1 to 63  
`save_mode`| The save mode for the AVIF file. `"still images"` saves each image in the batch as a separate still file; `"animated"` saves the entire batch as a single animated AVIF file and reveals `fps` and `loop_count`. (default: “still images”)| DYNAMIC_COMBO| Yes (conditional)| `"still images"`  
`"animated"`  
  
### 

​

AVIF Animated Options

These options appear when `save_mode` is set to `"animated"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`fps`| The frame rate of the animation. (default: 6.0)| FLOAT| Yes (conditional)| 0.01 to 1000.0  
`loop_count`| Number of times to loop the animation. 0 loops forever. (default: 0)| INT| Yes (conditional)| 0 to 1000  
  
**Notes on Parameter Dependencies:**

  * The format-specific parameters (`bit_depth`, `input_color_space`, and for AVIF also `crf` and `save_mode`) are only available when a specific `format` is selected.
  * For PNG format, only “8-bit” and “16-bit” bit depths are available, and only “sRGB” color space.
  * For EXR format, both “16-bit float” and “32-bit float” bit depths are available, with “sRGB”, “HDR”, or “linear” color spaces. “16-bit float” is the default and produces smaller files.
  * For AVIF format, `fps` and `loop_count` are only available when `save_mode` is set to `"animated"`.
  * PNG and EXR images must have 1 (grayscale), 3 (RGB), or 4 (RGBA) channels; other channel counts are not supported and raise an error.
  * AVIF supports only 1-channel grayscale and 3-channel RGB images; RGBA (alpha) images are not supported and raise an error.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The input images, passed through unchanged. The node’s UI output provides a list of saved image results, each containing the filename, subfolder, and type (“output”). For animated AVIF with more than one image, the UI output also includes an `animated` flag.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/en.md)

* * *

**Source fingerprint (SHA-256):** `a0f7fccb3b25ffa814bf5d2a970c41fd4114368eb9a9998880b1108a272a41bb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveImageAdvanced.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveImageAdvanced)

[SaveImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveImage)[SaveImageDataSetToFolder - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveImageDataSetToFolder)

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
