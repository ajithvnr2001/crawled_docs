---
url: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity/
title: GenerativeUIActivity
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:51.713251+00:00
---

# GenerativeUIActivity

> Source: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity/

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

# GenerativeUIActivity

Render the surface that an agent rendered with render_ui, from its activity message, in a chat list or on a screen with no chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

Every surface the agent renders arrives as an **activity message** in `agent.messages`, and is updated in place while the agent streams. `GenerativeUIActivity` draws the surface of one such message with the components of your catalog. Put it wherever your app shows the agent's output: in your own message list, one per activity message, or on a screen with no chat at all, for example a home screen that a background agent run composes.

Like the web chat, it shows only surfaces aimed at the chat (target `"chat"`). A surface aimed at a named [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface) renders there, so a message list that passes every activity message does not show it twice; pass `target` to show such a surface here instead. It reads the surface from the thread of the `agent` you pass, so it shows that agent's output even when another agent ran last.

Render it under [`GenerativeUIProvider`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider). It renders nothing, and does not call `Wrapper`, when:

  * the message is not a generative UI activity;
  * its content is malformed (in development it warns with the issues);
  * there is no `GenerativeUIProvider` above it, or the provider has no `ui` (in development it warns);
  * `agent` is `undefined` or has no `threadId` yet (in development it warns);
  * the surface's target is not `target`;
  * the agent deleted the surface, or the provider holds no surface for it.



In development each instance warns once for each distinct cause, also when a cause goes away and comes back; a `message` with another id warns again. The first case and the last two are silent. The warnings are development-only: in a release build every case renders nothing without a word, and none of them reaches `onError`.

For a complete walkthrough, see [Generative UI with your own components](https://docs.copilotkit.ai/react-native#generative-ui-with-your-own-components).

## Import
    
    
    import {
      DefaultGenerativeUIActivityWrapper,
      GenerativeUIActivity,
      isGenerativeUIActivity,
    } from "@copilotkit/react-native/generative-ui";

## Props

Prop

Type

`message`GenerativeUIActivityMessage

Prop

Type

`agent`{ threadId?: string; agentId?: string } | undefined

Prop

Type

`target?`string

Prop

Type

`Wrapper?`ComponentType<GenerativeUIActivityWrapperProps>

## `isGenerativeUIActivity`
    
    
    function isGenerativeUIActivity<M extends GenerativeUIActivityMessage>(
      message: M,
    ): message is M & { role: "activity"; activityType: "generative-ui-surface" };

True for the activity messages that carry a generated surface: `role` is `"activity"` and `activityType` is the generative UI activity type. It is a type guard, so `agent.messages.filter(isGenerativeUIActivity)` gives activity messages. It does not check the content; `GenerativeUIActivity` does.

## Usage

### In a message list
    
    
    <FlatList
      data={agent.messages}
      keyExtractor={(message) => message.id}
      renderItem={({ item }) =>
        isGenerativeUIActivity(item) ? (
          <GenerativeUIActivity message={item} agent={agent} />
        ) : (
          <MessageBubble message={item} />
        )
      }
    />

A surface aimed at a named [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface) target renders nothing in the list, because `target` defaults to `"chat"`, so it does not show twice. It still takes a cell of the list, and so does a surface that the agent deleted, so the [guide's chat screen](https://docs.copilotkit.ai/react-native#render-surfaces-in-your-message-list) leaves both out of `data` with its `isChatSurface` helper.

### On a screen with no chat
    
    
    import { isChatSurface } from "./agentTurns"; // the helper from the guide
    
    const { agent } = useAgent({ agentId: "home" });
    // The surfaces that render here: aimed at the chat, and not deleted.
    const surfaces = agent.messages.filter(isChatSurface);
    
    return surfaces.length > 0 ? (
      <View>
        {surfaces.map((message) => (
          <GenerativeUIActivity key={message.id} message={message} agent={agent} />
        ))}
      </View>
    ) : (
      <HomeSkeleton />
    );

Render every chat surface, not only the latest activity message: the latest can be a deleted surface, or one aimed at a named target, and render nothing. Filtering with `isChatSurface` keeps the skeleton up until a surface that renders here arrives; `agent.messages.filter(isGenerativeUIActivity)` would drop the skeleton for a named-target or deleted surface and leave the screen blank. `isChatSurface` is defined in the [guide](https://docs.copilotkit.ai/react-native#render-surfaces-in-your-message-list).

Something has to run the `home` agent, and this part does not: on its own it shows the skeleton forever. The [home screen step](https://docs.copilotkit.ai/react-native#compose-a-screen-with-no-chat) of the guide starts the run once `isReady` from `useAgent` is true, so it goes to the registered agent rather than the stand-in used while the runtime connects, and shows a spinner while it runs and, when a run fails or renders nothing here, the reason with a retry, after it has taken the run's prompt back.

### With your own streaming and error state
    
    
    import { ActivityIndicator, Text, View } from "react-native";
    import type { GenerativeUIActivityWrapperProps } from "@copilotkit/react-native/generative-ui";
    
    function SurfaceCard({ isStreaming, error, children }: GenerativeUIActivityWrapperProps) {
      return (
        <View style={{ borderRadius: 12, padding: 12, backgroundColor: "#fafafa" }}>
          {children}
          {isStreaming ? <ActivityIndicator /> : null}
          {error ? <Text accessibilityRole="alert">{error.message}</Text> : null}
        </View>
      );
    }
    
    <GenerativeUIActivity message={message} agent={agent} Wrapper={SurfaceCard} />;

## Related

  * [`GenerativeUIProvider`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider): turns on generative UI and holds the catalog
  * [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface): a named place where the agent can render


