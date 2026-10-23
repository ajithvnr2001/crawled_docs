---
url: https://docs.comfy.org/built-in-nodes/GeminiInputFiles/
title: GeminiInputFiles - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.679108+00:00
---

# GeminiInputFiles - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GeminiInputFiles/

Gemini

# GeminiInputFiles - ComfyUI Built-in Node Documentation

Copy pageCopy page

Loads and formats input files for use with the Gemini API.

Copy pageCopy page

Loads and formats input files for use with the Gemini API. This node allows users to include text (.txt) and PDF (.pdf) files as input context for the Gemini model. Files are converted to the appropriate format required by the API and can be chained together to include multiple files in a single request.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`file`| Input files to include as context for the model. Only accepts text (.txt) and PDF (.pdf) files for now. Files must be smaller than the maximum input file size limit (20 MB).| COMBO| Yes| Multiple options available (only .txt and .pdf files under 20 MB)  
`GEMINI_INPUT_FILES`| An optional additional file(s) to batch together with the file loaded from this node. Allows chaining of input files so that a single message can include multiple input files.| GEMINI_INPUT_FILES| No| N/A  
  
**Note:** The `file` parameter only displays text (.txt) and PDF (.pdf) files that are smaller than 20 MB. Files are automatically filtered and sorted by name.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`GEMINI_INPUT_FILES`| Formatted file data ready for use with Gemini LLM nodes, containing the loaded file content in the appropriate API format.| GEMINI_INPUT_FILES  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/en.md)

* * *

**Source fingerprint (SHA-256):** `1c80a87746c7ac73379f5c1e2d5c4d22f0fc44d3241fafb0297e087e436df7d6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GeminiInputFiles.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GeminiInputFiles)

[ByteDanceSeedNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceSeedNode)[GeminiNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GeminiNode)

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
