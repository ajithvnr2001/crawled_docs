---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetector/
title: mp.tasks.vision.FaceDetector \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:32.433661+00:00
---

# mp.tasks.vision.FaceDetector  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetector/




#  mp.tasks.vision.FaceDetector

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L164-L445) Class that performs face detection on images.
    
    
    mp.tasks.vision.FaceDetector(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p,
        dispatcher: [mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher),
        async_callback: _C_TYPES_RESULT_CALLBACK
    )
    

| 

## Args  
  
---  
  
`lib` |  The dispatch library to use for the face detector.   
`handle` |  The C pointer to the face detector.   
`dispatcher` |  The async result handler for the face detector.   
`async_callback` |  The c callback for the face detector.   
  
## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L417-L424)
    
    
    close()
    

Shuts down the MediaPipe task instance.

### `create_from_model_path`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L192-L215)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'FaceDetector'
    

Creates an `FaceDetector` object from a TensorFlow Lite model and the default `FaceDetectorOptions`.

Note that the created `FaceDetector` instance is in image mode, for detecting faces on single image inputs.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`FaceDetector` object that's created from the model file and the default `FaceDetectorOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `FaceDetector` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L217-L273)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.vision.FaceDetectorOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions)
    ) -> 'FaceDetector'
    

Creates the `FaceDetector` object from face detector options.

Args  
---  
  
`options` |  Options for the face detector task.   
  
Returns  
---  
`FaceDetector` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `FaceDetector` object from `FaceDetectorOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `detect`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L275-L316)
    
    
    detect(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.vision.FaceDetectorResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult)
    

Performs face detection on the provided MediaPipe Image.

Only use this method when the FaceDetector is created with the image running mode.

Args  
---  
  
`image` |  MediaPipe Image.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
A face detection result object that contains a list of face detections, each detection has a bounding box that is expressed in the unrotated input frame of reference coordinates system, i.e. in `[0,image_width) x [0, image_height)`, which are the dimensions of the underlying image data.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If face detection failed to run.   
  
### `detect_async`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L366-L415)
    
    
    detect_async(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> None
    

Sends live image data (an Image with a unique timestamp) to perform face detection.

Only use this method when the FaceDetector is created with the live stream running mode. The input timestamps should be monotonically increasing for adjacent calls of this method. This method will return immediately after the input image is accepted. The results will be available via the `result_callback` provided in the `FaceDetectorOptions`. The `detect_async` method is designed to process live stream data such as camera input. To lower the overall latency, face detector may drop the input images if needed. In other words, it's not guaranteed to have output per input image.

The `result_callback` provides:

  * A face detection result object that contains a list of face detections, each detection has a bounding box that is expressed in the unrotated input frame of reference coordinates system, i.e. in `[0,image_width) x [0,image_height)`, which are the dimensions of the underlying image data.
  * The input image that the face detector runs on.
  * The input timestamp in milliseconds.



Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input image in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Raises  
---  
  
`ValueError` |  If the current input timestamp is smaller than what the face detector has already processed.   
`RuntimeError` |  If face detection failed to initialize.   
  
### `detect_for_video`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L318-L364)
    
    
    detect_for_video(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.vision.FaceDetectorResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult)
    

Performs face detection on the provided video frames.

Only use this method when the FaceDetector is created with the video running mode. It's required to provide the video frame's timestamp (in milliseconds) along with the video frame. The input timestamps should be monotonically increasing for adjacent calls of this method.

Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input video frame in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
A face detection result object that contains a list of face detections, each detection has a bounding box that is expressed in the unrotated input frame of reference coordinates system, i.e. in `[0,image_width) x [0, image_height)`, which are the dimensions of the underlying image data.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If face detection failed to run.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L426-L428)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L430-L442)
    
    
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
  
`RuntimeError` |  If the MediaPipe FaceDetector task failed to close.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
