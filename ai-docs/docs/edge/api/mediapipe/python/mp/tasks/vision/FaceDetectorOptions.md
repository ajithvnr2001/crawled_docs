---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions/
title: mp.tasks.vision.FaceDetectorOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:32.858982+00:00
---

# mp.tasks.vision.FaceDetectorOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions/




#  mp.tasks.vision.FaceDetectorOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_detector.py#L133-L161) Options for the face detector task.
    
    
    mp.tasks.vision.FaceDetectorOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        running_mode: [mp.tasks.vision.RunningMode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/RunningMode) = [mp.tasks.vision.FaceDetectorOptions.running_mode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions#running_mode),
        min_detection_confidence: float = 0.5,
        min_suppression_threshold: float = 0.3,
        result_callback: Optional[Callable[[detections_module.DetectionResult, image_module.Image,
            int], None]] = None
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the face detector task.   
`running_mode` |  The running mode of the task. Default to the image mode. Face detector task has three running modes: 1) The image mode for detecting faces on single image inputs. 2) The video mode for detecting faces on the decoded frames of a video. 3) The live stream mode for detecting faces on a live stream of input data, such as from camera.   
`min_detection_confidence` |  The minimum confidence score for the face detection to be considered successful.   
`min_suppression_threshold` |  The minimum non-maximum-suppression threshold for face detection to be considered overlapped.   
`result_callback` |  The user-defined result callback for processing live stream data. The result callback should only be specified when the running mode is set to the live stream mode.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
min_detection_confidence |  `0.5`  
min_suppression_threshold |  `0.3`  
result_callback |  `None`  
running_mode |  `<VisionTaskRunningMode.IMAGE: 'IMAGE'>`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
