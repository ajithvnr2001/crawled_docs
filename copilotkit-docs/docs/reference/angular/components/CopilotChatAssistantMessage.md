---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage/
title: CopilotChatAssistantMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:27.193809+00:00
---

# CopilotChatAssistantMessage

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage/

Angular/Components

# CopilotChatAssistantMessage

Angular standalone component that renders a single assistant message with markdown content, tool calls, and a toolbar of copy, thumbs, read-aloud, and regenerate actions.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatAssistantMessage` renders one assistant message. It shows the message content through a markdown renderer, renders attached tool calls, and shows a toolbar with copy, thumbs up/down, read-aloud, and regenerate actions.

The toolbar appears only when the message has non-empty text content. Inside the toolbar:

  * Copy: always renders.
  * Thumbs up and thumbs down: render when you provide a custom slot for them, or when a thumbs handler is available from a surrounding [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView).
  * Read aloud and regenerate: render only when you provide a custom slot for them.



By default, [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView) renders this component for every assistant message.

The component is standalone and uses `OnPush` change detection. Reactive inputs are Angular [signals](https://angular.dev/guide/signals).

## UsageCopy Anchor Link

Import the component class and use its `copilot-chat-assistant-message` selector. The `message` input is required.

src/app/assistant.component.ts

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotChatAssistantMessage } from "@copilotkit/angular";
    import type { AssistantMessage } from "@ag-ui/client";
    
    @Component({
      selector: "app-assistant",
      standalone: true,
      imports: [CopilotChatAssistantMessage],
      template: `
        <copilot-chat-assistant-message [message]="message()" />
      `,
    })
    export class AssistantComponent {
      message = signal<AssistantMessage>({
        id: "1",
        role: "assistant",
        content: "Hello, how can I help?",
      });
    }

## InputsCopy Anchor Link

Prop

Type

`message`AssistantMessage

`messages?`Message[]

`agentId?`string

`isLoading?`boolean

`toolbarVisible?`boolean

`additionalToolbarItems?`TemplateRef<any>

### Slot class inputsCopy Anchor Link

The current release applies `markdownRendererClass`, `toolbarClass`, and `copyButtonClass` to their default parts.

Prop

Type

`markdownRendererClass?`string

`toolbarClass?`string

`copyButtonClass?`string

`inputClass`, the thumbs, read-aloud, regenerate class inputs, and `toolCallsViewClass` are declared but do not affect rendering in the current release. Use component or template overrides for those parts.

### Slot component inputsCopy Anchor Link

Each of these replaces the corresponding default sub-component with a component class of your own. Content-projection templates (see below) take precedence over these.

Prop

Type

`markdownRendererComponent?`Type<any>

`toolbarComponent?`Type<any>

`copyButtonComponent?`Type<any>

`thumbsUpButtonComponent?`Type<any>

`thumbsDownButtonComponent?`Type<any>

`readAloudButtonComponent?`Type<any>

`regenerateButtonComponent?`Type<any>

`toolCallsViewComponent?`Type<any>

## OutputsCopy Anchor Link

Prop

Type

`thumbsUp?`CopilotChatAssistantMessageOnThumbsUpProps

`thumbsDown?`CopilotChatAssistantMessageOnThumbsDownProps

`readAloud?`CopilotChatAssistantMessageOnReadAloudProps

`regenerate?`CopilotChatAssistantMessageOnRegenerateProps

## Slots and content projectionCopy Anchor Link

You can override any piece of the message by projecting a named template. A projected template takes precedence over the matching `*Component` input. Each template receives a typed context object.

Template name| Context type| Replaces  
---|---|---  
`markdownRenderer`| `AssistantMessageMarkdownRendererContext` (`{ content: string }`)| The markdown content renderer  
`toolbar`| `AssistantMessageToolbarContext` (`{ children?: any }`)| The whole toolbar  
`copyButton`| `AssistantMessageCopyButtonContext` (`{ content?: string }`)| The copy button  
`thumbsUpButton`| `ThumbsUpButtonContext` (empty; click via outputs)| The thumbs-up button  
`thumbsDownButton`| `ThumbsDownButtonContext` (empty; click via outputs)| The thumbs-down button  
`readAloudButton`| `ReadAloudButtonContext` (empty; click via outputs)| The read-aloud button  
`regenerateButton`| `RegenerateButtonContext` (empty; click via outputs)| The regenerate button  
`toolCallsView`| `any`| The tool calls view  
  
src/app/assistant.component.html

Copy Text
    
    
    <copilot-chat-assistant-message [message]="message()">
      <ng-template #markdownRenderer let-content="content">
        <article class="my-markdown">{{ content }}</article>
      </ng-template>
    </copilot-chat-assistant-message>

How is this guide?

GoodBad

[Previous PageCopilotChat](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)[Next PageCopilotChatInput](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput)
