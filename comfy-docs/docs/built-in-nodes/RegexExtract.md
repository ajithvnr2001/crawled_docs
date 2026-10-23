---
url: https://docs.comfy.org/built-in-nodes/RegexExtract/
title: RegexExtract - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:49.702105+00:00
---

# RegexExtract - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RegexExtract/

Text

# RegexExtract - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RegexExtract node searches for patterns in text using regular expressions.

Copy pageCopy page

The RegexExtract node searches for patterns in text using regular expressions. It can find the first match, all matches, specific groups from matches, or all groups across multiple matches. The node supports various regex flags for case sensitivity, multiline matching, and dotall behavior.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`string`| The input text to search for patterns| STRING| Yes| -  
`regex_pattern`| The regular expression pattern to search for| STRING| Yes| -  
`mode`| The extraction mode determines what parts of matches are returned (default: “First Match”)| COMBO| Yes| ”First Match"  
"All Matches"  
"First Group"  
"All Groups”  
`case_insensitive`| Whether to ignore case when matching (default: True)| BOOLEAN| No| -  
`multiline`| Whether to treat the string as multiple lines (default: False)| BOOLEAN| No| -  
`dotall`| Whether the dot (.) matches newlines (default: False)| BOOLEAN| No| -  
`group_index`| The capture group index to extract when using group modes (default: 1)| INT| No| 0-100  
  
**Note:** When using “First Group” or “All Groups” modes, the `group_index` parameter specifies which capture group to extract. Group 0 represents the entire match, while groups 1+ represent the numbered capture groups in your regex pattern.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The extracted text based on the selected mode and parameters| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/en.md)

* * *

**Source fingerprint (SHA-256):** `a879e4fd7429edfada44b2f5778bb71e537a000be6c25d3f67359b9ee802812f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RegexExtract.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RegexExtract)

[MergeTextLists - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MergeTextLists)[RegexMatch - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RegexMatch)

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
