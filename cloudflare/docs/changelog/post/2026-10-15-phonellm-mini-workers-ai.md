---
url: https://developers.cloudflare.com/changelog/post/2026-10-15-phonellm-mini-workers-ai/
title: Pipecat PhoneLLM Mini now available on Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.285876+00:00
---

# Pipecat PhoneLLM Mini now available on Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-15-phonellm-mini-workers-ai/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 15, 2026

## Pipecat PhoneLLM Mini now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)[Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/daily-co/phonellm-mini-alpha-2`](https://developers.cloudflare.com/workers-ai/models/phonellm-mini-alpha-2/), a model from the [Pipecat ↗︎](https://www.pipecat.ai/) team at Daily, is now available on [Workers AI](https://developers.cloudflare.com/workers-ai/). PhoneLLM is built for voice agents and other realtime AI applications, where a model has to reply quickly and call the right tool mid-conversation.

In a voice agent, the language model sits between speech-to-text and text-to-speech, so every second it takes adds to the caller's wait. Developers usually choose between a fast model without reasoning mode, which can miss instructions or tool calls, and a slower model in reasoning mode, which handles both well. Pipecat post-trained NVIDIA Nemotron 3 Nano 30B on phone and customer support scenarios so PhoneLLM follows instructions and calls tools better without reasoning mode.

You can use PhoneLLM through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`) or the [REST API](https://developers.cloudflare.com/workers-ai/get-started/rest-api/) at `/ai/run`. Pipecat recommends `temperature: 0`. Also set `chat_template_kwargs: { enable_thinking: false }`.

#### Run a voice agent with Pipecat on Workers

[Pipecat ↗︎](https://docs.pipecat.ai/) is an open-source Python framework for building voice agents. Now that [Python Workers](https://developers.cloudflare.com/workers/languages/python/) are generally available, you can run a Pipecat voice agent on Cloudflare.

Our [Pipecat voice agent example ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/pipecat-voice-agent) runs in a [Durable Object](https://developers.cloudflare.com/durable-objects/) and uses WebRTC as the voice transport through the [Realtime SFU](https://developers.cloudflare.com/realtime/sfu/). It uses [DeepSeek V4 Flash](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/) by default. To deploy it with PhoneLLM, give this prompt to your coding agent:

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

For more information, refer to the [PhoneLLM Mini model page](https://developers.cloudflare.com/workers-ai/models/phonellm-mini-alpha-2/), [Pipecat's model card ↗︎](https://huggingface.co/pipecat-ai/phonellm-mini-alpha-2), and [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).
