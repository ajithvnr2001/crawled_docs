---
url: https://docs.comfy.org/built-in-nodes/StringCompare/
title: StringCompare - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:06.266130+00:00
---

# StringCompare - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StringCompare/

Text

# StringCompare - ComfyUI Built-in Node Documentation

Copy pageCopy page

The StringCompare node compares two text strings using different comparison methods.

Copy pageCopy page

The StringCompare node compares two text strings using different comparison methods. It can check if one string starts with another, ends with another, or if both strings are exactly equal. The comparison can be performed with or without considering letter case differences.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`string_a`| The first string to compare| STRING| Yes| -  
`string_b`| The second string to compare against| STRING| Yes| -  
`mode`| The comparison method to use (default: “Starts With”)| COMBO| Yes| ”Starts With"  
"Ends With"  
"Equal”  
`case_sensitive`| Whether to consider letter case during comparison (default: true)| BOOLEAN| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| Returns true if the comparison condition is met, false otherwise| BOOLEAN  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/en.md)

* * *

**Source fingerprint (SHA-256):** `18599228c31543f270afde0f3b838512ee12d1998b8de42c4d3e7852b1a5d8b2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StringCompare.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StringCompare)

[SaveText - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveText)[StringConcatenate - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StringConcatenate)

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
