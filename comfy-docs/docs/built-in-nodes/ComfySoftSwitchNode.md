---
url: https://docs.comfy.org/built-in-nodes/ComfySoftSwitchNode/
title: ComfySoftSwitchNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:39.896054+00:00
---

# ComfySoftSwitchNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ComfySoftSwitchNode/

Logic

# ComfySoftSwitchNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Soft Switch node selects between two possible input values based on a boolean condition.

Copy pageCopy page

The Soft Switch node selects between two possible input values based on a boolean condition. It outputs the value from the `on_true` input when the `switch` is true, and the value from the `on_false` input when the `switch` is false. This node is designed to be lazy, meaning it only evaluates the input that is actually needed based on the switch state.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`switch`| The boolean condition that determines which input to pass through. When true, the `on_true` input is selected. When false, the `on_false` input is selected.| BOOLEAN| Yes| True or False  
`on_false`| The value to output when the `switch` condition is false. This input is optional, but at least one of `on_false` or `on_true` must be connected.| MATCH_TYPE| No| Same data type as `on_true`  
`on_true`| The value to output when the `switch` condition is true. This input is optional, but at least one of `on_false` or `on_true` must be connected.| MATCH_TYPE| No| Same data type as `on_false`  
  
**Note:** The `on_false` and `on_true` inputs must be of the same data type, as defined by the node’s internal template. At least one of these two inputs must be connected, otherwise the node returns the validation message “At least one of on_false or on_true must be connected to Switch node”. Because the node is lazy, when only one input is connected, the node always outputs that input’s value regardless of the `switch` state.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The selected value. It matches the data type of the connected `on_false` or `on_true` input. When both inputs are connected, it outputs `on_true` if `switch` is true, and `on_false` if `switch` is false.| MATCH_TYPE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/en.md)

* * *

**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ComfySoftSwitchNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ComfySoftSwitchNode)

[ComfyOrNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ComfyOrNode)[ComfySwitchNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ComfySwitchNode)

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
