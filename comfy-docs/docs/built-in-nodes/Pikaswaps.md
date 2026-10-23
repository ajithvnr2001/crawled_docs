---
url: https://docs.comfy.org/built-in-nodes/Pikaswaps/
title: Pikaswaps - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:42.152533+00:00
---

# Pikaswaps - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Pikaswaps/

Pika

# Pikaswaps - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Pika Swaps node replaces objects or regions in your video with a new image.

Copy pageCopy page

The Pika Swaps node replaces objects or regions in your video with a new image. You define the areas to replace using a mask, and the node seamlessly swaps the specified content throughout the video sequence.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The video to swap an object in.| VIDEO| Yes| -  
`image`| The image used to replace the masked object in the video.| IMAGE| Yes| -  
`mask`| Use the mask to define areas in the video to replace.| MASK| Yes| -  
`prompt_text`| Text prompt describing the desired replacement.| STRING| Yes| -  
`negative_prompt`| Text prompt describing what to avoid in the replacement.| STRING| Yes| -  
`seed`| Random seed value for consistent results.| INT| Yes| 0 to 4294967295  
  
**Note:** This node requires all input parameters to be provided. The `video`, `image`, and `mask` work together to define the replacement operation, where the mask specifies which areas of the video will be replaced with the provided image.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The processed video with the specified object or region replaced.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/en.md)

* * *

**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Pikaswaps.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Pikaswaps)

[PikaStartEndFrameNode2_2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PikaStartEndFrameNode2_2)[PikaTextToVideoNode2_2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PikaTextToVideoNode2_2)

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
