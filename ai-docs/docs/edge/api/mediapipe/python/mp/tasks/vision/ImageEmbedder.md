---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageEmbedder/
title: mp.tasks.vision.ImageEmbedder \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:38.726739+00:00
---

# mp.tasks.vision.ImageEmbedder  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageEmbedder/




#  mp.tasks.vision.ImageEmbedder

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L198-L497) Class that performs embedding extraction on images.
    
    
    mp.tasks.vision.ImageEmbedder(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p,
        dispatcher: [mp.tasks.vision.drawing_styles.face_landmarker.async_result_dispatcher.AsyncResultDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/async_result_dispatcher/AsyncResultDispatcher)
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

  * `N` components corresponding to the `N` dimensions of the returned feature vector for this output layer.
  * Either 2 or 4 dimensions, i.e. `[1 x N]` or `[1 x 1 x 1 x N]`.



## Args  
  
---  
  
`lib` |  The dispatcher to use for all C function calls.   
`handle` |  The C pointer to the underlying image embedder.   
`dispatcher` |  The handler for async results.   
  
## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L452-L459)
    
    
    close()
    

Closes the ImageEmbedder.

### `cosine_similarity`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L461-L485)
    
    
    @classmethod
    cosine_similarity(
        u: [mp.tasks.components.containers.Embedding](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Embedding),
        v: [mp.tasks.components.containers.Embedding](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Embedding)
    ) -> float
    

Utility function to compute cosine similarity between two embedding entries.

May return an InvalidArgumentError if e.g. the feature vectors are of different types (quantized vs. float), have different sizes, or have an L2-norm of 0.

Args  
---  
  
`u` |  An embedding entry.   
`v` |  An embedding entry.   
  
Returns  
---  
The cosine similarity for the two embeddings.   
  
Raises  
---  
  
`ValueError` |  May return an error if e.g. the feature vectors are of different types (quantized vs. float), have different sizes, or have an L2-norm of 0.   
  
### `create_from_model_path`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L239-L262)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'ImageEmbedder'
    

Creates an `ImageEmbedder` object from a TensorFlow Lite model and the default `ImageEmbedderOptions`.

Note that the created `ImageEmbedder` instance is in image mode, for embedding image on single image inputs.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`ImageEmbedder` object that's created from the model file and the default `ImageEmbedderOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `ImageEmbedder` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L264-L315)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.vision.ImageEmbedderOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageEmbedderOptions)
    ) -> 'ImageEmbedder'
    

Creates the `ImageEmbedder` object from image embedder options.

Args  
---  
  
`options` |  Options for the image embedder task.   
  
Returns  
---  
`ImageEmbedder` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `ImageEmbedder` object from `ImageEmbedderOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `embed`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L317-L353)
    
    
    embed(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.text.TextEmbedderResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextEmbedderResult)
    

Performs image embedding extraction on the provided MediaPipe Image.

Extraction is performed on the region of interest specified by the `roi` argument if provided, or on the entire image otherwise.

Args  
---  
  
`image` |  MediaPipe Image.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
An embedding result object that contains a list of embeddings.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If image embedder failed to run.   
  
### `embed_async`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L402-L450)
    
    
    embed_async(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> None
    

Sends live image data to embedder.

The results will be available via the "result_callback" provided in the ImageEmbedderOptions. Embedding extraction is performed on the region of interested specified by the `roi` argument if provided, or on the entire image otherwise.

Only use this method when the ImageEmbedder is created with the live stream running mode. The input timestamps should be monotonically increasing for adjacent calls of this method. This method will return immediately after the input image is accepted. The results will be available via the `result_callback` provided in the `ImageEmbedderOptions`. The `embed_async` method is designed to process live stream data such as camera input. To lower the overall latency, image embedder may drop the input images if needed. In other words, it's not guaranteed to have output per input image.

The `result_callback` provides:

  * An embedding result object that contains a list of embeddings.
  * The input image that the image embedder runs on.
  * The input timestamp in milliseconds.



Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input image in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Raises  
---  
  
`ValueError` |  If the current input timestamp is smaller than what the image embedder has already processed.   
  
### `embed_for_video`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L355-L400)
    
    
    embed_for_video(
        image: [mp.Image](https://ai.google.dev/edge/api/mediapipe/python/mp/Image),
        timestamp_ms: int,
        image_processing_options: Optional[[mp.tasks.vision.ImageProcessingOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageProcessingOptions)] = None
    ) -> [mp.tasks.text.TextEmbedderResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextEmbedderResult)
    

Performs image embedding extraction on the provided video frames.

Extraction is performed on the region of interested specified by the `roi` argument if provided, or on the entire image otherwise.

Only use this method when the ImageEmbedder is created with the video running mode. It's required to provide the video frame's timestamp (in milliseconds) along with the video frame. The input timestamps should be monotonically increasing for adjacent calls of this method.

Args  
---  
  
`image` |  MediaPipe Image.   
`timestamp_ms` |  The timestamp of the input video frame in milliseconds.   
`image_processing_options` |  Options for image processing.   
  
Returns  
---  
An embedding result object that contains a list of embeddings.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If image embedder failed to run.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L487-L489)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L491-L494)
    
    
    __exit__(
        exc_type, exc_value, traceback
    )
    

Shuts down the MediaPipe task instance on exit of the context manager.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
