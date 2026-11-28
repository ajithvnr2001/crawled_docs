---
url: https://docs.copilotkit.ai/reference/channels/
title: Channels SDK
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:17.057785+00:00
---

# Channels SDK

> Source: https://docs.copilotkit.ai/reference/channels/

Channels

# Channels SDK

API reference for managed and direct provider agents built with @copilotkit/channels.

Copy MarkdownOpen

The Channels SDK connects an agent to chat providers through a long-running `@copilotkit/channels` process. In the managed Slack and Microsoft Teams path, CopilotKit Intelligence owns the provider connection while your process owns the agent, tools, approvals, state, and deployment. The package also exports developer-operated direct adapters for Slack, Teams, Discord, and WhatsApp.

Use this tested package combination. Keep exact versions in your lockfile and verify compatibility before changing either package.

Terminal

Copy Text
    
    
    npm install --save-exact @copilotkit/channels@0.11.0 @copilotkit/runtime@1.73.3

## API referenceCopy Anchor Link

### [createChannelDeclare a managed provider or developer-operated direct adapter and attach the Channel to CopilotRuntime.](https://docs.copilotkit.ai/reference/channels/functions/createChannel)### [ChannelConfigure managed or direct delivery, register handlers and tools, configure storage, and inspect the Channel declaration.](https://docs.copilotkit.ai/reference/channels/classes/Channel)### [ThreadPost and update messages, run or resume the agent, read history, and manage conversation state.](https://docs.copilotkit.ai/reference/channels/classes/Thread)### [StateStorePersist workflow state, callback snapshots, transcripts, locks, deduplication, and queues.](https://docs.copilotkit.ai/reference/channels/types/StateStore)

### ClassesCopy Anchor Link

  * [`Channel`](https://docs.copilotkit.ai/reference/channels/classes/Channel)
  * [`Thread`](https://docs.copilotkit.ai/reference/channels/classes/Thread)
  * [`MemoryStore`](https://docs.copilotkit.ai/reference/channels/classes/MemoryStore)
  * [`Transcripts`](https://docs.copilotkit.ai/reference/channels/classes/Transcripts)



### FunctionsCopy Anchor Link

  * [`createChannel`](https://docs.copilotkit.ai/reference/channels/functions/createChannel)
  * [`defineChannelTool`](https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool)
  * [`defineChannelCommand`](https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand)
  * [`bind`](https://docs.copilotkit.ai/reference/channels/functions/bind)
  * [`renderToIR`](https://docs.copilotkit.ai/reference/channels/functions/renderToIR)



### Message componentsCopy Anchor Link

  * [`Message`](https://docs.copilotkit.ai/reference/channels/components/Message)
  * [`Header`](https://docs.copilotkit.ai/reference/channels/components/Header)
  * [`Section`](https://docs.copilotkit.ai/reference/channels/components/Section) and [`Markdown`](https://docs.copilotkit.ai/reference/channels/components/Markdown)
  * [`Fields` and `Field`](https://docs.copilotkit.ai/reference/channels/components/Fields)
  * [`Context`](https://docs.copilotkit.ai/reference/channels/components/Context)
  * [`Image`](https://docs.copilotkit.ai/reference/channels/components/Image) and [`Divider`](https://docs.copilotkit.ai/reference/channels/components/Divider)
  * [`Table`, `Row`, and `Cell`](https://docs.copilotkit.ai/reference/channels/components/Table)
  * [`Chart`](https://docs.copilotkit.ai/reference/channels/components/Chart)



### Interactive componentsCopy Anchor Link

  * [`Actions`](https://docs.copilotkit.ai/reference/channels/components/Actions)
  * [`Button`](https://docs.copilotkit.ai/reference/channels/components/Button)
  * [`Select`](https://docs.copilotkit.ai/reference/channels/components/Select)
  * [`Input`](https://docs.copilotkit.ai/reference/channels/components/Input)
  * [Modal components](https://docs.copilotkit.ai/reference/channels/components/Modal): exported for direct adapters; unavailable on managed Slack and Teams
  * [JSX callbacks](https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks)



### TypesCopy Anchor Link

  * [`IncomingMessage`](https://docs.copilotkit.ai/reference/channels/types/IncomingMessage)
  * [`AgentContentPart`](https://docs.copilotkit.ai/reference/channels/types/AgentContentPart)
  * [`InteractionContext`](https://docs.copilotkit.ai/reference/channels/types/InteractionContext)
  * [`MessageRef`](https://docs.copilotkit.ai/reference/channels/types/MessageRef)
  * [`StoreConfig`](https://docs.copilotkit.ai/reference/channels/types/StoreConfig)
  * [`StateStore`](https://docs.copilotkit.ai/reference/channels/types/StateStore)
  * [`ChannelNode`](https://docs.copilotkit.ai/reference/channels/types/ChannelNode)
  * [`ActionStore`](https://docs.copilotkit.ai/reference/channels/types/ActionStore): deprecated migration reference



### Provider SDKsCopy Anchor Link

  * [Direct provider adapters](https://docs.copilotkit.ai/reference/channels/sdk/direct-adapters): public entry points, required options, and the boundary between managed and developer-operated delivery



## Provider guidesCopy Anchor Link

Start with the provider and agent framework you are deploying:

  * [Connect and run your agent in Slack](https://docs.copilotkit.ai/slack/connect)
  * [Connect and run your agent in Microsoft Teams](https://docs.copilotkit.ai/teams/connect)



The provider picker in those guides keeps the same task and selected agent framework when you switch between Slack and Teams.

How is this guide?

GoodBad

[Previous PageSuggestionsConfig](https://docs.copilotkit.ai/reference/core/types/SuggestionsConfig)[Next PageChannel](https://docs.copilotkit.ai/reference/channels/classes/Channel)
