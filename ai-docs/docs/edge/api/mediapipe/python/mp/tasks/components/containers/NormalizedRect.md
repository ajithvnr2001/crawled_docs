---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedRect/
title: mp.tasks.components.containers.NormalizedRect \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:11.477051+00:00
---

# mp.tasks.components.containers.NormalizedRect  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedRect/




#  mp.tasks.components.containers.NormalizedRect

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/rect.py#L77-L123) A rectangle with rotation in normalized coordinates.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.image_processing_options_lib.rect_module.NormalizedRect`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedRect), [`mp.tasks.vision.drawing_styles.face_landmarker.image_processing_options_lib.rect_module.NormalizedRect`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedRect), [`mp.tasks.vision.drawing_styles.hand_landmarker.image_processing_options_lib.rect_module.NormalizedRect`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedRect), [`mp.tasks.vision.drawing_styles.pose_landmarker.image_processing_options_lib.rect_module.NormalizedRect`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedRect), [`mp.tasks.vision.drawing_utils.face_landmarker.image_processing_options_lib.rect_module.NormalizedRect`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedRect)
    
    
    mp.tasks.components.containers.NormalizedRect(
        x_center: float,
        y_center: float,
        width: float,
        height: float,
        rotation: Optional[float] = 0.0,
        rect_id: Optional[int] = None
    )
    

Location of the center of the rectangle in image coordinates. The (0.0, 0.0) point is at the (top, left) corner. The values of box center location and size are within [0, 1]. | 

## Attributes  
  
---  
  
`x_center` |  The normalized X coordinate of the rectangle, in image coordinates.   
`y_center` |  The normalized Y coordinate of the rectangle, in image coordinates.   
`width` |  The width of the rectangle.   
`height` |  The height of the rectangle.   
`rotation` |  Rotation angle is clockwise in radians.   
`rect_id` |  Optional unique id to help associate different rectangles to each other.   
  
## Methods

### `__eq__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/rect.py#L105-L123)
    
    
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
  
rect_id |  `None`  
rotation |  `0.0`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
