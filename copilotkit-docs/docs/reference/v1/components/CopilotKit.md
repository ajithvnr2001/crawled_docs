---
url: https://docs.copilotkit.ai/reference/v1/components/CopilotKit/
title: CopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:21.122418+00:00
---

# CopilotKit

> Source: https://docs.copilotkit.ai/reference/v1/components/CopilotKit/

React/v1

# CopilotKit

The CopilotKit provider component, wrapping your application.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

In v2, use `CopilotKitProvider` from `@copilotkit/react-core/v2`. See the [v2 provider reference](https://docs.copilotkit.ai/reference/v2/components/CopilotKit).

This component will typically wrap your entire application (or a sub-tree of your application where you want to have a copilot). It provides the copilot context to all other components and hooks.

## ExampleCopy Anchor Link

You can find more information about self-hosting CopilotKit [here](https://docs.copilotkit.ai/backend/copilot-runtime).

Copy Text
    
    
    import { CopilotKit } from "@copilotkit/react-core";
    
    <CopilotKit runtimeUrl="<your-runtime-url>">
      // ... your app ...
    </CopilotKit>

`CopilotKit` also passes the props of the [v2 `CopilotKitProvider`](https://docs.copilotkit.ai/reference/v2/components/CopilotKit) through to it, such as `selfManagedAgents`, `frontendTools`, `renderToolCalls`, and `defaultThrottleMs`. To name the agent, use `agent`.

## PropertiesCopy Anchor Link

Prop

Type

`publicApiKey?`string

`publicLicenseKey?`string

`runtimeUrl?`string

`transcribeAudioUrl?`string

`textToSpeechUrl?`string

`headers?`CopilotKitHeadersSource

`children`ReactNode

`properties?`Record<string, any>

`credentials?`RequestCredentials

`agent?`string

`forwardedParameters?`Pick<ForwardedParametersInput, 'temperature'>

`threadId?`string

`onError?`CopilotErrorHandler

`enableInspector?`boolean

`debug?`DebugConfig

How is this guide?

GoodBad

[Previous PageCopilotTextarea](https://docs.copilotkit.ai/reference/v1/components/CopilotTextarea)[Next PageuseAgent](https://docs.copilotkit.ai/reference/v1/hooks/useAgent)
