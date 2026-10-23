---
url: https://docs.comfy.org/built-in-nodes/QuiverImageToSVGNodeV2/
title: QuiverImageToSVGNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:46.004771+00:00
---

# QuiverImageToSVGNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/QuiverImageToSVGNodeV2/

Quiver

# QuiverImageToSVGNodeV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Vectorize a raster image into a scalable vector graphic (SVG) with Quiver AI.

Copy pageCopy page

Vectorize a raster image into a scalable vector graphic (SVG) with Quiver AI. The image is sent to Quiver AI’s API, which returns the vectorized result. **Note:** Quiver retires the Arrow 1-series models on October 16, 2026, so the `arrow-1.1`, `arrow-1.1-max`, and `arrow-preview` options stop working after that date. Use `arrow-2` or `arrow-2-telos` instead. Selecting a `model` reveals the model-specific parameters listed below.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for SVG vectorization.| DYNAMIC_COMBO| Yes| `"arrow-2"`  
`"arrow-2-telos"`  
`"arrow-1.1"`  
`"arrow-1.1-max"`  
`"arrow-preview"`  
`image`| Input image to vectorize.| IMAGE| Yes| N/A  
`auto_crop`| Automatically crop to the dominant subject. Advanced parameter (default: False).| BOOLEAN| Yes| `True`  
`False`  
`target_size`| Square resize applied to the input image before vectorizing, in pixels. 0 keeps the source size, which vectorizes more cleanly than forcing a resize; any other value below 128 is clamped to 128. This does not set the output canvas; use `width` and `height` for that. Advanced parameter (default: 0).| INT| Yes| 0 to 4096  
`width`| Width of the output SVG canvas (viewBox), in user units. Set both `width` and `height` to control the output size and aspect ratio; leave either at 0 to let the model choose, which usually gives a square canvas. Advanced parameter (default: 0).| INT| Yes| 0 to 8192  
`height`| Height of the output SVG canvas (viewBox), in user units. Set both `width` and `height` to control the output size and aspect ratio; leave either at 0 to let the model choose, which usually gives a square canvas. Advanced parameter (default: 0).| INT| Yes| 0 to 8192  
`seed`| Seed to determine if the node should re-run; the actual results are nondeterministic regardless of the seed value. This parameter has “control after generate” functionality (default: 42).| INT| Yes| 0 to 2147483647  
  
### 

​

Model-Specific Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reasoning_effort`| How much reasoning the model spends before drawing. Higher levels improve detail and cost more tokens. Only used by the `"arrow-2"` and `"arrow-2-telos"` models (default: `"high"`).| COMBO| Yes| `"low"`  
`"medium"`  
`"high"`  
`"xhigh"`  
`temperature`| Randomness control. Higher values increase randomness. Not used by the `"arrow-2-telos"` model. Advanced parameter (default: 1.0).| FLOAT| Yes| 0.0 to 2.0 (step 0.1)  
`top_p`| Nucleus sampling parameter. Not used by the `"arrow-2-telos"` model. Advanced parameter (default: 1.0).| FLOAT| Yes| 0.05 to 1.0 (step 0.05)  
`presence_penalty`| Token presence penalty. Not used by the `"arrow-2-telos"` model. Advanced parameter (default: 0.0).| FLOAT| Yes| -2.0 to 2.0 (step 0.1)  
  
**Note:** `target_size` is applied before vectorizing and does not change the output canvas. Leave `width` or `height` at 0 to let the model pick the canvas size.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SVG`| The vectorized SVG output.| SVG  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNodeV2/en.md)

* * *

**Source fingerprint (SHA-256):** `186769b09bef2d2dbbfc26102f375ff80f8b324a24cd593da20afcea9cc2095b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/QuiverImageToSVGNodeV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/QuiverImageToSVGNodeV2)

[QuiverImageToSVGNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/QuiverImageToSVGNode)[QuiverTextToSVGNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/QuiverTextToSVGNode)

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
