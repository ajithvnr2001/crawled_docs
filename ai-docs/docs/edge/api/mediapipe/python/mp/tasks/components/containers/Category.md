---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Category/
title: mp.tasks.components.containers.Category \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:09.715488+00:00
---

# mp.tasks.components.containers.Category  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Category/




#  mp.tasks.components.containers.Category

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/category.py#L23-L86) A classification category.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.detections_module.category_lib.Category`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/Category), [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.category_lib.Category`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/Category), [`mp.tasks.vision.drawing_styles.face_landmarker.category_lib.Category`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/Category), [`mp.tasks.vision.drawing_styles.hand_landmarker.category.Category`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/Category), [`mp.tasks.vision.drawing_utils.detections_module.category_lib.Category`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/Category), [`mp.tasks.vision.drawing_utils.face_landmarker.category_lib.Category`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/Category), [`mp.tasks.vision.gesture_recognizer_result.category_module.Category`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/Category)
    
    
    mp.tasks.components.containers.Category(
        index: Optional[int] = None,
        score: Optional[float] = None,
        display_name: Optional[str] = None,
        category_name: Optional[str] = None
    )
    

Category is a util class, contains a label, its display name, a float value as score, and the index of the label in the corresponding label file. Typically it's used as the result of classification tasks. | 

## Attributes  
  
---  
  
`index` |  The index of the label in the corresponding label file.   
`score` |  The probability score of this label category.   
`display_name` |  The display name of the label, which may be translated for different locales. For example, a label, "apple", may be translated into Spanish for display purpose, so that the `display_name` is "manzana".   
`category_name` |  The label of this category object.   
  
## Methods

### `__eq__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/category.py#L70-L86)
    
    
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
  
category_name |  `None`  
display_name |  `None`  
index |  `None`  
score |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
