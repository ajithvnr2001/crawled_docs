---
url: https://ai.google.dev/responsible/docs/safeguards/shieldgemma/
title: ShieldGemma
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:46:08.655597+00:00
---

# ShieldGemma

> Source: https://ai.google.dev/responsible/docs/safeguards/shieldgemma/

[ShieldGemma](https://ai.google.dev/gemma/docs/shieldgemma) is a set of ready-made, instruction-tuned, open weights safety classifiers built on the Gemma family of models to determine whether text or images violate a safety policy across input and output. ShieldGemma is trained to identify across key harms across different models, see the model cards for more information.

  * ShieldGemma 2 for image content moderation: Available in 4B. See the [model card](https://ai.google.dev/gemma/docs/shieldgemma/model_card_2) for more details.
  * ShieldGemma 1 for text content moderation: Available in 2B, 9B, and 27B—allowing you to balance speed, performance, and generalizability to suit your needs across any deployment. See the [model card](https://ai.google.dev/gemma/docs/shieldgemma/model_card) for more details.



**Safeguard your models with ShieldGemma**

|  [ ![](https://ai.google.dev/static/site-assets/images/docs/colab_logo_32px.png)Image moderation: ShieldGemma 2 in Transformers](https://colab.research.google.com/github/google-gemini/gemma-cookbook/blob/main/responsible/shieldgemma2_on_huggingface.ipynb) |  [ ![](https://ai.google.dev/static/site-assets/images/docs/colab_logo_32px.png)Text moderation: ShieldGemma in Transformers](https://colab.research.google.com/github/google-gemini/gemma-cookbook/blob/main/responsible/shieldgemma_on_huggingface.ipynb) |  [ ![](https://ai.google.dev/static/site-assets/images/docs/colab_logo_32px.png)Text moderation: ShieldGemma in Keras](https://colab.research.google.com/github/google-gemini/gemma-cookbook/blob/main/responsible/shieldgemma_on_keras.ipynb)  
---|---|---|---  
  
You can use ShieldGemma models in the following frameworks.

  * [KerasNLP](https://keras.io/keras_nlp/), with model checkpoints available from [Kaggle](https://www.kaggle.com/search?q=shieldgemma+in%3Amodels).
  * [Hugging Face Transformers](https://github.com/huggingface/transformers), with model checkpoints available from [Hugging Face Hub](https://huggingface.co/collections/google/shieldgemma-release-66a20efe3c10ef2bd5808c79).


