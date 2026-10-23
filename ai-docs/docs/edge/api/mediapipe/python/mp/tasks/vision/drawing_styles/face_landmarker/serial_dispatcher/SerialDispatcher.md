---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher/
title: mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:59.175748+00:00
---

# mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher/




#  mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/serial_dispatcher.py#L25-L91) A wrapper class for a ctypes.CDLL object that serializes all calls.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.image_lib.mediapipe_c_bindings.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.mediapipe_c_bindings_lib.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.face_landmarker.image_lib.mediapipe_c_bindings.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_bindings_lib.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.hand_landmarker.image_lib.mediapipe_c_bindings.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.hand_landmarker.mediapipe_c_bindings.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.hand_landmarker.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.pose_landmarker.image_lib.mediapipe_c_bindings.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.pose_landmarker.mediapipe_c_bindings_lib.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_styles.pose_landmarker.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_utils.face_landmarker.image_lib.mediapipe_c_bindings.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_utils.face_landmarker.mediapipe_c_bindings_lib.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher), [`mp.tasks.vision.drawing_utils.face_landmarker.serial_dispatcher.SerialDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher)
    
    
    mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher(
        lib: ctypes.CDLL,
        signatures: Sequence[[mp.tasks.vision.drawing_styles.face_landmarker.mediapipe_c_utils.CFunction](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/mediapipe_c_utils/CFunction)]
    )
    

This ensures that functions from a non-thread-safe C library are called sequentially from a single dedicated thread, preventing race conditions and segmentation faults. If a function is a CStatusFunction, the dispatcher will raise a Python exception if the returned MpStatus code is not kMpOk. | 

## Args  
  
---  
  
`lib` |  The ctypes.CDLL object to wrap.   
`signatures` |  the CFunction objects specifying the functions to wrap.   
  
## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/serial_dispatcher.py#L78-L84)
    
    
    close()
    

Shuts down the dispatcher and waits for pending tasks to complete.

### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/serial_dispatcher.py#L86-L87)
    
    
    __enter__()
    

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/serial_dispatcher.py#L89-L91)
    
    
    __exit__(
        exc_type, exc_val, exc_tb
    )
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
