---
url: https://docs.comfy.org/built-in-nodes/ReplaceText/
title: ReplaceText - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:52.261038+00:00
---

# ReplaceText - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ReplaceText/

Text

# ReplaceText - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Replace Text node performs a simple text substitution.

Copy pageCopy page

The Replace Text node performs a simple text substitution. It searches for a specified piece of text within the input and replaces every occurrence with a new piece of text. The operation is applied to all text inputs provided to the node. **Note:** This node is deprecated and superseded by the other Replace Text node.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`text`| The text to process.| STRING| Yes| -  
`find`| Text to find (default: empty string).| STRING| Yes| -  
`replace`| Text to replace with (default: empty string).| STRING| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`text`| The processed text with all occurrences of the `find` text replaced by the `replace` text.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/en.md)

* * *

**Source fingerprint (SHA-256):** `38beeabc232b19efedf2dcf4e2490f537d9a07d60c89de2811b7a4bddb98cf57`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ReplaceText.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ReplaceText)

[RegexReplace](https://docs.comfy.org/built-in-nodes/RegexReplace)[SaveText](https://docs.comfy.org/built-in-nodes/SaveText)
