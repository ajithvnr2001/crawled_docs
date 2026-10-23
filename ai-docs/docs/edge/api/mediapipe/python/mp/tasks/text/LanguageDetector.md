---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/LanguageDetector/
title: mp.tasks.text.LanguageDetector \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:27.660875+00:00
---

# mp.tasks.text.LanguageDetector  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/LanguageDetector/




#  mp.tasks.text.LanguageDetector

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/language_detector.py#L169-L290) Class that predicts the language of an input text.
    
    
    mp.tasks.text.LanguageDetector(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p
    )
    

This API expects a TFLite model with TFLite Model Metadata that contains the mandatory (described below) input tensors, output tensor, and the language codes in an AssociatedFile. | 

## Input tensors  
  
---  
(kTfLiteString) 

  * 1 input tensor that is scalar or has shape [1] containing the input string. 

  
  
## Output tensor  
  
---  
(kTfLiteFloat32) 

  * 1 output tensor of shape`[1 x N]` where `N` is the number of languages. 

  
  
## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/language_detector.py#L269-L275)
    
    
    close()
    

Shuts down the MediaPipe task instance.

### `create_from_model_path`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/language_detector.py#L193-L214)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'LanguageDetector'
    

Creates an `LanguageDetector` object from a TensorFlow Lite model and the default `LanguageDetectorOptions`.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`LanguageDetector` object that's created from the model file and the default `LanguageDetectorOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `LanguageDetector` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/language_detector.py#L216-L242)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.text.LanguageDetectorOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/LanguageDetectorOptions)
    ) -> 'LanguageDetector'
    

Creates the `LanguageDetector` object from language detector options.

Args  
---  
  
`options` |  Options for the language detector task.   
  
Returns  
---  
`LanguageDetector` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `LanguageDetector` object from `LanguageDetectorOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `detect`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/language_detector.py#L244-L267)
    
    
    detect(
        text: str
    ) -> [mp.tasks.text.LanguageDetectorResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/LanguageDetectorResult)
    

Predicts the language of the input [`text`](https://www.tensorflow.org/text/api_docs/python/text).

Args  
---  
  
[`text`](https://www.tensorflow.org/text/api_docs/python/text) |  The input text.   
  
Returns  
---  
A `LanguageDetectorResult` object that contains a list of languages and scores.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If language detection failed to run.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/language_detector.py#L277-L279)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/language_detector.py#L281-L287)
    
    
    __exit__(
        unused_exc_type, unused_exc_value, unused_traceback
    )
    

Shuts down the MediaPipe task instance on exit of the context manager.

Raises  
---  
  
`RuntimeError` |  If the MediaPipe LanguageDetector task failed to close.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
