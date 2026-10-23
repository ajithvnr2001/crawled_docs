---
url: https://docs.comfy.org/built-in-nodes/ConditioningCombine/
title: ConditioningCombine - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:40.398358+00:00
---

# ConditioningCombine - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningCombine/

Image

# ConditioningCombine - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node combines two conditioning inputs into a single output, effectively merging their information.

Copy pageCopy page

This node combines two conditioning inputs into a single output, effectively merging their information. The two conditions are combined using list concatenation.

## 

​

Inputs

Parameter Name| Description| Data Type  
---|---|---  
`conditioning_1`| The first conditioning input to be combined. It has equal importance with `conditioning_2` in the combination process.| `CONDITIONING`  
`conditioning_2`| The second conditioning input to be combined. It has equal importance with `conditioning_1` in the combination process.| `CONDITIONING`  
  
## 

​

Outputs

Parameter Name| Description| Data Type  
---|---|---  
`conditioning`| The result of combining `conditioning_1` and `conditioning_2`, encapsulating the merged information.| `CONDITIONING`  
  
## 

​

Usage Scenarios

Compare the two groups below: the left side uses the ConditioningCombine node, while the right side shows normal output. ![Compare](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ConditioningCombine/compare.jpg?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=b12d255c2a5bc25704099f40aedabf0c) In this example, the two conditions used in `Conditioning Combine` have equivalent importance. Therefore, you can use different text encodings for image style, subject features, etc., allowing the prompt features to be output more completely. The second prompt uses the combined complete prompt, but semantic understanding may encode completely different conditions. Using this node, you can achieve:

  * Basic text merging: Connect the outputs of two `CLIP Text Encode` nodes to the two input ports of `Conditioning Combine`
  * Complex prompt combination: Combine positive and negative prompts, or separately encode main descriptions and style descriptions before merging
  * Conditional chain combination: Multiple `Conditioning Combine` nodes can be used in series to achieve gradual combination of multiple conditions



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningCombine.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningCombine)

[BatchImagesNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BatchImagesNode)[EmptyImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyImage)

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
