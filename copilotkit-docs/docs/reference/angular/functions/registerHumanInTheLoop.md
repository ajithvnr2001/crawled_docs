---
url: https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop/
title: registerHumanInTheLoop
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:25.354204+00:00
---

# registerHumanInTheLoop

> Source: https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop/

Angular/Functions

# registerHumanInTheLoop

Angular function for registering a human-in-the-loop tool with CopilotKit that pauses the agent and resumes it when the user responds from a rendered component

Copy MarkdownOpen

## OverviewCopy Anchor Link

`registerHumanInTheLoop` registers a tool that pauses the agent and waits for human input. When the agent calls the tool, CopilotKit renders the `component` you provide and suspends the agent run. The component collects a decision from the user (for example a confirm or reject choice) and calls `respond(result)`. That call resolves the tool with the value you passed to `respond`, serialized as described below, and lets the run continue.

You call `registerHumanInTheLoop` inside an Angular injection context (a component or service constructor, or a field initializer). The tool registers immediately. When the owning injector is destroyed, CopilotKit removes tool and renderer registrations with the same name and optional agent id.

Unlike [`registerFrontendTool`](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool), you do not write a `handler`. CopilotKit supplies one that waits for the user's `respond` call, so the rendered component controls when the agent resumes.

Import from the package root, `@copilotkit/angular`. There is no `/v2` subpath. `registerHumanInTheLoop` must run in an injection context that has [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit) in scope.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { registerHumanInTheLoop } from "@copilotkit/angular";
    
    function registerHumanInTheLoop<Args extends Record<string, unknown>>(
      humanInTheLoop: HumanInTheLoopConfig<Args>,
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`humanInTheLoop`HumanInTheLoopConfig<Args>

## Return ValueCopy Anchor Link

`registerHumanInTheLoop` returns `void`. It registers the tool as a side effect and wires up name-and-agent-id cleanup for the owning injector.

## The renderer componentCopy Anchor Link

For a renderer with no handler, see [`registerRenderToolCall`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall). Your `component` implements the `HumanInTheLoopToolRenderer<Args>` interface. It exposes a single `toolCall` signal input, so declare it with Angular's `input()`:

Copy Text
    
    
    import { Signal } from "@angular/core";
    
    interface HumanInTheLoopToolRenderer<Args extends Record<string, unknown>> {
      toolCall: Signal<HumanInTheLoopToolCall<Args>>;
    }

### HumanInTheLoopToolCallCopy Anchor Link

`toolCall()` returns a discriminated union keyed on `status`. Every variant carries a `respond` callback:

Copy Text
    
    
    type HumanInTheLoopToolCall<Args extends Record<string, unknown>> =
      | {
          name?: string;
          args: Partial<Args>; // streaming, may be incomplete
          status: "in-progress";
          result: undefined;
          respond: (result: unknown) => void;
        }
      | {
          name?: string;
          args: Args; // fully parsed
          status: "executing";
          result: undefined;
          respond: (result: unknown) => void;
        }
      | {
          name?: string;
          args: Args; // fully parsed
          status: "complete";
          result: string; // stored tool-message content
          respond: (result: unknown) => void;
        };

The `respond(result)` callback is how your component resumes the agent. The value you pass to `respond` becomes the tool result directly: a string is stored as-is, and any other value is serialized to JSON by core. The `status` values are:

  * `in-progress`: the agent run is still active, for example while the arguments stream.
  * `executing`: the agent waits for `respond`.
  * `complete`: the tool message arrived, and `result` contains the stored tool-message string.



## UsageCopy Anchor Link

### A confirmation dialogCopy Anchor Link

This component renders a confirm and a reject button. Each records a different decision and resumes the agent.

src/app/confirm-dialog.component.ts

Copy Text
    
    
    import { Component, computed, input } from "@angular/core";
    import { HumanInTheLoopToolCall, HumanInTheLoopToolRenderer } from "@copilotkit/angular";
    
    type ConfirmArgs = { message: string };
    
    @Component({
      selector: "app-confirm-dialog",
      standalone: true,
      template: `
        @let call = toolCall();
        @if (call.status === "complete") {
          <pre class="text-sm opacity-70">{{ call.result }}</pre>
        } @else {
          <div class="rounded border p-4">
            <p>{{ message() }}</p>
            <div class="mt-3 flex gap-2">
              <button type="button" (click)="call.respond('confirmed')">Confirm</button>
              <button type="button" (click)="call.respond('rejected')">Reject</button>
            </div>
          </div>
        }
      `,
    })
    export class ConfirmDialogComponent implements HumanInTheLoopToolRenderer<ConfirmArgs> {
      readonly toolCall = input.required<HumanInTheLoopToolCall<ConfirmArgs>>();
      readonly message = computed(() => this.toolCall().args.message ?? "Are you sure?");
    }

Register the tool with that component:

src/app/chat.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { z } from "zod";
    import { registerHumanInTheLoop } from "@copilotkit/angular";
    import { ConfirmDialogComponent } from "./confirm-dialog.component";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      template: ``,
    })
    export class ChatComponent {
      constructor() {
        registerHumanInTheLoop({
          name: "confirmAction",
          description: "Ask the user to confirm before performing a sensitive action",
          parameters: z.object({
            message: z.string().describe("The confirmation question to show the user"),
          }),
          component: ConfirmDialogComponent,
        });
      }
    }

When the agent calls `confirmAction`, the dialog appears in the chat and the run pauses. A button click sends `"confirmed"` or `"rejected"` as the tool result. The completed tool call exposes that stored string.

Cleanup uses the same shared name-and-agent-id removal path as the other tool registration helpers. Frontend tools, human-in-the-loop tools, and tool-call renderers that share that key are removed together.

How is this guide?

GoodBad

[Previous PageregisterFrontendTool](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)[Next PageregisterRenderActivityMessage](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)
