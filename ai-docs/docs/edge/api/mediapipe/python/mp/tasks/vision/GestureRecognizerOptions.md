---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizerOptions/
title: mp.tasks.vision.GestureRecognizerOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:34.495862+00:00
---

# mp.tasks.vision.GestureRecognizerOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizerOptions/




#  mp.tasks.vision.GestureRecognizerOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/gesture_recognizer.py#L155-L201) Options for the gesture recognizer task.
    
    
    mp.tasks.vision.GestureRecognizerOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        running_mode: [mp.tasks.vision.RunningMode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/RunningMode) = [mp.tasks.vision.FaceDetectorOptions.running_mode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions#running_mode),
        num_hands: int = 1,
        min_hand_detection_confidence: float = 0.5,
        min_hand_presence_confidence: float = 0.5,
        min_tracking_confidence: float = 0.5,
        canned_gesture_classifier_options: [mp.tasks.components.processors.ClassifierOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/processors/ClassifierOptions) = dataclasses.field(default_factory=_ClassifierOptions),
        custom_gesture_classifier_options: [mp.tasks.components.processors.ClassifierOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/processors/ClassifierOptions) = dataclasses.field(default_factory=_ClassifierOptions),
        result_callback: Optional[Callable[[GestureRecognizerResult, image_lib.Image, int], None]] = None
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the hand gesture recognizer task.   
`running_mode` |  The running mode of the task. Default to the image mode. Gesture recognizer task has three running modes: 1) The image mode for recognizing hand gestures on single image inputs. 2) The video mode for recognizing hand gestures on the decoded frames of a video. 3) The live stream mode for recognizing hand gestures on a live stream of input data, such as from camera.   
`num_hands` |  The maximum number of hands can be detected by the recognizer.   
`min_hand_detection_confidence` |  The minimum confidence score for the hand detection to be considered successful.   
`min_hand_presence_confidence` |  The minimum confidence score of hand presence score in the hand landmark detection.   
`min_tracking_confidence` |  The minimum confidence score for the hand tracking to be considered successful.   
`canned_gesture_classifier_options` |  Options for configuring the canned gestures classifier, such as score threshold, allow list and deny list of gestures. The categories for canned gesture classifiers are: ["None", "Closed_Fist", "Open_Palm", "Pointing_Up", "Thumb_Down", "Thumb_Up", "Victory", "ILoveYou"]. Note this option is subject to change.   
`custom_gesture_classifier_options` |  Options for configuring the custom gestures classifier, such as score threshold, allow list and deny list of gestures. Note this option is subject to change.   
`result_callback` |  The user-defined result callback for processing live stream data. The result callback should only be specified when the running mode is set to the live stream mode.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
min_hand_detection_confidence |  `0.5`  
min_hand_presence_confidence |  `0.5`  
min_tracking_confidence |  `0.5`  
num_hands |  `1`  
result_callback |  `None`  
running_mode |  `<VisionTaskRunningMode.IMAGE: 'IMAGE'>`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
