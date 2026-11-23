---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput/
title: CopilotChatInput
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:22.241707+00:00
---

# CopilotChatInput

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput/

React/Components

# CopilotChatInput

Primary text input and control surface for chat interactions

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatInput` is the primary text input and control surface for chat interactions. It provides a multi-line textarea that auto-grows up to 5 rows, action buttons for sending messages, voice transcription, and file attachment, and an optional tools menu for declarative command surfaces. [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) renders it below the transcript. The placeholder and button labels come from [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration).

The component operates in three modes: `"input"` (default text entry), `"transcribe"` (replaces the textarea with an audio recorder), and `"processing"` (indicates background processing is underway). When text spans multiple rows, the layout stacks the textarea above the control row.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChatInput } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## PropsCopy Anchor Link

Prop

Type

`mode?`"input" | "transcribe" | "processing"

`value?`string

`onChange?`(value: string) => void

`autoFocus?`boolean

`isRunning?`boolean

`onSubmitMessage?`(value: string) => void

`onStop?`() => void

`onStartTranscribe?`() => void

`onCancelTranscribe?`() => void

`onFinishTranscribe?`() => void

`onFinishTranscribeWithAudio?`(audioBlob: Blob) => Promise<void>

`onAddFile?`() => void

`toolsMenu?`(ToolsMenuItem | '-')[]

`children?`(props: { textArea: React.ReactElement; sendButton: React.ReactElement; addMenuButton: React.ReactElement; startTranscribeButton: React.ReactElement; cancelTranscribeButton: React.ReactElement; finishTranscribeButton: React.ReactElement; audioRecorder: React.ReactElement; disclaimer: React.ReactElement }) => React.ReactNode

## SlotsCopy Anchor Link

All slot props follow the CopilotKit slot system: each accepts a replacement React component, a `className` string that is merged into the default component's classes, or a partial props object that extends the default component.

Prop

Type

`textArea?`SlotValue<typeof CopilotChatInput.TextArea>

`sendButton?`SlotValue<typeof CopilotChatInput.SendButton>

`startTranscribeButton?`SlotValue<typeof CopilotChatInput.StartTranscribeButton>

`cancelTranscribeButton?`SlotValue<typeof CopilotChatInput.CancelTranscribeButton>

`finishTranscribeButton?`SlotValue<typeof CopilotChatInput.FinishTranscribeButton>

`addMenuButton?`SlotValue<typeof CopilotChatInput.AddMenuButton>

`audioRecorder?`SlotValue<typeof CopilotChatAudioRecorder>

## ToolsMenuItemCopy Anchor Link

The `ToolsMenuItem` type defines items in the tools menu. Items can trigger actions directly or contain nested submenus.

Copy Text
    
    
    type ToolsMenuItem = { label: string } & (
      | { action: () => void }
      | { items: (ToolsMenuItem | "-")[] }
    );

Prop

Type

`label`string

`action?`() => void

`items?`(ToolsMenuItem | '-')[]

### SeparatorsCopy Anchor Link

Use the string `"-"` as an array entry to render a visual separator between menu items:

Copy Text
    
    
    toolsMenu={[
      { label: "Search", action: () => search() },
      "-",
      { label: "Settings", action: () => openSettings() },
    ]}

### Nested SubmenusCopy Anchor Link

Menu items with an `items` array render as expandable submenus:

Copy Text
    
    
    toolsMenu={[
      {
        label: "Export",
        items: [
          { label: "As PDF", action: () => exportPDF() },
          { label: "As CSV", action: () => exportCSV() },
          "-",
          { label: "Print", action: () => printDoc() },
        ],
      },
    ]}

## CopilotChatAudioRecorderCopy Anchor Link

A visual audio waveform component used during transcription mode. It displays a real-time waveform visualization of the microphone input and exposes an imperative API via `ref`.

### ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChatAudioRecorder } from "@copilotkit/react-core/v2";

### Imperative APICopy Anchor Link

The component exposes the following imperative methods via React `ref`:

Prop

Type

`state?`"idle" | "recording" | "processing"

`start?`() => Promise<void>

`stop?`() => Promise<Blob>

`dispose?`() => void

### UsageCopy Anchor Link

Copy Text
    
    
    function CustomRecorder() {
      const recorderRef = useRef(null);
    
      return (
        <div>
          <CopilotChatAudioRecorder ref={recorderRef} />
          <button onClick={() => recorderRef.current?.start()}>Record</button>
          <button onClick={() => recorderRef.current?.stop()}>Stop</button>
        </div>
      );
    }

## UsageCopy Anchor Link

### Basic Chat InputCopy Anchor Link

Copy Text
    
    
    function ChatInput() {
      const [value, setValue] = useState("");
    
      return (
        <CopilotChatInput
          value={value}
          onChange={setValue}
          onSubmitMessage={(text) => {
            sendMessage(text);
            setValue("");
          }}
          autoFocus
        />
      );
    }

### With Voice TranscriptionCopy Anchor Link

Copy Text
    
    
    function VoiceInput() {
      const [mode, setMode] = useState<"input" | "transcribe">("input");
      const [value, setValue] = useState("");
    
      return (
        <CopilotChatInput
          mode={mode}
          value={value}
          onChange={setValue}
          onSubmitMessage={(text) => sendMessage(text)}
          onStartTranscribe={() => setMode("transcribe")}
          onCancelTranscribe={() => setMode("input")}
          onFinishTranscribe={() => setMode("input")}
          onFinishTranscribeWithAudio={async (blob) => {
            const text = await transcribeAudio(blob);
            setValue(text);
          }}
        />
      );
    }

### With Tools MenuCopy Anchor Link

Copy Text
    
    
    function InputWithTools() {
      return (
        <CopilotChatInput
          onSubmitMessage={(text) => sendMessage(text)}
          toolsMenu={[
            { label: "Search the web", action: () => triggerSearch() },
            { label: "Analyze data", action: () => triggerAnalysis() },
            "-",
            {
              label: "Export",
              items: [
                { label: "As PDF", action: () => exportPDF() },
                { label: "As Markdown", action: () => exportMarkdown() },
              ],
            },
          ]}
        />
      );
    }

### With Stop Button During ExecutionCopy Anchor Link

Copy Text
    
    
    function ChatInputWithAgent() {
      const { agent } = useAgent();
      const { copilotkit } = useCopilotKit();
    
      return (
        <CopilotChatInput
          isRunning={agent.isRunning}
          onSubmitMessage={(text) => {
            agent.addMessage({
              role: "user",
              content: text,
              id: crypto.randomUUID(),
            });
            // Drive the run through CopilotKit so registered frontend tools
            // execute and the run is tracked for stop.
            copilotkit.runAgent({ agent });
          }}
          onStop={() => copilotkit.stopAgent({ agent })}
          autoFocus
        />
      );
    }

### Custom Layout with Children Render PropCopy Anchor Link

Copy Text
    
    
    function CustomLayoutInput() {
      return (
        <CopilotChatInput onSubmitMessage={(text) => sendMessage(text)}>
          {({ textArea, sendButton }) => (
            <div className="flex items-end gap-2 rounded-xl border p-2">
              {textArea}
              {sendButton}
            </div>
          )}
        </CopilotChatInput>
      );
    }

### Styled SlotsCopy Anchor Link

Copy Text
    
    
    function StyledInput() {
      return (
        <CopilotChatInput
          onSubmitMessage={(text) => sendMessage(text)}
          textArea="font-mono text-sm bg-gray-50 rounded-lg"
          sendButton="bg-green-500 hover:bg-green-600 text-white rounded-full"
        />
      );
    }

## BehaviorCopy Anchor Link

  * **Auto-Growing Textarea** : The default textarea automatically expands as the user types, up to a maximum of 5 rows. After reaching the maximum, the textarea becomes scrollable.
  * **Layout Stacking** : When the input text spans multiple rows, the layout switches from inline (textarea and buttons side by side) to stacked (textarea above the control row containing the action buttons).
  * **Mode Switching** : Setting `mode` to `"transcribe"` replaces the textarea with the `audioRecorder` slot component. The transcription control buttons (`cancelTranscribeButton`, `finishTranscribeButton`) replace the standard send button.
  * **Controlled and Uncontrolled** : The component supports both controlled mode (via `value` and `onChange`) and uncontrolled mode (internal state management).
  * **Tools Menu** : The `toolsMenu` prop enables a declarative menu with support for flat items, separators (`"-"`), and nested submenus. The items appear in the add-menu (+) button, which always renders and is disabled when it has no items.
  * **Slot System** : Each slot prop accepts three forms -- a replacement component, a className string merged into the default, or a partial props object that extends the default component's props.



How is this guide?

GoodBad

[Previous PageCopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)[Next PageCopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)
