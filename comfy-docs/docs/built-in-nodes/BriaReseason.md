---
url: https://docs.comfy.org/built-in-nodes/BriaReseason/
title: Bria Reseason - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:12.404420+00:00
---

# Bria Reseason - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaReseason/

Bria

# Bria Reseason - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node moves an image into a different season using Bria.

Copy pageCopy page

This node moves an image into a different season using Bria. The whole scene is re-rendered, so scenery can change beyond the season itself. Bria re-renders the whole frame at about 1 megapixel, so the result is not pixel-aligned with the input.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image to move to another season. Any alpha channel is removed before the image is sent.| IMAGE| Yes| -  
`season`| Season to apply.| COMBO| Yes| `"spring"`  
`"summer"`  
`"autumn"`  
`"winter"`  
`moderation`| Moderation settings. Selects whether content moderation options are configured for this request.| DYNAMIC_COMBO| Yes| `"false"`  
`"true"`  
  
### 

​

Moderation Inputs

These options appear when `moderation` is set to `"true"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`visual_input_moderation`| Enables content moderation on the input image (default: false).| BOOLEAN| No| true  
false  
`visual_output_moderation`| Enables content moderation on the generated output image (default: false).| BOOLEAN| No| true  
false  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The re-rendered image in the selected season.| IMAGE  
`structured_prompt`| Structured description of the edited image, for a follow-up edit with Bria FIBO Image Edit.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReseason/en.md)

* * *

**Source fingerprint (SHA-256):** `3bb9ee1c00c91759cc6f972e2ba8708ae73a186f4b66bf6669937e561efad0a4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaReseason.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaReseason)

[Bria Replace Object](https://docs.comfy.org/built-in-nodes/BriaReplaceObject)[Bria Restore Photo](https://docs.comfy.org/built-in-nodes/BriaRestorePhoto)
