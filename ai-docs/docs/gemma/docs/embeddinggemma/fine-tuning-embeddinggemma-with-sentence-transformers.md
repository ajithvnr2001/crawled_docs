---
url: https://ai.google.dev/gemma/docs/embeddinggemma/fine-tuning-embeddinggemma-with-sentence-transformers/
title: Fine-tune EmbeddingGemma 2 with Sentence Transformers
method: scrapling+scrapegraph
fetched_at: 2026-10-25T08:55:32.582806+00:00
---

# Fine-tune EmbeddingGemma 2 with Sentence Transformers

> Source: https://ai.google.dev/gemma/docs/embeddinggemma/fine-tuning-embeddinggemma-with-sentence-transformers/

[![](https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png)View on ai.google.dev](https://ai.google.dev/gemma/docs/embeddinggemma/fine-tuning-embeddinggemma-with-sentence-transformers) |  [![](https://www.tensorflow.org/images/colab_logo_32px.png)Run in Google Colab](https://colab.research.google.com/github/google-gemma/cookbook/blob/main/docs/embeddinggemma/fine-tuning-embeddinggemma-with-sentence-transformers.ipynb) |  [![](https://www.kaggle.com/static/images/logos/kaggle-logo-transparent-300.png)Run in Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/google-gemma/cookbook/blob/main/docs/embeddinggemma/fine-tuning-embeddinggemma-with-sentence-transformers.ipynb) |  [![](https://ai.google.dev/images/cloud-icon.svg)Open in Vertex AI](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2Fgoogle-gemma%2Fcookbook%2Fmain%2Fdocs%2Fembeddinggemma%2Ffine-tuning-embeddinggemma-with-sentence-transformers.ipynb) |  [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://github.com/google-gemma/cookbook/blob/main/docs/embeddinggemma/fine-tuning-embeddinggemma-with-sentence-transformers.ipynb) Fine-tuning helps close the gap between a model's general-purpose understanding and the specialized, high-performance accuracy that your application requires. While **EmbeddingGemma 2** provides strong out-of-the-box semantic representations across text and multimodal inputs, domain-specific terminology often benefits from targeted adaptation.

### Example Scenario: Financial Knowledge Base Search

Imagine your company, "Shibuya Financial", offers various complex financial products like investment trusts, **NISA accounts** (Japanese tax-advantaged savings accounts), and home loans. Customer support agents rely on an internal semantic search engine to retrieve relevant policy documents for customer inquiries. Without fine-tuning, general-purpose embeddings may struggle to separate closely related financial concepts, for example, confusing a query about a _tax-free investment account_ (NISA) with a _regular savings account_. **What this guide covers:**

  * Installing dependencies and loading **EmbeddingGemma 2** (`google/embeddinggemma-2`)
  * Evaluating baseline retrieval performance before fine-tuning
  * Preparing contrastive `(anchor, positive, negative)` training triplets
  * Fine-tuning the model using `SentenceTransformerTrainer` and `MultipleNegativesRankingLoss`
  * Evaluating post-training improvements and saving your adapted model



## Setup and Installation

Install `sentence-transformers`, `transformers`, and the multimedia libraries (`pillow`, `soundfile`, `torchcodec`) required for processing images, audio, and video. Sentence Transformers is a Python framework for using and training embedding and reranker models. For more details on the framework, see the [Sentence Transformers documentation](https://www.sbert.net/).
    
    
    pip install -U sentence-transformers transformers

## (Optional) Hugging Face Authenticatoin

You need a valid Hugging Face Token to publish your model. If you are running inside a Google Colab, you can securely use your Hugging Face Token using the Colab secrets otherwise you can set the token as directly in the login method. Make sure your token has write access too, as you push your model to the Hub during training.
    
    
    # Login into Hugging Face Hub
    from huggingface_hub import login
    login()
    

## Load the Base Model

Load `google/embeddinggemma-2` using `SentenceTransformer`.

> **Tip:** If you are fine-tuning exclusively on text data and want to minimize GPU memory usage, you can pass `config_kwargs={"vision_config": None, "audio_config": None}` during initialization to omit the vision and audio encoders.
    
    
    from sentence_transformers import SentenceTransformer
    
    model_id = "google/embeddinggemma-2"
    model = SentenceTransformer(
        model_id,
        config_kwargs={"vision_config": None, "audio_config": None},
    )
    
    print(f"Device: {model.device}")
    print(f"dtype: {model.dtype}")
    print(model)
    print("Total number of parameters in the model:", sum([p.numel() for _, p in model.named_parameters()]))
    
    
    
    Loading weights:   0%|          | 0/413 [00:00<?, ?it/s]
    Device: cuda:0
    dtype: torch.bfloat16
    SentenceTransformer(
      (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'image': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'audio': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'video': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'message': {'method': 'forward', 'method_output_name': 'last_hidden_state', 'format': 'structured'} }, 'module_output_name': 'token_embeddings', 'architecture': 'EmbeddingGemma2Model'})
      (1): Pooling({'embedding_dimension': 768, 'pooling_mode': 'mean', 'include_prompt': True})
      (2): Normalize({'module_input_name': 'sentence_embedding', 'module_output_name': 'sentence_embedding'})
    )
    Total number of parameters in the model: 271002624
    

## Baseline Evaluation (Before Fine-Tuning)

First, let's test how the base model ranks three candidate knowledge base documents when a customer asks:

> _"I want to start a tax-free installment investment, what should I do?"_

The correct match is **Opening a NISA Account** , since NISA is specifically a tax-free investment account.

> **Note on Task Prompts:** Always include task-specific prompts when encoding text with EmbeddingGemma 2. Here we use `prompt_name="STS"` (sentence similarity). For details on all available prompts, see the [EmbeddingGemma 2 model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2#best_practices).
    
    
    task_name = "STS"
    
    query = "I want to start a tax-free installment investment, what should I do?"
    documents = [
        "Opening a NISA Account",
        "Opening a Regular Savings Account",
        "Home Loan Application Guide",
    ]
    
    def evaluate_retrieval(query_text, docs):
        query_emb = model.encode(query_text, prompt_name=task_name)
        doc_embs = model.encode(docs, prompt_name=task_name)
        similarities = model.similarity(query_emb, doc_embs)[0]
    
        for doc, score in zip(docs, similarities):
            print(f"Document: {doc:<35} -> 🤖 Score: {score.item():.4f}")
    
    print("Baseline Scores (Before Fine-Tuning):")
    evaluate_retrieval(query, documents)
    
    
    
    Baseline Scores (Before Fine-Tuning):
    Document: Opening a NISA Account              -> 🤖 Score: 0.8552
    Document: Opening a Regular Savings Account   -> 🤖 Score: 0.8463
    Document: Home Loan Application Guide         -> 🤖 Score: 0.8078
    

## Prepare the Fine-Tuning Dataset

To teach the model domain-specific distinctions, we structure our training data as contrastive triplets: **`(anchor, positive, negative)`** :

  * **`anchor`** : The user query or reference sentence.
  * **`positive`** : A sentence that shares the exact domain intent (e.g., matching "NISA account" with "tax-free investment account").
  * **`negative`** : A hard negative sentence from the same domain that is semantically distinct (e.g., "regular savings account" or "investment trust fee").



> 
    from datasets import Dataset
    
    triplets = [
        [
            "How do I open a NISA account?",
            "What is the procedure for starting a new tax-free investment account?",
            "I want to check the balance of my regular savings account.",
        ],
        [
            "Are there fees for making an early repayment on a home loan?",
            "If I pay back my house loan early, will there be any costs?",
            "What is the management fee for this investment trust?",
        ],
        [
            "What is the coverage for medical insurance?",
            "Tell me about the benefits of the health insurance plan.",
            "What is the cancellation policy for my life insurance?",
        ],
    ]
    
    # Convert into a Hugging Face Dataset with 'anchor', 'positive', and 'negative' columns
    data_as_dicts = [
        {"anchor": row[0], "positive": row[1], "negative": row[2]}
        for row in triplets
    ]
    train_dataset = Dataset.from_list(data_as_dicts)
    print(train_dataset)
    
    
    
    Dataset({
        features: ['anchor', 'positive', 'negative'],
        num_rows: 3
    })
    

## Fine-Tuning the Model

We fine-tune the model using `SentenceTransformerTrainer` and **`MultipleNegativesRankingLoss`** , which pulls `(anchor, positive)` pairs closer together in vector space while pushing `(anchor, negative)` pairs (and all other in-batch negatives) apart. Crucially, we pass `prompts=model.prompts[task_name]` in `SentenceTransformerTrainingArguments` so the model is trained using the exact same task prefix used during inference.
    
    
    from sentence_transformers import (
        SentenceTransformerTrainer,
        SentenceTransformerTrainingArguments,
    )
    from sentence_transformers.losses import MultipleNegativesRankingLoss
    from transformers import TrainerCallback
    
    # Initialize contrastive ranking loss
    loss = MultipleNegativesRankingLoss(model)
    
    # Configure training arguments
    args = SentenceTransformerTrainingArguments(
        output_dir="my-embeddinggemma-2",
        prompts=model.prompts[task_name],  # Train with the target task prompt prefix
        num_train_epochs=5,
        per_device_train_batch_size=1,
        learning_rate=2e-5,
        warmup_steps=0.1,                  # 10% warmup ratio
        logging_steps=train_dataset.num_rows,
        report_to="none",
    )
    
    class EvaluationCallback(TrainerCallback):
        """Callback that evaluates retrieval scores at each logging step."""
    
        def __init__(self, eval_fn):
            self.eval_fn = eval_fn
    
        def on_log(self, args, state, control, **kwargs):
            print(f"\n--- Step {state.global_step} Evaluation ---")
            self.eval_fn()
    
    trainer = SentenceTransformerTrainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        loss=loss,
        callbacks=[EvaluationCallback(lambda: evaluate_retrieval(query, documents))],
    )
    
    trainer.train()
    
    
    
    /tmp/ipykernel_2017/3116461683.py:5: DeprecationWarning: Importing from 'sentence_transformers.losses' is deprecated and will be removed in a future version. Please use 'sentence_transformers.sentence_transformer.losses' instead.
      from sentence_transformers.losses import MultipleNegativesRankingLoss
    Computing widget examples:   0%|          | 0/1 [00:00<?, ?example/s]
    
    
    
    --- Step 3 Evaluation ---
    Document: Opening a NISA Account              -> 🤖 Score: 0.8502
    Document: Opening a Regular Savings Account   -> 🤖 Score: 0.8348
    Document: Home Loan Application Guide         -> 🤖 Score: 0.7903
    
    --- Step 6 Evaluation ---
    Document: Opening a NISA Account              -> 🤖 Score: 0.8316
    Document: Opening a Regular Savings Account   -> 🤖 Score: 0.8050
    Document: Home Loan Application Guide         -> 🤖 Score: 0.7470
    
    --- Step 9 Evaluation ---
    Document: Opening a NISA Account              -> 🤖 Score: 0.8194
    Document: Opening a Regular Savings Account   -> 🤖 Score: 0.7886
    Document: Home Loan Application Guide         -> 🤖 Score: 0.7239
    
    --- Step 12 Evaluation ---
    Document: Opening a NISA Account              -> 🤖 Score: 0.8153
    Document: Opening a Regular Savings Account   -> 🤖 Score: 0.7821
    Document: Home Loan Application Guide         -> 🤖 Score: 0.7148
    
    --- Step 15 Evaluation ---
    Document: Opening a NISA Account              -> 🤖 Score: 0.8139
    Document: Opening a Regular Savings Account   -> 🤖 Score: 0.7808
    Document: Home Loan Application Guide         -> 🤖 Score: 0.7128
    Writing model shards:   0%|          | 0/1 [00:00<?, ?it/s]
    --- Step 15 Evaluation ---
    Document: Opening a NISA Account              -> 🤖 Score: 0.8139
    Document: Opening a Regular Savings Account   -> 🤖 Score: 0.7808
    Document: Home Loan Application Guide         -> 🤖 Score: 0.7128
    TrainOutput(global_step=15, training_loss=0.038343556722005206, metrics={'train_runtime': 32.0074, 'train_samples_per_second': 0.469, 'train_steps_per_second': 0.469, 'total_flos': 0.0, 'train_loss': 0.038343556722005206, 'epoch': 5.0})
    

## Evaluation After Fine-Tuning

Let's run our test query once more on the fine-tuned model and compare the results against our baseline:
    
    
    print("Post-Training Scores (After Fine-Tuning):")
    evaluate_retrieval(query, documents)
    
    
    
    Post-Training Scores (After Fine-Tuning):
    Document: Opening a NISA Account              -> 🤖 Score: 0.8139
    Document: Opening a Regular Savings Account   -> 🤖 Score: 0.7808
    Document: Home Loan Application Guide         -> 🤖 Score: 0.7128
    

### Results Comparison

| Candidate Document | Relevance | Score (Before) | Score (After) | Separation Margin vs. Top Hit  
---|---|---|---|---  
**Opening a NISA Account** | **Target Match** | `0.8552` | `0.8139` | —  
**Opening a Regular Savings Account** | Hard Negative | `0.8463` | `0.7808` | **+0.0331** _(3.7x wider than 0.0089)_  
**Home Loan Application Guide** | Unrelated Distractor | `0.8078` | `0.7128` | **+0.1011** _(2.1x wider than 0.0474)_  
  
Even with just a few training steps, fine-tuning significantly increased the margin between the true match (**Opening a NISA Account**) and competing financial documents, making downstream search and RAG pipelines much more reliable.

## Saving and Sharing Your Model

Save your fine-tuned model locally so it can be reloaded directly with `SentenceTransformer`:
    
    
    # Save locally
    model.save_pretrained("my-embeddinggemma-2-finetuned")
    

To share your adapted model with your team or deploy it from the Hugging Face Hub, use `push_to_hub`:
    
    
    # Optional: Push your fine-tuned model to the Hugging Face Hub
    model.push_to_hub("my-embeddinggemma-2-finetuned")
    

## Summary and next steps

You have learned how to adapt **EmbeddingGemma 2** to specialized domain terminology using contrastive triplet fine-tuning with the Sentence Transformers library.

Explore what more you can do with EmbeddingGemma:

  * [Sentence Transformers Training Overview](https://sbert.net/docs/sentence_transformer/training_overview.html)
  * [Multimodal Embeddings with EmbeddingGemma 2](https://ai.google.dev/gemma/docs/embeddinggemma/inference-embeddinggemma-with-sentence-transformers)
  * [Simple RAG with EmbeddingGemma in the Gemma Cookbook](https://github.com/google-gemma/cookbook/blob/main/tutorials/RAG_with_EmbeddingGemma.ipynb)


