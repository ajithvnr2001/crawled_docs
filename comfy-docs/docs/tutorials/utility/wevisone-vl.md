---
url: https://docs.comfy.org/tutorials/utility/wevisone-vl/
title: WeVisOne-VL in ComfyUI: Text-Prompted Segmentation and Detection - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:07:52.352528+00:00
---

# WeVisOne-VL in ComfyUI: Text-Prompted Segmentation and Detection - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/wevisone-vl/

## On this page

Back to top

  * Image Segmentation: WeVisOne-VL
  * Tasks
  * Models
  * More control on the node



Segmentation & Background

# WeVisOne-VL in ComfyUI: Text-Prompted Segmentation and Detection

Copy pageCopy page

Segment, detect, count, and OCR images in ComfyUI with WeVisOne-VL: one short text query in, alpha mattes, boxes, points, or the raw answer out.

Copy pageCopy page

WeVisOne-VL is a compact vision-language model that answers in shapes instead of prose. Give it an image and a short text query, and it returns boxes, points, or a per-instance alpha matte in one pass: no annotation, no per-object prompting. In ComfyUI it runs as the **WeVisOne-VL Detect** node. The template below wraps it in a subgraph and previews the matte, the boxes drawn over the source image, and foreground and background cutouts, so the matte drops straight into a background-removal, masking, or compositing chain. The weights are the Apache-2.0 Tencent releases, repackaged for ComfyUI in [Comfy-Org/WeVisOne-VL](https://huggingface.co/Comfy-Org/WeVisOne-VL). Support landed in [ComfyUI #17632](https://github.com/Comfy-Org/ComfyUI/pull/17632) and the template needs ComfyUI 0.45.0 or later.

  * Local users

  * Cloud users




Make sure your ComfyUI is updated.

  * [Download ComfyUI](https://www.comfy.org/download)
  * [Update Guide](https://docs.comfy.org/installation/update_comfyui)

Workflows in this guide can be found in the [Workflow Templates](https://docs.comfy.org/interface/features/template). If you can’t find them in the template, your ComfyUI may be outdated.If nodes are missing when loading a workflow, possible reasons:

  1. You are not using the latest ComfyUI version (Nightly version)
  2. Some nodes failed to import at startup



  * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.

## Image Segmentation: WeVisOne-VL

Type what you want cut out in `query` and run. With the default `segmentation` task and the query `human`, the graph returns one combined matte of the people it finds, plus their boxes. Turn on `individual_masks` on the node for a separate matte per person. ![WeVisOne-VL segmentation workflow preview with matte, boxes and cutouts](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_segment_wevisone_vl-1.webp)

## Download Workflow

Download JSON or search “Image Segmentation: WeVisOne-VL” in Template Library

**Input material**

## utility_image_segment_wevisone_vl_input.png

Load into the `LoadImage` node

## Tasks

The `task` widget rewrites your query into the instruction the checkpoint was trained on. Each task takes its query in a slightly different form:

`task`| Query form| Returns  
---|---|---  
`segmentation`| One short noun phrase, such as `human`| Alpha matte plus boxes (one combined matte unless `individual_masks` is on)  
`detection`| One label per line| Boxes only  
`referring`| A describing phrase, such as `the cup on the left`| Boxes  
`point`| One label per line| Centre points as JSON  
`count_box`| The subject to count| A count, with a box on each instance  
`count_point`| The subject to count| A count, with a point on each instance  
`ocr`| Nothing| A box on every word in the image  
`ocr_grounding`| The exact string to find| A box around that string  
`visual_prompt`| Nothing, uses the `bboxes` input| Boxes for objects similar to the reference boxes  
`freeform`| Anything| The raw answer, with the query as the whole prompt  
  
Keep the query short. A full sentence makes `segmentation` ramble, and a phrase that names the thing works better than a description of it.

## Models

The workflow loads the 2B INT8 text encoder. The other three files are drop-in swaps for `clip_name` in the `CLIPLoader` node (`stable_diffusion` type): the 4B pair is heavier and slower, and the BF16 files trade size for precision.

## 2B INT8 (this workflow)

wevisone_vl_2b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## 2B BF16

wevisone_vl_2b_bf16.safetensors → ComfyUI/models/text_encoders/

## 4B INT8

wevisone_vl_4b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## 4B BF16

wevisone_vl_4b_bf16.safetensors → ComfyUI/models/text_encoders/

## More control on the node

  * **`individual_masks`** : on, one mask per box; off, one union mask per frame
  * **`max_length`** : answer length cap, 4096 tokens by default and up to 32768
  * **Outputs** : `masks`, `bboxes`, `points` (JSON with x, y, label and frame), and `text` (the raw answer)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/wevisone-vl.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/wevisone-vl)

[SAM 3.1 segmentation](https://docs.comfy.org/tutorials/utility/video-segment-sam3)[BiRefNet](https://docs.comfy.org/tutorials/utility/remove-background-birefnet)
