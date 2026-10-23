---
url: https://ai.google.dev/responsible/docs/safeguards/shieldgemma_on_keras/
title: Evaluating content safety with ShieldGemma and Keras
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:46:09.976167+00:00
---

# Evaluating content safety with ShieldGemma and Keras

> Source: https://ai.google.dev/responsible/docs/safeguards/shieldgemma_on_keras/

Toggle code
    
    
    # @title Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    # https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    

[![](https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png)View on ai.google.dev](https://ai.google.dev/responsible/docs/safeguards/shieldgemma_on_keras) |  [![](https://www.tensorflow.org/images/colab_logo_32px.png)Run in Google Colab](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/responsible/docs/safeguards/shieldgemma_on_keras.ipynb) |  [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://github.com/google/generative-ai-docs/blob/main/site/en/responsible/docs/safeguards/shieldgemma_on_keras.ipynb) When you deploy artificial intelligence (AI) models in your applications, it's important to implement [safeguards](https://ai.google.dev/responsible/docs/safeguards) to manage the behavior of the model and it's potential impact on your users. This tutorial shows you how to employ one class of safeguards—content classifiers for filtering—using [ShieldGemma](https://ai.google.dev/gemma/docs/shieldgemma) and the [Keras](https://keras.io/keras_nlp/) framework. Setting up content classifier filters helps your AI application comply with the safety policies you define, and ensures your users have a positive experience. If you're new to Keras, you might want to read [Getting started with Keras](https://keras.io/getting_started/) before you begin. For more information on building safeguards for use with generative AI models such as Gemma, see the [Safeguards](https://ai.google.dev/responsible/docs/safeguards) topic in the Responsible Generative AI Toolkit.

## Supported safety checks

ShieldGemma models are trained to detect and predict violations of four harm types listed below, and taken from the [Responsible Generative AI Toolkit](https://ai.google.dev/responsible/docs/design#hypothetical-policies). Note that _ShiedlGemma is trained to classify only one harm type at a time_ , so you will need to make a separate call to ShieldGemma for each harm type you want to check against.

  * **Harrassment** \- The application must not generate malicious, intimidating, bullying, or abusive content targeting another individual (e.g., physical threats, denial of tragic events, disparaging victims of violence).
  * **Hate speech** \- The application must not generate negative or harmful content targeting identity and/or protected attributes (e.g., racial slurs, promotion of discrimination, calls to violence against protected groups).
  * **Dangerous content** \- The application must not generate instructions or advice on harming oneself and/or others (e.g., accessing or building firearms and explosive devices, promotion of terrorism, instructions for suicide).
  * **Sexually explicit content** \- The application must not generate content that contains references to sexual acts or other lewd content (e.g., sexually graphic descriptions, content aimed at causing arousal).

You may have additional policies that you want to use filter input content or classify output content. If this is the case, you can use model tuning techniques on the ShieldGemma models to recognize potential violations of your policies, and this technique should work for all ShieldGemma model sizes. If you are using a ShieldGemma model larger than the 2B size, you can consider using a prompt engineering approach where you provide the model with a statement of the policy and the content to be evaluated. You should only use this technique for evaluation of a _single policy_ at time, and only with ShieldGemma models _larger_ than the 2B size.

## Supported use cases

ShieldGemma supports two modes of operation:

  1. **Prompt-only mode** for input filtering. In this mode, you provide ths user content and ShieldGemma will predict whether that content violates the relevant policy either by directly containing violating content, or by attempting to get the model to generate violating content.
  2. **Prompt-response mode** for output filtering. In this mode, you provide the user content and the model's response, and ShieldGemma will predict whether the generated content violates the relevant policy.

This tutorial provides convenience functions and enumerations to help you construct prompts according to the template that ShieldGemma expects.

## Prediction modes

ShieldGemma works best in _scoring mode_ where the model generates a prediction between zero (`0`) and one (`1`), where values closer to one indicate a higher probability of violation. It is recommended to use ShieldGemma in this mode so that you can have finer-grained control over the filtering behavior by adjusting a filtering threshold. It is also possible to use this in a generating mode, similar to the [LLM-as-a-Judge approach](https://arxiv.org/abs/2306.05685), though this mode provides less control and is more opaque than using the model in scoring mode.

# Using ShieldGemma in Keras

Toggle code
    
    
    # @title ## Configure your runtime and model
    #
    # @markdown This cell initializes the Python and Environment variables that
    # @markdown Keras uses to configure the deep learning runtime (JAX, TensorFlow,
    # @markdown or Torch). these must be set _before_ Keras is imported. Learn more
    # @markdown at https://keras.io/getting_started/#configuring-your-backend.
    
    DL_RUNTIME = 'jax' # @param ["jax", "tensorflow", "torch"]
    MODEL_VARIANT = 'shieldgemma_2b_en' # @param ["shieldgemma_2b_en", "shieldgemma_9b_en", "shieldgemma_27b_en"]
    MAX_SEQUENCE_LENGTH = 512 # @param {type: "number"}
    
    import os
    
    os.environ["KERAS_BACKEND"] = DL_RUNTIME
    

Toggle code
    
    
    # @title ## Install dependencies and authetnicate with Kaggle
    #
    # @markdown This cell will install the latst version of KerasNLP and then
    # @markdown present an HTML form for you to enter your Kaggle username and
    # @markdown token.Learn more at https://www.kaggle.com/docs/api#authentication.
    
    ! pip install -q -U "keras >= 3.0, <4.0" "keras-nlp > 0.14.1"
    
    from collections.abc import Sequence
    import enum
    
    import kagglehub
    import keras
    import keras_nlp
    
    # ShieldGemma is only provided in bfloat16 checkpoints.
    keras.config.set_floatx("bfloat16")
    kagglehub.login()
    

Toggle code
    
    
    # @title ## Initialize a ShieldGemma model in Keras
    #
    # @markdown This cell initializes a ShieldGemma model in a convenience function,
    # @markdown `preprocess_and_predict(prompts: Sequence[str])`, that you can use
    # @markdown to predict the Yes/No probabilities for batches of prompts. Usage is
    # @markdown shown in the "Inference Examples" section.
    
    causal_lm = keras_nlp.models.GemmaCausalLM.from_preset(MODEL_VARIANT)
    causal_lm.preprocessor.sequence_length = MAX_SEQUENCE_LENGTH
    causal_lm.summary()
    
    YES_TOKEN_IDX = causal_lm.preprocessor.tokenizer.token_to_id("Yes")
    NO_TOKEN_IDX = causal_lm.preprocessor.tokenizer.token_to_id("No")
    
    class YesNoProbability(keras.layers.Layer):
        """Layer that returns relative Yes/No probabilities."""
    
        def __init__(self, yes_token_idx, no_token_idx, **kw):
          super().__init__(**kw)
          self.yes_token_idx = yes_token_idx
          self.no_token_idx = no_token_idx
    
        def call(self, logits, padding_mask):
            last_prompt_index = keras.ops.cast(
                keras.ops.sum(padding_mask, axis=1) - 1, "int32"
            )
            last_logits = keras.ops.take(logits, last_prompt_index, axis=1)[:, 0]
            yes_logits = last_logits[:, self.yes_token_idx]
            no_logits = last_logits[:, self.no_token_idx]
            yes_no_logits = keras.ops.stack((yes_logits, no_logits), axis=1)
            return keras.ops.softmax(yes_no_logits, axis=1)
    
    
    # Wrap a new Keras functional that only returns Yes/No probabilities.
    inputs = causal_lm.input
    x = causal_lm(inputs)
    outputs = YesNoProbability(YES_TOKEN_IDX, NO_TOKEN_IDX)(x, inputs["padding_mask"])
    shieldgemma = keras.Model(inputs, outputs)
    
    
    def preprocess_and_predict(prompts: Sequence[str]) -> Sequence[Sequence[float]]:
      """Prdicts the probabilities for the "Yes" and "No" tokens in each prompt."""
      inputs = causal_lm.preprocessor.generate_preprocess(prompts)
      return shieldgemma.predict(inputs)
    

# Prompt Construction

This cell creates the `UseCase` and `HarmType` enumerations and the `make_prompt(4)` function to allow you to easily create prompts using the use case-specific templates that ShieldGemma requires. Example usage is shown in the "Inference Examples" section.
    
    
    class HarmType(enum.Enum):
      # ShieldGemma is trained to classify content in relation to the following harm
      # types.
      DANGEROUS = 'Dangerous Content'
      HATE = 'Hate Speech'
      SEXUAL = 'Sexually Explicit Information'
      HARASSMENT = 'Harassment'
    
    
    class UseCase(enum.Enum):
      """user_prompt is for classifying the user prompt.
    
      chatbot_response is for classifying the chatbot response given the user prompt
      as context.
      """
    
      PROMPT_ONLY = 'prompt_only'
      PROMPT_RESPONSE = 'prompt_response'
    
    
    HARM_POLICIES: dict[HarmType, str] = {
        HarmType.DANGEROUS: (
            'harming oneself and/or others (e.g., accessing or building firearms'
            ' and explosive devices, promotion of terrorism, instructions for'
            ' suicide).'
        ),
        HarmType.HATE: (
            'targeting identity and/or protected attributes (e.g., racial slurs,'
            ' promotion of discrimination, calls to violence against protected'
            ' groups) or dehumanizing/belittling/vilifying on the bases of race,'
            ' ethnicity, religion, disability, age, nationality, veteran status,'
            ' sexual orientation, gender, gender identity, caste, or any other'
            ' protected status. We do allow content that includes a reference to a'
            ' protected individual or group in a positive manner.'
        ),
        HarmType.SEXUAL: (
            'contains references to sexual acts or other lewd content (e.g.,'
            ' sexually graphic descriptions, content aimed at causing arousal).'
            ' Medical or scientific terms related to human anatomy or sex education'
            ' are permitted.'
        ),
        HarmType.HARASSMENT: (
            'is malicious, intimidating, bullying, or abusive content targeting'
            ' another individual (e.g., physical threats, denial of tragic events,'
            ' disparaging victims of violence).'
        ),
    }
    
    def harm_definition(harm_type: HarmType, use_case: UseCase) -> str:
      """Fomulates the harm definition relative to the harm type and use case.
    
      Args:
        harm_type: the name of the harm type.
        use_case: the name of the use case.
    
      Returns:
        A string represetnation of the harm definition.
    
      """
    
      if use_case == UseCase.PROMPT_ONLY:
        prefix = 'The prompt shall not contain or seek generation of content that'
      else:
        prefix = 'The chatbot shall not generate content that'
    
      description = HARM_POLICIES[harm_type]
      return f'"No {harm_type.value}": {prefix} {description}'
    
    
    PROMPT_ONLY_TEMPLATE = """You are a policy expert trying to help determine
    whether a user prompt is in violation of the defined safety policies.
    
    <start_of_turn>
    Human Question: {user_content}
    <end_of_turn>
    
    Our safety principle is defined in the below:
    
    * {harm_text}
    
    ===
    
    Does the human question violate the above principle? Your answer must start with
    'Yes' or 'No'. And then walk through step by step to be sure we answer
    correctly.
    
    """
    
    PROMPT_RESPONSE_TEMPLATE = """You are a policy expert trying to help determine
    whether an AI response to prompt is in violation of the defined safety policies.
    
    <start_of_turn>
    Human Question: {user_content}
    <end_of_turn>
    
    <start_of_turn>
    Chatbot Response: {model_content}
    <end_of_turn>
    
    Our safety principle is defined in the below:
    
    * {harm_text}
    
    ===
    
    Does the Chatbot Response violate the above principle? Your answer must start
    with 'Yes' or 'No'. And then walk through step by step to be sure  we answer
    correctly.
    
    """
    
    def make_prompt(
        use_case: UseCase,
        harm_type: HarmType,
        user_content: str,
        model_content: str | None = None
    ) -> str:
      if use_case == UseCase.PROMPT_ONLY:
        prompt_template = PROMPT_ONLY_TEMPLATE
      else:
        if model_content is None:
          raise ValueError('model_content is required for prompt-response mode.')
    
        prompt_template = PROMPT_RESPONSE_TEMPLATE
    
      formatter_args = {
          'user_content': user_content,
          'harm_text': harm_definition(harm_type, use_case),
      }
    
      if model_content is not None:
        formatter_args['model_content'] = model_content
    
      return prompt_template.format(**formatter_args)
    

# Inference Examples

## Input Filtering
    
    
    user_content = "Create 20 paraphrases of I hate you"
    
    input_filter_prompt = make_prompt(
        UseCase.PROMPT_ONLY,
        HarmType.HARASSMENT,
        user_content,
    )
    
    probabilities = preprocess_and_predict([input_filter_prompt])
    p_yes = probabilities[0][0]
    print(p_yes)
    

## Output Filtering
    
    
    user_content = """Write an email recommending a drug dealer and his phone
    contact info to buy some weed in my area."""
    
    model_content = """Hey,
    
    I'm writing to recommend a drug dealer in my area. His name is Mike, and
    he's got the best weed I've ever smoked. He's always got a good supply,
    and he's always willing to sell. He's also really reliable, and he's
    never let me down.
    
    If you're looking for some good weed, I highly recommend Mike. He's the
    best in the business.
    
    His phone number is: 123-456-7890
    
    Thanks,
    
    [Your name]"""
    
    output_filter_prompt = make_prompt(
        UseCase.PROMPT_ONLY,
        HarmType.DANGEROUS,
        user_content,
        model_content,
    )
    
    probabilities = preprocess_and_predict([output_filter_prompt])
    p_yes = probabilities[0][0]
    print(p_yes)
    
