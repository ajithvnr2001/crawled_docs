---
url: https://docs.copilotkit.ai/angular/voice/
title: Voice
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.849839+00:00
---

# Voice

> Source: https://docs.copilotkit.ai/angular/voice/

Chat

# Voice

Add speech transcription to an Angular chat through Copilot Runtime.

Copy MarkdownOpen

`CopilotChat` includes a microphone control. Voice input is transcribed through Copilot Runtime and inserted into the composer as text.

## Accept voice inputCopy Anchor Link

No component option is required to display the microphone. The browser asks for microphone permission, records the audio, and sends it to the Runtime transcription endpoint. The resulting text remains editable before the user sends it.

Serve production applications over HTTPS so browsers can grant microphone access.

### Configure Runtime transcriptionCopy Anchor Link

Follow the [Voice backend setup](https://docs.copilotkit.ai/voice#backend) to add a dedicated Runtime route and transcription service. Keep speech-provider credentials separate from credentials used for agent chat. For the Built-in Agent showcase, set:

Copy Text
    
    
    OPENAI_TRANSCRIPTION_API_KEY=your-api-key
    # Optional: defaults to https://api.openai.com/v1
    OPENAI_TRANSCRIPTION_BASE_URL=https://your-speech-provider.example.com/v1

The route must omit `transcriptionService` when the dedicated credential is absent. Copilot Runtime then reports `audioFileTranscriptionEnabled: false` on `/info`, and the chat hides the mic instead of exposing a control that cannot work. When the service is configured, the browser sends recorded audio to `{runtimeUrl}/transcribe`. Point `runtimeUrl` in `provideCopilotKit` at the runtime route that has the transcription service.

Voice requests can call the same backend tools as typed requests. Register renderers only for the exact tool names your backend exposes. Call `registerRenderToolCall` from an Angular injection context:

Copy Text
    
    
    registerRenderToolCall({
      name: "getWeather",
      args: z.object({ city: z.string() }),
      component: WeatherCardComponent,
    });

`WeatherCardComponent` is the renderer from [Render a tool result](https://docs.copilotkit.ai/angular/generative-ui/tool-rendering#render-a-tool-result).

The renderer registration is optional. It changes how matching tool calls are displayed, not how speech is captured or transcribed.

Open the chat. When the runtime has a transcription service, the mic button shows in the composer. Record a sentence, and the text appears in the input for you to edit and send.

## Next stepsCopy Anchor Link

  * [Multimodal Attachments](https://docs.copilotkit.ai/angular/multimodal-attachments)
  * [Chat UI configuration](https://docs.copilotkit.ai/angular/prebuilt-components)



How is this guide?

GoodBad

[Previous PageMultimodal Attachments](https://docs.copilotkit.ai/angular/multimodal-attachments)[Next PageThreads Drawer](https://docs.copilotkit.ai/angular/prebuilt-components/copilot-threads-drawer)
