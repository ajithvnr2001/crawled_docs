---
url: https://docs.copilotkit.ai/angular/troubleshooting/
title: Troubleshooting Angular apps
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.756495+00:00
---

# Troubleshooting Angular apps

> Source: https://docs.copilotkit.ai/angular/troubleshooting/

Troubleshooting

# Troubleshooting Angular apps

Diagnose Angular runtime connections, agent resolution, tools, threads, interrupts, SSR, and rendering failures.

Copy MarkdownOpen

Use this page for failures in the Angular application layer. Runtime and protocol diagnostics remain available in the shared troubleshooting pages, so you can investigate the complete request without switching frontend docs.

## Start at the connection boundaryCopy Anchor Link

Confirm that the browser is calling the same Copilot Runtime URL your server actually exposes:

src/app/app.config.ts

Copy Text
    
    
    import { provideCopilotKit } from "@copilotkit/angular";
    
    export const appConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
        }),
      ],
    };

Then inspect `GET {runtimeUrl}/info`. A healthy response lists the expected agent ids. If the request fails:

  * verify the path, origin, proxy, and deployment base URL;
  * verify the runtime process is running and allows the Angular origin;
  * check authentication headers without logging their values;
  * try `127.0.0.1` when local `localhost` resolution is unreliable.



The [`CopilotKit` service](https://docs.copilotkit.ai/reference/angular/services/CopilotKit) exposes `runtimeConnectionStatus`, `runtimeUrl`, and the resolved `agents` as signals. Use them in a temporary diagnostic component:

src/app/copilot-diagnostics.component.ts

Copy Text
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-copilot-diagnostics",
      standalone: true,
      template: `
        <p>Runtime: {{ copilotKit.runtimeConnectionStatus() }}</p>
        <p>Agents: {{ agentIds().join(", ") || "none" }}</p>
      `,
    })
    export class CopilotDiagnosticsComponent {
      protected readonly copilotKit = inject(CopilotKit);
      protected readonly agentIds = () =>
        Object.keys(this.copilotKit.agents());
    }

Remove diagnostics that expose topology or identifiers before production.

## Agent id does not resolveCopy Anchor Link

`injectAgentStore("support")` and `<copilot-chat agentId="support" />` must use an id returned by the runtime or registered through `agents` or `selfManagedAgents`. After the runtime finishes connecting, `injectAgentStore` throws an error that includes the requested id and known agents when no match exists.

If you intend to use the default agent, either register an agent named `default` or pass the real id explicitly everywhere the chat, state, tools, or interrupt controller selects an agent.

## A frontend tool is missing or never runsCopy Anchor Link

Registrations are injector-scoped. Call `registerFrontendTool`, `registerRenderToolCall`, or `registerHumanInTheLoop` from a field initializer, constructor, provider factory, or another active injection context.

Check these in order:

  1. The component or service that registers the tool is instantiated.
  2. Its injector has not been destroyed by route or conditional-view changes.
  3. The registered `agentId` matches the chat's agent.
  4. The tool description tells the model when it should call the tool.
  5. The input schema accepts the arguments emitted by the agent.
  6. The handler catches expected application failures and returns a deliberate result instead of silently throwing.



For a source-backed registration, see [Frontend Tools](https://docs.copilotkit.ai/angular/frontend-tools).

## A thread list or mutation failsCopy Anchor Link

Use `listError()` for user-visible thread-list and mutation failures. The broader `error()` signal can also contain developer configuration errors such as a missing runtime URL or unavailable thread endpoints.

Mutation methods return promises. Handle rejection and confirm before permanent deletion:

Copy Text
    
    
    await threads.renameThread(threadId, nextName).catch((error) => {
      console.error("Thread rename failed", error);
    });

See [`injectThreads`](https://docs.copilotkit.ai/reference/angular/functions/injectThreads) for loading, pagination, realtime, and optimistic-mutation behavior.

## An interrupt cannot resumeCopy Anchor Link

Read `injectInterrupt().error()` after a failed predicate, handler, or resume. Expired decisions use `InterruptExpiredError`. Resolve or cancel every pending interrupt id when the backend emits multiple simultaneous decisions.

The controller clears stale decisions when a thread changes or a new run starts. Do not cache it outside the injector that created it.

## SSR, hydration, or zoneless problemsCopy Anchor Link

  * **Hydration mismatch on the chat.** Cause: the server render and the first browser render used different provider options or initial inputs. Fix: use the same `provideCopilotKit` options and initial component inputs in both.
  * **Errors from agent or browser code during server rendering.** Cause: code starts an agent run, resumes an interrupt, or reads a browser API on the server. Fix: do this work only in the browser.
  * **Your own DOM or media code fails on the server.** Cause: it runs during server rendering. Fix: put it behind an Angular platform guard or `afterNextRender`.
  * **The UI does not update in a zoneless app.** Cause: the code reads CopilotKit state outside a reactive context. Fix: read CopilotKit signals from templates or computed signals.



The complete contract is in [Angular production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle).

## Watch the live event streamCopy Anchor Link

The [Inspector](https://docs.copilotkit.ai/angular/inspector) overlays the running application and reports the AG-UI event stream, the advertised agents, agent state, your registered tools, and the context you sent. `@copilotkit/angular` mounts it for you in development browser builds. To hide it, set `enableInspector: false` in `provideCopilotKit`.

## Continue through the shared stackCopy Anchor Link

  * [Common Copilot issues](https://docs.copilotkit.ai/angular/troubleshooting/common-issues)
  * [Runtime endpoints](https://docs.copilotkit.ai/angular/backend/runtime-endpoints)
  * [Runtime debug mode](https://docs.copilotkit.ai/angular/troubleshooting/debug-mode)
  * [AG-UI Event Inspector](https://docs.copilotkit.ai/angular/troubleshooting/event-inspector)
  * [Authentication](https://docs.copilotkit.ai/angular/auth)



How is this guide?

GoodBad

[Previous PageDocumentation Contributions](https://docs.copilotkit.ai/angular/contributing/docs-contributions)[Next PageCommon Copilot Issues](https://docs.copilotkit.ai/angular/troubleshooting/common-issues)
