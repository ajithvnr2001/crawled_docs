---
url: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider/
title: GenerativeUIProvider
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:51.655168+00:00
---

# GenerativeUIProvider

> Source: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React NativeSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[AssistantMessage](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage)[CopilotChat](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat)[CopilotKitProvider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)[CopilotMarkdown](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown)[CopilotModal](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal)[CopilotPopup](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar)[GenerativeUIActivity](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity)[GenerativeUIProvider](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider)[GenerativeUISurface](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface)[UserMessage](https://docs.copilotkit.ai/reference/react-native/components/UserMessage)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext)[useAttachments](https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments)[useCapabilities](https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useConfigureSuggestions)[useCopilotKit](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit)[useFrontendTool](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/react-native/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[react-native](https://docs.copilotkit.ai/reference/react-native)Components

# GenerativeUIProvider

Turn on generative UI for the agent runs of a CopilotKitProvider: the agent renders the components of your native catalog with the render_ui tool.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`GenerativeUIProvider` turns on [generative UI](https://docs.copilotkit.ai/generative-ui/components) on React Native. It sends your catalog with every agent run on the core of the enclosing `CopilotKitProvider`, wherever in the component tree the run starts, so the runtime gives those runs a `render_ui` tool; a catalog with no components gets no `render_ui` tool. Only `agentIds` narrows it to some agents. It also keeps the surfaces that the agent renders. Show them with [`GenerativeUIActivity`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity) (one activity message, in a chat list or on a screen with no chat) or [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface) (a named place in your app).

Place it inside [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider), and mount exactly one `GenerativeUIProvider` with a `ui` for each `CopilotKitProvider`, above every screen that shows generative UI, rather than one per screen. Each one sets the catalog and the named targets of every run on the core, so two of them override each other, and each shows only the surfaces built for its own catalog; in development, the second one mounted warns. It ingests every generative UI activity message of the agents it watches, and skips a message whose content is malformed (in development it warns once for each distinct issue), so such a message cannot break the agent's run. The runtime needs no setup by default; a server turns generative UI off with the `CopilotRuntime` option `generativeUI: false`, or limits it to some agents with `generativeUI: { agents: [...] }`.

Install `zod` 3.25 or later. Every entry of `@copilotkit/react-native` needs it, because `@copilotkit/react-core` requires it as a peer dependency; `@copilotkit/react-native` itself declares `zod` an optional peer at `>=3.0.0`, so the package manager does not enforce 3.25. Install zod 3 (`zod@^3.25`) for a catalog that uses `child()` or `childList()`: they return zod 3 schemas, which a zod 4 schema cannot hold.

For a complete walkthrough, see [Generative UI with your own components](https://docs.copilotkit.ai/react-native#generative-ui-with-your-own-components).

Experimental

Generative UI on React Native uses the tool transport only, has no standard catalog (the catalog holds your own native components), and has no `theme` prop. The prebuilt `CopilotChat` does not draw surfaces yet.

## Import
    
    
    import { GenerativeUIProvider } from "@copilotkit/react-native/generative-ui";

## Props

Prop

Type

`ui`GenerativeUI

Prop

Type

`children`ReactNode

Prop

Type

`agentIds?`string[]

Prop

Type

`errorBoundary?`GenerativeUIErrorBoundaryConfig

Prop

Type

`host?`GenerativeUIHost

Prop

Type

`transport?`"tool"

There is no `theme` prop: the web theme is a set of CSS variables, which React Native does not use, so passing `theme` is a type error, and a `theme` that gets past the types is dropped, with a warning in development. Style the components of your catalog instead. The `GenerativeUIToolConfig` type exported from `/generative-ui` is the web config without `theme`.

## Usage
    
    
    import { CopilotKitProvider } from "@copilotkit/react-native/headless";
    import { GenerativeUIProvider } from "@copilotkit/react-native/generative-ui";
    import { bankUI } from "./src/bankUI";
    import { ChatScreen } from "./src/ChatScreen";
    
    export default function App() {
      return (
        <CopilotKitProvider runtimeUrl="https://your-server/api/copilotkit">
          <GenerativeUIProvider
            ui={bankUI}
            agentIds={["default", "home"]}
            errorBoundary={{
              onError: (info) => console.warn(info.kind, info.surfaceId, info.error.message),
            }}
          >
            <ChatScreen />
          </GenerativeUIProvider>
        </CopilotKitProvider>
      );
    }

## Also exported from `/generative-ui`

The entry re-exports the catalog API from `@copilotkit/react-core/v2/generative-ui/native`, the build of `@copilotkit/react-core/v2/generative-ui` without DOM. It works the same on React Native:

Export| What it does  
---|---  
`createGenerativeUI`| Declares a catalog. See [Catalogs](https://docs.copilotkit.ai/generative-ui/components/catalogs).  
`child`, `childList`| Mark a prop of the schema as a child component reference.  
`useGenerativeUIState`| Gives a state key of the catalog its value from your app. See [State and actions](https://docs.copilotkit.ai/generative-ui/components/state-and-actions).  
`useGenerativeUIFunction`| Mounts the handler of a catalog function.  
`useGenerativeUIAccessibility`| The accessibility attributes that the agent gave the component being rendered.  
`useGenerativeUIRuntime`| The runtime of the nearest provider, or `null`.  
`GenerativeUIError`| The error class of generative UI failures.  
`exportA2UICatalog`| Writes the catalog as an A2UI 1.0 catalog definition.  
`nativeGenerativeUIHost`, `NativeNodeFallback`| The default React Native host elements, to reuse in a custom `host`.  
  
The types of these APIs come from the same entry, for example `GenerativeUIComponentProps`, `GenerativeUIErrorInfo`, `GenerativeUIHost`, `GenerativeUIRuntime`, `GenerativeUIRejectedOperation` and the props of each component (`GenerativeUIProviderProps`, `GenerativeUIActivityProps`, `GenerativeUIActivityWrapperProps`, `GenerativeUISurfaceProps`).

`standardUI` and the markdown surfaces are not exported: they render DOM.

## Related

  * [`GenerativeUIActivity`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity): render the surface of an activity message
  * [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface): a named place where the agent can render
  * [Components and surfaces](https://docs.copilotkit.ai/generative-ui/components): the feature, with React, Angular and React Native examples


