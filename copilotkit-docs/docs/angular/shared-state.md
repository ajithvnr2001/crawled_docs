---
url: https://docs.copilotkit.ai/angular/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.672888+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/angular/shared-state/

Shared state

# Shared State

Read and write agent state with Angular signals, and choose between shared state and agent context.

Copy MarkdownOpen

Shared state and agent context solve two different data flows.

Data flow| Use  
---|---  
Agent and application both read and write the value| `injectAgentStore` and `agent.setState`  
The application owns the value and the agent only reads it| `connectAgentContext` or `CopilotKitAgentContext`  
  
This page covers shared state. For values the agent only reads, see [Agent Read-Only Context](https://docs.copilotkit.ai/angular/shared-state/agent-readonly).

## Read agent stateCopy Anchor Link

`injectAgentStore` returns a signal that resolves one agent. The store exposes messages, state, and run status as nested signals.

src/app/workspace.component.ts

Copy Text
    
    
    import { Component, computed } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    type WorkspaceState = {
      notes: string[];
      priority: "low" | "normal" | "high";
    };
    
    const EMPTY_STATE: WorkspaceState = {
      notes: [],
      priority: "normal",
    };
    
    @Component({
      selector: "app-workspace",
      template: `
        <p>Priority: {{ state().priority }}</p>
        <ul>
          @for (note of state().notes; track note) {
            <li>{{ note }}</li>
          }
        </ul>
        <button type="button" (click)="setPriority('high')">
          Mark high priority
        </button>
      `,
    })
    export class WorkspaceComponent {
      readonly store = injectAgentStore("default");
      readonly state = computed(
        () => (this.store().state() as WorkspaceState | undefined) ?? EMPTY_STATE,
      );
    
      protected setPriority(priority: WorkspaceState["priority"]): void {
        const agent = this.store().agent;
        const current = (agent.state as WorkspaceState | undefined) ?? EMPTY_STATE;
        agent.setState({ ...current, priority });
      }
    }

Read through `store().state()` so Angular tracks changes. Write through the plain AG-UI agent at `store().agent`. Replace the object instead of mutating it in place.

Click **Mark high priority** , then ask the agent for the current priority. It answers "high".

The same store gives you:

  * `store().messages()` for the current conversation
  * `store().isRunning()` for loading controls
  * `store().agent` for `setState`, `addMessage`, and `abortRun`



To start a run, call `inject(CopilotKit).core.runAgent({ agent })`, as in the [headless chat](https://docs.copilotkit.ai/angular/custom-look-and-feel/headless-ui#build-a-headless-chat). That call sends your registered frontend tools and agent context with the run.

## Keep ownership clearCopy Anchor Link

  * Use shared state for data that the agent may change.
  * Use context for application-owned facts.
  * Keep durable user preferences in your own data store; publish only the part the current agent needs.
  * Scope `injectAgentStore` to the same agent id as the chat or workflow that reads the state.



## Next stepsCopy Anchor Link

  * [injectAgentStore API](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)
  * [Agent Read-Only Context](https://docs.copilotkit.ai/angular/shared-state/agent-readonly)



How is this guide?

GoodBad

[Previous PageOpen Generative UI](https://docs.copilotkit.ai/angular/generative-ui/open-generative-ui)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/angular/shared-state/agent-readonly)
