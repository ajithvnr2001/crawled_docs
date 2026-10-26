---
url: https://docs.comfy.org/built-in-nodes/BriaAddObject/
title: Bria Add Object - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:11.914709+00:00
---

# Bria Add Object - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaAddObject/

Bria

# Bria Add Object - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node inserts an object described in plain text into an image using Bria.

Copy pageCopy page

This node inserts an object described in plain text into an image using Bria. Bria re-renders the whole frame at about 1 megapixel, so the result is not pixel-aligned with the input.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image the described object is added to. The alpha channel is dropped before the image is uploaded.| IMAGE| Yes| -  
`instruction`| What to add and where, such as ‘Place a red vase with flowers on the table’. Must not be empty. Default: "" (empty string).| STRING| Yes| -  
`seed`| Bria takes no seed here and re-imagines the edit on each call, so repeated runs can differ. The value is never sent: it only changes this node’s cache key, so that an otherwise identical graph runs the edit again instead of returning the cached result. Default: 42.| INT| Yes| 0 to 2147483647  
`moderation`| Moderation settings. Choose “true” to reveal the moderation flags below.| DYNAMIC_COMBO| Yes| ”false"  
"true”  
  
### 

​

Moderation Enabled Inputs

Available when `moderation` is set to “true”.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`visual_input_moderation`| Enables content moderation on the input image. Default: False.| BOOLEAN| No| True / False  
`visual_output_moderation`| Enables content moderation on the generated output image. Default: False.| BOOLEAN| No| True / False  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The edited image with the described object added.| IMAGE  
`structured_prompt`| Structured description of the edited image, for a follow-up edit with Bria FIBO Image Edit.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaAddObject/en.md)

* * *

**Source fingerprint (SHA-256):** `41c9a3e511763372d8dc8be9da4f70158e53d5156a88eb3c66f81149efdbd566`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaAddObject.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaAddObject)

[Flux Virtual Try-On](https://docs.comfy.org/built-in-nodes/FluxVTONode)[Bria Erase by Text](https://docs.comfy.org/built-in-nodes/BriaEraseByText)
