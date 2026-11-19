---
url: https://docs.comfy.org/built-in-nodes/Kling4ImageNode/
title: Kling4ImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-19T16:26:05.527268+00:00
---

# Kling4ImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Kling4ImageNode/

Kling

# Kling4ImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate or edit images with Kling 4.0 from a text prompt and up to 10 reference images.

Copy pageCopy page

Generate or edit images with Kling 4.0 from a text prompt and up to 10 reference images. Ask for a single image, or let the node return a series of related images that keep the same characters and style.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference_images`| Growable slots for reference images (`image_1` … `image_10`). Refer to them in the prompt as `@Image1`, `@Image2` and so on.| AUTOGROW| No| 0 to 10 images  
`prompt`| Description of the image. Refer to the connected images as `@Image1`, `@Image2`, … Default: empty string.| STRING| Yes| Multiline text  
`resolution`| Resolution of the output image. Default: `"2K"`.| COMBO| Yes| `"2K"`  
`"4K"`  
`"8K"`  
`aspect_ratio`| Aspect ratio of the output image. `"auto"` follows the reference images, otherwise the prompt. Default: `"auto"`.| COMBO| Yes| `"auto"`  
`"9:16"`  
`"2:3"`  
`"3:4"`  
`"1:1"`  
`"4:3"`  
`"3:2"`  
`"16:9"`  
`"21:9"`  
`series_amount`| Generate a series of related images that keep the same characters and style. `"auto"` lets the model choose 2 to 10 images. Default: `"disabled"`.| COMBO| Yes| `"disabled"`  
`"auto"`  
`"2"`  
`"3"`  
`"4"`  
`"5"`  
`"6"`  
`"7"`  
`"8"`  
`"9"`  
`"10"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. Default: 42.| INT| Yes| 0 to 2147483647  
  
**Constraints and behavior:**

  * At most 10 reference images can be connected.
  * Every image must be at least 300x300 pixels with an aspect ratio between 2:5 and 5:2.
  * A prompt that mentions `@ImageN` raises an error when fewer than N images are connected.
  * With `series_amount` set to `"disabled"` the node returns one image; any other value returns a batch of that many images.
  * The price of a call scales with the resolution, the number of reference images and the number of images in the series.



## Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image, or a batch of images when `series_amount` is enabled.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `7840b108419e759942aed332456cab73e748d9f018462011da3b1293646a4ffe`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Kling4ImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Kling4ImageNode)

[Ideogram V4](https://docs.comfy.org/built-in-nodes/IdeogramV4)[Kling4LongImageNode](https://docs.comfy.org/built-in-nodes/Kling4LongImageNode)
