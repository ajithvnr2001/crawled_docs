---
url: https://docs.copilotkit.ai/reference/react-native/components/UserMessage/
title: UserMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:14.100817+00:00
---

# UserMessage

> Source: https://docs.copilotkit.ai/reference/react-native/components/UserMessage/

React Native/Components

# UserMessage

A right-aligned user chat bubble that renders plain text, with an optional timestamp.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`UserMessage` renders a right-aligned chat bubble for user turns. Content is shown as plain text (no Markdown), with white text on a primary-color background. Useful when building a custom chat UI on top of the headless [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat). For the assistant side, see [`AssistantMessage`](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage).

## ImportCopy Anchor Link

Copy Text
    
    
    import { UserMessage } from "@copilotkit/react-native/components";

## PropsCopy Anchor Link

Prop

Type

`content`string

`timestamp?`Date

`style?`ViewStyle

## UsageCopy Anchor Link

Copy Text
    
    
    import { UserMessage } from "@copilotkit/react-native/components";
    
    <UserMessage content="What's the weather today?" timestamp={new Date()} />;

How is this guide?

GoodBad

[Previous PageGenerativeUISurface](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUISurface)[Next PageuseAgent](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)
