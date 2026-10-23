---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/PoseLandmarkerResult/
title: mp.tasks.vision.PoseLandmarkerResult \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:43.349238+00:00
---

# mp.tasks.vision.PoseLandmarkerResult  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/PoseLandmarkerResult/




#  mp.tasks.vision.PoseLandmarkerResult

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/pose_landmarker.py#L63-L107) The pose landmarks detection result from PoseLandmarker, where each vector element represents a single pose detected in the image.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.pose_landmarker.PoseLandmarkerResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/PoseLandmarkerResult)
    
    
    mp.tasks.vision.PoseLandmarkerResult(
        pose_landmarks: list[list[landmark_lib.NormalizedLandmark]],
        pose_world_landmarks: list[list[landmark_lib.Landmark]],
        segmentation_masks: Optional[list[image_lib.Image]] = None
    )
    

| 

## Attributes  
  
---  
  
`pose_landmarks` |  Detected pose landmarks in normalized image coordinates.   
`pose_world_landmarks` |  Detected pose landmarks in world coordinates.   
`segmentation_masks` |  Optional segmentation masks for pose.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
segmentation_masks |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
