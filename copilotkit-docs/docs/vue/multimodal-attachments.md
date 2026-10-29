---
url: https://docs.copilotkit.ai/vue/multimodal-attachments/
title: Multimodal Attachments
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:27.544719+00:00
---

# Multimodal Attachments

> Source: https://docs.copilotkit.ai/vue/multimodal-attachments/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/vue/frontend-tools)

Generative UI

Controlled

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/vue/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/vue/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/vue/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/vue/learning)

[User Memories](https://docs.copilotkit.ai/vue/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/vue/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/vue/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/vue/intelligence/analytics)[Channels](https://docs.copilotkit.ai/vue/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

# Multimodal Attachments

Let users send images, audio, video, and documents from a Vue chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

You can enable file attachments on `CopilotChat` without replacing the Vue composer. CopilotKit validates each file in the browser, shows previews, and adds ready attachments to the next agent message.

## Quick start#

App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <CopilotChat :attachments="{ enabled: true }" />
      </CopilotKitProvider>
    </template>

Users can choose files with the attachment button, drag them onto the chat, or paste supported file items from the clipboard.

## Configuration#

The `attachments` prop accepts an `AttachmentsConfig` object:
    
    
    <CopilotChat
      :attachments="{
        enabled: true,
        accept: 'image/*,audio/*,video/*,application/pdf',
        maxSize: 10 * 1024 * 1024,
      }"
    />

Option| Type| Default| Description  
---|---|---|---  
`enabled`| `boolean`| —| Enable file attachments in the composer.  
`accept`| `string`| `"*/*"`| MIME filter, including patterns such as `image/*` and extensions such as `.pdf`.  
`maxSize`| `number`| `20 * 1024 * 1024`| Maximum file size in bytes.  
`onUpload`| `(file: File) => AttachmentUploadResult | Promise<AttachmentUploadResult>`| —| Upload the file yourself and return a data or URL source.  
`onUploadFailed`| `(error: AttachmentUploadError) => void`| —| Handle validation and upload failures.  
  
`accept` and `maxSize` are client-side checks, not server-side security controls. Validate files again wherever your application stores or processes them.

## Supported file types#

CopilotKit maps MIME types to four attachment modalities:

Modality| MIME types| Default preview  
---|---|---  
Image| `image/*`| Thumbnail and lightbox.  
Audio| `audio/*`| Audio player.  
Video| `video/*`| Thumbnail, play button, and lightbox.  
Document| Other types| File name/icon; PDF and text can be previewed.  
  
The selected model and backend converter still need to support the content. A model that cannot consume a modality can report a run error after the message has been sent; bind `:on-error` on `CopilotChat` for that path.

## Custom upload handler#

By default, Vue reads each file as base64 data and sends it inline. Return a hosted URL instead when your application stores uploads separately:
    
    
    <script setup lang="ts">
    async function upload(file: File) {
      const form = new FormData();
      form.append('file', file);
      const response = await fetch('/api/upload', { method: 'POST', body: form });
      const { url } = await response.json();
      return { type: 'url' as const, value: url, mimeType: file.type };
    }
    </script>
    
    <template>
      <CopilotChat :attachments="{ enabled: true, onUpload: upload }" />
    </template>

The other supported result is `{ type: "data", value, mimeType }`. Either variant can include a `metadata` object; the filename is added to attachment metadata automatically.

## Handling upload errors#
    
    
    <script setup lang="ts">
    function onUploadFailed(error: {
      reason: 'file-too-large' | 'invalid-type' | 'upload-failed';
      file: File;
      message: string;
    }) {
      toast.error(error.message);
    }
    </script>
    
    <template>
      <CopilotChat
        :attachments="{
          enabled: true,
          accept: 'image/*',
          maxSize: 5 * 1024 * 1024,
          onUploadFailed,
        }"
      />
    </template>

Validation failures use `invalid-type` or `file-too-large`; an upload handler or the default reader failing uses `upload-failed`. Errors after sending are reported through the chat `:on-error` callback instead.

## How it works#

When the user sends a message, Vue:

  1. Reads each file with the default reader or calls `onUpload`.
  2. Builds typed AG-UI content parts alongside the text part.
  3. Consumes the ready attachment queue and sends those parts with the user message.



Attachment sources use the standard AG-UI input-content shape, so the runtime and agent must support the modalities you accept.

### On this page

Quick startConfigurationSupported file typesCustom upload handlerHandling upload errorsHow it works
