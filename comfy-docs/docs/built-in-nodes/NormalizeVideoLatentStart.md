---
url: https://docs.comfy.org/built-in-nodes/NormalizeVideoLatentStart/
title: NormalizeVideoLatentStart - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:38.865379+00:00
---

# NormalizeVideoLatentStart - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/NormalizeVideoLatentStart/

Conditioning

# NormalizeVideoLatentStart - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node adjusts the first few frames of a video latent to make them look more like the frames that come after.

Copy pageCopy page

This node adjusts the first few frames of a video latent to make them look more like the frames that come after. It calculates the average and variation from a set of reference frames later in the video and applies those same characteristics to the starting frames. This helps reduce differences between the starting frames and the rest of the video, creating a smoother and more consistent transition.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latent`| The video latent representation to process.| LATENT| Yes| -  
`start_frame_count`| Number of latent frames to normalize, counted from the start (default: 4).| INT| Yes| 1 to 16384 (max resolution)  
`reference_frame_count`| Number of latent frames after the start frames to use as reference (default: 5).| INT| Yes| 1 to 16384 (max resolution)  
  
**Note:** The reference frames are taken starting right after the `start_frame_count` frames. If there are fewer frames available than `reference_frame_count` requests, the node uses however many are available (at most one less than the total frame count of the latent). If the video latent has only 1 frame, no normalization is performed and the original latent is returned unchanged.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latent`| The processed video latent with the starting frames normalized.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/en.md)

* * *

**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/NormalizeVideoLatentStart.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/NormalizeVideoLatentStart)

[InpaintModelConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/InpaintModelConditioning)[PiDConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PiDConditioning)

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
