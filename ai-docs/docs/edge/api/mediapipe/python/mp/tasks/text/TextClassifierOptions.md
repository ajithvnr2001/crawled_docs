---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextClassifierOptions/
title: mp.tasks.text.TextClassifierOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:29.111278+00:00
---

# mp.tasks.text.TextClassifierOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/text/TextClassifierOptions/




#  mp.tasks.text.TextClassifierOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_classifier.py#L44-L90) Options for the text classifier task.
    
    
    mp.tasks.text.TextClassifierOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        display_names_locale: Optional[str] = None,
        max_results: Optional[int] = None,
        score_threshold: Optional[float] = None,
        category_allowlist: Optional[List[str]] = None,
        category_denylist: Optional[List[str]] = None
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the text classifier task.   
`display_names_locale` |  The locale to use for display names specified through the TFLite Model Metadata.   
`max_results` |  The maximum number of top-scored classification results to return.   
`score_threshold` |  Overrides the ones provided in the model metadata. Results below this value are rejected.   
`category_allowlist` |  Allowlist of category names. If non-empty, classification results whose category name is not in this set will be filtered out. Duplicate or unknown category names are ignored. Mutually exclusive with `category_denylist`.   
`category_denylist` |  Denylist of category names. If non-empty, classification results whose category name is in this set will be filtered out. Duplicate or unknown category names are ignored. Mutually exclusive with `category_allowlist`.   
  
## Methods

### `to_ctypes`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/text/text_classifier.py#L72-L90)
    
    
    to_ctypes() -> TextClassifierOptionsC
    

Generates a ctypes TextClassifierOptionsC.

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
category_allowlist |  `None`  
category_denylist |  `None`  
display_names_locale |  `None`  
max_results |  `None`  
score_threshold |  `None`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
