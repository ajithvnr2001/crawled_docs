---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/plot_landmarks/
title: mp.tasks.vision.drawing_utils.plot_landmarks
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:31.124227+00:00
---

# mp.tasks.vision.drawing_utils.plot_landmarks

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/plot_landmarks/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/drawing_utils.py#L268-L338) Plot the landmarks and the connections in matplotlib 3d.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.plot_landmarks`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/plot_landmarks)
    
    
    mp.tasks.vision.drawing_utils.plot_landmarks(
        landmark_list: list[landmark_module.NormalizedLandmark],
        connections: Optional[list[tuple[int, int]]] = None,
        landmark_drawing_spec: [mp.tasks.vision.drawing_utils.DrawingSpec](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec) = [DrawingSpec(color=RED_COLOR, thickness=5)](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec),
        connection_drawing_spec: [mp.tasks.vision.drawing_utils.DrawingSpec](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec) = [DrawingSpec(color=BLACK_COLOR, thickness=5)](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec),
        elevation: int = 10,
        azimuth: int = 10
    )
    

| 

## Args  
  
---  
  
`landmark_list` |  A list of normalized landmarks to be plotted.   
`connections` |  A list of landmark index tuples that specifies how landmarks to be connected.   
`landmark_drawing_spec` |  A DrawingSpec object that specifies the landmarks' drawing settings such as color and line thickness.   
`connection_drawing_spec` |  A DrawingSpec object that specifies the connections' drawing settings such as color and line thickness.   
`elevation` |  The elevation from which to view the plot.   
`azimuth` |  the azimuth angle to rotate the plot.   
  
## Raises  
  
---  
  
`ValueError` |  If any connection contains an invalid landmark index. 
