---
url: https://docs.sarvam.ai/changelog/
title: Change Log | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-11-07T06:39:10.152560+00:00
---

# Change Log | Sarvam API Docs

> Source: https://docs.sarvam.ai/changelog/

Skip to navigation

This page is for Changelog.

# [Change Log](https://docs.sarvam.ai/changelog)

Subscribe via RSS

Track new features, model updates, and breaking changes across Sarvam AI’s APIs and products. Use the filters below to narrow the timeline to a single product - Model APIs, Voice Agents, Document AI, Content Studio, or Cowork.

Subscribe to updates: append `.rss`, `.atom`, or `.json` to this page’s URL - e.g. `https://docs.sarvam.ai/changelog.rss`.

[Request a feature](mailto:support@sarvam.ai?subject=Sarvam%20feature%20request)

Select filters

Nov 6, 2026

### [Provisioned Throughput and Kimi K3.1 Pro on Token Factory](https://docs.sarvam.ai/changelog/2026/11/6)

Token Factory models are now labelled **Serverless** (any API key can call them, billed per token) or **Provisioned Throughput**. Models that were labelled beta are now on [Provisioned Throughput](https://docs.sarvam.ai/api/token-factory/models#provisioned-throughput): capacity set up for your workload and enabled for your organisation. Access works as before; [contact us](https://docs.sarvam.ai/api/getting-started/help) to request it.

  * **[`kimi-k3.1-pro`](https://docs.sarvam.ai/api/token-factory/models/kimi-k3.1-pro)** replaces `kimi-k3`, on Provisioned Throughput at ₹250 input, ₹25 cached input, and ₹1,350 output per 1M tokens.
  * `kimi-k3`, `mimo-v2.6-flash`, and `mimo-v2.6-pro` are no longer offered. For the lowest per-token price, use [`glm5.3-flash`](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash).



Model APIs

Nov 3, 2026

### [Knowledge Base Metadata Fields](https://docs.sarvam.ai/changelog/2026/11/3)

You can now define your own metadata fields on a knowledge base, such as department, year or document type, and fill in the values for each file as you upload it. Mark a field as required, limit it to a list of allowed values, or make it filterable, then change the definitions later from the **Fields** tab. Every file’s values show up in the file table and in the preview pane. See [Knowledge Bases](https://docs.sarvam.ai/cowork/build/knowledge-bases).

Cowork

Oct 31, 2026

### [MCP Integrations Are Now Available](https://docs.sarvam.ai/changelog/2026/10/31)

You can now connect third-party tools to Sarvam and use them in your voice agents. Open **Integrations** in the sidebar to browse or search the catalogue, connect a tool once for the whole workspace by approving access on the vendor’s consent screen, or add any other MCP server by its endpoint URL. To use one, open **Add a tool** in the agent editor, choose **MCP** , and tick the actions that agent should be able to call — each parameter can be a fixed value, an agent variable, or decided from the conversation.

Voice Agents

Oct 30, 2026

### [Larger Knowledge Base Files](https://docs.sarvam.ai/changelog/2026/10/30)

You can now add files up to 5 GB to a knowledge base, up from the 100 MB the upload dialog was quietly allowing. Files that are too large or the wrong type are now flagged with a clear message instead of disappearing without explanation. See [Knowledge Bases](https://docs.sarvam.ai/cowork/build/knowledge-bases).

Cowork

### [DeepSeek V4.1 Flash 1017 Is Generally Available](https://docs.sarvam.ai/changelog/2026/10/30#2026-10-30-deepseek-v41-flash-1017-is-generally-available)

[`deepseekv4.1-flash-1017`](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017) is now generally available on `POST /v2/chat/completions` and `POST /v2/responses`. Your API key no longer needs beta access. It reasons at `high` by default (`reasoning_effort: "none"` turns thinking off), accepts text and image input, and has a 1,048,576-token context window.

Pricing is unchanged: ₹25 input, ₹0.5 cached input, and ₹105 output per 1M tokens. See [Pricing](https://docs.sarvam.ai/api/getting-started/pricing).

Model APIs

Oct 29, 2026

### [Email Download Links for Call Log Exports](https://docs.sarvam.ai/changelog/2026/10/29)

When you click **Download CSV** in [Call Logs](https://docs.sarvam.ai/voice-agents/monitor/agent-analytics/call-logs#export-calls-to-csv), we now email you a download link once your file is ready. You can also find your exports from the last 7 days under **Recent exports**.

Voice Agents

Oct 28, 2026

### [Exclude Cohort for Campaigns](https://docs.sarvam.ai/changelog/2026/10/28)

You can now exclude contacts already on a campaign with [Exclude cohort](https://docs.sarvam.ai/voice-agents/api/campaigns/cohorts/exclude-cohort). Upload a CSV of users to remove — matched by user identifier or phone number — via the same cohort upload endpoint with `cohort_category` set to `stop_file`. An exclude cohort only removes contacts already on that campaign; it does not filter users added later. See [Exclude cohort](https://docs.sarvam.ai/voice-agents/deploy/campaigns/cohorts#exclude-cohort).

Voice Agents

Oct 26, 2026

### [Optional language on Instant Voice Cloning](https://docs.sarvam.ai/changelog/2026/10/26)

`language_code` / `target_language_code` is now optional on `POST /voices/clone`, `POST /voices/clone/stream`, and `GET /voices/clone/ws`. Omit it to detect the language from `text`. Pass the code when pronunciation has to be exact — detection can be wrong on short or code-mixed text, romanized Indic and Urdu return `400`, and short Assamese without ৰ or ৱ is often detected as Bengali. On the WebSocket the first detection stays locked until you send a new `config` with an explicit code. See [Supported languages](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/supported-languages).

Model APIs

Oct 24, 2026

### [GitHub App Connector Is Faster and Lighter](https://docs.sarvam.ai/changelog/2026/10/24)

You can now connect GitHub App as a Cowork connector and choose exactly which repositories your agent can reach. In our tests it finished tasks 26% faster and used 40% fewer tokens than the old connector. See [Connectors](https://docs.sarvam.ai/cowork/build/connectors).

Cowork

Oct 22, 2026

### [Agent Session History](https://docs.sarvam.ai/changelog/2026/10/22)

Agent pages now have a **Mine** / **Team** toggle, so you can see your own recent sessions or those of your teammates in the same workspace. Any session opens as a read-only transcript you can review after the run finishes.

Cowork

### [GLM-5.3, Gemma 4 31B, DeepSeek V4.1 Flash, and the Responses API Are Generally Available](https://docs.sarvam.ai/changelog/2026/10/22#2026-10-22-glm-53-gemma-4-31b-deepseek-v41-flash-and-the-responses-api-are-generally-available)

[`POST /v2/chat/completions`](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2) and [`POST /v2/responses`](https://docs.sarvam.ai/api-reference/responses/create) are now generally available with [GLM-5.3](https://docs.sarvam.ai/api/token-factory/models/glm-5-3), [Gemma 4 31B](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b), and [DeepSeek V4.1 Flash](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017), alongside `sarvam-105b`. No beta whitelisting is required for these endpoints or models. See [Beta APIs and Models](https://docs.sarvam.ai/api-reference/beta-apis) for anything still in beta.

Model APIs

Oct 20, 2026

### [New Models on Chat Completion V2 and Responses](https://docs.sarvam.ai/changelog/2026/10/20)

New open-weight models are available on `POST /v2/chat/completions` and `POST /v2/responses`.

**Generally available:**

  * **[`glm5.3-flash`](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)** : a faster GLM-5.3 with image input, log probabilities, and `n` > 1\. Reasons by default. 1,048,576-token context.



**In beta:**

Model APIs

### [Chat Completion V2 and Responses Are Generally Available](https://docs.sarvam.ai/changelog/2026/10/20#2026-10-20-chat-completion-v2-and-responses-are-generally-available)

`POST /v2/chat/completions` and `POST /v2/responses` are now generally available with `sarvam-105b`, `glm5.3`, `glm5.3-flash`, and `gemma4`. Your API key no longer needs to be whitelisted. The new models in the entry above are in beta; see [Beta models](https://docs.sarvam.ai/api-reference/beta-apis).

Model APIs

Oct 16, 2026

### [Dual-Channel Call Recordings](https://docs.sarvam.ai/changelog/2026/10/16)

Call recordings are now captured in stereo, with the **user on the left channel and the agent on the right**. Mono recordings mixed both speakers onto a single channel, so overlapping speech was summed and could clip; in stereo each speaker stays isolated, which makes recordings easier to listen to and better suited for downstream processing (transcription, analytics). This is now enabled for all calls. See [Call recordings](https://docs.sarvam.ai/voice-agents/monitor/call-recordings).

Voice Agents

### [Forwarded Call Recordings, Call Traces, and Provider Details in the Analytics API](https://docs.sarvam.ai/changelog/2026/10/16#2026-10-16-forwarded-call-recordings-call-traces-and-provider-details-in-the-analytics-api)

The Analytics API now gives you more of what happened on each call. [Get forwarded recording](https://docs.sarvam.ai/voice-agents/api/analytics/forwarded-recordings) returns the recording of the part of a call after your agent transferred it, currently for transfers made through Vobiz, and [Get trace](https://docs.sarvam.ai/voice-agents/api/analytics/traces) returns a call’s step-by-step event trace: the speech recognition, LLM, tool-call, and text-to-speech events of every turn, plus the conversation’s start, end, and post-call analysis. [List attempts](https://docs.sarvam.ai/voice-agents/api/analytics/attempts) and [List interactions](https://docs.sarvam.ai/voice-agents/api/analytics/interactions) now include provider details for each call, `channel_provider` (the telephony provider that carried it) and `provider_identifier` (that provider’s own call ID, such as a call SID), so you can match calls to your provider’s records. Both also add `deployment_id`, `app_version`, `bot_contact_identifier` (your agent’s own number), and goal results in `goal_overall_status` and `goal_criteria`. You can also sort by `attempted_at`, and filter on `app_version` and `goal_overall_status`.

Voice Agents

Oct 15, 2026

### [Higher Saved-Voice Limit](https://docs.sarvam.ai/changelog/2026/10/15)

You can now save up to 50 cloned voices on the Starter plan, up from 5. Pro and Enterprise plans have higher limits. Voices are counted across your whole organization, in Content Studio and the API, and deleting a voice frees up a slot. See [Managing Your Voice Library](https://docs.sarvam.ai/creative-voice-library-manage).

Content Studio

Oct 14, 2026

### [Genie Across the Voice Agents Platform](https://docs.sarvam.ai/changelog/2026/10/14)

Genie, the AI assistant in Voice Agents, now goes beyond creating and editing agents. It is available from every Voice Agents page through **Ask Genie** , in a panel that stays open as you move between pages, so you can build an agent, deploy it, and check its calls in a single chat. Genie can now put an agent live on one of your connected phone numbers for inbound calls and place a test call to your phone. It can also create outbound campaigns, upload contact lists from a CSV, and pause, resume, edit, or cancel campaigns. To analyze calls, Genie can summarize performance and connect rates, explain why calls didn’t connect, read transcripts, check tool errors, and build Boards. Within an agent, it can also set up knowledge bases and test suites. Genie asks you to confirm before anything that places calls, affects live traffic, or can’t be undone. See [Genie](https://docs.sarvam.ai/voice-agents/build/genie).

Voice Agents

### [Bulbul V3 End of Life for Voice Agents](https://docs.sarvam.ai/changelog/2026/10/14#2026-10-14-bulbul-v3-end-of-life-for-voice-agents)

Bulbul V3 reaches end of life on Voice Agents on **November 10, 2026**. Switch every agent that speaks with Bulbul V3 to Bulbul V4 before that date. In the agent’s **Settings** , set the model under **Speaking** to **Bulbul V4** and pick a voice. To keep a voice you use today, find its Bulbul V4 name in [Voice name changes from V3 to V4](https://docs.sarvam.ai/voice-agents/build/voice-language#voice-name-changes-from-v3-to-v4). This change applies to Voice Agents only. Bulbul V3 stays available on the [Text-to-Speech API](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul).

Voice Agents

### [Volume Adjustment for Voice Agents](https://docs.sarvam.ai/changelog/2026/10/14#2026-10-14-volume-adjustment-for-voice-agents)

You can now control how loud your voice agent sounds. A new **Volume** slider in the agent’s voice settings (Sarvam / Bulbul voices) sets the loudness of the agent’s speech, from `0.7` (quieter) to `2.0` (louder), with `1.0` as the natural level. The volume is stored with the agent’s voice configuration and applied on every call, so it can be set once and manipulated later. See [Speakers & voice](https://docs.sarvam.ai/voice-agents/build/voice-language#volume).

Voice Agents

Oct 13, 2026

### [Editable Decks and Documents](https://docs.sarvam.ai/changelog/2026/10/13)

You can now edit the presentations and documents your agent creates, right in the app. Every edit you make becomes the next version, and any document can be exported as a PDF.

Cowork

[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

  *     * [Changelog](https://docs.sarvam.ai/changelog "Last updated today at 12:00 AM")



  * [Changelog](https://docs.sarvam.ai/changelog)



  * [Model APIs](https://docs.sarvam.ai/api)
  * [Voice Agents](https://docs.sarvam.ai/voice-agents)
  * [Document AI](https://docs.sarvam.ai/doc-ai)
  * [Content Studio](https://docs.sarvam.ai/creative)
  * [Cowork](https://docs.sarvam.ai/cowork)
  * [API Reference](https://docs.sarvam.ai/api-reference)
  * [Changelog](https://docs.sarvam.ai/changelog)


