---
url: https://docs.copilotkit.ai/troubleshooting/inspector-dev-console/
title: Inspector and dev console
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:34.125133+00:00
---

# Inspector and dev console

> Source: https://docs.copilotkit.ai/troubleshooting/inspector-dev-console/

Troubleshooting

# Inspector and dev console

Configure the CopilotKit Inspector in React, Vue, and Angular.

Copy MarkdownOpen

`enableInspector` controls the built-in Inspector in browser applications:

  * `true` or omitted: show it in development builds.
  * `false`: hide it in development builds.



The Inspector is never loaded or rendered in production builds or during server-side rendering. This safety guard cannot be overridden by an explicit `true`. In React, the Inspector also needs a `localhost`, `127.0.0.1`, or `[::1]` host. Vue and Angular do not check the host.

To learn what the Inspector shows, see [Inspector](https://docs.copilotkit.ai/inspector).

## React v2Copy Anchor Link

Copy Text
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit runtimeUrl="/api/copilotkit" enableInspector={false}>
      {children}
    </CopilotKit>;

`showDevConsole` is deprecated and does not show or hide the Inspector. Use `enableInspector` for Inspector visibility.

## VueCopy Anchor Link

Copy Text
    
    
    <CopilotKitProvider runtime-url="/api/copilotkit" :enable-inspector="false">
      <App />
    </CopilotKitProvider>

Vue's `showDevConsole` prop is deprecated and does not show or hide the Inspector.

## AngularCopy Anchor Link

Copy Text
    
    
    provideCopilotKit({
      runtimeUrl: "/api/copilotkit",
      enableInspector: false,
    });

Configure the Inspector through `enableInspector` on `CopilotKitConfig`.

## React v1Copy Anchor Link

The v1 compatibility component follows the same development-only `enableInspector` behavior. Its deprecated `showDevConsole?: boolean` prop controls the error toasts and banners described in [Error Debugging](https://docs.copilotkit.ai/troubleshooting/error-debugging). It does not control the Inspector.

The Inspector cannot be enabled in a production build. In Vue and Angular, use a development build to debug a deployed or remote environment. In React, the Inspector shows only on a `localhost`, `127.0.0.1`, or `[::1]` host, so run a local development server.

## React NativeCopy Anchor Link

Native iOS and Android applications do not have a built-in Inspector yet. The current Inspector is a DOM web component and is not included in the React Native dependency graph.

How is this guide?

GoodBad

[Previous PageError Debugging & Observability](https://docs.copilotkit.ai/troubleshooting/error-debugging)[Next PageDebug Mode](https://docs.copilotkit.ai/troubleshooting/debug-mode)
