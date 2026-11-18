---
url: https://developers.cloudflare.com/ai/models/minimax/speech-02-turbo/
title: MiniMax Speech 02 Turbo (MiniMax) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:16.290703+00:00
---

# MiniMax Speech 02 Turbo (MiniMax) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/minimax/speech-02-turbo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![MiniMax logo](https://developers.cloudflare.com/_astro/minimax.B0Y99aoe.svg)

# MiniMax Speech 02 Turbo

Text-to-Speech • MiniMax

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`minimax/speech-02-turbo`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



MiniMax Speech 02 Turbo is a fast, lower-cost multilingual text-to-speech model with emotion control and support for cloned and designed voices.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.minimaxi.com/terms)  
More information| [link ↗](https://platform.minimax.io/docs/api-reference/speech-t2a-http)  
Pricing| 

  * Per character$0.00006

  
  
## Usage
    
    
    const response = await env.AI.run(
      'minimax/speech-02-turbo',
      {
        format: 'mp3',
        pitch: 0,
        speed: 1,
        text: 'Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.',
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-02-turbo",
      "input": {
        "format": "mp3",
        "pitch": 0,
        "speed": 1,
        "text": "Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/minimax/speech-02-turbo/simple-speech.mp3"
      }
    }

## Examples

**Fast Narration** — Speed up narration for quick playback
    
    
    const response = await env.AI.run(
      'minimax/speech-02-turbo',
      {
        format: 'mp3',
        pitch: 0,
        speed: 1.5,
        text: 'This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent and user growth exceeded expectations.',
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-02-turbo",
      "input": {
        "format": "mp3",
        "pitch": 0,
        "speed": 1.5,
        "text": "This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent and user growth exceeded expectations.",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/minimax/speech-02-turbo/fast-narration.mp3"
      }
    }

**Calm Tone** — Calm and steady speech for meditation or relaxation
    
    
    const response = await env.AI.run(
      'minimax/speech-02-turbo',
      {
        emotion: 'calm',
        format: 'mp3',
        pitch: 0,
        speed: 0.8,
        text: 'Take a deep breath in. Hold it for a moment. Now slowly exhale. Let your shoulders relax and release any tension.',
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-02-turbo",
      "input": {
        "emotion": "calm",
        "format": "mp3",
        "pitch": 0,
        "speed": 0.8,
        "text": "Take a deep breath in. Hold it for a moment. Now slowly exhale. Let your shoulders relax and release any tension.",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/minimax/speech-02-turbo/calm-tone.mp3"
      }
    }

**Adjusted Pitch** — Lower the pitch for a deeper voice
    
    
    const response = await env.AI.run(
      'minimax/speech-02-turbo',
      {
        format: 'mp3',
        pitch: -6,
        speed: 1,
        text: 'Good evening. Tonight we explore the mysteries of the deep ocean and the creatures that live in total darkness.',
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-02-turbo",
      "input": {
        "format": "mp3",
        "pitch": -6,
        "speed": 1,
        "text": "Good evening. Tonight we explore the mysteries of the deep ocean and the creatures that live in total darkness.",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/minimax/speech-02-turbo/adjusted-pitch.mp3"
      }
    }

## Parameters

text

`string`requiredmaxLength: 10000The text to convert to speech. Maximum 10,000 characters.

voice_id

`string`requireddefault: English_expressive_narratorThe voice ID to use for synthesis

speed

`number`requireddefault: 1minimum: 0.5maximum: 2Speech speed (0.5 to 2)

volume

`number`requireddefault: 1minimum: 0maximum: 10Speech volume (0 to 10)

pitch

`integer`requireddefault: 0minimum: -12maximum: 12Pitch adjustment (-12 to 12)

emotion

`string`enum: happy, sad, angry, fearful, disgusted, surprised, calmEmotion control for synthesized speech

format

`string`requireddefault: mp3enum: mp3, flac, wavOutput audio format

▶sample_rate

`one of`

audio

`string`URL to the generated audio file

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/minimax/speech-02-turbo/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/speech-02-turbo/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/minimax/speech-02-turbo/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/speech-02-turbo/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
