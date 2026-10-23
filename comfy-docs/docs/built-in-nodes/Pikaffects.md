---
url: https://docs.comfy.org/built-in-nodes/Pikaffects/
title: Pikaffects - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:42.319679+00:00
---

# Pikaffects - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Pikaffects/

Pika

# Pikaffects - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Pikaffects node generates videos with various visual effects applied to an input image.

Copy pageCopy page

The Pikaffects node generates videos with various visual effects applied to an input image. It uses Pika’s video generation API to transform static images into animated videos with specific effects like melting, exploding, or levitating. The node requires an API key and authentication token to access the Pika service.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The reference image to apply the Pikaffect to.| IMAGE| Yes| -  
`pikaffect`| The specific visual effect to apply to the image (default: “Cake-ify”).| COMBO| Yes| ”Cake-ify"  
"Crumble"  
"Crush"  
"Decapitate"  
"Deflate"  
"Dissolve"  
"Explode"  
"Eye-pop"  
"Inflate"  
"Levitate"  
"Melt"  
"Peel"  
"Poke"  
"Squish"  
"Ta-da"  
"Tear”  
`prompt_text`| Text description guiding the video generation.| STRING| Yes| -  
`negative_prompt`| Text description of what to avoid in the generated video.| STRING| Yes| -  
`seed`| Random seed value for reproducible results.| INT| Yes| 0 to 4294967295  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video with the applied Pikaffect.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/en.md)

* * *

**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Pikaffects.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Pikaffects)

[Pikadditions - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Pikadditions)[PikaImageToVideoNode2_2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PikaImageToVideoNode2_2)

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
