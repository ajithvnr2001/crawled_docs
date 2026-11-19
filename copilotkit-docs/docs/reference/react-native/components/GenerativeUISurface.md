---
url: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface/
title: GenerativeUISurface
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:30.664114+00:00
---

# GenerativeUISurface

> Source: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface/

React Native/Components

# GenerativeUISurface

A named place in a React Native app where the agent can render UI, with a description the agent reads in each run that starts while it is mounted.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`GenerativeUISurface` marks a place in your app as a **target** for generated UI. The targets are sent when a run starts, so the agent sees its `id` and `description` in each run that starts while it is mounted, and can render a surface into it. Until then it shows `fallback`.

A target follows the thread that is active in the provider: the thread of the last run that started on the core, of any agent, also one that the provider's `agentIds` leaves out. To show the output of one particular agent, for example a background run on a home screen, render that agent's activity message with [`GenerativeUIActivity`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity) instead.

Render it under [`GenerativeUIProvider`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider): outside one it throws, naming `GenerativeUIProvider`, unlike `GenerativeUIActivity`, which renders nothing. Under a provider that has no `ui`, it shows its `fallback` and warns in development. The concepts are the same as on the web; see [Surfaces](https://docs.copilotkit.ai/generative-ui/components/surfaces).

The operations of its surface that were rejected, by the runtime or by the app, reach its `Wrapper` (see below); by default it shows "Part of this UI couldn't be shown." under the surface. The ones that the runtime rejected never reach `errorBoundary.onError`; the ones that the app rejected go there too, as usual.

## ImportCopy Anchor Link

Copy Text
    
    
    import { GenerativeUISurface } from "@copilotkit/react-native/generative-ui";

## PropsCopy Anchor Link

Prop

Type

`id`string

`description?`string

`ui?`GenerativeUI

`components?`readonly GenerativeUIComponentName<UI>[]

`fallback?`ReactNode

`style?`StyleProp<ViewStyle>

`onGenerationStart?`() => void

`Wrapper?`ComponentType<GenerativeUIActivityWrapperProps>

## UsageCopy Anchor Link

Copy Text
    
    
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

## RelatedCopy Anchor Link

  * [`GenerativeUIActivity`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity): render one agent's surface from its activity message
  * [Surfaces](https://docs.copilotkit.ai/generative-ui/components/surfaces): descriptions, component limits and one target per item



How is this guide?

GoodBad

[Previous PageGenerativeUIProvider](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider)[Next PageUserMessage](https://docs.copilotkit.ai/reference/react-native/components/UserMessage)
