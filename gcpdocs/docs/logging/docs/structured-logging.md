---
url: https://docs.cloud.google.com/logging/docs/structured-logging/
title: Structured logging \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T10:53:37.082510+00:00
---

# Structured logging  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/structured-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Structured logging Stay organized with collections  Save and categorize content based on your preferences. 

In Cloud Logging, a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object can store a log payload as either structured data or unstructured text. A _structured_ log entry stores its payload as a JSON object in the `jsonPayload` field, whereas an _unstructured_ log entry stores its payload as a string in the `textPayload` field.

Formatting your log payload as a JSON object lets you query by JSON paths in the Logs Explorer, query individual fields on the [Observability Analytics](https://docs.cloud.google.com/logging/docs/log-analytics) page, and [index specific fields](https://docs.cloud.google.com/logging/docs/analyze/custom-index) to speed up queries. With unstructured logs, you can search the text string, but you can't query or index individual keys.

## How structured logs are written

How structured log entries are written to Logging depends on your environment and how your logs are collected:

  * **[OpenTelemetry](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach) and the Telemetry (OTLP) API**: When you send OpenTelemetry Protocol (OTLP) log records to Logging, Google Cloud Observability converts structured log data into the `jsonPayload` field. See [OTLP log record to log entry mapping](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/otlp-log-record-to-log-entry).


  * **Built-in logging agents** : In managed compute environments (such as Google Kubernetes Engine and Cloud Run), built-in agents parse single-line JSON written to `stdout` or `stderr` into the `jsonPayload` field. See [Choose a logging framework](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach#logging-frameworks).
  * **[Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent)** : On Compute Engine VMs, the agent writes structured logs when it collects JSON logs or parses text logs. See [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration).


  * **[Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries)** : These libraries write structured logs when you pass a JSON object or map as the payload, or when they output single-line JSON to `stdout` or `stderr`. See [Writing structured logs](https://docs.cloud.google.com/logging/docs/samples/logging-write-log-entry).


  * **Google Cloud CLI or the Logging API**: You can run [`gcloud logging write`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/write) with the `--payload-type=json` flag ([example](https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud)), or call the [`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write) API method with a `jsonPayload` object.


  * **BindPlane** : This service sends logs with JSON payloads from on-premises or hybrid sources to Logging. See the [BindPlane quickstart guide](https://bindplane.com/docs/getting-started/quickstart-guide).



## Special JSON fields in structured payloads

When logging agents ingest structured logs, they can map specific fields in your log data to top-level fields in the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object instead of leaving them in `jsonPayload`:

  * **Ops Agent** : For the JSON fields that the Ops Agent maps automatically when you use the `parse_json` processor or the `tcp` and `fluent_forward` receivers, see [Special fields in structured payloads](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#special-fields).

  * **OpenTelemetry (OTLP)** : For information about how Google Cloud Observability maps OTLP log records to `LogEntry` fields, see [OTLP log record to log entry mapping](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/otlp-log-record-to-log-entry).

  * **Built-in logging agents (`stdout` and `stderr`)**: On managed compute platforms such as Google Kubernetes Engine, Cloud Run, Cloud Run functions, and App Engine, the built-in logging agent recognizes the following top-level JSON keys and moves their values into the corresponding `LogEntry` fields:

    * `severity`: Sets the [`LogEntry.severity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.severity) field.
    * `message`: Sets the main log message displayed in the Logs Explorer.
    * `httpRequest`: Sets the [`LogEntry.httpRequest`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest) field.
    * `time` or `timestamp` (or `timestampSeconds` and `timestampNanos`): Sets the [`LogEntry.timestamp`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.timestamp) field.
    * `logging.googleapis.com/insertId`: Sets the `LogEntry.insertId` field.
    * `logging.googleapis.com/labels`: Sets user-defined `LogEntry.labels` key-value pairs.
    * `logging.googleapis.com/operation`: Sets the [`LogEntry.operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogEntryOperation) field.
    * `logging.googleapis.com/sourceLocation`: Sets the `LogEntry.sourceLocation` field.
    * `logging.googleapis.com/trace`, `logging.googleapis.com/spanId`, and `logging.googleapis.com/trace_sampled`: Set the `trace`, `spanId`, and `traceSampled` fields for [linking logs with traces](https://docs.cloud.google.com/trace/docs/trace-log-integration).

Any remaining fields in the JSON record stay in the `LogEntry.jsonPayload` field.




## What's next

  * To choose an instrumentation strategy for your compute platform, see [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).


  * To query and view log entries, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  * To read log entries by using the gcloud CLI, see [Reading log entries](https://docs.cloud.google.com/logging/docs/api/gcloud-logging#reading_log_entries).

  * To read log entries by using the Logging API, see the [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
