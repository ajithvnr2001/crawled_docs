---
url: https://docs.comfy.org/built-in-nodes/RegexMatch/
title: RegexMatch - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:50.238106+00:00
---

# RegexMatch - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RegexMatch/

Text

# RegexMatch - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RegexMatch node checks if a text string contains a match for a given regular expression pattern.

Copy pageCopy page

The RegexMatch node checks if a text string contains a match for a given regular expression pattern. It searches the input string and returns a simple yes/no result indicating whether the pattern was found anywhere in the text. You can adjust how the search works by enabling options like case-insensitive matching or multiline mode.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`string`| The text string to search for matches| STRING| Yes| -  
`regex_pattern`| The regular expression pattern to match against the string| STRING| Yes| -  
`case_insensitive`| Whether to ignore case when matching (default: True)| BOOLEAN| No| -  
`multiline`| Whether to enable multiline mode for regex matching (default: False)| BOOLEAN| No| -  
`dotall`| Whether to enable dotall mode for regex matching (default: False)| BOOLEAN| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`matches`| Returns True if the regex pattern matches any part of the input string, False otherwise| BOOLEAN  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/en.md)

* * *

**Source fingerprint (SHA-256):** `4f0fa717bde7406e42d9a99599eab546690140166d2bb01bb4fde3c5d60e0397`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RegexMatch.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RegexMatch)

[RegexExtract - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RegexExtract)[RegexReplace - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RegexReplace)

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
