---
url: https://ai.google.dev/gemma/docs/integrations/mlx/
title: Run Gemma with MLX
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:54.797425+00:00
---

# Run Gemma with MLX

> Source: https://ai.google.dev/gemma/docs/integrations/mlx/

MLX is an array framework for machine learning on Apple silicon.

## Quick start

[Install](https://ml-explore.github.io/mlx/build/html/install.html) from the Python Package Index (PyPI)
    
    
    pip install mlx mlx-lm mlx-vlm
    

Example command:
    
    
    # Text Generation
    mlx_lm.generate --model mlx-community/gemma-4-e2b-it-4bit --prompt "Who are you?"
    
    # Vision Task
    mlx_vlm.generate --model mlx-community/gemma-4-e2b-it-4bit --prompt "Describe this image." --image <path_to_image>
    

You can start the server with:
    
    
    mlx_vlm.server --port 8080
    
    # Preload a model at startup (Hugging Face repo or local path)
    mlx_vlm.server --model mlx-community/gemma-4-e2b-it-4bit
    

This creates a server that lets you access your model with the OpenAI-compatible endpoint (`http://localhost:8080/v1`).

For more information and instructions on how to use MLX with Gemma, refer to the official repository:

  * [MLX on GitHub](https://github.com/ml-explore/mlx)
  * [MLX Community on Hugging Face](https://huggingface.co/mlx-community)


