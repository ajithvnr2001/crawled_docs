---
url: https://docs.comfy.org/built-in-nodes/StabilityStableImageUltraNode/
title: StabilityStableImageUltraNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:52.656449+00:00
---

# StabilityStableImageUltraNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StabilityStableImageUltraNode/

Advanced

# StabilityStableImageUltraNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates images synchronously based on prompt and resolution.

Copy pageCopy page

Generates images synchronously based on prompt and resolution. This node creates images using Stability AI’s Stable Image Ultra model, processing your text prompt and generating a corresponding image with the specified aspect ratio and style.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| What you wish to see in the output image. A strong, descriptive prompt that clearly defines elements, colors, and subjects will lead to better results. To control the weight of a given word use the format `(word:weight)`, where `word` is the word you’d like to control the weight of and `weight` is a value between 0 and 1. For example: `The sky was a crisp (blue:0.3) and (green:0.8)` would convey a sky that was blue and green, but more green than blue.| STRING| Yes| -  
`aspect_ratio`| Aspect ratio of generated image (default: “1:1”).| COMBO| Yes| `"1:1"`  
`"16:9"`  
`"21:9"`  
`"2:3"`  
`"3:2"`  
`"4:5"`  
`"5:4"`  
`"9:16"`  
`"9:21"`  
`style_preset`| Optional desired style of generated image. Select “None” to not apply any style preset.| COMBO| No| `"3d-model"`  
`"analog-film"`  
`"anime"`  
`"cinematic"`  
`"comic-book"`  
`"digital-art"`  
`"enhance"`  
`"fantasy-art"`  
`"isometric"`  
`"line-art"`  
`"low-poly"`  
`"modeling-compound"`  
`"neon-punk"`  
`"origami"`  
`"photographic"`  
`"pixel-art"`  
`"tile-texture"`  
`seed`| The random seed used for creating the noise.| INT| Yes| 0 - 4294967294  
`image`| Optional input image for image-to-image generation.| IMAGE| No| -  
`negative_prompt`| A blurb of text describing what you do not wish to see in the output image. This is an advanced feature.| STRING| No| -  
`image_denoise`| Denoise of input image; 0.0 yields image identical to input, 1.0 is as if no image was provided at all (default: 0.5).| FLOAT| No| 0.0 - 1.0  
  
**Note:** When an input image is not provided, the `image_denoise` parameter is automatically disabled and ignored.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated image based on the input parameters.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/en.md)

* * *

**Source fingerprint (SHA-256):** `86a9ace60a1f9f2b872865381c695bd0e3e3578e0dd3453f1ab3be58bae2e2f0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StabilityStableImageUltraNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StabilityStableImageUltraNode)

[StabilityStableImageSD_3_5Node](https://docs.comfy.org/built-in-nodes/StabilityStableImageSD_3_5Node)[StabilityTextToAudio](https://docs.comfy.org/built-in-nodes/StabilityTextToAudio)
