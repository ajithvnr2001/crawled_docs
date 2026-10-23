---
url: https://www.comfy.org/ltx-2.5/
title: LTX 2.5 on Comfy: Open-Source AI Video Model
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:00.116626+00:00
---

# LTX 2.5 on Comfy: Open-Source AI Video Model

> Source: https://www.comfy.org/ltx-2.5/

  1. [Home](https://www.comfy.org/)
  2. / [Models](https://www.comfy.org/hub/models/)
  3. / LTX 2.5



Updated August 2026

00:00

# LTX 2.5 is here

LTX is the fastest video generation model on the planet, and this version sharpens prompt adherence, visuals, and audio quality across the board. With a new Diffusion Fidelity Rendering capability, fine textures, faces, and complex shots hold up at cinematic-grade detail.

[RUN LTX 2.5](https://cloud.comfy.org/?template=video_ltx2_5_i2v)[TRY WORKFLOWS](https://comfy.org/workflows/model/ltx/)

Open SourceImage to VideoText to VideoPartner Node

## Made with LTX 2.5

FreeIncluded free

[](https://cloud.comfy.org/?template=video_ltx2_5_i2v)

A fighter jet banks hard over a stormy, moonlit sea.

FreeIncluded free

[](https://cloud.comfy.org/?template=video_ltx2_5_i2v)

Luminous figure drinks from a flower-filled glass.

FreeIncluded free

[](https://cloud.comfy.org/?template=video_ltx2_5_i2v)

A weathered face stares out from deep shadow.

FreeIncluded free

[](https://cloud.comfy.org/?template=video_ltx2_5_i2v)

Heavy-lift drones haul goats across a misty mountain range.

PremiumPay-as-you-go

[](https://cloud.comfy.org/?template=api_ltx2_5_flf2v)

A frost-covered astronaut gazes up at the aurora.

PremiumPay-as-you-go

[](https://cloud.comfy.org/?template=api_ltx2_5_flf2v)

A coated rider and horse stand atop the clouds above Earth.

## Choose a plan

Access cloud-powered ComfyUI workflows with straightforward, usage-based pricing.

MonthlyYearly (Up to 20% off)

Start Comfy Cloud for free. Upgrade when you're ready.

5 free runs on real GPUs — no credit card required.

[TRY FREE](https://cloud.comfy.org)

STANDARD

$20

/month

Billed monthly

What's included:

  * Included: 30 minute max workflow runtime
  * Included: Add more credits anytime



Comfy Agent

  * Included: 4 concurrent agent sessions per workspace



Comfy API

  * Included: 5 builds
  * Included: 2 deployments
  * Included: Up to 2 workers per deployment



4,200 monthly credits

Generates ~380 5s videos*

[SUBSCRIBE TO STANDARD](https://cloud.comfy.org/?pricing=standard&cycle=monthly)

CREATORMOST POPULAR

$35

/month

Billed monthly

Everything in Standard, plus:

  * Included: Import your own models



Comfy Agent

  * Included: 6 concurrent agent sessions per workspace



Comfy API

  * Included: 5 builds
  * Included: 2 deployments
  * Included: Up to 2 workers per deployment



7,400 monthly credits

Generates ~670 5s videos*

[SUBSCRIBE TO CREATOR](https://cloud.comfy.org/?pricing=creator&cycle=monthly)

PRO

$100

/month

Billed monthly

Everything in Creator, plus:

  * Included: Longer workflow runtime (up to 1 hr)



Comfy Agent

  * Included: 8 concurrent agent sessions per workspace



Comfy API

  * Included: 10 builds
  * Included: 5 deployments
  * Included: Up to 10 workers per deployment



21,100 monthly credits

Generates ~1,915 5s videos*

[SUBSCRIBE TO PRO](https://cloud.comfy.org/?pricing=pro&cycle=monthly)

TEAM

Built for teams collaborating on workflows together.

$665

$700/month

Save 5% ($35)

Billed monthly

42.2K

84.4K

147.7K

295.4K

527.5K

147,700 monthly credits

Generates ~13,405 5s videos*

Everything in Pro, plus:

  * Included: Invite members
  * Included: Members can run workflows concurrently
  * Included: Shared credit pool for all members
  * Included: Role-based permissions



Comfy Agent

  * Included: 16 concurrent agent sessions per workspace



Comfy API

  * Included: 40 builds
  * Included: 20 deployments
  * Included: Up to 20 workers per deployment



Coming soon...

  * Coming soon: Shared workflows & assets
  * Coming soon: Projects



[SUBSCRIBE TO TEAM](https://cloud.comfy.org/?pricing=team&stop=team_700&cycle=monthly)

ENTERPRISE

Need more members? Looking for more flexibility or custom features?

[Contact Us](https://www.comfy.org/contact/)

*Based on 5s videos created with the Wan 2.2 Image-to-Video template using default settings (81 frames, 18fps, 640x640, 4-step sampler)

## Q&A

### What is LTX-2.5?

LTX-2.5 is the newest version of LTX's open video model, with day 0 support in ComfyUI. Weights are downloadable and it runs fast on local GPUs. Native 4K, synchronized audio and video, and frame rates up to 50 FPS. Read the full announcement on [the Comfy blog](https://blog.comfy.org/p/ltx-25-day-0-support-in-comfyui).

### What's new in LTX-2.5 vs LTX-2.3?

LTX-2.5 improves the full generation stack rather than a single stage. New in this release: Diffusion Fidelity Rendering, a diffusion video decoder, a custom text encoder, a reworked distilled variant, a prompt enhancer, and a base checkpoint built for adaptation. Native 4K, synchronized audio, and up to 50 FPS carry over from 2.3. Read the full breakdown on [the Comfy blog](https://blog.comfy.org/p/ltx-25-day-0-support-in-comfyui).

### What is Diffusion Fidelity Rendering?

The core change in this release. Instead of spending compute evenly across a scene, the model allocates it by complexity. Structure comes first: motion, composition, and framing generate in an 8x temporally compressed latent space, alongside a set of high-fidelity keyframes, more for complex scenes and fewer for simple ones. A dedicated pixel-diffusion stage then renders the final video from structure and keyframes together. Textures, materials, intricate objects, and faces resolve with pixel-level precision, and busy shots draw more rendering compute than static ones.

### Which LTX-2.5 variant should I use?

Open weights you run yourself: LTX-2.5 dev is the main model, and LTX-2.5 distilled is a smaller, faster variant that now carries more quality, prompt adherence, and motion than earlier distilled releases. Through [Partner Nodes](https://docs.comfy.org/tutorials/partner-nodes/lightricks/ltx-2-5): LTX-2.5 (Fast) covers the wider envelope at 2 to 20 seconds, 720p through 4K, landscape or portrait, at 24, 25, 48, or 50 FPS. LTX-2.5 (Pro) runs 2 to 10 seconds at 720p or 1080p, at 24, 25, or 50 FPS.

### How do I run LTX-2.5 in ComfyUI?

Update ComfyUI to 0.32.0, or open Comfy Cloud. Download [the LTX-2.5 weights](https://huggingface.co/Lightricks/LTX-2.5) and place them in your models directory. Load the LTX-2.5 template from the Templates panel: Text to Video, Image to Video, or FLF2V. Add your prompt and input images, then run. Full setup steps are in [the docs](https://docs.comfy.org/tutorials/video/ltx/ltx-2-5).

### How long can LTX-2.5 videos be?

Through Partner Nodes, Fast runs 2 to 20 seconds, with clips over 10 seconds capped at 720p or 1080p and 24 or 25 FPS. Pro runs 2 to 10 seconds. LTX-2.5 also ships an experimental duration head that reads the action in your prompt and sets clip length before diffusion starts.

### Does LTX-2.5 generate audio?

Yes. Synchronized audio and video carry over from LTX-2.3, and multi-shot generations hold voice across cuts.

### Can LTX-2.5 generate more than one shot?

Yes. One generation produces multiple connected shots, holding character, environment, lighting, voice, and style across the cuts. You get a sequence from a single run instead of matching separate generations afterward.

### Can I fine-tune LTX-2.5?

Yes. The base checkpoint is built for adaptation, so you can fine-tune the raw model on your own data.

### Is LTX-2.5 free to use?

Open weights are free to download and run on your own hardware. Running LTX-2.5 through Partner Nodes uses credits. See [the docs](https://docs.comfy.org/tutorials/video/ltx/ltx-2-5) for setup details.

## One engine, every way to run it

Run LTX 2.5 in the browser today. Batch campaigns with the API, or bring it in-house.

### [Comfy DesktopRun ComfyUI on your own hardware.LEARN MORE](https://www.comfy.org/download/)### [Comfy CloudThe full power of ComfyUI from anywhere.LEARN MORE](https://www.comfy.org/cloud/)### [Developer PlatformDeploy and scale ComfyUI workflows.LEARN MORE](https://www.comfy.org/platform/)### [Comfy EnterpriseEnterprise-grade infrastructure for the creative engine inside your organization.LEARN MORE](https://www.comfy.org/enterprise/)

### Comfy MCP: now turn your agent into a creative technologist.

Your AI assistant can access the ecosystem, build workflows, and generate images, video, audio, or 3D.

[GET STARTED](https://www.comfy.org/mcp/)

## 4+ million Comfy creators say

"Comfy has innovated a new and powerful ecosystem for creativity without compromising creative control. It has been amazing to watch technical artists and curious creative minds leverage Comfy to explore the full surface area of their ideas." 

Scott Belsky,  
Founder of Behance

"The best part for me is the node-based workflow: it offers a lot of possibilities and enables many different combinations. I also appreciate the optimization options and the automatic memory handling, even when working with tight models." 

Richard N.,  
Owner

"I appreciate being able to use models that my computer can no longer keep up with. I prefer the node-based approach because it is adjustable, rather than being behind a closed door." 

MaryAnn E.,  
Broker at Pop RV's

"The UI and UX of ComfyUI are intuitive and user-friendly, making navigation straightforward and efficient. Its integrations with other tools streamline workflows and enhance overall productivity." 

Alan M.,  
Co-Founder

"I use ComfyUI to help me create VFX for my animated show. It's easy to use, especially with importing a Comfy pipeline on the cloud, and I really like the clean UI and how straightforward it is." 

Kirk H.

"I love that ComfyUI is extremely fast and very reliable. It gives me so much freedom to create the characters I want." 

Fred C.

"The one-click workflows are something I do love, as they simplify many processes for me. The setup was very easy, even for someone who isn't familiar with it all." 

Matthew P.

"I like how in-depth ComfyUI can be. It makes me feel like the software itself isn't limited, which encourages me to keep experimenting and learning." 

Verified User

"A holistic approach and visualisation through an endless whiteboard." 

Nikolai K.,  
3D Artist

"Having full control of the GenAI process, and being able to use it unlimited times, integrating it into your workflow whenever you need to create." 

Leonardo S.,  
Social Media Marketing Expert

"Helps me run AI models locally and generate images, video, and audio, all free of cost." 

Verified User,  
Computer Software

![](https://www.comfy.org/icons/arrow-right.svg)![](https://www.comfy.org/icons/arrow-right.svg)
