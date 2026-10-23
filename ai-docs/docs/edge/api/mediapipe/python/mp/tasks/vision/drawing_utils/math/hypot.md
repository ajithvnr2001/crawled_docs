---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/hypot/
title: mp.tasks.vision.drawing_utils.math.hypot
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:41:59.158556+00:00
---

# mp.tasks.vision.drawing_utils.math.hypot

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/hypot/

hypot(*coordinates) -> value

#### View aliases

**Main aliases**

[`mp.tasks.vision.drawing_styles.drawing_utils.math.hypot`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/hypot)
    
    
    mp.tasks.vision.drawing_utils.math.hypot()
    

Multidimensional Euclidean distance from the origin to a point.

## Roughly equivalent to  
  
---  
sqrt(sum(x**2 for x in coordinates))   
  
For a two dimensional point (x, y), gives the hypotenuse using the Pythagorean theorem: sqrt(x _x + y_ y).

For example, the hypotenuse of a 3/4/5 right triangle is:
    
    
    <pre class="devsite-click-to-copy prettyprint lang-py">
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">hypot(3.0, 4.0)</code>
    <code class="no-select nocode">    5.0</code>
    <code class="no-select nocode">    </code>
    </pre>
    
