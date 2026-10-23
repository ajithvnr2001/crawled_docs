---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/comb/
title: mp.tasks.vision.drawing_utils.math.comb
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:41:50.445952+00:00
---

# mp.tasks.vision.drawing_utils.math.comb

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/comb/

Number of ways to choose k items from n items without repetition and without order.

#### View aliases

**Main aliases**

[`mp.tasks.vision.drawing_styles.drawing_utils.math.comb`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/comb)
    
    
    mp.tasks.vision.drawing_utils.math.comb(
        n, k, /
    )
    

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates to zero when k > n.

Also called the binomial coefficient because it is equivalent to the coefficient of k-th term in polynomial expansion of the expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers. Raises ValueError if either of the arguments are negative.
