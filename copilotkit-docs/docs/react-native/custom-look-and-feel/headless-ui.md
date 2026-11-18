---
url: https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:54.015169+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui/

Chat/Custom Look and Feel

# Headless UI

Build your own React Native chat, or a screen that isn't a chat, on CopilotKit's hooks.

Copy MarkdownOpen

## What is this?Copy Anchor Link

A headless UI gives you **full control** over the chat experience. You bring your own views, layout, and styles. CopilotKit handles agent communication, message state, tool-call rendering, and streaming. You compose your screens from the low-level hooks, with no prebuilt chat.

On React Native, this is the main way to build a chat. `@copilotkit/react-native/headless` has the provider and every hook, and it needs no native peer dependencies.

## When should I use this?Copy Anchor Link

Use headless UI when:

  * The props of the [prebuilt chat](https://docs.copilotkit.ai/react-native/prebuilt-components) can't give you the layout or the look you need.
  * You're adding chat to an app that already has its own components and patterns.
  * You're building a screen that talks to an agent but isn't a chat, such as a dashboard or a form.
  * You want to render tool calls or agent state outside a chat.



## The core hooksCopy Anchor Link

Three hooks power it. The prebuilt chat from `/components` uses the same ones.

  * `useAgent({ agentId })`: the agent, with its `messages`, `state`, and `isRunning`.
  * `useCopilotKit()`: the CopilotKit core. You call `runAgent({ agent })` and `stopAgent({ agent })` on it.
  * `useRenderToolCall()`: a function that renders any registered tool call as a React Native element.



## Minimal exampleCopy Anchor Link

The [quickstart](https://docs.copilotkit.ai/react-native/quickstart) builds the smallest version: a `FlatList` of user and assistant text, a `TextInput`, and a send button that calls `agent.addMessage` and `copilotkit.runAgent`. You get text only. Tool calls do not show until you render them yourself.

## Complete exampleCopy Anchor Link

This chat shows text, tool calls with their results, and starter suggestions. It also has a stop button.

src/ChatScreen.tsx

Copy Text
    
    
    import { useState } from "react";
    import {
      FlatList,
      KeyboardAvoidingView,
      Platform,
      Pressable,
      Text,
      TextInput,
      View,
    } from "react-native";
    import {
      useAgent,
      useCopilotKit,
      useRenderToolCall,
      useSuggestions,
      type Message,
      type ToolCall,
      type ToolMessage,
    } from "@copilotkit/react-native/headless";
    
    type Row =
      | { kind: "text"; id: string; role: "user" | "assistant"; text: string }
      | { kind: "tool"; id: string; toolCall: ToolCall };
    
    // One row per text message and one per tool call.
    function toRows(messages: Message[]): Row[] {
      const rows: Row[] = [];
      for (const message of messages) {
        if (message.role === "user" && typeof message.content === "string") {
          rows.push({ kind: "text", id: message.id, role: "user", text: message.content });
        }
        if (message.role === "assistant") {
          if (message.content) {
            rows.push({ kind: "text", id: message.id, role: "assistant", text: message.content });
          }
          for (const toolCall of message.toolCalls ?? []) {
            rows.push({ kind: "tool", id: `${message.id}:${toolCall.id}`, toolCall });
          }
        }
      }
      return rows;
    }
    
    export function ChatScreen() {
      const { copilotkit } = useCopilotKit();
      const { agent } = useAgent({ agentId: "default" });
      const renderToolCall = useRenderToolCall();
      const { suggestions } = useSuggestions({ agentId: "default" });
      const [input, setInput] = useState("");
    
      // Rebuilt on every render: useAgent re-renders this screen on each change.
      const rows = toRows(agent.messages);
      const toolResults = new Map<string, ToolMessage>();
      for (const message of agent.messages) {
        if (message.role === "tool") toolResults.set(message.toolCallId, message);
      }
    
      const send = async (text: string) => {
        if (!text.trim() || agent.isRunning) return;
        setInput("");
        agent.addMessage({ id: `user-${Date.now()}`, role: "user", content: text });
        try {
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("runAgent failed", error);
        }
      };
    
      return (
        <KeyboardAvoidingView
          style={{ flex: 1 }}
          behavior={Platform.OS === "ios" ? "padding" : "height"}
        >
          <FlatList
            data={rows}
            keyExtractor={(row) => row.id}
            contentContainerStyle={{ padding: 12, gap: 8 }}
            renderItem={({ item }) => {
              if (item.kind === "tool") {
                return (
                  renderToolCall({
                    toolCall: item.toolCall,
                    toolMessage: toolResults.get(item.toolCall.id),
                  }) ?? <Text style={{ color: "#888" }}>Called {item.toolCall.function.name}</Text>
                );
              }
              return (
                <View
                  style={{
                    alignSelf: item.role === "user" ? "flex-end" : "flex-start",
                    backgroundColor: item.role === "user" ? "#4f46e5" : "#f1f1f4",
                    borderRadius: 16,
                    padding: 12,
                    maxWidth: "80%",
                  }}
                >
                  <Text style={{ color: item.role === "user" ? "#fff" : "#111" }}>{item.text}</Text>
                </View>
              );
            }}
            ListEmptyComponent={
              <View style={{ gap: 8 }}>
                {suggestions.map((suggestion) => (
                  <Pressable key={suggestion.title} onPress={() => send(suggestion.message)}>
                    <Text>{suggestion.title}</Text>
                  </Pressable>
                ))}
              </View>
            }
          />
          <View style={{ flexDirection: "row", gap: 8, padding: 8 }}>
            <TextInput
              style={{ flex: 1, borderWidth: 1, borderRadius: 8, padding: 8 }}
              value={input}
              onChangeText={setInput}
              placeholder="Type a message..."
            />
            {agent.isRunning ? (
              <Pressable onPress={() => copilotkit.stopAgent({ agent })}>
                <Text>Stop</Text>
              </Pressable>
            ) : (
              <Pressable onPress={() => send(input)}>
                <Text>Send</Text>
              </Pressable>
            )}
          </View>
        </KeyboardAvoidingView>
      );
    }

How the pieces fit:

  * **Rows.** An assistant message can carry text, tool calls, or both. `toRows` gives each tool call its own row, so the list can draw it where it happened.

  * **Tool calls.** For each call, the chat looks up the `tool` message whose `toolCallId` matches, and hands both to `renderToolCall`. The renderer gets the parsed arguments, a live `status`, and the result once it arrives. `renderToolCall` returns `null` when no renderer is registered for that tool, so the sample shows a small fallback line.

  * **Suggestions.** `useSuggestions` returns the prompts that `useConfigureSuggestions` set up. Configure them once, anywhere under the provider:

Copy Text
        
        useConfigureSuggestions({
          suggestions: [
            { title: "Plan my day", message: "Plan my day around my calendar." },
            { title: "What's due?", message: "Which tasks are due this week?" },
          ],
        });

  * **Ids.** The polyfills give Hermes `crypto.getRandomValues`, not `crypto.randomUUID`, so the sample builds message ids from a timestamp.




Register the renderers that `renderToolCall` draws with `useFrontendTool`, `useRenderTool`, `useComponent`, or `useHumanInTheLoop`. See [Tool Call Rendering](https://docs.copilotkit.ai/react-native/generative-ui/tool-rendering).

To check it, register a renderer for one of your agent's tools and ask for something that calls it. The tool card renders in your own list, between your own bubbles.

## MarkdownCopy Anchor Link

Agents often answer in markdown. A plain `Text` shows it as-is. To render it, use `CopilotMarkdown` from `/components`, or any React Native markdown library. See [Markdown Rendering](https://docs.copilotkit.ai/react-native/custom-look-and-feel/markdown).

## Interrupts and approvalsCopy Anchor Link

A headless chat also places the interrupt UI itself. Call `useInterrupt` with `renderInChat: false`, and render the element it returns, for example as the list's `ListFooterComponent`. See [Headless Interrupts](https://docs.copilotkit.ai/react-native/human-in-the-loop/headless). To answer a pause from a button, see [Programmatic Control](https://docs.copilotkit.ai/react-native/programmatic-control).

How is this guide?

GoodBad

[Previous PageMarkdown Rendering](https://docs.copilotkit.ai/react-native/custom-look-and-feel/markdown)[Next PageMultimodal Attachments](https://docs.copilotkit.ai/react-native/multimodal-attachments)
