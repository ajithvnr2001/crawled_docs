---
url: https://docs.comfy.org/built-in-nodes/ConditioningAverage/
title: ConditioningAverage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:40.089113+00:00
---

# ConditioningAverage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningAverage/

Conditioning

# ConditioningAverage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ConditioningAverage node is used to blend two different sets of conditioning (such as text prompts) according to a specified weight

Copy pageCopy page

The `ConditioningAverage` node is used to blend two different sets of conditioning (such as text prompts) according to a specified weight, generating a new conditioning vector that lies between the two. By adjusting the weight parameter, you can flexibly control the influence of each conditioning on the final result. This is especially suitable for prompt interpolation, style fusion, and other advanced use cases. As shown below, by adjusting the strength of `conditioning_to`, you can output a result between the two conditionings. ![example](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ConditioningAverage/example.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=11b0e3044d3ac1c7c571c7e8b60ec6be)

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning_to`| The target conditioning vector, serving as the main base for the weighted average.| `CONDITIONING`  
`conditioning_from`| The source conditioning vector, which will be blended into the target according to a certain weight.| `CONDITIONING`  
`conditioning_to_strength`| The strength of the target conditioning, range 0.0-1.0, default 1.0, step 0.01.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning`| The resulting conditioning vector after blending, reflecting the weighted average.| `CONDITIONING`  
  
## 

​

Typical Use Cases

  * **Prompt Interpolation:** Smoothly transition between two different text prompts, generating content with intermediate style or semantics.
  * **Style Fusion:** Combine different artistic styles or semantic conditions to create novel effects.
  * **Strength Adjustment:** Precisely control the influence of a particular conditioning on the result by adjusting the weight.
  * **Creative Exploration:** Explore diverse generative effects by mixing different prompts.



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningAverage/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningAverage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningAverage)

[SvdImg2vidConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SvdImg2vidConditioning)[Sd4xupscaleConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Sd4xupscaleConditioning)

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
