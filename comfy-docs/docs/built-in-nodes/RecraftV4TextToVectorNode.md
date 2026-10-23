---
url: https://docs.comfy.org/built-in-nodes/RecraftV4TextToVectorNode/
title: RecraftV4TextToVectorNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:49.502448+00:00
---

# RecraftV4TextToVectorNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftV4TextToVectorNode/

Recraft

# RecraftV4TextToVectorNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Recraft V4 Text to Vector node generates Scalable Vector Graphics (SVG) illustrations from a text description using Recraft V4 and V4.1 models.

Copy pageCopy page

The Recraft V4 Text to Vector node generates Scalable Vector Graphics (SVG) illustrations from a text description using Recraft V4 and V4.1 models. It connects to the Recraft API to generate one or more SVG files based on your prompt, and can apply an existing vector style or create a new one from reference images — when reference images are used, the created style is returned as a `style_id` for reuse.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to use for generation. The recraftv4_styles models are built for style-consistent generation and always require a style_id or style_references. Selecting a model changes the available `size` options.| DYNAMIC_COMBO| Yes| `"recraftv4_1_vector"`  
`"recraftv4_1_utility_vector"`  
`"recraftv4_1_pro_vector"`  
`"recraftv4_1_utility_pro_vector"`  
`"recraftv4"`  
`"recraftv4_pro"`  
`"recraftv4_styles_vector"`  
`"recraftv4_styles_pro_vector"`  
`prompt`| Prompt for the image generation. Maximum 10,000 characters.| STRING| Yes| N/A  
`negative_prompt`| This input is ignored: negative prompt is not supported by Recraft V4 and V4.1 models.| STRING| Yes| N/A  
`n`| The number of images to generate (default: 1).| INT| Yes| 1 to 6  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0).| INT| Yes| 0 to 18446744073709551615  
`recraft_controls`| Optional additional controls over the generation via the Recraft Controls node.| CUSTOM| No| N/A  
`style_id`| UUID of a Recraft V4 vector style to apply, e.g. from the Recraft V4 Create Style node or the style_id output of a previous run. Cannot be combined with style_references.| STRING| No| N/A  
`style_match`| How closely to follow the style: precise reproduces it in detail, flexible matches the general look. Only used when a style is provided (default: “precise”).| COMBO| No| `"precise"`  
`"flexible"`  
  
### 

​

recraftv4_1_vector, recraftv4_1_utility_vector, recraftv4, and recraftv4_styles_vector Inputs

These models share the same `size` options.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`size`| The size of the generated image. Default is `"1024x1024"`.| COMBO| Yes| `"1024x1024"`  
`"1152x896"`  
`"896x1152"`  
`"1216x832"`  
`"832x1216"`  
`"1344x768"`  
`"768x1344"`  
`"1536x640"`  
`"640x1536"`  
  
### 

​

recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, recraftv4_pro, and recraftv4_styles_pro_vector Inputs

These models share the same `size` options.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`size`| The size of the generated image. Default is `"2048x2048"`.| COMBO| Yes| `"2048x2048"`  
`"2304x1792"`  
`"1792x2304"`  
`"2432x1664"`  
`"1664x2432"`  
`"2688x1536"`  
`"1536x2688"`  
`"3072x1280"`  
`"1280x3072"`  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`style_references`| Reference images to create a vector style from on the fly, billed on top of the generation. The created style is returned as style_id for reuse. Cannot be combined with style_id.| IMAGE| No| Growable slot: connect 1..N reference images (up to the node’s maximum)  
  
**Note:** The `size` parameter is a dynamic input whose available options change based on the selected `model`. The `seed` value does not guarantee reproducible results from the external API. The `recraftv4_styles_vector` and `recraftv4_styles_pro_vector` models always require a style: provide a `style_id` or connect at least one `style_references` image. `style_id` and `style_references` cannot be used together — providing both raises an error, and `style_id` must be a valid UUID. Style reference images are limited in number, and their total encoded size must not exceed 10 MB.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated Scalable Vector Graphics (SVG) image(s).| SVG  
`style_id`| The style UUID returned by the Recraft API. When reference images are provided, the created style is returned here for reuse; otherwise an empty string.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/en.md)

* * *

**Source fingerprint (SHA-256):** `182a40b206b164cf2e96c7344d23e4906b7d61b90e3000743a3fd31941e08539`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftV4TextToVectorNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftV4TextToVectorNode)

[RecraftV4TextToImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftV4TextToImageNode)[RecraftVectorizeImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftVectorizeImageNode)

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
