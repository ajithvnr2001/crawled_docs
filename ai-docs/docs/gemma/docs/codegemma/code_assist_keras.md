---
url: https://ai.google.dev/gemma/docs/codegemma/code_assist_keras/
title: AI Assisted programming with CodeGemma and KerasNLP
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:39.074159+00:00
---

# AI Assisted programming with CodeGemma and KerasNLP

> Source: https://ai.google.dev/gemma/docs/codegemma/code_assist_keras/

[![](https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png)View on ai.google.dev](https://ai.google.dev/gemma/docs/codegemma/code_assist_keras) |  [![](https://www.tensorflow.org/images/colab_logo_32px.png)Run in Google Colab](https://colab.research.google.com/github/google-gemma/cookbook/blob/main/docs/codegemma/code_assist_keras.ipynb) |  [![](https://www.kaggle.com/static/images/logos/kaggle-logo-transparent-300.png)Run in Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/google-gemma/cookbook/blob/main/docs/codegemma/code_assist_keras.ipynb) |  [![](https://ai.google.dev/images/cloud-icon.svg)Open in Vertex AI](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2Fgoogle-gemmma%2Fcookbook%2Fmain%2Fdocs%2Fcodegemma%2Fcode_assist_keras.ipynb) |  [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://github.com/google-gemma/cookbook/blob/main/docs/codegemma/code_assist_keras.ipynb)

## Overview

CodeGemma is a variant of Gemma that is fine-tuned for coding tasks. This tutorial builds on the [Keras CodeGemma quickstart](https://colab.research.google.com/drive/11Va7W2Yl12JUnfx9YDJmy90kBu1i4rtw) and shows you more ways in which CodeGemma can assist your programming tasks.

## Setup

### Get access to CodeGemma

To complete this tutorial, you will first need to complete the setup instructions at [Gemma setup](https://ai.google.dev/gemma/docs/setup). The Gemma setup instructions show you how to do the following:

  * Get access to Gemma on [kaggle.com](https://kaggle.com).
  * Select a Colab runtime with sufficient resources to run the Gemma 7B model.
  * Generate and configure a Kaggle username and API key.

After you've completed the Gemma setup, move on to the next section, where you'll set environment variables for your Colab environment.

### Select the runtime

To run the CodeGemma 7B models, you'll need to have a paid Colab Pro plan which provides a runtime with an A100 GPU.

  1. In the upper-right of the Colab window, select ▾ (**Additional connection options**).
  2. Select **Change runtime type**.
  3. Under **Hardware accelerator** , select **A100 GPU**.



### Configure your API key

To use Gemma, you must provide your Kaggle username and a Kaggle API key. To generate a Kaggle API key, go to the **Account** tab of your Kaggle user profile and select **Create New Token**. This will trigger the download of a `kaggle.json` file containing your API credentials. In Colab, select **Secrets** (🔑) in the left pane and add your Kaggle username and Kaggle API key. Store your username under the name `KAGGLE_USERNAME` and your API key under the name `KAGGLE_KEY`.

### Set environment variables

Set environment variables for `KAGGLE_USERNAME` and `KAGGLE_KEY`.
    
    
    import os
    from google.colab import userdata
    
    os.environ["KAGGLE_USERNAME"] = userdata.get('KAGGLE_USERNAME')
    os.environ["KAGGLE_KEY"] = userdata.get('KAGGLE_KEY')
    

### Install dependencies
    
    
    pip install -q -U keras-nlp

### Select a backend

Keras is a high-level, multi-framework deep learning API designed for simplicity and ease of use. Using Keras 3, you can run workflows on one of three backends: TensorFlow, JAX, or PyTorch. For this tutorial, configure the backend for JAX.
    
    
    os.environ["KERAS_BACKEND"] = "jax"  # Or "tensorflow" or "torch".
    

### Import packages

Import Keras and KerasNLP.
    
    
    import keras_nlp
    import keras
    
    # Run at half precision.
    keras.config.set_floatx("bfloat16")
    

## CodeGemma 7B Model Examples

This section covers examples of using the pre-trained 7B CodeGemma model to help with coding tasks.

### Load the model

KerasNLP provides implementations of all three CodeGemma variants (2B and 7B pre-trained (PT) and 7B instruction-tuned (IT)) using [`GemmaCausalLM`](https://keras.io/api/keras_nlp/models/gemma/gemma_causal_lm/), an end-to-end Gemma model for causal language modeling. A causal language model predicts the next token based on previous tokens. For this example, load the `code_gemma_7b_en` model using the [`from_preset`](https://keras.io/api/keras_nlp/models/gemma/gemma_causal_lm/#frompreset-method) method.
    
    
    gemma_lm_7b = keras_nlp.models.GemmaCausalLM.from_preset("code_gemma_7b_en")
    
    
    
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_7b_en/1/download/config.json...
    100%|██████████| 556/556 [00:00<00:00, 790kB/s]
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_7b_en/1/download/model.weights.h5...
    100%|██████████| 15.9G/15.9G [02:39<00:00, 107MB/s]
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_7b_en/1/download/tokenizer.json...
    100%|██████████| 401/401 [00:00<00:00, 587kB/s]
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_7b_en/1/download/assets/tokenizer/vocabulary.spm...
    100%|██████████| 4.04M/4.04M [00:00<00:00, 16.4MB/s]
    
    
    
    gemma_lm_7b.summary()
    

The `from_preset` method instantiates the model from a preset architecture and weights.

### Code completion with Multi-line FIM

The PT CodeGemma models are trained on code infilling tasks. This section shows examples that use CodeGemma's multi-line fill-in the-middle (FIM) capability to autofill code at the specified cursor location based on the surrounding context. As a first step, define constants and a prompt formatting helper function.
    
    
    # Formatting control tokens to specify cursor location
    BEFORE_CURSOR = "<|fim_prefix|>"
    AFTER_CURSOR = "<|fim_suffix|>"
    AT_CURSOR = "<|fim_middle|>"
    FILE_SEPARATOR = "<|file_separator|>"
    
    # Define model stop tokens
    END_TOKEN = gemma_lm_7b.preprocessor.tokenizer.end_token
    stop_tokens = (BEFORE_CURSOR, AFTER_CURSOR, AT_CURSOR, FILE_SEPARATOR, END_TOKEN)
    stop_token_ids = tuple(gemma_lm_7b.preprocessor.tokenizer.token_to_id(x) for x in stop_tokens)
    
    def format_completion_prompt(before, after):
        return f"{BEFORE_CURSOR}{before}{AFTER_CURSOR}{after}{AT_CURSOR}"
    

#### Example 1 - Insert missing condition

The example code below to generate the Fibonacci sequence will not execute correctly if `n=1`:
    
    
    def fibonacci(n: int) -> int:
      if n == 0:
        return 0
      # The cursor is right before the e in the following line
      else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

Assuming that the cursor is at the beginning of line 4 (where the `else` clause is), then the content before and after the cursor is:
    
    
    before = """def fibonacci(n: int) -> int:\n  if n == 0:\n    return 0\n""" # Mind the spaces!
    after = """\n  else:\n    return fibonacci(n - 1) + fibonacci(n-2)\n"""
    
    
    
    prompt = format_completion_prompt(before, after)
    print(prompt)
    
    
    
    <|fim_prefix|>def fibonacci(n: int) -> int:
      if n == 0:
        return 0
    <|fim_suffix|>
      else:
        return fibonacci(n - 1) + fibonacci(n-2)
    <|fim_middle|>
    

Run the prompt.
    
    
    print(gemma_lm_7b.generate(prompt, stop_token_ids=stop_token_ids, max_length=128))
    
    
    
    <|fim_prefix|>def fibonacci(n: int) -> int:
      if n == 0:
        return 0
    <|fim_suffix|>
      else:
        return fibonacci(n - 1) + fibonacci(n-2)
    <|fim_middle|>elif n == 1:
        return 1<|file_separator|>
    

The model inserts the correct `elif` conidtion for `n=1` at the location of the cursor.

#### Example 2 - Complete DFS traversal algorithm

Auto-complete code for a depth-first search (DFS) tree traversal algorithm.
    
    
    before = """void dfs(node* root) {
      if (root->left) {
        dfs(root->left);
      }"""
    after = """\nprintf("%d", root->value);
    }"""
    
    
    
    prompt = format_completion_prompt(before, after)
    print(prompt)
    
    
    
    <|fim_prefix|>void dfs(node* root) {
      if (root->left) {
        dfs(root->left);
      }<|fim_suffix|>
    printf("%d", root->value);
    }<|fim_middle|>
    

Run the prompt.
    
    
    print(gemma_lm_7b.generate(prompt, stop_token_ids=stop_token_ids, max_length=128))
    
    
    
    <|fim_prefix|>void dfs(node* root) {
      if (root->left) {
        dfs(root->left);
      }<|fim_suffix|>
    printf("%d", root->value);
    }<|fim_middle|>
      if (root->right) {
        dfs(root->right);
      }<|file_separator|>
    

### Code generation

In addition to code infilling, the CodeGemma 7B PT is model is also trained on natural language corpuses. You can use this to prompt the model to generate code.
    
    
    generation_prompt= """Write a rust function to identify non-prime numbers.
    Examples:
    >>> is_not_prime(2)
    False
    >>> is_not_prime(10)
    True
    pub fn is_not_prime(n: i32) -> bool {"""
    
    
    
    print(gemma_lm_7b.generate(generation_prompt, max_length=500))
    
    
    
    Write a rust function to identify non-prime numbers.
    Examples:
    >>> is_not_prime(2)
    False
    >>> is_not_prime(10)
    True
    pub fn is_not_prime(n: i32) -> bool {
        if n <= 1 {
            return true;
        }
        for i in 2..n {
            if n % i == 0 {
                return true;
            }
        }
        false
    }
    

## 7B IT model examples

This section uses the CodeGemma 7B Instruction-Tuned model for more advanced coding tasks. The CodeGemma 7B IT model is derived from the CodeGemma 7B PT model through supervised fine-tuning on code along with Reinforcement Learning with Human Feedback. This section covers examples of using this model for open-ended generation.

### Load the IT model

Load the `code_gemma_instruct_7b_en` model using the `from_preset` method.
    
    
    gemma_lm_7b_it = keras_nlp.models.GemmaCausalLM.from_preset("code_gemma_instruct_7b_en")
    gemma_lm_7b_it.summary()
    
    
    
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_instruct_7b_en/1/download/config.json...
    100%|██████████| 556/556 [00:00<00:00, 754kB/s]
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_instruct_7b_en/1/download/model.weights.h5...
    100%|██████████| 15.9G/15.9G [03:18<00:00, 86.2MB/s]
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_instruct_7b_en/1/download/tokenizer.json...
    100%|██████████| 401/401 [00:00<00:00, 593kB/s]
    Downloading from https://www.kaggle.com/api/v1/models/keras/codegemma/keras/code_gemma_instruct_7b_en/1/download/assets/tokenizer/vocabulary.spm...
    100%|██████████| 4.04M/4.04M [00:00<00:00, 16.8MB/s]
    

IT models are trained with a specific formatter that annotates all instruction tuning examples with extra information to indicate roles and delineate turns in a conversation. As a first step, define constants and a prompt formatting helper function.
    
    
    # Formatting control tokens for instruction tuning
    START_OF_TURN_USER = "<start_of_turn>user"
    END_OF_TURN = "<end_of_turn>"
    START_OF_TURN_MODEL = "<start_of_turn>model"
    
    # Formatting helper function
    def format_instruction_prompt(context):
        return f"{START_OF_TURN_USER}\n{context}{END_OF_TURN}\n{START_OF_TURN_MODEL}\n"
    

### Code translation
    
    
    context1 = """
    You are an experienced C and Python programmer. Convert the following Python code into C.
    ```python
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    ```\n"""
    

Format the prompt.
    
    
    prompt1 = format_instruction_prompt(context1)
    print(prompt1)
    
    
    
    <start_of_turn>user
    
    You are an experienced C and Python programmer. Convert the following Python code into C.
    
    ```python
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    ```
    <end_of_turn>
    <start_of_turn>model
    

Run the prompt.
    
    
    print(gemma_lm_7b_it.generate(prompt1, max_length=500))
    
    
    
    <start_of_turn>user
    
    You are an experienced C and Python programmer. Convert the following Python code into C.
    
    ```python
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    ```
    <end_of_turn>
    <start_of_turn>model
    Here is the C code equivalent of the Python code:
    
    ```c
    int factorial(int n) {
      int result = 1;
      for (int i = 2; i <= n; i++) {
        result *= i;
      }
      return result;
    }
    ```
    
    Here is a breakdown of the changes:
    
    * The function is declared with the `int` return type, as in Python.
    * The `for` loop is converted to a `for` loop with an `int` variable `i` initialized to 2 and incremented by 1 in each iteration.
    * The `range` function is replaced with a simple loop that iterates from 2 to `n` (inclusive).
    * The `result *= i` statement is used to multiply `result` by `i` in each iteration.
    * The `return` statement is used to return the final value of `result`.
    

### Code vulnerability detection
    
    
    context2 = """
    You are an experienced C++ programmer hunting for vulnerable code. Is the following code vulnerable? Explain your reasoning.
    ```cpp
    int i;
    unsigned int numWidgets;
    Widget **WidgetList;
    
    numWidgets = GetUntrustedSizeValue();
    if ((numWidgets == 0) || (numWidgets > MAX_NUM_WIDGETS)) {
        ExitError("Incorrect number of widgets requested!");
    }
    WidgetList = (Widget **) malloc(numWidgets * sizeof(Widget *));
    printf("WidgetList ptr=%p\n", WidgetList);
    for (i = 0; i < numWidgets; i++) {
        WidgetList[i] = InitializeWidget();
    }
    WidgetList[numWidgets] = NULL;
    showWidgets(WidgetList);
    ```\n"""
    

Format the prompt.
    
    
    prompt2 = format_instruction_prompt(context2)
    print(prompt2)
    
    
    
    <start_of_turn>user
    
    You are an experienced C++ programmer hunting for vulnerable code. Is the following code vulnerable? Explain your reasoning.
    
    ```cpp
    int i;
    unsigned int numWidgets;
    Widget **WidgetList;
    
    numWidgets = GetUntrustedSizeValue();
    if ((numWidgets == 0) || (numWidgets > MAX_NUM_WIDGETS)) {
        ExitError("Incorrect number of widgets requested!");
    }
    WidgetList = (Widget **) malloc(numWidgets * sizeof(Widget *));
    printf("WidgetList ptr=%p
    ", WidgetList);
    for (i = 0; i < numWidgets; i++) {
        WidgetList[i] = InitializeWidget();
    }
    WidgetList[numWidgets] = NULL;
    showWidgets(WidgetList);
    ```
    <end_of_turn>
    <start_of_turn>model
    
    
    
    print(gemma_lm_7b_it.generate(prompt2, max_length=1000))
    
    
    
    <start_of_turn>user
    
    You are an experienced C++ programmer hunting for vulnerable code. Is the following code vulnerable? Explain your reasoning.
    
    ```cpp
    int i;
    unsigned int numWidgets;
    Widget **WidgetList;
    
    numWidgets = GetUntrustedSizeValue();
    if ((numWidgets == 0) || (numWidgets > MAX_NUM_WIDGETS)) {
        ExitError("Incorrect number of widgets requested!");
    }
    WidgetList = (Widget **) malloc(numWidgets * sizeof(Widget *));
    printf("WidgetList ptr=%p
    ", WidgetList);
    for (i = 0; i < numWidgets; i++) {
        WidgetList[i] = InitializeWidget();
    }
    WidgetList[numWidgets] = NULL;
    showWidgets(WidgetList);
    ```
    <end_of_turn>
    <start_of_turn>model
    Yes, the code is vulnerable to a memory access error.
    
    **Reasoning:**
    
    * The code allocates memory for `WidgetList` using `malloc` based on the value of `numWidgets`.
    * However, the loop iterates from `0` to `numWidgets`, which is one element beyond the allocated memory.
    * This means that accessing `WidgetList[numWidgets]` will result in a memory access error, as it is outside the bounds of the allocated memory.
    
    **Example of Memory Access Error:**
    
    When `numWidgets` is 5, the code allocates memory for `WidgetList` as follows:
    
    ```
    WidgetList = (Widget **) malloc(5 * sizeof(Widget *));
    ```
    
    The loop iterates from 0 to 4, accessing the following elements:
    
    * `WidgetList[0]`
    * `WidgetList[1]`
    * `WidgetList[2]`
    * `WidgetList[3]`
    * `WidgetList[4]`
    
    However, the code then attempts to access `WidgetList[5]`, which is outside the allocated memory range. This will result in a memory access error.
    
    **Solution:**
    
    To resolve this vulnerability, the loop should be modified to iterate from 0 to `numWidgets - 1`:
    
    ```cpp
    for (i = 0; i < numWidgets - 1; i++) {
        WidgetList[i] = InitializeWidget();
    }
    ```
    
    This ensures that the loop does not access elements beyond the allocated memory range.
    

The model detects a potential vulnerability in the code and provides code changes to mitigate it.

## Summary

This tutorial walked you through using CodeGemma for a variety of coding tasks. To learn more about CodeGemma:

  * Refer to the [CodeGemma model card](https://ai.google.dev/gemma/docs/codegemma/model_card) for the technical specs of the CodeGemma models.
  * Learn more about how to use CodeGemma in VertexAI [here](https://colab.sandbox.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_codegemma_deployment_on_vertex.ipynb).
  * Check out the [Keras CodeGemma quickstart](https://ai.google.dev/gemma/docs/codegemma/keras_quickstart).


