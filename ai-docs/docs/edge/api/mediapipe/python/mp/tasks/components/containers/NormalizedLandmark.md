---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark/
title: mp.tasks.components.containers.NormalizedLandmark \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:11.189701+00:00
---

# mp.tasks.components.containers.NormalizedLandmark  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark/




#  mp.tasks.components.containers.NormalizedLandmark

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/landmark.py#L66-L108) A normalized version of above Landmark proto.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.landmark_lib.NormalizedLandmark`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark), [`mp.tasks.vision.drawing_styles.drawing_utils.landmark_module.NormalizedLandmark`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark), [`mp.tasks.vision.drawing_styles.face_landmarker.landmark_lib.NormalizedLandmark`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark), [`mp.tasks.vision.drawing_styles.hand_landmarker.landmark.NormalizedLandmark`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark), [`mp.tasks.vision.drawing_styles.pose_landmarker.landmark_lib.NormalizedLandmark`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark), [`mp.tasks.vision.drawing_utils.face_landmarker.landmark_lib.NormalizedLandmark`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark), [`mp.tasks.vision.drawing_utils.landmark_module.NormalizedLandmark`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark), [`mp.tasks.vision.gesture_recognizer_result.landmark_module.NormalizedLandmark`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark)
    
    
    mp.tasks.components.containers.NormalizedLandmark(
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        visibility: Optional[float] = None,
        presence: Optional[float] = None,
        name: Optional[str] = None
    )
    

All coordinates should be within [0, 1]. | 

## Attributes  
  
---  
  
`x` |  The normalized x coordinate.   
`y` |  The normalized y coordinate.   
`z` |  The normalized z coordinate.   
`visibility` |  Landmark visibility. Should stay unset if not supported. Float score of whether landmark is visible or occluded by other objects. Landmark considered as invisible also if it is not present on the screen (out of scene bounds). Depending on the model, visibility value is either a sigmoid or an argument of sigmoid.   
`presence` |  Landmark presence. Should stay unset if not supported. Float score of whether landmark is present on the scene (located within scene bounds). Depending on the model, presence value is either a result of sigmoid or an argument of sigmoid function to get landmark presence probability.   
`name` |  The name of the landmark.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
name |  `None`  
presence |  `None`  
visibility |  `None`  
x |  `None`  
y |  `None`  
z |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
