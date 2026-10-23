---
url: https://docs.comfy.org/built-in-nodes/MediaPipeFaceLandmarker/
title: MediaPipeFaceLandmarker - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.082743+00:00
---

# MediaPipeFaceLandmarker - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MediaPipeFaceLandmarker/

Detection

# MediaPipeFaceLandmarker - ComfyUI Built-in Node Documentation

Copy pageCopy page

Detects faces in an image and identifies 468 facial landmarks (key points) on each face using MediaPipe’s BlazeFace and FaceMesh models.

Copy pageCopy page

## 

​

Overview

Detects faces in an image and identifies 468 facial landmarks (key points) on each face using MediaPipe’s BlazeFace and FaceMesh models. It also calculates ARKit-52 blendshape coefficients for facial expression analysis. The node can process multiple images in a batch and outputs both the landmark data and bounding boxes for each detected face.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`face_detection_model`| The MediaPipe face detection model to use for landmark detection.| FACE_DETECTION_MODEL| Yes|   
`image`| The input image or batch of images to detect faces in.| IMAGE| Yes|   
`detector_variant`| Face detector range. `"short"` is tuned for close-up faces (within ~2 m of the camera); `"full"` covers farther/smaller faces (up to ~5 m) but is slower. `"both"` runs both detectors and keeps whichever found more faces per frame (~2x detection cost). Default: `"short"`.| COMBO| Yes| `"short"`  
`"full"`  
`"both"`  
`num_faces`| Maximum number of faces to return per frame. 0 means no cap (return all detected). Default: 1.| INT| Yes| 0 to 16  
`min_confidence`| BlazeFace score threshold. Lower values help catch small or occluded faces. Default: 0.5.| FLOAT| No| 0.00 to 1.00  
`missing_frame_fallback`| Per-frame behavior when detection fails in a batch. `"empty"` leaves the frame faceless. `"previous"` copies the most recent successful detection. `"interpolate"` lerps landmarks/bbox/blendshapes between bracketing successful frames. Multi-face: pairs faces across frames by greedy bbox-centre NN. Default: `"empty"`.| COMBO| No| `"empty"`  
`"previous"`  
`"interpolate"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`face_landmarks`| A structured output containing per-frame face detection results, including 468 facial landmarks, ARKit-52 blendshape coefficients, transformation matrices, and connection sets for mesh visualization.| FACE_LANDMARKS  
`bboxes`| A list of bounding boxes for each detected face, with coordinates (x, y, width, height), label “face”, and confidence score. One list per input frame.| BOUNDING_BOX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceLandmarker/en.md)

* * *

**Source fingerprint (SHA-256):** `f60ed6201288a59d65d62cc98c12f227a353870c36decea8da81a063cfdf2bba`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MediaPipeFaceLandmarker.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MediaPipeFaceLandmarker)

[DrawBBoxes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DrawBBoxes)[MediaPipeFaceMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MediaPipeFaceMask)

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
