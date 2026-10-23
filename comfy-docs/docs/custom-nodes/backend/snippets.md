---
url: https://docs.comfy.org/custom-nodes/backend/snippets/
title: Annotated Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:36.701415+00:00
---

# Annotated Examples - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/snippets/

## On this page

  * Images and Masks
    * Load an image
    * Save an image batch
    * Invert a mask
    * Convert a mask to Image shape
    * Using Masks as Transparency Layers
  * Noise
    * Creating noise variations



Python (Backend)

# Annotated Examples

Copy pageCopy page

Annotated code examples for ComfyUI custom nodes: load and save images, invert masks, convert mask shapes, use masks as transparency layers, and create noise.

Copy pageCopy page

A growing collection of fragments of example code…

## 

​

Images and Masks

### 

​

Load an image

Load an image into a batch of size 1 (based on `LoadImage` source code in `nodes.py`)
    
    
    i = Image.open(image_path)
    i = ImageOps.exif_transpose(i)
    if i.mode == 'I':
        i = i.point(lambda i: i * (1 / 255))
    image = i.convert("RGB")
    image = np.array(image).astype(np.float32) / 255.0
    image = torch.from_numpy(image)[None,]
    

### 

​

Save an image batch

Save a batch of images (based on `SaveImage` source code in `nodes.py`)
    
    
    for (batch_number, image) in enumerate(images):
        i = 255. * image.cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        filepath = # some path that takes the batch number into account
        img.save(filepath)
    

### 

​

Invert a mask

Inverting a mask is a straightforward process. Since masks are normalised to the range [0,1]:
    
    
    mask = 1.0 - mask
    

### 

​

Convert a mask to Image shape
    
    
    # We want [B,H,W,C] with C = 1
    if len(mask.shape)==2: # we have [H,W], so insert B and C as dimension 1
        mask = mask[None,:,:,None]
    elif len(mask.shape)==3 and mask.shape[2]==1: # we have [H,W,C]
        mask = mask[None,:,:,:]
    elif len(mask.shape)==3:                      # we have [B,H,W]
        mask = mask[:,:,:,None]
    

### 

​

Using Masks as Transparency Layers

When used for tasks like inpainting or segmentation, the MASK’s values will eventually be rounded to the nearest integer so that they are binary — 0 indicating regions to be ignored and 1 indicating regions to be targeted. However, this doesn’t happen until the MASK is passed to those nodes. This flexibility allows you to use MASKs as you would in digital photography contexts as a transparency layer:
    
    
    # Invert mask back to original transparency layer
    mask = 1.0 - mask
    
    # Unsqueeze the `C` (channels) dimension
    mask = mask.unsqueeze(-1)
    
    # Concatenate ("cat") along the `C` dimension
    rgba_image = torch.cat((rgb_image, mask), dim=-1)
    

## 

​

Noise

### 

​

Creating noise variations

Here’s an example of creating a noise object which mixes the noise from two sources. This could be used to create slight noise variations by varying `weight2`.
    
    
    class Noise_MixedNoise:
        def __init__(self, nosie1, noise2, weight2):
            self.noise1  = noise1
            self.noise2  = noise2
            self.weight2 = weight2
    
        @property
        def seed(self): return self.noise1.seed
    
        def generate_noise(self, input_latent:torch.Tensor) -> torch.Tensor:
            noise1 = self.noise1.generate_noise(input_latent)
            noise2 = self.noise2.generate_noise(input_latent)
            return noise1 * (1.0-self.weight2) + noise2 * (self.weight2)
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/snippets.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/snippets)

[Working with torch.TensorPrevious](https://docs.comfy.org/custom-nodes/backend/tensors)[Execution Model Inversion GuideNext](https://docs.comfy.org/development/comfyui-server/execution_model_inversion_guide)

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
