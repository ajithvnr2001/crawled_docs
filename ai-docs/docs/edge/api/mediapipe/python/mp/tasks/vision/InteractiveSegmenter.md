---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/InteractiveSegmenter/
title: mp.tasks.vision.InteractiveSegmenter \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:40.492910+00:00
---

# mp.tasks.vision.InteractiveSegmenter  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/InteractiveSegmenter/




#  mp.tasks.vision.InteractiveSegmenter

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/interactive_segmenter.py#L185-L344) Class that performs interactive segmentation on images.
    
    
    mp.tasks.vision.InteractiveSegmenter(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p,
        dispatcher: [mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher)
    )
    

Users can represent user interaction through `RegionOfInterest`, which gives a hint to InteractiveSegmenter to perform segmentation focusing on the given region of interest. The API expects a TFLite model with mandatory TFLite Model Metadata. | 

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
  * if `output_type` is CATEGORY_MASK, uint8 Image, Image vector of size 1.
  * if `output_type` is CONFIDENCE_MASK, float32 Image list of size `channels`.
  * batch is always 1 

  
  
An example of such model can be found at: <https://tfhub.dev/tensorflow/lite-model/deeplabv3/1/metadata/2>

## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/interactive_segmenter.py#L325-L332)
    
    
    close()
    

Closes the InteractiveSegmenter.

### `create_from_model_path`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/interactive_segmenter.py#L229-L250)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'InteractiveSegmenter'
    

Creates an `InteractiveSegmenter` object from a TensorFlow Lite model and the default `InteractiveSegmenterOptions`.

Note that the created `InteractiveSegmenter` instance is in image mode, for performing image segmentation on single image inputs.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`InteractiveSegmenter` object that's created from the model file and the default `InteractiveSegmenterOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `InteractiveSegmenter` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/interactive_segmenter.py#L252-L277)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.vision.InteractiveSegmenterOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/InteractiveSegmenterOptions)
    ) -> 'InteractiveSegmenter'
    

Creates the `InteractiveSegmenter` object from interactive segmenter options.

Args  
---  
  
`options` |  Options for the interactive segmenter task.   
  
Returns  
---  
`InteractiveSegmenter` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `InteractiveSegmenter` object from `InteractiveSegmenterOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `segment`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/interactive_segmenter.py#L279-L323)
    
    
    segment(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        roi: [mp.tasks.vision.InteractiveSegmenterRegionOfInterest](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/InteractiveSegmenterRegionOfInterest),
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> InteractiveSegmenterResult
    

Performs the actual segmentation task on the provided MediaPipe Image.

The image can be of any size with format RGB.

Args  
---  
  
`image` |  MediaPipe Image.   
`roi` |  Optional user-specified region of interest for segmentation.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
If the output_type is CATEGORY_MASK, the returned vector of images is per-category segmented image mask. If the output_type is CONFIDENCE_MASK, the returned vector of images contains only one confidence image mask. A segmentation result object that contains a list of segmentation masks as images.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If image segmentation failed to run.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/interactive_segmenter.py#L334-L336)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/interactive_segmenter.py#L338-L341)
    
    
    __exit__(
        exc_type, exc_value, traceback
    )
    

Shuts down the MediaPipe task instance on exit of the context manager.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
