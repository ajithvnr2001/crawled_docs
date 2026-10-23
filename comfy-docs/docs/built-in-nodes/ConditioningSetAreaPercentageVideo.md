---
url: https://docs.comfy.org/built-in-nodes/ConditioningSetAreaPercentageVideo/
title: ConditioningSetAreaPercentageVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:41.431244+00:00
---

# ConditioningSetAreaPercentageVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningSetAreaPercentageVideo/

Transform

# ConditioningSetAreaPercentageVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ConditioningSetAreaPercentageVideo node modifies conditioning data by defining a specific area and temporal region for video generation.

Copy pageCopy page

The ConditioningSetAreaPercentageVideo node modifies conditioning data by defining a specific area and temporal region for video generation. It uses percentage values relative to the overall dimensions to set the position, size, and duration of the area where the conditioning is applied. This is useful for focusing the generation on specific parts of a video sequence.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`conditioning`| The conditioning data to be modified| CONDITIONING| Yes| -  
`width`| The width of the area as a percentage of the total width (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step 0.01)  
`height`| The height of the area as a percentage of the total height (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step 0.01)  
`temporal`| The temporal duration of the area as a percentage of the total video length (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step 0.01)  
`x`| The horizontal starting position of the area as a percentage (default: 0.0)| FLOAT| Yes| 0.0 - 1.0 (step 0.01)  
`y`| The vertical starting position of the area as a percentage (default: 0.0)| FLOAT| Yes| 0.0 - 1.0 (step 0.01)  
`z`| The temporal starting position of the area as a percentage of the video timeline (default: 0.0)| FLOAT| Yes| 0.0 - 1.0 (step 0.01)  
`strength`| The strength multiplier applied to the conditioning within the defined area (default: 1.0)| FLOAT| Yes| 0.0 - 10.0 (step 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`conditioning`| The modified conditioning data with the specified area and strength settings applied| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningSetAreaPercentageVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningSetAreaPercentageVideo)

[ConditioningSetAreaPercentage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningSetAreaPercentage)[ConditioningSetAreaStrength - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningSetAreaStrength)

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
