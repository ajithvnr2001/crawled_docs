---
url: https://docs.sarvam.ai/api/developer-tools/mcp/
title: MCP Server | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T06:34:15.374729+00:00
---

# MCP Server | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/developer-tools/mcp/

Skip to navigation

On this page

  * Sarvam API MCP server
  * Quickstart
  * 1\. Get your API key
  * 2\. Add to your MCP client
  * 3\. Alternative: credentials file
  * Verify your install
  * Tools
  * Speech-to-text
  * Text-to-speech
  * Text and language
  * Document AI
  * Document translation and dubbing
  * Pronunciation dictionaries
  * Multi-step workflows
  * Builder tools
  * Configuration
  * Two namespaces
  * Related pages



Scroll to top

[Developer Tools](https://docs.sarvam.ai/api/developer-tools/mcp)

# MCP Server

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/developer-tools/mcp.md "View this page as plain text")|More actions

This page is for Model APIs.

## Sarvam API MCP server

Official Sarvam [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server. Exposes every public Sarvam API — STT (batch and realtime), TTS, text translation, transliteration, Language ID, LLM (105B and 105B Conversations), Document AI (parse, extract, classify, split), Document Translation, Dubbing, and Pronunciation Dictionaries — as first-class MCP tools so any MCP-aware client (Claude Desktop, Claude Code, Cursor, Windsurf, Zed) can call Sarvam with zero boilerplate.

For whole-file translation (PDF, Office, HTML), see the [Document Translation API](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/overview) in the docs — the MCP server’s `sarvam_tools_translate` tool covers **text** translation only, while `sarvam_tools_document_translate` handles documents.

Cross-platform Python package: macOS, Windows, and Linux (Python 3.11+).

### Quickstart

#### 1\. Get your API key

Sign up or log in at [indus.sarvam.ai/key-management](https://indus.sarvam.ai/key-management?ref=docs) and copy your API key.

#### 2\. Add to your MCP client

Paste this JSON into your favorite agent (Cursor, Claude Desktop, Windsurf, etc.) and it’ll set up Sarvam for you:
    
    
    {
    
      "mcpServers": {
    
        "sarvam": {
    
          "command": "uvx",
    
          "args": ["sarvam-mcp"],
    
          "env": {
    
            "SARVAM_API_KEY": "<YOUR_SARVAM_API_KEY>"
    
          }
    
        }
    
      }
    
    }

Replace `<YOUR_SARVAM_API_KEY>` with your actual API key.

If you installed with `pip install sarvam-mcp` instead, drop the `args` array and use the console script directly:
    
    
    {
    
      "mcpServers": {
    
        "sarvam": {
    
          "command": "sarvam-mcp",
    
          "env": {
    
            "SARVAM_API_KEY": "<YOUR_SARVAM_API_KEY>"
    
          }
    
        }
    
      }
    
    }

#### 3\. Alternative: credentials file

Instead of setting `SARVAM_API_KEY` in the JSON config, you can store it in `~/.sarvam/credentials`:
    
    
    api_key = <YOUR_SARVAM_API_KEY>

The server checks the `SARVAM_API_KEY` env var first, then falls back to `~/.sarvam/credentials`.

### Verify your install

Ask your assistant something that exercises a Sarvam tool, for example:

> “Translate ‘good morning’ to Hindi using sarvam.”

### Tools

All defaults below reflect the latest non-deprecated models. Tools are registered under their namespace prefix, so the name your client sees is exactly what’s in the tables below.

#### Speech-to-text

Tool| What it does| Default model  
---|---|---  
`sarvam_tools_stt_transcribe`| Audio file → transcript. Five modes: `transcribe`, `translate` (any Indic language → English), `verbatim`, `translit`, `codemix`| `saaras:v4`  
`sarvam_tools_stt_realtime`| Mono 16-bit WAV (8000 or 16000 Hz) → realtime transcript over the WebSocket| `saaras:v3-realtime`  
`sarvam_tools_stt_batch_submit`| Long audio (> 30 s) → batch job; creates the job and uploads the audio for you| —  
`sarvam_tools_stt_batch_status`| Poll a batch job, returns the transcript when completed| —  
`sarvam_tools_stt_batch_download`| Fresh presigned download URLs for a finished batch job| —  
  
See [Batch Speech-to-Text](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/apis/batch) for the underlying job pipeline.

#### Text-to-speech

Tool| What it does| Default model  
---|---|---  
`sarvam_tools_tts_speak`| Text → audio file, written under `SARVAM_MCP_BASE_PATH`| `bulbul:v3` (default) or `bulbul:v4-flash`  
`sarvam_tools_tts_stream`| Text → streamed audio over the TTS WebSocket| `bulbul:v3` (default) or `bulbul:v4-flash`  
  
Speakers are model-specific: `bulbul:v3` uses short names (`shubh` is the default), while `bulbul:v4-flash` uses persona IDs of the form `<voice>_<lang>_<style>` (default `shubh_enhi_ads`). See [Voices](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/voices) for both catalogs.

#### Text and language

Tool| What it does| Default model  
---|---|---  
`sarvam_tools_translate`| Cross-language text translation| `mayura:v1` (11 languages, formal/colloquial/code-mixed) or `sarvam-translate:v1` (22 scheduled languages + English, formal only)  
`sarvam_tools_transliterate`| Script conversion without translating meaning| —  
`sarvam_tools_identify_language`| Detect language (BCP-47) and script| —  
`sarvam_tools_llm_complete`| Chat completions, OpenAI-compatible message format incl. function calling and structured output| `sarvam-105b` (128K context) or `sarvam-105b-conversations` (32K, post-trained for dialogue)  
  
#### Document AI

Tool| What it does| Default model  
---|---|---  
`sarvam_tools_vision_parse`| Full-document OCR that keeps layout, reading order and tables → markdown (`md`), HTML, or JSON. Pass `md`, not `markdown`| Sarvam Vision  
`sarvam_tools_vision_extract`| Schema extraction — pass a JSON schema, get structured values back| Sarvam Vision  
`sarvam_tools_vision_classify`| Label the whole document, or each page with `scope='page'`, against your categories| Sarvam Vision  
`sarvam_tools_vision_split`| Split a bundle of pages into separate child documents (`semantic`, `fixed_pages`, `page_ranges`, or `triggers`)| Sarvam Vision  
`sarvam_tools_vision_job_status`| Poll any Document AI job — parse, extract, classify or split| —  
  
`parse` replaces the old `digitise` job, which was renamed upstream. See [Document Intelligence](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview) for job shapes.

**Page limits:** 30 pages per PDF for `parse`, 20 for `extract`, and 500 for `split` and `classify`. Split and Classify also accept up to 10 documents per request, 20 categories and 1,000 segments. Full table in [Languages, Formats & Limits](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/languages-formats-limits).

#### Document translation and dubbing

Tool| What it does| Default model  
---|---|---  
`sarvam_tools_document_translate`| Whole document (PDF, Word, Excel, PowerPoint, HTML) with layout preserved, up to 12 target languages| —  
`sarvam_tools_document_translate_status`| Poll a document translation job; set `export=true` once a language is completed to get download links| —  
`sarvam_tools_dubbing_submit`| Start an official dubbing job for a video or audio file — creates the job, uploads the media, starts processing| —  
`sarvam_tools_dubbing_status`| Poll a dubbing job, or fetch signed export URLs (video, audio, mp3, srt) that last about 24 hours| —  
  
See [Dubbing API](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/apis/overview) for pipeline and export formats.

#### Pronunciation dictionaries

Tool| What it does| Default model  
---|---|---  
`sarvam_tools_pronunciation_list`| List pronunciation dictionary IDs you own| —  
`sarvam_tools_pronunciation_get`| Get a dictionary’s word → pronunciation entries| —  
`sarvam_tools_pronunciation_create`| Create a dictionary to control how specific words are spoken in TTS| —  
`sarvam_tools_pronunciation_delete`| Delete a dictionary by ID| —  
  
#### Multi-step workflows

Tool| What it does| Default model  
---|---|---  
`sarvam_tools_voice`| Voice agent loop: transcribe an Indic audio file → LLM reply → synthesize the reply| —  
`sarvam_tools_dub`| Dub a short Indic audio clip into another Indic language (STT → translate → TTS)| —  
`sarvam_tools_localize`| Translate a JSON or `key=value` string-table file, walking every string value (nested JSON supported)| —  
`sarvam_tools_recall`| Answer a natural-language question grounded in a set of files — audio is transcribed, text and markdown read directly| —  
  
`sarvam_tools_text_analytics` is still registered for compatibility but raises immediately: Sarvam retired the `/text-analytics` endpoint, so there is no network call to make. For document and text extraction, use the Document AI tools above.

#### Builder tools

Builder tools help your assistant write code that uses Sarvam. They don’t call the API.

Tool| What it does  
---|---  
`sarvam_code_api_reference`| Authoritative request/response shape for an endpoint — parameters, defaults, errors  
`sarvam_code_languages`| Supported BCP-47 language codes for a given API (coverage varies by endpoint)  
`sarvam_code_speakers`| TTS speakers compatible with a model tag, e.g. `bulbul:v4-flash`  
`sarvam_code_pricing`| Current pricing and billing unit for a model  
`sarvam_code_snippet`| Tested, copy-paste-ready code snippet for calling a Sarvam API  
`sarvam_code_recommend_model`| Recommend the right model and mode from a plain-English description of what you’re building  
`sarvam_code_validate_request`| Validate a draft request body against the canonical schema before you send it  
  
### Configuration

Env var| Default| Description  
---|---|---  
`SARVAM_API_KEY`| —| **Required.** API key from [indus.sarvam.ai](https://indus.sarvam.ai/key-management?ref=docs). Falls back to `~/.sarvam/credentials`.  
`SARVAM_API_BASE_URL`| `https://api.sarvam.ai`| Override for testing/staging.  
`SARVAM_MCP_BASE_PATH`| `~/Desktop`| Where audio/document files land.  
`SARVAM_AUDIO_OUTPUT_MODE`| `files`| `files`, `resources`, or `both` — whether audio comes back as a file path, an MCP resource, or both.  
  
### Two namespaces

The server exposes tools across two namespaces:

  * `sarvam_tools_*`, runtime tools. Call Sarvam APIs to do things (transcribe, speak, translate, parse a document, etc.).
  * `sarvam_code_*`, builder tools. Help you write code that uses Sarvam: docs, endpoint shapes, language lists, code snippets, starter projects.



## Related pages

  * [Context7](https://docs.sarvam.ai/api/developer-tools/context7)
  * [llms.txt & Markdown docs](https://docs.sarvam.ai/api/developer-tools/llms-txt)
  * [Agent Skills](https://docs.sarvam.ai/api/developer-tools/agent-skills)
  * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
  * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)



Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/integration/pipecat-production-guide)[Markdown & llms.txtNext](https://docs.sarvam.ai/api/developer-tools/llms-txt)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

  * Getting Started

    * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
    * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
    * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
    * [Pricing, Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/pricing)
    * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
  * [Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)
    * [Models](https://docs.sarvam.ai/api/token-factory/models)

    * [Chat Completions](https://docs.sarvam.ai/api/token-factory/chat-completions)
    * [Responses API](https://docs.sarvam.ai/api/token-factory/responses-api)
    * How-to

    * Migration Guides

  * Sarvam Models

    * Models

    * Speech to Text

    * Text to Speech

    * Text Processing

    * Document Intelligence

    * Document Translation

    * Dubbing

    * Instant Voice CloningBeta

    * Self-Hosted Deployments

  *     * Integration

    * Developer Tools
      * [MCP Server](https://docs.sarvam.ai/api/developer-tools/mcp)
      * [Markdown & llms.txt](https://docs.sarvam.ai/api/developer-tools/llms-txt)
      * [Context7](https://docs.sarvam.ai/api/developer-tools/context7)
      * [Agent Skills](https://docs.sarvam.ai/api/developer-tools/agent-skills)

  * Cookbook

    * Guides

    * Example Voice Agents

  *     * Migrations

  * Resources

    * [Building for Indian Languages](https://docs.sarvam.ai/api/getting-started/building-for-india)
    * [All Models](https://docs.sarvam.ai/api/getting-started/models)
    * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)
    * [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing)
    * Account & Billing




  * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
  * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
  * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
  * [Pricing, Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/pricing)
  * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
  * [Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)
  * [Models](https://docs.sarvam.ai/api/token-factory/models)
  * [Sarvam 105B](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)
  * [GLM-5.3](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)
  * [GLM-5.3 Flash](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)
  * [Gemma 4 31B](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)
  * [DeepSeek V4.1 Flash 1017](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017)
  * [DeepSeek V4 Pro](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro)
  * [Kimi K3](https://docs.sarvam.ai/api/token-factory/models/kimi-k3)
  * [MiMo V2.6 Flash](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)
  * [MiMo V2.6 Pro](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro)
  * [Chat Completions](https://docs.sarvam.ai/api/token-factory/chat-completions)
  * [Responses API](https://docs.sarvam.ai/api/token-factory/responses-api)
  * [List your chat messages](https://docs.sarvam.ai/api/token-factory/how-to/list-your-chat-messages)
  * [Control response randomness](https://docs.sarvam.ai/api/token-factory/how-to/control-response-randomness)
  * [Control response diversity](https://docs.sarvam.ai/api/token-factory/how-to/control-response-diversity)
  * [Adjust the model's thinking level](https://docs.sarvam.ai/api/token-factory/how-to/adjust-the-models-thinking-level)
  * [Encourage new topics in response](https://docs.sarvam.ai/api/token-factory/how-to/encourage-new-topics-in-response)
  * [Reduce repetition words or phrases in response](https://docs.sarvam.ai/api/token-factory/how-to/reduce-repetition-words-or-phrases-in-response)
  * [Get repeatable results](https://docs.sarvam.ai/api/token-factory/how-to/get-repeatable-results)
  * [Control the response length](https://docs.sarvam.ai/api/token-factory/how-to/control-the-response-length)
  * [Control where the model stops](https://docs.sarvam.ai/api/token-factory/how-to/control-where-the-model-stops)
  * [Overview](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)
  * [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion)
  * [Responses API](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/responses-api)
  * [Overview](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview)
  * [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion)
  * [Responses API](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/responses-api)
  * [Overview](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview)
  * [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-together/chat-completion)
  * [Saaras](https://docs.sarvam.ai/api/api-guides-tutorials/models/saaras)
  * [Bulbul](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul)
  * [Mayura](https://docs.sarvam.ai/api/api-guides-tutorials/models/mayura)
  * [Sarvam Translate](https://docs.sarvam.ai/api/api-guides-tutorials/models/sarvam-translate)
  * [Sarvam Vision](https://docs.sarvam.ai/api/api-guides-tutorials/models/sarvam-vision)
  * [Saarika (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/saarika)
  * [Sarvam 30B (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/sarvam-30b)
  * [Sarvam M (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/sarvam-m)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/overview)
  * [Which API to Use](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/which-api-to-use)
  * [Rest API](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/rest-api)
  * [Batch API](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/batch-api)
  * [Realtime Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/realtime-streaming)
  * [Best Practices](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/best-practices)
  * [FAQs](https://docs.sarvam.ai/api/speech-to-text/faq)
  * [Select Output Mode](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/select-output-mode)
  * [Specify Language Codes](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/specify-language-codes)
  * [Enable Speaker Diarization](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/enable-speaker-diarization)
  * [Keyterm Prompting](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/keyterms)
  * [IVR & Contact Center](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/ivr-contact-center)
  * [BFSI Voice Bots](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/bfsi-voice-bots)
  * [EdTech](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/edtech)
  * [Government Services](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/government-services)
  * [Agri & Rural](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/agri-rural)
  * [Streaming API](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/streaming-api)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/overview)
  * [Voices](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/voices)
  * [Which API to Use](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/which-api-to-use)
  * [Rest API](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/rest-api)
  * [HTTP Stream](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/streaming-api/http-stream)
  * [WebSocket](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/streaming-api/web-socket)
  * [Pronunciation Dictionary](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/pronunciation-dictionary)
  * [Best Practice Guide for Bulbul v4 Flash](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/best-practices)
  * [Best Practices (Bulbul v3)](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/bulbul-v3-best-practices)
  * [Set the Language](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-the-language)
  * [Change the Speaker Voice](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/change-the-speaker-voice)
  * [Adjust the Tone](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/adjust-the-tone)
  * [Adjust the Speed](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/adjust-the-speed)
  * [Adjust the Loudness](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/adjust-the-loudness)
  * [Set the Sample rate](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-the-sample-rate)
  * [Enable Text Preprocessing](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/enable-text-preprocessing)
  * [Set audio format for output](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-audio-format-for-output)
  * [Set bitrate for output](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-bitrate-for-output)
  * [Set maximum length for sentence splitting](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-maximum-length-for-sentence-splitting)
  * [Set buffer size to start processing](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-buffer-size-to-start-processing)
  * [IVR & Contact Center](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/ivr-contact-center)
  * [BFSI Voice Bots](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/bfsi-voice-bots)
  * [EdTech](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/edtech)
  * [Government Services](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/government-services)
  * [Agri & Rural](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/agri-rural)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/overview)
  * [Text Translation](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/translation)
  * [Transliteration](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/transliteration)
  * [Language Detection](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/language-detection)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview)
  * [Parse](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/parse)
  * [Extract](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract)
  * [Split](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split)
  * [Classify](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify)
  * [Jobs & Errors](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/job-lifecycle)
  * [Languages, Formats & Limits](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/languages-formats-limits)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/overview)
  * [Set Style Guidelines](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/style-guidelines)
  * [Pick a Genre](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/genre-and-model-tier)
  * [Use Native Numerals](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/native-numerals)
  * [Poll Status and Export Results](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/poll-and-export)
  * [FAQs](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/faq)
  * [Use Cases](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/use-cases)
  * [Translate a PDF](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/guides/translate-a-pdf)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/overview)
  * [Job Lifecycle](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/job-lifecycle)
  * [Specify Language Codes](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/specify-language-codes)
  * [Control Translation Tone](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/control-translation-tone)
  * [Choose a Voice](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/choose-a-voice)
  * [Choose Export Formats](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/choose-export-formats)
  * [FAQs](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/faq)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/overview)
  * [Prepare Reference Audio](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/prepare-reference-audio)
  * [Clone Across Languages](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/clone-across-languages)
  * [Choose Audio Formats](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/choose-audio-formats)
  * [Use Quality Control](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/use-quality-control)
  * [HTTP Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/http-streaming)
  * [WebSocket Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/websocket-streaming)
  * [Supported Languages](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/supported-languages)
  * [FAQs](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/faq)
  * [Introduction](https://docs.sarvam.ai/api/self-hosted/introduction)
  * [Managed vs Self-Hosted](https://docs.sarvam.ai/api/self-hosted/hosted-vs-self-hosted)
  * [How it works](https://docs.sarvam.ai/api/self-hosted/architecture)
  * [Get started](https://docs.sarvam.ai/api/self-hosted/sagemaker/get-started)
  * [Speech-to-Text (Saaras v3)](https://docs.sarvam.ai/api/self-hosted/sagemaker/deploy-saaras)
  * [Sarvam Vision](https://docs.sarvam.ai/api/self-hosted/sagemaker/deploy-vision)
  * [Text-to-Speech (Bulbul v3)](https://docs.sarvam.ai/api/self-hosted/sagemaker/deploy-bulbul)
  * [Deploy with Terraform](https://docs.sarvam.ai/api/self-hosted/sagemaker/terraform)
  * [Speech-to-Text](https://docs.sarvam.ai/api/self-hosted/sagemaker/api-saaras)
  * [Sarvam Vision](https://docs.sarvam.ai/api/self-hosted/sagemaker/api-vision)
  * [Text-to-Speech](https://docs.sarvam.ai/api/self-hosted/sagemaker/api-bulbul)
  * [Error handling](https://docs.sarvam.ai/api/self-hosted/sagemaker/errors)
  * [Configure & tune](https://docs.sarvam.ai/api/self-hosted/sagemaker/configure)
  * [Operations](https://docs.sarvam.ai/api/self-hosted/sagemaker/operations)
  * [Limitations](https://docs.sarvam.ai/api/self-hosted/sagemaker/limitations)
  * [Troubleshooting](https://docs.sarvam.ai/api/self-hosted/sagemaker/troubleshooting)
  * [LiveKit](https://docs.sarvam.ai/api/integration/build-voice-agent-with-live-kit)
  * [Pipecat](https://docs.sarvam.ai/api/integration/build-voice-agent-with-pipecat)
  * [Twilio](https://docs.sarvam.ai/api/integration/build-voice-agent-with-twilio)
  * [Exotel](https://docs.sarvam.ai/api/integration/build-voice-agent-with-exotel)
  * [Vobiz](https://docs.sarvam.ai/api/integration/build-voice-agent-with-vobiz)
  * [Vapi](https://docs.sarvam.ai/api/integration/build-voice-agent-with-vapi)
  * [n8n](https://docs.sarvam.ai/api/integration/n8n)
  * [Vercel AI SDK](https://docs.sarvam.ai/api/integration/vercel-ai-sdk)
  * [LangChain](https://docs.sarvam.ai/api/integration/langchain)
  * [LiveKit in Production](https://docs.sarvam.ai/api/integration/livekit-production-best-practices)
  * [Pipecat in Production](https://docs.sarvam.ai/api/integration/pipecat-production-guide)
  * [MCP Server](https://docs.sarvam.ai/api/developer-tools/mcp)
  * [Markdown & llms.txt](https://docs.sarvam.ai/api/developer-tools/llms-txt)
  * [Context7](https://docs.sarvam.ai/api/developer-tools/context7)
  * [Agent Skills](https://docs.sarvam.ai/api/developer-tools/agent-skills)
  * [Call Analytics Pipeline](https://docs.sarvam.ai/api/cookbook/guides/call-analytics-pipeline)
  * [Live Video Transcription](https://docs.sarvam.ai/api/cookbook/guides/live-video-transcription)
  * [Podcast Generator](https://docs.sarvam.ai/api/cookbook/guides/podcast-generator)
  * [WhatsApp Bot](https://docs.sarvam.ai/api/cookbook/guides/whats-app-bot)
  * [Support Voice Notes](https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes)
  * [Collection Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/collection-agent)
  * [Government Scheme Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/government-scheme-agent)
  * [Tutor Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/tutor-agent)
  * [Loan Advisory Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/loan-advisory-agent)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-elevenlabs/overview)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-elevenlabs/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-elevenlabs/speech-to-text)
  * [Instant Voice Cloning](https://docs.sarvam.ai/api/migrations/from-elevenlabs/voice-cloning)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-cartesia/overview)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-cartesia/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-cartesia/speech-to-text)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-deepgram/overview)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-deepgram/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-deepgram/speech-to-text)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-gemini/overview)
  * [Chat Completion](https://docs.sarvam.ai/api/migrations/from-gemini/chat-completion)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-gemini/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-gemini/speech-to-text)
  * [Building for Indian Languages](https://docs.sarvam.ai/api/getting-started/building-for-india)
  * [All Models](https://docs.sarvam.ai/api/getting-started/models)
  * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)
  * [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing)
  * [Organisations & workspaces](https://docs.sarvam.ai/api/platform/organisations-and-workspaces)
  * [Create an organisation](https://docs.sarvam.ai/api/platform/create-an-organisation)
  * [Create a workspace](https://docs.sarvam.ai/api/platform/create-a-workspace)
  * [Invite your team](https://docs.sarvam.ai/api/platform/invite-your-team)
  * [Billing & payments](https://docs.sarvam.ai/api/platform/billing)
  * [Platform FAQ](https://docs.sarvam.ai/api/platform/faq)



  * [Model APIs](https://docs.sarvam.ai/api)
  * [Voice Agents](https://docs.sarvam.ai/voice-agents)
  * [Doc Agents](https://docs.sarvam.ai/docai)
  * [Content Studio](https://docs.sarvam.ai/creative)
  * [Cowork](https://docs.sarvam.ai/cowork)
  * [API Reference](https://docs.sarvam.ai/api-reference)
  * [Changelog](https://docs.sarvam.ai/changelog)


