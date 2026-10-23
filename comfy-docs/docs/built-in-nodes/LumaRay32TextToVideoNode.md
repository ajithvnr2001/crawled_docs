---
url: https://docs.comfy.org/built-in-nodes/LumaRay32TextToVideoNode/
title: LumaRay32TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:27.920069+00:00
---

# LumaRay32TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaRay32TextToVideoNode/

Luma

# LumaRay32TextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video from a text prompt using Luma’s Ray 3.2 model.

Copy pageCopy page

This node generates a video from a text prompt using Luma’s Ray 3.2 model. It sends your prompt and video settings to the Luma API and returns the generated video along with a generation ID.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for the video generation.| STRING| Yes| 1 to 6000 characters  
`aspect_ratio`| The aspect ratio of the generated video.| STRING| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`"21:9"`  
`resolution`| The output resolution of the video (default: “720p”).| STRING| Yes| `"360p"`  
`"540p"`  
`"720p"`  
`"1080p"`  
`duration`| The duration of the generated video.| STRING| Yes| `"5s"`  
`"10s"`  
`loop`| Make the video loop seamlessly. Only available with 5s duration.| BOOLEAN| No| True/False (default: False)  
`seed`| Seed for reproducible generation.| INT| No| 0 to 2147483647  
  
**Note:** The `loop` parameter can only be enabled when `duration` is set to “5s”. If you set `duration` to ”10s” and enable `loop`, the node returns an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated video file.| VIDEO  
`generation_id`| The unique identifier for the video generation request.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32TextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `04358a872530e5a2622bf0f148a694f2c707ce8535586d8f860bdf9911e1fa6a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaRay32TextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaRay32TextToVideoNode)

[LumaRay32KeyframesToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaRay32KeyframesToVideoNode)[LumaRay32VideoEditNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaRay32VideoEditNode)

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
