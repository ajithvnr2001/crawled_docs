---
url: https://docs.comfy.org/tutorials/utility/face-detection/mediapipe/
title: MediaPipe: Face Detection in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:40.193555+00:00
---

# MediaPipe: Face Detection in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/face-detection/mediapipe/

## On this page

  * Key capabilities
  * MediaPipe Face Detection Workflow
    * Mediapipe: Image Face Detection
    * 1\. Download the Workflow
    * 2\. Download the Model
    * 3\. Using the Workflow
    * 4\. Run the Workflow
  * Community Resources



Face Detection

# MediaPipe: Face Detection in ComfyUI

Copy pageCopy page

Learn how to use MediaPipe Face Detection in ComfyUI to detect faces and extract facial landmarks, bounding boxes, and region masks from images

Copy pageCopy page

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

[MediaPipe](https://github.com/google-ai-edge/mediapipe) is Google’s open-source machine learning solution for real-time perception. In ComfyUI, MediaPipe Face Detection provides **BlazeFace** detection, **FaceMesh v2** landmark estimation, and **ARKit-52 blendshapes** , all in a single unified workflow. MediaPipe Face Detection is natively supported in ComfyUI (PR [#14009](https://github.com/Comfy-Org/ComfyUI/pull/14009)), and the model weights are available under the [Apache 2.0 License](https://github.com/google-ai-edge/mediapipe/blob/master/LICENSE). [MediaPipe GitHub](https://github.com/google-ai-edge/mediapipe) | [Comfy-Org Model Repository](https://huggingface.co/Comfy-Org/mediapipe)

### 

​

Key capabilities

  * **Fast face detection** : BlazeFace-based detector with short (~2 m) and full (~5 m) range variants
  * **478 facial landmarks** : dense FaceMesh v2 keypoints per detected face
  * **ARKit-52 blendshapes** : real-time facial expression coefficients
  * **Face region masks** : per-region masks for face oval, lips, eyes, and irises
  * **Face bounding boxes** : outputs compatible with `DrawBBoxes` for bounding box visualization



> **Scope:** Face detection only: BlazeFace + FaceMesh v2 + ARKit blendshapes. This does not cover hand, pose, or holistic detection.

## 

​

MediaPipe Face Detection Workflow

### 

​

Mediapipe: Image Face Detection

Input an image and detect up to 6 facial landmarks per face, enabling ultrafast multi-face detection. ![Mediapipe image face detection workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_face_detection_mediapipe-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Mediapipe: Image Face Detection” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## soft_neon_girl.png

`LoadImage` node 5 · `soft_neon_girl.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/soft_neon_girl.png)

### 

​

1\. Download the Workflow

Update your ComfyUI to the latest version, then go to `Workflow` → `Browse Templates` and find “Mediapipe: Image Face Detection” under the Utility category.

### 

​

2\. Download the Model

The MediaPipe Face Detection model is hosted on the [Comfy-Org MediaPipe model repository](https://huggingface.co/Comfy-Org/mediapipe).

  * [mediapipe_face_fp32.safetensors](https://huggingface.co/Comfy-Org/mediapipe/blob/main/detection/mediapipe_face_fp32.safetensors)

Place it in the following directory structure:
    
    
    📂 ComfyUI/
    └── 📂 models/
        └── 📂 detection/
            └── mediapipe_face_fp32.safetensors
    

### 

​

3\. Using the Workflow

This workflow uses a **subgraph** node that orchestrates face detection, visualization, and mask generation. The subgraph exposes the following controls:

## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

**Subgraph inputs:**

Input| Description  
---|---  
**image**|  Input image batch to analyze  
**face_landmarker**|  Optional. Leave empty to use the built-in model loader. Connect an external `FACE_DETECTION_MODEL` output to override  
  
**Subgraph parameters:**

Parameter| Default| Description  
---|---|---  
**model_name**| `mediapipe_face_fp32.safetensors`| Checkpoint in `ComfyUI/models/detection/`. If missing, download the model above  
**detector_variant**| `short`| **short** : tuned for close/large faces (~2 m range). **full** : covers smaller/farther faces (~5 m), slower. **both** : runs both detectors and keeps whichever found more faces per frame (~2× cost)  
**num_faces**| `1`| Maximum faces to return per frame. `0` = no cap (return all detected). Range: 0–16  
**custom_face_oval**| `false`| Include face-outline region in the mask output  
**custom_lips**| `false`| Include lips in the mask (union with other enabled regions)  
**custom_left_eye**| `false`| Include left eye region in the mask  
**custom_right_eye**| `false`| Include right eye region in the mask  
**custom_irises**| `false`| Include iris regions in the mask  
  
Mask toggles use custom mode internally: only checked regions are filled; multiple ON regions are **unioned** into one mask per frame. **Subgraph outputs:**

Output| Type| Description  
---|---|---  
**face_landmarks**| `FACE_LANDMARKS`| Per-frame faces with 478 2D/3D landmarks, ARKit-52 blendshapes, mesh topology data. Feeds into visualization and mask nodes  
**bboxes**| `BOUNDING_BOX`| Face bounding boxes: compatible with `DrawBBoxes` node  
**mask**| `MASK`| Binary mask from the enabled region toggles  
  
### 

​

4\. Run the Workflow

  1. Ensure the model file is placed in `ComfyUI/models/detection/`
  2. Load an image in the `Load Image` node
  3. Adjust detection parameters as needed
  4. Click `Queue` or use `Ctrl(Cmd) + Enter` to run
  5. The workflow outputs the mesh overlay, bounding boxes, and mask preview



## 

​

Community Resources

  * [MediaPipe GitHub](https://github.com/google-ai-edge/mediapipe): Upstream MediaPipe framework
  * [Comfy-Org/mediapipe](https://huggingface.co/Comfy-Org/mediapipe): Official ComfyUI model weights
  * [ComfyUI Subgraph Guide](https://docs.comfy.org/interface/features/subgraph): Learn how subgraphs work



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/face-detection/mediapipe.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/face-detection/mediapipe)

[SDPose: Pose Detection in ComfyUIPrevious](https://docs.comfy.org/tutorials/utility/pose-detection-sdpose)[SAM 3D Body: Extract 3D Human Mesh From Video in ComfyUINext](https://docs.comfy.org/tutorials/utility/sam3d-body)

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
