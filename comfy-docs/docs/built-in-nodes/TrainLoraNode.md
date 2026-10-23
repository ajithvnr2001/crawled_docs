---
url: https://docs.comfy.org/built-in-nodes/TrainLoraNode/
title: TrainLoraNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:10.954025+00:00
---

# TrainLoraNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TrainLoraNode/

Training

# TrainLoraNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TrainLoraNode creates and trains a LoRA (Low-Rank Adaptation) model on a diffusion model using provided latents and conditioning data.

Copy pageCopy page

The TrainLoraNode creates and trains a LoRA (Low-Rank Adaptation) model on a diffusion model using provided latents and conditioning data. It allows you to fine-tune a model with custom training parameters, optimizers, and loss functions. The node outputs the trained LoRA weights, a loss history map, and the total training steps completed.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to train the LoRA on.| MODEL| Yes| -  
`latents`| The Latents to use for training, serve as dataset/input of the model.| LATENT| Yes| -  
`positive`| The positive conditioning to use for training.| CONDITIONING| Yes| -  
`batch_size`| The batch size to use for training (default: 1).| INT| Yes| 1-10000  
`grad_accumulation_steps`| The number of gradient accumulation steps to use for training (default: 1).| INT| Yes| 1-1024  
`steps`| The number of steps to train the LoRA for (default: 16).| INT| Yes| 1-100000  
`learning_rate`| The learning rate to use for training (default: 0.0005).| FLOAT| Yes| 0.0000001-1.0  
`rank`| The rank of the LoRA layers (default: 8).| INT| Yes| 1-128  
`optimizer`| The optimizer to use for training (default: “AdamW”).| COMBO| Yes| ”AdamW"  
"Adam"  
"SGD"  
"RMSprop”  
`loss_function`| The loss function to use for training (default: “MSE”).| COMBO| Yes| ”MSE"  
"L1"  
"Huber"  
"SmoothL1”  
`seed`| The seed to use for training (used in generator for LoRA weight initialization and noise sampling) (default: 0).| INT| Yes| 0-18446744073709551615  
`training_dtype`| The dtype to use for training. ‘none’ preserves the model’s native compute dtype instead of overriding it. For fp16 models, GradScaler is automatically enabled (default: “bf16”).| COMBO| Yes| ”bf16"  
"fp32"  
"none”  
`lora_dtype`| The dtype to use for lora (default: “bf16”).| COMBO| Yes| ”bf16"  
"fp32”  
`quantized_backward`| When using training_dtype ‘none’ and training on quantized model, doing backward with quantized matmul when enabled (default: False).| BOOLEAN| Yes| -  
`algorithm`| The algorithm to use for training.| COMBO| Yes| Multiple options available  
`gradient_checkpointing`| Use gradient checkpointing for training (default: True).| BOOLEAN| Yes| -  
`checkpoint_depth`| Depth level for gradient checkpointing (default: 1).| INT| Yes| 1-5  
`offloading`| Offload model weights to CPU during training to save GPU memory (default: False).| BOOLEAN| Yes| -  
`existing_lora`| The existing LoRA to append to. Set to None for new LoRA (default: “[None]”).| COMBO| Yes| Multiple options available  
`bucket_mode`| Enable resolution bucket mode. When enabled, expects pre-bucketed latents from ResolutionBucket node (default: False).| BOOLEAN| Yes| -  
`bypass_mode`| Enable bypass mode for training. When enabled, adapters are applied via forward hooks instead of weight modification. Useful for quantized models where weights cannot be directly modified (default: False).| BOOLEAN| Yes| -  
  
**Note:** The number of positive conditioning inputs must match the number of latent images. If only one positive conditioning is provided with multiple images, it will be automatically repeated for all images. **Note on`training_dtype`:** When set to “none”, the model’s native compute dtype is preserved. For fp16 models, GradScaler is automatically enabled to prevent underflow during gradient computation. If `fp16_accumulation` is also enabled (via `--fast` flags), this combination can be numerically unstable and may cause NaN values. **Note on`quantized_backward`:** This parameter is only relevant when `training_dtype` is set to “none” and the model is a quantized model. It enables quantized matrix multiplication during the backward pass. **Note on`bypass_mode`:** When enabled, adapters are applied via forward hooks instead of modifying the model weights directly. This is particularly useful for quantized models where weights cannot be directly modified.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`lora`| The trained LoRA weights that can be saved or applied to other models.| LORA_MODEL  
`loss_map`| A dictionary containing the training loss values over time.| LOSS_MAP  
`steps`| The total number of training steps completed (including any previous steps from existing LoRA).| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/en.md)

* * *

**Source fingerprint (SHA-256):** `39e88045270d36855442024b62d6a225a58b34842f45ac04fbc6c1ade6768a76`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TrainLoraNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TrainLoraNode)

[SaveTrainingDataset - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveTrainingDataset)[MeshyAnimateModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MeshyAnimateModelNode)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
