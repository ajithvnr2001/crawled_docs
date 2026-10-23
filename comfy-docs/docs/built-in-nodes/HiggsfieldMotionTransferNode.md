---
url: https://docs.comfy.org/built-in-nodes/HiggsfieldMotionTransferNode/
title: HiggsfieldMotionTransferNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:04.102934+00:00
---

# HiggsfieldMotionTransferNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HiggsfieldMotionTransferNode/

Higgsfield

# HiggsfieldMotionTransferNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Higgsfield Genjutsu Motion Transfer node recasts a video with new characters, locations or styles taken from reference images while keeping the motion

Copy pageCopy page

The **Higgsfield Genjutsu Motion Transfer** node recasts a video with new characters, locations or styles taken from reference images while keeping the motion, camera movement, timing and audio of the source clip. Connect the clip to restyle and one or more reference images that describe the new look, then describe the result in the prompt. The request is sent to the Higgsfield API and the generated video is returned.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use. Selecting a model reveals the parameters specific to it: `video`, `reference_images`, `prompt`, `resolution`, and `seed`.| DYNAMIC_COMBO| Yes| `"genjutsu-v1.0"`  
`video`| Source video whose motion, camera movement, timing and audio are kept. At least 4 seconds; only the first 30 seconds are used.| VIDEO| Yes| 4 to 30 seconds  
`reference_images`| Growable slot: connect 1 to 8 images (`image_1`, `image_2`, …) of the characters, locations or styles to use. A batched input counts once per image.| IMAGE| Yes| 1 to 8 images  
`prompt`| Optional. Describe the result, for example which reference replaces which person, or a new setting. (default: empty)| STRING| Yes| Any text  
`resolution`| Resolution of the output video. (default: `"720p"`)| COMBO| Yes| `"480p"`  
`"720p"`  
`"1080p"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. This parameter has “control after generate” functionality (default: 42).| INT| Yes| 0 to 2147483647  
  
The source video is validated before the request is sent: a clip shorter than 4 seconds is rejected, and a clip longer than 30 seconds is trimmed to its first 30 seconds. Its audio is carried over to the result. Reference images are uploaded first, and the total number of images across all connected slots cannot exceed 8, even though the node exposes eight slots. Higgsfield’s content moderation can reject the input or the result, which raises an error instead of returning a video.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The restyled video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiggsfieldMotionTransferNode/en.md)

* * *

**Source fingerprint (SHA-256):** `f0c30fb93dd2af8d564335290fdb6ff61c38e36ab62cef9641fd1aa81cc10cd2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HiggsfieldMotionTransferNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HiggsfieldMotionTransferNode)

[HeyGenVideoTranslateNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HeyGenVideoTranslateNode)[HitPawVideoEnhance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HitPawVideoEnhance)

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
