---
url: https://docs.comfy.org/built-in-nodes/SDPoseKeypointExtractor/
title: SDPoseKeypointExtractor - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:55.267793+00:00
---

# SDPoseKeypointExtractor - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SDPoseKeypointExtractor/

Detection

# SDPoseKeypointExtractor - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SDPoseKeypointExtractor node detects human pose keypoints from input images using the SDPose model.

Copy pageCopy page

The SDPoseKeypointExtractor node detects human pose keypoints from input images using the SDPose model. It can process full images or specific regions defined by bounding boxes and outputs the detected keypoints in the OpenPose format, which includes the coordinates for each person and a confidence score for each keypoint.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The SDPose model used for keypoint detection. Must be a model with a `heatmap_head` attribute, specifically from the SDPose repository.| MODEL| Yes| -  
`vae`| The VAE model used to encode the input images into the latent space for processing.| VAE| Yes| -  
`image`| The input image or batch of images from which to extract pose keypoints.| IMAGE| Yes| -  
`batch_size`| The number of images to process at once when running in full-image mode (i.e., when `bboxes` is not provided). This can speed up processing. (default: 16)| INT| No| 1 to 10000  
`bboxes`| Optional bounding boxes for more accurate detections. Required for multi-person detection. If provided, the node will extract keypoints from each specified region.| BOUNDINGBOX| No| -  
  
**Parameter Constraints:**

  * The `model` input must be a specific SDPose model. If the provided model does not have a `heatmap_head` attribute, the node will raise an error.
  * The node operates in two distinct modes based on the `bboxes` input: 
    1. **Bounding Box Mode:** When `bboxes` is provided, it processes each specified region individually. This is required for detecting multiple people in a single image.
    2. **Full-Image Mode:** When `bboxes` is not provided, it processes the entire image as a batch. The `batch_size` parameter only applies in this mode.
  * When `bboxes` is provided, it must be a list of bounding boxes. If there are fewer bounding box lists than images, the last list is reused for remaining images.
  * Bounding boxes with zero width or height (e.g., `x2 <= x1` or `y2 <= y1`) are skipped.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`keypoints`| Keypoints in OpenPose frame format (canvas_width, canvas_height, people). The output contains the detected persons, each with an array of keypoint coordinates (x, y) and their corresponding confidence scores.| POSE_KEYPOINT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/en.md)

* * *

**Source fingerprint (SHA-256):** `5e199e9d08a46d934c6d1f4b1a411f0ca95eb5e7f85ec39f59a058c9be598e9f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SDPoseKeypointExtractor.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SDPoseKeypointExtractor)

[SDPoseFaceBBoxes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SDPoseFaceBBoxes)[Canny - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Canny)

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
