---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/draw_landmarks/
title: mp.tasks.vision.drawing_utils.draw_landmarks
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:41:40.433968+00:00
---

# mp.tasks.vision.drawing_utils.draw_landmarks

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/draw_landmarks/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/drawing_utils.py#L122-L207) Draws the landmarks and the connections on the image.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.draw_landmarks`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/draw_landmarks)
    
    
    mp.tasks.vision.drawing_utils.draw_landmarks(
        image: np.ndarray,
        landmark_list: list[landmark_module.NormalizedLandmark],
        connections: Optional[list[_CONNECTION]] = None,
        landmark_drawing_spec: Optional[Union[DrawingSpec, Mapping[int, DrawingSpec]]] = [DrawingSpec(color=RED_COLOR)](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec),
        connection_drawing_spec: Union[DrawingSpec, Mapping[tuple[int, int], DrawingSpec]] = [DrawingSpec()](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/DrawingSpec),
        is_drawing_landmarks: bool = True
    )
    

| 

## Args  
  
---  
  
`image` |  A three channel BGR image represented as numpy ndarray.   
`landmark_list` |  A list of normalized landmarks to be annotated on the image.   
`connections` |  A list of landmark index tuples that specifies how landmarks to be connected in the drawing.   
`landmark_drawing_spec` |  Either a DrawingSpec object or a mapping from hand landmarks to the DrawingSpecs that specifies the landmarks' drawing settings such as color, line thickness, and circle radius. If this argument is explicitly set to None, no landmarks will be drawn.   
`connection_drawing_spec` |  Either a DrawingSpec object or a mapping from hand connections to the DrawingSpecs that specifies the connections' drawing settings such as color and line thickness. If this argument is explicitly set to None, no landmark connections will be drawn.   
`is_drawing_landmarks` |  Whether to draw landmarks. If set false, skip drawing landmarks, only contours will be drawed.   
  
## Raises  
  
---  
  
`ValueError` |  If one of the followings: a) If the input image is not three channel BGR. b) If any connetions contain invalid landmark index. 
