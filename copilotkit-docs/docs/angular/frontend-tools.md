---
url: https://docs.copilotkit.ai/angular/frontend-tools/
title: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:52.925901+00:00
---

# Frontend Tools

> Source: https://docs.copilotkit.ai/angular/frontend-tools/

# Frontend Tools

Let an agent run browser code in your Angular app with registerFrontendTool.

Copy MarkdownOpen

Frontend tools let an agent call code inside the user's browser. [Add a renderer](https://docs.copilotkit.ai/angular/generative-ui/tool-rendering) to the same registration when the tool should show progress or a result in chat.

## Register a browser toolCopy Anchor Link

Call `registerFrontendTool` from an Angular injection context. The live Showcase example builds a typed tool config around a writable signal:

tool-feature-model.ts

Copy Text
    
    
    /** Create the frontend tool that applies a requested CSS gradient. */
    export function createBackgroundTool(
      background: WritableSignal<string>,
    ): FrontendToolConfig<BackgroundToolArgs> {
      return {
        name: "change_background",
        description: "Change the application background to a CSS gradient.",
        parameters: z.object({
          background: z.string().optional(),
          color: z.string().optional(),
        }),
        handler: async (args) => {
          const next = resolveGradient(args.background ?? args.color);
          background.set(next);
          return { background: next };
        },
      };
    }

Register that config from a component or service with `registerFrontendTool(createBackgroundTool(background))`. The registration is removed when that injector is destroyed.

The schema advertises the input shape and supplies TypeScript inference. Runtime arguments arrive as parsed JSON; validate inside the handler when the action needs a hard trust boundary. The handler receives the calling agent, the raw tool call, and an optional abort signal as its second argument.

## Next stepsCopy Anchor Link

  * [registerFrontendTool API](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)
  * [Tool Call Rendering](https://docs.copilotkit.ai/angular/generative-ui/tool-rendering): show the tool's progress and result in chat.



How is this guide?

GoodBad

[Previous PageHeadless Threads](https://docs.copilotkit.ai/angular/headless-threads)[Next PageOverview](https://docs.copilotkit.ai/angular/generative-ui)
