---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/running_mode_lib/validate_running_mode/
title: mp.tasks.vision.drawing_styles.face_landmarker.running_mode_lib.validate_running_mode
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:41:39.810182+00:00
---

# mp.tasks.vision.drawing_styles.face_landmarker.running_mode_lib.validate_running_mode

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/running_mode_lib/validate_running_mode/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/vision_task_running_mode.py#L55-L79) Validates the running mode of the mediapipe vision task.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.running_mode_lib.validate_running_mode`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/running_mode_lib/validate_running_mode), [`mp.tasks.vision.drawing_styles.hand_landmarker.vision_task_running_mode.validate_running_mode`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/running_mode_lib/validate_running_mode), [`mp.tasks.vision.drawing_styles.pose_landmarker.running_mode_lib.validate_running_mode`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/running_mode_lib/validate_running_mode), [`mp.tasks.vision.drawing_utils.face_landmarker.running_mode_lib.validate_running_mode`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_styles/face_landmarker/running_mode_lib/validate_running_mode)
    
    
    mp.tasks.vision.drawing_styles.face_landmarker.running_mode_lib.validate_running_mode(
        running_mode: [mp.tasks.vision.RunningMode](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/RunningMode),
        packet_callback: Optional[Callable[[Mapping[str, Any]], None]] = None
    ) -> None
    

| 

## Args  
  
---  
  
`running_mode` |  The running mode of the mediapipe vision task.   
`packet_callback` |  The user-defined result callback.   
  
## Raises  
  
---  
  
`ValueError` |  If packet callback is provided in image or video mode or missing in live stream mode. 
