---
url: https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract/
title: How to extract fields from a document | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-27T14:22:30.396794+00:00
---

# How to extract fields from a document | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract/

Skip to navigation

On this page

  * Quick start
  * Parameters
  * Common gotchas
  * Schema rules
  * Write specific descriptions
  * Reuse a schema
  * Output formats
  * Next steps



Scroll to top

[API Guides & Tutorials](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview)[Document Intelligence](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview)[How-to](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/digitise)

# How to extract fields from a document

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract.md "View this page as plain text")|More actions

This page is for Model APIs.

Extract is schema-based key-value extraction. You define the fields you want and Sarvam Vision returns them as structured data. Use it for KYC, invoices, forms, and other structured data capture where you want **specific fields** , not the whole page.

|   
---|---  
**You provide**|  A document + a schema (or a saved `config_id`)  
**Endpoint**| `POST /doc-ai/v1/job/extract`  
**Output**|  The fields you define, as JSON, CSV, or XLSX  
**Page limit**|  20 pages per PDF or ZIP  
  
## Quick start

Extract takes the same document input, plus a **schema** describing the fields you want (or a saved `config_id`). The result is structured JSON with the field values you defined.

[1](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract#submit-the-job)

### Submit the job

Send the document with a schema describing the fields you want (or a saved `config_id`). You get a `job_id` back right away.

PythonJavaScriptcURL
    
    
    import json, os
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])
    
    # Define the fields you want back
    
    schema = {
    
        "type": "object",
    
        "properties": {
    
            "policy_number": {"type": "string", "description": "Insurance policy number"},
    
            "insured_name": {"type": "string", "description": "Name of the insured person"},
    
            "sum_insured": {"type": "number", "description": "Total sum insured, in INR"},
    
        },
    
    }
    
    with open("./insurance-policy.pdf", "rb") as f:
    
        job = client.doc_ai.extract(
    
            file=[("insurance-policy.pdf", f, "application/pdf")],
    
            schema=json.dumps(schema),  # or: config_id="cfg_abc123"
    
            language="en-IN",
    
            output_format="json",
    
        )
    
    print(job.job_id, job.status)  # status starts as "pending"

[2](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract#wait-for-it-to-finish)

### Wait for it to finish

Poll `get_status()` every few seconds until the job reaches a [terminal state](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/job-lifecycle#job-states).

PythonJavaScriptcURL
    
    
    import time
    
    TERMINAL = {"completed", "partially_completed", "failed", "rejected"}
    
    while True:
    
        st = client.doc_ai.get_status(job_id=job.job_id)
    
        print(f"status={st.status} pages={st.usage.pages_processed}/{st.usage.pages_total}")
    
        if st.status.lower() in TERMINAL:
    
            break
    
        time.sleep(5)

[3](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract#get-the-extracted-fields)

### Get the extracted fields

When the job is `completed` or `partially_completed`, fetch the field values.

PythonJavaScriptcURL
    
    
    if st.status.lower() in ("completed", "partially_completed"):
    
        results = client.doc_ai.get_results(job_id=job.job_id)
    
        print(results.result)  # {"policy_number": ..., "insured_name": ..., "sum_insured": ...}
    
    else:
    
        print("job did not complete:", st.status)

###### Full example (copy and run)

Submit, wait, and get the output in one script. Save it next to your document and run it.

PythonJavaScript
    
    
    import json, os, time
    
    from sarvamai import SarvamAI
    
    from sarvamai.core.api_error import ApiError
    
    client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])
    
    # Define the fields you want back
    
    schema = {
    
        "type": "object",
    
        "properties": {
    
            "policy_number": {"type": "string", "description": "Insurance policy number"},
    
            "insured_name": {"type": "string", "description": "Name of the insured person"},
    
            "sum_insured": {"type": "number", "description": "Total sum insured, in INR"},
    
        },
    
    }
    
    try:
    
        # 1. Submit the job
    
        with open("./insurance-policy.pdf", "rb") as f:
    
            job = client.doc_ai.extract(
    
                file=[("insurance-policy.pdf", f, "application/pdf")],
    
                schema=json.dumps(schema),  # or: config_id="cfg_abc123"
    
                language="en-IN",
    
                output_format="json",
    
            )
    
        print(job.job_id, job.status)  # status starts as "pending"
    
        # 2. Wait until it reaches a terminal state
    
        TERMINAL = {"completed", "partially_completed", "failed", "rejected"}
    
        while True:
    
            st = client.doc_ai.get_status(job_id=job.job_id)
    
            print(f"status={st.status} pages={st.usage.pages_processed}/{st.usage.pages_total}")
    
            if st.status.lower() in TERMINAL:
    
                break
    
            time.sleep(5)
    
        # 3. Get the output
    
        if st.status.lower() in ("completed", "partially_completed"):
    
            results = client.doc_ai.get_results(job_id=job.job_id)
    
            print(results.result)  # {"policy_number": ..., "insured_name": ..., "sum_insured": ...}
    
        else:
    
            print("job did not complete:", st.status)
    
    except FileNotFoundError:
    
        print("Document file not found: ./insurance-policy.pdf")
    
    except ApiError as e:
    
        print(f"API error {e.status_code}: {e.body}")

For a one-page invoice and a schema with `invoice_number`, `customer_name`, and `total_due`, `results.result` is a flat object of your fields:
    
    
    {
    
      "invoice_number": "2001",
    
      "customer_name": "Asha Rao",
    
      "total_due": 4500
    
    }

## Parameters

Parameter| Required| Default| Description  
---|---|---|---  
`file`| Yes| | The document to process. See [Languages, formats & limits](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/languages-formats-limits).  
`schema`| One of `schema` / `config_id`| | The fields to extract, as a JSON **string**. See [Schema rules](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract#schema-rules).  
`config_id`| One of `schema` / `config_id`| | A saved schema to reuse. See [Reuse a schema](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract#reuse-a-schema).  
`language`| No| Indic| A BCP-47 code such as `en-IN` or `hi-IN`. Always pass the correct code for best accuracy.  
`output_format`| No| `json`| `json`, `csv`, or `xlsx`.  
  
**Provide exactly one of`schema` or `config_id`.** Sending both, or neither, returns a `400`.

### Common gotchas

  * **`schema` is a JSON string, not an object.** It is sent as a multipart form field. Use `json.dumps(schema)` in Python and `JSON.stringify(schema)` in JavaScript. Passing a dict in Python raises `AttributeError: 'dict' object has no attribute 'read'`.
  * **The JavaScript SDK uses wire names, not camelCase.** Parameters and response fields are `output_format`, `job_id`, and `pages_processed`.
  * **`file` takes an array** in both SDKs.
  * **`job_id` is positional in JavaScript:** `getStatus(job_id)`, not `getStatus({ job_id })`.



## Schema rules

The inline schema is a JSON object with these constraints:

  * Root must be `type: "object"` with a non-empty `properties` map.
  * Every field needs a `type` and a non-empty `description`. The description guides the model, so make it specific.
  * Supported field types: `string`, `number`, `integer`, `boolean`, `object`, `array`.
  * An optional `enum` may be supplied to constrain values.
  * Maximum nesting depth is 4.



## Write specific descriptions

Each field’s `description` guides the model. A specific description outperforms a generic one:

Weak| Strong  
---|---  
`policy number`| `Insurance policy number, top-right, format ABC-1234`  
`date`| `Date the policy was issued, as YYYY-MM-DD`  
`amount`| `Total sum insured, in INR, digits only`  
  
## Reuse a schema

To reuse the same fields across many calls without re-sending the schema, save it as a Config and pass its `config_id` in place of `schema`.

  1. In the [Doc Agents](https://docs.sarvam.ai/docai/getting-started/overview) dashboard at [indus.sarvam.ai](https://indus.sarvam.ai/akshar/dashboard?ref=docs), start an Extract project, upload a document, and describe the fields you want.
  2. When the project finishes, open the **Config** tab, adjust the schema, and click **Save**.
  3. Copy the `config_id` shown on the saved Config (a UUID). Alternatively, click **Deploy as API endpoint** for a ready-made cURL command with the `config_id` filled in.



Then send it with your document:
    
    
    job = client.doc_ai.extract(
    
        file=[("insurance-policy.pdf", f, "application/pdf")],
    
        config_id="019ff577-91b7-7dde-b128-c5f418d06881",
    
        language="en-IN",
    
        output_format="json",
    
    )

## Output formats

Format| `output_format` value| Description  
---|---|---  
JSON| `json`| Structured field values (default)  
CSV| `csv`| Flat tabular output, one row per document  
XLSX| `xlsx`| Spreadsheet output  
  
**Page limit:** PDF and ZIP uploads are limited to **20 pages for Extract**. Exceeding the limit returns a `400 Bad Request` with code `invalid_request_error`. Split larger documents into batches before uploading.

## Next steps

  * [Jobs & Errors](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/job-lifecycle): job states, polling, and error handling.
  * [How to classify](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify): route documents to the right schema by type.



Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/digitise)[How to split a document bundleNext](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=docs.sarvam.ai)

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
        * [Digitise](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/digitise)
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
  * [Digitise](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/digitise)
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


