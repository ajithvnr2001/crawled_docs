---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/draw_axis/
title: mp.tasks.vision.drawing_utils.draw_axis
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:41:40.606534+00:00
---

# mp.tasks.vision.drawing_utils.draw_axis

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/draw_axis/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/drawing_utils.py#L210-L261) Draws the 3D axis on the image.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.draw_axis`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/draw_axis)
    
    
    mp.tasks.vision.drawing_utils.draw_axis(
        image: np.ndarray,
        rotation: np.ndarray,
        translation: np.ndarray,
        focal_length: tuple[float, float] = (1.0, 1.0),
        principal_point: tuple[float, float] = (0.0, 0.0),
        axis_length: float = 0.1,
        axis_drawing_spec: [mp.tasks.vision.drawing_utils.DrawingSpec](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec) = [DrawingSpec()](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec)
    )
    

| 

## Args  
  
---  
  
`image` |  A three channel BGR image represented as numpy ndarray.   
`rotation` |  Rotation matrix from object to camera coordinate frame.   
`translation` |  Translation vector from object to camera coordinate frame.   
`focal_length` |  camera focal length along x and y directions.   
`principal_point` |  camera principal point in x and y.   
`axis_length` |  length of the axis in the drawing.   
`axis_drawing_spec` |  A DrawingSpec object that specifies the xyz axis drawing settings such as line thickness.   
  
## Raises  
  
---  
  
`ValueError` |  If one of the followings: a) If the input image is not three channel BGR. 
