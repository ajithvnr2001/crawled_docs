---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/InteractiveSegmenterOptions/
title: mp.tasks.vision.InteractiveSegmenterOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:40.570827+00:00
---

# mp.tasks.vision.InteractiveSegmenterOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/InteractiveSegmenterOptions/




#  mp.tasks.vision.InteractiveSegmenterOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/interactive_segmenter.py#L126-L150) Options for the interactive segmenter task.
    
    
    mp.tasks.vision.InteractiveSegmenterOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        output_confidence_masks: bool = True,
        output_category_mask: bool = False
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the interactive segmenter task.   
`running_mode` |  The running mode of the task.   
`output_confidence_masks` |  Whether to output confidence masks.   
`output_category_mask` |  Whether to output category mask.   
`result_callback` |  The callback function that is invoked synchronously when the current thread is idle.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
output_category_mask |  `False`  
output_confidence_masks |  `True`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
