---
url: https://docs.copilotkit.ai/angular/custom-look-and-feel/headless-ui/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:52.636226+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/angular/custom-look-and-feel/headless-ui/

Chat/Custom Look and Feel

# Headless UI

Render your own Angular transcript and composer on CopilotKit's signal-based agent store.

Copy MarkdownOpen

Use this page when you need more than the default `CopilotChat` and want to render the whole chat yourself.

## Build a headless chatCopy Anchor Link

`injectAgentStore` gives you the state needed to render your own transcript and composer. Add the user message to the agent, then run that same agent through `CopilotKitCore`.

src/app/headless-chat.component.ts

Copy Text
    
    
    import { Component, inject, signal } from "@angular/core";
    import { CopilotKit, injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-headless-chat",
      template: `
        <div aria-live="polite">
          @for (message of store().messages(); track message.id) {
            <article [attr.data-role]="message.role">
              {{ message.content }}
            </article>
          }
          @if (store().isRunning()) {
            <p>Agent is working…</p>
          }
        </div>
    
        <textarea
          aria-label="Message"
          [value]="draft()"
          (input)="updateDraft($event)"
        ></textarea>
        <button
          type="button"
          [disabled]="store().isRunning() || !draft().trim()"
          (click)="send()"
        >
          Send
        </button>
      `,
    })
    export class HeadlessChatComponent {
      private readonly copilotKit = inject(CopilotKit);
      readonly store = injectAgentStore("default");
      readonly draft = signal("");
    
      protected updateDraft(event: Event): void {
        this.draft.set((event.target as HTMLTextAreaElement).value);
      }
    
      protected async send(): Promise<void> {
        const content = this.draft().trim();
        if (!content || this.store().isRunning()) return;
    
        const agent = this.store().agent;
        agent.addMessage({
          id: crypto.randomUUID(),
          role: "user",
          content,
        });
        this.draft.set("");
        await this.copilotKit.core.runAgent({ agent });
      }
    }

Add error handling around `runAgent` in production and disable repeated sends while `isRunning()` is true. The store tears down its agent subscription with the owning injector.

Type a message and click **Send**. Your message appears, then "Agent is working…", then the agent's reply.

## Next stepsCopy Anchor Link

  * [injectAgentStore API](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)



How is this guide?

GoodBad

[Previous PageSlots (Subcomponents)](https://docs.copilotkit.ai/angular/custom-look-and-feel/slots)[Next PageMultimodal Attachments](https://docs.copilotkit.ai/angular/multimodal-attachments)
