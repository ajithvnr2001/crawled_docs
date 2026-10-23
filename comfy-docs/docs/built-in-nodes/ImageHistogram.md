---
url: https://docs.comfy.org/built-in-nodes/ImageHistogram/
title: ImageHistogram - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.443651+00:00
---

# ImageHistogram - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageHistogram/

Utilities

# ImageHistogram - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageHistogram node analyzes the color distribution of an input image.

Copy pageCopy page

The ImageHistogram node analyzes the color distribution of an input image. It calculates and outputs several histograms, which are graphs showing how many pixels in the image have each possible intensity value. It generates separate histograms for the red, green, and blue color channels, a composite RGB histogram, and a luminance histogram based on a standard brightness formula. Each histogram contains 256 bins, covering intensity levels from 0 to 255.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to analyze. The node processes the first image in the batch.| IMAGE| Yes| N/A  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`rgb`| A composite histogram representing the average pixel intensity across the red, green, and blue channels.| HISTOGRAM  
`luminance`| A histogram of the image’s perceived brightness, calculated using the ITU-R BT.709 standard luminance formula.| HISTOGRAM  
`red`| A histogram showing the distribution of pixel intensities in the red color channel.| HISTOGRAM  
`green`| A histogram showing the distribution of pixel intensities in the green color channel.| HISTOGRAM  
`blue`| A histogram showing the distribution of pixel intensities in the blue color channel.| HISTOGRAM  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/en.md)

* * *

**Source fingerprint (SHA-256):** `5020f5cedd325250a207a00950011f4b6dc19ddfe4d172665ffca4982731dd5e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageHistogram.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageHistogram)

[GetItemFromList - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GetItemFromList)[PreviewAny - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PreviewAny)

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
