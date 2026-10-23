---
url: https://docs.comfy.org/built-in-nodes/PreviewAny/
title: PreviewAny - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:44.212652+00:00
---

# PreviewAny - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PreviewAny/

Utilities

# PreviewAny - ComfyUI Built-in Node Documentation

Copy pageCopy page

PreviewAny converts any input value into readable text so you can inspect it.

Copy pageCopy page

PreviewAny converts any input value into readable text so you can inspect it. Strings pass through unchanged, numbers and booleans become plain text, and other data types are serialized to JSON when possible (falling back to their plain string form if serialization fails). The resulting text is shown in the user interface and also returned as a string output for further processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`source`| Accepts any input data type for preview display. If no value is provided, the preview shows ‘None’.| ANY| Yes| Any data type  
  
**Conversion behavior**

  * Values of type STRING are shown exactly as provided.
  * Values of type INT, FLOAT, or BOOLEAN are converted to plain text.
  * Any other non-empty value is converted to JSON text with an indent of 4 spaces; if that conversion fails, the node falls back to the value’s plain text form. If that also fails, the preview shows the message ‘source exists, but could not be serialized.’
  * If no value is connected or the value is empty, the preview shows ‘None’.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`result`| The input value converted to text format. The same text is also displayed in the user interface.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/en.md)

* * *

**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PreviewAny.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PreviewAny)

[ImageHistogram - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageHistogram)[ResolutionSelector - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ResolutionSelector)

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
