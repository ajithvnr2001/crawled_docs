---
url: https://docs.comfy.org/built-in-nodes/LumaRay32ExtendVideoNode/
title: LumaRay32ExtendVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:27.626655+00:00
---

# LumaRay32ExtendVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaRay32ExtendVideoNode/

Luma

# LumaRay32ExtendVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Luma Ray 3.2 Extend Video continues a previous Luma Ray 3.2 video generation by creating a new 5-second segment either after the original clip (forward)

Copy pageCopy page

Luma Ray 3.2 Extend Video continues a previous Luma Ray 3.2 video generation by creating a new 5-second segment either after the original clip (forward) or before it (backward). Connect the `generation_id` output from an earlier Luma Ray 3.2 node to use that clip as the starting frame (forward) or ending frame (backward) of the extension. Extensions are always 5 seconds long.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`source_generation_id`| Generation ID of the prior Ray 3.2 video to extend. Connect the `generation_id` output of another Luma Ray 3.2 node. Default: "" (empty). This value is required and must not be empty.| STRING| Yes| –  
`direction`| Forward continues after the prior clip; backward is prepended before it. Forward uses the source clip as the starting frame; backward uses it as the ending frame. Selecting “Forward (continue after)” adds the `loop` option.| DYNAMIC_COMBO| Yes| ”Forward (continue after)"  
"Backward (lead-in before)“  
`prompt`| Text prompt for the new content. Default: "" (empty). Must be between 1 and 6000 characters.| STRING| Yes| 1 to 6000 characters  
`resolution`| Output resolution for the extended video segment. Default: “720p”.| COMBO| Yes| ”540p"  
"720p"  
"1080p”  
`seed`| Seed to determine if node should re-run; results are nondeterministic regardless of seed. Default: 0.| INT| Yes| 0 to 0xFFFFFFFFFFFFFFFF (18446744073709551615)  
  
### 

​

Forward (continue after) Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`loop`| Loop the extended video seamlessly (forward extend only). Default: False.| BOOLEAN| No| True  
False  
  
### 

​

Backward (lead-in before) Inputs

This direction adds no additional parameters. **Note:** Extensions are always 5 seconds. The `loop` parameter is only available when `direction` is “Forward (continue after)”; when using “Backward (lead-in before)”, the `loop` option is not available. The `prompt` must be between 1 and 6000 characters. The `source_generation_id` is required and must be connected from a prior Luma Ray 3.2 node’s `generation_id` output.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated 5-second extended video segment.| VIDEO  
`generation_id`| Unique identifier for this generation, which can be connected to another Luma Ray 3.2 Extend Video node for further extensions.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaRay32ExtendVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaRay32ExtendVideoNode)

[LumaImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaImageToVideoNode)[LumaRay32ImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaRay32ImageToVideoNode)

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
