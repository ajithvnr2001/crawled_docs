---
url: https://developers.cloudflare.com/ai/models/google/lyria-3-pro/
title: Lyria 3 Pro (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:03.928205+00:00
---

# Lyria 3 Pro (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/lyria-3-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Lyria 3 Pro

Music Generation • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`google/lyria-3-pro`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Google's Lyria 3 Pro model generates full-length MP3 songs from detailed text prompts and optional image prompts.

Model Info|   
---|---  
More information| [link ↗](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3)  
Pricing| 

  * Per track$0.08

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/lyria-3-pro',
      {
        prompt:
          'A cinematic folk song about finding home, with acoustic guitar, intimate vocals, brushed drums, and a soaring final chorus',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/lyria-3-pro",
      "input": {
        "prompt": "A cinematic folk song about finding home, with acoustic guitar, intimate vocals, brushed drums, and a soaring final chorus"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/google/lyria-3-pro/cinematic-folk-song.mp3"
      }
    }

## Parameters

prompt

`string`requiredminLength: 1maxLength: 5000

image

`string`minLength: 1Base64-encoded image used as visual inspiration

audio

`string`Generated music as an audio URL

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/lyria-3-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/lyria-3-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/lyria-3-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/lyria-3-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
