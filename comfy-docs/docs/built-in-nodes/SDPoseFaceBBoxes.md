---
url: https://docs.comfy.org/built-in-nodes/SDPoseFaceBBoxes/
title: SDPoseFaceBBoxes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:55.200844+00:00
---

# SDPoseFaceBBoxes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SDPoseFaceBBoxes/

Detection

# SDPoseFaceBBoxes - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SDPoseFaceBBoxes node processes pose keypoint data to detect and generate bounding boxes around human faces.

Copy pageCopy page

The SDPoseFaceBBoxes node processes pose keypoint data to detect and generate bounding boxes around human faces. It analyzes the 2D face keypoints for each person in a frame, calculates a bounding box based on those points, and can adjust the box’s size and shape. The resulting bounding boxes are formatted to be compatible with other nodes in the SDPose workflow, such as the SDPoseKeypointExtractor.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`keypoints`| The pose keypoint data containing information about detected people and their body/face landmarks per frame.| POSE_KEYPOINT| Yes| -  
`scale`| Multiplier for the bounding box area around each detected face. A larger value creates a larger box. (default: 1.5)| FLOAT| No| 1.0 - 10.0  
`force_square`| Expand the shorter bbox axis so the crop region is always square. (default: True)| BOOLEAN| No| -  
  
**Note:** The `keypoints` input must be in the specific format produced by nodes like SDPoseKeypointExtractor, containing `canvas_height`, `canvas_width`, and `people` data with `face_keypoints_2d` for each person.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`bboxes`| A list of face bounding boxes for each frame. Each bounding box is defined by its top-left coordinates (`x`, `y`), `width`, and `height`. This output is compatible with the `bboxes` input of the SDPoseKeypointExtractor node.| BOUNDINGBOX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/en.md)

* * *

**Source fingerprint (SHA-256):** `dc68640f46afcba4c10a907fd9467671d508cd5bac7670b35a038d159f9d8f50`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SDPoseFaceBBoxes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SDPoseFaceBBoxes)

[SDPoseDrawKeypoints - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SDPoseDrawKeypoints)[SDPoseKeypointExtractor - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SDPoseKeypointExtractor)

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
