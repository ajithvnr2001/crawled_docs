---
url: https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split/
title: How to split a document bundle | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T06:34:25.512219+00:00
---

# How to split a document bundle | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split/

Skip to navigation

On this page

  * Quick start
  * Split methods
  * Split at markers
  * Split results
  * Request behaviours
  * Next steps



Scroll to top

[API Guides & Tutorials](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview)[Document Intelligence](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview)[How-to](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/parse)

# How to split a document bundle

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split.md "View this page as plain text")|More actions

This page is for Model APIs.

Split divides a bundle of pages into separate documents. Use it when **one file holds several documents** , such as a scanned stack of invoices and receipts.

|   
---|---  
**You provide**|  A document (+ a split method)  
**Endpoint**| `POST /doc-ai/v1/job/split`  
**Output**|  Child documents, each with its original page numbers and a `document_ref`  
**Input**|  PDF, PNG, JPEG, TIFF; up to 500 pages and 512 MB per document  
  
## Quick start

Split takes the same document input, plus a **method** describing where one document ends and the next begins. The result lists the child documents, each with its original page numbers and a `document_ref` you can reuse in other requests.

PythonJavaScriptcURL
    
    
    import os, time
    
    from sarvamai import SarvamAI
    
    from sarvamai.core.api_error import ApiError
    
    client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])
    
    try:
    
        # Create and submit a split job in one call
    
        with open("./sample-document.pdf", "rb") as f:
    
            job = client.doc_ai.split(
    
                file=[("sample-document.pdf", f, "application/pdf")],
    
                request={
    
                    "config": {
    
                        "method": "fixed_pages",
    
                        "pages_per_segment": 2,
    
                        "classify_segments": False,
    
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
    
        # Fetch the child documents
    
        if st.status.lower() in ("completed", "partially_completed"):
    
            results = client.doc_ai.get_results(job_id=job.job_id)
    
            for seg in results.result.segments:
    
                print(seg.pages, seg.document_ref, "review:", seg.review_required)
    
    except FileNotFoundError:
    
        print("Document file not found: ./sample-document.pdf")
    
    except ApiError as e:
    
        print(f"API error {e.status_code}: {e.body}")

**Send the options as a JSON string in`request`.** Split and Classify read their options from a `request` form field next to the file. In Python the SDK takes it as a dict (`request={...}`); with cURL, pass the JSON text. In Python, `file` takes a list and `job_id` is passed by name, `get_status(job_id=...)`. In JavaScript, `file` takes an array, `job_id` is positional, `getStatus(job_id)`, and request and response fields use the wire names (`pages_per_segment`, `review_required`), as for Parse and Extract.

## Split methods

Set `config.method` to one of:

Method| Use it when| Also needs  
---|---|---  
`semantic`| The model should find where each document starts and ends (default)| `categories`, or `classify_segments: false`  
`fixed_pages`| Every document has the same number of pages| `pages_per_segment`  
`page_ranges`| You already know the boundaries| `segment_ranges`  
`triggers`| Documents start at a marker such as a blank page or a line of text| `split_on`  
  
Other options:

  * `classify_segments`: `true` (the default) labels each child document with one of your `categories`; `false` only splits. With `true`, `categories` is required. With `false`, sending `categories` is rejected.
  * `categories`: up to 20 entries, each with a `type` and a `description`. Names are yours to choose and must be unique.
  * `remainder`: for `fixed_pages`, `keep` (the default) keeps a shorter last group and `error` rejects the request when the pages do not divide evenly.
  * `segment_ranges`: 1-based, inclusive ranges, such as `[{"start": 1, "end": 5}, {"start": 6, "end": 10}]`. They must cover the selected pages exactly once, in order.
  * `pages`: add `"pages": [{"start": 1, "end": 2}]` to the `request` to split only those pages.



## Split at markers

With `triggers`, a new document starts at each page that matches a marker in `split_on`:
    
    
    {"config": {"method": "triggers", "split_on": [{"type": "text", "match": {"prefix": "Cover:"}}], "classify_segments": false}}

  * `type`: `blank_page`, `text`, `qr_code`, `barcode`, or `photo`. A `photo` marker needs a `description` of the image.
  * `match`: for `text`, `qr_code`, and `barcode`, exactly one of `equals`, `prefix`, or `regex`. These go **inside** `match`, not on the marker itself.
  * Optional: `where` (`anywhere` or `top_of_page`), `trigger_page` (`first_page`, `separator_exclude`, or `separator_keep`), `split_when` (`every_match` or `value_changes`, for codes only), and `formats` for barcodes.



A blank separator page is left out of the segments (listed under `coverage.excluded_pages`). Pages before the first marker form a segment flagged `LEADING_PAGES_WITHOUT_TRIGGER`, and a file with no marker comes back as one segment flagged the same way. To label the segments, add `categories` and leave `classify_segments` on; with `classify_segments: false`, `categories` is rejected.

## Split results
    
    
    {
    
      "job_id": "01a17998-07ef-7040-800d-745a95140cf5",
    
      "type": "split",
    
      "status": "completed",
    
      "result": {
    
        "summary": {"documents": 2, "ready": 2, "needs_review": 0, "excluded_pages": 0, "unresolved_pages": 0},
    
        "review_required": false,
    
        "review_reasons": [],
    
        "coverage": {"complete": true, "excluded_pages": [], "unresolved_pages": []},
    
        "segments": [
    
          {
    
            "id": "seg_80d6fa828cfad12c7c13446b16bf81a0",
    
            "document_ref": "doc_80d6fa82...",
    
            "pages": [1, 2],
    
            "role": "document",
    
            "type": null,
    
            "classification_status": "not_requested",
    
            "review_required": false,
    
            "review_reasons": []
    
          }
    
        ]
    
      },
    
      "usage": {"pages_processed": 4, "pages_source": 4}
    
    }

  * Each segment is a child document. `pages` refers to its original page numbers, and `document_ref` lets you reuse it in another request.
  * With `classify_segments: true`, `type` is the matching category and `classification_status` is `matched`, or `unknown` with `unknown_reason: "no_matching_type"` when none fits.
  * `status: "completed"` means processing finished, not that every segment passed review. Check `review_required` on each segment before accepting the result automatically.



## Request behaviours

Split and [Classify](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify) share these request behaviours:

  * **Inputs:** PDF, PNG, JPEG, or TIFF. Repeat the `file` field for up to 10 documents with the same config; you get a parent job and a `documents` list of individual jobs, each with its own `status_url` and `results_url`. The parent’s results include each document’s result under `documents`. You can also upload first with `POST /doc-ai/v1/job/upload` and send the id as `upload_ids`. URL input is not available.
  * **Retries:** add an `Idempotency-Key` header to retry the same submission without creating another job. A changed request under the same key returns `409`.
  * **Waiting:** send `"execution": "auto"` in `request` to wait briefly for a single document. A finished answer returns with HTTP `200`; otherwise you get the job to poll.
  * **Capabilities:** `GET /doc-ai/v1/capabilities` lists the operations, input formats, split methods, and limits enabled on your deployment.



## Next steps

[How to classifyLabel each child document by its `document_ref`.](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify)[Jobs & ErrorsJob states, polling, and error handling.](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/job-lifecycle)

Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract)[How to classify documentsNext](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=docs.sarvam.ai)

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


