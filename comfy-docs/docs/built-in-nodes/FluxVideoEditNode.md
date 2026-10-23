---
url: https://docs.comfy.org/built-in-nodes/FluxVideoEditNode/
title: FluxVideoEditNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.523903+00:00
---

# FluxVideoEditNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxVideoEditNode/

BFL

# FluxVideoEditNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Edits an existing video clip from a written instruction.

Copy pageCopy page

Edits an existing video clip from a written instruction. You can remove, add, or replace objects, change the setting, restyle the footage, change on-screen text, or replace the spoken dialogue. The length, framing, camera motion, and audio come from the source clip, so anything you do not mention in the prompt is meant to stay as it was.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Source clip of 0.7 to 15 seconds, at least 160x160 pixels. The output is rendered at 24 fps and capped at about 0.9 megapixels per frame, so a larger source comes back smaller.| VIDEO| Yes| 0.7 to 15 seconds; minimum 160x160 pixels  
`prompt`| What to change, in plain language, up to 4096 characters. Anything you do not mention is meant to stay as it was. Replacement dialogue has to fit the time the original speech takes, and a silent clip stays silent. Default: empty string.| STRING| Yes| 1 to 4096 characters  
`auto_downscale`| Automatically downscale sources larger than 1280x704 pixels in area before upload. Aspect ratio is preserved; smaller videos are untouched. Default: true.| BOOLEAN| No| true  
false  
`safety_tolerance`| Moderation tolerance, 0 is the strictest. Default: 4.| INT| No| 0 to 4  
`seed`| Seed to determine if node should re-run; FLUX picks its own seed, so actual results are nondeterministic regardless of this value. Default: 42.| INT| No| 0 to 4294967295  
  
**Note:** The `prompt` must contain at least 1 character and no more than 4096 characters. The source `video` must be between 0.7 and 15 seconds long and at least 160x160 pixels; uploads that fall outside these limits are rejected before the request is sent.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The edited video clip returned by the FLUX service.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoEditNode/en.md)

* * *

**Source fingerprint (SHA-256):** `169b14700acfee3f6ccc247f08f3ae8c5f3c4610062a447e8215246460299b6a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxVideoEditNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxVideoEditNode)

[Flux3VideoContinuationNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Flux3VideoContinuationNode)[FluxVideoUpscaleNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxVideoUpscaleNode)

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
