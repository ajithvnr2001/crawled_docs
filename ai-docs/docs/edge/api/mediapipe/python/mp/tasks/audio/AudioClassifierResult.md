---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/audio/AudioClassifierResult/
title: mp.tasks.audio.AudioClassifierResult \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:07.064988+00:00
---

# mp.tasks.audio.AudioClassifierResult  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/audio/AudioClassifierResult/




#  mp.tasks.audio.AudioClassifierResult

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/classification_result.py#L64-L99) Contains the classification results of a model.

#### View aliases

**Main aliases** [`mp.tasks.components.containers.ClassificationResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/audio/AudioClassifierResult), [`mp.tasks.text.TextClassifierResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/audio/AudioClassifierResult), [`mp.tasks.vision.ImageClassifierResult`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/audio/AudioClassifierResult)
    
    
    mp.tasks.audio.AudioClassifierResult(
        classifications: List[[mp.tasks.components.containers.Classifications](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Classifications)],
        timestamp_ms: Optional[int] = None
    )
    

| 

## Attributes  
  
---  
  
`classifications` |  A list of `Classifications` objects, each for a head of the model.   
`timestamp_ms` |  The optional timestamp (in milliseconds) of the start of the chunk of data corresponding to these results. This is only used for classification on time series (e.g. audio classification). In these use cases, the amount of data to process might exceed the maximum size that the model can process: to solve this, the input data is split into multiple chunks starting at different timestamps.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
timestamp_ms |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
