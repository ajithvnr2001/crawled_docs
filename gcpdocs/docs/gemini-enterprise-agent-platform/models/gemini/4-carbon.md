---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-carbon/
title: Gemini 4 Carbon \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:56:04.640143+00:00
---

# Gemini 4 Carbon  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-carbon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini 4 Carbon Stay organized with collections  Save and categorize content based on your preferences. 

Gemini 4 Carbon is Google's frontier model that excels at deep work in complex, real-world tasks across domains including coding, finance, legal, cybersecurity, and science. Gemini 4 Carbon is a Google Frontier Model subject to Section 34 of the [Service Specific Terms](https://cloud.google.com/terms/service-terms) (for details, see [Abuse monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/abuse-monitoring#google-frontier-models)).

4 Carbon differs from earlier Gemini models in the following ways:

  * **Unified input and output token limit and long decodes** : 4 Carbon has a unified 1,048,576-token limit that includes both input and output tokens (where output includes thinking, function calls, and the final response) across all supported API surfaces (the [`GenerateContent` API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference), the [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions), and the [OpenAI compatibility Chat Completions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/openai)). A single foreground segment generates up to 65,536 output tokens when streaming (or 32,768 tokens when non-streaming). On both the [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions) and the [`GenerateContent` API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference) (`v1beta1`), you can extend output up to 1,048,576 tokens (minus your input tokens) using long decodes: the Google Gen AI SDK and Agent Studio handle `continuation_token` automatically across segments, or you can use `background=true` on the Interactions API or pass `continuation_token` in a custom continuation loop (known issue: `continuation_token` is supported only in the `v1beta1` API, which the Google Gen AI SDK uses by default). For details, see the [developer's guide to Gemini 4 Carbon](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-carbon#long-decodes).
  * **Thinking levels** : 4 Carbon supports [thinking levels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking) `LOW`, `MEDIUM` (default on `gemini-4-carbon`), and `HIGH` (default on `gemini-4-carbon-cyber-permissive`). Setting `thinking_budget` or `thinking_level="MINIMAL"` returns an HTTP `400` validation error.
  * **Sampling parameters** : Custom values for [sampling parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/content-generation-parameters) (`temperature`, `top_p`, and `top_k`) are ignored.
  * **Context caching** : 4 Carbon supports [implicit caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview) only (4,096-token minimum), with durable caching enabled by default. Explicit context caching isn't supported.
  * **Office and OpenDocument file inputs** : In addition to PDF (`application/pdf`) and plain text (`text/plain`), 4 Carbon accepts Microsoft Office (`.docx`, `.dotx`, `.doc`, `.pptx`, `.ppt`, `.xlsx`, `.xls`) and OpenDocument (`.odt`, `.odp`, `.ods`) files inline or from Cloud Storage on both the [`GenerateContent` API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference) and the [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions).



[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/chat?model=gemini-4-carbon) [Deploy example app](https://console.cloud.google.com/agent-platform/studio/chat?suggestedPrompt=How%20does%20AI%20work&deploy=true&model=gemini-4-carbon) [Developer guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-carbon) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Note: "Deploy example app" requires a Google Cloud project with billing and Agent Platform API enabled.Model ID | `gemini-4-carbon`  
---|---  
Modalities |  description  Text   
Input and output  photo  Image   
Input only  mic  Audio   
Input only  videocam  Video   
Input only   
Token limits | Context window | 1,048,576  
Maximum output tokens | 1,048,576  
Capabilities | 

  * [Thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)   
Supported
  * [System instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instruction-introduction)   
Supported
  * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output)   
Supported
  * [Context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)   
Implicit context caching  
Supported
  * [RAG Engine ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview)   
Not supported
  * [Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning)   
Not supported
  * [Agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing)   
Supported

  
Tools | 

  * [Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview)   
Google Search, Google Maps, Agent Search, Parallel Web Search, Exa Web Search, Web Grounding for Enterprise  
Supported
  * [Code execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/code-execution)   
Supported
  * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling)   
Supported
  * [URL context](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/url-context)   
Supported
  * [Computer use](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/computer-use)   
Supported

  
APIs | 

  * [GenerateContent API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference)   
Supported
  * [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions)   
Supported
  * [Gemini Live API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api)   
Not supported
  * [Count Tokens API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/get-token-count)   
Supported
  * [Chat Completions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/overview)   
Supported

  
Consumption options | 

  * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)   
Supported
  * [Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference)   
Supported
  * [Pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)   
Standard PayGo, Priority PayGo  
Supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Not supported

  
Input size limit | 

  * GenerateContent API: 500 MiB compressed
  * Interactions API: 256 MiB compressed (synchronous or streaming); 9.75 MiB uncompressed (deferred, when background and store are true)

  
Interactions API URI limit |  Up to 100 distinct Cloud Storage (`gs://`) URIs per request across all modalities on the [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions), including URIs carried forward from earlier turns using `previous_interaction_id`. `generateContent` supports `gs://` URIs up to the per-modality model item limits (up to 6,500 combined multimodal files when including plain-text files).   
Technical specifications |  **Image** photo | 

  * Maximum images per prompt: 3,000 (images and documents combined)
  * Maximum inline part size (GenerateContent API): 256 MB
  * Maximum file size per file from Cloud Storage: 2 GiB minus 500 KiB
  * Maximum file size per file from public HTTP or HTTPS URLs: 15 MiB
  * Maximum file size per file for direct local uploads in the console: 7 MiB inline (up to 50 MiB staged to Cloud Storage)
  * Maximum file size per file for Google Drive imports in the console: 7 MB (10 MB total)
  * Default resolution tokens: 1,120
  * Supported MIME types: `image/png`, `image/jpeg`, `image/webp`, `image/heic`, `image/heif`

  
**Text** description | 

  * Maximum number of files per prompt: 3,000 documents (shared with images; up to 6,500 total files when including plain text)
  * Maximum number of pages per file: 3,000
  * Maximum inline part size (GenerateContent API): 256 MB
  * Maximum file size per file from Cloud Storage: 2 GiB minus 500 KiB
  * Maximum file size per file from public HTTP or HTTPS URLs: 15 MiB
  * Maximum file size per file for direct local uploads in the console: 7 MiB inline (up to 50 MiB staged to Cloud Storage)
  * Maximum file size per file for Google Drive imports in the console: 7 MB (10 MB total)
  * Default resolution tokens: 560
  * OCR for scanned PDFs: Not used by default
  * Supported MIME types: `application/pdf`, `text/plain`, `application/msword`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `application/vnd.openxmlformats-officedocument.wordprocessingml.template`, `application/vnd.oasis.opendocument.text`, `application/vnd.ms-powerpoint`, `application/vnd.openxmlformats-officedocument.presentationml.presentation`, `application/vnd.oasis.opendocument.presentation`, `application/vnd.ms-excel`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, `application/vnd.oasis.opendocument.spreadsheet`

  
**Video** videocam | 

  * Maximum video length (with audio): Approximately 45 minutes
  * Maximum video length (without audio): Approximately 1 hour
  * Maximum number of videos per prompt: 10
  * Maximum inline part size (GenerateContent API): 256 MB
  * Maximum file size per file from Cloud Storage: 2 GiB minus 500 KiB
  * Maximum file size per file from public HTTP or HTTPS URLs: 15 MiB
  * Default resolution tokens per frame: 70
  * Supported MIME types: `video/x-flv`, `video/quicktime`, `video/mpeg`, `video/mpegs`, `video/mpg`, `video/mp4`, `video/webm`, `video/wmv`, `video/3gpp`

  
**Audio** mic | 

  * Maximum audio length per prompt: Approximately 8.4 hours, or up to 1 million tokens
  * Maximum number of audio files per prompt: 1,000
  * Maximum inline part size (GenerateContent API): 256 MB
  * Maximum file size per file from Cloud Storage: 2 GiB minus 500 KiB
  * Maximum file size per file from public HTTP or HTTPS URLs: 15 MiB
  * Speech understanding for: Audio summarization, transcription, and translation
  * Supported MIME types: `audio/x-aac`, `audio/flac`, `audio/mp3`, `audio/m4a`, `audio/mpeg`, `audio/mpga`, `audio/mp4`, `audio/ogg`, `audio/pcm`, `audio/wav`, `audio/webm`

  
**Parameter defaults** tune | 

  * Temperature: 1.0 (fixed; custom values ignored)
  * topP: 0.95 (fixed; custom values ignored)
  * topK: 64 (fixed; custom values ignored)
  * candidateCount: 1 (fixed)

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`

  
**[ML processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency) ** | 

  * Multi-region: `us`, `eu`

  
**[Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/supported-models) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`

  
**[Standard PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`

  
**[Priority PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/priority-paygo) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`

  
Knowledge cutoff date |  March 2026   
Versions | 

  * `gemini-4-carbon`
    * Launch stage: GA
    * Release date: November 10, 2026

  
Security controls | **Online prediction** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
**Batch inference** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
**Context caching** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
See [Security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) for more information.  
  
## Gemini 4 Carbon for cyber

Gemini 4 Carbon for cyber is a version of Gemini 4 Carbon for defensive cybersecurity use cases, such as vulnerability discovery, reverse engineering, exploit verification, and patch generation. Gemini 4 Carbon for cyber is a Google Frontier Cyber Model subject to Section 31 of the [Service Specific Terms](https://cloud.google.com/terms/service-terms) (for details, see [Abuse monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/abuse-monitoring#google-frontier-models)).

Gemini 4 Carbon for cyber is generally available on Gemini Enterprise Agent Platform behind an allowlist. To request access, contact your Google team or apply through the [Fairwind Program](https://deepmind.google/fairwind-program/). Access to earlier Gemini Cyber models (such as Gemini 4 Argon Cyber Permissive or Gemini 3.8 Flash Cyber) doesn't carry over; you must apply separately.

The following table shows how Gemini 4 Carbon for cyber differs from Gemini 4 Carbon:

| 4 Carbon | 4 Carbon for cyber  
---|---|---  
Model ID | `gemini-4-carbon` | `gemini-4-carbon-cyber-permissive`  
Access | Publicly available | Allowlist only ([Fairwind Program](https://deepmind.google/fairwind-program/))  
Default thinking level | `MEDIUM` (supports `LOW`, `MEDIUM`, `HIGH`) | `HIGH` (supports `LOW`, `MEDIUM`, `HIGH`)  
Computer use | Supported | Not supported  
Supported regions | `global`, `us`, `eu` | `global`, `us`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
