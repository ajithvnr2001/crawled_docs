---
url: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/android-studio/
title: Android Studio \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:19.267503+00:00
---

# Android Studio · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/android-studio/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Integrations

  4. /[Coding agents](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/)
  5. /Android Studio



# Android Studio

Last updated Oct 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesConfigure the built-in AI assistantConfigure GitHub Copilot Chat

[Android Studio ↗︎](https://developer.android.com/studio) supports custom model providers through its built-in AI assistant and the [GitHub Copilot plugin ↗︎](https://plugins.jetbrains.com/plugin/17718-github-copilot). Point a provider at AI Gateway's [OpenAI-compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) to route requests through your gateway. Authenticate with a Cloudflare API token and use [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) or a stored [provider key](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/) to authenticate with the model provider.

Configure the assistant you use. The built-in AI assistant and GitHub Copilot Chat have separate provider settings.

## Prerequisites

Before you start, you need:

  * Your Cloudflare account ID. To find it, refer to [Find your account and zone IDs](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).
  * An [authenticated AI Gateway](https://developers.cloudflare.com/ai-gateway/configuration/authentication/). You can use your account's `default` gateway or [create a gateway](https://developers.cloudflare.com/ai-gateway/get-started/) and use its slug.
  * A [Cloudflare API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with **Account** > **AI Gateway** > **Run** permission.
  * [Unified Billing credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/#load-credits) or a stored [provider key](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/) for the models you select.
  * Android Studio installed. For the built-in AI assistant, use a version with support for third-party remote model providers. For GitHub Copilot Chat, install the latest [GitHub Copilot plugin ↗︎](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=jetbrains) and complete its sign-in flow.



## Configure the built-in AI assistant

  1. In Android Studio settings, go to **Tools** > **AI** > **Model Providers**.

  2. Select **Add** > **Third-Party Remote Provider**.

  3. For **Description** , enter a name such as `Cloudflare AI Gateway`.

  4. For **URL** , enter the following value. Replace `<ACCOUNT_ID>` and `<GATEWAY_ID>` with your Cloudflare account ID and gateway slug. You can use `default` as the gateway slug.
         
         https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/<GATEWAY_ID>/compat

Enter the base URL without `/chat/completions`. Android Studio retrieves the model list before you select a model.

Note

The `/compat` endpoint is deprecated for standard single-model calls. This integration uses it because Android Studio retrieves a model list during setup. The recommended [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) does not provide a `/v1/models` endpoint.

  5. For **URL Schema** , select **OpenAI-compatible**. For **API key** , enter your Cloudflare API token.

  6. Select **Refresh** to retrieve the model list. Select the models you want to use, then select **OK** to save your settings.

Choose models supported by your Unified Billing credits or stored provider keys. A model appearing in the list does not mean you have configured credentials for it.

  7. Open the AI chat window. Use the model picker to select a model from your remote provider, then send a prompt.




Some specialized Android Studio AI features may not work with third-party models. For feature compatibility, refer to [Use a remote model ↗︎](https://developer.android.com/studio/gemini/use-a-remote-model).

## Configure GitHub Copilot Chat

Use a custom endpoint provider in GitHub Copilot Chat. Select **Chat Completions** explicitly for this configuration.

  1. Open **GitHub Copilot Chat**. In the model picker, select **Manage Models**.

  2. In **Language Models (Copilot)** , select **Add Models** , then select the custom endpoint provider option.

  3. In **Add Custom Endpoint Provider** , enter the following values:

     * **Provider Name** : `Cloudflare AI Gateway`.
     * **API Key** : your Cloudflare API token.
     * **API Type** : **Chat Completions**.
  4. Select **Save**. In the **Add Model** dialog, enter a model ID in `provider/model` format. For example, enter `openai/gpt-4.1-mini`.

Choose a model supported by your Unified Billing credits or stored provider keys.

  5. For **Deployment URL** , enter the following value. Replace `<ACCOUNT_ID>` and `<GATEWAY_ID>` with your Cloudflare account ID and gateway slug:
         
         https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/<GATEWAY_ID>/compat/chat/completions

Include `/chat/completions`. Unlike the built-in assistant, this field takes the full endpoint URL.

  6. For **Model Friendly Display Name** , enter a name such as `GPT-4.1 mini via AI Gateway`. Set the token limits and capabilities to match your model. For `openai/gpt-4.1-mini`, you can use the following settings:

     * **Max Input Tokens** : `128000`.
     * **Max Output Tokens** : `16000`.
     * **Support Tool Calling** : selected.
     * **Support Vision** : selected.
     * **Custom Request Headers** : not selected.
  7. Select **Save** , then **OK**. Start a new Copilot chat and select your custom model from the model picker.

  8. Send a prompt such as `Reply with exactly: copilot-gateway-test`. Confirm that Copilot displays the reply.




To confirm traffic reaches AI Gateway, refer to [Verify it works](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/#verify-it-works).

[PreviousXcode](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/xcode/)[NextGemini CLI](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/gemini-cli/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/coding-agents/android-studio.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
