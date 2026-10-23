---
url: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/Analyzer/
title: tf.lite.experimental.Analyzer
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:34.167828+00:00
---

# tf.lite.experimental.Analyzer

> Source: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/Analyzer/

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/tensorflow/tensorflow/blob/v2.1.0/tensorflow/lite/python/analyzer.py#L35-L107) Provides a collection of TFLite model analyzer tools.

### Used in the notebooks

| Used in the guide  
---  
  
  * [TensorFlow Lite Model Analyzer](https://www.tensorflow.org/lite/guide/model_analyzer)

  
  
#### Example:
    
    
    model = tf.keras.applications.MobileNetV3Large()
    fb_model = tf.lite.TFLiteConverterV2.from_keras_model(model).convert()
    tf.lite.experimental.Analyzer.analyze(model_content=fb_model)
    # === TFLite ModelAnalyzer ===
    #
    # Your TFLite model has ‘1’ subgraph(s). In the subgraph description below,
    # T# represents the Tensor numbers. For example, in Subgraph#0, the MUL op
    # takes tensor #0 and tensor #19 as input and produces tensor #136 as output.
    #
    # Subgraph#0 main(T#0) -> [T#263]
    #   Op#0 MUL(T#0, T#19) -> [T#136]
    #   Op#1 ADD(T#136, T#18) -> [T#137]
    #   Op#2 CONV_2D(T#137, T#44, T#93) -> [T#138]
    #   Op#3 HARD_SWISH(T#138) -> [T#139]
    #   Op#4 DEPTHWISE_CONV_2D(T#139, T#94, T#24) -> [T#140]
    #   ...
    

## Methods

### `analyze`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.1.0/tensorflow/lite/python/analyzer.py#L63-L107)
    
    
    @staticmethod
    analyze(
        model_path=None, model_content=None, gpu_compatibility=False, **kwargs
    )
    

Analyzes the given tflite_model with dumping model structure.

This tool provides a way to understand users' TFLite flatbuffer model by dumping internal graph structure. It also provides additional features like checking GPU delegate compatibility.

Args  
---  
  
`model_path` |  TFLite flatbuffer model path.   
`model_content` |  TFLite flatbuffer model object.   
`gpu_compatibility` |  Whether to check GPU delegate compatibility.   
`**kwargs` |  Experimental keyword arguments to analyze API.   
  
Returns  
---  
Print analyzed report via console output. 
