---
url: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/load_delegate/
title: tf.lite.experimental.load_delegate
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:37.530564+00:00
---

# tf.lite.experimental.load_delegate

> Source: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/load_delegate/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/tensorflow/tensorflow/blob/v2.1.0/tensorflow/lite/python/interpreter.py#L137-L182) Returns loaded Delegate object.
    
    
    tf.lite.experimental.load_delegate(
        library, options=None
    )
    

#### Example usage:
    
    
    import tensorflow as tf
    
    try:
      delegate = tf.lite.experimental.load_delegate('delegate.so')
    except ValueError:
      // Fallback to CPU
    
    if delegate:
      interpreter = tf.lite.Interpreter(
          model_path='model.tflite',
          experimental_delegates=[delegate])
    else:
      interpreter = tf.lite.Interpreter(model_path='model.tflite')
    

This is typically used to leverage EdgeTPU for running TensorFlow Lite models. For more information see: <https://coral.ai/docs/edgetpu/tflite-python/> | 

## Args  
  
---  
  
`library` |  Name of shared library containing the [TfLiteDelegate](https://www.tensorflow.org/lite/performance/delegates).   
`options` |  Dictionary of options that are required to load the delegate. All keys and values in the dictionary should be convertible to str. Consult the documentation of the specific delegate for required and legal options. (default None)   
  
## Returns  
  
---  
Delegate object.   
  
## Raises  
  
---  
  
`ValueError` |  Delegate failed to load.   
`RuntimeError` |  If delegate loading is used on unsupported platform. 
