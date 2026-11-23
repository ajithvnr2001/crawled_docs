---
url: https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig/
title: injectCopilotKitConfig
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:25.483861+00:00
---

# injectCopilotKitConfig

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig/

Angular/Functions

# injectCopilotKitConfig

Angular function that reads the CopilotKitConfig provided through provideCopilotKit from the current injection context

Copy MarkdownOpen

## OverviewCopy Anchor Link

`injectCopilotKitConfig` returns the [`CopilotKitConfig`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit#parameters) that you registered with [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit). It reads the value bound to the `COPILOT_KIT_CONFIG` injection token, so it must run inside an Angular injection context (a constructor, a field initializer, or a factory).

Most applications do not call this directly. The [`CopilotKit`](https://docs.copilotkit.ai/reference/angular/services/CopilotKit) service uses it internally to build its core. Reach for it when you need to read the raw config you provided, for example to read your own `properties` or `runtimeUrl`.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { injectCopilotKitConfig } from "@copilotkit/angular";
    
    function injectCopilotKitConfig(): CopilotKitConfig;

## Return ValueCopy Anchor Link

Returns the `CopilotKitConfig` bound to the `COPILOT_KIT_CONFIG` token. This is the object that you passed to `provideCopilotKit`, unchanged.

## UsageCopy Anchor Link

Call it from an injection context, such as a service constructor or a component field initializer.

src/app/runtime-info.service.ts

Copy Text
    
    
    import { Injectable } from "@angular/core";
    import { injectCopilotKitConfig } from "@copilotkit/angular";
    
    @Injectable({ providedIn: "root" })
    export class RuntimeInfoService {
      private readonly config = injectCopilotKitConfig();
    
      get runtimeUrl(): string | undefined {
        return this.config.runtimeUrl;
      }
    }

How is this guide?

GoodBad

[Previous PageinjectChatLabels](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels)[Next PageinjectInterrupt](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)
