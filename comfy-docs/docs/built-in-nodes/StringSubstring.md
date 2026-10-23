---
url: https://docs.comfy.org/built-in-nodes/StringSubstring/
title: StringSubstring - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:06.552503+00:00
---

# StringSubstring - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StringSubstring/

Text

# StringSubstring - ComfyUI Built-in Node Documentation

Copy pageCopy page

The StringSubstring node extracts a portion of text from a larger string.

Copy pageCopy page

The StringSubstring node extracts a portion of text from a larger string. It takes a starting position and ending position to define the section you want to extract, then returns the text between those two positions.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`string`| The input text string to extract from. Supports multi-line text.| STRING| Yes| -  
`start`| The starting position index for the substring. The first character is at index 0.| INT| Yes| -  
`end`| The ending position index for the substring. The character at this index is not included in the result.| INT| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The extracted substring from the input text, containing all characters from the `start` position up to (but not including) the `end` position.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/en.md)

* * *

**Source fingerprint (SHA-256):** `fd3ec23bbfe3a51f5481f1b0fe8b77f66e08469bb2a4bd3e266a7607f014e544`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StringSubstring.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StringSubstring)

[StringReplace - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StringReplace)[StringTrim - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StringTrim)

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
