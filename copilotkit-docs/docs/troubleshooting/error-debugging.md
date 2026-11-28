---
url: https://docs.copilotkit.ai/troubleshooting/error-debugging/
title: Error Debugging & Observability
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:18.268088+00:00
---

# Error Debugging & Observability

> Source: https://docs.copilotkit.ai/troubleshooting/error-debugging/

Troubleshooting

# Error Debugging & Observability

Surface errors visually in development, and wire programmatic error handlers for Sentry / Datadog / your analytics pipeline in production.

Copy MarkdownOpen

## How to debug errorsCopy Anchor Link

When a run fails, you need to see the error while you develop and send it to your error tracker in production. Turn on the dev console for development. The dev console shows error banners and toasts in your app. Then add an `onError` handler for production.

### Quick setupCopy Anchor Link

Copy Text
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    export default function App() {
      return (
        <CopilotKit
          runtimeUrl="/api/copilotkit"
          showDevConsole={true}
        >
          {/* your app */}
        </CopilotKit>
      );
    }

`showDevConsole` is deprecated. It still turns on the error banners and toasts of the dev console. For the Inspector, use `enableInspector`.

To check the setup, stop your runtime and reload the page. An error banner appears. Click **Show Details** to see the code `runtime_info_fetch_failed`.

Avoid showing the dev console in production. It exposes internal error details to end users.

### When to use development debuggingCopy Anchor Link

  * **Local development** : errors appear immediately in your UI
  * **Quick debugging** : no setup required, works by default
  * **Testing** : verify error handling during development



### Programmatic error handlingCopy Anchor Link

Pass `onError` to the provider to catch every error, or to `CopilotChat` to catch the errors of one chat.

#### Provider-level error handlingCopy Anchor Link

Catches every error across the entire application:

Copy Text
    
    
    import { CopilotKitProvider } from "@copilotkit/react-core/v2";
    
    <CopilotKitProvider
      runtimeUrl="/api/copilotkit"
      onError={(event) => {
        // event.code    — error type (e.g. "runtime_info_fetch_failed", "agent_run_failed")
        // event.error   — the Error object
        // event.context — additional context (agentId, toolName, etc.)
        console.error(`[CopilotKit ${event.code}]`, event.error.message);
        errorTracker.capture(event);
      }}
    >
      <App />
    </CopilotKitProvider>;

#### Chat-level error handlingCopy Anchor Link

Scoped to a specific chat's agent. It fires **in addition to** the provider-level handler:

Copy Text
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    <CopilotChat
      agentId="my-agent"
      onError={(event) => {
        showToast(`Agent error: ${event.error.message}`);
      }}
    />;

#### Errors replayed from thread historyCopy Anchor Link

Connecting to an existing thread replays its history, including a `RUN_ERROR` from an earlier run. `onError` receives that error with the code `agent_run_error_event`, like a live failure. `event.context.phase` tells them apart: `"live"` for a run happening now, `"replay"` for thread history, and `"unknown"` when the connection can't tell.

If your handler shows a banner, skip only `"replay"`. Keep `"unknown"` visible, so a live failure is never hidden:

Copy Text
    
    
    import {
      CopilotKitProvider,
      CopilotKitCoreErrorCode,
    } from "@copilotkit/react-core/v2";
    
    <CopilotKitProvider
      runtimeUrl="/api/copilotkit"
      onError={(event) => {
        errorTracker.capture(event); // Still record every error.
        if (
          event.code === CopilotKitCoreErrorCode.AGENT_RUN_ERROR_EVENT &&
          event.context.phase === "replay"
        ) {
          return; // An earlier run's failure, replayed on connect.
        }
        showErrorBanner(event.error.message);
      }}
    >
      <App />
    </CopilotKitProvider>;

#### Error codesCopy Anchor Link

Code| Description  
---|---  
`runtime_info_fetch_failed`| Could not reach the runtime's `/info` endpoint  
`agent_connect_failed`| Agent connection (thread setup) failed  
`agent_run_failed`| Agent run rejected (e.g. network error)  
`agent_run_failed_event`| The agent's `onRunFailed` subscriber fired  
`agent_run_error_event`| Agent emitted a `RUN_ERROR` event  
`tool_argument_parse_failed`| Tool call arguments were not valid JSON  
`tool_handler_failed`| A frontend tool handler threw  
  
To see every event your agent emits and where events drop, open the [Inspector](https://docs.copilotkit.ai/inspector). When a run fails, the launcher turns red. Click the launcher to open the pane for the failure. The pane shows the agent, the tool if one failed, and the error.

### TroubleshootingCopy Anchor Link

#### Dev console not showingCopy Anchor Link

  * Confirm `showDevConsole={true}`
  * Check for JavaScript errors in the browser console
  * Make sure that no CSS hides the error banners of the dev console



#### Production error pipeline checklistCopy Anchor Link

  * Provider-level `onError` is wired and forwards to your error tracker
  * `showDevConsole` is **false** in production builds
  * Agent IDs in errors match the agents registered on your runtime
  * Critical error codes (`agent_run_failed`, `tool_handler_failed`) are alerted on, not just logged



How is this guide?

GoodBad

[Previous PageError message reference](https://docs.copilotkit.ai/troubleshooting/error-reference)[Next PageInspector and dev console](https://docs.copilotkit.ai/troubleshooting/inspector-dev-console)
