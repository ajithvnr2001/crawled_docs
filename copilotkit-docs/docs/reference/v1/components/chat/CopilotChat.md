---
url: https://docs.copilotkit.ai/reference/v1/components/chat/CopilotChat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:21.015947+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/reference/v1/components/chat/CopilotChat/

React/v1/[Chat Components](https://docs.copilotkit.ai/reference/v1/components/chat)

# CopilotChat

The CopilotChat component, providing a chat interface for interacting with your copilot.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

In v2, use [`CopilotChat`](https://docs.copilotkit.ai/reference/v2/components/CopilotChat) from `@copilotkit/react-core/v2`.

  
![](https://cdn.copilotkit.ai/docs/copilotkit/images/CopilotChat.gif)

A chatbot panel component for the CopilotKit framework. The component allows for a high degree of customization through various props and custom CSS.

## Install DependenciesCopy Anchor Link

This component is part of the [@copilotkit/react-ui](https://npmjs.com/package/@copilotkit/react-ui) package.

Copy Text
    
    
    npm install @copilotkit/react-core @copilotkit/react-ui

## UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotChat } from "@copilotkit/react-ui";
    import "@copilotkit/react-ui/styles.css";
    
    <CopilotChat
      labels={{
        title: "Your Assistant",
        initial: "Hi! 👋 How can I assist you today?",
      }}
    />

### With Observability HooksCopy Anchor Link

To monitor user interactions, set `publicLicenseKey` on `<CopilotKit>` and pass the `observabilityHooks` prop. Without the key, the hooks do not run and the chat shows an error banner.

Copy Text
    
    
    <CopilotKit publicLicenseKey="YOUR_PUBLIC_LICENSE_KEY">
      <CopilotChat
        observabilityHooks={{
          onMessageSent: (message) => {
            console.log("Message sent:", message);
          },
        }}
      />
    </CopilotKit>

### Look & FeelCopy Anchor Link

By default, CopilotKit components do not have any styles. You can import CopilotKit's stylesheet at the root of your project:

YourRootComponent.tsx

Copy Text
    
    
    ...
    import "@copilotkit/react-ui/styles.css";
    
    export function YourRootComponent() {
      return (
        <CopilotKit>
          ...
        </CopilotKit>
      );
    }

For more information about how to customize the styles, check out the [Customize Look & Feel](https://docs.copilotkit.ai/custom-look-and-feel/css) guide.

## PropertiesCopy Anchor Link

Prop

Type

`instructions?`string

`suggestions?`ChatSuggestions

`onInProgress?`(inProgress: boolean) => void

`onSubmitMessage?`(message: string) => void | Promise<void>

`onStopGeneration?`OnStopGeneration

`onReloadMessages?`OnReloadMessages

`onRegenerate?`(messageId: string) => void

`onCopy?`(message: string) => void

`onThumbsUp?`(message: Message, isActive?: boolean) => void

`onThumbsDown?`(message: Message, isActive?: boolean) => void

`markdownTagRenderers?`ComponentsMap

`icons?`CopilotChatIcons

`labels?`CopilotChatLabels

`attachments?`AttachmentsConfig

`makeSystemMessage?`SystemMessageFunction

`disableSystemMessage?`boolean

`AssistantMessage?`React.ComponentType<AssistantMessageProps>

`UserMessage?`React.ComponentType<UserMessageProps>

`ErrorMessage?`React.ComponentType<ErrorMessageProps>

`Messages?`React.ComponentType<MessagesProps>

`RenderMessage?`React.ComponentType<RenderMessageProps>

`RenderSuggestionsList?`React.ComponentType<RenderSuggestionsListProps>

`Input?`React.ComponentType<InputProps>

`className?`string

`children?`React.ReactNode

`hideStopButton?`boolean

`observabilityHooks?`CopilotObservabilityHooks

`renderError?`(error: { message: string; operation?: string; timestamp: number; onDismiss: () => void; onRetry?: () => void; }) => React.ReactNode

`onError?`CopilotErrorHandler

How is this guide?

GoodBad

[Previous PageAll Chat Components](https://docs.copilotkit.ai/reference/v1/components/chat)[Next PageCopilotPopup](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotPopup)
