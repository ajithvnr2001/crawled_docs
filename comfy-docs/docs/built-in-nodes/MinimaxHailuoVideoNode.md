---
url: https://docs.comfy.org/built-in-nodes/MinimaxHailuoVideoNode/
title: MinimaxHailuoVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:33.337476+00:00
---

# MinimaxHailuoVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MinimaxHailuoVideoNode/

Minimax

# MinimaxHailuoVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates videos from text prompts using the MiniMax Hailuo-02 model.

Copy pageCopy page

Generates videos from text prompts using the MiniMax Hailuo-02 model. You can optionally provide a starting image to use as the first frame, which creates a video that continues from that image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt_text`| Text prompt to guide the video generation (default: empty).| STRING| Yes| -  
`seed`| The random seed used for creating the noise (default: 0).| INT| No| 0 to 18446744073709551615  
`first_frame_image`| Optional image to use as the first frame to generate a video.| IMAGE| No| -  
`prompt_optimizer`| Optimize prompt to improve generation quality when needed (default: True).| BOOLEAN| No| True  
False  
`duration`| The length of the output video in seconds (default: 6).| COMBO| No| 6  
10  
`resolution`| The dimensions of the video display. 1080p is 1920x1080, 768p is 1366x768 (default: “768P”).| COMBO| No| ”768P"  
"1080P”  
  
**Note:** When `resolution` is set to “1080P”, `duration` is limited to 6 seconds. When `first_frame_image` is not provided, `prompt_text` must not be empty.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MinimaxHailuoVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MinimaxHailuoVideoNode)

[MinimaxHailuo03TextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MinimaxHailuo03TextToVideoNode)[MinimaxImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MinimaxImageToVideoNode)

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
