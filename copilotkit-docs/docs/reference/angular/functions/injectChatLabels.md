---
url: https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels/
title: injectChatLabels
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:17.049860+00:00
---

# injectChatLabels

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels/

Angular/Functions

# injectChatLabels

Angular function that returns the CopilotKit chat labels, with provided overrides merged over the defaults

Copy MarkdownOpen

## OverviewCopy Anchor Link

`injectChatLabels` returns the full set of [`CopilotChatLabels`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels#parameters) in scope: any labels you provided through [`provideCopilotChatLabels`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels) merged over `COPILOT_CHAT_DEFAULT_LABELS`. If no labels were provided, it returns the defaults unchanged.

It reads the `COPILOT_CHAT_LABELS` injection token (optionally), so it must run inside an Angular injection context (a constructor, a field initializer, or a factory). The prebuilt chat components call it internally; use it directly when you build your own chat UI and want the same configurable strings.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { injectChatLabels } from "@copilotkit/angular";
    
    function injectChatLabels(): CopilotChatLabels;

## Return ValueCopy Anchor Link

Returns a complete `CopilotChatLabels` object. Because the value is the merge of your overrides over the defaults, every field is always present (never `undefined`).

## UsageCopy Anchor Link

Call it from an injection context and read the labels you need.

src/app/my-chat.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { injectChatLabels } from "@copilotkit/angular";
    
    @Component({
      selector: "app-my-chat",
      standalone: true,
      template: `<input [placeholder]="labels.chatInputPlaceholder" />`,
    })
    export class MyChatComponent {
      protected readonly labels = injectChatLabels();
    }

How is this guide?

GoodBad

[Previous PageinjectCapabilities](https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities)[Next PageinjectCopilotKitConfig](https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig)
