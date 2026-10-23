---
url: https://docs.comfy.org/built-in-nodes/RTDETR_detect/
title: RTDETR_detect - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:46.408021+00:00
---

# RTDETR_detect - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RTDETR_detect/

Detection

# RTDETR_detect - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RT-DETR Detect node performs object detection on input images using an RT-DETR model.

Copy pageCopy page

The RT-DETR Detect node performs object detection on input images using an RT-DETR model. It identifies objects, returns bounding boxes around them, and labels them according to the COCO dataset classes. You can filter the results by confidence score, object class, and limit the total number of detections.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The RT-DETR model used for object detection.| MODEL| Yes| N/A  
`image`| The input image(s) to detect objects in. The node processes images in batches of up to 32.| IMAGE| Yes| N/A  
`threshold`| The minimum confidence score a detection must have to be included in the results (default: 0.5).| FLOAT| Yes| N/A  
`class_name`| Filter detections by class. Set to ‘all’ to disable filtering (default: “all”).| COMBO| Yes| `"all"`  
`"person"`  
`"bicycle"`  
`"car"`  
`"motorcycle"`  
`"airplane"`  
`"bus"`  
`"train"`  
`"truck"`  
`"boat"`  
`"traffic light"`  
`"fire hydrant"`  
`"stop sign"`  
`"parking meter"`  
`"bench"`  
`"bird"`  
`"cat"`  
`"dog"`  
`"horse"`  
`"sheep"`  
`"cow"`  
`"elephant"`  
`"bear"`  
`"zebra"`  
`"giraffe"`  
`"backpack"`  
`"umbrella"`  
`"handbag"`  
`"tie"`  
`"suitcase"`  
`"frisbee"`  
`"skis"`  
`"snowboard"`  
`"sports ball"`  
`"kite"`  
`"baseball bat"`  
`"baseball glove"`  
`"skateboard"`  
`"surfboard"`  
`"tennis racket"`  
`"bottle"`  
`"wine glass"`  
`"cup"`  
`"fork"`  
`"knife"`  
`"spoon"`  
`"bowl"`  
`"banana"`  
`"apple"`  
`"sandwich"`  
`"orange"`  
`"broccoli"`  
`"carrot"`  
`"hot dog"`  
`"pizza"`  
`"donut"`  
`"cake"`  
`"chair"`  
`"couch"`  
`"potted plant"`  
`"bed"`  
`"dining table"`  
`"toilet"`  
`"tv"`  
`"laptop"`  
`"mouse"`  
`"remote"`  
`"keyboard"`  
`"cell phone"`  
`"microwave"`  
`"oven"`  
`"toaster"`  
`"sink"`  
`"refrigerator"`  
`"book"`  
`"clock"`  
`"vase"`  
`"scissors"`  
`"teddy bear"`  
`"hair drier"`  
`"toothbrush"`  
`max_detections`| Maximum number of detections to return per image. In order of descending confidence score (default: 100).| INT| Yes| N/A  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`bboxes`| A list of bounding boxes for each input image. Each box contains coordinates (x, y, width, height), a class label, and a confidence score.| BOUNDINGBOX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/en.md)

* * *

**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RTDETR_detect.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RTDETR_detect)

[MediaPipeFaceMeshVisualize - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MediaPipeFaceMeshVisualize)[SAM3_Detect - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SAM3_Detect)

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
