---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotKit/
title: CopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:58.820871+00:00
---

# CopilotKit

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotKit/

React/Components

# CopilotKit

The CopilotKit provider component, wrapping your application.

Copy MarkdownOpen

This is the v1 provider, re-exported for back-compat

`<CopilotKit>` is the v1 provider. It is re-exported from `@copilotkit/react-core/v2` so that a v1 application keeps working after the import path changes, and it renders `<CopilotKitProvider>` internally. **The v2 provider is`<CopilotKitProvider>`**. Reach for that one in new v2 code.

`<CopilotKit>` and `<CopilotKitProvider>` use different props to name the agent:

| v1 `<CopilotKit>`| v2 `<CopilotKitProvider>`  
---|---|---  
Name the agent| `agent="my_agent"`| `agentId="my_agent"`  
  
You can also name the agent per chat with `<CopilotChat agentId="my_agent">`, or for a subtree with `<CopilotChatConfigurationProvider agentId="my_agent">`. Both of those override the provider-level default. See [Provider and handler pairs](https://docs.copilotkit.ai/backend/runtime-endpoints#provider-and-handler-pairs).

Both providers treat an omitted `useSingleEndpoint` the same way: the transport is negotiated from the Runtime info response. Versions before 1.69.0 pinned `<CopilotKit>` to the single-route transport.

This component will typically wrap your entire application (or a sub-tree of your application where you want to have a copilot). It provides the copilot context to all other components and hooks.

## ExampleCopy Anchor Link

To host the runtime yourself, see [Copilot Runtime](https://docs.copilotkit.ai/backend/copilot-runtime).

Copy Text
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit runtimeUrl="<your-runtime-url>">// ... your app ...</CopilotKit>;

## PropertiesCopy Anchor Link

Prop

Type

`publicApiKey?`string

`publicLicenseKey?`string

`licenseToken?`string

`guardrails_c?`{ validTopics?: string[]; invalidTopics?: string[]; }

`runtimeUrl?`string

`transcribeAudioUrl?`string

`textToSpeechUrl?`string

`headers?`Record<string, string> | (() => Record<string, string>) | (() => Promise<Record<string, string>>)

`children`ReactNode

`properties?`Record<string, any>

`credentials?`RequestCredentials

`showDevConsole?`boolean

`showIntelligenceIndicator?`boolean

`selfManagedAgents?`Record<string, AbstractAgent>

`agents__unsafe_dev_only?`Record<string, AbstractAgent>

`a2ui?`{ theme?: Theme; catalog?: any; loadingComponent?: React.ComponentType; includeSchema?: boolean; recovery?: A2UIRecoveryRendererOptions }

`mcpApps?`{ allowSameOriginFallback?: boolean }

`openGenerativeUI?`{ sandboxFunctions?: SandboxFunction[]; designSkill?: string }

`defaultThrottleMs?`number

`agent?`string

`forwardedParameters?`Pick<ForwardedParametersInput, 'temperature'>

`authConfig_c?`{ SignInComponent: React.ComponentType<{ onSignInComplete: (authState: AuthState) => void; }>; }

`threadId?`string

`onError?`CopilotErrorHandler

`enableInspector?`boolean

`debug?`DebugConfig

How is this guide?

GoodBad

[Previous PageCopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)[Next PageCopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)
