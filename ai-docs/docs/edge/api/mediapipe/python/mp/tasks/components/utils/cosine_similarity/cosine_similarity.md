---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/utils/cosine_similarity/cosine_similarity/
title: mp.tasks.components.utils.cosine_similarity.cosine_similarity \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:26.605210+00:00
---

# mp.tasks.components.utils.cosine_similarity.cosine_similarity  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/utils/cosine_similarity/cosine_similarity/




#  mp.tasks.components.utils.cosine_similarity.cosine_similarity

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/utils/cosine_similarity.py#L39-L68) Utility function to compute cosine similarity between two embedding.
    
    
    mp.tasks.components.utils.cosine_similarity.cosine_similarity(
        u: [mp.tasks.components.containers.Embedding](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Embedding),
        v: [mp.tasks.components.containers.Embedding](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/Embedding)
    ) -> float
    

May return an InvalidArgumentError if e.g. the feature vectors are of different types (quantized vs. float), have different sizes, or have an L2-norm of 0. | 

## Args  
  
---  
  
`u` |  An embedding.   
`v` |  An embedding.   
  
## Returns  
  
---  
Cosine similarity value.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
