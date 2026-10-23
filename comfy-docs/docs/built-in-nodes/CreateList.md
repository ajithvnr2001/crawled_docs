---
url: https://docs.comfy.org/built-in-nodes/CreateList/
title: CreateList - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.095469+00:00
---

# CreateList - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateList/

Utilities

# CreateList - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Create List node combines multiple inputs into a single, sequential list.

Copy pageCopy page

The Create List node combines multiple inputs into a single, sequential list. It accepts any number of input slots that share the same data type and concatenates their items in the order the slots are connected. The result is one list containing all connected items.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`inputs`| A variable number of input slots named `input`, `input_2`, `input_3`, and so on. Each slot accepts a list of items of the same data type (for example, all IMAGE or all STRING). New slots are created automatically as needed. The node concatenates the lists in slot order.| Any| Yes| Any number of slots; each slot accepts any number of items  
  
**Note:** All connected inputs must share the same data type. Each connected slot provides a list of items, and the node combines the lists in slot order (`input`, then `input_2`, then `input_3`, …). The node is also searchable under the aliases “Image Iterator”, “Text Iterator”, and “Iterator”.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`list`| A single list containing all items from the connected inputs, concatenated in the order the slots were provided. The output data type matches the input data type.| Any  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/en.md)

* * *

**Source fingerprint (SHA-256):** `4824fa6af46ab08cd3c10b033dbb3e43682b468e1dbd934fffb571349e025b96`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateList.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateList)

[CreateBoundingBoxes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CreateBoundingBoxes)[CurveEditor - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CurveEditor)

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
