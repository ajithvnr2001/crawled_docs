---
url: https://docs.comfy.org/built-in-nodes/LumaRay32VideoEditNode/
title: LumaRay32VideoEditNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.126029+00:00
---

# LumaRay32VideoEditNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaRay32VideoEditNode/

Luma

# LumaRay32VideoEditNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node re-renders an existing video under a new prompt using Luma Ray 3.2, allowing you to restyle, relight, add

Copy pageCopy page

## 

​

Overview

This node re-renders an existing video under a new prompt using Luma Ray 3.2, allowing you to restyle, relight, add, or remove elements while keeping the original motion. The source video can be up to 18 seconds, and the edited video retains the source’s original length.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Source video to edit. Up to 18 seconds.| VIDEO| Yes| -  
`prompt`| Describes the desired edit.| STRING| Yes| -  
`resolution`| The output resolution for the edited video. (default: “720p”)| COMBO| Yes| `"360p"`  
`"540p"`  
`"720p"`  
`"1080p"`  
`strength`| How strongly to preserve vs. reimagine the source. “auto” lets Ray 3.2 choose; adhere_* preserves the most, flex_* is balanced, reimagine_* changes the most. (default: “auto”)| COMBO| Yes| `"auto"`  
`"adhere_1"`  
`"adhere_2"`  
`"adhere_3"`  
`"flex_1"`  
`"flex_2"`  
`"flex_3"`  
`"reimagine_1"`  
`"reimagine_2"`  
`"reimagine_3"`  
`seed`| Seed for reproducibility.| INT| Yes| -  
  
**Note:** The `prompt` must be between 1 and 6000 characters. The source video must not exceed 18 seconds in duration.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The edited video output.| VIDEO  
`generation_id`| The unique identifier for the generation request.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/en.md)

* * *

**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaRay32VideoEditNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaRay32VideoEditNode)

[LumaRay32TextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaRay32TextToVideoNode)[LumaRay32VideoReframeNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaRay32VideoReframeNode)

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
