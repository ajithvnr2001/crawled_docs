---
url: https://docs.comfy.org/built-in-nodes/LoopResult/
title: LoopResult - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:25.532082+00:00
---

# LoopResult - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoopResult/

Advanced

# LoopResult - ComfyUI Built-in Node Documentation

Copy pageCopy page

LoopResult is a developer-only output node that marks the closing point of a loop block.

Copy pageCopy page

LoopResult is a developer-only output node that marks the closing point of a loop block. It collects the values that are passed into it in order (named `output0`, `output1`, and so on) and releases the external execution block identified by a close ID. Because input fingerprinting always returns NaN, the node is treated as always changed and is re-executed every run.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`close_id`| Identifier of the loop block to close; only the first value of the list is used| STRING| Yes| -  
`output0`, `output1`, …| Values collected from the loop block. The node accepts any additional inputs and gathers them in sequential order starting at `output0`, stopping at the first missing index| Any type| No| -  
  
Note: This node accepts all inputs (`accept_all_inputs`). Any input beyond `close_id` is treated as a collected loop value and must be named `output0`, `output1`, `output2`, etc., without gaps, for it to be included in the result.

## 

​

Outputs

This node does not return any outputs. It only releases the external execution block associated with `close_id`.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopResult/en.md)

* * *

**Source fingerprint (SHA-256):** `637f8a39b0e99e8d4453cfc482463bd14d909b710264021ac2c27fdcd68b6063`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoopResult.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoopResult)

[LoopProgress - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoopProgress)[LtxvApiImageToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LtxvApiImageToVideo)

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
