---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage/
title: CopilotChatUserMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:26.909257+00:00
---

# CopilotChatUserMessage

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage/

Angular/Components

# CopilotChatUserMessage

Angular standalone component that renders a single user message with attachments, copy and edit actions, and branch navigation.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatUserMessage` renders one user message. It shows image or file attachments, renders the message text, and shows a toolbar with copy and edit actions. When the message belongs to a set of regenerated branches, a branch control lets you move between them.

The copy and edit buttons always render. The branch navigation control renders only when `numberOfBranches` is greater than 1.

By default, [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView) renders this component for every user message.

The component is standalone and uses `OnPush` change detection. Reactive inputs are Angular [signals](https://angular.dev/guide/signals).

## UsageCopy Anchor Link

Import the component class and use its `copilot-chat-user-message` selector.

src/app/user-message.component.ts

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotChatUserMessage } from "@copilotkit/angular";
    import type { UserMessage } from "@ag-ui/core";
    
    @Component({
      selector: "app-user-message",
      standalone: true,
      imports: [CopilotChatUserMessage],
      template: `
        <copilot-chat-user-message
          [message]="message()"
          (editMessage)="onEdit($event)"
        />
      `,
    })
    export class UserMessageComponent {
      message = signal<UserMessage>({
        id: "1",
        role: "user",
        content: "What is the weather today?",
      });
    
      onEdit(event: { message: UserMessage }) {
        console.log("edit", event.message.id);
      }
    }

## InputsCopy Anchor Link

Prop

Type

`message?`UserMessage

`branchIndex?`number

`numberOfBranches?`number

`additionalToolbarItems?`TemplateRef<any>

`inputClass?`string

### Slot class inputsCopy Anchor Link

Each of these passes extra CSS classes to the corresponding default sub-component.

Prop

Type

`messageRendererClass?`string

`toolbarClass?`string

`copyButtonClass?`string

`editButtonClass?`string

`branchNavigationClass?`string

### Slot component inputsCopy Anchor Link

Each of these replaces the corresponding default sub-component with a component class of your own. Content-projection templates (see below) take precedence over these.

Prop

Type

`messageRendererComponent?`Type<any>

`toolbarComponent?`Type<any>

`copyButtonComponent?`Type<any>

`editButtonComponent?`Type<any>

`branchNavigationComponent?`Type<any>

## OutputsCopy Anchor Link

Prop

Type

`editMessage?`CopilotChatUserMessageOnEditMessageProps

`switchToBranch?`CopilotChatUserMessageOnSwitchToBranchProps

## Slots and content projectionCopy Anchor Link

You can override any piece of the message by projecting a named template. A projected template takes precedence over the matching `*Component` input. Each template receives a typed context object.

Template name| Context type| Replaces  
---|---|---  
`messageRenderer`| `MessageRendererContext` (`{ content: string }`)| The message text renderer  
`toolbar`| `UserMessageToolbarContext` (`{ children?: any }`)| The whole toolbar  
`copyButton`| `CopyButtonContext` (`{ content?: string; copied?: boolean }`)| The copy button  
`editButton`| `EditButtonContext` (empty; click via outputs)| The edit button  
`branchNavigation`| `BranchNavigationContext` (`{ currentBranch, numberOfBranches, onSwitchToBranch?, message }`)| The branch navigation control  
  
src/app/user-message.component.html

Copy Text
    
    
    <copilot-chat-user-message [message]="message()">
      <ng-template #messageRenderer let-content="content">
        <p class="my-user-text">{{ content }}</p>
      </ng-template>
    </copilot-chat-user-message>

How is this guide?

GoodBad

[Previous PageCopilotChatMessageView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView)[Next PageCopilotChatView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)
