---
url: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/OpResolverType/
title: tf.lite.experimental.OpResolverType
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:34.440951+00:00
---

# tf.lite.experimental.OpResolverType

> Source: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/OpResolverType/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/tensorflow/tensorflow/blob/v2.1.0/tensorflow/lite/python/interpreter.py#L315-L343) Different types of op resolvers for Tensorflow Lite.

  * `AUTO`: Indicates the op resolver that is chosen by default in TfLite Python, which is the "BUILTIN" as described below.
  * `BUILTIN`: Indicates the op resolver for built-in ops with optimized kernel implementation.
  * `BUILTIN_REF`: Indicates the op resolver for built-in ops with reference kernel implementation. It's generally used for testing and debugging.
  * `BUILTIN_WITHOUT_DEFAULT_DELEGATES`: Indicates the op resolver for built-in ops with optimized kernel implementation, but it will disable the application of default TfLite delegates (like the XNNPACK delegate) to the model graph. Generally this should not be used unless there are issues with the default configuration.

| 

## Class Variables  
  
---  
  
AUTO |  `<OpResolverType.AUTO: 0>`  
BUILTIN |  `<OpResolverType.BUILTIN: 1>`  
BUILTIN_REF |  `<OpResolverType.BUILTIN_REF: 2>`  
BUILTIN_WITHOUT_DEFAULT_DELEGATES |  `<OpResolverType.BUILTIN_WITHOUT_DEFAULT_DELEGATES: 3>`
