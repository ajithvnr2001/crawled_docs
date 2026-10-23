---
url: https://ai.google.dev/edge/api/tflite/python/tf/lite/RepresentativeDataset/
title: tf.lite.RepresentativeDataset
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:33.590380+00:00
---

# tf.lite.RepresentativeDataset

> Source: https://ai.google.dev/edge/api/tflite/python/tf/lite/RepresentativeDataset/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/tensorflow/tensorflow/blob/v2.1.0/tensorflow/lite/python/lite.py#L171-L192) Representative dataset used to optimize the model.
    
    
    tf.lite.RepresentativeDataset(
        input_gen
    )
    

This is a generator function that provides a small dataset to calibrate or estimate the range, i.e, (min, max) of all floating-point arrays in the model (such as model input, activation outputs of intermediate layers, and model output) for quantization. Usually, this is a small subset of a few hundred samples randomly chosen, in no particular order, from the training or evaluation dataset. | 

## Args  
  
---  
  
`input_gen` |  A generator function that generates input samples for the model and has the same order, type and shape as the inputs to the model. Usually, this is a small subset of a few hundred samples randomly chosen, in no particular order, from the training or evaluation dataset. 
