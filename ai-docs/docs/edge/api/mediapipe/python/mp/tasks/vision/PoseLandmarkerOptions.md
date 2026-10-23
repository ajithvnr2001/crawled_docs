---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/PoseLandmarkerOptions/
title: mp.tasks.vision.PoseLandmarkerOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:42.187662+00:00
---

# mp.tasks.vision.PoseLandmarkerOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/PoseLandmarkerOptions/




#  mp.tasks.vision.PoseLandmarkerOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/pose_landmarker.py#L240-L276) Options for the pose landmarker task.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.pose_landmarker.PoseLandmarkerOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/PoseLandmarkerOptions)
    
    
    mp.tasks.vision.PoseLandmarkerOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        running_mode: [mp.tasks.vision.RunningMode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/RunningMode) = [mp.tasks.vision.FaceDetectorOptions.running_mode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions#running_mode),
        num_poses: int = 1,
        min_pose_detection_confidence: float = 0.5,
        min_pose_presence_confidence: float = 0.5,
        min_tracking_confidence: float = 0.5,
        output_segmentation_masks: bool = False,
        result_callback: Optional[Callable[[PoseLandmarkerResult, image_lib.Image, int], None]] = None
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the pose landmarker task.   
`running_mode` |  The running mode of the task. Default to the image mode. PoseLandmarker has three running modes: 1) The image mode for detecting pose landmarks on single image inputs. 2) The video mode for detecting pose landmarks on the decoded frames of a video. 3) The live stream mode for detecting pose landmarks on the live stream of input data, such as from camera. In this mode, the "result_callback" below must be specified to receive the detection results asynchronously.   
`num_poses` |  The maximum number of poses can be detected by the PoseLandmarker.   
`min_pose_detection_confidence` |  The minimum confidence score for the pose detection to be considered successful.   
`min_pose_presence_confidence` |  The minimum confidence score of pose presence score in the pose landmark detection.   
`min_tracking_confidence` |  The minimum confidence score for the pose tracking to be considered successful.   
`output_segmentation_masks` |  whether to output segmentation masks.   
`result_callback` |  The user-defined result callback for processing live stream data. The result callback should only be specified when the running mode is set to the live stream mode.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
min_pose_detection_confidence |  `0.5`  
min_pose_presence_confidence |  `0.5`  
min_tracking_confidence |  `0.5`  
num_poses |  `1`  
output_segmentation_masks |  `False`  
result_callback |  `None`  
running_mode |  `<VisionTaskRunningMode.IMAGE: 'IMAGE'>`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
