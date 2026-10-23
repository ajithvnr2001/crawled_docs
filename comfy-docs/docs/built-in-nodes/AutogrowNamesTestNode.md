---
url: https://docs.comfy.org/built-in-nodes/AutogrowNamesTestNode/
title: AutogrowNamesTestNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.453471+00:00
---

# AutogrowNamesTestNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AutogrowNamesTestNode/

Logic

# AutogrowNamesTestNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is a test for the Autogrow input feature.

Copy pageCopy page

This node is a test for the Autogrow input feature. It accepts a dynamic group of float inputs, each with a predefined name, and combines their values into a single comma-separated string.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`autogrow`| A dynamic input group. You can add multiple float inputs, each with a predefined name from the list: “a”, “b”, or “c”. The node accepts any combination of these named inputs.| FLOAT| Yes| Named slots: `a`, `b`, `c`  
  
**Note:** The `autogrow` input is dynamic. Individual float inputs named “a”, “b”, and “c” can be added or removed as needed. All provided values are processed by the node.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| A single string containing the values from all provided float inputs, joined together with commas.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/en.md)

* * *

**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AutogrowNamesTestNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AutogrowNamesTestNode)

[TruncateText - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TruncateText)[AutogrowPrefixTestNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AutogrowPrefixTestNode)

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
