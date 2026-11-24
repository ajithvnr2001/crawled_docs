---
url: https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage/
title: AssistantMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:51.668236+00:00
---

# AssistantMessage

> Source: https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage/

React Native/Components

# AssistantMessage

A left-aligned assistant chat bubble that renders Markdown content, with an optional typing indicator and timestamp.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`AssistantMessage` renders a left-aligned chat bubble for assistant turns. Content is rendered as Markdown through [`CopilotMarkdown`](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown). When `isLoading` is `true`, the bubble also shows an animated typing indicator below any content. Useful when building a custom chat UI on top of the headless [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat). For the user side, see [`UserMessage`](https://docs.copilotkit.ai/reference/react-native/components/UserMessage).

## ImportCopy Anchor Link

Copy Text
    
    
    import { AssistantMessage } from "@copilotkit/react-native/components";

## PropsCopy Anchor Link

Prop

Type

`content`string

`isLoading?`boolean

`timestamp?`Date

`style?`ViewStyle

## UsageCopy Anchor Link

Copy Text
    
    
    import { AssistantMessage } from "@copilotkit/react-native/components";
    
    <AssistantMessage content="Hello! How can I help?" timestamp={new Date()} />;
    
    // While the agent is responding:
    <AssistantMessage content="" isLoading />;

How is this guide?

GoodBad

[Previous PageOverview](https://docs.copilotkit.ai/reference/react-native)[Next PageCopilotChat](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat)
