---
url: https://docs.comfy.org/built-in-nodes/BriaEraser/
title: Bria Eraser - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:12.275544+00:00
---

# Bria Eraser - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaEraser/

Bria

# Bria Eraser - ComfyUI Built-in Node Documentation

Copy pageCopy page

Bria Eraser removes objects or areas from an image using the Bria API.

Copy pageCopy page

Bria Eraser removes objects or areas from an image using the Bria API. You provide an image and a mask that outlines the regions to remove; the node uploads both to Bria, runs the erase job, waits for it to complete, and returns the edited image with the masked areas erased.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image containing the objects or areas to remove.| IMAGE| Yes| -  
`mask`| White areas are erased, black areas are preserved. The mask is binarized before sending with a 50% cutoff: only areas painted above 50% opacity count as white. Must have the same aspect ratio as the image.| MASK| Yes| -  
`mask_type`| The mask source type. “manual” is for hand-drawn or brush masks; “automatic” is for masks produced by segmentation models such as SAM.| COMBO| Yes| ”manual"  
"automatic”  
`moderation`| Moderation settings. Set to “true” to enable visual content moderation on the input and/or output images.| DYNAMIC_COMBO| Yes| ”false"  
"true”  
  
When `moderation` is set to “true”, two additional boolean settings become available:

  * `visual_input_moderation` — applies visual content moderation to the input image (default: false)
  * `visual_output_moderation` — applies visual content moderation to the output image (default: false)

Note: The mask must match the aspect ratio of the image, otherwise the request fails. The mask is converted to a binary (black and white) mask before being sent to the API: areas painted at less than half opacity are ignored, and partially painted areas are treated as white and will be erased. The mask must contain at least some white area; an empty mask causes the request to fail because there is nothing to erase.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The edited image with the masked objects or areas removed.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/en.md)

* * *

**Source fingerprint (SHA-256):** `5528b7a3cb4d0a7b1b28acbc642a8bd21e2eacf5aa225403d6344c29f0cdba80`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaEraser.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaEraser)

[Bria Erase Foreground](https://docs.comfy.org/built-in-nodes/BriaEraseForeground)[Bria Expand Image](https://docs.comfy.org/built-in-nodes/BriaExpandImage)
