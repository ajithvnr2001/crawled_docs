---
url: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity/
title: GenerativeUIActivity
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:30.603836+00:00
---

# GenerativeUIActivity

> Source: https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity/

React Native/Components

# GenerativeUIActivity

Render the surface that an agent rendered with render_ui, from its activity message, in a chat list or on a screen with no chat.

Copy MarkdownOpen

## OverviewCopy Anchor Link

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

## ImportCopy Anchor Link

Copy Text
    
    
    import {
      DefaultGenerativeUIActivityWrapper,
      GenerativeUIActivity,
      isGenerativeUIActivity,
    } from "@copilotkit/react-native/generative-ui";

## PropsCopy Anchor Link

Prop

Type

`message`GenerativeUIActivityMessage

`agent`{ threadId?: string; agentId?: string } | undefined

`target?`string

`Wrapper?`ComponentType<GenerativeUIActivityWrapperProps>

## `isGenerativeUIActivity`Copy Anchor Link

Copy Text
    
    
    function isGenerativeUIActivity<M extends GenerativeUIActivityMessage>(
      message: M,
    ): message is M & { role: "activity"; activityType: "generative-ui-surface" };

True for the activity messages that carry a generated surface: `role` is `"activity"` and `activityType` is the generative UI activity type. It is a type guard, so `agent.messages.filter(isGenerativeUIActivity)` gives activity messages. It does not check the content; `GenerativeUIActivity` does.

## UsageCopy Anchor Link

### In a message listCopy Anchor Link

Copy Text
    
    
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

### On a screen with no chatCopy Anchor Link

Copy Text
    
    
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

### With your own streaming and error stateCopy Anchor Link

Copy Text
    
    
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

## RelatedCopy Anchor Link

  * [`GenerativeUIProvider`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider): turns on generative UI and holds the catalog
  * [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface): a named place where the agent can render



How is this guide?

GoodBad

[Previous PageCopilotSidebar](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar)[Next PageGenerativeUIProvider](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIProvider)
