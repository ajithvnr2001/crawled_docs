---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:20.513219+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChat/

Angular/Components

# CopilotChat

Angular standalone component that wires an agent to a complete chat UI

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChat` is the all-in-one chat component. It wires an agent into [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView) so you get a working chat interface with one selector. It does this work for you:

  * Resolves the agent through [`injectAgentStore`](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore).
  * Subscribes to the agent's messages and running state.
  * Manages suggestions.
  * Tracks the input value.
  * Handles audio transcription.
  * Wires file attachments.
  * Clears the input after each message is sent.



`CopilotChat` extends `ChatState` and provides itself to the view and input beneath it. You usually only need to point it at an agent.

For the layout without the agent wiring, use [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView) directly.

## UsageCopy Anchor Link

`CopilotChat` is a standalone component with the selector `copilot-chat`. Import the class into your component's `imports` array and use the element in the template. The chat reads its configuration from [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit), so the provider must be in scope.

src/app/app.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { CopilotChat } from "@copilotkit/angular";
    
    @Component({
      selector: "app-root",
      standalone: true,
      imports: [CopilotChat],
      template: `<copilot-chat />`,
    })
    export class AppComponent {}

Remember to import the stylesheet once in your global styles:

src/styles.css

Copy Text
    
    
    @import "@copilotkit/angular/styles.css";

## InputsCopy Anchor Link

Prop

Type

`agentId?`string

`threadId?`string

`attachments?`AttachmentsConfig

`inputComponent?`Type<any>

`assistantMessageComponent?`Type<any>

`assistantMessageTemplate?`TemplateRef<any>

`assistantMessageClass?`string

`reasoningMessageComponent?`Type<any>

`reasoningMessageTemplate?`TemplateRef<any>

`reasoningMessageClass?`string

`messageViewChildrenComponent?`Type<any>

`messageViewChildrenTemplate?`TemplateRef<any>

`messageViewChildrenClass?`string

## OutputsCopy Anchor Link

`CopilotChat` does not declare its own outputs. It handles message submission, suggestion selection, and transcription internally through the `ChatState` it provides to the input and view. To observe lower-level interactions, render a custom input via `inputComponent` (or use [`CopilotChatInput`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput) directly), which exposes outputs such as `submitMessage` and the transcription events.

## CustomizationCopy Anchor Link

`CopilotChat` keeps the layout simple and delegates slot customization to the view it renders. Swap the input area with the `inputComponent` input, or compose the layout yourself with [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView), which exposes slot inputs for the message view, feather, disclaimer, and input container, plus a `customLayout` template. To change the input buttons, use `inputComponent`.

To customize the text strings (input placeholder, welcome message, toolbar labels, disclaimer), provide labels through [`provideCopilotChatLabels`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels). The chat reads them through `injectChatLabels` internally.

How is this guide?

GoodBad

[Previous PageCopilotActivity](https://docs.copilotkit.ai/reference/angular/components/CopilotActivity)[Next PageCopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage)
