---
url: https://docs.comfy.org/built-in-nodes/GetItemFromList/
title: GetItemFromList - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:29.018481+00:00
---

# GetItemFromList - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GetItemFromList/

Utilities

# GetItemFromList - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node returns a single item from a list, selected by its position.

Copy pageCopy page

This node returns a single item from a list, selected by its position. You provide the list and the index number of the item you want, and the node outputs that item. This makes it useful for picking one specific element out of a group of values, such as a particular image from a batch.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`list`| The list of values to select from. Because this node is marked as taking a list input, the connected value is handled as a group of items.| Any Type| Yes| Any list of values  
`index`| The position of the item to return. The value starts at 0, so `0` returns the first item, `1` returns the second item, and so on (default: 0).| INT| Yes| Any integer index  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`OUTPUT`| The single item located at the given `index` within the provided `list`.| Any Type  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetItemFromList/en.md)

* * *

**Source fingerprint (SHA-256):** `11c1c90fed0e29f1110b4c1dda64d60797aff38d7f3af69f76b74e94fe94e976`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GetItemFromList.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GetItemFromList)

[CustomCombo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CustomCombo)[ImageHistogram - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageHistogram)

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
