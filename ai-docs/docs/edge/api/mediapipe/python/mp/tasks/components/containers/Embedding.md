---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Embedding/
title: mp.tasks.components.containers.Embedding \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:10.455828+00:00
---

# mp.tasks.components.containers.Embedding  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Embedding/




#  mp.tasks.components.containers.Embedding

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/embedding_result.py#L25-L39) Embedding result for a given embedder head.

#### View aliases

**Main aliases** [`mp.tasks.components.utils.cosine_similarity.embedding_result.Embedding`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/components/containers/Embedding)
    
    
    mp.tasks.components.containers.Embedding(
        embedding: np.ndarray,
        head_index: Optional[int] = None,
        head_name: Optional[str] = None
    )
    

| 

## Attributes  
  
---  
  
`embedding` |  The actual embedding, either floating-point or scalar-quantized.   
`head_index` |  The index of the embedder head that produced this embedding. This is useful for multi-head models.   
`head_name` |  The name of the embedder head, which is the corresponding tensor metadata name (if any). This is useful for multi-head models.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
head_index |  `None`  
head_name |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
