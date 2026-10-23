---
url: https://docs.comfy.org/built-in-nodes/ColorTransfer/
title: ColorTransfer - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.833249+00:00
---

# ColorTransfer - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ColorTransfer/

Filters

# ColorTransfer - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ColorTransfer node adjusts the color palette of a target image to match the colors of a reference image.

Copy pageCopy page

The ColorTransfer node adjusts the color palette of a target image to match the colors of a reference image. It uses different mathematical algorithms to analyze and transfer the color characteristics, such as brightness, contrast, and hue distribution, from the reference to the target. This is useful for creating visual consistency across multiple images or applying a specific color grade.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image_target`| Image(s) to apply the color transform to.| IMAGE| Yes| -  
`image_ref`| Reference image(s) to match colors to.| IMAGE| Yes| -  
`method`| The color transfer algorithm to use.| COMBO| Yes| `"reinhard_lab"`  
`"mkl_lab"`  
`"histogram"`  
`source_stats`| Determines how color statistics are calculated from the source (target) image(s).| DYNAMICCOMBO| Yes| `"per_frame"`  
`"uniform"`  
`"target_frame"`  
`strength`| The intensity of the color transfer effect. A value of 1.0 applies the full transform, while 0.0 returns the original image. Default: 1.0| FLOAT| Yes| 0.0 to 10.0  
  
**Parameter Details:**

  * **`source_stats` Options:**
    * **`per_frame`** : Each frame in a batch is matched to the `image_ref` individually.
    * **`uniform`** : Color statistics are pooled across all source frames to create a single baseline, which is then matched to the `image_ref`.
    * **`target_frame`** : Uses one chosen frame from the target batch as the baseline for computing the transform to the `image_ref`. This transform is then applied uniformly to all frames, which preserves the relative color differences between them. When this option is selected, an additional `target_index` parameter becomes available.
  * **`target_index`** (appears when `source_stats` is `"target_frame"`): The frame index (starting from 0) used as the source baseline for computing the transform. Default: 0. Must be between 0 and 10000.

**Constraints:**

  * If `strength` is set to 0.0 or `image_ref` is `None`, the node returns the original `image_target` without processing.
  * When `source_stats` is set to `"target_frame"`, the `target_index` must be a valid index within the batch of `image_target`. If it exceeds the number of frames, the last frame is used.
  * For the `histogram` method with `source_stats` set to `"per_frame"`, if the batch size of `image_ref` is greater than 1, each target frame is matched to the corresponding reference frame by index. If the reference batch has only one frame, it is used for all target frames.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resulting image(s) after the color transfer has been applied.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/en.md)

* * *

**Source fingerprint (SHA-256):** `f844af34ac6129c7751953c48e2d12aa0d2c556937e610f649f3eb2725955711`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ColorTransfer.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ColorTransfer)

[Canny - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Canny)[ImageAddNoise - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageAddNoise)

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
