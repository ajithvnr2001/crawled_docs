---
url: https://docs.copilotkit.ai/vue/voice/
title: Voice
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:30.223509+00:00
---

# Voice

> Source: https://docs.copilotkit.ai/vue/voice/

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

# Voice

Add runtime-backed speech-to-text to a Vue chat composer.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

You can add voice input to `CopilotChat` without wiring a separate microphone button. The component renders its transcription controls only when the runtime advertises `audioFileTranscriptionEnabled` and the browser supports `MediaRecorder`.

## When to use this#

  * Use voice input for hands-free, accessibility, mobile, kiosk, and long-form prompts.
  * Use [multimodal attachments](https://docs.copilotkit.ai/vue/multimodal-attachments) when the user is sending an audio file rather than speaking live.



## Frontend setup#

App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <CopilotChat />
      </CopilotKitProvider>
    </template>

When the user starts recording, the browser requests microphone permission. After recording finishes, the Vue component sends the audio to the runtime, places the returned transcript into the composer, and leaves it editable. The user submits it like any other message; Vue does not auto-send the transcript. Serve production pages over HTTPS so browsers can grant microphone access.

The default REST transport posts multipart form data to `{runtimeUrl}/transcribe` with an `audio` field. With `use-single-endpoint`, the Vue client sends a JSON envelope to `runtimeUrl` containing base64 audio, `mimeType`, and `filename`.

Set the provider prop when your runtime exposes one single endpoint:
    
    
    <CopilotKitProvider
      runtime-url="/api/copilotkit"
      :use-single-endpoint="true"
    >
      <CopilotChat />
    </CopilotKitProvider>

## Custom audio handling#

Pass `on-finish-transcribe-with-audio` when your application wants to receive the recorded `Blob` and handle transcription itself. This callback replaces the default runtime request, so it must put any resulting text into your own UI:
    
    
    <script setup lang="ts">
    async function handleAudio(audio: Blob) {
      const transcript = await myTranscriptionService(audio);
      console.log(transcript);
    }
    </script>
    
    <template>
      <CopilotChat :on-finish-transcribe-with-audio="handleAudio" />
    </template>

The Vue package does not expose the React demo's `onTranscribed` canned-audio callback or a runnable voice Showcase route. For deterministic demos and tests, call your own handler with a recorded `Blob` instead of documenting a non-existent Vue prop.

## Configure the runtime#

The mic appears only when the runtime has a `TranscriptionService`. Configure that service in your V2 runtime and mount the normal runtime handler. The service implements:
    
    
    import {
      CopilotRuntime,
      TranscriptionService,
    } from "@copilotkit/runtime/v2";
    
    class MyTranscriptionService extends TranscriptionService {
      async transcribeFile({ audioFile }: { audioFile: File }): Promise<string> {
        return transcribeWithYourProvider(audioFile);
      }
    }
    
    const runtime = new CopilotRuntime({
      agents,
      transcriptionService: new MyTranscriptionService(),
    });

With the service configured, `GET /info` reports `audioFileTranscriptionEnabled: true` and `POST /transcribe` dispatches to `transcribeFile`. Without it, the runtime cannot produce a transcript even if the browser has a microphone.

See [Runtime HTTP endpoints](https://docs.copilotkit.ai/backend/runtime-endpoints) for route mounting, request shapes, and server-side error handling. The V2 runtime maps service errors to transcription error codes such as `rate_limited`, `auth_failed`, `audio_too_long`, and `provider_error`; the Vue composer presents a retryable or actionable message and clears it after a short delay.

### On this page

When to use thisFrontend setupCustom audio handlingConfigure the runtime
