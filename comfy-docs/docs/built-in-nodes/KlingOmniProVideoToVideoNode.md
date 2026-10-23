---
url: https://docs.comfy.org/built-in-nodes/KlingOmniProVideoToVideoNode/
title: KlingOmniProVideoToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:15.286944+00:00
---

# KlingOmniProVideoToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingOmniProVideoToVideoNode/

Kling

# KlingOmniProVideoToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node uses the Kling AI model to generate a new video based on an input video and optional reference images.

Copy pageCopy page

This node uses the Kling AI model to generate a new video based on an input video and optional reference images. You provide a text prompt describing the desired content, and the node transforms the reference video accordingly. It can also incorporate up to four additional reference images to guide the style and content of the output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| The specific Kling model to use for video generation (default: “kling-v3-omni”).| COMBO| Yes| `"kling-v3-omni"`  
`"kling-video-o1"`  
`prompt`| A text prompt describing the video content. This can include both positive and negative descriptions.| STRING| Yes| N/A  
`aspect_ratio`| The desired aspect ratio for the generated video.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`duration`| The length of the generated video in seconds (default: 3).| INT| Yes| 3 to 10  
`reference_video`| Video to use as a reference.| VIDEO| Yes| N/A  
`keep_original_sound`| Determines if the audio from the reference video is kept in the output (default: True).| BOOLEAN| Yes| N/A  
`reference_images`| Up to 4 additional reference images.| IMAGE| No| N/A  
`resolution`| The resolution for the generated video (default: “1080p”).| COMBO| No| `"1080p"`  
`"720p"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0).| INT| No| 0 to 2147483647  
  
**Parameter Constraints:**

  * The `prompt` must be between 1 and 2500 characters long.
  * The `reference_video` must be between 3.0 and 10.05 seconds in duration.
  * The `reference_video` must have dimensions between 720x720 and 2160x2160 pixels.
  * A maximum of 4 `reference_images` can be provided. Each image must be at least 300x300 pixels and have an aspect ratio between 1:2.5 and 2.5:1.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The newly generated video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `3dc2e3d153ddd9e6da705b764c51b4a859d66464b893fdebb0689d2ad5e870c7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingOmniProVideoToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingOmniProVideoToVideoNode)

[KlingOmniProTextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingOmniProTextToVideoNode)[KlingStartEndFrameNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingStartEndFrameNode)

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
