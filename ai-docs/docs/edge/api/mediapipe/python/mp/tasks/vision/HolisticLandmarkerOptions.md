---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/HolisticLandmarkerOptions/
title: mp.tasks.vision.HolisticLandmarkerOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:36.860448+00:00
---

# mp.tasks.vision.HolisticLandmarkerOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/HolisticLandmarkerOptions/




#  mp.tasks.vision.HolisticLandmarkerOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/holistic_landmarker.py#L225-L273) Options for the holistic landmarker task.
    
    
    mp.tasks.vision.HolisticLandmarkerOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        running_mode: [mp.tasks.vision.RunningMode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/RunningMode) = [mp.tasks.vision.FaceDetectorOptions.running_mode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions#running_mode),
        min_face_detection_confidence: float = 0.5,
        min_face_suppression_threshold: float = 0.5,
        min_face_landmarks_confidence: float = 0.5,
        min_pose_detection_confidence: float = 0.5,
        min_pose_suppression_threshold: float = 0.5,
        min_pose_landmarks_confidence: float = 0.5,
        min_hand_landmarks_confidence: float = 0.5,
        output_face_blendshapes: bool = False,
        output_segmentation_mask: bool = False,
        result_callback: Optional[Callable[[HolisticLandmarkerResult, image_lib.Image, int], None]] = None
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the holistic landmarker task.   
`running_mode` |  The running mode of the task. Default to the image mode. HolisticLandmarker has three running modes: 1) The image mode for detecting holistic landmarks on single image inputs. 2) The video mode for detecting holistic landmarks on the decoded frames of a video. 3) The live stream mode for detecting holistic landmarks on the live stream of input data, such as from camera. In this mode, the "result_callback" below must be specified to receive the detection results asynchronously.   
`min_face_detection_confidence` |  The minimum confidence score for the face detection to be considered successful.   
`min_face_suppression_threshold` |  The minimum non-maximum-suppression threshold for face detection to be considered overlapped.   
`min_face_landmarks_confidence` |  The minimum confidence score for the face landmark detection to be considered successful.   
`min_pose_detection_confidence` |  The minimum confidence score for the pose detection to be considered successful.   
`min_pose_suppression_threshold` |  The minimum non-maximum-suppression threshold for pose detection to be considered overlapped.   
`min_pose_landmarks_confidence` |  The minimum confidence score for the pose landmark detection to be considered successful.   
`min_hand_landmarks_confidence` |  The minimum confidence score for the hand landmark detection to be considered successful.   
`output_face_blendshapes` |  Whether HolisticLandmarker outputs face blendshapes classification. Face blendshapes are used for rendering the 3D face model.   
`output_segmentation_mask` |  whether to output segmentation masks.   
`result_callback` |  The user-defined result callback for processing live stream data. The result callback should only be specified when the running mode is set to the live stream mode.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
min_face_detection_confidence |  `0.5`  
min_face_landmarks_confidence |  `0.5`  
min_face_suppression_threshold |  `0.5`  
min_hand_landmarks_confidence |  `0.5`  
min_pose_detection_confidence |  `0.5`  
min_pose_landmarks_confidence |  `0.5`  
min_pose_suppression_threshold |  `0.5`  
output_face_blendshapes |  `False`  
output_segmentation_mask |  `False`  
result_callback |  `None`  
running_mode |  `<VisionTaskRunningMode.IMAGE: 'IMAGE'>`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
