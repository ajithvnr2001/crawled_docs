---
url: https://developers.cloudflare.com/ai/models/minimax/speech-02-hd/
title: MiniMax Speech 02 HD (MiniMax) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:16.555762+00:00
---

# MiniMax Speech 02 HD (MiniMax) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/minimax/speech-02-hd/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![MiniMax logo](https://developers.cloudflare.com/_astro/minimax.B0Y99aoe.svg)

# MiniMax Speech 02 HD

Text-to-Speech • MiniMax

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`minimax/speech-02-hd`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



MiniMax Speech 02 HD is a studio-quality multilingual text-to-speech model with emotion control and support for cloned and designed voices.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.minimaxi.com/terms)  
More information| [link ↗](https://platform.minimax.io/docs/api-reference/speech-t2a-http)  
Pricing| 

  * Per character$0.0001

  
  
## Usage
    
    
    const response = await env.AI.run(
      'minimax/speech-02-hd',
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
      "model": "minimax/speech-02-hd",
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
        "audio": "https://examples.aig.cloudflare.com/minimax/speech-02-hd/simple-speech.mp3"
      }
    }

## Examples

**Custom Voice** — Use a specific voice and adjust speed
    
    
    const response = await env.AI.run(
      'minimax/speech-02-hd',
      {
        format: 'mp3',
        pitch: 0,
        speed: 0.9,
        text: 'The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.',
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-02-hd",
      "input": {
        "format": "mp3",
        "pitch": 0,
        "speed": 0.9,
        "text": "The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/minimax/speech-02-hd/custom-voice.mp3"
      }
    }

**With Emotion** — Apply emotional tone to speech
    
    
    const response = await env.AI.run(
      'minimax/speech-02-hd',
      {
        emotion: 'happy',
        format: 'mp3',
        pitch: 0,
        speed: 1,
        text: "Congratulations! You've just won the grand prize! This is absolutely incredible news!",
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-02-hd",
      "input": {
        "emotion": "happy",
        "format": "mp3",
        "pitch": 0,
        "speed": 1,
        "text": "Congratulations! You'\''ve just won the grand prize! This is absolutely incredible news!",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/minimax/speech-02-hd/with-emotion.mp3"
      }
    }

**High Sample Rate** — Studio quality at 44.1kHz sample rate
    
    
    const response = await env.AI.run(
      'minimax/speech-02-hd',
      {
        format: 'mp3',
        pitch: 0,
        sample_rate: 44100,
        speed: 1,
        text: 'This recording is generated at studio quality sample rate for the highest possible audio fidelity.',
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-02-hd",
      "input": {
        "format": "mp3",
        "pitch": 0,
        "sample_rate": 44100,
        "speed": 1,
        "text": "This recording is generated at studio quality sample rate for the highest possible audio fidelity.",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/minimax/speech-02-hd/high-sample-rate.mp3"
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

Input[](https://developers.cloudflare.com/ai/models/minimax/speech-02-hd/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/speech-02-hd/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/minimax/speech-02-hd/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/speech-02-hd/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
