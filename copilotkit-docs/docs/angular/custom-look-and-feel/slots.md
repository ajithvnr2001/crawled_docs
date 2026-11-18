---
url: https://docs.copilotkit.ai/angular/custom-look-and-feel/slots/
title: Slots (Subcomponents)
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:52.672481+00:00
---

# Slots (Subcomponents)

> Source: https://docs.copilotkit.ai/angular/custom-look-and-feel/slots/

Chat/Custom Look and Feel

# Slots (Subcomponents)

Replace an assistant message or another part of the Angular chat with your own standalone component or template.

Copy MarkdownOpen

Swap one part of the prebuilt chat from [Prebuilt Components](https://docs.copilotkit.ai/angular/prebuilt-components) for your own standalone component or template. The rest of the chat keeps working as before.

## Replace an assistant messageCopy Anchor Link

Pass a standalone component class to `assistantMessageComponent`. CopilotKit creates it for each assistant message and binds its `message` input.

src/app/custom-assistant-message.component.ts

Copy Text
    
    
    import { ChangeDetectionStrategy, Component, input } from "@angular/core";
    
    type AssistantMessage = {
      id: string;
      role: "assistant";
      content?: string;
    };
    
    @Component({
      selector: "app-custom-assistant-message",
      changeDetection: ChangeDetectionStrategy.OnPush,
      template: `
        <article class="answer">
          <span class="answer__label">Assistant</span>
          <p>{{ message().content }}</p>
        </article>
      `,
    })
    export class CustomAssistantMessageComponent {
      readonly message = input.required<AssistantMessage>();
    }

src/app/support-chat.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { CopilotChat } from "@copilotkit/angular";
    import { CustomAssistantMessageComponent } from "./custom-assistant-message.component";
    
    @Component({
      selector: "app-support-chat",
      imports: [CopilotChat],
      template: `
        <copilot-chat
          [assistantMessageComponent]="assistantMessageComponent"
          assistantMessageClass="support-answer"
        />
      `,
    })
    export class SupportChatComponent {
      protected readonly assistantMessageComponent =
        CustomAssistantMessageComponent;
    }

`CopilotChat` also accepts component or template slots for reasoning messages, the composer, and content after the transcript. Use `CopilotChatView` directly when you need its scroll view, disclaimer, feather, input-container, or scroll-to-bottom slots.

## Next stepsCopy Anchor Link

  * [CopilotChat API](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)
  * [CopilotChatView slots](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)
  * [CSS customization](https://docs.copilotkit.ai/angular/custom-look-and-feel/css)



How is this guide?

GoodBad

[Previous PageCSS Customization](https://docs.copilotkit.ai/angular/custom-look-and-feel/css)[Next PageHeadless UI](https://docs.copilotkit.ai/angular/custom-look-and-feel/headless-ui)
