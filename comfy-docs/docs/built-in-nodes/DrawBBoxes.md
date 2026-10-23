---
url: https://docs.comfy.org/built-in-nodes/DrawBBoxes/
title: DrawBBoxes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:50.893064+00:00
---

# DrawBBoxes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DrawBBoxes/

Detection

# DrawBBoxes - ComfyUI Built-in Node Documentation

Copy pageCopy page

The DrawBBoxes node visualizes object detection results by drawing bounding boxes, labels, and confidence scores onto an image.

Copy pageCopy page

The DrawBBoxes node visualizes object detection results by drawing bounding boxes, labels, and confidence scores onto an image. If no input image is provided, it creates a blank canvas large enough to contain all the drawn boxes. It supports batch processing, allowing you to draw different sets of detections for multiple images or repeat the same detections across a batch.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image(s) to draw the bounding boxes onto. If not provided, a blank canvas will be generated.| IMAGE| No| -  
`bboxes`| A list of bounding box dictionaries. Each dictionary should contain keys for `x`, `y`, `width`, `height`, and optionally `label` and `score`.| BOUNDINGBOX| Yes| -  
  
**Input Constraints:**

  * The `bboxes` input is required and must be provided.
  * The node automatically handles different input formats for `bboxes`. A single dictionary will be applied to all images in the batch. A flat list of dictionaries will be treated as the same set of detections for every image. A list of lists allows you to specify different detections for each image in the batch.
  * If an `image` is not provided, the node will create a blank image with dimensions large enough to fit all provided bounding boxes, with a default minimum size of 640x640.
  * The `label` field in each bounding box dictionary is matched against the COCO dataset classes. If the label is not a recognized COCO class, it will be ignored and no text label will be drawn for that box.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`out_image`| The output image(s) with the drawn bounding boxes, labels, and confidence scores overlaid.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DrawBBoxes/en.md)

* * *

**Source fingerprint (SHA-256):** `ce5da10ec83e579515d70b7184fc78dfa04df4c514faccdcb75130212f56c84f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DrawBBoxes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DrawBBoxes)

[SplitImageWithAlpha - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SplitImageWithAlpha)[MediaPipeFaceLandmarker - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MediaPipeFaceLandmarker)

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
