---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView/
title: CopilotChatMessageView
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:20.837564+00:00
---

# CopilotChatMessageView

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView/

Angular/Components

# CopilotChatMessageView

Angular standalone component that renders a list of chat messages, routing each message to assistant, user, reasoning, or activity rendering with slot customization.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatMessageView` renders an array of messages. It routes each message by its `role`:

  * `assistant`: [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage).
  * `user`: [`CopilotChatUserMessage`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage).
  * `reasoning`: the reasoning renderer.
  * `activity`: [`CopilotActivity`](https://docs.copilotkit.ai/reference/angular/components/CopilotActivity), which resolves the registered activity renderer.



It optionally renders a typing cursor at the end of the list while the agent is streaming.

This is the message-list layer used by [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView). Use it directly when you manage your own `messages` array and want the list without the surrounding scroll container and input.

The component is standalone and uses `OnPush` change detection. Reactive inputs are Angular [signals](https://angular.dev/guide/signals).

## UsageCopy Anchor Link

Import the component class and use its `copilot-chat-message-view` selector in your template.

src/app/messages.component.ts

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotChatMessageView } from "@copilotkit/angular";
    import type { Message } from "@ag-ui/core";
    
    @Component({
      selector: "app-messages",
      standalone: true,
      imports: [CopilotChatMessageView],
      template: `
        <copilot-chat-message-view
          [messages]="messages()"
          [showCursor]="isLoading()"
          [isLoading]="isLoading()"
        />
      `,
    })
    export class MessagesComponent {
      messages = signal<Message[]>([]);
      isLoading = signal(false);
    }

## InputsCopy Anchor Link

Prop

Type

`messages?`Message[]

`showCursor?`boolean

`isLoading?`boolean

`state?`unknown

`inputClass?`string

`agentId?`string

### Assistant message slot inputsCopy Anchor Link

Prop

Type

`assistantMessageComponent?`Type<any>

`assistantMessageTemplate?`TemplateRef<any>

`assistantMessageClass?`string

### User message slot inputsCopy Anchor Link

Prop

Type

`userMessageComponent?`Type<any>

`userMessageTemplate?`TemplateRef<any>

`userMessageClass?`string

### Reasoning message slot inputsCopy Anchor Link

Prop

Type

`reasoningMessageComponent?`Type<any>

`reasoningMessageTemplate?`TemplateRef<any>

`reasoningMessageClass?`string

### Content after the message listCopy Anchor Link

Prop

Type

`childrenComponent?`Type<any>

`childrenTemplate?`TemplateRef<any>

`childrenClass?`string

### Cursor slot inputsCopy Anchor Link

Prop

Type

`cursorComponent?`Type<any>

`cursorTemplate?`TemplateRef<any>

`cursorClass?`string

## OutputsCopy Anchor Link

Assistant actions bubble up from the assistant-message child component. Each payload is `{ message: Message }`.

Prop

Type

`assistantMessageThumbsUp?`{ message: Message }

`assistantMessageThumbsDown?`{ message: Message }

`assistantMessageReadAloud?`{ message: Message }

`assistantMessageRegenerate?`{ message: Message }

The current release declares `userMessageCopy` and `userMessageEdit`, but the default user-message child does not forward those events. Listen on a custom user-message component when you need them.

## Custom layoutCopy Anchor Link

For full control over how the list is laid out, project a template named `customLayout`. It receives a context object with the current `messages`, the `isLoading` and `showCursor` flags, and `messageElements` (the messages filtered to the renderable roles). When this template is present, the default list rendering is replaced entirely.

src/app/messages.component.html

Copy Text
    
    
    <copilot-chat-message-view [messages]="messages()" [showCursor]="isLoading()">
      <ng-template #customLayout let-messages="messages" let-showCursor="showCursor">
        <div class="my-list">
          @for (message of messages; track message.id) {
            <div class="my-row">{{ message.content }}</div>
          }
          @if (showCursor) {
            <span class="my-cursor">...</span>
          }
        </div>
      </ng-template>
    </copilot-chat-message-view>

## Customizing message renderingCopy Anchor Link

To swap out how a whole role is rendered without rebuilding the layout, pass a slot input. The slot accepts either a component class or a template, with the template taking precedence.

src/app/messages.component.ts

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotChatMessageView } from "@copilotkit/angular";
    import { MyAssistantMessage } from "./my-assistant-message.component";
    import type { Message } from "@ag-ui/core";
    
    @Component({
      selector: "app-messages",
      standalone: true,
      imports: [CopilotChatMessageView],
      template: `
        <copilot-chat-message-view
          [messages]="messages()"
          [assistantMessageComponent]="assistantMessage"
        />
      `,
    })
    export class MessagesComponent {
      messages = signal<Message[]>([]);
      protected readonly assistantMessage = MyAssistantMessage;
    }

How is this guide?

GoodBad

[Previous PageCopilotChatInput](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput)[Next PageCopilotChatUserMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage)
