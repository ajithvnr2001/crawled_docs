---
url: https://developers.cloudflare.com/ai-gateway/features/guardrails/
title: Guardrails \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-11-21T09:24:35.720761+00:00
---

# Guardrails · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/features/guardrails/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /[Features](https://developers.cloudflare.com/ai-gateway/features/)
  4. /Guardrails



# Guardrails

Last updated Nov 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewVideo demoHow Guardrails workRelated resources

AI Gateway Guardrails checks traffic between your application and your [model providers](https://developers.cloudflare.com/ai-gateway/usage/providers/). Guardrails uses [`@cf/meta/llama-guard-3-8b`](https://developers.cloudflare.com/workers-ai/models/llama-guard-3-8b/) to check for content hazards (`S1` to `S14`). It uses `@cf/meta/prompt-guard-2-86m` to check prompts for [prompt injection ↗︎](https://www.cloudflare.com/learning/ai/prompt-injection/) (`P1`).

Configure one policy per gateway and apply it to supported traffic across providers, including OpenAI, Anthropic, DeepSeek, and Workers AI. Set the action for each supported category to **Flag** , **Block** , or **Ignore**.

Use [AI Gateway Logs](https://developers.cloudflare.com/ai-gateway/observability/logging/) to review evaluations for logged requests. Prompt and response bodies are available only when payloads are stored.

## Video demo

## How Guardrails work

Guardrails applies your configured policy in three steps:

  1. **Intercept traffic** : AI Gateway proxies requests and responses between your application and its model provider.
  2. **Evaluate prompts and responses** : 
     * **User prompts** : Guardrails checks prompts for content hazards and prompt injection. If a prompt matches a category set to **Block** , it does not reach the model provider.
     * **Model responses** : Guardrails checks eligible response text for content hazards. It skips responses from embedding and unknown model types. For streaming requests, the REST API evaluates responses without enforcing the response policy. Gateway endpoints buffer streamed responses for evaluation and return a single non-streamed payload.
  3. **Apply configured actions** : **Flag** marks a match for review without blocking it. **Ignore** takes no action for that category. A block returns error code `2016` for a prompt or `2017` for a response.



For setup steps, [hazard categories](https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/#hazard-categories), [supported model types](https://developers.cloudflare.com/ai-gateway/features/guardrails/supported-model-types/), and [streaming behavior](https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/#streaming-behavior), refer to [Set up Guardrails](https://developers.cloudflare.com/ai-gateway/features/guardrails/set-up-guardrail/).

## Related resources

  * [Cloudflare Learning Center: How to prevent misuse of AI ↗︎](https://www.cloudflare.com/learning/ai/ai-misuse/)
  * [Cloudflare Learning Center: How to prevent prompt injection ↗︎](https://www.cloudflare.com/learning/ai/prompt-injection/)
  * [Cloudflare Learning Center: What is AI security? ↗︎](https://www.cloudflare.com/learning/ai/what-is-ai-security/)
  * [Cloudflare Learning Center: What are the OWASP Top 10 risks for LLMs? ↗︎](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)
  * [Cloudflare Blog: Guardrails launch announcement ↗︎](https://blog.cloudflare.com/guardrails-in-ai-gateway/)



[PreviousSet up Data Loss Prevention (DLP)](https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/)[NextSet up Guardrails](https://developers.cloudflare.com/ai-gateway/features/guardrails/set-up-guardrail/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/features/guardrails/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
