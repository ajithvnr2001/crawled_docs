---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/ImageFormat/
title: mp.ImageFormat \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:04.596339+00:00
---

# mp.ImageFormat  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/ImageFormat/




#  mp.ImageFormat

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image.py#L30-L64) An enum describing supported raw image formats.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.image_lib.ImageFormat`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/ImageFormat), [`mp.tasks.vision.drawing_styles.face_landmarker.image_lib.ImageFormat`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/ImageFormat), [`mp.tasks.vision.drawing_styles.hand_landmarker.image_lib.ImageFormat`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/ImageFormat), [`mp.tasks.vision.drawing_styles.pose_landmarker.image_lib.ImageFormat`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/ImageFormat), [`mp.tasks.vision.drawing_utils.face_landmarker.image_lib.ImageFormat`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/ImageFormat) SRGB: sRGB, interleaved: one byte for R, then one byte for G, then one byte for B for each pixel. SRGBA: sRGBA, interleaved: one byte for R, one byte for G, one byte for B, one byte for alpha or unused. SBGRA: sBGRA, interleaved: one byte for B, one byte for G, one byte for R, one byte for alpha or unused. GRAY8: Grayscale, one byte per pixel. GRAY16: Grayscale, one uint16 per pixel. SRGB48: sRGB, interleaved, each component is a uint16. SRGBA64: sRGBA, interleaved, each component is a uint16. VEC32F1: One float per pixel. VEC32F2: Two floats per pixel. | 

## Class Variables  
  
---  
  
GRAY16 |  `<ImageFormat.GRAY16: 4>`  
GRAY8 |  `<ImageFormat.GRAY8: 3>`  
SRGB |  `<ImageFormat.SRGB: 1>`  
SRGB48 |  `<ImageFormat.SRGB48: 7>`  
SRGBA |  `<ImageFormat.SRGBA: 2>`  
SRGBA64 |  `<ImageFormat.SRGBA64: 8>`  
UNKNOWN |  `<ImageFormat.UNKNOWN: 0>`  
VEC32F1 |  `<ImageFormat.VEC32F1: 9>`  
VEC32F2 |  `<ImageFormat.VEC32F2: 12>`  
VEC32F4 |  `<ImageFormat.VEC32F4: 13>`  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
