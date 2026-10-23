---
url: https://www.comfy.org/platform/router/
title: Comfy Router \u00b7 Developer Platform
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:00.925614+00:00
---

# Comfy Router · Developer Platform

> Source: https://www.comfy.org/platform/router/

![](https://www.comfy.org/icons/node-left.svg)![Comfy](https://www.comfy.org/icons/logo.svg)![](https://www.comfy.org/icons/node-union-2size.svg)ROUTER![](https://www.comfy.org/icons/node-right.svg)

# One API for frontier media models.

Integrate frontier image, video, 3D and audio models once. Then choose the provider for each job for better availability and prices.

PythonTypeScriptcURL
    
    
    from comfy_sdk import Comfy
    
    client = Comfy(api_key="comfyui-...")
    
    result = client.models.run(
        "openai/gpt-image-2",
        {"prompt": "aerial view of a neon coral reef at dusk"},
    )

[Get your API key](https://platform.comfy.org/profile/api-keys?onboarding=router)[Browse Models](https://www.comfy.org/hub/models/)

PythonTypeScriptcURL
    
    
    from comfy_sdk import Comfy
    
    client = Comfy(api_key="comfyui-...")
    
    result = client.models.run(
        "openai/gpt-image-2",
        {"prompt": "aerial view of a neon coral reef at dusk"},
    )

### Integrate once. Add models as you go.

Every provider you add brings another SDK, another key, another job lifecycle, and another set of errors. Build that once through Comfy Router, and the next model is one line.

![Integrate once. Add models as you go.](https://media.comfy.org/website/router/integrate-once-v2.webp)

### Better availability. Better prices. No subscription.

Run the same model on fal, Runware, or Wavespeed, and switch with one parameter when one is rate limited or another is cheaper. Comfy never switches the route for you, and every job reports the provider that ran it.

![Better availability. Better prices. No subscription.](https://media.comfy.org/website/router/provider-comfy.webp)

### Hit a concurrency limit? Queue the job.

And let Comfy handle the wait. Use `submit` to get a request ID immediately. The job runs when a slot opens, and you can use the ID to check progress and retrieve the result. Or use `subscribe` to submit the job and wait until it completes.

![Hit a concurrency limit? Queue the job.](https://media.comfy.org/website/router/model-stream.webp)

Supported providers

  * ![Runware](https://www.comfy.org/icons/router-providers/runware.svg)
  * ![fal](https://www.comfy.org/icons/router-providers/fal.svg)
  * ![WaveSpeed](https://www.comfy.org/icons/router-providers/wavespeed.svg)
  * ![Higgsfield](https://www.comfy.org/icons/router-providers/higgsfield.svg)



Migrate to Comfy Router with your agent

Help me migrate this project's existing model integration to Comfy Router.

COPY PROMPTCOPIEDCOPY PROMPT

The same models 3M+ ComfyUI users already use, now behind one API.

[Seedance 2.5](https://www.comfy.org/hub/models/seedance-2-5-text-to-video/)[![Nano Banana Pro](https://media.comfy.org/website/cloud/ai-models/nano-banana-pro.webp)Nano Banana Pro](https://www.comfy.org/hub/models/nano-banana-pro-text-to-image/)[ChatGPT Images 2.5](https://www.comfy.org/hub/models/gpt-image-2-5-flare-text-to-image/)[![KlingAI 3.0](https://media.comfy.org/website/router/kling-3-video.webp)KlingAI 3.0](https://www.comfy.org/hub/models/kling-3-0-turbo-text-to-video/)[![Flux 3](https://media.comfy.org/website/router/flux-3-t2v.webp)Flux 3](https://www.comfy.org/hub/models/flux-3-video-text-to-video/)[Gemini Omni 1.1 Flash](https://www.comfy.org/hub/models/gemini-omni-1-1-flash-image-to-video/)

## Choose the provider in one line.

Python

![](https://www.comfy.org/icons/router-providers/comfy.svg)![](https://www.comfy.org/icons/router-providers/fal.svg)![](https://www.comfy.org/icons/router-providers/runware.svg)![](https://www.comfy.org/icons/router-providers/wavespeed.svg)
    
    
    from comfy_sdk import Comfy
    
    client = Comfy(api_key="comfyui-...")
    
    result = client.models.run(
        "openai/gpt-image-2",
        {"prompt": "aerial view of a neon coral reef at dusk"},
    )

Change the provider. Keep everything else.

## Same models. More places to run them.

Every model runs on Comfy by default, you can set `model_provider` to run them on another provider. We're starting with the highest-traffic models, more models and providers are coming soon.

MODEL| ![Comfy](https://www.comfy.org/icons/router-providers/comfy.svg)| ![fal](https://www.comfy.org/icons/router-providers/fal.svg)| ![Higgsfield](https://www.comfy.org/icons/router-providers/higgsfield.svg)| ![Runware](https://www.comfy.org/icons/router-providers/runware.svg)| ![WaveSpeed](https://www.comfy.org/icons/router-providers/wavespeed.svg)  
---|---|---|---|---|---  
[GPT Image 2](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2/code)| Served| Served| –Not served| Served| Served  
[GPT Image 2.5 Flare](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2-5-flare/code)| Served| Served| –Not served| Served| Served  
[GPT Image 2.5 Sunburst](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code)| Served| Served| –Not served| Served| Served  
[Kling 3.0 Turbo](https://docs.comfy.org/development/comfy-router/models/kling/kling-3-0-turbo/code)| Served| –Not served| Served| –Not served| –Not served  
[Kling V3](https://docs.comfy.org/development/comfy-router/models/kling/kling-v3/code)| Served| –Not served| Served| –Not served| –Not served  
[Nano Banana 2](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-2/code)| Served| Served| –Not served| Served| Served  
[Nano Banana Pro](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-pro/code)| Served| Served| –Not served| Served| Served  
[Seedance 2.0](https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-0-260128/code)| Served| Served| Served| Served| Served  
[Seedance 2.5](https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-5-260628/code)| Served| Served| Served| Served| Served  
[Wan 3.0 Video](https://docs.comfy.org/development/comfy-router/models/wan/wan3-0-video/code)| Served| –Not served| Served| –Not served| –Not served  
[MiniMax H3](https://docs.comfy.org/development/comfy-router/models/minimax/minimax-h3/code)| Served| –Not served| –Not served| –Not served| –Not served  
FLUX 2 Pro| Served| –Not served| –Not served| –Not served| –Not served  
Grok Imagine Video 1.5| Served| –Not served| –Not served| –Not served| –Not served  
  
+200 more models run on Comfy

[Browse all 213 models](https://www.comfy.org/hub/models/)

Roadmap

## Coming soon to the same API. 

Provider choice is the foundation. Everything below arrives on the integration you ship today.

### Comfy workflows

Run a ComfyUI workflow from the same SDK. Just like models.

Workflows run today through the Comfy API on the Developer Platform. Router support brings them behind the same key, the same job surface, and the same credits as every model call, so a pipeline you build in ComfyUI ships to your app as one request.

Read more Comfy workflows

### Routing strategies

Name the policy: reliable, fast_start, fast_finish, or lowest_cost.

Name the outcome you want instead of a provider. Comfy picks a route that fits the policy, and every job still reports the provider that ran it. Ordered fallback arrives alongside: a backup list Comfy uses only when a retry is known to be safe.

Read more Routing strategies

### Route by use case

Request an upscale, a background removal, or an animation, and Comfy picks a model or workflow that can do it.

Describe the task instead of the model. Comfy matches it to a model or workflow that can do it, on a provider that is up, so new models slot in without a change on your side.

Read more Route by use case

### BYOK

Use your own provider key for supported models while keeping the same Comfy Router integration.

Connect your own provider credentials and run supported models through the same Comfy Router API. Keep one SDK and job lifecycle while usage and billing for those calls stay with your provider.

Read more BYOK

[LEARN MORE](https://docs.comfy.org/development/comfy-router/quickstart#comfy-router-quickstart)

## FAQ

Why not call fal, Runware, or Wavespeed directly?+

You can, and plenty of teams do. Comfy Router earns its place when you need more than one: the same model on more than one provider, one key and one job surface, and a route you pick. Each provider routes to itself. Comfy Router gives you one surface across them.

Is Comfy Router “OpenRouter for media”?+

OpenRouter is known for routing language models. Comfy Router is built for generative media: large assets, model-specific controls, and jobs that run for minutes.

Does Comfy pick the provider for me?+

Not at launch. You name the provider and Comfy runs it there. Nothing is swapped behind your back.

What happens if my provider is unavailable?+

The request fails on the provider you chose, with no silent substitution. Ordered fallback is on the roadmap: a backup list, used only when a retry is known to be safe.

What happens when I hit my concurrency limit?+

Queue the job instead of retrying on a 429. Use submit to send the job and receive a request ID immediately; use that ID to check progress and retrieve the result on your own terms. If you want Comfy to wait for the result, use subscribe, which submits the job and polls until it completes. Queueing is available for all supported models. [Learn more about concurrency limits.](https://docs.comfy.org/tutorials/partner-nodes/concurrency-limits)

How long do you keep my inputs and outputs?+

Inputs are kept for 24 hours after upload and outputs for 24 hours after generation. Then they’re deleted.

I already use ComfyUI. What does Comfy Router add?+

More ways to run the models you use. Reach supported models across providers, choose where they run, and switch when price, speed, or availability changes.

Can I call Comfy workflows too?+

Not through Comfy Router yet. Workflows run today through the Comfy API on the Developer Platform, and Router support is on the roadmap.

Where do my API keys, usage, and billing live?+

On the Developer Platform. Your API keys, run history, credits, and payments live there.

Can I bring my own provider key?+

BYOK is available for select models on Enterprise. Access is enabled by request. [Contact Enterprise Sales](https://www.comfy.org/enterprise/)

How is Comfy Router priced?+

Comfy Router uses the same Comfy credits that cover Partner Nodes, Comfy Cloud workflow runs, and other supported model calls. Per-model pricing is listed in the model catalog, so you can see the cost for each model before you run it.

Do I need a Comfy subscription?+

No. Router runs on credits. Add credits and start calling models.

## ![](https://www.comfy.org/assets/platform/hero/badge-left.svg)DEVELOPER PLATFORM![](https://www.comfy.org/assets/platform/hero/badge-left.svg)Start building with Comfy Router today.

Call frontier media models, choose your provider, get better pricing and availability. All behind one API.

[Get Started](https://platform.comfy.org/profile/api-keys?onboarding=router)[Read the docs](https://docs.comfy.org/development/overview)

Products

## The AI creation engine for complete control

Over every model, every node, every step, every output.

### [Comfy DesktopRun ComfyUI on your own hardware.SEE DESKTOP FEATURES](https://www.comfy.org/download/)### [Comfy CloudThe full power of ComfyUI from anywhere.SEE CLOUD FEATURES](https://www.comfy.org/cloud/)### [Developer PlatformDeploy and scale ComfyUI workflows.SEE PLATFORM FEATURES](https://www.comfy.org/platform/)### [Comfy EnterpriseEnterprise-grade infrastructure for the creative engine inside your organization.SEE ENTERPRISE FEATURES](https://www.comfy.org/enterprise/)
