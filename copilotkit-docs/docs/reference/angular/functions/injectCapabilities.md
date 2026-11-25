---
url: https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities/
title: injectCapabilities
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:15.295605+00:00
---

# injectCapabilities

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities/

Angular/Functions

# injectCapabilities

Angular function for reading an agent's declared capabilities as a readonly signal.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`injectCapabilities` returns the [AG-UI `AgentCapabilities`](https://docs.ag-ui.com/concepts/capabilities) declared by the resolved agent as an Angular signal.

Capabilities are populated from the runtime `/info` response. This function is a convenience selector over [`injectAgentStore`](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore); it does not keep separate capability state or make its own request. The signal is `undefined` until runtime discovery completes or when the agent does not declare capabilities.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { injectCapabilities } from "@copilotkit/angular";
    import type { Signal } from "@angular/core";
    import type { AgentCapabilities } from "@ag-ui/core";
    
    function injectCapabilities(
      agentId?: string | Signal<string | undefined>,
    ): Signal<AgentCapabilities | undefined>;

## ParametersCopy Anchor Link

Prop

Type

`agentId?`string | Signal<string | undefined>

## Return ValueCopy Anchor Link

Prop

Type

`capabilities?`Signal<AgentCapabilities | undefined>

## UsageCopy Anchor Link

src/app/tool-panel.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { injectCapabilities } from "@copilotkit/angular";
    
    @Component({
      selector: "app-tool-panel",
      standalone: true,
      template: `
        @if (capabilities()?.tools?.supported === true) {
          <p>This agent supports tools.</p>
        }
      `,
    })
    export class ToolPanelComponent {
      readonly capabilities = injectCapabilities();
    }

To read another agent or switch reactively, pass its id or an id signal from a component class:

Copy Text
    
    
    import { signal } from "@angular/core";
    import { injectCapabilities } from "@copilotkit/angular";
    
    export class AgentCapabilitiesComponent {
      readonly agentId = signal<string | undefined>("support");
      readonly capabilities = injectCapabilities(this.agentId);
    }

How is this guide?

GoodBad

[Previous PageinjectAgentStore](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)[Next PageinjectChatLabels](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels)
