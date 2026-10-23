---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult/
title: mp.tasks.vision.FaceDetectorResult \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:31.480184+00:00
---

# mp.tasks.vision.FaceDetectorResult  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult/




#  mp.tasks.vision.FaceDetectorResult

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/detections.py#L88-L122) Represents the list of detected objects.

#### View aliases

**Main aliases** [`mp.tasks.components.containers.DetectionResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult), [`mp.tasks.vision.ObjectDetectorResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult), [`mp.tasks.vision.drawing_styles.drawing_utils.detections_module.DetectionResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult), [`mp.tasks.vision.drawing_utils.detections_module.DetectionResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult)
    
    
    mp.tasks.vision.FaceDetectorResult(
        detections: List[[mp.tasks.components.containers.Detection](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Detection)]
    )
    

| 

## Attributes  
  
---  
  
`detections` |  A list of `Detection` objects.   
  
## Methods

### `__eq__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/detections.py#L98-L109)
    
    
    __eq__(
        other: Any
    ) -> bool
    

Checks if this object is equal to the given object.

Args  
---  
  
`other` |  The object to be compared with.   
  
Returns  
---  
True if the objects are equal.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
