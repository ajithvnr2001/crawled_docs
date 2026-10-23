---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions/
title: mp.tasks.vision.ImageProcessingOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:39.835891+00:00
---

# mp.tasks.vision.ImageProcessingOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions/




#  mp.tasks.vision.ImageProcessingOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image_processing_options.py#L25-L57) Options for image processing.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.image_processing_options_lib.ImageProcessingOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions), [`mp.tasks.vision.drawing_styles.face_landmarker.image_processing_options_lib.ImageProcessingOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions), [`mp.tasks.vision.drawing_styles.hand_landmarker.image_processing_options_lib.ImageProcessingOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions), [`mp.tasks.vision.drawing_styles.pose_landmarker.image_processing_options_lib.ImageProcessingOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions), [`mp.tasks.vision.drawing_utils.face_landmarker.image_processing_options_lib.ImageProcessingOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)
    
    
    mp.tasks.vision.ImageProcessingOptions(
        region_of_interest: Optional[[mp.tasks.vision.drawing_styles.face_landmarker.image_processing_options_lib.rect_module.RectF](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/image_processing_options_lib/rect_module/RectF)] = None,
        rotation_degrees: int = 0
    )
    

If both region-of-interest and rotation are specified, the crop around the region-of-interest is extracted first, then the specified rotation is applied to the crop. | 

## Attributes  
  
---  
  
`region_of_interest` |  The optional region-of-interest to crop from the image. If not specified, the full image is used. Coordinates must be in [0,1] with 'left' < 'right' and 'top' < 'bottom'.   
`rotation_degrees` |  The rotation to apply to the image (or cropped region-of-interest), in degrees clockwise. The rotation must be a multiple (positive or negative) of 90°.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
region_of_interest |  `None`  
rotation_degrees |  `0`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
