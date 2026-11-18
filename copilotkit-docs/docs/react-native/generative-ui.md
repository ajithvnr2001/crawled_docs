---
url: https://docs.copilotkit.ai/react-native/generative-ui/
title: Generative UI
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:54.243518+00:00
---

# Generative UI

> Source: https://docs.copilotkit.ai/react-native/generative-ui/

# Generative UI

Let your agent answer with React Native components, not just text.

Copy MarkdownOpen

Your agent can answer with UI in place of text. On React Native, you build the components, and the agent's tool calls and state decide what they show.

## ControlledCopy Anchor Link

  * [Components as Tools](https://docs.copilotkit.ai/react-native/generative-ui/tool-based): the agent calls your React Native components as tools, with `useComponent`.
  * [Tool Call Rendering](https://docs.copilotkit.ai/react-native/generative-ui/tool-rendering): render your agent's tool calls with your own components, with `useRenderTool`.
  * [State Rendering](https://docs.copilotkit.ai/react-native/generative-ui/state-rendering): render UI from agent state, with `useAgent`.



## InteractiveCopy Anchor Link

  * [Human-in-the-loop](https://docs.copilotkit.ai/react-native/human-in-the-loop): the agent pauses for a decision in a component you build, with `useHumanInTheLoop` or `useInterrupt`.



## Where the UI rendersCopy Anchor Link

The rendered `CopilotChat` and `CopilotModal` from `@copilotkit/react-native/components` draw tool calls and interrupts in the conversation. In a chat you build yourself, `useRenderToolCall` returns a React Native element for each tool call, ready for a `FlatList`. See [Headless UI](https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui).

Every renderer must return a React Native element or `null`. React Native throws when a bare string reaches a view outside a `Text`.

## Not on React Native yetCopy Anchor Link

The declarative and open-ended approaches render web content, so `@copilotkit/react-native` doesn't include them: A2UI, JSON Render, Hashbrown, MCP Apps, and Open Generative UI. The package also leaves out `useDefaultRenderTool`, whose card uses web elements, and the activity and custom message renderers. For a card your app inserts on its own, add a row to your own `FlatList` data.

How is this guide?

GoodBad

[Previous PageFrontend Tools](https://docs.copilotkit.ai/react-native/frontend-tools)[Next PageComponents as Tools](https://docs.copilotkit.ai/react-native/generative-ui/tool-based)
