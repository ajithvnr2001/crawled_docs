---
url: https://developers.cloudflare.com/ai/models/elevenlabs/eleven-text-to-sound-v3/
title: Eleven Sound Effects v3 (ElevenLabs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-17T10:23:32.546362+00:00
---

# Eleven Sound Effects v3 (ElevenLabs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/elevenlabs/eleven-text-to-sound-v3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ElevenLabs logo](https://developers.cloudflare.com/_astro/elevenlabs.0RXw7U95.svg)

# Eleven Sound Effects v3

Music Generation • ElevenLabs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`elevenlabs/eleven-text-to-sound-v3`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Eleven Sound Effects v3 generates sound effects up to 30 seconds long from a text description, with optional seamless looping.

Model Info|   
---|---  
Terms and License| [link ↗](https://elevenlabs.io/terms)  
More information| [link ↗](https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert)  
Pricing| 

  * output audio seconds$0.002

  
  
## Usage
    
    
    const response = await env.AI.run(
      'elevenlabs/eleven-text-to-sound-v3',
      { text: 'Heavy wooden door creaking open slowly in an empty stone hallway', duration_seconds: 4 },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "elevenlabs/eleven-text-to-sound-v3",
      "input": {
        "text": "Heavy wooden door creaking open slowly in an empty stone hallway",
        "duration_seconds": 4
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/elevenlabs/eleven-text-to-sound-v3/door-creak.mp3"
      }
    }

## Examples

**Rain Loop** — Generate a seamless loop for background ambience
    
    
    const response = await env.AI.run(
      'elevenlabs/eleven-text-to-sound-v3',
      {
        text: 'Gentle rain on a tin roof with distant thunder',
        duration_seconds: 8,
        loop: true,
        output_format: 'mp3_44100_128',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "elevenlabs/eleven-text-to-sound-v3",
      "input": {
        "text": "Gentle rain on a tin roof with distant thunder",
        "duration_seconds": 8,
        "loop": true,
        "output_format": "mp3_44100_128"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/elevenlabs/eleven-text-to-sound-v3/rain-loop.mp3"
      }
    }

## Parameters

text

`string`requiredminLength: 1Description of the sound effect to generate.

duration_seconds

`number`requiredminimum: 0.5maximum: 30Length of the sound effect in seconds, from 0.5 to 30.

loop

`boolean`Create a sound effect that loops smoothly.

prompt_influence

`number`minimum: 0maximum: 1How closely to follow the prompt, from 0 to 1 (default 0.3). Higher is closer and less varied.

output_format

`string`enum: mp3_22050_32, mp3_24000_48, mp3_44100_32, mp3_44100_64, mp3_44100_96, mp3_44100_128, mp3_44100_192, opus_48000_32, opus_48000_64, opus_48000_96, opus_48000_128, opus_48000_192Audio codec, sample rate and bitrate (default mp3_44100_128).

audio

`string`URL of the generated sound effect.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-text-to-sound-v3/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-text-to-sound-v3/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-text-to-sound-v3/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-text-to-sound-v3/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
