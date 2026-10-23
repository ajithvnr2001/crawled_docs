---
url: https://docs.comfy.org/built-in-nodes/ColorToRGBInt/
title: ColorToRGBInt - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:37.176152+00:00
---

# ColorToRGBInt - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ColorToRGBInt/

Utilities

# ColorToRGBInt - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ColorToRGBInt node converts a color given in hexadecimal format (like FF5733) into a single RGB integer value.

Copy pageCopy page

The **ColorToRGBInt** node converts a color given in hexadecimal format (like `#FF5733`) into a single RGB integer value. It extracts the red, green, and blue components from the color string, combines them into one integer, and also returns the original hexadecimal representation and the alpha (opacity) value.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`color`| A color value in the hexadecimal format `#RRGGBB` or `#RRGGBBAA`. Must be 7 or 9 characters long and start with `#`.| COLOR| Yes| `#RRGGBB`  
`#RRGGBBAA`  
  
**Note:** The input `color` string must follow the format `#RRGGBB` or `#RRGGBBAA`. If it is not 7 or 9 characters long, does not start with `#`, or contains invalid hexadecimal characters, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`rgb_int`| The calculated RGB integer value, derived from the formula: `(Red * 65536) + (Green * 256) + Blue`.| INT  
`hex`| The hexadecimal color string in the format `#RRGGBB`. If the input included an alpha channel, it is removed from this output.| COLOR  
`alpha`| The alpha (opacity) value between 0.0 and 1.0. Equals 1.0 when the input is `#RRGGBB`, or the alpha channel value divided by 255 when the input is `#RRGGBBAA`.| FLOAT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/en.md)

* * *

**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ColorToRGBInt.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ColorToRGBInt)

[PrimitiveStringMultiline - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PrimitiveStringMultiline)[ComfyMathExpression - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ComfyMathExpression)

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
