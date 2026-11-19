---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotChat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:31.813868+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotChat/

React Native/Components

# CopilotChat

Headless chat primitive that wires an agent into context, plus a prebuilt full-screen chat UI from the /components subpath.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChat` connects an agent and exposes its conversation state to descendants. There are **two** versions, chosen by import path:

  * **Headless** (`@copilotkit/react-native`) renders no UI. It wires up [`useAgent`](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent), manages attachments, and exposes everything through `useCopilotChatContext` so you build the interface from React Native views.
  * **Prebuilt UI** (`@copilotkit/react-native/components`) is a ready-made full-screen chat with a message list, input bar, and optional header. See Prebuilt UI.



## Headless `CopilotChat`Copy Anchor Link

Copy Text
    
    
    import { CopilotChat, useCopilotChatContext } from "@copilotkit/react-native";

### PropsCopy Anchor Link

Prop

Type

`agentId?`string

`agentName?`string

`threadId?`string

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

`throttleMs?`number

`attachments?`NativeAttachmentsConfig

`children?`ReactNode

### `useCopilotChatContext`Copy Anchor Link

Call inside a `<CopilotChat>` tree to read the conversation state and actions. Throws if called outside a `<CopilotChat>`.

Copy Text
    
    
    function useCopilotChatContext(): CopilotChatContextValue;

Prop

Type

`agent?`AbstractAgent

`isRunning?`boolean

`messages?`Message[]

`attachments?`Attachment[]

`attachmentsEnabled?`boolean

`openPicker?`() => Promise<void>

`removeAttachment?`(id: string) => void

`submitMessage?`(text: string) => Promise<void>

### UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotChat, useCopilotChatContext } from "@copilotkit/react-native";
    import { useState } from "react";
    import { FlatList, Text, TextInput, TouchableOpacity, View } from "react-native";
    
    function ChatUI() {
      const { messages, isRunning, submitMessage } = useCopilotChatContext();
      const [text, setText] = useState("");
    
      return (
        <View style={{ flex: 1 }}>
          <FlatList
            data={messages.filter((m) => m.content)}
            keyExtractor={(m, i) => m.id ?? String(i)}
            renderItem={({ item }) => (
              <Text style={{ padding: 12 }}>{item.content}</Text>
            )}
          />
          <View style={{ flexDirection: "row", padding: 8 }}>
            <TextInput
              style={{ flex: 1, borderWidth: 1, borderRadius: 8, padding: 8 }}
              value={text}
              onChangeText={setText}
              placeholder="Type a message..."
            />
            <TouchableOpacity
              disabled={isRunning}
              onPress={() => {
                submitMessage(text);
                setText("");
              }}
              style={{ padding: 8 }}
            >
              <Text>Send</Text>
            </TouchableOpacity>
          </View>
        </View>
      );
    }
    
    export function ChatScreen() {
      return (
        <CopilotChat agentId="default">
          <ChatUI />
        </CopilotChat>
      );
    }

## Prebuilt UICopy Anchor Link

For a ready-made interface, import `CopilotChat` from the `/components` subpath. It renders a full-screen chat with a message list, an input bar, an optional header, and tool calls. Tool calls render with the renderers that [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool), `useFrontendTool`, and `useComponent` register. For a modal, a drawer, or a popup, see [`CopilotModal`](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal), [`CopilotSidebar`](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar), or [`CopilotPopup`](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup).

Copy Text
    
    
    import { CopilotChat } from "@copilotkit/react-native/components";

### PropsCopy Anchor Link

The prebuilt UI components select their agent with `agentName` (not the headless `agentId`). The two are equivalent; `agentName` is the prop name the prebuilt components currently expose.

Prop

Type

`agentName?`string

`placeholder?`string

`initialMessages?`string[]

`emptyStateTitle?`string

`emptyStateSubtitle?`string

`headerTitle?`string

`showHeader?`boolean

`style?`ViewStyle

`messageContainerStyle?`ViewStyle

`inputContainerStyle?`ViewStyle

`onSendMessage?`(text: string) => void

`FlatListComponent?`React.ComponentType<any>

`disableKeyboardAvoiding?`boolean

### UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotChat } from "@copilotkit/react-native/components";
    
    export function ChatScreen() {
      return (
        <CopilotChat
          agentName="default"
          headerTitle="Assistant"
          placeholder="Ask me anything..."
          initialMessages={["What's the weather?", "Summarize my tasks"]}
        />
      );
    }

How is this guide?

GoodBad

[Previous PageAssistantMessage](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage)[Next PageCopilotKitProvider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)
