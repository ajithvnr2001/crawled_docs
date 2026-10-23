---
url: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/authoring/compatible/
title: tf.lite.experimental.authoring.compatible
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:35.927516+00:00
---

# tf.lite.experimental.authoring.compatible

> Source: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/authoring/compatible/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/tensorflow/tensorflow/blob/v2.1.0/tensorflow/lite/python/authoring/authoring.py#L263-L301) Wraps [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) into a callable function with TFLite compatibility checking.
    
    
    tf.lite.experimental.authoring.compatible(
        target=None, converter_target_spec=None, **kwargs
    )
    

### Used in the notebooks

| Used in the guide  
---  
  
  * [TFLite Authoring Tool](https://www.tensorflow.org/lite/guide/authoring)

  
  
#### Example:
    
    
    @tf.lite.experimental.authoring.compatible
    @tf.function(input_signature=[
        tf.TensorSpec(shape=[None], dtype=tf.float32)
    ])
    def f(x):
        return tf.cosh(x)
    
    result = f(tf.constant([0.0]))
    # COMPATIBILITY WARNING: op 'tf.Cosh' require(s) "Select TF Ops" for model
    # conversion for TensorFlow Lite.
    # Op: tf.Cosh
    #   - tensorflow/python/framework/op_def_library.py:748
    #   - tensorflow/python/ops/gen_math_ops.py:2458
    #   - <stdin>:6
    

## Args  
  
---  
  
`target` |  A [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) to decorate.   
`converter_target_spec` |  target_spec of TFLite converter parameter.   
`**kwargs` |  The keyword arguments of the decorator class _Compatible.   
  
## Returns  
  
---  
A callable object of `tf.lite.experimental.authoring._Compatible`. 
