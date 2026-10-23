---
url: https://docs.comfy.org/built-in-nodes/ComfyAndNode/
title: ComfyAndNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.149497+00:00
---

# ComfyAndNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ComfyAndNode/

Logic

# ComfyAndNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The And node performs a logical AND operation on a group of input values.

Copy pageCopy page

The And node performs a logical AND operation on a group of input values. It returns `true` only when every connected value is considered truthy according to Python’s truthiness rules, which makes it useful for checking that several conditions are all met at the same time.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`values`| A growable group of values to evaluate. The node starts with one slot and you can add more by clicking the ”+” button on the node. Accepts any data type.| ANY| Yes| Minimum 1 (no maximum)  
  
**Note:** This input is a growable slot group. Slots are added individually (for example `value_1`, `value_2`, and so on), and at least one slot must be present. **Note:** The node uses Python’s truthiness rules to decide whether a value is `true` or `false`. For example, an empty string, the number 0, an empty list, and `None` are all treated as `false`. All other values are treated as `true`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`BOOLEAN`| Returns `true` if all input values are truthy, otherwise returns `false`.| BOOLEAN  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/en.md)

* * *

**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ComfyAndNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ComfyAndNode)

[ComboOptionTestNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ComboOptionTestNode)[ComfyNotNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ComfyNotNode)

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
