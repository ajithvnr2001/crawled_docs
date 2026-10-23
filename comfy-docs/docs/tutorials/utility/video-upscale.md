---
url: https://docs.comfy.org/tutorials/utility/video-upscale/
title: Video Upscaling in ComfyUI: Models and Use Cases - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:42.009890+00:00
---

# Video Upscaling in ComfyUI: Models and Use Cases - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/video-upscale/

## On this page

  * TL;DR
  * Key concepts
    * Upscaling vs. enhancement
    * Creative vs. conservative upscale
  * Use cases
    * Quality mode
    * Speed mode
    * AI video fix
    * Archival restoration
    * CGI / 3D render
    * Animation and motion graphics
  * Upscale speed comparison (10s 720p clips)
  * Available models
    * Partner nodes
    * Topaz Video Enhance features
  * Getting started with Topaz Video Enhance
  * Tips



Upscale & Restore

# Video Upscaling in ComfyUI: Models and Use Cases

Copy pageCopy page

Upscale videos in ComfyUI with SeedVR2, Topaz Astra, FlashVSR, HitPaw, Fast GAN, and Wan 2.2 for quality, speed, restoration, and CGI use cases.

Copy pageCopy page

This guide covers video upscaling workflows in ComfyUI, including local models and partner node options for various use cases.

## The Complete AI Upscaling Handbook

For a comprehensive deep-dive with benchmarks and visual comparisons, see the full article on the ComfyUI Blog.

## 

​

TL;DR

  * **Quality mode** : SeedVR2 and HitPaw deliver the most accurate and consistent realism.
  * **Speed mode** : FlashVSR and HitPaw are the fastest options.
  * **AI video fix** : Topaz Astra Creative is strongest for cinematic polish and fixing AI-generated video.
  * **Archival restoration** : SeedVR2 preserves original structure while enhancing clarity.
  * **CGI/3D render** : Topaz, SeedVR2, and HitPaw all produce clean, sharp results.



## 

​

Key concepts

### 

​

Upscaling vs. enhancement

  * **Upscaling** increases resolution while reconstructing detail.
  * **Enhancement** improves perceived quality (denoise, sharpen, restore, temporal consistency, etc.).

Video upscaling adds temporal considerations—maintaining consistency across frames while improving resolution.

### 

​

Creative vs. conservative upscale

| Conservative| Creative  
---|---|---  
**Approach**|  Preserve the original| Reimagine and enhance  
**Strengths**|  High accuracy, temporal consistency, production-safe| Rich details, sharper, more visually striking  
**Limits**|  Can appear flat, limited improvement on poor input| Possible hallucinations, temporal flickering  
**Models**|  Topaz Starlight Fast, FlashVSR, SeedVR2, HitPaw| Topaz Starlight Creative (Astra), Wan 2.2, HitPaw  
  
## 

​

Use cases

### 

​

Quality mode

**SeedVR2** and **HitPaw** deliver the most accurate results, with strong image quality and excellent character consistency. **Topaz** also upscales effectively, but it can sometimes be more creative than expected. This makes it especially suitable for cinematic footage where a stylized look is acceptable.

## SeedVR2 - Conservative (WaveSpeed API)

Try on Comfy Cloud or download workflow

## SeedVR2 - Conservative (Open Source)

Try on Comfy Cloud or download workflow

## HitPaw - All-in-one

Try on Comfy Cloud or download workflow

## Topaz Astra - Creative

Try on Comfy Cloud or download workflow

### 

​

Speed mode

**FlashVSR** performs extremely well when speed is the priority. Upscaling from 720p to 1080p takes about **41 seconds for a 10-second video** , making it one of the fastest options available. **HitPaw** is also relatively fast. In **Topaz** , the Fast and Creative modes render at similar speeds, so using **Creative** mode is generally recommended for better visual results without sacrificing time.

## FlashVSR - Conservative (WaveSpeed API)

Try on Comfy Cloud or download workflow

## HitPaw - All-in-one

Try on Comfy Cloud or download workflow

## Topaz Astra - Creative

Try on Comfy Cloud or download workflow

### 

​

AI video fix

**Topaz Astra Creative** produces very smooth and visually consistent outputs, making it a strong choice for repairing AI-generated videos. A useful workflow tip is to first run a **fix or cleanup pass** , then upscale to **1080p** , and finally upscale gradually to **4K**. This step-by-step approach usually leads to better stability and detail.

## Topaz Astra - Creative

Try on Comfy Cloud or download workflow

## Wan 2.2 Upscale - Creative

Try on Comfy Cloud or download workflow

### 

​

Archival restoration

**SeedVR2** is particularly impressive for archival restoration. It preserves the original structure and detail of the source footage while enhancing clarity, avoiding the introduction of artificial or exaggerated features.

## SeedVR2 - Conservative (Open Source)

Try on Comfy Cloud or download workflow

## SeedVR2 - Conservative (WaveSpeed API)

Try on Comfy Cloud or download workflow

## Fast GAN - Traditional

Try on Comfy Cloud or download workflow

### 

​

CGI / 3D render

**Topaz, SeedVR2 and HitPaw** all perform very well on CGI and 3D-rendered footage. They produce clean, sharp results and maintain the crisp edges that are important for synthetic imagery.

## Topaz Astra - Creative

Try on Comfy Cloud or download workflow

## SeedVR2 - Conservative (WaveSpeed API)

Try on Comfy Cloud or download workflow

## HitPaw - All-in-one

Try on Comfy Cloud or download workflow

### 

​

Animation and motion graphics

Clean lines and consistent colors are essential. Conservative upscaling preserves the intended style. **Recommended** : Topaz Starlight Fast, Fast GAN

## Fast GAN - Traditional

Try on Comfy Cloud or download workflow

## 

​

Upscale speed comparison (10s 720p clips)

Model| Resolution| Time  
---|---|---  
FlashVSR (local)| 1080p| ~41s  
FlashVSR (local)| 4K| ~52s  
HitPaw| 2K| ~80s  
HitPaw| 4K| ~175s  
SeedVR2 (local, 5090)| 1080p| ~312s  
Topaz Astra| 1080p| ~374s  
Topaz Astra| 4K| ~560s  
  
## 

​

Available models

### 

​

Partner nodes

Partner nodes provide access to advanced video upscaling models via API.

Model| Type| Max resolution| Features  
---|---|---|---  
Topaz Starlight Fast| Conservative| 4K| Fast, precision upscale  
Topaz Starlight Creative (Astra)| Creative| 4K| Diffusion-based creative upscale  
Topaz Apollo| -| -| Frame interpolation  
WaveSpeed SeedVR2| Conservative| -| High fidelity  
WaveSpeed FlashVSR| Conservative| -| Fast video super-resolution  
HitPaw| Both| -| All-in-one video enhancement  
  
### 

​

Topaz Video Enhance features

  * **Upscaling** : Starlight (Astra) supports fast video upscaling to FullHD (1080p) or 4K while maintaining clarity.
  * **Interpolation** : Apollo model for frame interpolation with slowmo settings and custom frame rates (e.g., 60fps).
  * **Dynamic compression** : Intelligently identifies and handles compression artifacts to improve image purity.



## 

​

Getting started with Topaz Video Enhance

  1. Update ComfyUI to the latest version.
  2. Search for the `Topaz Video Enhance` node in the node list.
  3. Connect your video input and configure the settings.
  4. Run the workflow.



## 

​

Tips

  * Combine upscaling with [frame interpolation](https://docs.comfy.org/tutorials/utility/frame-interpolation) for smoother, higher-resolution output.
  * For AI-generated videos, consider fixing artifacts before upscaling rather than relying on creative upscaling to fix them.
  * Test different models on sample clips before processing full videos.
  * Use conservative upscaling for content that requires strict fidelity to the original.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/video-upscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/video-upscale)

[Image upscaling in ComfyUIPrevious](https://docs.comfy.org/tutorials/utility/image-upscale)[SeedVR2: Image and video upscaling in ComfyUINext](https://docs.comfy.org/tutorials/utility/seedvr2)

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
