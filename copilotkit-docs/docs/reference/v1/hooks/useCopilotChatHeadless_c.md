---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c/
title: useCopilotChatHeadless_c
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:27.035876+00:00
---

# useCopilotChatHeadless_c

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c/

React/v1

# useCopilotChatHeadless_c

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`useCopilotChatHeadless_c` has no direct v2 replacement. In v2, build headless UI on [`useAgent`](https://docs.copilotkit.ai/reference/v2/hooks/useAgent). See [Headless UI](https://docs.copilotkit.ai/custom-look-and-feel/headless-ui).

`useCopilotChatHeadless_c` is for building fully custom UI (headless UI) implementations.

This is a CopilotKit Intelligence feature

Read more about [CopilotKit Intelligence](https://docs.copilotkit.ai/intelligence/overview).

Usage is generous and **free** to get started.

The hook needs a public license key. Without one, it returns no-op functions.

## Key FeaturesCopy Anchor Link

  * **Fully headless** : Build your own fully custom UI's for your agentic applications.
  * **Advanced Suggestions** : Direct access to suggestions array with full control
  * **Interrupt Handling** : Interrupt content for human-in-the-loop workflows
  * **MCP Server Support** : Model Context Protocol server configurations



## UsageCopy Anchor Link

### Basic SetupCopy Anchor Link

Copy Text
    
    
    import { CopilotKit } from "@copilotkit/react-core";
    import { useCopilotChatHeadless_c } from "@copilotkit/react-core";
    
    export function App() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit" publicLicenseKey="YOUR_PUBLIC_LICENSE_KEY">
          <YourComponent />
        </CopilotKit>
      );
    }
    
    export function YourComponent() {
      const { messages, sendMessage, isLoading } = useCopilotChatHeadless_c();
    
      const handleSendMessage = async () => {
        await sendMessage({
          id: "123",
          role: "user",
          content: "Hello World",
        });
      };
    
      return (
        <div>
          {messages.map(msg => <div key={msg.id}>{msg.content}</div>)}
          <button onClick={handleSendMessage} disabled={isLoading}>
            Send Message
          </button>
        </div>
      );
    }

### Working with SuggestionsCopy Anchor Link

Copy Text
    
    
    import { useCopilotChatHeadless_c, useCopilotChatSuggestions } from "@copilotkit/react-core";
    
    export function SuggestionExample() {
      const {
        suggestions,
        setSuggestions,
        generateSuggestions,
        isLoadingSuggestions
      } = useCopilotChatHeadless_c();
    
      // Configure AI suggestion generation
      useCopilotChatSuggestions({
        instructions: "Suggest helpful actions based on the current context",
        maxSuggestions: 3
      });
    
      return (
        <div>
          {suggestions.map(suggestion => (
            <button key={suggestion.title}>{suggestion.title}</button>
          ))}
          <button onClick={generateSuggestions} disabled={isLoadingSuggestions}>
            Generate Suggestions
          </button>
        </div>
      );
    }

## Return ValuesCopy Anchor Link

The following properties are returned from the hook:

Prop

Type

`messages?`Message[]

`sendMessage?`(message: Message, options?) => Promise<void>

`setMessages?`(messages: Message[] | DeprecatedGqlMessage[]) => void

`deleteMessage?`(messageId: string) => void

`reloadMessages?`(messageId: string) => Promise<void>

`stopGeneration?`() => void

`reset?`() => void

`isLoading?`boolean

`runChatCompletion?`() => Promise<Message[]>

`mcpServers?`MCPServerConfig[]

`setMcpServers?`(servers: MCPServerConfig[]) => void

`suggestions?`Suggestion[]

`setSuggestions?`(suggestions: Omit<Suggestion, 'isLoading'>[]) => void

`generateSuggestions?`() => Promise<void>

`resetSuggestions?`() => void

`isLoadingSuggestions?`boolean

`interrupt?`string | React.ReactElement | null

`isAvailable?`boolean

`agent?`AbstractAgent | undefined

`threadId?`string | undefined

## ParametersCopy Anchor Link

Prop

Type

`suggestions?`'auto' | 'manual' | Omit<Suggestion, 'isLoading'>[]

`onInProgress?`(isLoading: boolean) => void

`onSubmitMessage?`(messageContent: string) => Promise<void> | void

`onStopGeneration?`OnStopGeneration

`onReloadMessages?`OnReloadMessages

How is this guide?

GoodBad

[Previous PageuseCopilotChat](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChat)[Next PageuseCopilotChatSuggestions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatSuggestions)
