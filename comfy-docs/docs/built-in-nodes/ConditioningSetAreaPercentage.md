---
url: https://docs.comfy.org/built-in-nodes/ConditioningSetAreaPercentage/
title: ConditioningSetAreaPercentage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:41.704446+00:00
---

# ConditioningSetAreaPercentage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningSetAreaPercentage/

Transform

# ConditioningSetAreaPercentage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ConditioningSetAreaPercentage node specializes in adjusting the area of influence for conditioning elements based on percentage values.

Copy pageCopy page

The ConditioningSetAreaPercentage node specializes in adjusting the area of influence for conditioning elements based on percentage values. It allows for the specification of the area’s dimensions and position as percentages of the total image size, alongside a strength parameter to modulate the intensity of the conditioning effect.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`CONDITIONING`| Represents the conditioning elements to be modified, serving as the foundation for applying area and strength adjustments.| CONDITIONING  
`width`| Specifies the width of the area as a percentage of the total image width, influencing how much of the image the conditioning affects horizontally.| `FLOAT`  
`height`| Determines the height of the area as a percentage of the total image height, affecting the vertical extent of the conditioning’s influence.| `FLOAT`  
`x`| Indicates the horizontal starting point of the area as a percentage of the total image width, positioning the conditioning effect.| `FLOAT`  
`y`| Specifies the vertical starting point of the area as a percentage of the total image height, positioning the conditioning effect.| `FLOAT`  
`strength`| Controls the intensity of the conditioning effect within the specified area, allowing for fine-tuning of its impact.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`CONDITIONING`| Returns the modified conditioning elements with updated area and strength parameters, ready for further processing or application.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningSetAreaPercentage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningSetAreaPercentage)

[ConditioningSetArea - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningSetArea)[ConditioningSetAreaPercentageVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningSetAreaPercentageVideo)

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
