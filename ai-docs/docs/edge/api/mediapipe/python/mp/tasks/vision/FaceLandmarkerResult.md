---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerResult/
title: mp.tasks.vision.FaceLandmarkerResult \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:33.224967+00:00
---

# mp.tasks.vision.FaceLandmarkerResult  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerResult/




#  mp.tasks.vision.FaceLandmarkerResult

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_landmarker.py#L2889-L2930) The face landmarks detection result from FaceLandmarker, where each vector element represents a single face detected in the image.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.FaceLandmarkerResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerResult), [`mp.tasks.vision.drawing_styles.face_landmarker.FaceLandmarkerResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerResult), [`mp.tasks.vision.drawing_utils.face_landmarker.FaceLandmarkerResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerResult)
    
    
    mp.tasks.vision.FaceLandmarkerResult(
        face_landmarks: List[List[landmark_lib.NormalizedLandmark]],
        face_blendshapes: List[List[category_lib.Category]],
        facial_transformation_matrixes: List[np.ndarray]
    )
    

| 

## Attributes  
  
---  
  
`face_landmarks` |  Detected face landmarks in normalized image coordinates.   
`face_blendshapes` |  Optional face blendshapes results.   
`facial_transformation_matrixes` |  Optional facial transformation matrix.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
