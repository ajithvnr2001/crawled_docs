---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-6-flash/
title: Gemini 3.6 Flash \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:57:34.488844+00:00
---

# Gemini 3.6 Flash  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-6-flash/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini 3.6 Flash Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Gemini 3.6 Flash will be retired on November 19, 2026. Upgrade to [Gemini 3.8 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash) to avoid service disruptions.

Gemini 3.6 Flash is optimized for multi-step orchestration, full-stack code refactoring, and general reasoning. It improves on many key areas critical to the Flash line of models.

Improvements from previous Flash models include:

  * **Improved token efficiency** over Gemini 3.5 Flash. 3.6 Flash uses less tokens and completes multi-step workflows in fewer turns.
  * **Improved code generation** with lower compile-failure and revision rates across building, prototyping, and IDE agent environments.
  * **Reduces action bias** by resolving read-only diagnostic tasks without making unsolicited edits.
  * **Improved multimodal reasoning** with respect to chart interpretation, visual blueprint conversion, and multi-element web layout generation.



Flash includes the following potentially breaking changes when compared to previous Gemini models:

  * **Custom values for parameters like temperature, top-K, and top-P aren't supported.** If you set a custom value for these parameters, that value will be ignored.
  * **Custom values for frequency and presence penalty parameters aren't supported.** Setting a custom value for these parameters will throw an error.
  * API requests where the last input turn has a role of `Model` aren't supported. The following kinds of requests will return an error: 
    * When using the Interactions API: Requests where the last object in the `input` array has `"type": "model_output"`.
    * When using the GenerateContent API: Requests where the last object in the `contents` array has `"role": "model"`.



[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/chat?model=gemini-3.6-flash) [Deploy example app](https://console.cloud.google.com/agent-platform/studio/chat?suggestedPrompt=How%20does%20AI%20work&deploy=true&model=gemini-3.6-flash) [Developer guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-3-6-flash) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Note: "Deploy example app" requires a Google Cloud project with billing and Agent Platform API enabled.Model ID | `gemini-3.6-flash`  
---|---  
Modalities |  description  Text   
Input and output  photo  Image   
Input only  mic  Audio   
Input only  videocam  Video   
Input only   
Token limits | Context window | 1,048,576  
Maximum output tokens | 65,536  
Capabilities | 

  * [Thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)   
Supported
  * [System instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instruction-introduction)   
Supported
  * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output)   
Supported
  * [Context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)   
Implicit context caching, explicit context caching  
Supported
  * [RAG Engine ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview)   
Supported
  * [Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning)   
Not supported
  * [Agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing)   
Supported

  
Tools | 

  * [Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview)   
Google Search, Google Maps, Parallel Web Search, Exa Web Search  
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
Standard PayGo with Usage Tiers, Flex PayGo, Priority PayGo  
Supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Not supported

  
Input size limit | 

  * GenerateContent API: 500 MiB compressed
  * Interactions API: 256 MiB compressed (synchronous or streaming); 9.75 MiB uncompressed (deferred, when background and store are true)

  
Interactions API URI limit |  Up to 100 distinct Cloud Storage (`gs://`) URIs per request across all modalities on the [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions), including URIs carried forward from earlier turns using `previous_interaction_id`. `generateContent` supports `gs://` URIs up to the per-modality model item limits (up to 6,500 combined multimodal files when including plain-text files).   
Technical specifications |  **Image** photo | 

  * Maximum images per prompt: 3,000 (images and PDFs combined)
  * Maximum inline part size (GenerateContent API): 256 MB
  * Maximum file size per file from Cloud Storage: 2 GiB minus 500 KiB
  * Maximum file size per file from public HTTP or HTTPS URLs: 15 MiB
  * Maximum file size per file for direct local uploads in the console: 7 MiB inline (up to 50 MiB staged to Cloud Storage)
  * Maximum file size per file for Google Drive imports in the console: 7 MB (10 MB total)
  * Default resolution tokens: 1,120
  * Supported MIME types: `image/png`, `image/jpeg`, `image/webp`, `image/heic`, `image/heif`

  
**Text** description | 

  * Maximum number of files per prompt: 3,000 PDFs (shared with images; up to 6,500 total files when including plain text)
  * Maximum number of pages per file: 3,000
  * Maximum inline part size (GenerateContent API): 256 MB
  * Maximum file size per file from Cloud Storage: 2 GiB minus 500 KiB
  * Maximum file size per file from public HTTP or HTTPS URLs: 15 MiB
  * Maximum file size per file for direct local uploads in the console: 7 MiB inline (up to 50 MiB staged to Cloud Storage)
  * Maximum file size per file for Google Drive imports in the console: 7 MB (10 MB total)
  * Default resolution tokens: 560
  * OCR for scanned PDFs: Not used by default
  * Supported MIME types: `application/pdf`, `text/plain`

  
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

  * Temperature: 1.0
  * topP: 0.95
  * topK: 64
  * Frequency penalty: 0
  * Presence penalty: 0

  
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

  
Versions | 

  * `gemini-3.6-flash`
    * Launch stage: GA
    * Release date: July 21, 2026
    * Retirement date†: November 19, 2026

  
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
  
† Listed retirement dates refer to retirement of support in Gemini Enterprise Agent Platform. Models may remain accessible through the Gemini API after these dates have passed. The Gemini API is not a Google Cloud offering and is subject to its own terms of service. For details, see the [Gemini API documentation](https://ai.google.dev/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
