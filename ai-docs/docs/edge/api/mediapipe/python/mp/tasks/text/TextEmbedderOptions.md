---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextEmbedderOptions/
title: mp.tasks.text.TextEmbedderOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:30.258664+00:00
---

# mp.tasks.text.TextEmbedderOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextEmbedderOptions/




#  mp.tasks.text.TextEmbedderOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L79-L109) Options for the text embedder task.
    
    
    mp.tasks.text.TextEmbedderOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        l2_normalize: Optional[bool] = None,
        quantize: Optional[bool] = None
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the text embedder task.   
`l2_normalize` |  Whether to normalize the returned feature vector with L2 norm. Use this option only if the model does not already contain a native L2_NORMALIZATION TF Lite Op. In most cases, this is already the case and L2 norm is thus achieved through TF Lite inference.   
`quantize` |  Whether the returned embedding should be quantized to bytes via scalar quantization. Embeddings are implicitly assumed to be unit-norm and therefore any dimension is guaranteed to have a value in [-1.0, 1.0]. Use the l2_normalize option if this is not the case.   
  
## Methods

### `to_ctypes`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_embedder.py#L98-L109)
    
    
    to_ctypes() -> _TextEmbedderOptionsC
    

Generates a ctypes TextEmbedderOptionsC object.

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
l2_normalize |  `None`  
quantize |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
