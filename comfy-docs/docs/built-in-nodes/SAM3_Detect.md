---
url: https://docs.comfy.org/built-in-nodes/SAM3_Detect/
title: SAM3_Detect - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.693090+00:00
---

# SAM3_Detect - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SAM3_Detect/

Detection

# SAM3_Detect - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SAM3 Detect node performs open-vocabulary detection and segmentation using text descriptions, bounding boxes, or point prompts.

Copy pageCopy page

## 

​

Overview

The SAM3 Detect node performs open-vocabulary detection and segmentation using text descriptions, bounding boxes, or point prompts. It can identify and segment objects in an image based on what you describe in text, where you draw boxes, or where you click points.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The SAM3 model to use for detection and segmentation| MODEL| Yes| -  
`image`| The input image to process| IMAGE| Yes| -  
`conditioning`| Text conditioning from CLIPTextEncode. Required when using text prompts for detection| CONDITIONING| No| -  
`bboxes`| Bounding boxes to segment within. Can be a single box (applied to all frames), a list of boxes (applied to all frames), or a list of lists (per-frame boxes). When provided without text conditioning, the node segments inside each box| BOUNDING_BOX| No| -  
`positive_coords`| Positive point prompts as JSON format `[{"x": int, "y": int}, ...]` using pixel coordinates. These are points you want to include in the segmentation| STRING| No| -  
`negative_coords`| Negative point prompts as JSON format `[{"x": int, "y": int}, ...]` using pixel coordinates. These are points you want to exclude from the segmentation| STRING| No| -  
`threshold`| Confidence threshold for text-based detections. Only detections with scores above this value are kept (default: 0.5)| FLOAT| No| 0.0 to 1.0  
`refine_iterations`| Number of SAM decoder refinement passes. Higher values can improve mask quality. Set to 0 to use raw detector masks without refinement (default: 2)| INT| No| 0 to 5  
`individual_masks`| When enabled, outputs separate masks for each detected object instead of combining them into a single mask (default: False)| BOOLEAN| No| True/False  
  
### 

​

Parameter Constraints and Notes

  * **Text prompts** : To use text-based detection, you must provide `conditioning` input. When text conditioning is provided, the node runs text-guided detection on the image.
  * **Box prompts** : When `bboxes` are provided without text conditioning, the node segments the area inside each bounding box.
  * **Point prompts** : When `positive_coords` or `negative_coords` are provided, the node uses point-based segmentation. Points are scaled to the model’s internal resolution automatically.
  * **Multiple prompt types** : You can combine different prompt types. For example, you can provide both text conditioning and bounding boxes to restrict text detection to specific areas.
  * **Batch processing** : The node supports batched images. When processing multiple frames, bounding boxes can be provided per-frame using a list of lists format.
  * **JSON format for points** : Point coordinates must be provided as valid JSON strings in the format `[{"x": 100, "y": 200}, {"x": 150, "y": 250}]`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`masks`| Segmentation masks. When `individual_masks` is False (default), returns a single combined mask per frame. When True, returns individual masks for each detected object| MASK  
`bboxes`| Detected bounding boxes with coordinates and confidence scores. Each box includes `x`, `y`, `width`, `height`, and `score` values| BOUNDING_BOX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_Detect/en.md)

* * *

**Source fingerprint (SHA-256):** `3f61343c284c249476f2010831863c6094260b11d0a348003b270a126c67d399`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SAM3_Detect.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SAM3_Detect)

[RTDETR_detect - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RTDETR_detect)[SAM3_TrackPreview - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SAM3_TrackPreview)

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
