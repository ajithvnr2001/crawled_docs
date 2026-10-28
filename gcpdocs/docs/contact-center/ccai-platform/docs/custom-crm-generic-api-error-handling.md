---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm-generic-api-error-handling/
title: Error handling, retries, and call ordering in custom CRM (generic API) \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T19:38:21.064069+00:00
---

# Error handling, retries, and call ordering in custom CRM (generic API)  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm-generic-api-error-handling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Error handling, retries, and call ordering in custom CRM (generic API) Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the behavior of CCAI Platform's custom CRM (generic API) feature when your CRM endpoints return responses other than `HTTP 200 "Success."` It is intended as a behavior reference for integrators configuring API account and API record endpoints.

**Note:** This document covers the direction where CCAI Platform calls your CRM endpoints.

## High-level execution order and relationships

When an interaction triggers a custom CRM integration, the platform calls your endpoints in this order:

  1. Account-level operations (API account) - contact

Examples:

     * Find a contact.

     * Create a contact.

     * Update a contact.

  2. Record-level operations (API record) - ticket or case

Examples:

     * Find a ticket.

     * Create a ticket.

     * Update a ticket.

  3. Post-session actions (if configured)

Examples:

     * Add a comment or note.

     * Upload an attachment or transcript.

     * Apply wrap-up updates.




Earlier steps typically produce IDs that later steps may use. For example, a `contact_id` can be passed to ticket creation when included in your endpoint payload template, and a `ticket_id` is required for post-session actions in typical generic API setups Note that not every endpoint is configured to extract an ID - see Important nuance: 2xx + missing ID on ID-extracting endpoints.

## Important nuance: `2xx` \+ missing ID on ID-extracting endpoints

Not every custom CRM endpoint extracts an ID from the response it receives. This behavior applies only to endpoints configured with a `response_data_location` and (for create endpoints) a `custom_id_location` \- typically lookup endpoints (extracting an existing record's ID) and create endpoints (extracting a newly-created record's ID). Endpoints such as comments, attachments, and updates don't extract IDs from their responses.

**Caution:** If one of those ID-extracting endpoints returns `2xx` but the platform can't extract the expected ID from the configured response location, the platform may treat the call as successful and continue — while carrying a `null` or missing ID forward.

### Impact of missing ID on ID-extracting endpoints

  * For lookup endpoints: A `200 OK` response with no matching record (and therefore no extractable ID) is normal "not found" behavior. If your instance has `skip_account_creation` or `skip_record_creation` enabled, the platform will intentionally proceed downstream with a null `contact_id` or `ticket_id` rather than attempting creation. This is expected behavior under those configurations and isn't a misconfiguration.

  * For create endpoints: A `200 OK` response that doesn't include the newly created ID at the configured location is a configuration or response-contract issue. The HTTP request succeeded, so retries won't be triggered - but downstream steps may proceed with missing data.

  * In both cases, the failure (where it is a failure) appears as missing data rather than as an endpoint error, which can be confusing during debugging.




### Integrator guidance

  * For create operations, make returning the expected ID at the configured location part of your success contract, not just returning `2xx`. Treat a missing ID as a configuration or response-contract issue worth investigating.

  * For lookup operations, returning `200 OK` with no match is acceptable. If your instance intentionally relies on "lookup without creation" patterns (for example, `skip_account_creation = true`), document that decision so downstream endpoints know how to handle missing IDs gracefully.

  * In testing, verify that:

    * For create endpoints, the ID is reliably present in the response and at the exact location configured in custom CRM.

    * For lookup endpoints, the platform's downstream behavior matches your instance's skip-flag configuration.




## Error handling: overview

When an endpoint returns a non-success response (non-`2xx`) or doesn't respond:

  * The platform may retry the request:

    * Once immediately for some statuses.

    * Over a longer period for failures that can be retried.

  * Downstream steps may be delayed while the platform continues retrying an upstream step.

  * Some failures are treated as non-retriable (for example, configuration or validation failures).




The detailed retry rules are described in Retry and backoff behavior. The relationship between failures and downstream calls is described in Chaining and dependency rules.

## Chaining and dependency rules

Custom CRM behavior is governed by your instance's CRM configuration - specifically the settings documented in [Skip CRM account and record creation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/skip-crm-account-record-creation). This document refers to those settings by their backend configuration names (`skip_account_creation`, `skip_account_lookup`, `skip_record_creation`) since they appear that way in the following JSON configuration examples.

Within those settings, the platform is biased toward continuing the chain when it can - for example, by creating an anonymous contact when lookup fails and account creation is enabled - rather than always "hard-stopping."

### Impact of account failures on record operations

The record step (ticket/case) may run even when the account step doesn't produce a contact, but the exact behavior depends on the instance's configuration.

Depending on your configuration, the platform can:

  * Create an anonymous contact as a fallback and continue to ticket creation.

  * Proceed to record steps without a `contact_id` when account lookup or account creation is configured to be skipped.




#### What this means for your endpoints

  * A missing `contact_id` on ticket creation usually indicates an instance configuration where account lookup or account creation is disabled.

  * If your instance requires accounts, treat a missing `contact_id` as a signal worth investigating rather than silently inserting tickets without a contact.

  * If your configuration intentionally allows ticket creation without a contact, make sure your ticket endpoint handles that case explicitly and predictably.




### Impact of record failures on post-session actions

For generic API setups where ticket lookup is configured, the platform doesn't dispatch post-session calls - such as `call_finished`, `chat_finished`, `email_finished`, `save_call_recording`, `save_chat_history`, `update_ticket`, and `done_ticket`, until a `ticket_id` exists.

If a post-session endpoint is invoked without a `ticket_id`, it usually indicates one of the following conditions:

  * Ticket lookup is disabled for the instance configuration, which is uncommon for a typical generic API setup.

  * The payload template omitted the `ticket_id` variable, which is a configuration issue worth investigating.




#### What this means for your endpoints

  * Treat a missing `ticket_id` on post-session calls as a configuration signal worth investigating, not as expected behavior to silently absorb.

  * If your configuration intentionally doesn't require ticket lookup, configure your post-session endpoints to handle a missing `ticket_id` gracefully. For example, log the issue and no-op, or return a clear, well-structured error message instead of crashing.




## Retry and backoff behavior

Retries happen in three layers:

  1. HTTP-level immediate retry (a quick second attempt).

  2. Adaptor-level retry (fast recovery for network failures and specific transient responses).

  3. Command-level retries (long-tail retries over days).


**Note:** Regarding ID checks in the retry flow, any _ID expected at the configuration location?_ decision applies only to endpoints that are configured to extract an ID from the response. Endpoints that don't extract an ID skip that decision and treat a 2xx response as HTTP success.

### HTTP-level immediate retry (quick retry)

For certain transient statuses, the platform makes up to 2 attempts total (1 initial attempt + 1 immediate retry). This typically applies to the following error statuses:

  * `408`, `413`, `429`, `500`, `502`, `503`, `504`, `521`, `522`, and `524`.

**Note:** Statuses like `400`, `401`, `403`, and `404` aren't retried at this immediate HTTP layer.



### Adaptor-level retry (fast network recovery)

Between the HTTP call and the command-level schedule, an intermediate retry layer in the CRM adaptor (`command_runner.js`) handles failures that don't produce an HTTP response at all, or that match specific transient messages:

  * Immediate re-queue: Triggered by TCP/socket-level errors - `ECONNRESET`, `ENOTFOUND`, `ESOCKETTIMEDOUT`, `ETIMEDOUT`, `ECONNREFUSED`, `EHOSTUNREACH`, `EPIPE`, `EAI_AGAIN`. These are network failures that occur before an HTTP response is received.

  * 30-second delayed retry: Triggered when the error message is `"Too Early"` (HTTP 425), `"Service Unavailable"`, or `"Unordered Collection"`.

  * Non-retriable at this layer: Everything else falls through to the command-level retry schedule (Layer 3).




#### Why this matters for integrators

These errors occur when the platform can't establish or maintain a TCP connection to your endpoint - meaning they often indicate a problem at your server (server down, refusing connections, or dropping the connection mid-request), not just internal infrastructure. The practical effect is that some network failures recover much faster than the 7-day command-level schedule — often within seconds.

### Command-level retries (~7 days, 14 attempts)

If an operation fails and can be retried, the platform may retry it up to 14 times over approximately 7 days, using this schedule:
    
    
      10s → 1m → 5m → 30m → 1h → 6h → 6h → 12h → 1d → 1d → 1d → 1d → 1d → 1d
    

This long-tail retry behavior can apply to:

  * Account operations.

  * Record operations.

  * Post-session operations.




### Non-retriable failures

Some failures are treated as non-retriable, for example:

  * Configuration or validation failures (for example, required endpoints aren't configured or misconfigured).

  * Certain internal error categories detected by the platform.




If you need to ensure a failure is treated as permanent (no retries), contact support or your implementation team to confirm the correct way to indicate a non-retriable failure in your specific setup.

### Timeouts and network failures

The platform handles two distinct paths:

  1. Application-level timeouts: When the configured HTTP timeout is exceeded (the request was sent but no response was received), the platform raises an internal error that can be retried at the command level (Layer 3). This means the request follows the standard backoff schedule (up to 14 retries over ~7 days).

  2. TCP/socket-level errors: When the connection fails at the network level before an HTTP response is received (for example, `ETIMEDOUT`, `ESOCKETTIMEDOUT`, and `ECONNREFUSED`), the adaptor layer (Layer 2) catches these and immediately re-queues the command. Recovery from these failures is typically much faster - often within seconds rather than following the 7-day schedule.




#### Why the distinction matters

  * An application timeout (your server accepted the connection but didn't respond in time) retries more slowly.

  * A network-level failure (your server couldn't be reached at all) retries much faster.

  * In both cases, the request may have been partially processed, so endpoints should be idempotent — see Building resilient endpoints (idempotency and design tips).




## Status code and timeout behavior matrix (with examples)

The following tables and examples describe how CCAI Platform handles different HTTP status codes, timeouts, and network failures.

### Outcome summary table

The ID-related rows in the following table only apply to endpoints that are configured to extract an ID from the response, such as lookup or create endpoints. Most other endpoints don't perform response ID extraction.

Outcome | Examples | Immediate HTTP retry? | Long-tail retries (~7 days)? | Downstream impact  
---|---|---|---|---  
**Success for an ID-extracting endpoint** | `2xx` \+ expected ID present in the configured response location. | No | No | Downstream proceeds with the extracted ID.  
**Lookup with no match** | `2xx` but no record found at the configured location. | No | No | Normal "not found" behavior. With `skip_account_creation` or `skip_record_creation` enabled, downstream intentionally proceeds with null IDs.  
**Create returning`2xx` without an ID** | `2xx` from a create endpoint, but the new record's ID is missing at the configured location. | No | No | Downstream may proceed with missing data. Treat as a configuration or response-contract issue.  
**Success from a non-ID extracting endpoint** | `2xx` from endpoints such as note, update, or attachment actions that don't extract IDs. | No | No | Downstream proceeds according to the command chain and instance configuration.  
**Transient-ish error** | `408`, `413`, `429`, `500`, `502`, `503`, `504`, `521`, `522`, and `524`. | Yes (two total attempts) | Often yes | Downstream steps may be **delayed** while retries occur.  
**Other errors** | `400`, `401`, `403`, `404`, and other `4xx`/`5xx`. | No | Often yes | Downstream steps may be **delayed** while retries occur.  
**Config/validation failure** | misconfiguration, missing endpoints. | N/A | No | Chain may stop or partially complete depending on configuration.  
**Network-level failure (TCP/socket)** | `ECONNRESET`, `ENOTFOUND`, `ESOCKETTIMEDOUT`, `ETIMEDOUT`, `ECONNREFUSED`, `EHOSTUNREACH`, `EPIPE`, and `EAI_AGAIN`. | N/A | No (handled by adaptor Layer 2) | Adaptor immediately re-queues; recovery is typically fast (seconds). Downstream steps may be briefly **delayed**.  
**Application-level timeout** | `HTTP timeout exceeded` (no response received). | N/A | Often yes (Layer 3) | Downstream steps may be **delayed** while command-level retries occur.  
**Note:** **Often yes** means that retries typically occur unless the failure is classified as non-retriable.

## Worked example with minimal generic API configuration

A baseline custom CRM generic API setup with the three endpoints exercised by the chain: find or create contact, find or create ticket, and a post-session comment. Use this as a starting point and adapt to your CRM specifics.

### Instance-level settings
    
    
    {
      "lookup_method": "genericApi",
      "auth_method": "basic",
      "basic_auth_username": "ccai-integration",
      "basic_auth_password": "<secret>",
      "api_request_timeout": 10,
      "case_lookup_url": "https://crm.example.com/api/cases/{RECORD_ID}",
      "contact_lookup_url": "https://crm.example.com/api/contacts/{ACCOUNT_ID}",
      "skip_account_lookup": false,
      "skip_account_creation": false,
      "skip_record_creation": false
    }
    

### Response shapes

Your CRM's response shape is customer-specific. `response_data_location` is a lodash-style path that reaches the relevant object inside the parsed response body. There is no requirement to wrap responses in a top-level `data` field - the following examples show realistic flat shapes by default.

For example, a CRM that nests resources under `data.contact` would set `response_data_location: "data.contact"` and a response body of `{ "contact": { "id": "c_99812" } }`; the rest of the configuration is unchanged.

### Endpoint 1 - `contact_find_endpoint`

Looks up a contact by phone number or email.
    
    
    {
      "request_url": "https://crm.example.com/api/contacts/search?phone={PHONE_NUMBER}&email={EMAIL}",
      "request_method": "GET",
      "request_parameters": {},
      "response_data_location": "data"
    }
    

#### Success: Contact found
    
    
    200 OK
    Content-Type: application/json
    { "id": "c_42018", "first_name": "Jane", "last_name": "Doe" }
    

#### Contact not found
    
    
    404 Not Found
    

The platform treats `404` as "not found" (not an error). If `skip_account_creation` is false, the flow proceeds to `contact_create_endpoint`.

#### Alternative not found pattern: also valid
    
    
    200 OK
    {}
    

Some CRMs return `200 OK` with empty data instead of `404` when no record matches. The platform handles both equivalently - both trigger the next step (creation, if enabled).

#### Transient failure
    
    
    503 Service Unavailable
    }
    

Triggers Layer 1 immediate HTTP retry (2 total attempts). If still failing, falls through to Layer 3 command-level retries.

### Endpoint 2 - `contact_create_endpoint`

Creates a contact. The `custom_id_location` field tells the platform where to find the new contact's ID inside the response.
    
    
    {
      "request_url": "https://crm.example.com/api/contacts",
      "request_method": "POST",
      "request_parameters": {
        "first_name": "{FIRST_NAME}",
        "last_name": "{LAST_NAME}",
        "email": "{EMAIL}",
        "phone": "{PHONE_NUMBER}",
        "external_session_id": "{SESSION_TYPE}-{SESSION_ID}"
      },
      "response_data_location": "data",
      "custom_id_location": "id"
    }
    

#### Successful creation
    
    
    201 Created
    { "id": "c_99812", "first_name": "John", "last_name": "Doe" }
    

#### 2xx but missing ID at the configured location
    
    
    200 OK
    {}
    

The endpoint returned `200 OK` with no `id` at the configured location. The platform logs a warning and forwards a null `contact_id` downstream (no exception thrown, no retry). Treat this as a configuration smell — `response_data_location` and `custom_id_location` should reliably yield an ID for any `2xx` your endpoint returns from this path.

### Endpoint 3 - `case_create_endpoint`

Creates a ticket. The `contact_id` from the previous step is available as `{ACCOUNT_ID}`.
    
    
    {
      "request_url": "https://crm.example.com/api/cases",
      "request_method": "POST",
      "request_parameters": {
        "subject": "{TICKET_SUBJECT}",
        "description": "{TICKET_DESCRIPTION}",
        "contact_id": "{ACCOUNT_ID}",
        "channel": "{CHANNEL}",
        "external_session_id": "{SESSION_TYPE}-{SESSION_ID}"
      },
      "response_data_location": "data",
      "custom_id_location": "id"
    }
    

**Note:** `{ACCOUNT_ID}` is optional in the payload. If empty (for example, under `skip_account_creation` configurations), the field is automatically dropped from the outgoing request rather than sent as `null` or empty string.

#### Successful creation
    
    
    201 Created
    { "id": "case_77103", "status": "new" }
    

With `response_data_location: "data"`, the platform resolves the path to the parsed response body. It then reads the field at `custom_id_location: "id"` → `ticket_id = "case_77103"`, which flows to post-session.

### Endpoint 4 - `case_comment_endpoint`

This endpoint adds a session summary comment to the ticket after the call or chat ends. The `RECORD_ID` variable carries the `ticket_id` produced by step 3.
    
    
    {
      "request_url": "https://crm.example.com/api/cases/{RECORD_ID}/comments",
      "request_method": "POST",
      "request_parameters": {
        "body": "{COMMENT_BODY}",
        "agent_email": "{AGENT_EMAIL}",
        "channel": "{CHANNEL}",
        "duration": "{CALL_DURATION}",
        "external_session_id": "{SESSION_TYPE}-{SESSION_ID}"
      }
    }
    

**Note:** The preceding `external_session_id` field demonstrates the composite key pattern from Building resilient endpoints (idempotency and design tips) \- your endpoint can detect that this comment for `call-12345` has already been delivered and avoid creating a duplicate if the platform retries.

For generic API instances with `case_lookup_url` configured, the platform won't dispatch this endpoint until the ticket creation step completes successfully - so missing `RECORD_ID` here means a configuration issue, not a transient state.

### Variation: account creation disabled

This example is very similar to the previous one given for a minimal generic API configuration, except here your instance doesn't permit creating contacts in the CRM. While account lookup runs, creation doesn't.

#### Instance settings change
    
    
    {
      "skip_account_creation": true,
      "skip_account_lookup": false
    }
    

The instance settings changes include these behaviors:

  * The account step calls `contact_find_endpoint` only. If no contact is found, it doesn't call `contact_create_endpoint`.

  * The record step receives a null `contact_id`. The platform proceeds to ticket creation without a `contact_id` \- `{ACCOUNT_ID}` resolves to empty, and the `contact_id` field is dropped from your `case_create_endpoint` payload entirely.

  * This means your ticket-creation endpoint must be able to create tickets without a `contact_id` in this configuration. If your CRM requires an associated contact for every ticket, this configuration is incompatible.




#### Defensive pattern in `case_create_endpoint`

Without a `contact_id`, your CRM has less context about the caller than it would normally. You can use the `=DEFAULT_VALUE` helper to capture whatever identifying information _is_ available in the request and pass it as a fallback signal:
    
    
    "request_parameters": {
      "subject": "{TICKET_SUBJECT}",
      "contact_id": "{ACCOUNT_ID}",
      "contact_origin": "=DEFAULT_VALUE(\"{EMAIL}\", \"{PHONE_NUMBER}\", \"anonymous\")"
    }
    

The `=DEFAULT_VALUE` helper picks the first non-empty value, so your CRM receives an email or phone number when one is available, and the literal string `"anonymous"` only when neither is - useful for flagging tickets that have no identifying contact info attached.

### Variation: lookup-only ticket flow (no record creation)

Account operations run normally, but ticket creation is disabled. The integration only attaches comments to _existing_ tickets surfaced by lookup.

#### Instance settings change
    
    
    {
      "skip_record_creation": true,
      "case_lookup_url": "https://crm.example.com/api/cases/{RECORD_ID}"
    }
    

The changes encompass these behaviors:

  * The record step calls `case_find_endpoint` and uses the returned ticket. If no ticket is found, the chain stops at the record step - `case_create_endpoint` isn't invoked.

  * Post-session endpoints (`case_comment_endpoint`, `case_update_endpoint`, and similar) are only dispatched when a ticket was successfully looked up. The Rails-side `ready?` guard ensures these commands stay queued (and eventually expire) if no `ticket_id` ever materializes.

  * Practical implication: in this configuration, your post-session endpoints will _only_ receive sessions that were tied to a known ticket. You don't need to handle the `"missing ticket_id"` branch.




### Recommended idempotency key in practice

The platform exposes both `SESSION_TYPE` and `SESSION_ID` as template variables. The cleanest way to apply the composite key pattern is to bake it directly into every relevant request body - your endpoints then have the canonical key to work with, with no additional logic on your side:
    
    
    "request_parameters": {
      "...your fields...": "...",
      "ccai_session_key": "{SESSION_TYPE}-{SESSION_ID}"
    }
    

For the same call, every retry of every endpoint in the chain (account > record > post-session) will produce the same `ccai_session_key`. Use it as the deduplication anchor in your CRM's create or upsert logic — for example, an upsert on (`ccai_session_key`, `endpoint_kind`) will safely absorb retries without producing duplicate records.

## Building resilient endpoints (idempotency and design tips)

Because requests may be repeated (immediate retry + retries over days), your endpoints should be idempotent:

  * Use a stable composite interaction identifier as your idempotency key:

    * Combine the session type with the session ID, for example, `call-12345` or `chat-12345`.

    * Don't rely on `call_id` or `chat_id` alone. Voice and chat IDs can overlap because each sequence can start at 1.

  * If you receive what appears to be a duplicate request:

    * Examine the payload to determine whether it is truly a duplicate. Some shared endpoints, such as comment or note endpoints, can be used by multiple command types.

    * For create operations, duplicate requests shouldn't occur under normal successful conditions, but they can occur if the CRM processed the request and then returned an error or timed out before the platform received a successful response.

    * When a duplicate create request is confirmed, return the previously created record ID instead of another record.

  * Handle missing IDs explicitly:

    * A missing `contact_id` on ticket creation usually indicates a configuration where account lookup or account creation is disabled. If your instance requires accounts, investigate it instead of silently creating tickets without contacts.

    * A missing `ticket_id` on post-session calls isn't expected for typical generic API setups where ticket lookup is configured. Check ticket lookup configuration and payload templates before treating the request as a normal no-op.

  * For updates, prefer setting fields to specific values rather than incrementing counters, so repeated calls are safe.




## Troubleshooting and observability

When you are debugging a custom CRM integration, keep these patterns in mind:

  * Repeated calls to the same endpoint:

    * Compare timestamps against the retry schedule in Command-level retries (~7 days, 14 attempts).

    * Correlate events by using the composite session identifier, such as session type + call or chat session ID.

    * CCAI Platform exported logs can help show the call or chat session ID alongside API events for traceability.

    * Check whether your endpoint is consistently returning an error that can be retried (for example, `500`) instead of a non-retriable configuration failure.

  * Retries that "won't stop":

    * Inspect the error responses your endpoint is returning.

    * If you intended a permanent failure, contact support for guidance on how to indicate a non-retriable error for your configuration.

  * Endpoint was never called:

    * Verify that:

      * Upstream steps (account/record) completed successfully and produced the necessary IDs.

      * The endpoint is correctly configured and enabled in your custom CRM settings.

    * A misconfigured or disabled endpoint, or a failure earlier in the chain, can prevent certain steps from running.

  * Correlating logs:

    * Log the full request and response on your side, including the interaction ID (`call_id` / `chat_id`).

    * Use that ID to correlate your CRM logs with the platform's behavior over time (especially during retries).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
