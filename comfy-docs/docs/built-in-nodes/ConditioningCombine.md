---
url: https://docs.comfy.org/built-in-nodes/ConditioningCombine/
title: Conditioning (Combine) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:07:55.309050+00:00
---

# Conditioning (Combine) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningCombine/

Image

# Conditioning (Combine) - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node combines two conditioning inputs into a single output, effectively merging their information.

Copy pageCopy page

This node combines two conditioning inputs into a single output, effectively merging their information. The two conditions are combined using list concatenation.

## Inputs

Parameter Name| Description| Data Type  
---|---|---  
`conditioning_1`| The first conditioning input to be combined. It has equal importance with `conditioning_2` in the combination process.| `CONDITIONING`  
`conditioning_2`| The second conditioning input to be combined. It has equal importance with `conditioning_1` in the combination process.| `CONDITIONING`  
  
## Outputs

Parameter Name| Description| Data Type  
---|---|---  
`conditioning`| The result of combining `conditioning_1` and `conditioning_2`, encapsulating the merged information.| `CONDITIONING`  
  
## Usage Scenarios

Compare the two groups below: the left side uses the ConditioningCombine node, while the right side shows normal output. ![Compare](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ConditioningCombine/compare.jpg?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=b12d255c2a5bc25704099f40aedabf0c) In this example, the two conditions used in `Conditioning Combine` carry equal weight. This lets you use separate text encodings for the image style, subject features, etc., which can help each part of your prompt be captured more accurately. The second prompt uses the combined complete prompt, but semantic understanding may encode completely different conditions. Using this node, you can achieve:

  * Basic text merging: Connect the outputs of two `CLIP Text Encode` nodes to the two input ports of `Conditioning Combine`
  * Complex prompt combination: Combine positive and negative prompts, or separately encode main descriptions and style descriptions before merging
  * Conditional chain combination: Multiple `Conditioning Combine` nodes can be used in series to achieve gradual combination of multiple conditions



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningCombine.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningCombine)

[Batch Images](https://docs.comfy.org/built-in-nodes/BatchImagesNode)[Empty Image](https://docs.comfy.org/built-in-nodes/EmptyImage)
