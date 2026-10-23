---
url: https://docs.comfy.org/built-in-nodes/NormalizeImages/
title: NormalizeImages - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:38.403334+00:00
---

# NormalizeImages - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/NormalizeImages/

Color

# NormalizeImages - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node normalizes the colors of an input image by adjusting its pixel values based on a specified mean and standard deviation.

Copy pageCopy page

This node normalizes the colors of an input image by adjusting its pixel values based on a specified mean and standard deviation. Each pixel has the mean subtracted from it and is then divided by the standard deviation, which is a common step to standardize image data before other processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be normalized.| IMAGE| Yes| -  
`mean`| Mean value for normalization (default: 0.5).| FLOAT| No| 0.0 - 1.0  
`std`| Standard deviation for normalization (default: 0.5).| FLOAT| No| 0.001 - 1.0  
  
The `mean` and `std` parameters control the normalization applied to the input image. The default value for both parameters is 0.5. Note: If the input image has an alpha (transparency) channel, that channel is not normalized. It is copied unchanged to the output because alpha stores transparency rather than color. Note: The node works with any batch size, so multiple images can be processed at once.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resulting image after the normalization process has been applied. Pixel values are adjusted using the specified mean and standard deviation, and the alpha channel (if present) is preserved.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/en.md)

* * *

**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/NormalizeImages.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/NormalizeImages)

[ImageYUVToRGB - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageYUVToRGB)[ImageCompositeMasked - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageCompositeMasked)

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
