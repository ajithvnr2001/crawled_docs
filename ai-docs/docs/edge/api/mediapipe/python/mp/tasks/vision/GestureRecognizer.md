---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizer/
title: mp.tasks.vision.GestureRecognizer \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:34.699043+00:00
---

# mp.tasks.vision.GestureRecognizer  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizer/




#  mp.tasks.vision.GestureRecognizer

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L204-L493) Class that performs gesture recognition on images.
    
    
    mp.tasks.vision.GestureRecognizer(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p,
        dispatcher: [mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher),
        async_callback: _C_TYPES_RESULT_CALLBACK
    )
    

| 

## Args  
  
---  
  
`lib` |  The dispatch library to use for the gesture recognizer.   
`handle` |  The C pointer to the gesture recognizer.   
`dispatcher` |  The async result handler for the gesture recognizer.   
`async_callback` |  The c callback for the gesture recognizer.   
  
## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L464-L471)
    
    
    close()
    

Closes GestureRecognizer.

### `create_from_model_path`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L232-L255)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'GestureRecognizer'
    

Creates an `GestureRecognizer` object from a TensorFlow Lite model and the default `GestureRecognizerOptions`.

Note that the created `GestureRecognizer` instance is in image mode, for recognizing hand gestures on single image inputs.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`GestureRecognizer` object that's created from the model file and the default `GestureRecognizerOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `GestureRecognizer` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L257-L323)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.vision.GestureRecognizerOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizerOptions)
    ) -> 'GestureRecognizer'
    

Creates the `GestureRecognizer` object from gesture recognizer options.

Args  
---  
  
`options` |  Options for the gesture recognizer task.   
  
Returns  
---  
`GestureRecognizer` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `GestureRecognizer` object from `GestureRecognizerOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `recognize`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L325-L366)
    
    
    recognize(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.vision.GestureRecognizerResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizerResult)
    

Performs hand gesture recognition on the given image.

Only use this method when the GestureRecognizer is created with the image running mode.

The image can be of any size with format RGB or RGBA.

support is implemented.

Args  
---  
  
`image` |  MediaPipe Image.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
The hand gesture recognition results.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If gesture recognition failed to run.   
  
### `recognize_async`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L415-L462)
    
    
    recognize_async(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> None
    

Sends live image data to perform gesture recognition.

The results will be available via the "result_callback" provided in the GestureRecognizerOptions. Only use this method when the GestureRecognizer is created with the live stream running mode.

Only use this method when the GestureRecognizer is created with the live stream running mode. The input timestamps should be monotonically increasing for adjacent calls of this method. This method will return immediately after the input image is accepted. The results will be available via the `result_callback` provided in the `GestureRecognizerOptions`. The `recognize_async` method is designed to process live stream data such as camera input. To lower the overall latency, gesture recognizer may drop the input images if needed. In other words, it's not guaranteed to have output per input image.

The `result_callback` provides:

  * The hand gesture recognition results.
  * The input image that the gesture recognizer runs on.
  * The input timestamp in milliseconds.



Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input image in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Raises  
---  
  
`ValueError` |  If the current input timestamp is smaller than what the gesture recognizer has already processed.   
  
### `recognize_for_video`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L368-L413)
    
    
    recognize_for_video(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.vision.GestureRecognizerResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizerResult)
    

Performs gesture recognition on the provided video frame.

Only use this method when the GestureRecognizer is created with the video running mode.

Only use this method when the GestureRecognizer is created with the video running mode. It's required to provide the video frame's timestamp (in milliseconds) along with the video frame. The input timestamps should be monotonically increasing for adjacent calls of this method.

Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input video frame in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
The hand gesture recognition results.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If gesture recognition failed to run.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L473-L475)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L477-L490)
    
    
    __exit__(
        exc_type, exc_value, traceback
    )
    

Closes GestureRecognizers and exits the context manager.

Args  
---  
  
`exc_type` |  The exception type that caused the context manager to exit.   
`exc_value` |  The exception value that caused the context manager to exit.   
`traceback` |  The exception traceback that caused the context manager to exit.   
  
Raises  
---  
  
`RuntimeError` |  If the MediaPipe Gesture Recognizer task failed to close.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
