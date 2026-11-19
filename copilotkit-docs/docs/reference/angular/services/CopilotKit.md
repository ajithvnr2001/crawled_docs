---
url: https://docs.copilotkit.ai/reference/angular/services/CopilotKit/
title: CopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:38.416650+00:00
---

# CopilotKit

> Source: https://docs.copilotkit.ai/reference/angular/services/CopilotKit/

Angular/Services

# CopilotKit

The root Angular service that exposes CopilotKit agents, tools, runtime state, and suggestions as signals

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotKit` is the central injectable service for `@copilotkit/angular`. It is `providedIn: "root"`, so a single instance is shared across your application. It builds and owns the underlying `CopilotKitCore` from the [`CopilotKitConfig`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit#parameters) you registered with [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit), exposes reactive runtime state as Angular [signals](https://angular.dev/guide/signals), and provides methods to register tools, manage suggestions, and update the runtime connection.

In most apps you do not call its methods directly. The injectable functions such as [`registerFrontendTool`](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool), [`registerRenderToolCall`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall), and [`registerHumanInTheLoop`](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop) register against the current injector and remove registrations with the same name and optional agent id when that injector is destroyed. Inject the service when you need direct access to its signals or the `core` instance.

## Accessing the serviceCopy Anchor Link

Inject it from any injection context, for example a component or service.

src/app/status.component.ts

Copy Text
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-status",
      standalone: true,
      template: `<p>Status: {{ copilotKit.runtimeConnectionStatus() }}</p>`,
    })
    export class StatusComponent {
      protected readonly copilotKit = inject(CopilotKit);
    }

## SignalsCopy Anchor Link

All reactive state is exposed as read-only Angular signals. Read a signal by calling it, for example `copilotKit.agents()`.

Prop

Type

`agents?`Signal<Record<string, AbstractAgent>>

`runtimeConnectionStatus?`Signal<CopilotKitCoreRuntimeConnectionStatus>

`runtimeUrl?`Signal<string | undefined>

`runtimeTransport?`Signal<CopilotRuntimeTransport>

`headers?`Signal<Record<string, string>>

`credentials?`Signal<RequestCredentials | undefined>

`threadEndpoints?`Signal<ThreadEndpointRuntimeInfo | undefined>

`audioFileTranscriptionEnabled?`Signal<boolean>

`intelligence?`Signal<IntelligenceRuntimeInfo | undefined>

`licenseStatus?`Signal<RuntimeLicenseStatus | undefined>

`runtimeEntitlements?`Signal<RuntimeEntitlementResponse | undefined>

`runtimeEntitlementRetryPending?`Signal<boolean>

`suggestionsByAgent?`Signal<Record<string, CopilotKitCoreGetSuggestionsResult>>

`toolCallRenderConfigs?`Signal<RenderToolCallConfig[]>

`clientToolCallRenderConfigs?`Signal<FrontendToolConfig[]>

`humanInTheLoopToolRenderConfigs?`Signal<HumanInTheLoopConfig[]>

`activityMessageRenderConfigs?`Signal<RenderActivityMessageConfig[]>

## PropertiesCopy Anchor Link

Prop

Type

`core?`CopilotKitCore

`defaultToolRenderingEnabled?`boolean

## MethodsCopy Anchor Link

Prop

Type

`addFrontendTool?`(tool: FrontendToolConfig & { injector: Injector }) => void

`addRenderToolCall?`(renderConfig: RenderToolCallConfig) => void

`addRenderActivityMessage?`(renderConfig: RenderActivityMessageConfig) => void

`removeRenderActivityMessage?`(renderConfig: RenderActivityMessageConfig) => void

`addHumanInTheLoop?`(humanInTheLoopTool: HumanInTheLoopConfig) => void

`addSuggestionsConfig?`(config: SuggestionsConfig) => string

`removeSuggestionsConfig?`(id: string) => void

`getSuggestions?`(agentId: string) => CopilotKitCoreGetSuggestionsResult

`reloadSuggestions?`(agentId: string) => void

`clearSuggestions?`(agentId: string) => void

`removeTool?`(toolName: string, agentId?: string) => void

`getAgent?`(agentId: string) => AbstractAgent | undefined

`updateRuntime?`(options: { runtimeUrl?: string; runtimeTransport?: CopilotRuntimeTransport; headers?: CopilotKitHeadersSource; credentials?: RequestCredentials; messageFilter?: CopilotKitMessageFilter; properties?: Record<string, unknown>; agents?: Record<string, AbstractAgent>; selfManagedAgents?: Record<string, AbstractAgent> }) => void

## UsageCopy Anchor Link

### Read agents and connection status in a templateCopy Anchor Link

src/app/agents-panel.component.ts

Copy Text
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-agents-panel",
      standalone: true,
      template: `
        <p>Status: {{ copilotKit.runtimeConnectionStatus() }}</p>
        <ul>
          @for (id of agentIds(); track id) {
            <li>{{ id }}</li>
          }
        </ul>
      `,
    })
    export class AgentsPanelComponent {
      protected readonly copilotKit = inject(CopilotKit);
      protected readonly agentIds = () => Object.keys(this.copilotKit.agents());
    }

### Switch the runtime URL at runtimeCopy Anchor Link

src/app/runtime-switcher.component.ts

Copy Text
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-runtime-switcher",
      standalone: true,
      template: `<button (click)="useStaging()">Use staging</button>`,
    })
    export class RuntimeSwitcherComponent {
      private readonly copilotKit = inject(CopilotKit);
    
      protected useStaging(): void {
        this.copilotKit.updateRuntime({
          runtimeUrl: "https://staging.example.com/api/copilotkit",
        });
      }
    }

### Reload suggestions for an agentCopy Anchor Link

src/app/suggestions.component.ts

Copy Text
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-suggestions",
      standalone: true,
      template: `<button (click)="refresh()">Refresh suggestions</button>`,
    })
    export class SuggestionsComponent {
      private readonly copilotKit = inject(CopilotKit);
    
      protected refresh(): void {
        this.copilotKit.reloadSuggestions("default");
      }
    }

How is this guide?

GoodBad

[Previous PageregisterRenderToolCall](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)[Next PageOverview](https://docs.copilotkit.ai/reference/core)
