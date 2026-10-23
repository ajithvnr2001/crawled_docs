---
url: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/cursor/
title: Cursor \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-17T06:26:04.621774+00:00
---

# Cursor · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/cursor/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Integrations

  4. /[Coding agents](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/)
  5. /Cursor



# Cursor

Last updated Oct 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites

[Cursor ↗︎](https://cursor.com/) supports a custom OpenAI base URL for models that use a custom API key. Point it at AI Gateway's [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) to route Cursor chat and agent requests through AI Gateway. Cursor sends requests through its servers, so your AI Gateway endpoint must be publicly reachable.

## Prerequisites

Before you start, you need:

  * Your Cloudflare account ID. To find it, refer to [Find your account and zone IDs](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).
  * A [Cloudflare API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with **Account** > **Workers AI** > **Read** permission.
  * [Credits loaded](https://developers.cloudflare.com/ai-gateway/features/unified-billing/#load-credits) on your account for third-party models.
  * [Cursor ↗︎](https://cursor.com/downloads) installed and updated to the latest version.



  1. In Cursor, go to **Cursor Settings** > **Models**. Under **API Keys** , enter your Cloudflare API token in the **OpenAI API Key** field, then select **Save**.

  2. Turn on **Override OpenAI Base URL**. Enter the following value, replacing `<ACCOUNT_ID>` with your Cloudflare account ID:
         
         https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai/v1

Note

If Cursor does not show **Override OpenAI Base URL** , this Cursor version or plan does not support routing OpenAI-compatible requests through AI Gateway.

  3. Select **\+ Add Custom Model**. Enter a model name, then turn on the model.

Use a Workers AI model for chat, such as `@cf/meta/llama-3.3-70b-instruct-fp8-fast`. For agent mode, use a third-party model that supports the OpenAI Responses API, such as `openai/gpt-4.1-mini`.

For available models, refer to the [model catalog](https://developers.cloudflare.com/ai/models/).

  4. Select the custom model in Cursor and send a prompt. Requests now route through AI Gateway.




Note

Workers AI models work with Cursor chat requests through the OpenAI Chat Completions API. Cursor agent mode uses the OpenAI Responses API. Use a third-party Responses-compatible model, such as `openai/gpt-4.1-mini`, for agent mode.

To confirm traffic reaches AI Gateway, refer to [Verify it works](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/#verify-it-works).

[PreviousClaude Desktop](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-desktop/)[NextGitHub Copilot CLI](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/github-copilot-cli/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/coding-agents/cursor.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
