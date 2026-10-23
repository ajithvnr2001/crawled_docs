---
url: https://docs.comfy.org/built-in-nodes/CustomCombo/
title: CustomCombo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:49.142678+00:00
---

# CustomCombo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CustomCombo/

Utilities

# CustomCombo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Custom Combo node lets you define your own list of text options for a dropdown menu instead of choosing from fixed values.

Copy pageCopy page

The Custom Combo node lets you define your own list of text options for a dropdown menu instead of choosing from fixed values. It is a frontend-focused node that also has a backend representation, so workflows that contain it stay compatible. When you select an option, the node outputs the selected text and its index position.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`choice`| The text option selected from the custom dropdown. The list of available options is defined by the user in the node’s frontend interface.| COMBO| Yes| User-defined  
`index`| An integer value that can be used to specify an index. Default: 0.| INT| No| Any integer (default: 0)  
  
**Note:** Validation for this node’s inputs is intentionally disabled. This allows you to write any custom text options in the frontend without the backend checking whether your selection matches a predefined list. Widgets other than the combo dropdown are fully defined in the frontend. This node is marked as experimental.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`STRING`| The text string of the option selected from the custom combo box.| STRING  
`INDEX`| The index position of the selected option in the dropdown list.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/en.md)

* * *

**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CustomCombo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CustomCombo)

[CurveEditor - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CurveEditor)[GetItemFromList - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GetItemFromList)

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
