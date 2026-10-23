---
url: https://docs.comfy.org/built-in-nodes/QuiverTextToSVGNode/
title: QuiverTextToSVGNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:45.891484+00:00
---

# QuiverTextToSVGNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/QuiverTextToSVGNode/

Quiver

# QuiverTextToSVGNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Quiver Text to SVG node generates a Scalable Vector Graphic (SVG) image from a text description using Quiver AI’s models.

Copy pageCopy page

The Quiver Text to SVG node generates a Scalable Vector Graphic (SVG) image from a text description using Quiver AI’s models. You can optionally provide reference images and style instructions to guide the generation process. **Note:** This node is marked as deprecated in the source code. Quiver retires the Arrow 1-series models on October 16, 2026, so the `arrow-1.1`, `arrow-1.1-max`, and `arrow-preview` options stop working after that date. Use `arrow-2` or `arrow-2-telos` instead.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text description of the desired SVG output. This is the main instruction for what to generate.| STRING| Yes| N/A  
`instructions`| Additional style or formatting guidance. This is an optional, advanced parameter.| STRING| No| N/A  
`reference_images`| Up to 4 reference images to guide the generation. This is an optional input.| IMAGE| No| 0 to 4 images  
`model`| Model to use for SVG generation. Selecting a model reveals additional parameters specific to that model: `temperature`, `top_p`, and `presence_penalty`.| DYNAMIC_COMBO| Yes| `"arrow-2"`  
`"arrow-2-telos"`  
`"arrow-1.1"`  
`"arrow-1.1-max"`  
`"arrow-preview"`  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed. Default: 0.| INT| Yes| 0 to 2147483647  
`reasoning_effort`| How much reasoning the model spends before drawing. Higher levels improve detail and cost more tokens. Only used by the Arrow 2 models (default: “high”).| COMBO| No| `"low"`  
`"medium"`  
`"high"`  
`"xhigh"`  
  
**Note:** The `reference_images` input accepts a maximum of 4 images.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SVG`| The generated Scalable Vector Graphic (SVG) image.| SVG  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/en.md)

* * *

* * *

**Source fingerprint (SHA-256):** `e03e130a4aedbf003e898300b3a83e343fdfa5b3da35df20d55876d437bf5426`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/QuiverTextToSVGNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/QuiverTextToSVGNode)

[QuiverImageToSVGNodeV2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/QuiverImageToSVGNodeV2)[QuiverTextToSVGNodeV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/QuiverTextToSVGNodeV2)

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
