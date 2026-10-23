---
url: https://docs.comfy.org/built-in-nodes/StringTrim/
title: StringTrim - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:06.628179+00:00
---

# StringTrim - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StringTrim/

Text

# StringTrim - ComfyUI Built-in Node Documentation

Copy pageCopy page

The StringTrim node removes whitespace characters (such as spaces, tabs, and newlines) from the beginning, end, or both sides of a text string.

Copy pageCopy page

The StringTrim node removes whitespace characters (such as spaces, tabs, and newlines) from the beginning, end, or both sides of a text string. You can choose to trim from the left side, right side, or both sides of the string. This is useful for cleaning up text inputs by removing unwanted whitespace.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`string`| The text string to process. Supports multiline input.| STRING| Yes| -  
`mode`| Specifies which side(s) of the string to trim. “Both” removes whitespace from both ends, “Left” removes from the beginning only, “Right” removes from the end only.| COMBO| Yes| ”Both"  
"Left"  
"Right”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The trimmed text string with whitespace removed according to the selected mode.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/en.md)

* * *

**Source fingerprint (SHA-256):** `b7d0694b752f3017a5f8ee9a6ca1d88260f761576b5960f2cb210e34efb09d18`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StringTrim.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StringTrim)

[StringSubstring - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StringSubstring)[StripWhitespace - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StripWhitespace)

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
