---
url: https://ai.google.dev/gemma/docs/embeddinggemma/
title: EmbeddingGemma
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:46.981203+00:00
---

# EmbeddingGemma

> Source: https://ai.google.dev/gemma/docs/embeddinggemma/

**EmbeddingGemma 2** is a lightweight, open-source 740M parameter model designed for unified multimodal embeddings. Built on the Gemma 4 decoder architecture, it maps **text, images, audio, and video** into a unified 768-dimensional vector space. You can run demanding cross-modal workflows (e.g. multimodal Retrieval-Augmented Generation (RAG), semantic search, and zero-shot classification) locally and offline on consumer GPUs or CPUs.

[Get it on Hugging Face](https://huggingface.co/collections/google/embeddinggemma-2)

EmbeddingGemma 2 is provided with open weights and licensed under the [Apache 2.0 License](https://ai.google.dev/gemma/apache_2), allowing you to fine-tune and deploy it in your own projects and applications.

[Try EmbeddingGemma 2](https://ai.google.dev/gemma/docs/embeddinggemma/inference-embeddinggemma-with-sentence-transformers) [Fine-tune EmbeddingGemma 2](https://ai.google.dev/gemma/docs/embeddinggemma/fine-tuning-embeddinggemma-with-sentence-transformers)

## Key features

EmbeddingGemma 2 introduces major improvements over EmbeddingGemma 1:

  * **Native Multimodality** : Unlocks zero-shot text, code, image, video, and audio search directly in a single unified vector space.
  * **Superior quality across text and code** : Outperforms EmbeddingGemma 1 on Code MTEB (Massive Text Embedding Benchmark).
  * **Smaller base footprint** : Reduces the base text and code model size from 300M parameters down to **270M parameters**.
  * **High storage efficiency** : Matryoshka Representation Learning (MRL) enables dynamic output truncation across **128, 256, 512, and 768 dimensions** , delivering up to a **6x reduction in vector database storage costs** with minimal quality degradation.
  * **Extended context length** : Supports up to **8,192 tokens** for text and source code across over 100 languages.



## Previous Versions

### EmbeddingGemma 1

EmbeddingGemma 1 is a 308M parameter multilingual text embedding model based on Gemma 3. It is optimized for use in everyday devices, such as phones, laptops, and tablets. The model produces numerical representations of text to be used for downstream tasks like information retrieval, semantic similarity search, classification, and clustering.

EmbeddingGemma 1 includes the following key features:

  * **Multilingual support** : Wide linguistic data understanding, trained in over 100 languages.
  * **Flexible output dimensions** : Customize your output dimensions from 768 to 128 for speed and storage tradeoffs using Matryoshka Representation Learning (MRL).
  * **2K token context** : Substantial input context for processing text data and documents directly on your hardware.
  * **Storage efficient** : Run it on less than 200MB of RAM with quantization.
  * **Low latency** : Generative embeddings in less than 22ms on EdgeTPU for fast and fluid applications.
  * **Offline and secure** : Generate embeddings of documents directly on your hardware, works without internet connection to keep sensitive data secure.


