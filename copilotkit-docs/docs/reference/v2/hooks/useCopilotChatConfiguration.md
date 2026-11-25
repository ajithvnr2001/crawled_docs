---
url: https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration/
title: useCopilotChatConfiguration
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:10.914309+00:00
---

# useCopilotChatConfiguration

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration/

React/Hooks

# useCopilotChatConfiguration

React hook and provider for chat UI configuration and labels

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useCopilotChatConfiguration` is a React hook that reads the chat configuration context. It returns the configuration value from the nearest `CopilotChatConfigurationProvider`, or `null` if no provider is present.

Wrap your chat in `CopilotChatConfigurationProvider` to change its labels, bind it to an agent and thread, or control its modal. Read those values in any child with `useCopilotChatConfiguration`. [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) wraps its children in this provider.

## CopilotChatConfigurationProviderCopy Anchor Link

A provider component that exposes localized labels, agent and thread IDs, and modal state to all descendant chat components.

### SignatureCopy Anchor Link

Copy Text
    
    
    import { CopilotChatConfigurationProvider } from "@copilotkit/react-core/v2";
    
    <CopilotChatConfigurationProvider
      labels={...}
      agentId="my-agent"
      threadId="thread-123"
      isModalDefaultOpen={true}
    >
      {children}
    </CopilotChatConfigurationProvider>

### PropsCopy Anchor Link

Prop

Type

`children`ReactNode

`labels?`Partial<CopilotChatLabels>

`agentId?`string

`threadId?`string

`isModalDefaultOpen?`boolean

## useCopilotChatConfigurationCopy Anchor Link

### SignatureCopy Anchor Link

Copy Text
    
    
    import { useCopilotChatConfiguration } from "@copilotkit/react-core/v2";
    
    function useCopilotChatConfiguration(): CopilotChatConfigurationValue | null;

### ParametersCopy Anchor Link

This hook takes no parameters.

### Return ValueCopy Anchor Link

Returns `null` if used outside of a `CopilotChatConfigurationProvider`. Otherwise returns a `CopilotChatConfigurationValue` object:

Prop

Type

`config?`CopilotChatConfigurationValue

## CopilotChatLabelsCopy Anchor Link

The `CopilotChatLabels` type defines all customizable text strings used by the chat UI. The following keys are available with their default values:

Key| Default Value  
---|---  
`chatInputPlaceholder`| `"Type a message..."`  
`chatInputToolbarStartTranscribeButtonLabel`| `"Transcribe"`  
`chatInputToolbarCancelTranscribeButtonLabel`| `"Cancel"`  
`chatInputToolbarFinishTranscribeButtonLabel`| `"Finish"`  
`chatInputToolbarAddButtonLabel`| `"Add attachments"`  
`chatInputToolbarToolsButtonLabel`| `"Tools"`  
`chatInputToolbarSendButtonLabel`| `"Send message"`  
`chatInputToolbarStopButtonLabel`| `"Stop"`  
`assistantMessageToolbarCopyCodeLabel`| `"Copy"`  
`assistantMessageToolbarCopyCodeCopiedLabel`| `"Copied"`  
`assistantMessageToolbarCopyMessageLabel`| `"Copy"`  
`assistantMessageToolbarThumbsUpLabel`| `"Good response"`  
`assistantMessageToolbarThumbsDownLabel`| `"Bad response"`  
`assistantMessageFeedbackCommentPlaceholder`| `"Add a comment (optional)"`  
`assistantMessageFeedbackCommentSubmitLabel`| `"Send comment"`  
`assistantMessageToolbarReadAloudLabel`| `"Read aloud"`  
`assistantMessageToolbarRegenerateLabel`| `"Regenerate"`  
`userMessageToolbarCopyMessageLabel`| `"Copy"`  
`userMessageToolbarEditMessageLabel`| `"Edit"`  
`userMessageToolbarPreviousBranchLabel`| `"Previous branch"`  
`userMessageToolbarNextBranchLabel`| `"Next branch"`  
`chatDisclaimerText`| `"AI can make mistakes. Please verify important information."`  
`chatToggleOpenLabel`| `"Open chat"`  
`chatToggleCloseLabel`| `"Close chat"`  
`chatScrollToBottomLabel`| `"Scroll to bottom"`  
`modalHeaderTitle`| `"CopilotKit Chat"`  
`welcomeMessageText`| `"How can I help you today?"`  
`reasoningMessageThinkingLabel`| `"Thinking…"`  
`chatInputSlashMenuLabel`| `"Slash commands"`  
`chatInputSlashMenuEmptyText`| `"No commands found"`  
`attachmentRemoveButtonLabel`| `"Remove attachment"`  
`attachmentPlayVideoButtonLabel`| `"Play video"`  
`attachmentPreviewCloseButtonLabel`| `"Close preview"`  
`modalHeaderCloseButtonLabel`| `"Close"`  
`modalHeaderThreadsButtonLabel`| `"Open threads"`  
`sidebarLabel`| `"Copilot chat sidebar"`  
  
## UsageCopy Anchor Link

### Basic Label CustomizationCopy Anchor Link

Copy Text
    
    
    import {
      CopilotChatConfigurationProvider,
      useCopilotChatConfiguration,
    } from "@copilotkit/react-core/v2";
    
    function App() {
      return (
        <CopilotChatConfigurationProvider
          labels={{
            chatInputPlaceholder: "Ask me anything...",
            modalHeaderTitle: "AI Assistant",
            welcomeMessageText: "Hello! What can I do for you?",
            chatDisclaimerText: "Responses are AI-generated.",
          }}
        >
          <ChatUI />
        </CopilotChatConfigurationProvider>
      );
    }

### Reading Configuration in a ComponentCopy Anchor Link

Copy Text
    
    
    function ChatHeader() {
      const config = useCopilotChatConfiguration();
    
      if (!config) {
        return <h2>Chat</h2>;
      }
    
      return <h2>{config.labels.modalHeaderTitle}</h2>;
    }

### Binding to a Specific Agent and ThreadCopy Anchor Link

Copy Text
    
    
    function SupportChat() {
      return (
        <CopilotChatConfigurationProvider
          agentId="support-agent"
          threadId="ticket-456"
          labels={{
            chatInputPlaceholder: "Describe your issue...",
            modalHeaderTitle: "Support Chat",
          }}
        >
          <ChatWindow />
        </CopilotChatConfigurationProvider>
      );
    }

### Modal State ManagementCopy Anchor Link

Copy Text
    
    
    import {
      CopilotChatConfigurationProvider,
      useCopilotChatConfiguration,
    } from "@copilotkit/react-core/v2";
    
    function App() {
      return (
        <CopilotChatConfigurationProvider isModalDefaultOpen={false}>
          <ToggleButton />
          <ChatModal />
        </CopilotChatConfigurationProvider>
      );
    }
    
    function ToggleButton() {
      const config = useCopilotChatConfiguration();
    
      if (!config?.setModalOpen) return null;
    
      return (
        <button onClick={() => config.setModalOpen!(!config.isModalOpen)}>
          {config.isModalOpen
            ? config.labels.chatToggleCloseLabel
            : config.labels.chatToggleOpenLabel}
        </button>
      );
    }

### Nested ProvidersCopy Anchor Link

Providers can be nested. Child providers inherit and merge labels from their parent, with child overrides taking precedence.

Copy Text
    
    
    function App() {
      return (
        <CopilotChatConfigurationProvider
          labels={{ chatDisclaimerText: "Company-wide disclaimer." }}
        >
          <CopilotChatConfigurationProvider
            agentId="sales"
            labels={{ modalHeaderTitle: "Sales Assistant" }}
          >
            {/* This context has both the company disclaimer and the sales title */}
            <SalesChat />
          </CopilotChatConfigurationProvider>
        </CopilotChatConfigurationProvider>
      );
    }

## BehaviorCopy Anchor Link

  * **Label Merging** : Labels are merged in order: built-in defaults, then parent provider labels, then current provider labels. This allows partial overrides at any level.
  * **Agent ID Resolution** : The `agentId` resolves from the nearest provider, falling back to parent providers, then to the `agentId` on `CopilotKitProvider`, then to `"default"`. [`useSuggestions`](https://docs.copilotkit.ai/reference/hooks/useSuggestions) reads this `agentId` when you do not pass one.
  * **Thread ID Generation** : If no `threadId` is provided at any level, a random UUID is generated and remains stable for the lifetime of the provider.
  * **Modal State Ownership** : A provider that sets `isModalDefaultOpen` owns its modal state (`isModalOpen` and `setModalOpen`). A nested provider without this prop uses the parent state. A top-level provider without this prop owns its state, and the modal starts open.
  * **Null Return** : The hook returns `null` when used outside any `CopilotChatConfigurationProvider`, rather than throwing an error. Components should handle this case.



How is this guide?

GoodBad

[Previous PageuseConfigureSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions)[Next PageuseCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)
