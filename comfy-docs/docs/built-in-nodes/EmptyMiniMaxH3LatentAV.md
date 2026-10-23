---
url: https://docs.comfy.org/built-in-nodes/EmptyMiniMaxH3LatentAV/
title: EmptyMiniMaxH3LatentAV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:53.523797+00:00
---

# EmptyMiniMaxH3LatentAV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyMiniMaxH3LatentAV/

Minimax

# EmptyMiniMaxH3LatentAV - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates an empty latent that combines both video and audio information for the MiniMax H3 model.

Copy pageCopy page

This node creates an empty latent that combines both video and audio information for the MiniMax H3 model. You define the width, height, and length of the content, and the node produces a blank latent that the model can use as a starting point for generation. The duration (length) is automatically adjusted to fit the model’s required frame grid of 17k+5 frames at 24 fps.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent in pixels. Values must be multiples of 32. Default: 1344.| INT| Yes| 32 - MAX_RESOLUTION (step 32)  
`height`| The height of the latent in pixels. Values must be multiples of 32. Default: 768.| INT| Yes| 32 - MAX_RESOLUTION (step 32)  
`length`| Frame count at 24 fps, snapped up to the model’s 17k+5 grid (124 = ~5s; trained range is ~124-362, longer is untested). Default: 124.| INT| Yes| 5 - 3600 (step 17)  
  
Note: The `length` value is snapped up to the next frame count that fits the model’s 17k+5 grid (17 x k + 5 frames, such as 5, 22, 39, 56, 73, 90, 107, 124, and so on). The `width` and `height` values must be multiples of 32. The maximum resolution is the system-defined value in ComfyUI.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latent`| The generated empty joint video+audio latent for MiniMax H3, sized according to the input width, height, and length.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxH3LatentAV/en.md)

* * *

**Source fingerprint (SHA-256):** `ee24f4ac630858d87b9b98bb402689a5790e0ed882ec47dffe7b497216e37a5c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyMiniMaxH3LatentAV.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyMiniMaxH3LatentAV)

[LTXVSeparateAVLatent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVSeparateAVLatent)[EmptyMiniMaxMusic3LatentAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyMiniMaxMusic3LatentAudio)

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
