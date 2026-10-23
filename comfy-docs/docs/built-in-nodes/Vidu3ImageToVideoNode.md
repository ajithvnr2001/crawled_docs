---
url: https://docs.comfy.org/built-in-nodes/Vidu3ImageToVideoNode/
title: Vidu3ImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.890367+00:00
---

# Vidu3ImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Vidu3ImageToVideoNode/

Vidu

# Vidu3ImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Vidu Q3 Image-to-Video Generation node creates a video sequence starting from an input image.

Copy pageCopy page

The Vidu Q3 Image-to-Video Generation node creates a video sequence starting from an input image. It uses a Vidu Q3 model to animate the image, optionally guided by a text prompt, and outputs a video file.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for video generation.| DYNAMIC_COMBO| Yes| `"viduq3-pro"`  
`"viduq3-turbo"`  
`image`| An image to be used as the start frame of the generated video.| IMAGE| Yes| -  
`prompt`| An optional text prompt for video generation (max 2000 characters) (default: empty).| STRING| Yes| -  
`seed`| The seed value used to control the randomness of the generation (default: 1).| INT| Yes| 0 to 2147483647  
  
### 

​

viduq3-pro Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`resolution`| Resolution of the output video.| COMBO| Yes| `"720p"`  
`"1080p"`  
`"2K"`  
`duration`| Duration of the output video in seconds (default: 5).| INT| Yes| 1 to 16  
`audio`| When enabled, outputs video with sound (including dialogue and sound effects) (default: False).| BOOLEAN| Yes| `True`  
`False`  
  
### 

​

viduq3-turbo Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`resolution`| Resolution of the output video.| COMBO| Yes| `"720p"`  
`"1080p"`  
`duration`| Duration of the output video in seconds (default: 5).| INT| Yes| 1 to 16  
`audio`| When enabled, outputs video with sound (including dialogue and sound effects) (default: False).| BOOLEAN| Yes| `True`  
`False`  
  
**Note:** The `image` must have an aspect ratio between 1:4 and 4:1 (portrait to landscape). The `prompt` is optional but cannot exceed 2000 characters. The available `resolution` options depend on the selected model: `"viduq3-pro"` supports `"720p"`, `"1080p"`, and `"2K"`; `"viduq3-turbo"` supports `"720p"` and `"1080p"`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `77500d1e19928128decc010540670e311cd8ec4fcad913412517f47f0e27e15f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Vidu3ImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Vidu3ImageToVideoNode)

[Vidu2TextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Vidu2TextToVideoNode)[Vidu3StartEndToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Vidu3StartEndToVideoNode)

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
