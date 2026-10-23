---
url: https://ai.google.dev/gemma/docs/codegemma/codegemma_flax_inference/
title: Inference with CodeGemma using JAX and Flax
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:36.798152+00:00
---

# Inference with CodeGemma using JAX and Flax

> Source: https://ai.google.dev/gemma/docs/codegemma/codegemma_flax_inference/

[![](https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png)View on ai.google.dev](https://ai.google.dev/gemma/docs/codegemma/codegemma_flax_inference) |  [![](https://www.tensorflow.org/images/colab_logo_32px.png)Run in Google Colab](https://colab.research.google.com/github/google-gemma/cookbook/blob/main/docs/codegemma/codegemma_flax_inference.ipynb) |  [![](https://www.kaggle.com/static/images/logos/kaggle-logo-transparent-300.png)Run in Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/google-gemma/cookbook/blob/main/docs/codegemma/codegemma_flax_inference.ipynb) |  [![](https://ai.google.dev/images/cloud-icon.svg)Open in Vertex AI](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2Fgoogle-gemma%2Fcookbook%2Fmain%2Fdocs%2Fcodegemma%2Fcodegemma_flax_inference.ipynb) |  [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://github.com/google-gemma/cookbook/blob/main/docs/codegemma/codegemma_flax_inference.ipynb) We present CodeGemma, a collection of open code models based on Google DeepMind’s Gemma models (Gemma Team et al., 2024). CodeGemma is a family of lightweight, state-of-the art open models built from the same research and technology used to create the Gemini models. Continuing from Gemma pretrained models, CodeGemma models are further trained on more than 500 to 1000 billion tokens of primarily code, using the same architectures as the Gemma model family. As a result, CodeGemma models achieve state of-the-art code performance in both completion and generation tasks, while maintaining strong understanding and reasoning skills at scale. CodeGemma has 3 variants:

  * A 7B code pretrained model
  * A 7B instruction-tuned code model
  * A 2B model, trained specifically for code infilling and open-ended generation.

This guide walks you through using the CodeGemma model with Flax for a code completion task.

## Setup

### 1\. Set up Kaggle access for CodeGemma

To complete this tutorial, you first need to follow the setup instructions at [Gemma setup](https://ai.google.dev/gemma/docs/setup), which show you how to do the following:

  * Get access to CodeGemma on [kaggle.com](https://www.kaggle.com/models/google/codegemma/).
  * Select a Colab runtime with sufficient resources (**T4 GPU has insufficient memory, use TPU v2 instead**) to run the CodeGemma model.
  * Generate and configure a Kaggle username and API key.

After you've completed the Gemma setup, move on to the next section, where you'll set environment variables for your Colab environment.

### 2\. Set environment variables

Set environment variables for `KAGGLE_USERNAME` and `KAGGLE_KEY`. When prompted with the "Grant access?" messages, agree to provide secret access.
    
    
    import os
    from google.colab import userdata # `userdata` is a Colab API.
    
    os.environ["KAGGLE_USERNAME"] = userdata.get('KAGGLE_USERNAME')
    os.environ["KAGGLE_KEY"] = userdata.get('KAGGLE_KEY')
    

### 3\. Install the `gemma` library

Free Colab hardware acceleration is currently _insufficient_ to run this notebook. If you are using [Colab Pay As You Go or Colab Pro](https://colab.research.google.com/signup), click on **Edit** > **Notebook settings** > Select **A100 GPU** > **Save** to enable hardware acceleration. Next, you need to install the Google DeepMind `gemma` library from [`github.com/google-deepmind/gemma`](https://github.com/google-deepmind/gemma). If you get an error about "pip's dependency resolver", you can usually ignore it.
    
    
    pip install -q git+https://github.com/google-deepmind/gemma.git

### 4\. Import libraries

This notebook uses [Gemma](https://github.com/google-deepmind/gemma) (which uses [Flax](https://flax.readthedocs.io) to build its neural network layers), and [SentencePiece](https://github.com/google/sentencepiece) (for tokenization).
    
    
    import os
    from gemma import params as params_lib
    from gemma import sampler as sampler_lib
    from gemma import transformer as transformer_lib
    import sentencepiece as spm
    

## Load the CodeGemma model

Load the CodeGemma model with [`kagglehub.model_download`](https://github.com/Kaggle/kagglehub/blob/bddefc718182282882b72f814d407d89e5d178c4/src/kagglehub/models.py#L12), which takes three arguments:

  * `handle`: The model handle from Kaggle
  * `path`: (Optional string) The local path
  * `force_download`: (Optional boolean) Forces to re-download the model


    
    
    GEMMA_VARIANT = '2b-pt' # @param ['2b-pt', '7b-it', '7b-pt', '1.1-2b-pt', '1.1-7b-it'] {type:"string"}
    
    
    
    import kagglehub
    
    GEMMA_PATH = kagglehub.model_download(f'google/codegemma/flax/{GEMMA_VARIANT}')
    
    
    
    Warning: Looks like you're using an outdated `kagglehub` version, please consider updating (latest version: 0.2.7)
    Downloading from https://www.kaggle.com/api/v1/models/google/codegemma/flax/2b-pt/3/download...
    100%|██████████| 3.67G/3.67G [00:22<00:00, 173MB/s]
    Extracting model files...
    
    
    
    print('GEMMA_PATH:', GEMMA_PATH)
    
    
    
    GEMMA_PATH: /root/.cache/kagglehub/models/google/codegemma/flax/2b-pt/3
    

Check the location of the model weights and the tokenizer, then set the path variables. The tokenizer directory will be in the main directory where you downloaded the model, while the model weights will be in a sub-directory. For example:

  * The `spm.model` tokenizer file will be in `/LOCAL/PATH/TO/codegemma/flax/2b-pt/3`
  * The model checkpoint will be in `/LOCAL/PATH/TO/codegemma/flax/2b-pt/3/2b-pt`


    
    
    CKPT_PATH = os.path.join(GEMMA_PATH, GEMMA_VARIANT[-5:])
    TOKENIZER_PATH = os.path.join(GEMMA_PATH, 'spm.model')
    print('CKPT_PATH:', CKPT_PATH)
    print('TOKENIZER_PATH:', TOKENIZER_PATH)
    
    
    
    CKPT_PATH: /root/.cache/kagglehub/models/google/codegemma/flax/2b-pt/3/2b-pt
    TOKENIZER_PATH: /root/.cache/kagglehub/models/google/codegemma/flax/2b-pt/3/spm.model
    

## Perform sampling/inference

Load and format the CodeGemma model checkpoint with the [`gemma.params.load_and_format_params`](https://github.com/google-deepmind/gemma/blob/c6bd156c246530e1620a7c62de98542a377e3934/gemma/params.py#L27) method:
    
    
    params = params_lib.load_and_format_params(CKPT_PATH)
    

Load the CodeGemma tokenizer, constructed using [`sentencepiece.SentencePieceProcessor`](https://github.com/google/sentencepiece/blob/4d6a1f41069c4636c51a5590f7578a0dbed83450/python/src/sentencepiece/__init__.py#L423):
    
    
    vocab = spm.SentencePieceProcessor()
    vocab.Load(TOKENIZER_PATH)
    
    
    
    True
    

To automatically load the correct configuration from the CodeGemma model checkpoint, use [`gemma.transformer.TransformerConfig`](https://github.com/google-deepmind/gemma/blob/56e501ce147af4ea5c23cc0ddf5a9c4a6b7bd0d0/gemma/transformer.py#L65). The `cache_size` argument is the number of time steps in the CodeGemma `Transformer` cache. Afterwards, instantiate the CodeGemma model as `model_2b` with [`gemma.transformer.Transformer`](https://github.com/google-deepmind/gemma/blob/56e501ce147af4ea5c23cc0ddf5a9c4a6b7bd0d0/gemma/transformer.py#L136) (which inherits from [`flax.linen.Module`](https://flax.readthedocs.io/en/latest/api_reference/flax.linen/module.html)).
    
    
    transformer_config = transformer_lib.TransformerConfig.from_params(
        params,
        cache_size=1024
    )
    
    transformer = transformer_lib.Transformer(config=transformer_config)
    

Create a `sampler` with [`gemma.sampler.Sampler`](https://github.com/google-deepmind/gemma/blob/56e501ce147af4ea5c23cc0ddf5a9c4a6b7bd0d0/gemma/sampler.py#L88). It uses the CodeGemma model checkpoint and the tokenizer.
    
    
    sampler = sampler_lib.Sampler(
        transformer=transformer,
        vocab=vocab,
        params=params['transformer']
    )
    

Create some variables to represent the fill-in-the-middle (fim) tokens and create some helper functions to format the prompt and generated output. For example, let's look at the following code:
    
    
    def function(string):
    assert function('asdf') == 'fdsa'
    

We would like to fill in the `function` so that the assertion holds `True`. In this case, the prefix would be:
    
    
    "def function(string):\n"
    

And the suffix would be:
    
    
    "assert function('asdf') == 'fdsa'"
    

We then format this into a prompt as PREFIX-SUFFIX-MIDDLE (the middle section that needs to be filled is always at the end of the prompt):
    
    
    "<|fim_prefix|>def function(string):\n<|fim_suffix|>assert function('asdf') == 'fdsa'<|fim_middle|>"
    
    
    
    # In the context of a code editor,
    # the cursor is the location where the text will be inserted
    BEFORE_CURSOR = "<|fim_prefix|>"
    AFTER_CURSOR = "<|fim_suffix|>"
    AT_CURSOR = "<|fim_middle|>"
    FILE_SEPARATOR = "<|file_separator|>"
    
    def format_completion_prompt(before, after):
      print(f"\nORIGINAL PROMPT:\n{before}{after}")
      prompt = f"{BEFORE_CURSOR}{before}{AFTER_CURSOR}{after}{AT_CURSOR}"
      print(f"\nFORMATTED PROMPT:\n{repr(prompt)}")
      return prompt
    def format_generated_output(before, after, output):
      print(f"\nGENERATED OUTPUT:\n{repr(output)}")
      formatted_output = f"{before}{output.replace(FILE_SEPARATOR, '')}{after}"
      print(f"\nFILL-IN COMPLETION:\n{formatted_output}")
      return formatted_output
    

Create a prompt and perform inference. Specify the prefix `before` text and the suffix `after` text and generate the formatted prompt using the helper function `format_completion prompt`. You can tweak `total_generation_steps` (the number of steps performed when generating a response — this example uses `100` to preserve host memory).
    
    
    before = "def function(string):\n"
    after = "assert function('asdf') == 'fdsa'"
    prompt = format_completion_prompt(before, after)
    
    output = sampler(
        [prompt],
        total_generation_steps=100,
        ).text
    
    formatted_output = format_generated_output(before, after, output[0])
    
    
    
    ORIGINAL PROMPT:
    def function(string):
    assert function('asdf') == 'fdsa'
    
    FORMATTED PROMPT:
    "<|fim_prefix|>def function(string):\n<|fim_suffix|>assert function('asdf') == 'fdsa'<|fim_middle|>"
    
    GENERATED OUTPUT:
    '    return string[::-1]\n\n<|file_separator|>'
    
    FILL-IN COMPLETION:
    def function(string):
        return string[::-1]
    
    assert function('asdf') == 'fdsa'
    
    
    
    before = "import "
    after = """if __name__ == "__main__":\n    sys.exit(0)"""
    prompt = format_completion_prompt(before, after)
    
    output = sampler(
        [prompt],
        total_generation_steps=100,
        ).text
    
    formatted_output = format_generated_output(before, after, output[0])
    
    
    
    ORIGINAL PROMPT:
    import if __name__ == "__main__":
        sys.exit(0)
    
    FORMATTED PROMPT:
    '<|fim_prefix|>import <|fim_suffix|>if __name__ == "__main__":\n    sys.exit(0)<|fim_middle|>'
    
    GENERATED OUTPUT:
    'sys\n<|file_separator|>'
    
    FILL-IN COMPLETION:
    import sys
    if __name__ == "__main__":
        sys.exit(0)
    
    
    
    before = """import numpy as np
    def reflect(matrix):
      # horizontally reflect a matrix
    """
    after = ""
    prompt = format_completion_prompt(before, after)
    
    output = sampler(
        [prompt],
        total_generation_steps=100,
        ).text
    
    formatted_output = format_generated_output(before, after, output[0])
    
    
    
    ORIGINAL PROMPT:
    import numpy as np
    def reflect(matrix):
      # horizontally reflect a matrix
    
    
    FORMATTED PROMPT:
    '<|fim_prefix|>import numpy as np\ndef reflect(matrix):\n  # horizontally reflect a matrix\n<|fim_suffix|><|fim_middle|>'
    
    GENERATED OUTPUT:
    '  return np.flip(matrix, axis=1)\n<|file_separator|>'
    
    FILL-IN COMPLETION:
    import numpy as np
    def reflect(matrix):
      # horizontally reflect a matrix
      return np.flip(matrix, axis=1)
    

## Learn more

  * You can learn more about the Google DeepMind [`gemma` library on GitHub](https://github.com/google-deepmind/gemma), which contains docstrings of modules you used in this tutorial, such as [`gemma.params`](https://github.com/google-deepmind/gemma/blob/main/gemma/params.py), [`gemma.transformer`](https://github.com/google-deepmind/gemma/blob/main/gemma/transformer.py), and [`gemma.sampler`](https://github.com/google-deepmind/gemma/blob/main/gemma/sampler.py).
  * The following libraries have their own documentation sites: [core JAX](https://jax.readthedocs.io), [Flax](https://flax.readthedocs.io), and [Orbax](https://orbax.readthedocs.io/).
  * For `sentencepiece` tokenizer/detokenizer documentation, check out [Google's `sentencepiece` GitHub repo](https://github.com/google/sentencepiece).
  * For `kagglehub` documentation, check out `README.md` on [Kaggle's `kagglehub` GitHub repo](https://github.com/Kaggle/kagglehub).
  * Learn how to [use Gemma models with Google Cloud Vertex AI](https://cloud.google.com/vertex-ai/docs/generative-ai/open-models/use-gemma).
  * If you are using Google Cloud TPUs (v3-8 and newer), make sure to also update to the latest `jax[tpu]` package (`!pip install -U jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html`), restart the runtime, and check that `jax` and `jaxlib` versions match (`!pip list | grep jax`). This can prevent the `RuntimeError` that can arise because of the `jaxlib` and `jax` version mismatch. For more JAX installation instructions, refer to the [JAX docs](https://jax.readthedocs.io/en/latest/tutorials/installation.html#install-google-tpu).


