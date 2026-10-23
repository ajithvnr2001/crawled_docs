---
url: https://docs.comfy.org/built-in-nodes/DCTestNode/
title: DCTestNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:50.176356+00:00
---

# DCTestNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DCTestNode/

Logic

# DCTestNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

DCTestNode is a logic node that returns different types of data based on a user’s selection from a dynamic combo box.

Copy pageCopy page

DCTestNode is a logic node that returns different types of data based on a user’s selection from a dynamic combo box. It acts as a conditional router, where the chosen option determines which input field is active and what type of value the node will output. The node is flagged as an output node in ComfyUI.

## 

​

Inputs

The node uses a dynamic combo selector: the `combo` parameter is always visible, and the other input fields appear only when their corresponding option is selected.

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`combo`| The main selection that determines which input field is active and what the node will output.| DYNAMIC_COMBO| Yes| `"option1"`  
`"option2"`  
`"option3"`  
`"option4"`  
  
### 

​

option1 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`string`| A text input field. This field is only active and required when `combo` is set to `"option1"`.| STRING| Yes| -  
  
### 

​

option2 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`integer`| A whole number input field. This field is only active and required when `combo` is set to `"option2"`.| INT| Yes| -  
  
### 

​

option3 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| An image input field. This field is only active and required when `combo` is set to `"option3"`.| IMAGE| Yes| -  
  
### 

​

option4 Inputs

When `combo` is set to `"option4"`, the node shows a second dynamic combo selector (`subcombo`) that controls a nested set of input fields.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`subcombo`| A secondary dynamic combo selection that appears when `combo` is set to `"option4"`. It determines which nested input fields are active.| DYNAMIC_COMBO| Yes| `"opt1"`  
`"opt2"`  
`float_x`| A decimal number input. This field is only active and required when `combo` is set to `"option4"` and `subcombo` is set to `"opt1"`.| FLOAT| Yes| -  
`float_y`| A decimal number input. This field is only active and required when `combo` is set to `"option4"` and `subcombo` is set to `"opt1"`.| FLOAT| Yes| -  
`mask1`| A mask input field. This field is only active when `combo` is set to `"option4"` and `subcombo` is set to `"opt2"`. It is optional.| MASK| No| -  
  
**Parameter Constraints:**

  * The `combo` parameter controls the visibility and requirement of all other input fields. Only the inputs associated with the selected `combo` option will be shown and are required (except for `mask1`, which is optional).
  * When `combo` is set to `"option4"`, the `subcombo` parameter becomes required and controls a second set of nested inputs (`float_x`/`float_y` or `mask1`).
  * If `combo` receives a value that is not one of the four listed options, the node raises an error.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The output depends on the selected `combo` option. It can be a STRING (`"option1"`), an INT (`"option2"`), an IMAGE (`"option3"`), or a string representation of the `subcombo` value (`"option4"`).| ANYTYPE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DCTestNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DCTestNode)

[ConvertStringToComboNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConvertStringToComboNode)[InvertBooleanNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/InvertBooleanNode)

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
