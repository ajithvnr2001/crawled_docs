---
url: https://docs.comfy.org/built-in-nodes/CreateVideo/
title: CreateVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.471817+00:00
---

# CreateVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateVideo/

Video

# CreateVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Create Video node combines a sequence of images into a video.

Copy pageCopy page

The Create Video node combines a sequence of images into a video. You can set the playback speed in frames per second, optionally add audio, and choose the compression format, bit depth, and color space of the resulting video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The images to create a video from.| IMAGE| Yes| -  
`fps`| The frames per second for the video playback speed (default: 30.0).| FLOAT| Yes| 1.0 - 120.0  
`audio`| The audio to add to the video.| AUDIO| No| -  
`bit_depth`| Auto uses 8-bit for sRGB and 10-bit for HDR and HDR PQ. Explicit 8-bit and 10-bit choices are independent of colorspace. (default: “auto”)| COMBO| No| `"auto"`  
8  
10  
`color_space`| Colorspace of the input images. HDR selects BT.2020/HLG and HDR PQ selects BT.2020/PQ. (default: “sRGB”)| COMBO| No| `"sRGB"`  
`"HDR"`  
`"HDR PQ"`  
`codec`| Optionally encode the video immediately. None keeps the images in tensor form; Auto uses H.264. (default: “none”)| COMBO| No| `"none"`  
Available video codec options from the video codec list (e.g. `"auto"` and other supported codecs)  
  
Note: When `bit_depth` is set to `"auto"`, the node automatically uses 10-bit for the HDR and HDR PQ color spaces, and 8-bit for sRGB. Note: The `codec` parameter is an advanced option. When it is left at `"none"`, the output stays in tensor form; selecting any other codec encodes the video immediately.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video containing the input images and optional audio.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `9274559caabbafbcaad47883bf017967f9685f155ea1031e66cf22ee8d0d14c3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateVideo)

[ConcatenateVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConcatenateVideo)[FrameInterpolate - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FrameInterpolate)

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
