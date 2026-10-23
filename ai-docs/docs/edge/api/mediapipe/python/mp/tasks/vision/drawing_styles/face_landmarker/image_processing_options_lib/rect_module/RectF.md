---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/image_processing_options_lib/rect_module/RectF/
title: mp.tasks.vision.drawing_styles.face_landmarker.image_processing_options_lib.rect_module.RectF \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:51.022778+00:00
---

# mp.tasks.vision.drawing_styles.face_landmarker.image_processing_options_lib.rect_module.RectF  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/image_processing_options_lib/rect_module/RectF/




#  mp.tasks.vision.drawing_styles.face_landmarker.image_processing_options_lib.rect_module.RectF

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/rect.py#L49-L74) A rectangle, used as part as input region-of-interest.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.image_processing_options_lib.rect_module.RectF`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/image_processing_options_lib/rect_module/RectF), [`mp.tasks.vision.drawing_styles.hand_landmarker.image_processing_options_lib.rect_module.RectF`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/image_processing_options_lib/rect_module/RectF), [`mp.tasks.vision.drawing_styles.pose_landmarker.image_processing_options_lib.rect_module.RectF`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/image_processing_options_lib/rect_module/RectF), [`mp.tasks.vision.drawing_utils.face_landmarker.image_processing_options_lib.rect_module.RectF`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/image_processing_options_lib/rect_module/RectF)
    
    
    mp.tasks.vision.drawing_styles.face_landmarker.image_processing_options_lib.rect_module.RectF(
        left: float, top: float, bottom: float, right: float
    )
    

The coordinates are normalized wrt the image dimensions, i.e. generally in [0,1] but they may exceed these bounds if describing a region overlapping the image. The origin is on the top-left corner of the image. | 

## Attributes  
  
---  
  
`left` |  The X coordinate of the left side of the rectangle.   
`top` |  The Y coordinate of the top of the rectangle.   
`bottom` |  The Y coordinate of the bottom of the rectangle.   
`right` |  The X coordinate of the right side of the rectangle.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
