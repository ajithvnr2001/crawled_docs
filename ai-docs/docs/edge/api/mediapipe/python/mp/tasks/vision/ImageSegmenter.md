---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageSegmenter/
title: mp.tasks.vision.ImageSegmenter \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:40.319849+00:00
---

# mp.tasks.vision.ImageSegmenter  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageSegmenter/




#  mp.tasks.vision.ImageSegmenter

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_segmenter.py#L224-L544) Class that performs image segmentation on images.
    
    
    mp.tasks.vision.ImageSegmenter(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p,
        dispatcher: [mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher),
        async_callback: _C_TYPES_RESULT_CALLBACK
    ) -> None
    

The API expects a TFLite model with mandatory TFLite Model Metadata. | 

## Input tensor  
  
---  
(kTfLiteUInt8/kTfLiteFloat32) 

  * image input of size `[batch x height x width x channels]`.
  * batch inference is not supported (`batch` is required to be 1).
  * RGB and greyscale inputs are supported (`channels` is required to be 1 or 3).
  * if type is kTfLiteFloat32, NormalizationOptions are required to be attached to the metadata for input normalization. 

  
  
## Output tensors  
  
---  
(kTfLiteUInt8/kTfLiteFloat32) 

  * list of segmented masks.
  * if `output_category_mask` is True, uint8 Image, Image vector of size 1.
  * if `output_confidence_masks` is True, float32 Image list of size `channels`.
  * batch is always 1 

  
  
An example of such model can be found at: <https://tfhub.dev/tensorflow/lite-model/deeplabv3/1/metadata/2>

## Args  
  
---  
  
`lib` |  The dispatch library to use for the image segmenter.   
`handle` |  The C pointer to the image segmenter.   
`dispatcher` |  The async result handler for the image segmenter.   
`async_callback` |  The c callback for the image segmenter.   
  
## Attributes  
  
---  
  
`labels` |  Get the category label list the ImageSegmenter can recognize. For CATEGORY_MASK type, the index in the category mask corresponds to the category in the label list. For CONFIDENCE_MASK type, the output mask list at index corresponds to the category in the label list. If there is no label map provided in the model file, empty label list is returned.   
  
## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_segmenter.py#L515-L522)
    
    
    close()
    

Closes ImageSegmenter.

### `create_from_model_path`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_segmenter.py#L275-L298)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'ImageSegmenter'
    

Creates an `ImageSegmenter` object from a TensorFlow Lite model and the default `ImageSegmenterOptions`.

Note that the created `ImageSegmenter` instance is in image mode, for performing image segmentation on single image inputs.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`ImageSegmenter` object that's created from the model file and the default `ImageSegmenterOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `ImageSegmenter` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_segmenter.py#L300-L355)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.vision.ImageSegmenterOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageSegmenterOptions)
    ) -> 'ImageSegmenter'
    

Creates the `ImageSegmenter` object from image segmenter options.

Args  
---  
  
`options` |  Options for the image segmenter task.   
  
Returns  
---  
`ImageSegmenter` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `ImageSegmenter` object from `ImageSegmenterOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `segment`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_segmenter.py#L357-L394)
    
    
    segment(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> ImageSegmenterResult
    

Performs the actual segmentation task on the provided MediaPipe Image.

Args  
---  
  
`image` |  MediaPipe Image.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
If the output_type is CATEGORY_MASK, the returned vector of images is per-category segmented image mask. If the output_type is CONFIDENCE_MASK, the returned vector of images contains only one confidence image mask. A segmentation result object that contains a list of segmentation masks as images.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If image segmentation failed to run.   
  
### `segment_async`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_segmenter.py#L443-L487)
    
    
    segment_async(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> None
    

Sends live image data (an Image with a unique timestamp) to perform image segmentation.

Only use this method when the ImageSegmenter is created with the live stream running mode. The input timestamps should be monotonically increasing for adjacent calls of this method. This method will return immediately after the input image is accepted. The results will be available via the `result_callback` provided in the `ImageSegmenterOptions`. The `segment_async` method is designed to process live stream data such as camera input. To lower the overall latency, image segmenter may drop the input images if needed. In other words, it's not guaranteed to have output per input image.

The `result_callback` prvoides:

  * A segmentation result object that contains a list of segmentation masks as images.
  * The input image that the image segmenter runs on.
  * The input timestamp in milliseconds.



Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input image in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Raises  
---  
  
`ValueError` |  If the current input timestamp is smaller than what the image segmenter has already processed.   
  
### `segment_for_video`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_segmenter.py#L396-L441)
    
    
    segment_for_video(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> ImageSegmenterResult
    

Performs segmentation on the provided video frames.

Only use this method when the ImageSegmenter is created with the video running mode. It's required to provide the video frame's timestamp (in milliseconds) along with the video frame. The input timestamps should be monotonically increasing for adjacent calls of this method.

Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input video frame in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
If the output_type is CATEGORY_MASK, the returned vector of images is per-category segmented image mask. If the output_type is CONFIDENCE_MASK, the returned vector of images contains only one confidence image mask. A segmentation result object that contains a list of segmentation masks as images.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If image segmentation failed to run.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_segmenter.py#L524-L526)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_segmenter.py#L528-L541)
    
    
    __exit__(
        exc_type, exc_value, traceback
    )
    

Closes ImageSegmenters and exits the context manager.

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
