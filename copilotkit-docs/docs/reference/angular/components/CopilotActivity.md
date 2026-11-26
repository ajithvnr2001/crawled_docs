---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotActivity/
title: CopilotActivity
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:20.227679+00:00
---

# CopilotActivity

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotActivity/

Angular/Components

# CopilotActivity

Angular component that renders a single activity message through the activity renderer registered for its activity type.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotActivity` renders one activity message. It looks up the renderer registered for the message's `activityType` (via `provideCopilotKit({ renderActivityMessages })` or [`registerRenderActivityMessage`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)), validates the message content against the renderer's schema, and mounts the renderer component with the `activityType`, `content`, `message`, and `agent` inputs.

It is the activity counterpart of `RenderToolCalls` and the Angular equivalent of React's `useRenderActivityMessage()`. [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView) uses it for every message with `role: "activity"`, so the built-in chat and your own templates share one implementation.

Use it directly when you build a custom chat shell without `CopilotChatMessageView`, or when you host activities outside of a chat entirely, such as a dashboard, a side panel, or an output area.

The component is standalone. Reactive inputs are Angular [signals](https://angular.dev/guide/signals).

## UsageCopy Anchor Link

src/app/activity-panel.component.ts

Copy Text
    
    
    import { Component, computed, input } from "@angular/core";
    import { CopilotActivity } from "@copilotkit/angular";
    import type { ActivityMessage, Message } from "@ag-ui/core";
    
    @Component({
      selector: "app-activity-panel",
      standalone: true,
      imports: [CopilotActivity],
      template: `
        @for (activity of activities(); track activity.id) {
          <copilot-activity [message]="activity" [agentId]="agentId()" />
        }
      `,
    })
    export class ActivityPanelComponent {
      messages = input.required<Message[]>();
      agentId = input<string>();
    
      activities = computed(() =>
        this.messages().filter(
          (message): message is ActivityMessage => message.role === "activity",
        ),
      );
    }

## Renderer resolutionCopy Anchor Link

For a given `activityType`, the first matching renderer wins in this order:

  1. a renderer for that type registered with the same `agentId`
  2. a renderer for that type without an `agentId` (global)
  3. the `"*"` wildcard renderer



Within a tier, the first registered renderer wins. Renderers from `provideCopilotKit` and runtime registrations come before the built-in renderers (A2UI, Open Generative UI, MCP Apps). So your renderer can override a built-in renderer for the same activity type.

If no renderer matches, nothing is rendered. If the renderer's content schema rejects the message content, nothing is rendered and a warning is logged.

## InputsCopy Anchor Link

Input| Type| Default| Description  
---|---|---|---  
`message`| `ActivityMessage`|  _required_|  The activity message to render.  
`agentId`| `string | undefined`| `undefined`| Agent scope for renderer resolution. Also used to look up the `AbstractAgent` handed to the renderer's `agent` input.  
  
How is this guide?

GoodBad

[Previous PagePublic API inventory](https://docs.copilotkit.ai/reference/angular/public-api)[Next PageCopilotChat](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)
