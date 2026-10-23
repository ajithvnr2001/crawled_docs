---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ObjectDetectorOptions/
title: mp.tasks.vision.ObjectDetectorOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:42.513721+00:00
---

# mp.tasks.vision.ObjectDetectorOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/ObjectDetectorOptions/




#  mp.tasks.vision.ObjectDetectorOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/object_detector.py#L167-L208) Options for the object detector task.
    
    
    mp.tasks.vision.ObjectDetectorOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        running_mode: [mp.tasks.vision.RunningMode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/RunningMode) = [mp.tasks.vision.FaceDetectorOptions.running_mode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions#running_mode),
        display_names_locale: Optional[str] = None,
        max_results: Optional[int] = -1,
        score_threshold: Optional[float] = 0.0,
        category_allowlist: Optional[List[str]] = None,
        category_denylist: Optional[List[str]] = None,
        result_callback: Optional[Callable[[detections_module.DetectionResult, image_module.Image,
            int], None]] = None
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the object detector task.   
`running_mode` |  The running mode of the task. Default to the image mode. Object detector task has three running modes: 1) The image mode for detecting objects on single image inputs. 2) The video mode for detecting objects on the decoded frames of a video. 3) The live stream mode for detecting objects on a live stream of input data, such as from camera.   
`display_names_locale` |  The locale to use for display names specified through the TFLite Model Metadata.   
`max_results` |  The maximum number of top-scored classification results to return.   
`score_threshold` |  Overrides the ones provided in the model metadata. Results below this value are rejected.   
`category_allowlist` |  Allowlist of category names. If non-empty, detection results whose category name is not in this set will be filtered out. Duplicate or unknown category names are ignored. Mutually exclusive with `category_denylist`.   
`category_denylist` |  Denylist of category names. If non-empty, detection results whose category name is in this set will be filtered out. Duplicate or unknown category names are ignored. Mutually exclusive with `category_allowlist`.   
`result_callback` |  The user-defined result callback for processing live stream data. The result callback should only be specified when the running mode is set to the live stream mode.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
category_allowlist |  `None`  
category_denylist |  `None`  
display_names_locale |  `None`  
max_results |  `-1`  
result_callback |  `None`  
running_mode |  `<VisionTaskRunningMode.IMAGE: 'IMAGE'>`  
score_threshold |  `0.0`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
