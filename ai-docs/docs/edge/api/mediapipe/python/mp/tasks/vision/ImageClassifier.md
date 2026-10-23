---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageClassifier/
title: mp.tasks.vision.ImageClassifier \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:38.612097+00:00
---

# mp.tasks.vision.ImageClassifier  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageClassifier/




#  mp.tasks.vision.ImageClassifier

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_classifier.py#L174-L481) Class that performs image classification on images.
    
    
    mp.tasks.vision.ImageClassifier(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p,
        dispatcher: [mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher),
        async_callback: _C_TYPES_RESULT_CALLBACK
    )
    

The API expects a TFLite model with optional, but strongly recommended, TFLite Model Metadata. | 

## Input tensor  
  
---  
(kTfLiteUInt8/kTfLiteFloat32) 

  * image input of size `[batch x height x width x channels]`.
  * batch inference is not supported (`batch` is required to be 1).
  * only RGB inputs are supported (`channels` is required to be 3).
  * if type is kTfLiteFloat32, NormalizationOptions are required to be attached to the metadata for input normalization. 

  
  
At least one output tensor with: (kTfLiteUInt8/kTfLiteFloat32)

  * `N`classes and either 2 or 4 dimensions, i.e. `[1 x N]` or `[1 x 1 x 1 x N]`
  * optional (but recommended) label map(s) as AssociatedFiles with type TENSOR_AXIS_LABELS, containing one label per line. The first such AssociatedFile (if any) is used to fill the `class_name` field of the results. The `display_name` field is filled from the AssociatedFile (if any) whose locale matches the `display_names_locale` field of the `ImageClassifierOptions` used at creation time ("en" by default, i.e. English). If none of these are available, only the `index` field of the results will be filled.
  * optional score calibration can be attached using ScoreCalibrationOptions and an AssociatedFile with type TENSOR_AXIS_SCORE_CALIBRATION. See metadata_schema.fbs [1](https://github.com/google/mediapipe/blob/6cdc6443b6a7ed662744e2a2ce2d58d9c83e6d6f/mediapipe/tasks/metadata/metadata_schema.fbs#L456) for more details.



An example of such model can be found at: <https://tfhub.dev/bohemian-visual-recognition-alliance/lite-model/models/mushroom-identification_v1/1>

## Args  
  
---  
  
`lib` |  The dispatch library to use for the image classifier.   
`handle` |  The C pointer to the image classifier.   
`dispatcher` |  The async result handler for the image classifier.   
`async_callback` |  The c callback for the image classifier.   
  
## Methods

### `classify`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_classifier.py#L324-L361)
    
    
    classify(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.audio.AudioClassifierResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/audio/AudioClassifierResult)
    

Performs image classification on the provided MediaPipe Image.

Only use this method when the ImageClassifier is created with the image running mode.

Args  
---  
  
`image` |  MediaPipe Image.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
A classification result object that contains a list of classifications.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If image classification failed to run.   
  
### `classify_async`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_classifier.py#L407-L450)
    
    
    classify_async(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> None
    

Sends live image data (an Image with a unique timestamp) to perform image classification.

Only use this method when the ImageClassifier is created with the live stream running mode. The input timestamps should be monotonically increasing for adjacent calls of this method. This method will return immediately after the input image is accepted. The results will be available via the `result_callback` provided in the `ImageClassifierOptions`. The `classify_async` method is designed to process live stream data such as camera input. To lower the overall latency, image classifier may drop the input images if needed. In other words, it's not guaranteed to have output per input image.

The `result_callback` provides:

  * A classification result object that contains a list of classifications.
  * The input image that the image classifier runs on.
  * The input timestamp in milliseconds.



Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input image in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Raises  
---  
  
`ValueError` |  If the current input timestamp is smaller than what the image classifier has already processed.   
  
### `classify_for_video`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_classifier.py#L363-L405)
    
    
    classify_for_video(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.audio.AudioClassifierResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/audio/AudioClassifierResult)
    

Performs image classification on the provided video frames.

Only use this method when the ImageClassifier is created with the video running mode. It's required to provide the video frame's timestamp (in milliseconds) along with the video frame. The input timestamps should be monotonically increasing for adjacent calls of this method.

Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input video frame in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
A classification result object that contains a list of classifications.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If image classification failed to run.   
  
### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_classifier.py#L452-L459)
    
    
    close()
    

Closes ImageClassifier.

### `create_from_model_path`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_classifier.py#L235-L258)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'ImageClassifier'
    

Creates an `ImageClassifier` object from a TensorFlow Lite model and the default `ImageClassifierOptions`.

Note that the created `ImageClassifier` instance is in image mode, for classifying objects on single image inputs.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`ImageClassifier` object that's created from the model file and the default `ImageClassifierOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `ImageClassifier` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_classifier.py#L260-L322)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.vision.ImageClassifierOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageClassifierOptions)
    ) -> 'ImageClassifier'
    

Creates the `ImageClassifier` object from image classifier options.

Args  
---  
  
`options` |  Options for the image classifier task.   
  
Returns  
---  
`ImageClassifier` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `ImageClassifier` object from `ImageClassifierOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_classifier.py#L461-L463)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_classifier.py#L465-L478)
    
    
    __exit__(
        exc_type, exc_value, traceback
    )
    

Closes ImageClassifier and exits the context manager.

Args  
---  
  
`exc_type` |  The exception type that caused the context manager to exit.   
`exc_value` |  The exception value that caused the context manager to exit.   
`traceback` |  The exception traceback that caused the context manager to exit.   
  
Raises  
---  
  
`RuntimeError` |  If the MediaPipe Image Classifier task failed to close.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
