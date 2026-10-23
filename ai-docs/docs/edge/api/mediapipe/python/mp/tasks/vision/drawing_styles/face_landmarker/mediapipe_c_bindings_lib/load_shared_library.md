---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library/
title: mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_bindings_lib.load_shared_library \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:52.699366+00:00
---

# mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_bindings_lib.load_shared_library  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library/




#  mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_bindings_lib.load_shared_library

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/mediapipe_c_bindings.py#L68-L84) Loads the shared library in a SerialDispatcher and registers signatures.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.image_lib.mediapipe_c_bindings.load_shared_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library), [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.mediapipe_c_bindings_lib.load_shared_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library), [`mp.tasks.vision.drawing_styles.face_landmarker.image_lib.mediapipe_c_bindings.load_shared_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library), [`mp.tasks.vision.drawing_styles.hand_landmarker.image_lib.mediapipe_c_bindings.load_shared_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library), [`mp.tasks.vision.drawing_styles.hand_landmarker.mediapipe_c_bindings.load_shared_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library), [`mp.tasks.vision.drawing_styles.pose_landmarker.image_lib.mediapipe_c_bindings.load_shared_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library), [`mp.tasks.vision.drawing_styles.pose_landmarker.mediapipe_c_bindings_lib.load_shared_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library), [`mp.tasks.vision.drawing_utils.face_landmarker.image_lib.mediapipe_c_bindings.load_shared_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library), [`mp.tasks.vision.drawing_utils.face_landmarker.mediapipe_c_bindings_lib.load_shared_library`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_bindings_lib/load_shared_library)
    
    
    mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_bindings_lib.load_shared_library(
        signatures: Sequence[[mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_utils.CFunction](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_utils/CFunction)] = ()
    ) -> [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher)
    

This function creates a thread-safe wrapper for the shared library that dispatches all calls through a single dedicated thread. Every call to this function uses a different dispatch library with its own thread. | 

## Args  
  
---  
  
`signatures` |  The ctypes function signatures to register in the library.   
  
## Returns  
  
---  
A thread-safe wrapper for the ctypes shared library.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
