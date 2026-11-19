---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider/
title: CopilotKitProvider
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:31.556494+00:00
---

# CopilotKitProvider

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider/

React Native/Components

# CopilotKitProvider

The React Native provider that configures the CopilotKit runtime connection and shares it with all hooks and components.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotKitProvider` is the React Native provider for CopilotKit. Wrap your app (or the sub-tree that needs a copilot) with it to configure the runtime connection. Every hook and component below it, for example [`useCopilotKit`](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit) and [`useAgent`](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent), reads the configured client from context.

Importing the package auto-installs the [polyfills](https://docs.copilotkit.ai/reference/react-native#polyfills) CopilotKit needs on Hermes, so you do not have to import them manually before using the provider. One thing it cannot do for you: its `crypto.getRandomValues` falls back to `Math.random`, which is not cryptographically secure. For a secure one, import `react-native-get-random-values` on the first line of your entry point, before any CopilotKit import; once a CopilotKit module has loaded, the fallback stays and the secure import does nothing. See [Polyfills](https://docs.copilotkit.ai/react-native#polyfills) in the guide.

Cloud features (`publicLicenseKey` and other license-gated features) are not yet supported on React Native. Point `runtimeUrl` at a self-hosted runtime.

Native iOS and Android applications do not have a built-in Inspector yet. The browser Inspector requires a DOM and is intentionally excluded from the React Native dependency graph, so this provider does not expose an inspector prop.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotKitProvider } from "@copilotkit/react-native";

## PropsCopy Anchor Link

Prop

Type

`children`ReactNode

`runtimeUrl`string

`headers?`Record<string, string> | (() => Record<string, string>)

`credentials?`RequestCredentials

`messageFilter?`(messages: Message[], context: { agentId: string }) => Message[]

`useSingleEndpoint?`boolean

`properties?`Record<string, unknown>

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

`debug?`DebugConfig

`defaultThrottleMs?`number

## UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotKitProvider } from "@copilotkit/react-native";
    import { SafeAreaProvider } from "react-native-safe-area-context";
    import { ChatScreen } from "./ChatScreen";
    
    export default function App() {
      return (
        <SafeAreaProvider>
          <CopilotKitProvider runtimeUrl="https://your-server/api/copilotkit">
            <ChatScreen />
          </CopilotKitProvider>
        </SafeAreaProvider>
      );
    }

## BehaviorCopy Anchor Link

  * **Auto-polyfills** : importing the package installs the Web API polyfills CopilotKit relies on (`ReadableStream`, `TextEncoder`, `crypto.getRandomValues`, `DOMException`, `location`) before any CopilotKit code runs. Each polyfill installs only when its global is missing, so a secure `crypto.getRandomValues` from `react-native-get-random-values` must be imported first, on the first line of the entry point.
  * **Shared render-tool registry** : the provider instantiates the CopilotKit client whose renderer registry is shared with the rest of CopilotKit. Render functions registered by [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool), [`useFrontendTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool) or [`useComponent`](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent) write into that one registry, so they and [`useRenderToolCall`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool#rendering-a-tool-call-outside-the-chat) work anywhere below the provider. There is no second registry and no extra provider to mount for rendering.
  * **Stable references** : header functions and `properties` are memoized internally to avoid effect churn on re-render.



How is this guide?

GoodBad

[Previous PageCopilotChat](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat)[Next PageCopilotMarkdown](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown)
