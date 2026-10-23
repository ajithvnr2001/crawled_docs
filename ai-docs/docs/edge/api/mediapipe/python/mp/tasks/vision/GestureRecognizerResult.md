---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizerResult/
title: mp.tasks.vision.GestureRecognizerResult \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:34.922401+00:00
---

# mp.tasks.vision.GestureRecognizerResult  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizerResult/




#  mp.tasks.vision.GestureRecognizerResult

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer_result.py#L26-L96) The gesture recognition result from GestureRecognizer.

#### View aliases

**Main aliases** [`mp.tasks.vision.gesture_recognizer_result.GestureRecognizerResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizerResult)
    
    
    mp.tasks.vision.GestureRecognizerResult(
        gestures: list[list[category_module.Category]],
        handedness: list[list[category_module.Category]],
        hand_landmarks: list[list[landmark_module.NormalizedLandmark]],
        hand_world_landmarks: list[list[landmark_module.Landmark]]
    )
    

Each vector element represents a single hand detected in the image. | 

## Attributes  
  
---  
  
`gestures` |  Recognized hand gestures of detected hands. Note that the index of the gesture is always -1, because the raw indices from multiple gesture classifiers cannot consolidate to a meaningful index.   
`handedness` |  Classification of handedness.   
`hand_landmarks` |  Detected hand landmarks in normalized image coordinates.   
`hand_world_landmarks` |  Detected hand landmarks in world coordinates.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
