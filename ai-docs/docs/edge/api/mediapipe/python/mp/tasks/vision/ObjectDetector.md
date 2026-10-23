---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ObjectDetector/
title: mp.tasks.vision.ObjectDetector \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:41.956270+00:00
---

# mp.tasks.vision.ObjectDetector  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ObjectDetector/




#  mp.tasks.vision.ObjectDetector

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L211-L538) Class that performs object detection on images.
    
    
    mp.tasks.vision.ObjectDetector(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p,
        dispatcher: [mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher),
        async_callback: _C_TYPES_RESULT_CALLBACK
    )
    

The API expects a TFLite model with mandatory TFLite Model Metadata. | 

## Input tensor  
  
---  
(kTfLiteUInt8/kTfLiteFloat32) 

  * image input of size `[batch x height x width x channels]`.
  * batch inference is not supported (`batch` is required to be 1).
  * only RGB inputs are supported (`channels` is required to be 3).
  * if type is kTfLiteFloat32, NormalizationOptions are required to be attached to the metadata for input normalization. 

  
  
Output tensors must be the 4 outputs of a `DetectionPostProcess` op, i.e: (kTfLiteFloat32)

  * locations tensor of size `[num_results x 4]`, the inner array representing bounding boxes in the form [top, left, right, bottom].
  * BoundingBoxProperties are required to be attached to the metadata and must specify type=BOUNDARIES and coordinate_type=RATIO. (kTfLiteFloat32)
  * classes tensor of size `[num_results]`, each value representing the integer index of a class.
  * optional (but recommended) label map(s) can be attached as AssociatedFile-s with type TENSOR_VALUE_LABELS, containing one label per line. The first such AssociatedFile (if any) is used to fill the `class_name` field of the results. The `display_name` field is filled from the AssociatedFile (if any) whose locale matches the `display_names_locale` field of the `ObjectDetectorOptions` used at creation time ("en" by default, i.e. English). If none of these are available, only the `index` field of the results will be filled. (kTfLiteFloat32)
  * scores tensor of size `[num_results]`, each value representing the score of the detected object.
  * optional score calibration can be attached using ScoreCalibrationOptions and an AssociatedFile with type TENSOR_AXIS_SCORE_CALIBRATION. See metadata_schema.fbs [1](https://github.com/google/mediapipe/blob/6cdc6443b6a7ed662744e2a2ce2d58d9c83e6d6f/mediapipe/tasks/metadata/metadata_schema.fbs#L456) for more details. (kTfLiteFloat32)
  * integer num_results as a tensor of size `[1]`



An example of such model can be found at: <https://tfhub.dev/google/lite-model/object_detection/mobile_object_localizer_v1/1/metadata/1>

## Args  
  
---  
  
`lib` |  The dispatch library to use for the object detector.   
`handle` |  The C pointer to the object detector.   
`dispatcher` |  The async result handler for the object detector.   
`async_callback` |  The c callback for the object detector.   
  
## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L511-L517)
    
    
    close()
    

Shuts down the MediaPipe task instance.

### `create_from_model_path`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L281-L304)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'ObjectDetector'
    

Creates an `ObjectDetector` object from a TensorFlow Lite model and the default `ObjectDetectorOptions`.

Note that the created `ObjectDetector` instance is in image mode, for detecting objects on single image inputs.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`ObjectDetector` object that's created from the model file and the default `ObjectDetectorOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `ObjectDetector` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L306-L366)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.vision.ObjectDetectorOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ObjectDetectorOptions)
    ) -> 'ObjectDetector'
    

Creates the `ObjectDetector` object from object detector options.

Args  
---  
  
`options` |  Options for the object detector task.   
  
Returns  
---  
`ObjectDetector` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `ObjectDetector` object from `ObjectDetectorOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `detect`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L369-L411)
    
    
    detect(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.vision.FaceDetectorResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult)
    

Performs object detection on the provided MediaPipe Image.

Only use this method when the ObjectDetector is created with the image running mode.

Args  
---  
  
`image` |  MediaPipe Image.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
A detection result object that contains a list of detections, each detection has a bounding box that is expressed in the unrotated input frame of reference coordinates system, i.e. in `[0,image_width) x [0, image_height)`, which are the dimensions of the underlying image data.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If object detection failed to run.   
  
### `detect_async`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L461-L509)
    
    
    detect_async(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> None
    

Sends live image data (an Image with a unique timestamp) to perform object detection.

Only use this method when the ObjectDetector is created with the live stream running mode. The input timestamps should be monotonically increasing for adjacent calls of this method. This method will return immediately after the input image is accepted. The results will be available via the `result_callback` provided in the `ObjectDetectorOptions`. The `detect_async` method is designed to process live stream data such as camera input. To lower the overall latency, object detector may drop the input images if needed. In other words, it's not guaranteed to have output per input image.

The `result_callback` prvoides:

  * A detection result object that contains a list of detections, each detection has a bounding box that is expressed in the unrotated input frame of reference coordinates system, i.e. in `[0,image_width) x [0, image_height)`, which are the dimensions of the underlying image data.
  * The input image that the object detector runs on.
  * The input timestamp in milliseconds.



Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input image in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Raises  
---  
  
`ValueError` |  If the current input timestamp is smaller than what the object detector has already processed.   
`RuntimeError` |  If object detection failed to run.   
  
### `detect_for_video`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L413-L459)
    
    
    detect_for_video(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.vision.FaceDetectorResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorResult)
    

Performs object detection on the provided video frames.

Only use this method when the ObjectDetector is created with the video running mode. It's required to provide the video frame's timestamp (in milliseconds) along with the video frame. The input timestamps should be monotonically increasing for adjacent calls of this method.

Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input video frame in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
A detection result object that contains a list of detections, each detection has a bounding box that is expressed in the unrotated input frame of reference coordinates system, i.e. in `[0,image_width) x [0, image_height)`, which are the dimensions of the underlying image data.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If object detection failed to run.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L519-L521)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L523-L535)
    
    
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
