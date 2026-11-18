---
url: https://docs.copilotkit.ai/angular/prebuilt-components/
title: Prebuilt Components
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.713182+00:00
---

# Prebuilt Components

> Source: https://docs.copilotkit.ai/angular/prebuilt-components/

Chat

# Prebuilt Components

Add a full Angular chat and choose its layout, inline, popup, or sidebar.

Copy MarkdownOpen

`CopilotChat` gives you a complete chat surface backed by the agent from your Copilot Runtime. It owns message streaming, suggestions, the composer, attachments, transcription, and the active thread.

You need the provider from the [Angular quickstart](https://docs.copilotkit.ai/angular).

## Choose a chat surfaceCopy Anchor Link

Surface| Use it when  
---|---  
`CopilotChat`| Chat belongs inside an existing page or panel.  
`CopilotPopup`| Chat should open from a floating launcher.  
`CopilotSidebar`| Chat should sit beside the main application or open as an overlay.  
`CopilotChatView`| You own the agent wiring and only need the chat layout.  
  
All four are standalone Angular components.

## Add an inline chatCopy Anchor Link

Import `CopilotChat`, give its host a real height, and point it at an agent when you do not want the default agent.

src/app/support-chat.component.ts

Copy Text
    
    
    import { ChangeDetectionStrategy, Component } from "@angular/core";
    import { CopilotChat } from "@copilotkit/angular";
    
    @Component({
      selector: "app-support-chat",
      imports: [CopilotChat],
      changeDetection: ChangeDetectionStrategy.OnPush,
      template: `
        <section class="chat-shell" aria-label="Support assistant">
          <copilot-chat agentId="support" />
        </section>
      `,
      styles: `
        .chat-shell {
          height: min(48rem, 80vh);
          overflow: hidden;
          border: 1px solid #dbe3eb;
          border-radius: 1rem;
        }
      `,
    })
    export class SupportChatComponent {}

Import the package stylesheet once in the application's global stylesheet:

src/styles.css

Copy Text
    
    
    @import "@copilotkit/angular/styles.css";

## Use a popup or sidebarCopy Anchor Link

Both modal surfaces manage focus, Escape closing, and launcher-focus restore. Their `open` model supports two-way binding.

src/app/app.component.ts

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotPopup, CopilotSidebar } from "@copilotkit/angular";
    
    @Component({
      selector: "app-root",
      imports: [CopilotPopup, CopilotSidebar],
      template: `
        <copilot-popup
          [(open)]="popupOpen"
          title="Support assistant"
          [clickOutsideToClose]="true"
        />
    
        <copilot-sidebar
          [(open)]="sidebarOpen"
          mode="docked"
          position="right"
          title="Workspace assistant"
          [width]="480"
        />
      `,
    })
    export class AppComponent {
      readonly popupOpen = signal(false);
      readonly sidebarOpen = signal(false);
    }

Compact viewports render the sidebar as a modal even when `mode` is `"docked"`. Only one open docked sidebar can own the page margin at a time.

Run `npm start` and open the app. Click the popup launcher button. The popup opens, and a message you send gets its reply in the popup.

## Next stepsCopy Anchor Link

  * [Slots](https://docs.copilotkit.ai/angular/custom-look-and-feel/slots): replace an assistant message or another part of the chat.
  * [CSS customization](https://docs.copilotkit.ai/angular/custom-look-and-feel/css): restyle the chat classes.
  * [CopilotChat API](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)
  * [CopilotChatView slots](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)
  * [CopilotPopup API](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)
  * [CopilotSidebar API](https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar)



How is this guide?

GoodBad

[Previous PageIntelligence](https://docs.copilotkit.ai/angular/intelligence/overview)[Next PageCSS Customization](https://docs.copilotkit.ai/angular/custom-look-and-feel/css)
