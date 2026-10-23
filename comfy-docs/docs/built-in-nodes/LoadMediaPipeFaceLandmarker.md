---
url: https://docs.comfy.org/built-in-nodes/LoadMediaPipeFaceLandmarker/
title: LoadMediaPipeFaceLandmarker - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:23.770908+00:00
---

# LoadMediaPipeFaceLandmarker - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadMediaPipeFaceLandmarker/

Loaders

# LoadMediaPipeFaceLandmarker - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node loads a MediaPipe Face Landmarker v2 model, which detects faces and facial landmarks (such as eyes, nose, and mouth) in images.

Copy pageCopy page

This node loads a MediaPipe Face Landmarker v2 model, which detects faces and facial landmarks (such as eyes, nose, and mouth) in images. The loaded model bundles two detection variants (short-range and full-range) together with shared mesh data, blendshapes, and canonical geometry used for facial analysis.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| Face detection model from models/detection/.| COMBO| Yes| List of available model filenames found in the `models/detection/` directory  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`FACE_DETECTION_MODEL`| A loaded FaceLandmarker model object containing both detection variants (short/full), connection sets for facial topology, canonical data, and model patchers for GPU management.| FACE_DETECTION_MODEL  
  
**Note:** The output is a complex object that can be used by other nodes for face detection and landmark extraction tasks. It contains two detection variants: “short” for close-range detection and “full” for full-range detection.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/en.md)

* * *

**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadMediaPipeFaceLandmarker.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadMediaPipeFaceLandmarker)

[LoadLoraTextEncoder - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadLoraTextEncoder)[LoadMoGeModel - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadMoGeModel)

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
