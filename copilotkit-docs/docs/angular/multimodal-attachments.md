---
url: https://docs.copilotkit.ai/angular/multimodal-attachments/
title: Multimodal Attachments
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.635332+00:00
---

# Multimodal Attachments

> Source: https://docs.copilotkit.ai/angular/multimodal-attachments/

Chat

# Multimodal Attachments

Accept files in an Angular chat and send image or document content parts with a message.

Copy MarkdownOpen

`CopilotChat` includes an attachment composer. Multimodal input sends image or document content parts with the user's message.

## Enable attachmentsCopy Anchor Link

Pass an `AttachmentsConfig` to `CopilotChat`. The built-in input supports the file picker, drag and drop, and paste.

src/app/media-chat.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import {
      CopilotChat,
      type AttachmentsConfig,
    } from "@copilotkit/angular";
    
    @Component({
      selector: "app-media-chat",
      imports: [CopilotChat],
      template: `
        <copilot-chat [attachments]="attachments" />
      `,
    })
    export class MediaChatComponent {
      protected readonly attachments: AttachmentsConfig = {
        enabled: true,
        accept: "image/*,application/pdf",
        maxSize: 10 * 1024 * 1024,
        onUploadFailed: (error) => {
          console.error(error.reason, error.message);
        },
      };
    }

Without `onUpload`, files are read as base64. Supply `onUpload` to place large files in your own storage and return a URL. The selected model and backend must support each content type you allow.

## Configure attachmentsCopy Anchor Link

Define an `AttachmentsConfig` and bind it to the chat surface. The runnable Showcase accepts images and PDFs up to 10 MiB:

media-feature.component.ts

Copy Text
    
    
    const MULTIMODAL_ATTACHMENTS: AttachmentsConfig = {
      enabled: true,
      accept: "image/*,application/pdf",
      maxSize: 10 * 1024 * 1024,
    };

Expose the config as a field on your chat component:

Copy Text
    
    
    protected readonly multimodalAttachments = MULTIMODAL_ATTACHMENTS;

Then bind the field in the template:

media-chat.component.html

Copy Text
    
    
    <copilot-chat [attachments]="multimodalAttachments" />

The `accept` value filters the file picker and `maxSize` provides immediate client feedback. They are not server-side security controls. Validate file type, size, and content again wherever uploads are stored or processed. Use the configuration's upload callbacks when files should go to object storage instead of traveling inline with a message.

## Send media programmaticallyCopy Anchor Link

For a bundled sample or custom uploader, add a user message whose `content` contains normal AG-UI content parts. The Showcase constructs a text part plus an image or document part:

media-model.ts

Copy Text
    
    
    export function createMultimodalMessage(
      spec: Pick<SampleSpec, "filename" | "mimeType" | "autoPrompt">,
      base64: string,
      size: number,
      id: string,
    ): MediaAgentMessage {
      return {
        id,
        role: "user",
        content: [
          { type: "text", text: spec.autoPrompt },
          {
            type: spec.mimeType === "application/pdf" ? "document" : "image",
            source: {
              type: "data",
              value: base64,
              mimeType: spec.mimeType,
            },
            metadata: { filename: spec.filename, size },
          },
        ],
      };
    }

Add that message to the selected agent and run the agent. Keep the MIME type authoritative: use an `image` part for images and a `document` part for PDFs and other documents. The chosen model and backend converter must support each MIME type you accept.

## Next stepsCopy Anchor Link

  * [CopilotChat attachments input](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)
  * [Voice](https://docs.copilotkit.ai/angular/voice)
  * [Chat UI configuration](https://docs.copilotkit.ai/angular/prebuilt-components)



How is this guide?

GoodBad

[Previous PageHeadless UI](https://docs.copilotkit.ai/angular/custom-look-and-feel/headless-ui)[Next PageVoice](https://docs.copilotkit.ai/angular/voice)
