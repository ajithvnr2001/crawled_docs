---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider/
title: CopilotKitProvider
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:19.199979+00:00
---

# CopilotKitProvider

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider/

Vue/Components

# CopilotKitProvider

The Vue 3 provider component that wraps your application and supplies the CopilotKit context.

Copy MarkdownOpen

This is the Vue 3 provider component. Import it from `@copilotkit/vue/v2`.

`CopilotKitProvider` typically wraps your entire application (or a sub-tree where you want a copilot). It creates the CopilotKit core instance and provides the copilot context to all descendant components and composables (such as [`useCopilotKit`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit) and [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)).

The wrapped application is rendered through the component's default slot, since Vue uses slots rather than a `children` prop.

## ExampleCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <!-- ... your app ... -->
      </CopilotKitProvider>
    </template>

Connect to Copilot Cloud with a public API key instead of a self-hosted runtime:

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotKitProvider public-api-key="ck_pub_your_key">
        <!-- ... your app ... -->
      </CopilotKitProvider>
    </template>

## PropertiesCopy Anchor Link

You must provide at least one of `runtimeUrl`, `publicApiKey`, or `publicLicenseKey` (or a set of local agents), otherwise the provider warns in development and throws in production.

Prop

Type

`runtimeUrl?`string

`headers?`Record<string, string> | (() => Record<string, string>) | (() => Promise<Record<string, string>>)

`credentials?`RequestCredentials

`messageFilter?`(messages: Message[], context: { agentId: string }) => Message[]

`defaultThrottleMs?`number

`publicApiKey?`string

`publicLicenseKey?`string

`licenseToken?`string

`properties?`Record<string, unknown>

`useSingleEndpoint?`boolean

`agents__unsafe_dev_only?`Record<string, AbstractAgent>

`selfManagedAgents?`Record<string, AbstractAgent>

`renderToolCalls?`VueToolCallRenderer<any>[]

`renderActivityMessages?`VueActivityMessageRenderer<unknown>[]

`renderCustomMessages?`VueCustomMessageRenderer[]

`frontendTools?`VueFrontendTool[]

`humanInTheLoop?`VueHumanInTheLoop[]

`openGenerativeUI?`{ sandboxFunctions?: SandboxFunction[]; designSkill?: string }

`enableInspector?`boolean

`showDevConsole?`boolean | "auto"

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

`a2ui?`{ theme?: A2UITheme; catalog?: any; loadingComponent?: Component; includeSchema?: boolean }

`generativeUI?`GenerativeUIConfig

`mcpApps?`{ allowSameOriginFallback?: boolean }

`debug?`DebugConfig

## SlotsCopy Anchor Link

Prop

Type

`default`slot

How is this guide?

GoodBad

[Previous PageCopilotChatView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView)[Next PageCopilotPopup](https://docs.copilotkit.ai/reference/vue/components/CopilotPopup)
