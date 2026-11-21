---
url: https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit/
title: provideCopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:49.288477+00:00
---

# provideCopilotKit

> Source: https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit/

Angular/Functions

# provideCopilotKit

Angular provider that configures CopilotKit through dependency injection: runtime URL, agents, tools, headers, and more

Copy MarkdownOpen

## OverviewCopy Anchor Link

`provideCopilotKit` is the primary setup entry point for `@copilotkit/angular`. It returns an Angular [`Provider`](https://angular.dev/guide/di/dependency-injection-providers) that you add to your application providers. The provider stores your `CopilotKitConfig` behind the `COPILOT_KIT_CONFIG` injection token, where the root [`CopilotKit`](https://docs.copilotkit.ai/reference/angular/services/CopilotKit) service reads it.

Register it once in `app.config.ts`. A component-local config provider alone does not configure the root `CopilotKit` service.

You typically configure the connection one of two ways: point at a CopilotKit runtime with `runtimeUrl`, or connect directly to one or more AG-UI agents with `selfManagedAgents`.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { provideCopilotKit } from "@copilotkit/angular";
    import type { Provider } from "@angular/core";
    
    function provideCopilotKit(config?: CopilotKitConfig): Provider;

## ParametersCopy Anchor Link

Prop

Type

`config?`CopilotKitConfig

## Return ValueCopy Anchor Link

Returns an Angular `Provider` that binds your config, unchanged, to the `COPILOT_KIT_CONFIG` injection token. Add it to the application providers. The root `CopilotKit` service adds the license-key header when it sends requests.

## UsageCopy Anchor Link

### Connect through a runtimeCopy Anchor Link

Point `runtimeUrl` at your CopilotKit runtime endpoint and register the provider in your application config.

src/app/app.config.ts

Copy Text
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
          headers: {
            Authorization: "Bearer <token>",
          },
          properties: {
            userId: "user_123",
          },
        }),
      ],
    };

Then add [`CopilotChat`](https://docs.copilotkit.ai/reference/angular/components/CopilotChat) to a template.

### Connect directly to an AG-UI agentCopy Anchor Link

To talk to an agent server without a CopilotKit runtime, pass `selfManagedAgents` with an `@ag-ui/client` agent such as `HttpAgent`.

src/app/app.config.ts

Copy Text
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    import { HttpAgent } from "@ag-ui/client";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          selfManagedAgents: {
            default: new HttpAgent({ url: "http://localhost:8000/" }),
          },
        }),
      ],
    };

### Register startup toolsCopy Anchor Link

Pass `frontendTools` to register client tools when the application starts. Their handlers run inside the root injection context, so they can use `inject()`.

src/app/app.config.ts

Copy Text
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    import { z } from "zod";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
          frontendTools: [
            {
              name: "sayHello",
              description: "Greet the user by name",
              parameters: z.object({ name: z.string() }),
              handler: async ({ name }) => `Hello, ${name}!`,
            },
          ],
        }),
      ],
    };

## BehaviorCopy Anchor Link

  * The provided config is bound to the `COPILOT_KIT_CONFIG` injection token. Read it with [`injectCopilotKitConfig`](https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig).
  * A format-valid `licenseKey` is merged into the `X-CopilotCloud-Public-Api-Key` header unless that header is already present.
  * `agents` and `selfManagedAgents` are merged together when the underlying core is created, so an id present in both resolves to the `selfManagedAgents` entry.
  * The Inspector receives that same core instance. Angular reuses an existing `cpk-web-inspector` element when present and removes only an element it created when the root service is destroyed.



How is this guide?

GoodBad

[Previous PageprovideCopilotChatLabels](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels)[Next PageprovideMCPApps](https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps)
