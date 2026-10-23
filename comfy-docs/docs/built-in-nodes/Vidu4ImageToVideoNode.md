---
url: https://docs.comfy.org/built-in-nodes/Vidu4ImageToVideoNode/
title: Vidu4ImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:21.215456+00:00
---

# Vidu4ImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Vidu4ImageToVideoNode/

Vidu

# Vidu4ImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate a video from a start frame and an optional prompt with a Vidu Q4 model.

Copy pageCopy page

Generate a video from a start frame and an optional prompt with a Vidu Q4 model. The output keeps the aspect ratio of the input image. Selecting a `model` reveals the parameters specific to that model.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Start frame of the generated video. Aspect ratio must be between 1:5 and 5:1.| IMAGE| Yes| N/A  
`model`| Model to use for video generation. Selecting a model reveals the parameters specific to it: `prompt`, `resolution`, `duration`, `audio`, and `seed`.| DYNAMIC_COMBO| Yes| `"Vidu Q4 Preview"`  
`prompt`| An optional text prompt for video generation, up to 5000 characters (default: empty).| STRING| Yes| Any text  
`resolution`| Resolution of the output video (default: `"720p"`).| COMBO| Yes| `"540p"`  
`"720p"`  
`"1080p"`  
`"2K"`  
`"4K"`  
`duration`| Duration of the output video in seconds (default: 5).| INT| Yes| 3 to 16  
`audio`| When enabled, outputs video with sound, including dialogue and sound effects (default: True).| BOOLEAN| Yes| `True`  
`False`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. This parameter has “control after generate” functionality (default: 42).| INT| Yes| 1 to 2147483647  
  
**Note:** The aspect ratio of `image` must stay between 1:5 and 5:1, and the `prompt` cannot exceed 5000 characters. The result keeps the aspect ratio of the input image, so the output size follows the `resolution` setting only within that ratio.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `8778696edbdfb821afaa99dcba09cbebff57fd4cd2378273e82ad9fb18600b62`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Vidu4ImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Vidu4ImageToVideoNode)

[Vidu3TextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Vidu3TextToVideoNode)[Vidu4ReferenceVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Vidu4ReferenceVideoNode)

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
