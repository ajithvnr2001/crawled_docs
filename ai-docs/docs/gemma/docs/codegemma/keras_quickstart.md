---
url: https://ai.google.dev/gemma/docs/codegemma/keras_quickstart/
title: Keras CodeGemma Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:37.668503+00:00
---

# Keras CodeGemma Quickstart

> Source: https://ai.google.dev/gemma/docs/codegemma/keras_quickstart/

[![](https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png)View on ai.google.dev](https://ai.google.dev/gemma/docs/codegemma/keras_quickstart) |  [![](https://www.tensorflow.org/images/colab_logo_32px.png)Run in Google Colab](https://colab.research.google.com/github/google-gemma/cookbook/blob/main/docs/codegemma/keras_quickstart.ipynb) |  [![](https://www.kaggle.com/static/images/logos/kaggle-logo-transparent-300.png)Run in Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/google-gemma/cookbook/blob/main/docs/codegemma/keras_quickstart.ipynb) |  [![](https://ai.google.dev/images/cloud-icon.svg)Open in Vertex AI](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2Fgoogle-gemma%2Fcookbook%2Fmain%2Fdocs%2Fcodegemma%2Fkeras_quickstart.ipynb) |  [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://github.com/google-gemma/cookbook/blob/main/docs/codegemma/keras_quickstart.ipynb) CodeGemma is a family of lightweight, state-of-the art open models built from the same research and technology used to create the Gemini models. CodeGemma models are trained on more than 500 billion tokens of primarily code, using the same architectures as the Gemma model family. As a result, CodeGemma models achieve stateof-the-art code performance in both completion and generation tasks, while maintaining strong understanding and reasoning skills at scale. CodeGemma has 3 variants:

  * A 7B code pretrained model
  * A 7B instruction-tuned code model
  * A 2B model, trained specifically for code infilling and open-ended generation.

This guide walks you through using the CodeGemma 2B model with KerasHub for a code completion task.

## Setup

### Get access to CodeGemma

To complete this tutorial, you will first need to complete the setup instructions at [Gemma setup](https://ai.google.dev/gemma/docs/setup). The Gemma setup instructions show you how to do the following:

  * Get access to Gemma on [kaggle.com](https://kaggle.com).
  * Select a Colab runtime with sufficient resources to run the Gemma 2B model.
  * Generate and configure a Kaggle username and API key.

After you've completed the Gemma setup, move on to the next section, where you'll set environment variables for your Colab environment.

### Select the runtime

To complete this tutorial, you'll need to have a Colab runtime with sufficient resources to run the CodeGemma 2B model. In this case, you can use a T4 GPU:

  1. In the upper-right of the Colab window, select ▾ (**Additional connection options**).
  2. Select **Change runtime type**.
  3. Under **Hardware accelerator** , select **T4 GPU**.



### Configure your API key

To use Gemma, you must provide your Kaggle username and a Kaggle API key. To generate a Kaggle API key, go to the **Account** tab of your Kaggle user profile and select **Create New Token**. This will trigger the download of a `kaggle.json` file containing your API credentials. In Colab, select **Secrets** (🔑) in the left pane and add your Kaggle username and Kaggle API key. Store your username under the name `KAGGLE_USERNAME` and your API key under the name `KAGGLE_KEY`.

### Set environment variables

Set environment variables for `KAGGLE_USERNAME` and `KAGGLE_KEY`.
    
    
    import os
    from google.colab import userdata
    
    os.environ["KAGGLE_USERNAME"] = userdata.get('KAGGLE_USERNAME')
    os.environ["KAGGLE_KEY"] = userdata.get('KAGGLE_KEY')
    

### Install dependencies
    
    
    pip install -q -U keras-hub
    pip install -q -U keras

### Select a backend

Keras is a high-level, multi-framework deep learning API designed for simplicity and ease of use. Using Keras 3, you can run workflows on one of three backends: TensorFlow, JAX, or PyTorch. For this tutorial, configure the backend for TensorFlow.
    
    
    os.environ["KERAS_BACKEND"] = "tensorflow"  # Or "jax" or "torch".
    

### Import packages

Import Keras and KerasHub.
    
    
    import keras_hub
    import keras
    
    # Run at half precision.
    keras.config.set_floatx("bfloat16")
    

### Load Model

KerasHub provides implementations of many popular [model architectures](https://keras.io/api/keras_nlp/models/). In this tutorial, you'll create a model using `GemmaCausalLM`, an end-to-end Gemma model for causal language modeling. A causal language model predicts the next token based on previous tokens. Create the model using the `from_preset` method:
    
    
    gemma_lm = keras_hub.models.GemmaCausalLM.from_preset("code_gemma_2b_en")
    gemma_lm.summary()
    
    
    
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_2b_en/2/download/config.json...
    100%|██████████| 785/785 [00:00<00:00, 1.64MB/s]
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_2b_en/2/download/model.weights.h5...
    100%|██████████| 4.67G/4.67G [00:50<00:00, 99.2MB/s]
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_2b_en/2/download/tokenizer.json...
    100%|██████████| 591/591 [00:00<00:00, 946kB/s]
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_2b_en/2/download/assets/tokenizer/vocabulary.spm...
    100%|██████████| 4.04M/4.04M [00:00<00:00, 43.1MB/s]
    

The `from_preset` method instantiates the model from a preset architecture and weights. In the code above, the string `code_gemma_2b_en` specifies the preset architecture — a CodeGemma model with 2 billion parameters.

## Fill-in-the-middle code completion

This example uses CodeGemma's fill-in-the-middle (FIM) capability to complete code based on the surrounding context. This is particularly useful in code editor applications for inserting code where the text cursor is based on the code around it (before and after the cursor). CodeGemma lets you use 4 user-defined tokens - 3 for FIM and a `<|file_separator|>` token for multi-file context support. Use these to define constants.
    
    
    BEFORE_CURSOR = "<|fim_prefix|>"
    AFTER_CURSOR = "<|fim_suffix|>"
    AT_CURSOR = "<|fim_middle|>"
    FILE_SEPARATOR = "<|file_separator|>"
    

Define the stop tokens for the model.
    
    
    END_TOKEN = gemma_lm.preprocessor.tokenizer.end_token
    
    stop_tokens = (BEFORE_CURSOR, AFTER_CURSOR, AT_CURSOR, FILE_SEPARATOR, END_TOKEN)
    
    stop_token_ids = tuple(gemma_lm.preprocessor.tokenizer.token_to_id(x) for x in stop_tokens)
    

Format the prompt for code completion. Note that:

  * There should be no whitespaces between any FIM tokens and the prefix and suffix
  * The FIM middle token should be at the end to prime the model to continue filling in
  * The prefix or the suffix could be empty depending on where the cursor currently is in the file, or how much context you want to provide the model with

Use a helper function to format the prompt.
    
    
    def format_completion_prompt(before, after):
        return f"{BEFORE_CURSOR}{before}{AFTER_CURSOR}{after}{AT_CURSOR}"
    
    before = "import "
    after = """if __name__ == "__main__":\n    sys.exit(0)"""
    prompt = format_completion_prompt(before, after)
    print(prompt)
    
    
    
    <|fim_prefix|>import <|fim_suffix|>if __name__ == "__main__":
        sys.exit(0)<|fim_middle|>
    

Run the prompt. It is recommended to stream response tokens. Stop streaming upon encountering any of the user-defined or end of turn/senetence tokens to get the resulting code completion.
    
    
    gemma_lm.generate(prompt, stop_token_ids=stop_token_ids, max_length=128)
    
    
    
    '<|fim_prefix|>import <|fim_suffix|>if __name__ == "__main__":\n    sys.exit(0)<|fim_middle|>sys\n<|file_separator|>'
    

The model provides `sys` as the suggested code completion.

## Summary

This tutorial walked you through using CodeGemma to infill code based on the surrounding context. Next, check out the [AI Assisted Programming with CodeGemma and KerasHub notebook](https://ai.google.dev/gemma/docs/codegemma/code_assist_keras) for more examples on how you can use CodeGemma. Also refer to The [CodeGemma model card](https://ai.google.dev/gemma/docs/codegemma/model_card) for the technical specs of the CodeGemma models.
