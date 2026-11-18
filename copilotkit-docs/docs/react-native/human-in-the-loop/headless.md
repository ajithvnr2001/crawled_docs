---
url: https://docs.copilotkit.ai/react-native/human-in-the-loop/headless/
title: Headless Interrupts
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:54.663488+00:00
---

# Headless Interrupts

> Source: https://docs.copilotkit.ai/react-native/human-in-the-loop/headless/

Human-in-the-loop

# Headless Interrupts

Answer agent interrupts from any React Native view, outside the chat.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Sometimes the agent's question belongs outside the chat: on a dashboard, in a bottom sheet, or in a native alert. A headless interrupt lets any view show the question and resume the run with the answer. No chat needs to be mounted.

On React Native this is also how a custom chat shows interrupts. The root `CopilotChat`, `CopilotPopup`, and `CopilotSidebar` don't draw them, so your own UI places them.

> **Use`useHumanInTheLoop` on this framework.** Headless interrupts need an agent that emits an AG-UI interrupt (`RUN_FINISHED` with `outcome.type === "interrupt"`) or an `on_interrupt` custom event, and a working resume path. On the Built-in Agent, interrupts are temporarily unavailable. [`useHumanInTheLoop`](https://docs.copilotkit.ai/react-native/human-in-the-loop) pauses on a tool call instead. It works on every framework that supports tool calls.

## When should I use this?Copy Anchor Link

  * **Non-chat screens** : dashboards, settings, forms, or anywhere you want the agent's question without the transcript.
  * **Your own chat** : the question appears as a row in your `FlatList`, or as its footer.
  * **Testing** : a fixed button grid is easier to drive from Detox or Maestro than a picker that appears after a model call.
  * **Custom flow control** : you need to know exactly when the interrupt arrived (for example, to disable other controls) and when it was answered.



If you just want a picker in the rendered chat, use [`useInterrupt`](https://docs.copilotkit.ai/react-native/human-in-the-loop/useInterrupt) with the default `renderInChat: true`. For pauses that the model decides on, use [`useHumanInTheLoop`](https://docs.copilotkit.ai/react-native/human-in-the-loop).

How is this guide?

GoodBad

[Previous PagePausing the Agent for Input](https://docs.copilotkit.ai/react-native/human-in-the-loop/useInterrupt)[Next PageGoverned Action Approval UI](https://docs.copilotkit.ai/react-native/human-in-the-loop/governed-actions)
