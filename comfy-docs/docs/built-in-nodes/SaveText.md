---
url: https://docs.comfy.org/built-in-nodes/SaveText/
title: SaveText - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:59.735819+00:00
---

# SaveText - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveText/

Text

# SaveText - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Save Text node writes text content to a file in the output directory.

Copy pageCopy page

The Save Text node writes text content to a file in the output directory. It supports saving in .txt, .csv, .md, or .json format, and automatically handles JSON pretty-printing when valid JSON is provided.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`text`| The text content to save to a file. This input must be connected from another node.| STRING| Yes| -  
`filename_prefix`| Prefix for the output filename. A 5-digit counter is appended to prevent overwriting existing files (default: “ComfyUI”).| STRING| No| -  
`format`| The file format to save the text as (default: “txt”). When “json” is selected, valid JSON text is pretty-printed with 2-space indentation; otherwise, the text is saved as-is.| COMBO| No| `"txt"`  
`"csv"`  
`"md"`  
`"json"`  
  
### 

​

Notes

  * `text` is a forced input and must be connected to another node; it cannot be typed directly.
  * The saved file is named `<filename_prefix>_<5-digit counter>.<extension>` and is written into the ComfyUI output directory (in a subfolder derived from the prefix).
  * Selecting the `"json"` format attempts to parse the text as JSON. If parsing succeeds, the content is written pretty-printed with 2-space indentation; if parsing fails, the raw text is written unchanged.
  * The node reports the saved file back to the interface so it appears with the other generated output files.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`text`| The original text content that was saved to the file| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/en.md)

* * *

**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveText.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveText)

[ReplaceText - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ReplaceText)[StringCompare - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StringCompare)

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
