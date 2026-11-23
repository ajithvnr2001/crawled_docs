---
url: https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels/
title: provideCopilotChatLabels
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:25.094780+00:00
---

# provideCopilotChatLabels

> Source: https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels/

Angular/Functions

# provideCopilotChatLabels

Angular provider that overrides the default text labels used by the CopilotKit chat components

Copy MarkdownOpen

## OverviewCopy Anchor Link

`provideCopilotChatLabels` returns an Angular [`Provider`](https://angular.dev/guide/di/dependency-injection-providers) that customizes the text labels used throughout the [prebuilt chat components](https://docs.copilotkit.ai/reference/angular/components/CopilotChat), such as the input placeholder, toolbar button labels, the disclaimer text, and the welcome message. You pass a partial set of labels and they are merged over the defaults, so you only override the strings you want to change.

Add it to an application or component `providers` array. Components read the merged labels through [`injectChatLabels`](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels).

The full set of defaults lives in `COPILOT_CHAT_DEFAULT_LABELS`. Any field you omit falls back to its default value.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { provideCopilotChatLabels } from "@copilotkit/angular";
    import type { Provider } from "@angular/core";
    
    function provideCopilotChatLabels(
      config: Partial<CopilotChatLabels>,
    ): Provider;

## ParametersCopy Anchor Link

Prop

Type

`config`Partial<CopilotChatLabels>

## Return ValueCopy Anchor Link

Returns an Angular `Provider` that binds the merged labels to the `COPILOT_CHAT_LABELS` injection token.

## UsageCopy Anchor Link

Override a few labels in your application config. Everything you do not list keeps its default.

src/app/app.config.ts

Copy Text
    
    
    import { ApplicationConfig } from "@angular/core";
    import {
      provideCopilotKit,
      provideCopilotChatLabels,
    } from "@copilotkit/angular";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({ runtimeUrl: "/api/copilotkit" }),
        provideCopilotChatLabels({
          chatInputPlaceholder: "Ask me anything...",
          welcomeMessageText: "Welcome! What can I help you build?",
        }),
      ],
    };

You can also scope labels to part of your app by adding the provider to a feature component's `providers` array instead of the application config.

How is this guide?

GoodBad

[Previous PageinjectThreads](https://docs.copilotkit.ai/reference/angular/functions/injectThreads)[Next PageprovideCopilotKit](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)
