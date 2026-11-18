---
url: https://docs.copilotkit.ai/angular/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.239111+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/angular/human-in-the-loop/

Human-in-the-loop

# HITL Overview

Pause an Angular agent flow for a user decision, then resume it from a typed component or interrupt controller.

Copy MarkdownOpen

Human-in-the-loop flows pause agent work until a person supplies a decision. Angular has two paths with different owners.

Pattern| Who chooses the pause?| Angular API  
---|---|---  
Human-in-the-loop tool| The agent calls a registered browser tool| `registerHumanInTheLoop`  
Interrupt| The backend agent emits an AG-UI interrupt| `AgentStore.interruptController`, `injectInterrupt`  
  
Use a tool when the model should decide whether to ask. Use an interrupt when the backend workflow must stop at a fixed checkpoint.

This page covers the tool. For interrupts, see [Headless Interrupts](https://docs.copilotkit.ai/angular/human-in-the-loop/headless) for the controller on the agent store, and [Pausing the Agent for Input](https://docs.copilotkit.ai/angular/human-in-the-loop/useInterrupt) for the typed `injectInterrupt` controller.

## Register a decision toolCopy Anchor Link

The renderer receives a `toolCall` signal. Call `respond(result)` once the user has made a choice.

src/app/approval-card.component.ts

Copy Text
    
    
    import { Component, input } from "@angular/core";
    import {
      type HumanInTheLoopToolCall,
      type HumanInTheLoopToolRenderer,
    } from "@copilotkit/angular";
    
    type ApprovalArgs = {
      action: string;
      reason: string;
    };
    
    @Component({
      selector: "app-approval-card",
      template: `
        @let call = toolCall();
        <article>
          <h3>Approve {{ call.args.action ?? "this action" }}?</h3>
          <p>{{ call.args.reason }}</p>
    
          @if (call.status !== "complete") {
            <button type="button" (click)="call.respond({ approved: true })">
              Approve
            </button>
            <button type="button" (click)="call.respond({ approved: false })">
              Reject
            </button>
          }
        </article>
      `,
    })
    export class ApprovalCardComponent
      implements HumanInTheLoopToolRenderer<ApprovalArgs>
    {
      readonly toolCall =
        input.required<HumanInTheLoopToolCall<ApprovalArgs>>();
    }

Register the tool from the component or service that owns the decision UI:

src/app/approval-tools.service.ts

Copy Text
    
    
    import { Injectable } from "@angular/core";
    import { registerHumanInTheLoop } from "@copilotkit/angular";
    import { z } from "zod";
    import { ApprovalCardComponent } from "./approval-card.component";
    
    @Injectable()
    export class ApprovalToolsService {
      constructor() {
        registerHumanInTheLoop({
          name: "requestApproval",
          description: "Ask the user before a consequential action",
          parameters: z.object({
            action: z.string(),
            reason: z.string(),
          }),
          component: ApprovalCardComponent,
        });
      }
    }

There is no handler. CopilotKit supplies one that waits for `respond`, returns the decision to the agent, and continues the run. The registration is removed when the owning injector is destroyed.

## Place the decision UICopy Anchor Link

The tool renderer appears in the tool-call flow inside chat. An interrupt controller is headless: bind its signals anywhere in the application, including a route-level dialog, side panel, or task view.

Ask the agent to do the consequential action. The approval card appears in the chat. Click Approve, and the agent continues with `{ approved: true }`.

## Next stepsCopy Anchor Link

  * [registerHumanInTheLoop API](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)
  * [Headless Interrupts](https://docs.copilotkit.ai/angular/human-in-the-loop/headless)
  * [Pausing the Agent for Input](https://docs.copilotkit.ai/angular/human-in-the-loop/useInterrupt)



How is this guide?

GoodBad

[Previous PageAgent Read-Only Context](https://docs.copilotkit.ai/angular/shared-state/agent-readonly)[Next PagePausing the Agent for Input](https://docs.copilotkit.ai/angular/human-in-the-loop/useInterrupt)
