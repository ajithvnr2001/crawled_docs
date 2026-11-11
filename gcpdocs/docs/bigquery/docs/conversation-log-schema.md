---
url: https://docs.cloud.google.com/bigquery/docs/conversation-log-schema/
title: Conversation log schema \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:23:29.704017+00:00
---

# Conversation log schema  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/conversation-log-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Conversation log schema

This document describes the table layout, columns, event types, user identity fields, and JSON payload structure for conversational analytics conversation logging in BigQuery. For an overview of how conversation logging works, see [Conversation logging overview](https://docs.cloud.google.com/bigquery/docs/conversation-logging-overview).

## Table layout and auto-creation

Create the destination dataset in the same project as the data agent before enabling logging; the Conversational Analytics API service agent creates the table in the dataset's location on the first logged turn (or adds any missing schema columns to an existing compatible table). The auto-created table is partitioned by day on `timestamp` (inheriting any default partition expiration on the dataset) and clustered on `event_type`, `agent`, and `user_id`. Always filter on `timestamp` when you query the table.

## Columns

The following table describes the columns in the conversation logging destination table.

Column | Type | Mode | Contents  
---|---|---|---  
`timestamp` | `TIMESTAMP` | `REQUIRED` | UTC time of the event. Partitioning column.  
`event_id` | `STRING` | `NULLABLE` | Unique ID for the event. It stays the same if a write is retried, so you can use it to remove duplicates.  
`event_type` | `STRING` | `NULLABLE` | Kind of event. See [Event types](https://docs.cloud.google.com/bigquery/docs/conversation-log-schema#conversation-logging-event-types).  
`agent` | `STRING` | `NULLABLE` | The agent type, not your agent's name or ID (for example, `ConversationalAnalyticsAgent`). To tell agents apart, use the data agent ID (see [Fields inside `attributes`](https://docs.cloud.google.com/bigquery/docs/conversation-log-schema#conversation-logging-attributes)).  
`session_id` | `STRING` | `NULLABLE` | One turn, not a whole conversation. All events for one question and its answer share a `session_id`. To group turns into conversations, use the conversation ID in `attributes`.  
`invocation_id` | `STRING` | `NULLABLE` | One execution within a turn.  
`user_id` | `STRING` | `NULLABLE` | The caller who asked the question. See [User identity](https://docs.cloud.google.com/bigquery/docs/conversation-log-schema#conversation-logging-user-identity).  
`trace_id` | `STRING` | `NULLABLE` | OpenTelemetry trace ID (32 hexadecimal characters).  
`span_id` | `STRING` | `NULLABLE` | ID of this operation in the turn's execution tree.  
`parent_span_id` | `STRING` | `NULLABLE` | ID of the parent operation.  
`content` | `JSON` | `NULLABLE` | Event payload. Its shape depends on `event_type`.  
`content_parts` | `RECORD` | `REPEATED` | Multi-part content, with one element per part (for example, `mime_type`, `uri`, `object_ref`, `text`, `part_index`, `part_attributes`, and `storage_mode`).  
`attributes` | `JSON` | `NULLABLE` | Metadata: data agent ID, conversation ID, internal user key, model version, and detailed token usage.  
`latency_ms` | `JSON` | `NULLABLE` | Latency measurements, such as `total_ms` and `time_to_first_token_ms`.  
`status` | `STRING` | `NULLABLE` | `OK` or `ERROR`.  
`error_message` | `STRING` | `NULLABLE` | Error details. It can also be set on `OK` `LLM_RESPONSE` rows when the model stops for a reason other than a normal stop (for example, when it reaches the maximum token limit).  
`is_truncated` | `BOOLEAN` | `NULLABLE` | `true` if any text value in the event exceeded 512,000 characters (`500 * 1,024`) and was cut. Cut values end with `...[TRUNCATED]`. The removed part can't be recovered.  
  
## Event types

The following table describes the values that can appear in the `event_type` column and the columns or JSON fields that store the data for each event.

`event_type` value | Description | Populated columns and JSON fields  
---|---|---  
`INVOCATION_STARTING` | Start of a turn. | None  
`USER_MESSAGE_RECEIVED` | The user's question. | `content.text_summary`  
`AGENT_RESPONSE` | The agent's answer, as a structured object. | `content.text_summary` (plain text) and `content.response` (see [Structure of `AGENT_RESPONSE`](https://docs.cloud.google.com/bigquery/docs/conversation-log-schema#conversation-logging-agent-response))  
`LLM_RESPONSE` | One row for each model call, including calls that requested a tool (not written when a turn is answered directly from a verified query, where `attributes.fast_path` is `true`). The model's output isn't stored. | 

  * Tokens: `content.usage.prompt`, `content.usage.completion`, and `content.usage.total`.
  * Detailed token usage: `attributes.usage_metadata`, including `tool_use_prompt_token_count`, `thoughts_token_count`, and `cached_content_token_count`.
  * Total tokens: the `content.usage.total` value equals the `content.usage.prompt` \+ `tool_use_prompt_token_count` \+ `content.usage.completion` \+ `thoughts_token_count` values, with the `cached_content_token_count` value included in the `content.usage.prompt` value. For more information, see [Fields inside `attributes`](https://docs.cloud.google.com/bigquery/docs/conversation-log-schema#conversation-logging-attributes).
  * Model: `attributes.model_version`.
  * Finish reason: `attributes.finish_reason`.

  
`INVOCATION_COMPLETED` | End of a turn, with per-turn latency. `content` is empty. | `latency_ms.total_ms`  
`EMBEDDING_SUGGESTION` | Suggestions for the agent owner about columns that could benefit from embeddings. It appears only for some agents. | `content.reason`, `content.suggested_columns`  
`INVOCATION_ERROR`, `AGENT_ERROR`, `LLM_ERROR` | Failed turn. `status` is `ERROR` and `content` is `NULL`. | `error_message` (one-line summary with SQL statements and table names redacted)  
  
## User identity

The `user_id` column contains the caller's email address: the user's email address, a service account's email address when an API caller authenticates with a service account, or `NULL` if the caller has no email address (such as some Workforce Identity Federation identities). An internal user key is also recorded in `attributes.session_metadata.user_id` on every row, so you can count distinct users with `internal_user_key` (see [Create the cross-agent events view](https://docs.cloud.google.com/bigquery/docs/analyze-conversation-logs#recipe-cross-agent-events-view)).

To attribute turns to your own end users when you call the API through a service account, record the user mapping in your application. The API doesn't accept an end-user identifier for logging.

## Fields inside `attributes`

The following table shows the GoogleSQL expressions used to extract metadata fields from the `attributes` JSON column.

What you need | GoogleSQL expression  
---|---  
Data agent ID | `JSON_VALUE(attributes, '$.session_metadata.state."data-agent-id"')`  
Data agent full resource name | `JSON_VALUE(attributes, '$.adk.app_name')`  
Conversation ID | `JSON_VALUE(attributes, '$.session_metadata.state."conversation-id"')`  
Internal user key | `JSON_VALUE(attributes, '$.session_metadata.user_id')`  
Model version (on `LLM_RESPONSE` rows) | `JSON_VALUE(attributes, '$.model_version')`  
Tool-use prompt tokens (on `LLM_RESPONSE` rows) | `SAFE_CAST(JSON_VALUE(attributes, '$.usage_metadata.tool_use_prompt_token_count') AS INT64)`  
Thinking tokens (on `LLM_RESPONSE` rows) | `SAFE_CAST(JSON_VALUE(attributes, '$.usage_metadata.thoughts_token_count') AS INT64)`  
Cached prompt tokens (on `LLM_RESPONSE` rows) | `SAFE_CAST(JSON_VALUE(attributes, '$.usage_metadata.cached_content_token_count') AS INT64)`  
  
On `LLM_RESPONSE` rows, token counts split into the input tokens and the output tokens that add up to the `content.usage.total` value:

  * **Input tokens** : the `content.usage.prompt` value plus the `attributes.usage_metadata.tool_use_prompt_token_count` value, which counts tokens from tool execution results that are sent back to the model as input. If you use context caching, the `attributes.usage_metadata.cached_content_token_count` value is already included in the `content.usage.prompt` value.

  * **Output tokens** : the `content.usage.completion` value plus the `attributes.usage_metadata.thoughts_token_count` value, which counts reasoning tokens generated by thinking models.

  * **Total tokens** : the `content.usage.total` value equals the `content.usage.prompt` \+ `tool_use_prompt_token_count` \+ `content.usage.completion` \+ `thoughts_token_count` values. Optional `usage_metadata` fields are omitted or `null` when a model call doesn't use them. Wrap extracted counts in `COALESCE(..., 0)` before adding row values together (such as `prompt` \+ `completion`) or to prevent aggregate functions like `SUM(...)` from producing `null`. For an example query, see [Token use by model and by agent](https://docs.cloud.google.com/bigquery/docs/analyze-conversation-logs#recipe-token-use-by-model).




## Structure of `AGENT_RESPONSE`

To read the agent's answer as plain text, use `JSON_VALUE(content, '$.text_summary')`. It combines the answer's Markdown, assumption, and insight parts, and any clarifying questions. In `AGENT_RESPONSE` rows, `content.response` is a JSON object, not a string, so `JSON_VALUE(content, '$.response')` returns `NULL`.

The following table describes the paths under `content.response`.

Path under `content.response` | Type | Contents  
---|---|---  
`parts` | `ARRAY<JSON>` | The answer, in parts.  
`parts[].markdown` | `STRING` | Answer text (Markdown).  
`parts[].insight` | `STRING` | An insight drawn from the data.  
`parts[].assumption` | `STRING` | An assumption that the agent made.  
`parts[].data_result_artifact_name` | `STRING` | Name of a data result.  
`parts[].chart_artifact_name` | `STRING` | Name of a chart.  
`followup_questions` | `ARRAY<STRING>` | Suggested follow-up questions.  
`clarifying_question` | `STRING` | Set when the agent asked the user a clarifying question instead of answering.  
`citation_sources` | `JSON` | Sources cited in the answer.  
  
## What's next

  * [Analyze conversation logs](https://docs.cloud.google.com/bigquery/docs/analyze-conversation-logs).

  * [Read the conversation logging overview](https://docs.cloud.google.com/bigquery/docs/conversation-logging-overview).

  * [Create and configure data agents](https://docs.cloud.google.com/bigquery/docs/create-data-agents#configure_settings).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
