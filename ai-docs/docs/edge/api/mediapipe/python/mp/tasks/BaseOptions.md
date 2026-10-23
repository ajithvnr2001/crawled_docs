---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions/
title: mp.tasks.BaseOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:05.591861+00:00
---

# mp.tasks.BaseOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions/




#  mp.tasks.BaseOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/base_options.py#L59-L125) Base options for MediaPipe Tasks' Python APIs.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.base_options_lib.BaseOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/BaseOptions), [`mp.tasks.vision.drawing_styles.face_landmarker.base_options_lib.BaseOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/BaseOptions), [`mp.tasks.vision.drawing_styles.hand_landmarker.base_options_lib.BaseOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/BaseOptions), [`mp.tasks.vision.drawing_styles.pose_landmarker.base_options_lib.BaseOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/BaseOptions), [`mp.tasks.vision.drawing_utils.face_landmarker.base_options_lib.BaseOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/BaseOptions)
    
    
    mp.tasks.BaseOptions(
        model_asset_path: Optional[str] = None,
        model_asset_buffer: Optional[bytes] = None,
        delegate: Optional[[mp.tasks.BaseOptions.Delegate](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions/Delegate)] = None
    )
    

Represents external model asset used by the Task APIs. The files can be specified by one of the following two ways: (1) model asset file path in `model_asset_path`. (2) model asset contents loaded in `model_asset_buffer`. If more than one field of these fields is provided, they are used in this precedence order. | 

## Attributes  
  
---  
  
`model_asset_path` |  Path to the model asset file.   
`model_asset_buffer` |  The model asset file contents as bytes.   
`delegate` |  Acceleration to use. Supported values are GPU and CPU. GPU support is currently limited to Ubuntu platforms.   
  
## Child Classes

[`class Delegate`](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions/Delegate)

## Methods

### `__eq__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/base_options.py#L110-L125)
    
    
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
  
delegate |  `None`  
model_asset_buffer |  `None`  
model_asset_path |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
