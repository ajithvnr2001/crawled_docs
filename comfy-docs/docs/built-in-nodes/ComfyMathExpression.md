---
url: https://docs.comfy.org/built-in-nodes/ComfyMathExpression/
title: ComfyMathExpression - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:39.027966+00:00
---

# ComfyMathExpression - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ComfyMathExpression/

Utilities

# ComfyMathExpression - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ComfyMathExpression node evaluates a mathematical formula that you write as text.

Copy pageCopy page

The ComfyMathExpression node evaluates a mathematical formula that you write as text. The formula can reference the node’s input values using letter names such as `a`, `b`, `c`, and you can add as many input values as needed through the growable `values` group. The calculation result is returned simultaneously as a floating-point number, an integer, and a boolean value.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`expression`| The mathematical formula to evaluate, written as text (for example `a + b`), using the letter names of the input values as variables. Multiline input. (default: “a + b”)| STRING| Yes| N/A  
`values`| Growable group of input values that provides the variables for the expression. Each value added to the group automatically gets the next lowercase letter name starting at `a` (`a`, `b`, `c`, …), and that name can then be used inside `expression`. Each item accepts a number (INT or FLOAT) or a boolean (TRUE/FALSE).| FLOAT, INT, BOOLEAN| Yes| 1 to 26 values, named `a` to `z`  
  
### 

​

Notes and constraints

  * `expression` cannot be empty or contain only whitespace.
  * The expression must evaluate to a numeric result (INT or FLOAT) or a boolean result (TRUE/FALSE). Boolean results are treated as 1 for TRUE and 0 for FALSE. If the result is a different type, such as text, the node raises an error.
  * The numeric result must be finite and convertible to a float. Results that are too large or non-finite cause an error.
  * The whole set of input values is also available inside the expression under the variable name `values` (as a list), so expressions such as `sum(values)` are possible.
  * The following math functions are available inside the expression: `sum`, `min`, `max`, `abs`, `round`, `pow`, `sqrt`, `ceil`, `floor`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `int`, `float`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`FLOAT`| The result of the expression as a floating-point number.| FLOAT  
`INT`| The result of the expression converted to an integer, with the decimal part truncated.| INT  
`BOOL`| The result converted to a boolean value: TRUE when the numeric result is not zero, FALSE when it is zero.| BOOLEAN  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/en.md)

* * *

**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ComfyMathExpression.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ComfyMathExpression)

[ColorToRGBInt - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ColorToRGBInt)[ComfyNumberConvert - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ComfyNumberConvert)

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
