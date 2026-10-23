---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/HolisticLandmarkerResult/
title: mp.tasks.vision.HolisticLandmarkerResult \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:38.444439+00:00
---

# mp.tasks.vision.HolisticLandmarkerResult  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/HolisticLandmarkerResult/




#  mp.tasks.vision.HolisticLandmarkerResult

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/holistic_landmarker.py#L68-L170) The holistic landmarks result from HolisticLandmarker, where each vector element represents a single holistic detected in the image.
    
    
    mp.tasks.vision.HolisticLandmarkerResult(
        face_landmarks: List[[mp.tasks.components.containers.NormalizedLandmark](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark)],
        pose_landmarks: List[[mp.tasks.components.containers.NormalizedLandmark](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark)],
        pose_world_landmarks: List[[mp.tasks.components.containers.Landmark](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Landmark)],
        left_hand_landmarks: List[[mp.tasks.components.containers.NormalizedLandmark](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark)],
        left_hand_world_landmarks: List[[mp.tasks.components.containers.Landmark](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Landmark)],
        right_hand_landmarks: List[[mp.tasks.components.containers.NormalizedLandmark](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark)],
        right_hand_world_landmarks: List[[mp.tasks.components.containers.Landmark](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Landmark)],
        face_blendshapes: Optional[List[category_lib.Category]] = None,
        segmentation_mask: Optional[[mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image)] = None
    )
    

| 

## Attributes  
  
---  
  
`face_landmarks` |  Detected face landmarks in normalized image coordinates.   
`pose_landmarks` |  Detected pose landmarks in normalized image coordinates.   
`pose_world_landmarks` |  Detected pose world landmarks in image coordinates.   
`left_hand_landmarks` |  Detected left hand landmarks in normalized image coordinates.   
`left_hand_world_landmarks` |  Detected left hand landmarks in image coordinates.   
`right_hand_landmarks` |  Detected right hand landmarks in normalized image coordinates.   
`right_hand_world_landmarks` |  Detected right hand landmarks in image coordinates.   
`face_blendshapes` |  Optional face blendshapes.   
`segmentation_mask` |  Optional segmentation mask for pose.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
face_blendshapes |  `None`  
segmentation_mask |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
