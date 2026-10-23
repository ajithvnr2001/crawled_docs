---
url: https://docs.comfy.org/development/comfy-router/higgsfield-byok/
title: Use Your Higgsfield API Key on Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:11.781775+00:00
---

# Use Your Higgsfield API Key on Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/higgsfield-byok/

## On this page

  * What changes when you bring a key
  * Models
  * Reading the result
  * Notes



# Use Your Higgsfield API Key on Comfy Router

Copy pageCopy page

Bring your Higgsfield API key to Comfy Router: generations bill to your Higgsfield account, not your Comfy credits, through the same endpoint as every other model.

Copy pageCopy page

Higgsfield is [running a cashback promotion on API spend](https://higgsfield.ai). We are not going to try to talk you out of it. Bring your own Higgsfield key to Comfy Router and your generations run on **your** Higgsfield account — so they count as your Higgsfield spend, and whatever that promotion is worth to you is yours. You still get one endpoint, one client, and the same request shape as every other model on Router.

Higgsfield owns the promotion and its terms. Check the current offer on their site before you plan around it.

## 

​

What changes when you bring a key

| Your Comfy Key| Your Higgsfield Key  
---|---|---  
Billed to| Your Comfy credits| Your Higgsfield account  
Comfy credits charged| Yes| **None**  
Endpoint, request body, response| Same| Same  
  
Everything else about the call is identical. You do not change your code to switch — you save a key, and Router uses it.

1

Get a Higgsfield API key

Create a key in your [Higgsfield account](https://higgsfield.ai). Higgsfield issues it as an **id and secret pair** , and Comfy stores it as the single string `id:secret` — keep the colon, and do not split it into two fields.

2

Save it in Comfy

Open [**Provider keys**](https://platform.comfy.org/profile/provider-keys) in your Comfy profile, choose **Higgsfield** , and paste the `id:secret` value.Your key is encrypted at rest and is never returned by the API once saved. Router reads it only to sign your own calls.

3

Create a Comfy API key

This is the key that authenticates you to Comfy, separate from the Higgsfield one. Create it in [your Comfy workspace](https://platform.comfy.org/profile/api-keys), then set:
    
    
    export COMFY_API_KEY="comfyui-..."
    

Keep API keys on your server or in your local environment. These examples are for a terminal or server, not browser JavaScript.

4

Run a model

Copy and paste a code snippet below for your selected model.

## 

​

Models

  * Kling 3.0 std

  * Kling 3.0 pro

  * Kling 3.0 4K

  * Kling 3.0 turbo

  * Wan 3.0




Balanced quality and speed. `duration` accepts 3–15 seconds.

cURL

Python

TypeScript
    
    
    curl --max-time 660 \
      https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-std \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
        "duration": 5,
        "aspect_ratio": "16:9",
        "cfg_scale": 0.5,
        "sound": "on"
      }'
    
    
    
    # Python 3.10+
    # Install: python -m pip install "comfy-sdk>=0.3.0"
    
    from comfy_sdk import Comfy
    
    # Comfy reads COMFY_API_KEY from the environment.
    with Comfy() as client:
        result = client.models.run(
            "higgsfield/higgsfield-kling-3-std",
            {
                "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
                "duration": 5,
                "aspect_ratio": "16:9",
                "cfg_scale": 0.5,
                "sound": "on",
            },
            timeout=660.0,
        )
    
    print("video:", result["video"]["url"])
    
    
    
    // Node.js 22+
    // Install: npm install "@comfyorg/sdk@>=0.4.0" --save-dev tsx
    
    import { comfy } from "@comfyorg/sdk";
    
    type HiggsfieldResult = { video: { url: string } };
    
    const { data } = await comfy.models.run<HiggsfieldResult>(
      "higgsfield/higgsfield-kling-3-std",
      {
        prompt: "A cinematic glass pavilion in a misty pine forest at sunrise",
        duration: 5,
        aspect_ratio: "16:9",
        cfg_scale: 0.5,
        sound: "on",
      },
      { timeoutMs: 660_000 },
    );
    
    console.log("video:", data.video.url);
    

Higher fidelity than `std`, same body. `duration` accepts 3–15 seconds.

cURL

Python

TypeScript
    
    
    curl --max-time 660 \
      https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-pro \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
        "duration": 5,
        "aspect_ratio": "16:9",
        "cfg_scale": 0.5,
        "sound": "on"
      }'
    
    
    
    # Python 3.10+
    # Install: python -m pip install "comfy-sdk>=0.3.0"
    
    from comfy_sdk import Comfy
    
    with Comfy() as client:
        result = client.models.run(
            "higgsfield/higgsfield-kling-3-pro",
            {
                "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
                "duration": 5,
                "aspect_ratio": "16:9",
                "cfg_scale": 0.5,
                "sound": "on",
            },
            timeout=660.0,
        )
    
    print("video:", result["video"]["url"])
    
    
    
    // Node.js 22+
    // Install: npm install "@comfyorg/sdk@>=0.4.0" --save-dev tsx
    
    import { comfy } from "@comfyorg/sdk";
    
    type HiggsfieldResult = { video: { url: string } };
    
    const { data } = await comfy.models.run<HiggsfieldResult>(
      "higgsfield/higgsfield-kling-3-pro",
      {
        prompt: "A cinematic glass pavilion in a misty pine forest at sunrise",
        duration: 5,
        aspect_ratio: "16:9",
        cfg_scale: 0.5,
        sound: "on",
      },
      { timeoutMs: 660_000 },
    );
    
    console.log("video:", data.video.url);
    

The 4K tier, same body as `std` and `pro`. `duration` accepts 3–15 seconds.

cURL

Python

TypeScript
    
    
    curl --max-time 660 \
      https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-4k \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
        "duration": 5,
        "aspect_ratio": "16:9",
        "cfg_scale": 0.5,
        "sound": "on"
      }'
    
    
    
    # Python 3.10+
    # Install: python -m pip install "comfy-sdk>=0.3.0"
    
    from comfy_sdk import Comfy
    
    with Comfy() as client:
        result = client.models.run(
            "higgsfield/higgsfield-kling-3-4k",
            {
                "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
                "duration": 5,
                "aspect_ratio": "16:9",
                "cfg_scale": 0.5,
                "sound": "on",
            },
            timeout=660.0,
        )
    
    print("video:", result["video"]["url"])
    
    
    
    // Node.js 22+
    // Install: npm install "@comfyorg/sdk@>=0.4.0" --save-dev tsx
    
    import { comfy } from "@comfyorg/sdk";
    
    type HiggsfieldResult = { video: { url: string } };
    
    const { data } = await comfy.models.run<HiggsfieldResult>(
      "higgsfield/higgsfield-kling-3-4k",
      {
        prompt: "A cinematic glass pavilion in a misty pine forest at sunrise",
        duration: 5,
        aspect_ratio: "16:9",
        cfg_scale: 0.5,
        sound: "on",
      },
      { timeoutMs: 660_000 },
    );
    
    console.log("video:", data.video.url);
    

The fastest Kling tier. Its body carries `resolution` instead of `cfg_scale` and `sound`. `duration` accepts 3–15 seconds.

cURL

Python

TypeScript
    
    
    curl --max-time 660 \
      https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-turbo \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
        "duration": 5,
        "aspect_ratio": "16:9",
        "resolution": "720p"
      }'
    
    
    
    # Python 3.10+
    # Install: python -m pip install "comfy-sdk>=0.3.0"
    
    from comfy_sdk import Comfy
    
    with Comfy() as client:
        result = client.models.run(
            "higgsfield/higgsfield-kling-3-turbo",
            {
                "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
                "duration": 5,
                "aspect_ratio": "16:9",
                "resolution": "720p",
            },
            timeout=660.0,
        )
    
    print("video:", result["video"]["url"])
    
    
    
    // Node.js 22+
    // Install: npm install "@comfyorg/sdk@>=0.4.0" --save-dev tsx
    
    import { comfy } from "@comfyorg/sdk";
    
    type HiggsfieldResult = { video: { url: string } };
    
    const { data } = await comfy.models.run<HiggsfieldResult>(
      "higgsfield/higgsfield-kling-3-turbo",
      {
        prompt: "A cinematic glass pavilion in a misty pine forest at sunrise",
        duration: 5,
        aspect_ratio: "16:9",
        resolution: "720p",
      },
      { timeoutMs: 660_000 },
    );
    
    console.log("video:", data.video.url);
    

Reference-to-video: pass reference images or clips and describe how to use them. `duration` accepts up to 30 seconds.

cURL

Python

TypeScript
    
    
    curl --max-time 660 \
      https://api.comfy.org/v2/models/higgsfield/higgsfield-wan-3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "prompt": "Use Image 1 for the character and Video 1 for the camera movement",
        "image_urls": ["https://cdn.example.com/character.jpg"],
        "video_urls": ["https://cdn.example.com/camera-reference.mp4"],
        "duration": 8,
        "resolution": "1080p",
        "aspect_ratio": "adaptive",
        "generate_audio": true
      }'
    
    
    
    # Python 3.10+
    # Install: python -m pip install "comfy-sdk>=0.3.0"
    
    from comfy_sdk import Comfy
    
    with Comfy() as client:
        result = client.models.run(
            "higgsfield/higgsfield-wan-3",
            {
                "prompt": "Use Image 1 for the character and Video 1 for the camera movement",
                "image_urls": ["https://cdn.example.com/character.jpg"],
                "video_urls": ["https://cdn.example.com/camera-reference.mp4"],
                "duration": 8,
                "resolution": "1080p",
                "aspect_ratio": "adaptive",
                "generate_audio": True,
            },
            timeout=660.0,
        )
    
    print("video:", result["video"]["url"])
    
    
    
    // Node.js 22+
    // Install: npm install "@comfyorg/sdk@>=0.4.0" --save-dev tsx
    
    import { comfy } from "@comfyorg/sdk";
    
    type HiggsfieldResult = { video: { url: string } };
    
    const { data } = await comfy.models.run<HiggsfieldResult>(
      "higgsfield/higgsfield-wan-3",
      {
        prompt: "Use Image 1 for the character and Video 1 for the camera movement",
        image_urls: ["https://cdn.example.com/character.jpg"],
        video_urls: ["https://cdn.example.com/camera-reference.mp4"],
        duration: 8,
        resolution: "1080p",
        aspect_ratio: "adaptive",
        generate_audio: true,
      },
      { timeoutMs: 660_000 },
    );
    
    console.log("video:", data.video.url);
    

## 

​

Reading the result

`run` returns Higgsfield’s own terminal document. The download URL is at `video.url`:
    
    
    {
      "status": "completed",
      "request_id": "0c4a9e17-5b82-4d66-9a3f-7c1e08b45d29",
      "video": { "url": "https://example.com/generated.mp4" }
    }
    

Save it promptly:
    
    
    curl --fail --location "PASTE_VIDEO_URL_HERE" --output out.mp4
    

Router polls Higgsfield for you, so `queued` and `in_progress` never reach you — you get the finished document or an error. `nsfw`, `failed` and `canceled` are the terminal failures; `failed` carries detail in `error`.

## 

​

Notes

  * **Validation happens before Higgsfield is called.** A body outside the published bounds comes back `422` with the offending field named, and nothing is sent upstream — so a bad request costs you nothing.
  * **Your key is used only for models you have a key for.** Saving a Higgsfield key changes nothing about how any other provider on Router is billed.
  * Full request and response schemas for every model are in the [Comfy Router reference](https://docs.comfy.org/development/comfy-router/reference).



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/higgsfield-byok.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/higgsfield-byok)

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
