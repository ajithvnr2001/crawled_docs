---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput/
title: CopilotChatInput
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:57.241651+00:00
---

# CopilotChatInput

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput/

Vue/Components

# CopilotChatInput

Primary text input and control surface for chat interactions in Vue 3

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatInput` is the Vue 3 primary text input and control surface for chat interactions. It provides:

  * A textarea that grows up to `maxRows` rows (default 5).
  * Buttons to send a message and to record voice.
  * An optional tools menu. Binding `@add-file` adds a file item to it.
  * `/` slash commands for the menu items.



The component operates in three modes: `"input"` (default text entry), `"transcribe"` (replaces the textarea with an audio recorder), and `"processing"` (shows a spinner while background processing is underway). When text spans multiple rows, the layout stacks the textarea above the control row.

It supports both `v-model` (via `modelValue` / `update:modelValue`) and uncontrolled usage. When uncontrolled, the component manages its own text state internally and clears on submit (configurable via `clearOnSubmit`).

You opt into each control by listening for its event:

  * Microphone: renders only with `@start-transcribe`.
  * Cancel: renders only with `@cancel-transcribe`.
  * Finish: renders only with `@finish-transcribe` or `@finish-transcribe-with-audio`.
  * Send: always renders. It is enabled when a `@submit-message` listener is attached and the input has text.
  * Stop: while the agent runs, the send button becomes a stop button. It is enabled only with `@stop`.
  * Add file: binding `@add-file` adds a file item to the tools menu.



## ImportCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatInput } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## ExampleCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatInput } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    
    const value = ref("");
    
    function handleSubmit(text: string) {
      sendMessage(text);
    }
    </script>
    
    <template>
      <CopilotChatInput v-model="value" @submit-message="handleSubmit" />
    </template>

## PropsCopy Anchor Link

Prop

Type

`modelValue?`string

`mode?`"input" | "transcribe" | "processing"

`disabled?`boolean

`placeholder?`string

`autoFocus?`boolean

`clearOnSubmit?`boolean

`isRunning?`boolean

`toolsMenu?`(ToolsMenuItem | '-')[]

`maxRows?`number

`positioning?`"static" | "absolute"

`keyboardHeight?`number

`showDisclaimer?`boolean

`bottomAnchored?`boolean

## EventsCopy Anchor Link

`CopilotChatInput` emits the following events. Bind handlers with `v-on` (the `@` shorthand). Several action buttons only render when their corresponding event has a listener attached.

Prop

Type

`update:modelValue?`(value: string) => void

`submit-message?`(value: string) => void

`stop?`() => void

`add-file?`() => void

`start-transcribe?`() => void

`cancel-transcribe?`() => void

`finish-transcribe?`() => void

`finish-transcribe-with-audio?`(audioBlob: Blob) => void

## SlotsCopy Anchor Link

`CopilotChatInput` exposes named slots so you can override individual parts of the UI while keeping the component's behavior. Each slot receives scoped slot props (event handlers, state, and labels) so your custom markup can drive the same logic as the defaults.

Prop

Type

`text-area?`slot

`send-button?`slot

`add-menu-button?`slot

`start-transcribe-button?`slot

`cancel-transcribe-button?`slot

`finish-transcribe-button?`slot

`audio-recorder?`slot

`disclaimer?`slot

`layout?`slot

## ToolsMenuItemCopy Anchor Link

The `ToolsMenuItem` type defines items in the tools menu. Items can trigger actions directly or contain nested submenus.

Copy Text
    
    
    type ToolsMenuItem = { label: string } & (
      | { action: () => void; items?: never }
      | { action?: never; items: (ToolsMenuItem | "-")[] }
    );

Prop

Type

`label`string

`action?`() => void

`items?`(ToolsMenuItem | '-')[]

### SeparatorsCopy Anchor Link

Use the string `"-"` as an array entry to render a visual separator between menu items:

Copy Text
    
    
    const toolsMenu = [
      { label: "Search", action: () => search() },
      "-",
      { label: "Settings", action: () => openSettings() },
    ];

### Nested SubmenusCopy Anchor Link

A menu item with an `items` array renders as a group. The menu shows its label as a heading and lists the child items under it, indented:

Copy Text
    
    
    const toolsMenu = [
      {
        label: "Export",
        items: [
          { label: "As PDF", action: () => exportPDF() },
          { label: "As CSV", action: () => exportCSV() },
          "-",
          { label: "Print", action: () => printDoc() },
        ],
      },
    ];

## CopilotChatAudioRecorderCopy Anchor Link

A visual audio waveform component used during transcription mode. It displays a real-time waveform visualization of the microphone input and exposes an imperative API via a template `ref`.

### ImportCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatAudioRecorder } from "@copilotkit/vue/v2";
    </script>

### Imperative APICopy Anchor Link

The component exposes the following members via a template `ref`. Type the ref as `InstanceType<typeof CopilotChatAudioRecorder>`, as in the usage example below.

Prop

Type

`state?`"idle" | "recording" | "processing"

`start?`() => Promise<void>

`stop?`() => Promise<Blob>

`dispose?`() => void

### UsageCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatAudioRecorder } from "@copilotkit/vue/v2";
    
    // The component exposes `start()` / `stop()` via its instance type.
    const recorder = ref<InstanceType<typeof CopilotChatAudioRecorder> | null>(null);
    </script>
    
    <template>
      <CopilotChatAudioRecorder ref="recorder" />
      <button @click="recorder?.start()">Record</button>
      <button @click="recorder?.stop()">Stop</button>
    </template>

## UsageCopy Anchor Link

### With Voice TranscriptionCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatInput } from "@copilotkit/vue/v2";
    
    const value = ref("");
    const mode = ref<"input" | "transcribe">("input");
    
    async function handleFinishWithAudio(blob: Blob) {
      value.value = await transcribeAudio(blob);
      mode.value = "input";
    }
    </script>
    
    <template>
      <CopilotChatInput
        v-model="value"
        :mode="mode"
        @submit-message="(text) => sendMessage(text)"
        @start-transcribe="mode = 'transcribe'"
        @cancel-transcribe="mode = 'input'"
        @finish-transcribe-with-audio="handleFinishWithAudio"
      />
    </template>

### With Tools MenuCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatInput, type ToolsMenuItem } from "@copilotkit/vue/v2";
    
    const toolsMenu: (ToolsMenuItem | "-")[] = [
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
    ];
    </script>
    
    <template>
      <CopilotChatInput
        :tools-menu="toolsMenu"
        @submit-message="(text) => sendMessage(text)"
      />
    </template>

### With Stop Button During ExecutionCopy Anchor Link

This sample reads the running state from [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent).

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatInput, useAgent, useCopilotKit } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    const { copilotkit } = useCopilotKit();
    
    function handleSubmit(text: string) {
      if (!agent.value) return;
      agent.value.addMessage({
        role: "user",
        content: text,
        id: crypto.randomUUID(),
      });
      // Drive the run through CopilotKit so registered frontend tools execute and
      // the run is tracked for stop/abort.
      copilotkit.value.runAgent({ agent: agent.value });
    }
    
    function handleStop() {
      if (!agent.value) return;
      copilotkit.value.stopAgent({ agent: agent.value });
    }
    </script>
    
    <template>
      <CopilotChatInput
        :is-running="agent?.isRunning ?? false"
        auto-focus
        @submit-message="handleSubmit"
        @stop="handleStop"
      />
    </template>

### Styled SlotsCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatInput } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChatInput @submit-message="(text) => sendMessage(text)">
        <template #send-button="{ disabled, onClick }">
          <button
            :disabled="disabled"
            class="rounded-full bg-green-500 px-3 py-1 text-white"
            @click="onClick"
          >
            Send
          </button>
        </template>
      </CopilotChatInput>
    </template>

## BehaviorCopy Anchor Link

  * **Auto-Growing Textarea** : The default textarea automatically expands as the user types, up to `maxRows` rows (default 5). After reaching the maximum, the textarea becomes scrollable.
  * **Layout Stacking** : When the input text spans multiple rows, the layout switches from inline (textarea and buttons side by side) to stacked (textarea above the control row containing the action buttons). On narrow viewports the stacked layout is used unconditionally.
  * **Mode Switching** : Setting `mode` to `"transcribe"` replaces the textarea with the `audio-recorder` slot and automatically starts the recorder. The cancel and finish buttons replace the standard send button. Setting `mode` to `"processing"` shows a spinner in place of the textarea.
  * **Controlled and Uncontrolled** : The component supports controlled mode (via `v-model` / `modelValue`) and uncontrolled mode (internal state). With `clearOnSubmit` enabled (the default), the input clears after each submission.
  * **Tools Menu and Slash Commands** : The menu button always renders, and it is disabled while the menu has no items. The leaf actions of a non-empty `toolsMenu` are also available as `/` slash commands typed inline. Use arrow keys to navigate the slash menu and Enter to run the highlighted command.



How is this guide?

GoodBad

[Previous PageCopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage)[Next PageCopilotChatMessageView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView)
