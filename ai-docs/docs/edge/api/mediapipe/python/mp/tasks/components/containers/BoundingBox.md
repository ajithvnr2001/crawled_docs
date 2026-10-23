---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/BoundingBox/
title: mp.tasks.components.containers.BoundingBox \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:08.884270+00:00
---

# mp.tasks.components.containers.BoundingBox  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/BoundingBox/




#  mp.tasks.components.containers.BoundingBox

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/bounding_box.py#L23-L66) An integer bounding box, axis aligned.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.detections_module.bounding_box_lib.BoundingBox`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/BoundingBox), [`mp.tasks.vision.drawing_utils.detections_module.bounding_box_lib.BoundingBox`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/BoundingBox)
    
    
    mp.tasks.components.containers.BoundingBox(
        origin_x: int, origin_y: int, width: int, height: int
    )
    

| 

## Attributes  
  
---  
  
`origin_x` |  The X coordinate of the top-left corner, in pixels.   
`origin_y` |  The Y coordinate of the top-left corner, in pixels.   
`width` |  The width of the bounding box, in pixels.   
`height` |  The height of the bounding box, in pixels.   
  
## Methods

### `__eq__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/bounding_box.py#L50-L66)
    
    
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
