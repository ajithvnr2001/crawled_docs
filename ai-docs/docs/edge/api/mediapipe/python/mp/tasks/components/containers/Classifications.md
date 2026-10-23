---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Classifications/
title: mp.tasks.components.containers.Classifications \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:09.346199+00:00
---

# mp.tasks.components.containers.Classifications  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Classifications/




#  mp.tasks.components.containers.Classifications

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/classification_result.py#L24-L61) Represents the classification results for a given classifier head.
    
    
    mp.tasks.components.containers.Classifications(
        categories: List[[mp.tasks.components.containers.Category](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Category)],
        head_index: int,
        head_name: Optional[str] = None
    )
    

| 

## Attributes  
  
---  
  
`categories` |  The array of predicted categories, usually sorted by descending scores (e.g. from high to low probability).   
`head_index` |  The index of the classifier head these categories refer to. This is useful for multi-head models.   
`head_name` |  The name of the classifier head, which is the corresponding tensor metadata name.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
head_name |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
