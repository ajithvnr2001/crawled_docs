---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/draw_detection/
title: mp.tasks.vision.drawing_utils.draw_detection
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:41:40.291414+00:00
---

# mp.tasks.vision.drawing_utils.draw_detection

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/draw_detection/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/drawing_utils.py#L72-L119) Draws the detction bounding box and keypoints on the image.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.draw_detection`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/draw_detection)
    
    
    mp.tasks.vision.drawing_utils.draw_detection(
        image: np.ndarray,
        detection: [mp.tasks.components.containers.Detection](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Detection),
        keypoint_drawing_spec: [mp.tasks.vision.drawing_utils.DrawingSpec](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec) = [DrawingSpec(color=RED_COLOR)](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec),
        bbox_drawing_spec: [mp.tasks.vision.drawing_utils.DrawingSpec](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec) = [DrawingSpec()](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec)
    )
    

| 

## Args  
  
---  
  
`image` |  A three channel BGR image represented as numpy ndarray.   
`detection` |  A detection object with a bounding box.   
`keypoint_drawing_spec` |  A DrawingSpec object that specifies the keypoints' drawing settings such as color, line thickness, and circle radius.   
`bbox_drawing_spec` |  A DrawingSpec object that specifies the bounding box's drawing settings such as color and line thickness.   
  
## Raises  
  
---  
  
`ValueError` |  If the input image is not three channel BGR. 
