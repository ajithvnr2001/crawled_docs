---
url: https://ai.google.dev/gemma/docs/paligemma/
title: PaliGemma
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:58.052964+00:00
---

# PaliGemma

> Source: https://ai.google.dev/gemma/docs/paligemma/

##  PaliGemma 

PaliGemma 2 and PaliGemma are lightweight open _vision-language models_ (VLM) inspired by [PaLI-3](https://arxiv.org/abs/2310.09199), and based on open components like the [SigLIP vision model](https://arxiv.org/abs/2303.15343) and the [Gemma language model](https://arxiv.org/abs/2403.08295). PaliGemma takes both images and text as inputs and can answer questions about images with detail and context, meaning that PaliGemma can perform deeper analysis of images and provide useful insights, such as captioning for images and short videos, object detection, and reading text embedded within images. 

PaliGemma 2 is available in 3B, 10B, and 28B parameter sizes, which are based on Gemma 2 2B, 9B, and 27B models, respectively. The original PaliGemma models are available in the 3B size. For more information on Gemma model variants, see the [Gemma models list](https://ai.google.dev/gemma/docs/get_started#models-list). PaliGemma model variants support different pixel resolutions for image inputs, including 224 x 224, 448 x 448, and 896 x 896 pixels. 

You can view and download PaliGemma models from the follow sites: 

  * Download from [Kaggle](https://www.kaggle.com/models?query=paligemma). 
  * Download from [Hugging Face](https://huggingface.co/models?search=google/paligemma). 



There are three categories of PaliGemma models: 

  * **PaliGemma PT** \- General purpose pre-trained models that can be fine-tuned on a variety of tasks. 
  * **PaliGemma FT** \- Research-oriented models that are fine-tuned on specific research datasets. 
  * **PaliGemma mix** \- Models tuned to a mixture of tasks that can be used out-of-the-box for common use cases. 



Key benefits include: 

  * multiple_stop 

####  Multimodal capability 

Simultaneously handles both images and text input. 

  * build 

####  Versatile base model 

Can be fine-tuned on a wide range of vision-language tasks. 

  * explore 

####  Off-the-shelf exploration 

Comes with a checkpoint fine-tuned on a mixture of tasks for immediate research use. 




##  Learn more 

###  [ Run in Colab ](https://ai.google.dev/gemma/docs/paligemma/inference-with-keras)

Try detection and content generation capabilities with PaliGemma in Colab. 

###  [ Tune in Colab ](https://ai.google.dev/gemma/docs/paligemma/fine-tuning-paligemma)

Fine-tune a PaliGemma model with image data using JAX in Colab. 

###  [ View on Kaggle ](https://www.kaggle.com/models/google/paligemma-2)

View more code, Colab notebooks, information, and discussions about PaliGemma on Kaggle. 
