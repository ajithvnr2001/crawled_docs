---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/keypoint/NormalizedKeypoint/
title: mp.tasks.components.containers.keypoint.NormalizedKeypoint \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:18.483519+00:00
---

# mp.tasks.components.containers.keypoint.NormalizedKeypoint  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/keypoint/NormalizedKeypoint/




#  mp.tasks.components.containers.keypoint.NormalizedKeypoint

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/keypoint.py#L23-L72) A normalized keypoint.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.detections_module.keypoint_lib.NormalizedKeypoint`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/keypoint/NormalizedKeypoint), [`mp.tasks.vision.drawing_utils.detections_module.keypoint_lib.NormalizedKeypoint`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/keypoint/NormalizedKeypoint)
    
    
    mp.tasks.components.containers.keypoint.NormalizedKeypoint(
        x: Optional[float] = None,
        y: Optional[float] = None,
        label: Optional[str] = None,
        score: Optional[float] = None
    )
    

Normalized keypoint represents a point in 2D space with x, y coordinates. x and y are normalized to [0.0, 1.0] by the image width and height respectively. | 

## Attributes  
  
---  
  
`x` |  The x coordinates of the normalized keypoint.   
`y` |  The y coordinates of the normalized keypoint.   
`label` |  The optional label of the keypoint.   
`score` |  The score of the keypoint.   
  
## Methods

### `__eq__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/keypoint.py#L56-L72)
    
    
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
  
## Class Variables  
  
---  
  
label |  `None`  
score |  `None`  
x |  `None`  
y |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
