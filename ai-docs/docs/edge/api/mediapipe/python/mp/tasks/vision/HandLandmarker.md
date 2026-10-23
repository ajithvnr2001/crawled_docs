---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/HandLandmarker/
title: mp.tasks.vision.HandLandmarker \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:35.195621+00:00
---

# mp.tasks.vision.HandLandmarker  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/HandLandmarker/




#  mp.tasks.vision.HandLandmarker

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/hand_landmarker.py#L321-L603) Class that performs hand landmarks detection on images.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.hand_landmarker.HandLandmarker`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/HandLandmarker)
    
    
    mp.tasks.vision.HandLandmarker(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p,
        dispatcher: [mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher),
        async_callback: _C_TYPES_RESULT_CALLBACK
    )
    

| 

## Args  
  
---  
  
`lib` |  The dispatch library to use for the hand landmarker.   
`handle` |  The C pointer to the hand landmarker.   
`dispatcher` |  The async result handler for the hand landmarker.   
`async_callback` |  The c callback for the hand landmarker.   
  
## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/hand_landmarker.py#L576-L582)
    
    
    close()
    

Shuts down the MediaPipe task instance.

### `create_from_model_path`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/hand_landmarker.py#L349-L372)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'HandLandmarker'
    

Creates an `HandLandmarker` object from a TensorFlow Lite model and the default `HandLandmarkerOptions`.

Note that the created `HandLandmarker` instance is in image mode, for detecting hand landmarks on single image inputs.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`HandLandmarker` object that's created from the model file and the default `HandLandmarkerOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `HandLandmarker` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/hand_landmarker.py#L374-L431)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.vision.HandLandmarkerOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/HandLandmarkerOptions)
    ) -> 'HandLandmarker'
    

Creates the `HandLandmarker` object from hand landmarker options.

Args  
---  
  
`options` |  Options for the hand landmarker task.   
  
Returns  
---  
`HandLandmarker` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `HandLandmarker` object from `HandLandmarkerOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `detect`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/hand_landmarker.py#L433-L475)
    
    
    detect(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.vision.HandLandmarkerResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/HandLandmarkerResult)
    

Performs hand landmarks detection on the given image.

Only use this method when the HandLandmarker is created with the image running mode.

The image can be of any size with format RGB or RGBA.

support is implemented.

Args  
---  
  
`image` |  MediaPipe Image.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
The hand landmarks detection results.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If hand landmarker detection failed to run.   
  
### `detect_async`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/hand_landmarker.py#L525-L574)
    
    
    detect_async(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> None
    

Sends live image data to perform hand landmarks detection.

The results will be available via the "result_callback" provided in the HandLandmarkerOptions. Only use this method when the HandLandmarker is created with the live stream running mode.

Only use this method when the HandLandmarker is created with the live stream running mode. The input timestamps should be monotonically increasing for adjacent calls of this method. This method will return immediately after the input image is accepted. The results will be available via the `result_callback` provided in the `HandLandmarkerOptions`. The `detect_async` method is designed to process live stream data such as camera input. To lower the overall latency, hand landmarker may drop the input images if needed. In other words, it's not guaranteed to have output per input image.

The `result_callback` provides:

  * The hand landmarks detection results.
  * The input image that the hand landmarker runs on.
  * The input timestamp in milliseconds.



Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input image in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Raises  
---  
  
`ValueError` |  If the current input timestamp is smaller than what the hand landmarker has already processed.   
`RuntimeError` |  If hand landmarker detection failed to initialize.   
  
### `detect_for_video`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/hand_landmarker.py#L477-L523)
    
    
    detect_for_video(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.vision.HandLandmarkerResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/HandLandmarkerResult)
    

Performs hand landmarks detection on the provided video frame.

Only use this method when the HandLandmarker is created with the video running mode.

Only use this method when the HandLandmarker is created with the video running mode. It's required to provide the video frame's timestamp (in milliseconds) along with the video frame. The input timestamps should be monotonically increasing for adjacent calls of this method.

Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input video frame in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
The hand landmarks detection results.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If hand landmarker detection failed to run.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/hand_landmarker.py#L584-L586)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/hand_landmarker.py#L588-L600)
    
    
    __exit__(
        exc_type, exc_value, traceback
    )
    

Shuts down the MediaPipe task instance on exit of the context manager.

Args  
---  
  
`exc_type` |  The exception type that caused the exit.   
`exc_value` |  The exception value that caused the exit.   
`traceback` |  The exception traceback that caused the exit.   
  
Raises  
---  
  
`RuntimeError` |  If the MediaPipe HandLandmarker task failed to close.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
