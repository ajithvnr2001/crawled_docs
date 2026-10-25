---
url: https://docs.comfy.org/built-in-nodes/CombineHooks2/
title: CombineHooks2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:46.319004+00:00
---

# CombineHooks2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CombineHooks2/

Hooks

# CombineHooks2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Combine Hooks [2] node merges two hook groups into a single combined hook group.

Copy pageCopy page

The Combine Hooks [2] node merges two hook groups into a single combined hook group. It takes two optional hook inputs and combines them using ComfyUI’s hook combination functionality. This allows you to consolidate multiple hook configurations for streamlined processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`hooks_A`| First hook group to combine| HOOKS| No| -  
`hooks_B`| Second hook group to combine| HOOKS| No| -  
  
**Note:** Both inputs are optional, but at least one hook group must be provided for the node to function. If only one hook group is provided, it will be returned unchanged.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`hooks`| Combined hook group containing all hooks from both input groups| HOOKS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks2/en.md)

* * *

**Source fingerprint (SHA-256):** `558ceef1cebedd0b7e045b7d1eb1afa4316ea6a3c35f982968af132dca164126`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CombineHooks2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CombineHooks2)

[ConditioningTimestepsRange](https://docs.comfy.org/built-in-nodes/ConditioningTimestepsRange)[CombineHooks4](https://docs.comfy.org/built-in-nodes/CombineHooks4)
