---
url: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface/
title: GenerativeUISurface
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:51.803561+00:00
---

# GenerativeUISurface

> Source: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface/

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

# GenerativeUISurface

A named place in a React Native app where the agent can render UI, with a description the agent reads in each run that starts while it is mounted.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`GenerativeUISurface` marks a place in your app as a **target** for generated UI. The targets are sent when a run starts, so the agent sees its `id` and `description` in each run that starts while it is mounted, and can render a surface into it. Until then it shows `fallback`.

A target follows the thread that is active in the provider: the thread of the last run that started on the core, of any agent, also one that the provider's `agentIds` leaves out. To show the output of one particular agent, for example a background run on a home screen, render that agent's activity message with [`GenerativeUIActivity`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity) instead.

Render it under [`GenerativeUIProvider`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider): outside one it throws, naming `GenerativeUIProvider`, unlike `GenerativeUIActivity`, which renders nothing. Under a provider that has no `ui`, it shows its `fallback` and warns in development. The concepts are the same as on the web; see [Surfaces](https://docs.copilotkit.ai/generative-ui/components/surfaces).

The operations of its surface that were rejected, by the runtime or by the app, reach its `Wrapper` (see below); by default it shows "Part of this UI couldn't be shown." under the surface. The ones that the runtime rejected never reach `errorBoundary.onError`; the ones that the app rejected go there too, as usual.

## Import
    
    
    import { GenerativeUISurface } from "@copilotkit/react-native/generative-ui";

## Props

Prop

Type

`id`string

Prop

Type

`description?`string

Prop

Type

`ui?`GenerativeUI

Prop

Type

`components?`readonly GenerativeUIComponentName<UI>[]

Prop

Type

`fallback?`ReactNode

Prop

Type

`style?`StyleProp<ViewStyle>

Prop

Type

`onGenerationStart?`() => void

Prop

Type

`Wrapper?`ComponentType<GenerativeUIActivityWrapperProps>

## Usage
    
    
    import { useRef } from "react";
    import { ScrollView, View } from "react-native";
    import { GenerativeUISurface } from "@copilotkit/react-native/generative-ui";
    import { bankUI } from "./bankUI";
    
    export function AccountsScreen() {
      const scrollRef = useRef<ScrollView>(null);
      const insightsY = useRef<number | undefined>(undefined);
      // A target that mounts while the agent renders into it gets the call before
      // its first layout, and content above it can move as the generation starts.
      // Until this time, a new position of the target scrolls to it again.
      const followUntil = useRef(0);
    
      const scrollToInsights = () => {
        followUntil.current = Date.now() + 1000;
        // Undefined before the first layout: onLayout scrolls then.
        if (insightsY.current !== undefined) {
          scrollRef.current?.scrollTo({ y: insightsY.current, animated: true });
        }
      };
    
      return (
        <ScrollView ref={scrollRef}>
          <Balances />
          {/* A direct child of the ScrollView, so its layout y is its offset in the content. */}
          <View
            onLayout={(event) => {
              const { y } = event.nativeEvent.layout;
              if (y === insightsY.current) return; // same position: nothing to correct
              insightsY.current = y;
              if (Date.now() < followUntil.current) {
                scrollRef.current?.scrollTo({ y, animated: true });
              }
            }}
          >
            <GenerativeUISurface
              id="insights"
              ui={bankUI}
              description="Under the balances. Show spending insights here."
              components={["InsightCard"]}
              fallback={<InsightsPlaceholder />}
              onGenerationStart={scrollToInsights}
            />
          </View>
        </ScrollView>
      );
    }

## Related

  * [`GenerativeUIActivity`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity): render one agent's surface from its activity message
  * [Surfaces](https://docs.copilotkit.ai/generative-ui/components/surfaces): descriptions, component limits and one target per item


