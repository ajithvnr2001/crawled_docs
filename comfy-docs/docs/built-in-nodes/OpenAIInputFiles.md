---
url: https://docs.comfy.org/built-in-nodes/OpenAIInputFiles/
title: OpenAIInputFiles - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:39.566448+00:00
---

# OpenAIInputFiles - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/OpenAIInputFiles/

Openai

# OpenAIInputFiles - ComfyUI Built-in Node Documentation

Copy pageCopy page

Loads and formats input files for the OpenAI API.

Copy pageCopy page

Loads and formats input files for the OpenAI API. This node prepares text (.txt) and PDF (.pdf) files to include as context inputs for the OpenAI Chat Node. The files will be read by the OpenAI model when generating a response. Multiple OpenAI Input Files nodes can be chained together to include several files in a single message.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`file`| Input files to include as context for the model. Only accepts text (.txt) and PDF (.pdf) files for now. Files must be smaller than 32MB.| COMBO| Yes| Multiple options available (all .txt and .pdf files in the input directory under 32MB)  
`OPENAI_INPUT_FILES`| An optional additional file(s) to batch together with the file loaded from this node. Allows chaining of input files so that a single message can include multiple input files.| OPENAI_INPUT_FILES| No| N/A  
  
**File Constraints:**

  * Only .txt and .pdf files are supported
  * Maximum file size: 32MB
  * Files are loaded from the ComfyUI input directory



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`OPENAI_INPUT_FILES`| Formatted input files ready to be used as context for OpenAI API calls.| OPENAI_INPUT_FILES  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/en.md)

* * *

**Source fingerprint (SHA-256):** `6554e685184ced830ee27aa96efefc8bb9616bd0504685bdb643c715ebc6dd98`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/OpenAIInputFiles.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/OpenAIInputFiles)

[OpenAIChatNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/OpenAIChatNode)[OpenRouterLLMNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpenRouterLLMNode)

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
