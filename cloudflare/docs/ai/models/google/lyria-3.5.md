---
url: https://developers.cloudflare.com/ai/models/google/lyria-3.5/
title: Lyria 3.5 (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:03.767652+00:00
---

# Lyria 3.5 (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/lyria-3.5/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Lyria 3.5

Music Generation • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`google/lyria-3.5`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party
  * Zero data retention



Google's Lyria 3.5 model generates full-length MP3 songs from text prompts and optional image prompts.

Model Info|   
---|---  
More information| [link ↗](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)  
Zero data retention| Yes  
Pricing| 

  * Per track$0.08

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/lyria-3.5',
      {
        prompt:
          'A soulful alternative pop song about starting over, with two verses, a memorable chorus, a contrasting bridge, warm electric piano, expressive vocals, and a powerful final chorus',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/lyria-3.5",
      "input": {
        "prompt": "A soulful alternative pop song about starting over, with two verses, a memorable chorus, a contrasting bridge, warm electric piano, expressive vocals, and a powerful final chorus"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/google/lyria-3.5/full-length-alternative-pop.mp3"
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

Input[](https://developers.cloudflare.com/ai/models/google/lyria-3.5/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/lyria-3.5/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/lyria-3.5/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/lyria-3.5/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
