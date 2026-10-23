---
url: https://docs.comfy.org/built-in-nodes/PikaTextToVideoNode2_2/
title: PikaTextToVideoNode2_2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:41.955826+00:00
---

# PikaTextToVideoNode2_2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PikaTextToVideoNode2_2/

Pika

# PikaTextToVideoNode2_2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Pika Text2Video v2.2 Node sends a text prompt to the Pika API version 2.2 to generate a video.

Copy pageCopy page

The Pika Text2Video v2.2 Node sends a text prompt to the Pika API version 2.2 to generate a video. It converts your text description into a video using Pika’s AI video generation service. The node allows you to customize various aspects of the video generation process including aspect ratio, duration, and resolution.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt_text`| The main text description that describes what you want to generate in the video| STRING| Yes| -  
`negative_prompt`| Text describing what you don’t want to appear in the generated video| STRING| Yes| -  
`seed`| A number that controls the randomness of the generation for reproducible results| INT| Yes| -  
`resolution`| The resolution setting for the output video| STRING| Yes| -  
`duration`| The length of the video in seconds| INT| Yes| -  
`aspect_ratio`| Aspect ratio (width / height) (default: 1.7777777777777777)| FLOAT| No| 0.4 - 2.5  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file returned from the Pika API| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/en.md)

* * *

**Source fingerprint (SHA-256):** `b4287519f5d4cc4a1077a58fb13aa99697e3be038a0b382c4b4c9b0e53a0d8a8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PikaTextToVideoNode2_2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PikaTextToVideoNode2_2)

[Pikaswaps - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Pikaswaps)[PixVerse Image to Video - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-image-to-video)

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
