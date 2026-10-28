---
url: https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify/
title: How to classify documents | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T06:34:24.547061+00:00
---

# How to classify documents | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify/

Skip to navigation

On this page

  * Quick start
  * Classify options
  * Choose which pages to read
  * Classify results
  * Split, then classify
  * Next steps



Scroll to top

[API Guides & Tutorials](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview)[Document Intelligence](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview)[How-to](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/parse)

# How to classify documents

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify.md "View this page as plain text")|More actions

This page is for Model APIs.

Classify labels a whole document, or each page, against the categories you define. Without categories, it suggests a document type. Use it to **route or triage** documents before processing them.

|   
---|---  
**You provide**|  A document (+ categories, optional)  
**Endpoint**| `POST /doc-ai/v1/job/classify`  
**Output**|  A document type (or one per page), with evidence and a review flag  
**Input**|  PDF, PNG, JPEG, TIFF; up to 500 pages and 512 MB per document  
  
## Quick start

Classify takes the same document input, plus the **categories** you want to choose between. It labels the whole document, or each page. Without categories, it suggests a document type.

PythonJavaScriptcURL
    
    
    import os, time
    
    from sarvamai import SarvamAI
    
    from sarvamai.core.api_error import ApiError
    
    client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])
    
    try:
    
        # Create and submit a classify job in one call
    
        with open("./sample-document.pdf", "rb") as f:
    
            job = client.doc_ai.classify(
    
                file=[("sample-document.pdf", f, "application/pdf")],
    
                request={
    
                    "config": {
    
                        "scope": "page",
    
                        "categories": [
    
                            {"type": "Invoice", "description": "A supplier bill with totals and payment details."},
    
                            {"type": "Receipt", "description": "Proof of a completed payment."},
    
                        ],
    
                    },
    
                },
    
            )
    
        print("job created:", job.job_id, "| status:", job.status)
    
        # Poll until the job reaches a terminal state
    
        TERMINAL = {"completed", "partially_completed", "failed", "rejected"}
    
        while True:
    
            st = client.doc_ai.get_status(job_id=job.job_id)
    
            print(f"status={st.status} phase={st.phase}")
    
            if st.status.lower() in TERMINAL:
    
                break
    
            time.sleep(5)
    
        # Fetch the decisions
    
        if st.status.lower() in ("completed", "partially_completed"):
    
            results = client.doc_ai.get_results(job_id=job.job_id)
    
            for d in results.result.decisions:
    
                print(d.input_page, d.type, d.classification_status, "review:", d.review_required)
    
    except FileNotFoundError:
    
        print("Document file not found: ./sample-document.pdf")
    
    except ApiError as e:
    
        print(f"API error {e.status_code}: {e.body}")

## Classify options

  * `config.scope`: `document` (one decision for the file, the default) or `page` (one decision per page, returned in `decisions`).
  * `config.categories`: up to 20 entries, each with a `type` and a `description`. Names are yours to choose and must be unique. Omit them to let the API suggest a document type.
  * `config.unmatched_behavior`: `suggest_type` (the default) returns a `suggested_type` when no category fits; `other` returns `type: "other"` instead.
  * `config.prompt`: your own instruction text, up to 8,000 characters.
  * `output.include_evidence`: `true` returns the pages, text blocks, and region that support each decision.
  * `language`: a BCP-47 code such as `en-IN`. Omit it for the Indic default, as for Parse.
  * `reasoning_input`: `auto` (the default) or `text_only`.



Write each category `description` so it separates that category from the others, for example “A supplier bill with totals and payment details” rather than “financial document”.

## Choose which pages to read

Use one of `config.max_pages` (the first N pages), `config.target_pages` (such as `[1, 6, 8]`), or `config.inspection`. Combining them is rejected.

`inspection.policy`| Reads| Example  
---|---|---  
`first`| The first N pages| `{"policy": "first", "count": 2}`  
`last`| The last N pages| `{"policy": "last", "count": 2}`  
`head_tail`| The beginning and the end| `{"policy": "head_tail", "head_pages": 2, "tail_pages": 1}`  
`explicit`| Page ranges you choose| `{"policy": "explicit", "ranges": [{"start": 1, "end": 2}]}`  
`all`| Every selected page| `{"policy": "all"}`  
`adaptive`| Starts with a selection, expands if needed| `{"policy": "adaptive", "initial": {"policy": "first", "count": 2}, "max_pages": 10}`  
  
`count` must be at least 1. Page ranges are 1-based and inclusive. For `adaptive`, `initial` can be `first`, `last`, `head_tail`, or `explicit`, and `max_pages` must cover the initial selection.

Reading only some pages is faster, but a bundle of several documents can look like one. In testing, a PDF holding an invoice followed by two receipts classified as `Invoice` when only the first page was read, and as `mixed` when every page was read. Use `all`, or [split](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split) the file first.

## Classify results
    
    
    {
    
      "job_id": "01a17998-120b-73dc-ad42-5cd66e0fe0ff",
    
      "type": "classify",
    
      "status": "completed",
    
      "result": {
    
        "scope": "document",
    
        "type": "Invoice",
    
        "classification_status": "matched",
    
        "confidence": 1,
    
        "reasoning": "The document is explicitly titled 'INVOICE #2001' and contains a total amount due.",
    
        "review_required": false,
    
        "review_reasons": [],
    
        "suggested_type": null
    
      },
    
      "usage": {"pages_processed": 2, "pages_source": 2}
    
    }

Field| Meaning  
---|---  
`type`| The matching category. `null` when the status is `unknown` or `mixed`; `other` when nothing matched and `unmatched_behavior` is `other`  
`classification_status`| `matched` (a category fits), `unknown` (none fits), or `mixed` (the file holds several documents)  
`reason_code`| On `unknown`: `no_matching_type`, or `insufficient_evidence` when the pages were not enough to tell  
`confidence`| A token-based score from 0 to 1, or `null`. It is not a measured probability of being correct  
`review_required`| Whether a person should check the answer. Low or missing confidence and unresolved answers require review  
`review_reasons`| For example `NO_MATCHING_TYPE`, `MODEL_SCORE_UNAVAILABLE`, or `MULTIPLE_DOCUMENTS_DETECTED`  
`suggested_type`| A type you did not supply, with its `name` and supporting `evidence`. `null` when there is nothing to suggest  
  
When no category matches, the job still completes: you get `classification_status: "unknown"` and `reason_code: "no_matching_type"`, and, with `suggest_type`, the document’s own type in `suggested_type`. With `scope: "page"`, `result` holds a `decisions` list with one entry per page instead of a single decision.

Results are short by default. Add `?include=details` to the results request for the inspected pages and provenance.

## Split, then classify

Classify reads the pages you point it at, so a bundle of several documents can look like one. [Split](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split) first, then classify each child document by its `document_ref`. To classify one child document, send a JSON body instead of a file:
    
    
    curl -X POST https://api.sarvam.ai/doc-ai/v1/job/classify \
    
      -H "api-subscription-key: $SARVAM_API_KEY" \
    
      -H "Content-Type: application/json" \
    
      -d '{"input": {"document_ref": "doc_..."}, "config": {"scope": "document", "categories": [{"type": "Invoice", "description": "A supplier bill."}]}}'

Classify shares its request behaviours (multiple documents, `Idempotency-Key`, `execution: "auto"`, capabilities) with Split. See [Request behaviours](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split#request-behaviours).

## Next steps

[How to splitSeparate a bundle into documents first.](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split)[Jobs & ErrorsJob states, polling, and error handling.](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/job-lifecycle)

Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split)[Jobs & ErrorsNext](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/job-lifecycle)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=docs.sarvam.ai)

  * Getting Started

    * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
    * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
    * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
    * [Building for Indian Languages](https://docs.sarvam.ai/api/getting-started/building-for-india)
    * [Models](https://docs.sarvam.ai/api/getting-started/models)

    * [Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/ratelimits)
    * [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing)
    * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)
    * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
    * [Pricing](https://docs.sarvam.ai/api/getting-started/pricing)
    * Account & Billing

  * API Guides & Tutorials

    * Large Language Models

    * Speech to Text

    * Text to Speech

    * Text Processing

    * Document Intelligence
      * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview)
      * How-to
        * [Parse](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/parse)
        * [Extract](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract)
        * [Split](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split)
        * [Classify](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify)

      * [Jobs & Errors](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/job-lifecycle)
      * [Languages, Formats & Limits](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/languages-formats-limits)

    * Document Translation

    * Dubbing

    * Instant Voice CloningBeta

  *     * Integration

    * Developer Tools

  * Cookbook

    * Guides

    * Example Voice Agents

  * Self-Hosted Deployments

    * Overview

    * AWS SageMaker

  *     * Migrations




  * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
  * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
  * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
  * [Building for Indian Languages](https://docs.sarvam.ai/api/getting-started/building-for-india)
  * [Models](https://docs.sarvam.ai/api/getting-started/models)
  * [Saaras](https://docs.sarvam.ai/api/getting-started/models/saaras)
  * [Bulbul](https://docs.sarvam.ai/api/getting-started/models/bulbul)
  * [Sarvam 105B](https://docs.sarvam.ai/api/getting-started/models/sarvam-105b)
  * [Open-Weight Models](https://docs.sarvam.ai/api/getting-started/models/openweight)
  * [GLM-5.3](https://docs.sarvam.ai/api/getting-started/models/openweight/glm-5-3)
  * [Gemma 4 31B](https://docs.sarvam.ai/api/getting-started/models/openweight/gemma-4-31b)
  * [DeepSeek V4.1 Flash](https://docs.sarvam.ai/api/getting-started/models/openweight/deepseek-v4.1-flash)
  * [Mayura](https://docs.sarvam.ai/api/getting-started/models/mayura)
  * [Sarvam Translate](https://docs.sarvam.ai/api/getting-started/models/sarvam-translate)
  * [Sarvam Vision](https://docs.sarvam.ai/api/getting-started/models/sarvam-vision)
  * [Sarvam 30B (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/sarvam-30b)
  * [Sarvam M (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/sarvam-m)
  * [Saarika (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/saarika)
  * [Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/ratelimits)
  * [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing)
  * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)
  * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
  * [Pricing](https://docs.sarvam.ai/api/getting-started/pricing)
  * [Organisations & workspaces](https://docs.sarvam.ai/api/platform/organisations-and-workspaces)
  * [Create an organisation](https://docs.sarvam.ai/api/platform/create-an-organisation)
  * [Create a workspace](https://docs.sarvam.ai/api/platform/create-a-workspace)
  * [Invite your team](https://docs.sarvam.ai/api/platform/invite-your-team)
  * [Billing & payments](https://docs.sarvam.ai/api/platform/billing)
  * [Platform FAQ](https://docs.sarvam.ai/api/platform/faq)
  * [Chat Completion](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview)
  * [Responses API](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/responses-api)
  * [List your chat messages](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/list-your-chat-messages)
  * [Control response randomness](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/control-response-randomness)
  * [Control response diversity](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/control-response-diversity)
  * [Adjust the model's thinking level](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/adjust-the-models-thinking-level)
  * [Encourage new topics in response](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/encourage-new-topics-in-response)
  * [Reduce repetition words or phrases in response](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/reduce-repetition-words-or-phrases-in-response)
  * [Get repeatable results](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/get-repeatable-results)
  * [Control the response length](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/control-the-response-length)
  * [Control where the model stops](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/control-where-the-model-stops)
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



  * [Model APIs](https://docs.sarvam.ai/api)
  * [Voice Agents](https://docs.sarvam.ai/voice-agents)
  * [Doc Agents](https://docs.sarvam.ai/docai)
  * [Content Studio](https://docs.sarvam.ai/creative)
  * [Cowork](https://docs.sarvam.ai/cowork)
  * [API Reference](https://docs.sarvam.ai/api-reference)
  * [Changelog](https://docs.sarvam.ai/changelog)


