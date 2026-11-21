---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage/
title: CopilotChatUserMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:45.542664+00:00
---

# CopilotChatUserMessage

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage/

React/Components

# CopilotChatUserMessage

Component for displaying user-authored messages with branch navigation

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatUserMessage` shows user-authored messages aligned to the right with optional branch navigation. The default message renderer formats content with `white-space: pre-wrap` to preserve line breaks. Branch navigation controls only render when `numberOfBranches` is greater than 1 and an `onSwitchToBranch` handler is provided. Users can then move between the alternative branches of the conversation.

[`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView) renders this component for each user message. For assistant messages, see [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage).

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChatUserMessage } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## PropsCopy Anchor Link

Prop

Type

`message`UserMessage

`onEditMessage?`(props: { message: UserMessage }) => void

`onSwitchToBranch?`(props: { message: UserMessage; branchIndex: number; numberOfBranches: number }) => void

`branchIndex?`number

`numberOfBranches?`number

`additionalToolbarItems?`React.ReactNode

## SlotsCopy Anchor Link

All slot props follow the CopilotKit slot system: each accepts a replacement React component, a `className` string that is merged into the default component's classes, or a partial props object that extends the default component.

Prop

Type

`messageRenderer?`typeof CopilotChatUserMessage.MessageRenderer | string | Partial<React.ComponentProps<typeof CopilotChatUserMessage.MessageRenderer>>

`toolbar?`typeof CopilotChatUserMessage.Toolbar | string | Partial<React.ComponentProps<typeof CopilotChatUserMessage.Toolbar>>

`copyButton?`typeof CopilotChatUserMessage.CopyButton | string | Partial<React.ComponentProps<typeof CopilotChatUserMessage.CopyButton>>

`editButton?`typeof CopilotChatUserMessage.EditButton | string | Partial<React.ComponentProps<typeof CopilotChatUserMessage.EditButton>>

`branchNavigation?`typeof CopilotChatUserMessage.BranchNavigation | string | Partial<React.ComponentProps<typeof CopilotChatUserMessage.BranchNavigation>>

## UsageCopy Anchor Link

### Basic User MessageCopy Anchor Link

Copy Text
    
    
    function UserBubble({ message }) {
      return <CopilotChatUserMessage message={message} />;
    }

### With Edit SupportCopy Anchor Link

Copy Text
    
    
    function EditableUserMessage({ message, onEdit }) {
      return (
        <CopilotChatUserMessage
          message={message}
          onEditMessage={({ message }) => onEdit(message)}
        />
      );
    }

### With Branch NavigationCopy Anchor Link

Copy Text
    
    
    function BranchedUserMessage({
      message,
      branchIndex,
      totalBranches,
      onSwitch,
    }) {
      return (
        <CopilotChatUserMessage
          message={message}
          branchIndex={branchIndex}
          numberOfBranches={totalBranches}
          onSwitchToBranch={({ branchIndex }) => onSwitch(branchIndex)}
        />
      );
    }

### Customizing Appearance with SlotsCopy Anchor Link

Copy Text
    
    
    function StyledUserMessage({ message }) {
      return (
        <CopilotChatUserMessage
          message={message}
          messageRenderer="bg-blue-600 text-white rounded-2xl px-4 py-2"
          toolbar="mt-1"
          onEditMessage={({ message }) => console.log("Edit:", message.id)}
          additionalToolbarItems={
            <button onClick={() => console.log("Pin:", message.id)}>Pin</button>
          }
        />
      );
    }

### Full Edit and Branch WorkflowCopy Anchor Link

Copy Text
    
    
    function FullFeaturedUserMessage({ message, branches }) {
      const [currentBranch, setCurrentBranch] = useState(0);
    
      return (
        <CopilotChatUserMessage
          message={message}
          branchIndex={currentBranch}
          numberOfBranches={branches.length}
          onSwitchToBranch={({ branchIndex }) => setCurrentBranch(branchIndex)}
          onEditMessage={({ message }) => {
            // Open edit modal
            openEditModal(message);
          }}
        />
      );
    }

## BehaviorCopy Anchor Link

  * **Right-Aligned Layout** : User messages are rendered with right-aligned positioning to visually distinguish them from assistant messages.
  * **Whitespace Preservation** : The default message renderer uses `white-space: pre-wrap`, so line breaks and spacing in the original message are preserved.
  * **Conditional Branch Navigation** : The branch navigation controls are only rendered when both conditions are met: `numberOfBranches > 1` and `onSwitchToBranch` is provided. This prevents showing navigation for single-branch conversations.
  * **Conditional Edit Button** : The edit button only appears in the toolbar when `onEditMessage` is provided.
  * **Localized Labels** : Toolbar button tooltips are sourced from the nearest `CopilotChatConfigurationProvider`. See [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration) for available label keys.



How is this guide?

GoodBad

[Previous PageCopilotChatToolCallGroup](https://docs.copilotkit.ai/reference/v2/components/CopilotChatToolCallGroup)[Next PageCopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)
