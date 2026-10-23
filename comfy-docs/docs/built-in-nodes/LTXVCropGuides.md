---
url: https://docs.comfy.org/built-in-nodes/LTXVCropGuides/
title: LTXVCropGuides - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:18.184491+00:00
---

# LTXVCropGuides - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVCropGuides/

Ltxv

# LTXVCropGuides - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXVCropGuides node removes keyframe guidance data from a video generation workflow.

Copy pageCopy page

The LTXVCropGuides node removes keyframe guidance data from a video generation workflow. It counts the keyframes recorded in the positive conditioning, crops that many frames off the end of the latent samples and noise mask, and clears the keyframe index and guide attention entries from both conditioning inputs. When no keyframes are found, the conditioning inputs are returned unchanged and the latent is passed through with a cloned sample tensor and its noise mask.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning input containing guidance information for generation. The number of keyframes it holds determines how many frames are cropped from the latent.| CONDITIONING| Yes| -  
`negative`| The negative conditioning input containing guidance information for what to avoid in generation. Its keyframe data is cleared along with the positive conditioning.| CONDITIONING| Yes| -  
`latent`| The latent representation containing image samples and noise mask data. When keyframes are present, the final keyframe frames are removed from both the samples and the noise mask.| LATENT| Yes| -  
  
Note: Cropping only occurs when keyframe indices are detected in the positive conditioning. If no keyframes are detected, the positive and negative conditioning are returned unchanged, while the latent is still returned with a cloned sample tensor and an explicit noise mask (a mask of all ones is created if the input latent has none).

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The processed positive conditioning with keyframe indices and guide attention entries cleared| CONDITIONING  
`negative`| The processed negative conditioning with keyframe indices and guide attention entries cleared| CONDITIONING  
`latent`| The cropped latent representation with adjusted samples and noise mask, where keyframe sections have been removed| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/en.md)

* * *

**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVCropGuides.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVCropGuides)

[LTXVConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVConditioning)[LTXVDurationPredictor - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVDurationPredictor)

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
