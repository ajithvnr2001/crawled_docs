---
url: https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore/
title: injectAgentStore
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:26.480166+00:00
---

# injectAgentStore

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore/

Angular/Functions

# injectAgentStore

Angular function that subscribes to an AG-UI agent and returns a signal of reactive agent state (messages, state, isRunning) for @copilotkit/angular.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`injectAgentStore` subscribes to an [AG-UI agent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) and returns an Angular `Signal<AgentStore>`. The `AgentStore` exposes the agent instance plus its reactive state (messages, shared state, and run status) as Angular signals, so your component re-renders automatically when the agent changes.

Read the store by calling the outer signal, then read each member by calling its signal: `store().messages()`, `store().isRunning()`, `store().state()`. The `agent` member is the plain AG-UI instance (not a signal), so you read it directly: `store().agent`.

Call it from an injection context such as a constructor or field initializer. The subscription is torn down automatically when the owning component or service is destroyed.

Agent resolution is lazy and reactive. After the runtime syncs, reading the store signal throws an error if no agent matches `agentId`. The error lists the known agents. To find the cause, compare `agentId` with the agents in your runtime `/info` response and in `agents` or `selfManagedAgents`.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { injectAgentStore } from "@copilotkit/angular";
    import type { Signal } from "@angular/core";
    
    function injectAgentStore(
      agentId: string | Signal<string | undefined>,
    ): Signal<AgentStore>;

## ParametersCopy Anchor Link

Prop

Type

`agentId`string | Signal<string | undefined>

## Return ValueCopy Anchor Link

Prop

Type

`store?`Signal<AgentStore>

## UsageCopy Anchor Link

### Basic usageCopy Anchor Link

src/app/agent-status.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-agent-status",
      standalone: true,
      template: `
        <div>Messages: {{ store().messages().length }}</div>
        <div>Running: {{ store().isRunning() ? "Yes" : "No" }}</div>
      `,
    })
    export class AgentStatusComponent {
      readonly store = injectAgentStore("default");
    }

### Reading and updating shared stateCopy Anchor Link

Read the state via the signal, and write it through the agent instance.

src/app/theme-panel.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { JsonPipe } from "@angular/common";
    import { injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-theme-panel",
      standalone: true,
      imports: [JsonPipe],
      template: `
        <pre>{{ store().state() | json }}</pre>
        <button (click)="setDark()">Dark theme</button>
      `,
    })
    export class ThemePanelComponent {
      readonly store = injectAgentStore("default");
    
      setDark() {
        const agent = this.store().agent;
        agent.setState({ ...(agent.state as object), theme: "dark" });
      }
    }

### Switching agents reactivelyCopy Anchor Link

Pass a signal so the store re-resolves when the selected agent id changes.

src/app/multi-agent.component.ts

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-multi-agent",
      standalone: true,
      template: `
        <button (click)="agentId.set('support')">Support</button>
        <button (click)="agentId.set('sales')">Sales</button>
        <div>Active: {{ store().agent.agentId }}</div>
        <div>Messages: {{ store().messages().length }}</div>
      `,
    })
    export class MultiAgentComponent {
      readonly agentId = signal<string | undefined>("support");
      readonly store = injectAgentStore(this.agentId);
    }

## BehaviorCopy Anchor Link

  * **Reactive resolution.** The returned signal recomputes when the `agentId`, the set of available agents, the runtime connection status, the runtime URL or transport, or the request headers change.
  * **Provisional agents.** When a runtime is configured but not yet connected, a provisional proxied runtime agent is created and cached so the store has something to render before the runtime syncs.
  * **Automatic cleanup.** The agent subscription is unsubscribed when the owning component or service is destroyed. Switching to a new agent tears down the previous store's subscription first, including its interrupt controller.
  * **Error on missing agent.** If no agent resolves after the runtime has synced, reading the store signal throws an error that lists the known agent ids.



How is this guide?

GoodBad

[Previous PageconnectAgentContext](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)[Next PageinjectCapabilities](https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities)
