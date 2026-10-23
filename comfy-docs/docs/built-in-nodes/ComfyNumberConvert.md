---
url: https://docs.comfy.org/built-in-nodes/ComfyNumberConvert/
title: ComfyNumberConvert - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:39.376930+00:00
---

# ComfyNumberConvert - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ComfyNumberConvert/

Utilities

# ComfyNumberConvert - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Number Convert node transforms various input data types into numeric values.

Copy pageCopy page

The Number Convert node transforms various input data types into numeric values. It accepts a single input of type integer, float, string, or boolean and produces two outputs: a floating-point number and an integer. This is useful for converting text or logical values into a format that can be used by other mathematical or processing nodes in your workflow.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`value`| The value to be converted into numeric outputs. Accepts an integer, a floating-point number, a text string, or a true/false boolean.| INT, FLOAT, STRING, BOOLEAN| Yes| N/A  
  
**Note:** When the input is a string, it must not be empty and must contain a valid representation of a number (e.g., `"123"`, `"3.14"`). The node will raise an error for empty strings, text that cannot be parsed as a number, or values that are not finite (like `"inf"` or `"nan"`). For boolean inputs, `true` converts to 1.0 (FLOAT) and 1 (INT), while `false` converts to 0.0 (FLOAT) and 0 (INT). For float inputs and for strings that contain a decimal number, the integer output is obtained by truncating the decimal portion.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`FLOAT`| The input value converted to a floating-point number.| FLOAT  
`INT`| The input value converted to an integer. For float inputs and decimal strings, this performs a truncation.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/en.md)

* * *

**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ComfyNumberConvert.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ComfyNumberConvert)

[ComfyMathExpression - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ComfyMathExpression)[CreateBoundingBoxes - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateBoundingBoxes)

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
