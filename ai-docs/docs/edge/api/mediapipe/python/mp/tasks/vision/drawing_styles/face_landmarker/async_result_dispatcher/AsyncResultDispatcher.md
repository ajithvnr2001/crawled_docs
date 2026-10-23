---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher/
title: mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:45.981501+00:00
---

# mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher/




#  mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/async_result_dispatcher.py#L66-L232) A dispatcher to safely handle asynchronous results from a C library.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.async_result_dispatcher.AsyncResultDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher), [`mp.tasks.vision.drawing_styles.hand_landmarker.async_result_dispatcher.AsyncResultDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher), [`mp.tasks.vision.drawing_styles.pose_landmarker.async_result_dispatcher.AsyncResultDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher), [`mp.tasks.vision.drawing_utils.face_landmarker.async_result_dispatcher.AsyncResultDispatcher`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher)
    
    
    mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher(
        converter: Callable[..., Any]
    )
    

This class ensures that the user-provided Python callback is executed on a dedicated, GIL-holding Python thread, rather than directly on the C library's background thread. To use this class, you must supply a converter function that converts the C data types and then pass the Python callback you want to invoke to `wrap_callback()`, which returns a C callback that can be passed to the C library. The implementation uses OS level pipes to reduce the amount of Python code that is run without the GIL lock. The dispatcher trhead is only started when the C callback is first called. Here's an example of how to use `AsyncResultDispatcher`:
    
    
    def python_callback(result_data: MyResultType, timestamp: int):
        print(f"Received result at {timestamp}: {result_data}")
    
    def converter(c_result_ptr: ctypes.POINTER(CResult), c_timestamp: int):
        py_result = MyResultType.from_ctypes(c_result_ptr[0])
        py_timestamp = c_timestamp
        return py_result, py_timestamp
    
    dispatcher = AsyncResultDispatcher(converter=converter)
    c_callback_type = ctypes.CFUNCTYPE(
        None,  # Return type (void)
        ctypes.c_int32,  # Status code
        ctypes.POINTER(CResult), # First argument
        ctypes.c_int64 # Second argument
    )
    c_callback = dispatcher.wrap_callback(python_callback, c_callback_type)
    

| 

## Args  
  
---  
  
`converter` |  A function that takes the raw C-style arguments from the C library callback and converts them into Python-friendly types.   
  
## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/async_result_dispatcher.py#L208-L221)
    
    
    close() -> None
    

Shuts down the dispatcher thread and cleans up resources.

### `wrap_callback`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/core/async_result_dispatcher.py#L119-L164)
    
    
    wrap_callback(
        python_callback: Optional[Callable[..., None]],
        c_callback_type: type[CCallbackType]
    ) -> [mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.CCallbackType](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher#CCallbackType)
    

Returns a ctypes callback function that can be passed to a C library.

This function calls the converter function and schedules the user callback for execution with the converted data. This function can only be called once per instance.

Args  
---  
  
`python_callback` |  The user-defined result callback for processing live stream data.   
`c_callback_type` |  The ctypes callback function wrapperof the function you wish to create.   
  
Raises  
---  
  
`RuntimeError` |  If a callback has already been assigned.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
