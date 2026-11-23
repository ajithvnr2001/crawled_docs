---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatView/
title: CopilotChatView
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:27.148240+00:00
---

# CopilotChatView

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatView/

Angular/Components

# CopilotChatView

Angular standalone component that renders the chat layout without agent wiring

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatView` is the layout-only chat view. It renders the message feed, the input container, the feather effect, the disclaimer, the suggestion pills, and a welcome screen when there are no messages. It does not wire an agent on its own. You pass it `messages` and read interaction handlers from the surrounding `ChatState`.

[`CopilotChat`](https://docs.copilotkit.ai/reference/angular/components/CopilotChat) wires the agent, messages, running state, suggestions, and submission, then renders `CopilotChatView`. Use `CopilotChatView` directly when you manage those values and handlers, or when you need full control over the layout and its slots.

The active slot inputs accept a component class (`*Component`) or an Angular template (`*Template`). The template takes precedence when both are set.

## UsageCopy Anchor Link

`CopilotChatView` is a standalone component with the selector `copilot-chat-view`. Its default input needs a `ChatState` provider. The example below supplies one.

src/app/chat.component.ts

Copy Text
    
    
    import { Component, forwardRef, signal } from "@angular/core";
    import { ChatState, CopilotChatView } from "@copilotkit/angular";
    import type { Message } from "@ag-ui/client";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      imports: [CopilotChatView],
      providers: [
        {
          provide: ChatState,
          useExisting: forwardRef(() => ChatComponent),
        },
      ],
      template: `
        <copilot-chat-view [messages]="messages()" [autoScroll]="true" />
      `,
    })
    export class ChatComponent extends ChatState {
      readonly messages = signal<Message[]>([]);
      readonly inputValue = signal("");
    
      submitInput(value: string) {
        // Send the message through your chat state owner.
      }
    
      changeInput(value: string) {
        this.inputValue.set(value);
      }
    }

## InputsCopy Anchor Link

### Core inputsCopy Anchor Link

Prop

Type

`messages?`Message[]

`state?`unknown

`agentId?`string

`autoScroll?`boolean

`showCursor?`boolean

`hasExplicitThreadId?`boolean

### Slot inputsCopy Anchor Link

The view forwards message, input, scroll-button, input-container, feather, and disclaimer slots.

Prop

Type

`messageViewComponent?`Type<any>

`messageViewTemplate?`TemplateRef<any>

`messageViewClass?`string

The current release declares `scrollViewComponent`, `scrollViewTemplate`, and `scrollViewClass`, but the default layout always uses its built-in scroll view. Use `customLayout` when you need to replace it.

Prop

Type

`assistantMessageComponent?`Type<any>

`assistantMessageTemplate?`TemplateRef<any>

`assistantMessageClass?`string

`reasoningMessageComponent?`Type<any>

`reasoningMessageTemplate?`TemplateRef<any>

`reasoningMessageClass?`string

`messageViewChildrenComponent?`Type<any>

`messageViewChildrenTemplate?`TemplateRef<any>

`messageViewChildrenClass?`string

`scrollToBottomButtonComponent?`Type<any>

`scrollToBottomButtonTemplate?`TemplateRef<any>

`scrollToBottomButtonClass?`string

`inputComponent?`Type<any>

`inputTemplate?`TemplateRef<any>

`inputContainerComponent?`Type<any>

`inputContainerTemplate?`TemplateRef<any>

`inputContainerClass?`string

`featherComponent?`Type<any>

`featherTemplate?`TemplateRef<any>

`featherClass` is declared but the current release does not pass its string value to the feather slot. Use a feather component or template to style that region.

Prop

Type

`disclaimerComponent?`Type<any>

`disclaimerTemplate?`TemplateRef<any>

`disclaimerClass?`string

`disclaimerText?`string

## OutputsCopy Anchor Link

`CopilotChatView` bubbles assistant-message actions from the message feed. Each payload is an object with the relevant `message`.

Prop

Type

`assistantMessageThumbsUp?`{ message: Message }

`assistantMessageThumbsDown?`{ message: Message }

`assistantMessageReadAloud?`{ message: Message }

`assistantMessageRegenerate?`{ message: Message }

The current release declares `userMessageCopy` and `userMessageEdit`, but the default message view does not emit them.

## Content projectionCopy Anchor Link

`CopilotChatView` supports one active projected template named `customLayout`.

Prop

Type

`customLayout?`TemplateRef<CopilotChatViewLayoutContext>

The class declares projected templates for input buttons and assistant-message parts, but the current release does not forward them. Configure those parts through `inputComponent`, the message slot inputs, or a custom layout.

### Custom layout exampleCopy Anchor Link

src/app/chat.component.ts

Copy Text
    
    
    import { Component, forwardRef, signal } from "@angular/core";
    import {
      ChatState,
      CopilotChatInput,
      CopilotChatMessageView,
      CopilotChatView,
    } from "@copilotkit/angular";
    import type { Message } from "@ag-ui/client";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      imports: [CopilotChatInput, CopilotChatMessageView, CopilotChatView],
      providers: [
        {
          provide: ChatState,
          useExisting: forwardRef(() => ChatComponent),
        },
      ],
      template: `
        <copilot-chat-view [messages]="messages()">
          <ng-template #customLayout>
            <div class="my-layout">
              <copilot-chat-message-view [messages]="messages()" />
              <copilot-chat-input />
            </div>
          </ng-template>
        </copilot-chat-view>
      `,
    })
    export class ChatComponent extends ChatState {
      readonly messages = signal<Message[]>([]);
      readonly inputValue = signal("");
    
      submitInput(value: string) {
        // Send the message through your chat state owner.
      }
    
      changeInput(value: string) {
        this.inputValue.set(value);
      }
    }

How is this guide?

GoodBad

[Previous PageCopilotChatUserMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage)[Next PageCopilotPopup](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)
