---
url: https://docs.comfy.org/built-in-nodes/JsonExtractString/
title: JsonExtractString - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:13.235940+00:00
---

# JsonExtractString - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/JsonExtractString/

Text

# JsonExtractString - ComfyUI Built-in Node Documentation

Copy pageCopy page

The JsonExtractString node scans a text string for the first valid JSON object and extracts the value associated with a specific key, converted to a string.

Copy pageCopy page

The JsonExtractString node scans a text string for the first valid JSON object and extracts the value associated with a specific key, converted to a string. Any text before or after the JSON object is ignored, so the node also works on Markdown code blocks and on model replies that wrap the JSON in extra prose. If no valid JSON object is found, the key is not found, or the value is null, the node returns an empty string.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`json_string`| The text to search for a JSON object. This field supports multiline input and may contain surrounding prose or Markdown code fences.| STRING| Yes| N/A  
`key`| The specific key whose value you want to extract from the JSON object. This field supports single-line input only.| STRING| Yes| N/A  
  
**Note:** The node extracts values only from JSON objects (dictionaries). It tries each `{` in the input in order and decodes from the first position that yields a valid JSON object, so leading or trailing text is skipped. If no JSON object can be decoded or the specified key does not exist within it, the output is an empty string. If the value associated with the key is `null`, the node also returns an empty string. Values that are not strings are returned as their string representation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The string value extracted from the JSON for the specified key, or an empty string if the extraction fails.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/en.md)

* * *

**Source fingerprint (SHA-256):** `ca697fd3bd2d4de764372470ad1102b345d9d60f6df1c151fa0573e85fab2382`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/JsonExtractString.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/JsonExtractString)

[ConvertDictionaryToString - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConvertDictionaryToString)[MergeTextLists - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MergeTextLists)

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
