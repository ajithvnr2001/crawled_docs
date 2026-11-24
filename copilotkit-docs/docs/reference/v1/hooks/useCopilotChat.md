---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChat/
title: useCopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:48.439690+00:00
---

# useCopilotChat

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChat/

React/v1

# useCopilotChat

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`useCopilotChat` is a lightweight React hook for headless chat interactions.

**Open Source Friendly** \- Works without requiring a free public license key.

Looking for fully headless UI?

Get started with [useCopilotChatHeadless_c](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c).

## Use CasesCopy Anchor Link

  * **Programmatic Messaging** : Send messages without displaying chat UI
  * **Programmatic control** : Control prebuilt component programmatically
  * **Background Operations** : Trigger AI interactions in the background
  * **Fire-and-Forget** : Send messages without needing to read responses



## UsageCopy Anchor Link

Copy Text
    
    
    import { TextMessage, Role } from "@copilotkit/runtime-client-gql";
    
    const { appendMessage } = useCopilotChat();
    
    // Example usage without naming conflicts
    const handleSendMessage = async (content: string) => {
      await appendMessage(
        new TextMessage({
          role: Role.User,
          content,
        })
      );
    };

## Return ValuesCopy Anchor Link

The following properties are returned from the hook:

Prop

Type

`visibleMessages?`DeprecatedGqlMessage[]

`appendMessage?`(message: DeprecatedGqlMessage, options?) => Promise<void>

`reloadMessages?`(messageId: string) => Promise<void>

`stopGeneration?`() => void

`reset?`() => void

`isLoading?`boolean

`isAvailable?`boolean

`runChatCompletion?`() => Promise<Message[]>

`mcpServers?`MCPServerConfig[]

`setMcpServers?`(servers: MCPServerConfig[]) => void

## ParametersCopy Anchor Link

Prop

Type

`id?`string

`headers?`Record<string, string> | Headers

`initialMessages?`Message[]

`makeSystemMessage?`SystemMessageFunction

`disableSystemMessage?`boolean

`suggestions?`ChatSuggestions

`onInProgress?`(isLoading: boolean) => void

`onSubmitMessage?`(messageContent: string) => Promise<void> | void

`onStopGeneration?`OnStopGeneration

`onReloadMessages?`OnReloadMessages

How is this guide?

GoodBad

[Previous PageuseCopilotAdditionalInstructions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAdditionalInstructions)[Next PageuseCopilotChatHeadless_c](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c)
