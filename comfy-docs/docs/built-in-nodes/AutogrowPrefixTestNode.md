---
url: https://docs.comfy.org/built-in-nodes/AutogrowPrefixTestNode/
title: AutogrowPrefixTestNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:21.787281+00:00
---

# AutogrowPrefixTestNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AutogrowPrefixTestNode/

Logic

# AutogrowPrefixTestNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The AutogrowPrefixTestNode is a logic node that tests the autogrow input feature.

Copy pageCopy page

The AutogrowPrefixTestNode is a logic node that tests the autogrow input feature. It accepts a dynamic number of float inputs, converts each value into text, combines them into a comma-separated string, and outputs that string.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`autogrow`| A dynamic input group that accepts between 1 and 10 float values. Each value is a floating-point number, and the generated inputs are named with the prefix `float`.| AUTOGROW| Yes| 1 to 10 inputs  
  
**Note:** The `autogrow` input is a special dynamic input. You can add multiple float inputs to this group, from a minimum of 1 up to a maximum of 10. The node processes all provided values and includes every connected input in the output string.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| A single string containing all the input float values, separated by commas.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AutogrowPrefixTestNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AutogrowPrefixTestNode)

[AutogrowNamesTestNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AutogrowNamesTestNode)[ComboOptionTestNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ComboOptionTestNode)

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
