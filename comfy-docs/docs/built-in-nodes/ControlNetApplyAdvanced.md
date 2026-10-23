---
url: https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced/
title: ControlNetApplyAdvanced - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:43.520772+00:00
---

# ControlNetApplyAdvanced - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced/

Controlnet

# ControlNetApplyAdvanced - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies advanced control net transformations to conditioning data based on an image and a control net model.

Copy pageCopy page

This node applies advanced control net transformations to conditioning data based on an image and a control net model. It allows for fine-tuned adjustments of the control net’s influence over the generated content, enabling more precise and varied modifications to the conditioning.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`positive`| The positive conditioning data to which the control net transformations will be applied. It represents the desired attributes or features to enhance or maintain in the generated content.| `CONDITIONING`  
`negative`| The negative conditioning data, representing attributes or features to diminish or remove from the generated content. The control net transformations are applied to this data as well, allowing for a balanced adjustment of the content’s characteristics.| `CONDITIONING`  
`control_net`| The control net model is crucial for defining the specific adjustments and enhancements to the conditioning data. It interprets the reference image and strength parameters to apply transformations, significantly influencing the final output by modifying attributes in both positive and negative conditioning data.| `CONTROL_NET`  
`image`| The image serving as a reference for the control net transformations. It influences the adjustments made by the control net to the conditioning data, guiding the enhancement or suppression of specific features.| `IMAGE`  
`strength`| A scalar value determining the intensity of the control net’s influence on the conditioning data. Higher values result in more pronounced adjustments.| `FLOAT`  
`start_percent`| The starting percentage of the control net’s effect, allowing for gradual application of transformations over a specified range.| `FLOAT`  
`end_percent`| The ending percentage of the control net’s effect, defining the range over which the transformations are applied. This enables more nuanced control over the adjustment process.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`positive`| The modified positive conditioning data after the application of control net transformations, reflecting the enhancements made based on the input parameters.| `CONDITIONING`  
`negative`| The modified negative conditioning data after the application of control net transformations, reflecting the suppression or removal of specific features based on the input parameters.| `CONDITIONING`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlnetApplyAdvanced/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ControlNetApplyAdvanced.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ControlNetApplyAdvanced)

[ControlNetApply - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ControlNetApply)[ControlNetApplySD3 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ControlNetApplySD3)

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
