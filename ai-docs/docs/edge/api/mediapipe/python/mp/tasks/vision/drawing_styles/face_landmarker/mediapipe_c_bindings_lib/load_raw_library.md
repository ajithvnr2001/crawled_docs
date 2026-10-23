---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library/
title: mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_bindings_lib.load_raw_library \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:52.066040+00:00
---

# mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_bindings_lib.load_raw_library  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library/




#  mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_bindings_lib.load_raw_library

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/mediapipe_c_bindings.py#L30-L65) Loads the raw ctypes.CDLL shared library and registers signatures.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.image_lib.mediapipe_c_bindings.load_raw_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library), [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.mediapipe_c_bindings_lib.load_raw_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library), [`mp.tasks.vision.drawing_styles.face_landmarker.image_lib.mediapipe_c_bindings.load_raw_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library), [`mp.tasks.vision.drawing_styles.hand_landmarker.image_lib.mediapipe_c_bindings.load_raw_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library), [`mp.tasks.vision.drawing_styles.hand_landmarker.mediapipe_c_bindings.load_raw_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library), [`mp.tasks.vision.drawing_styles.pose_landmarker.image_lib.mediapipe_c_bindings.load_raw_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library), [`mp.tasks.vision.drawing_styles.pose_landmarker.mediapipe_c_bindings_lib.load_raw_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library), [`mp.tasks.vision.drawing_utils.face_landmarker.image_lib.mediapipe_c_bindings.load_raw_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library), [`mp.tasks.vision.drawing_utils.face_landmarker.mediapipe_c_bindings_lib.load_raw_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_raw_library)
    
    
    mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_bindings_lib.load_raw_library(
        signatures: Sequence[[mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_utils.CFunction](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_utils/CFunction)] = ()
    ) -> ctypes.CDLL
    

This function loads the raw ctypes.CDLL shared library if it hasn't been loaded yet, otherwise it re-uses the existing instance. It attaches the provided signatures and makes them available across all callsites. | 

## Args  
  
---  
  
`signatures` |  The ctypes function signatures to register in the library.   
  
## Returns  
  
---  
The ctypes shared library.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
