---
url: https://docs.comfy.org/built-in-nodes/RegexReplace/
title: RegexReplace - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:49.816968+00:00
---

# RegexReplace - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RegexReplace/

Text

# RegexReplace - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RegexReplace node finds and replaces text in strings using regular expression patterns.

Copy pageCopy page

The RegexReplace node finds and replaces text in strings using regular expression patterns. It allows you to search for text patterns and replace them with new text, with options to control how the pattern matching works including case sensitivity, multiline matching, and limiting the number of replacements.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`string`| The input text string to search and replace within| STRING| Yes| -  
`regex_pattern`| The regular expression pattern to search for in the input string| STRING| Yes| -  
`replace`| The replacement text to substitute for matched patterns| STRING| Yes| -  
`case_insensitive`| When enabled, makes the pattern matching ignore case differences (default: True)| BOOLEAN| No| -  
`multiline`| When enabled, changes the behavior of ^ and $ to match at the start/end of each line rather than just the start/end of the entire string (default: False)| BOOLEAN| No| -  
`dotall`| When enabled, the dot (.) character will match any character including newline characters. When disabled, dots won’t match newlines (default: False)| BOOLEAN| No| -  
`count`| Maximum number of replacements to make. Set to 0 to replace all occurrences (default). Set to 1 to replace only the first match, 2 for the first two matches, etc. (default: 0)| INT| No| 0-100  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The modified string with the specified replacements applied| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/en.md)

* * *

**Source fingerprint (SHA-256):** `58d4ec055aa5901b0e536bb2ca6993053ea85a9269d09cdcdf584df935d6876d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RegexReplace.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RegexReplace)

[RegexMatch - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RegexMatch)[ReplaceText - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ReplaceText)

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
