---
url: https://docs.comfy.org/built-in-nodes/MagnificImageRelightNode/
title: MagnificImageRelightNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:28.623622+00:00
---

# MagnificImageRelightNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MagnificImageRelightNode/

Magnific

# MagnificImageRelightNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Magnific Image Relight node adjusts the lighting of an input image.

Copy pageCopy page

The Magnific Image Relight node adjusts the lighting of an input image. It can apply stylistic lighting based on a text prompt or transfer the lighting characteristics from an optional reference image. The node offers various controls for fine-tuning the brightness, contrast, and overall mood of the final output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image to relight. Exactly one image is required. Minimum dimensions are 160x160 pixels. Aspect ratio must be between 1:3 and 3:1.| IMAGE| Yes| N/A  
`prompt`| Descriptive guidance for lighting. Supports emphasis notation (1-1.4). Default is an empty string.| STRING| No| N/A  
`light_transfer_strength`| Intensity of light transfer application. Default: 100.| INT| Yes| 0 to 100  
`style`| Stylistic output preference.| COMBO| Yes| `"standard"`  
`"darker_but_realistic"`  
`"clean"`  
`"smooth"`  
`"brighter"`  
`"contrasted_n_hdr"`  
`"just_composition"`  
`interpolate_from_original`| Restricts generation freedom to match original more closely. Default: False.| BOOLEAN| Yes| N/A  
`change_background`| Modifies background based on prompt/reference. Default: True.| BOOLEAN| Yes| N/A  
`preserve_details`| Maintains texture and fine details from original. Default: True.| BOOLEAN| Yes| N/A  
`advanced_settings`| Fine-tuning options for advanced lighting control. When set to `"enabled"`, additional parameters become available.| DYNAMICCOMBO| Yes| `"disabled"`  
`"enabled"`  
`reference_image`| Optional reference image to transfer lighting from. If provided, exactly one image is required. Minimum dimensions are 160x160 pixels. Aspect ratio must be between 1:3 and 3:1.| IMAGE| No| N/A  
  
**Note on Advanced Settings:** When `advanced_settings` is set to `"enabled"`, the following nested parameters become active:

  * `whites`: Adjusts the brightest tones in the image. Range: 0 to 100. Default: 50.
  * `blacks`: Adjusts the darkest tones in the image. Range: 0 to 100. Default: 50.
  * `brightness`: Overall brightness adjustment. Range: 0 to 100. Default: 50.
  * `contrast`: Contrast adjustment. Range: 0 to 100. Default: 50.
  * `saturation`: Color saturation adjustment. Range: 0 to 100. Default: 50.
  * `engine`: Processing engine selection. Options: `"automatic"`, `"balanced"`, `"cool"`, `"real"`, `"illusio"`, `"fairy"`, `"colorful_anime"`, `"hard_transform"`, `"softy"`.
  * `transfer_light_a`: The intensity of light transfer. Options: `"automatic"`, `"low"`, `"medium"`, `"normal"`, `"high"`, `"high_on_faces"`.
  * `transfer_light_b`: Also modifies light transfer intensity. Can be combined with the previous control for varied effects. Options: `"automatic"`, `"composition"`, `"straight"`, `"smooth_in"`, `"smooth_out"`, `"smooth_both"`, `"reverse_both"`, `"soft_in"`, `"soft_out"`, `"soft_mid"`, `"style_shift"`, `"strong_shift"`.
  * `fixed_generation`: Ensures consistent output with the same settings. Default: True.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The relit image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/en.md)

* * *

**Source fingerprint (SHA-256):** `45fe68b21e1da7c367800915c803ad4cf1c5b80e9a2e91d80cae51b8a9531144`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MagnificImageRelightNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MagnificImageRelightNode)

[LumaReferenceNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaReferenceNode)[MagnificImageSkinEnhancerNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MagnificImageSkinEnhancerNode)

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
