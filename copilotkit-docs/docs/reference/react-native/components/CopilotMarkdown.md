---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown/
title: CopilotMarkdown
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:51.574267+00:00
---

# CopilotMarkdown

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown/

React Native/Components

# CopilotMarkdown

Render Markdown text with React Native styling tuned for chat. Renders streaming content as it arrives.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotMarkdown` renders a Markdown string with sensible React Native styling, built on [`react-native-streamdown`](https://www.npmjs.com/package/react-native-streamdown). It renders incomplete (streaming) Markdown incrementally as content arrives, which makes it ideal for assistant messages. Requires the `react-native-streamdown` peer dependency. [`AssistantMessage`](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage) renders its content with this component.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotMarkdown, defaultMarkdownStyles } from "@copilotkit/react-native/components";

## PropsCopy Anchor Link

Prop

Type

`content`string

`style?`MarkdownStyle

`streamingAnimation?`boolean

## `defaultMarkdownStyles`Copy Anchor Link

The default style map. The component merges `style` over these defaults one element at a time. To change one property of an element, spread the default for that element:

Copy Text
    
    
    import { CopilotMarkdown, defaultMarkdownStyles } from "@copilotkit/react-native/components";
    
    const styles = {
      h1: { ...defaultMarkdownStyles.h1, fontSize: 28, fontWeight: "800" },
    };
    
    <CopilotMarkdown content={"# Hello\nThis is **bold**."} style={styles} />;

## UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotMarkdown } from "@copilotkit/react-native/components";
    
    <CopilotMarkdown content="**Hello** from CopilotKit!" />;

How is this guide?

GoodBad

[Previous PageCopilotKitProvider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)[Next PageCopilotModal](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal)
