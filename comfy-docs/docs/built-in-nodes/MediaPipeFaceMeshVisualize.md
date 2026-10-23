---
url: https://docs.comfy.org/built-in-nodes/MediaPipeFaceMeshVisualize/
title: MediaPipeFaceMeshVisualize - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.960475+00:00
---

# MediaPipeFaceMeshVisualize - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MediaPipeFaceMeshVisualize/

Detection

# MediaPipeFaceMeshVisualize - ComfyUI Built-in Node Documentation

Copy pageCopy page

Draws face landmark points and connection lines (a face mesh) on top of an input image.

Copy pageCopy page

## 

​

Overview

Draws face landmark points and connection lines (a face mesh) on top of an input image. This node uses the landmark data produced by a face detection node to visualize the detected facial features, such as the eyes, nose, mouth, and face outline.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`face_landmarks`| The face landmark data from a detection node.| FACE_LANDMARKS| Yes|   
`image`| The image to draw the mesh on. If not connected, a black canvas of the same size as the detection result will be used.| IMAGE| No|   
`connections`| Determines which parts of the face mesh to draw. `"all"` draws the full mesh (oval, eyes, brows, lips, irises, nose). `"fill"` draws a solid polygon of the face oval (silhouette mask). `"custom"` lets you toggle each feature individually. (default: `"all"`)| COMBO| Yes| `"all"`  
`"fill"`  
`"custom"`  
`color`| The color of the mesh lines and points. (default: `#00ff00`)| COLOR| Yes|   
`thickness`| The thickness of the mesh lines in pixels. Setting this to 0 disables line drawing. (default: 1)| INT| Yes| 0 to 8  
`point_size`| The radius of the landmark dots in pixels. Setting this to 0 disables dot drawing. (default: 2)| INT| Yes| 0 to 16  
  
**Note on`connections` parameter:** When `"custom"` is selected, additional boolean inputs appear for each facial feature (e.g., `face_oval`, `lips`, `left_eye`, `right_eye`, `left_eyebrow`, `right_eyebrow`, `left_iris`, `right_iris`, `nose`, `tesselation`). Only the features you enable will be drawn.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The input image with the face landmarks mesh drawn on it.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMeshVisualize/en.md)

* * *

**Source fingerprint (SHA-256):** `fb5437d73378b0c8daa68669c2e19058ccb7133ed68fc51c8d4c5bab8662f243`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MediaPipeFaceMeshVisualize.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MediaPipeFaceMeshVisualize)

[MediaPipeFaceMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MediaPipeFaceMask)[RTDETR_detect - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RTDETR_detect)

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
