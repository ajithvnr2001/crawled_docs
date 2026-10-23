---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerOptions/
title: mp.tasks.vision.FaceLandmarkerOptions \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:33.047389+00:00
---

# mp.tasks.vision.FaceLandmarkerOptions  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerOptions/




#  mp.tasks.vision.FaceLandmarkerOptions

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/face_landmarker.py#L2976-L3018) Options for the face landmarker task.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.FaceLandmarkerOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerOptions), [`mp.tasks.vision.drawing_styles.face_landmarker.FaceLandmarkerOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerOptions), [`mp.tasks.vision.drawing_utils.face_landmarker.FaceLandmarkerOptions`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/FaceLandmarkerOptions)
    
    
    mp.tasks.vision.FaceLandmarkerOptions(
        base_options: [mp.tasks.BaseOptions](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/BaseOptions),
        running_mode: [mp.tasks.vision.RunningMode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/RunningMode) = [mp.tasks.vision.FaceDetectorOptions.running_mode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/FaceDetectorOptions#running_mode),
        num_faces: int = 1,
        min_face_detection_confidence: float = 0.5,
        min_face_presence_confidence: float = 0.5,
        min_tracking_confidence: float = 0.5,
        output_face_blendshapes: bool = False,
        output_facial_transformation_matrixes: bool = False,
        result_callback: Optional[Callable[[FaceLandmarkerResult, image_lib.Image, int], None]] = None
    )
    

| 

## Attributes  
  
---  
  
`base_options` |  Base options for the face landmarker task.   
`running_mode` |  The running mode of the task. Default to the image mode. FaceLandmarker has three running modes: 1) The image mode for detecting face landmarks on single image inputs. 2) The video mode for detecting face landmarks on the decoded frames of a video. 3) The live stream mode for detecting face landmarks on the live stream of input data, such as from camera. In this mode, the "result_callback" below must be specified to receive the detection results asynchronously.   
`num_faces` |  The maximum number of faces that can be detected by the FaceLandmarker.   
`min_face_detection_confidence` |  The minimum confidence score for the face detection to be considered successful.   
`min_face_presence_confidence` |  The minimum confidence score of face presence score in the face landmark detection.   
`min_tracking_confidence` |  The minimum confidence score for the face tracking to be considered successful.   
`output_face_blendshapes` |  Whether FaceLandmarker outputs face blendshapes classification. Face blendshapes are used for rendering the 3D face model.   
`output_facial_transformation_matrixes` |  Whether FaceLandmarker outputs facial transformation_matrix. Facial transformation matrix is used to transform the face landmarks in canonical face to the detected face, so that users can apply face effects on the detected landmarks.   
`result_callback` |  The user-defined result callback for processing live stream data. The result callback should only be specified when the running mode is set to the live stream mode.   
  
## Methods

### `__eq__`
    
    
    __eq__(
        other
    )
    

## Class Variables  
  
---  
  
min_face_detection_confidence |  `0.5`  
min_face_presence_confidence |  `0.5`  
min_tracking_confidence |  `0.5`  
num_faces |  `1`  
output_face_blendshapes |  `False`  
output_facial_transformation_matrixes |  `False`  
result_callback |  `None`  
running_mode |  `<VisionTaskRunningMode.IMAGE: 'IMAGE'>`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
