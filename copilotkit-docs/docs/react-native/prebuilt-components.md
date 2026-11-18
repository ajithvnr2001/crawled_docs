---
url: https://docs.copilotkit.ai/react-native/prebuilt-components/
title: Prebuilt Components
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:55.231319+00:00
---

# Prebuilt Components

> Source: https://docs.copilotkit.ai/react-native/prebuilt-components/

Chat

# Prebuilt Components

Drop-in React Native chat surfaces, from a full-screen chat to a bottom sheet, a popup, and a drawer.

Copy MarkdownOpen

## Prebuilt components for agentic chatCopy Anchor Link

`@copilotkit/react-native` ships two kinds of prebuilt pieces:

  * **A rendered chat** , from `@copilotkit/react-native/components`. `CopilotChat` draws the message list, the composer, a header, tool calls, and interrupts. `CopilotModal` puts the same chat in a bottom sheet.
  * **Chrome for your own chat** , from `@copilotkit/react-native`. `CopilotPopup` draws a floating button and a modal card. `CopilotSidebar` draws a drawer that slides in from the right. Both draw the frame only. You put your chat UI inside them.



Component| Import| What it draws| Native peers  
---|---|---|---  
`CopilotChat`| `/components`| A full-screen chat| `@gorhom/bottom-sheet`, `react-native-gesture-handler`, `react-native-reanimated`, `react-native-streamdown`  
`CopilotModal`| `/components`| The same chat in a bottom sheet| Same as above  
`CopilotPopup`| root| A floating button and a modal card around your chat UI| `expo-document-picker`, `expo-file-system`  
`CopilotSidebar`| root| A right-side drawer around your chat UI| `expo-document-picker`, `expo-file-system`  
  
Metro resolves every peer of a surface when you import from it, even peers of components you don't use. See [Import surfaces](https://docs.copilotkit.ai/react-native/quickstart#import-surfaces). Follow each library's own setup guide. For example, `react-native-streamdown` has peers of its own and a required `react-native-worklets` setup, described in its [installation guide](https://github.com/software-mansion-labs/react-native-streamdown#installation).

Two components named CopilotChat

The root `CopilotChat` and `CopilotModal` draw nothing. They give an agent to their children through `useCopilotChatContext`. The ones that draw a chat come from `@copilotkit/react-native/components`. If you get a blank screen, check the import path.

## The customization ladderCopy Anchor Link

Start at the top and step down only when you need more control.

  1. **Drop in the rendered chat.** Render `CopilotChat` or `CopilotModal` from `/components`. Streaming, tool calls, and interrupts are wired up.
  2. **Adjust it with props.** Set the header title, the placeholder, the empty state, starter prompts, and container styles.
  3. **Put your own chat in the chrome.** Render your UI inside `CopilotPopup` or `CopilotSidebar`, and read the conversation with `useCopilotChatContext`.
  4. **Go fully headless.** Build any layout from `useAgent`, `useCopilotKit`, and `useRenderToolCall`. See [Headless UI](https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui).



## Drop-in chatCopy Anchor Link

Wrap your app in `CopilotKitProvider` and render `CopilotChat` from `/components`. The provider from `/headless` installs the polyfills. The `/components` entry relies on it for that.

App.tsx

Copy Text
    
    
    import { CopilotKitProvider } from "@copilotkit/react-native/headless";
    import { CopilotChat } from "@copilotkit/react-native/components";
    
    // See the quickstart for emulator and device hosts.
    const runtimeUrl = "http://localhost:8200/api/copilotkit";
    
    export default function App() {
      return (
        <CopilotKitProvider runtimeUrl={runtimeUrl}>
          <CopilotChat
            agentName="default"
            headerTitle="Assistant"
            placeholder="Ask me anything..."
            emptyStateTitle="How can I help?"
            initialMessages={["What can you do?", "Summarize my tasks"]}
          />
        </CopilotKitProvider>
      );
    }

What the rendered chat does:

  * It picks its agent with `agentName`, not `agentId`. The default is `"default"`.
  * It shows `initialMessages` as tappable prompts while the conversation is empty. A tap sends that text.
  * It draws each tool call with the renderer that `useFrontendTool`, `useRenderTool`, `useComponent`, or `useHumanInTheLoop` registered. A call with no renderer shows as a short "Called: tool_name" line.
  * It draws the element from [`useInterrupt`](https://docs.copilotkit.ai/react-native/human-in-the-loop/useInterrupt) after the last message.
  * It shows an error line above the composer when a run fails.



It does not show attachments, and it does not read `useConfigureSuggestions`. For those, build your own chat. See [Multimodal Attachments](https://docs.copilotkit.ai/react-native/multimodal-attachments) and [Headless UI](https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui).

### Adjust the look with propsCopy Anchor Link

The rendered chat takes three style props: `style` for the outer container, `messageContainerStyle` for the message list, and `inputContainerStyle` for the composer bar. `showHeader={false}` hides the header. The message bubbles have fixed colors. To change them, render your own bubbles in a headless chat.

Copy Text
    
    
    <CopilotChat
      showHeader={false}
      style={{ backgroundColor: "#fafafa" }}
      messageContainerStyle={{ paddingHorizontal: 24 }}
      inputContainerStyle={{ borderTopWidth: 0 }}
    />

## Bottom sheetCopy Anchor Link

`CopilotModal` from `/components` opens the rendered chat in a [`@gorhom/bottom-sheet`](https://ui.gorhom.dev/components/bottom-sheet/). Open it with a ref, or control it with the `visible` prop. The bottom sheet needs `GestureHandlerRootView` from `react-native-gesture-handler` at the root of your app.

App.tsx

Copy Text
    
    
    import { useRef } from "react";
    import { Button } from "react-native";
    import { GestureHandlerRootView } from "react-native-gesture-handler";
    import { CopilotKitProvider } from "@copilotkit/react-native/headless";
    import {
      CopilotModal,
      type CopilotModalRef,
    } from "@copilotkit/react-native/components";
    
    const runtimeUrl = "http://localhost:8200/api/copilotkit";
    
    export default function App() {
      const modalRef = useRef<CopilotModalRef>(null);
    
      return (
        <GestureHandlerRootView style={{ flex: 1 }}>
          <CopilotKitProvider runtimeUrl={runtimeUrl}>
            <Button title="Ask the assistant" onPress={() => modalRef.current?.open()} />
            <CopilotModal
              ref={modalRef}
              agentName="default"
              headerTitle="Assistant"
              snapPoints={["50%", "90%"]}
            />
          </CopilotKitProvider>
        </GestureHandlerRootView>
      );
    }

Swipe down or tap the backdrop to close the sheet. `onDismiss` fires when it closes.

## Popup and drawer around your own chatCopy Anchor Link

`CopilotPopup` and `CopilotSidebar` come from the package root. Each one shows a floating chat button, then opens a frame with a header and a close button. Inside the frame, they mount the root `CopilotChat`, so your children read the conversation with `useCopilotChatContext`:

src/AssistantPopup.tsx

Copy Text
    
    
    import { useState } from "react";
    import { FlatList, Text, TextInput, TouchableOpacity, View } from "react-native";
    import { CopilotPopup, useCopilotChatContext } from "@copilotkit/react-native";
    
    function PopupChat() {
      const { messages, isRunning, submitMessage } = useCopilotChatContext();
      const [text, setText] = useState("");
    
      return (
        <View style={{ flex: 1 }}>
          <FlatList
            data={messages.filter(
              (m) => (m.role === "user" || m.role === "assistant") && typeof m.content === "string" && m.content,
            )}
            keyExtractor={(m) => m.id}
            renderItem={({ item }) => <Text style={{ padding: 12 }}>{item.content}</Text>}
          />
          <View style={{ flexDirection: "row", padding: 8 }}>
            <TextInput
              style={{ flex: 1, borderWidth: 1, borderRadius: 8, padding: 8 }}
              value={text}
              onChangeText={setText}
              placeholder="Type a message..."
            />
            <TouchableOpacity
              disabled={isRunning || !text.trim()}
              onPress={() => {
                void submitMessage(text);
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
    
    export function AssistantPopup() {
      return (
        <CopilotPopup agentId="default" headerTitle="Assistant" height="70%">
          <PopupChat />
        </CopilotPopup>
      );
    }

Render `AssistantPopup` as the last child of a screen's root view that has `flex: 1`. The button floats in the bottom-right corner.

`CopilotSidebar` works the same way. It takes `width` (a number, or a percentage such as `"85%"`) in place of `height`. It draws the drawer above the screen with absolute positioning, so render it as the last child of the screen's root view too.

Both components take a `ref` with `open()`, `close()`, and `toggle()`, for your own button. Set `showToggleButton={false}` to hide the floating button. Pass `attachments` to turn on file picking for the inner chat. See [Multimodal Attachments](https://docs.copilotkit.ai/react-native/multimodal-attachments).

Tool calls and interrupts in your own chat UI

The root `CopilotChat` inside the popup and the drawer does not draw tool calls or interrupts. Render them in your list with `useRenderToolCall`, and place the `useInterrupt` element yourself with `renderInChat: false`. See [Headless UI](https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui).

## Which surface?Copy Anchor Link

  * [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#prebuilt-ui): a full screen or a pane that fills its container.
  * [`CopilotModal`](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal#prebuilt-ui): a bottom sheet over any screen.
  * [`CopilotPopup`](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup): a floating button and a modal card, with your own chat inside.
  * [`CopilotSidebar`](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar): a slide-in drawer, with your own chat inside.



## Choose your AI backendCopy Anchor Link

[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (Python)](https://docs.copilotkit.ai/react-native/langgraph-python/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (TypeScript)](https://docs.copilotkit.ai/react-native/langgraph-typescript/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (FastAPI)](https://docs.copilotkit.ai/react-native/langgraph-fastapi/prebuilt-components)### [Langchain DeepAgents](https://docs.copilotkit.ai/react-native/deepagents/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/google-adk.png)Google ADK](https://docs.copilotkit.ai/react-native/google-adk/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/mastra.svg)Mastra](https://docs.copilotkit.ai/react-native/mastra/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/crewai-crews.png)CrewAI Flows](https://docs.copilotkit.ai/react-native/crewai-crews/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/pydantic-ai.svg)PydanticAI](https://docs.copilotkit.ai/react-native/pydantic-ai/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/google-antigravity.png)Google Antigravity](https://docs.copilotkit.ai/react-native/google-antigravity/prebuilt-components)### [OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/react-native/openai-agents-python/prebuilt-components)### [Claude Agent SDK (Python)](https://docs.copilotkit.ai/react-native/claude-sdk-python/prebuilt-components)### [Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/react-native/claude-sdk-typescript/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/agno.png)Agno](https://docs.copilotkit.ai/react-native/agno/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/ag2-light.svg)![](https://docs.copilotkit.ai/logos/frameworks/ag2-dark.svg)AG2](https://docs.copilotkit.ai/react-native/ag2/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/llamaindex.png)LlamaIndex](https://docs.copilotkit.ai/react-native/llamaindex/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (Python)](https://docs.copilotkit.ai/react-native/strands/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (TypeScript)](https://docs.copilotkit.ai/react-native/strands-typescript/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (Python)](https://docs.copilotkit.ai/react-native/ms-agent-python/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-dotnet/prebuilt-components)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Harness (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-harness-dotnet/prebuilt-components)

How is this guide?

GoodBad

[Previous PageIntelligence](https://docs.copilotkit.ai/react-native/intelligence/overview)[Next PageMarkdown Rendering](https://docs.copilotkit.ai/react-native/custom-look-and-feel/markdown)
