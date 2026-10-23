---
url: https://docs.comfy.org/built-in-nodes/MergeTextLists/
title: MergeTextLists - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:31.084076+00:00
---

# MergeTextLists - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MergeTextLists/

Text

# MergeTextLists - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node merges multiple text lists into a single, combined list.

Copy pageCopy page

This node merges multiple text lists into a single, combined list. It is designed to receive text inputs as lists and concatenates them together. The node logs the total number of texts in the merged list.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`texts`| The text lists to be merged. Multiple lists can be connected to the input, and they will be concatenated into one.| STRING| Yes| N/A  
  
**Note:** This node is configured as a group process (`is_group_process = True`), meaning it automatically handles multiple list inputs by concatenating them before the main processing function runs. **Note:** This node is deprecated and superseded by the Create List node.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`texts`| The single, merged list containing all the input texts.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/en.md)

* * *

**Source fingerprint (SHA-256):** `bb7f45725c2c41a18d8cd3040d093c11be2ceb03cf1849385aa55d12fd9eb555`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MergeTextLists.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MergeTextLists)

[JsonExtractString - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/JsonExtractString)[RegexExtract - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RegexExtract)

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
