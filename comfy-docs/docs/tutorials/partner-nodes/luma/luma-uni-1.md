---
url: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-uni-1/
title: Luma Uni-1 Guide - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:34.576296+00:00
---

# Luma Uni-1 Guide - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/luma/luma-uni-1/

## On this page

  * What makes Uni-1 different
  * What Luma Uni-1 is good at
  * The core distinction: Create vs Modify
  * Available workflows
    * Image Create workflow
    * Image Edit workflow
  * Core parameters
  * Working with reference images
    * Create mode examples
    * Modify mode examples
  * Prompting guidelines
  * Aspect ratios
  * Seeds: control and reproducibility
  * Advanced techniques
    * Character consistency
    * Multi-reference architecture
    * Create → Modify chain
    * Iterative refinement
  * Troubleshooting
  * Quick reference
  * The golden rules
  * Key takeaway



Luma

# Luma Uni-1 Guide

Copy pageCopy page

Use Luma Uni-1 partner nodes in ComfyUI for Create and Modify image workflows.

Copy pageCopy page

In **ComfyUI** , Luma **Uni-1** shows up as **partner Partner Nodes** for unified image work: **Create** graphs generate new images from prompts (with optional references); **Modify** graphs take an existing image as input and edit it in place. You drive both through the usual workflow: wire **Load Image** / **Save Image** , set prompts, seeds, aspect ratio, and reference slots on the Luma node, then queue the graph locally or open a template on **Comfy Cloud**. Luma describes Uni-1 as a non-diffusion, decoder-only autoregressive model that reasons over your prompt before drawing. On the canvas, what matters most is choosing **Create vs Modify** , labeling references clearly, and iterating with seeds.

## 

​

What makes Uni-1 different

  * **Two clear modes** : Create Image (generate something new) and Modify Image (edit something existing)
  * **Up to 9 reference images** , each with a defined role
  * **Strong control over niche and specific visual styles**
  * **Seed support** for reproducibility and controlled iteration
  * **Nine aspect ratios** , from ultra-tall to ultra-wide
  * **Text rendering** that’s actually readable
  * **Web search grounding** for real-world context
  * **Multilingual prompts**
  * **Multi-panel output** with temporal consistency

If you understand the modes and how to control references, you understand Uni-1.

## 

​

What Luma Uni-1 is good at

Uni-1 excels across a wide range of tasks:

  * **Photorealism** with material accuracy
  * **Illustration & stylized art** with strong aesthetic control
  * **Old photo restoration** and vintage reproduction
  * **Surreal and conceptual** compositions
  * **Text rendering** : readable text inside images, great for infographics and posters
  * **Image editing** and multi-turn refinement
  * **Reference-guided generation** with identity preservation
  * **Multi-panel output** : consistent characters/scenes across multiple frames



To use the Partner Nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the Partner Nodes.

  * Local users

  * Cloud users




Make sure your ComfyUI is updated.

  * [Download ComfyUI](https://www.comfy.org/download)
  * [Update Guide](https://docs.comfy.org/installation/update_comfyui)

Workflows in this guide can be found in the [Workflow Templates](https://docs.comfy.org/interface/features/template). If you can’t find them in the template, your ComfyUI may be outdated.If nodes are missing when loading a workflow, possible reasons:

  1. You are not using the latest ComfyUI version (Nightly version)
  2. Some nodes failed to import at startup



  * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.

## 

​

The core distinction: Create vs Modify

Everything in Uni-1 starts with one question: **Am I creating something new, or changing something that already exists?**

Mode| What it does| When to use  
---|---|---  
**Create Image**|  Produces a brand-new composition. Can be inspired by references.| ”Create a new scene in the style of this photo”  
**Modify Image**|  Edits a specific input image. Preserves composition and structure unless told otherwise.| ”Make this photo look like nighttime”  
  
When in doubt:

  * If the output should look like a **version of your input** , use Modify
  * If it should feel **inspired but new** , use Create



## 

​

Available workflows

### 

​

Image Create workflow

![Luma Uni-1 Image Create workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_uni_1_image_create-1.webp)

## Run Image Create on Cloud

Try the Image Create workflow instantly on Comfy Cloud.

## Download Image Create Workflow

Download JSON or search “Luma UNI-1 Image Create” in Template Library

### 

​

Image Edit workflow

![Luma Uni-1 Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_uni_1_image_edit-1.webp)

## Run Image Edit on Cloud

Try the Image Edit workflow instantly on Comfy Cloud.

## Download Image Edit Workflow

Download JSON or search “Luma UNI-1 Image Edit” in Template Library

The workflow is simple: **prompt → evaluate → refine**. Leave the seed blank while exploring. Once you find something strong, lock the seed and iterate from there.

## 

​

Core parameters

Parameter| Description  
---|---  
**Prompt**|  Your primary control. Up to 6,000 characters. Be precise.  
**Aspect ratio**|  Controls framing, not quality. Choose based on use case.  
**Seed**|  Same seed + same prompt → same result. Same seed + changed prompt → controlled variation. No seed → exploration.  
**Reference images** (Create)| Up to 9 images to guide different aspects.  
**Source image** (Modify)| The image you are editing. Dimensions are preserved automatically.  
  
## 

​

Working with reference images

References only work if you tell the model what they are for. Use this structure:
    
    
    Use IMAGE1 ([description]) as a [ROLE] reference.
    

Possible roles: **Style** , **Character** , **Composition** , **Color palette** , **Lighting** , **Texture** , **Mood**. Without roles, the model guesses, and guesses are unreliable.

### 

​

Create mode examples

**Style reference**
    
    
    Use IMAGE1 (impressionist oil painting with loose brushwork and warm
    sunset tones) as a STYLE reference. Create a portrait of a woman in her
    30s applying IMAGE1's color palette and painterly texture. The subject
    should be new.
    

**Character reference**
    
    
    Use IMAGE1 (woman with short copper-red hair, freckles) as a CHARACTER
    reference. Preserve her features. Generate a new scene: she's sitting
    in a softly lit café.
    

**Multi-reference**
    
    
    Use IMAGE1 as a COLOR PALETTE reference, IMAGE2 as LIGHTING, IMAGE3 as
    COMPOSITION. Create a lone figure walking through a rain-slicked street
    at night.
    

### 

​

Modify mode examples

In Modify mode, clarity is everything. Always specify **what to change** and **what must stay untouched**.
    
    
    Change the time of day to golden hour. Update sky, light direction,
    shadows, and color temperature. Keep all subjects and composition
    unchanged.
    
    
    
    Make the rain heavier and add reflections on the ground. Keep all other
    elements unchanged.
    

## 

​

Prompting guidelines

Recommended lengths:

  * **Text-to-image** → 80–250 words
  * **Reference-guided** → 100–300 words
  * **Modify** → 30–100 words

Avoid vague terms (“beautiful”, “amazing”), redundant phrasing, and conflicting instructions. Instead, use specific, named aesthetics:

  * `Golden hour, 85mm lens, shallow depth of field`
  * `1970s Italian giallo film poster, high-contrast color blocking`

Precision beats generality.

## 

​

Aspect ratios

Choose based on where the image will live:

Ratio| Use case  
---|---  
1:1| Social posts  
9:16| Vertical video  
16:9| Widescreen  
3:2 / 2:3| Photography  
2:1 / 3:1| Cinematic / panoramic  
1:2 / 1:3| Ultra-tall  
  
In Modify mode, aspect ratio is locked to the source image.

## 

​

Seeds: control and reproducibility

Seeds turn experimentation into systems.

  * **Fixed seed** → consistency
  * **No seed** → exploration

Workflow:

  1. Explore with no seed
  2. Find a strong result
  3. Lock the seed
  4. Change one variable at a time

Save your prompt and seed together. That’s your reusable recipe.

## 

​

Advanced techniques

### 

​

Character consistency

  1. Generate a clean, front-facing reference image
  2. Reuse it as `IMAGE1 (CHARACTER)` in every scene
  3. Keep the label identical across prompts



### 

​

Multi-reference architecture

Assign one role per image:

  * IMAGE1 → character
  * IMAGE2 → style
  * IMAGE3 → lighting
  * IMAGE4 → environment

End the prompt with:
    
    
    Treat each reference as having authority over its assigned layer only.
    

### 

​

Create → Modify chain

Use Create to explore compositions, then Modify to refine details. This is one of the most powerful workflows.

### 

​

Iterative refinement

  1. Explore (no seed)
  2. Lock seed
  3. Change one variable per generation
  4. Document results

It feels slower, but it’s actually faster, because you always know what changed.

## 

​

Troubleshooting

Problem| Fix  
---|---  
References ignored| Label each one clearly  
Modify changes too much| Explicitly state what must stay unchanged  
Inconsistent outputs| Lock the seed  
Prompt partially ignored| Remove conflicts or split into steps  
Output looks like the reference image| You may be in Modify mode  
Character inconsistency| Reuse a canonical reference image  
  
## 

​

Quick reference

**Create Image**

  * New compositions
  * Text + up to 9 references
  * Descriptive prompts

**Modify Image**

  * Edits existing images
  * Source image + references
  * Direct, surgical prompts



## 

​

The golden rules

  1. Label every reference
  2. In Modify mode, always state what should **not** change
  3. Change one variable at a time when refining
  4. Save prompt + seed for reproducibility
  5. Create = new scenes, Modify = edits



## 

​

Key takeaway

Mastering Uni-1 comes down to three things: **choose the right mode → control your references → iterate with intention**. Once those are in place, you’re no longer guessing, you’re directing.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/luma/luma-uni-1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/luma/luma-uni-1)

[Krea 3 in ComfyUI: Text to Image and Image EditingPrevious](https://docs.comfy.org/tutorials/partner-nodes/krea/krea-3)[Luma Text to Image in ComfyUI: Style and Character ReferencesNext](https://docs.comfy.org/tutorials/partner-nodes/luma/luma-text-to-image)

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
