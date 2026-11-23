---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput/
title: CopilotChatInput
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:27.040619+00:00
---

# CopilotChatInput

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput/

Angular/Components

# CopilotChatInput

Angular standalone component for chat input, tools, file upload, and audio transcription

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatInput` is the input area of the chat. It renders the textarea, the send button, an optional tools menu, an add-file button, and the audio transcription controls. It has three modes: `"input"` (the default textarea), `"transcribe"` (records audio and shows transcription controls), and `"processing"` (disables the textarea and send button). The component never enters `"processing"` on its own. Set it with `mode="processing"`.

`CopilotChatInput` requires a parent injector to provide `ChatState`. It reads that state through `injectChatState` and wires submission, value changes, transcription, and file uploads to it. Its outputs fire in addition to that built-in behavior, so you can observe interactions without disabling them.

By default, [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView) renders this input.

## UsageCopy Anchor Link

`CopilotChatInput` is a standalone component with the selector `copilot-chat-input`. The example below provides the required `ChatState`. Use [`CopilotChat`](https://docs.copilotkit.ai/reference/angular/components/CopilotChat) when you want CopilotKit to manage this state for you.

src/app/chat.component.ts

Copy Text
    
    
    import { Component, forwardRef, signal } from "@angular/core";
    import { ChatState, CopilotChatInput } from "@copilotkit/angular";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      imports: [CopilotChatInput],
      providers: [
        {
          provide: ChatState,
          useExisting: forwardRef(() => ChatComponent),
        },
      ],
      template: `
        <copilot-chat-input
          [autoFocus]="true"
          (submitMessage)="onSubmit($event)"
        />
      `,
    })
    export class ChatComponent extends ChatState {
      readonly inputValue = signal("");
    
      submitInput(value: string) {
        // Send the message through your chat state owner.
      }
    
      changeInput(value: string) {
        this.inputValue.set(value);
      }
    
      onSubmit(value: string) {
        console.log("user submitted:", value);
      }
    }

## InputsCopy Anchor Link

### Behavior inputsCopy Anchor Link

Prop

Type

`mode?`"input" | "transcribe" | "processing"

`toolsMenu?`(ToolsMenuItem | "-")[]

`autoFocus?`boolean

`value?`string

`inputClass?`string

`additionalToolbarItems?`TemplateRef<any>

### Textarea inputsCopy Anchor Link

Prop

Type

`textAreaClass?`string

`textAreaMaxRows?`number

`textAreaPlaceholder?`string

### Slot override inputsCopy Anchor Link

Each interactive piece can be replaced with a component class (`*Component`). Templates for the same slots are read from content projection.

Prop

Type

`sendButtonComponent?`Type<any>

`toolbarComponent?`Type<any>

`textAreaComponent?`Type<any>

`audioRecorderComponent?`Type<any>

`startTranscribeButtonComponent?`Type<any>

`cancelTranscribeButtonComponent?`Type<any>

`finishTranscribeButtonComponent?`Type<any>

`addFileButtonComponent?`Type<any>

`toolsButtonComponent?`Type<any>

The current release declares class inputs for the toolbar, audio recorder, transcription buttons, add-file button, and tools button, but does not apply them. `sendButtonClass` and `textAreaClass` do apply.

## OutputsCopy Anchor Link

These events fire in addition to the input's built-in handling, so you can observe interactions without replacing default behavior.

Prop

Type

`submitMessage?`string

`valueChange?`string

`startTranscribe?`void

`cancelTranscribe?`void

`finishTranscribe?`void

`finishTranscribeWithAudio?`Blob

`addFile?`void

## SlotsCopy Anchor Link

For deep customization, provide named `<ng-template>` elements inside `<copilot-chat-input>`. Each is read with `contentChild` and takes precedence over the corresponding `*Component` input. The send button and toolbar templates receive a typed context.

Prop

Type

`sendButton?`TemplateRef<SendButtonContext>

`toolbar?`TemplateRef<ToolbarContext>

`textArea?`TemplateRef<any>

`audioRecorder?`TemplateRef<any>

`startTranscribeButton?`TemplateRef<any>

`cancelTranscribeButton?`TemplateRef<any>

`finishTranscribeButton?`TemplateRef<any>

`addFileButton?`TemplateRef<any>

`toolsButton?`TemplateRef<any>

### Tools menu exampleCopy Anchor Link

src/app/chat.component.ts

Copy Text
    
    
    import { Component, forwardRef, signal } from "@angular/core";
    import { ChatState, CopilotChatInput } from "@copilotkit/angular";
    import type { ToolsMenuItem } from "@copilotkit/angular";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      imports: [CopilotChatInput],
      providers: [
        {
          provide: ChatState,
          useExisting: forwardRef(() => ChatComponent),
        },
      ],
      template: `
        <copilot-chat-input [toolsMenu]="toolsMenu" />
      `,
    })
    export class ChatComponent extends ChatState {
      readonly inputValue = signal("");
      toolsMenu: (ToolsMenuItem | "-")[] = [
        { label: "Summarize", action: () => this.summarize() },
        "-",
        { label: "Translate", action: () => this.translate() },
      ];
    
      summarize() {}
      translate() {}
    
      submitInput(value: string) {
        // Send the message through your chat state owner.
      }
    
      changeInput(value: string) {
        this.inputValue.set(value);
      }
    }

How is this guide?

GoodBad

[Previous PageCopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage)[Next PageCopilotChatMessageView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView)
