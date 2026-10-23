---
url: https://docs.comfy.org/built-in-nodes/ComfySwitchNode/
title: ComfySwitchNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:40.543767+00:00
---

# ComfySwitchNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ComfySwitchNode/

Logic

# ComfySwitchNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The If/Else Switch node selects between two possible inputs based on a boolean condition.

Copy pageCopy page

The If/Else Switch node selects between two possible inputs based on a boolean condition. When `switch` is enabled (true), it passes the `on_true` input through to the output; when disabled (false), it passes `on_false`. The inputs are lazy, so only the selected branch is evaluated and the other input does not need to be connected.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`switch`| A boolean condition that determines which input is passed to the output. When enabled (true), the `on_true` input is selected. When disabled (false), the `on_false` input is selected.| BOOLEAN| Yes|   
`on_false`| The data to be passed to the output when `switch` is disabled (false). This input is requested only when `switch` is false.| MATCH_TYPE| No|   
`on_true`| The data to be passed to the output when `switch` is enabled (true). This input is requested only when `switch` is true.| MATCH_TYPE| No|   
  
**Note on Input Requirements:** The `on_false` and `on_true` inputs are conditionally requested. The node asks for `on_true` only when `switch` is true, and asks for `on_false` only when `switch` is false. Both inputs must be of the same data type, and that type must match the output data type. If the selected input is not connected, the node outputs no value.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The selected data: the value from `on_true` when `switch` is true, or the value from `on_false` when `switch` is false.| MATCH_TYPE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/en.md)

* * *

**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ComfySwitchNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ComfySwitchNode)

[ComfySoftSwitchNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ComfySoftSwitchNode)[ConvertStringToComboNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConvertStringToComboNode)

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
