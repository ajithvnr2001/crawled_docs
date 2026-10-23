---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextEmbedder/
title: mp.tasks.text.TextEmbedder \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:29.730672+00:00
---

# mp.tasks.text.TextEmbedder  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextEmbedder/




#  mp.tasks.text.TextEmbedder

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L112-L260) Class that performs embedding extraction on text.
    
    
    mp.tasks.text.TextEmbedder(
        lib: [mp.tasks.vision.drawing_styles.face_landmarker.serial_dispatcher.SerialDispatcher](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/serial_dispatcher/SerialDispatcher),
        handle: ctypes.c_void_p
    )
    

This API expects a TFLite model with TFLite Model Metadata that contains the mandatory (described below) input tensors and output tensors. Metadata should contain the input process unit for the model's Tokenizer as well as input / output tensor metadata. | 

## Input tensors  
  
---  
(kTfLiteInt32) 

  * 3 input tensors of size `[batch_size x bert_max_seq_len]` with names "ids", "mask", and "segment_ids" representing the input ids, mask ids, and segment ids respectively.
  * or 1 input tensor of size `[batch_size x max_seq_len]` representing the input ids. 

  
  
At least one output tensor with: (kTfLiteFloat32)

  * `N` components corresponding to the `N` dimensions of the returned feature vector for this output layer.
  * Either 2 or 4 dimensions, i.e. `[1 x N]` or `[1 x 1 x 1 x N]`.



## Methods

### `close`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L244-L249)
    
    
    close()
    

Shuts down the MediaPipe task instance.

### `cosine_similarity`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L218-L242)
    
    
    @classmethod
    cosine_similarity(
        u: [mp.tasks.components.containers.Embedding](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Embedding),
        v: [mp.tasks.components.containers.Embedding](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Embedding)
    ) -> float
    

Utility function to compute cosine similarity between two embedding entries.

May return an InvalidArgumentError if e.g. the feature vectors are of different types (quantized vs. float), have different sizes, or have a an L2-norm of 0.

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

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L145-L163)
    
    
    @classmethod
    create_from_model_path(
        model_path: str
    ) -> 'TextEmbedder'
    

Creates an `TextEmbedder` object from a TensorFlow Lite model and the default `TextEmbedderOptions`.

Args  
---  
  
`model_path` |  Path to the model.   
  
Returns  
---  
`TextEmbedder` object that's created from the model file and the default `TextEmbedderOptions`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `TextEmbedder` object from the provided file such as invalid file path.   
`RuntimeError` |  If other types of error occurred.   
  
### `create_from_options`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L165-L186)
    
    
    @classmethod
    create_from_options(
        options: [mp.tasks.text.TextEmbedderOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextEmbedderOptions)
    ) -> 'TextEmbedder'
    

Creates the `TextEmbedder` object from text embedder options.

Args  
---  
  
`options` |  Options for the text embedder task.   
  
Returns  
---  
`TextEmbedder` object that's created from `options`.   
  
Raises  
---  
  
`ValueError` |  If failed to create `TextEmbedder` object from `TextEmbedderOptions` such as missing the model.   
`RuntimeError` |  If other types of error occurred.   
  
### `embed`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L188-L216)
    
    
    embed(
        text: str
    ) -> [mp.tasks.text.TextEmbedderResult](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextEmbedderResult)
    

Performs text embedding extraction on the provided text.

Args  
---  
  
[`text`](https://www.tensorflow.org/text/api_docs/python/text) |  The input text.   
  
Returns  
---  
An embedding result object that contains a list of embeddings.   
  
Raises  
---  
  
`ValueError` |  If any of the input arguments is invalid.   
`RuntimeError` |  If text embedder failed to run.   
  
### `__enter__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L251-L253)
    
    
    __enter__()
    

Returns `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L255-L257)
    
    
    __exit__(
        unused_exc_type, unused_exc_value, unused_traceback
    )
    

Shuts down the MediaPipe task instance on exit of the context manager.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
