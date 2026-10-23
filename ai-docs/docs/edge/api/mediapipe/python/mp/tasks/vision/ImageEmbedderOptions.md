---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageEmbedderOptions/
title: mp.tasks.vision.ImageEmbedderOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:38.766755+00:00
---

# mp.tasks.vision.ImageEmbedderOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ImageEmbedderOptions/




#  mp.tasks.vision.ImageEmbedderOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/image_embedder.py#L134-L195) Options for the image embedder task.
    
    
    mp.tasks.vision.ImageEmbedderOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        running_mode: [mp.tasks.vision.RunningMode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/RunningMode) = [mp.tasks.vision.FaceDetectorOptions.running_mode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions#running_mode),
        l2_normalize: Optional[bool] = None,
        quantize: Optional[bool] = None,
        result_callback: Optional[Callable[[ImageEmbedderResult, image_module.Image, int], None]] = None,
        _result_callback_c: Optional[Callable[[ctypes.c_int32, ctypes.c_void_p, ctypes.c_void_p, ctypes
            .c_int64], None]] = None
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the image embedder task.   
`running_mode` |  The running mode of the task. Default to the image mode. Image embedder task has three running modes: 1) The image mode for embedding image on single image inputs. 2) The video mode for embedding image on the decoded frames of a video. 3) The live stream mode for embedding image on a live stream of input data, such as from camera.   
`l2_normalize` |  Whether to normalize the returned feature vector with L2 norm. Use this option only if the model does not already contain a native L2_NORMALIZATION TF Lite Op. In most cases, this is already the case and L2 norm is thus achieved through TF Lite inference.   
`quantize` |  Whether the returned embedding should be quantized to bytes via scalar quantization. Embeddings are implicitly assumed to be unit-norm and therefore any dimension is guaranteed to have a value in [-1.0, 1.0]. Use the l2_normalize option if this is not the case.   
`result_callback` |  The user-defined result callback for processing live stream data. The result callback should only be specified when the running mode is set to the live stream mode.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
l2_normalize |  `None`  
quantize |  `None`  
result_callback |  `None`  
running_mode |  `<VisionTaskRunningMode.IMAGE: 'IMAGE'>`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
