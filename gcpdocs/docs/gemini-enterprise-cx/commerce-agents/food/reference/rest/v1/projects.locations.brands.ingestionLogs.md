---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs
title: REST Resource: projects.locations.brands.ingestionLogs \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:00:18.690632+00:00
---

# REST Resource: projects.locations.brands.ingestionLogs  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  REST Resource: projects.locations.brands.ingestionLogs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: IngestionLog
    * JSON representation
  * State
  * IngestionPhase
    * JSON representation
  * Phase
  * State
  * IngestionType
  * Methods



## Resource: IngestionLog

A record of a menu ingestion run.

JSON representation  
---  
      
    
    {
      "name": string,
      "store": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#State)),
      "startTime": string,
      "endTime": string,
      "phases": [
        {
          object ([IngestionPhase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#IngestionPhase))
        }
      ],
      "ingestionType": enum ([IngestionType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#IngestionType))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the ingestion log. Format: projects/{project}/locations/{location}/brands/{brand}/ingestionLogs/{ingestionLog}  
`store` |  `string` Optional. The resource name of the store for the ingestion. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#State)`)` Output only. Data about the current state of the ingestion.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when ingestion job started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when ingestion job finished.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`phases[]` |  `object (`[IngestionPhase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#IngestionPhase)`)` Output only. List of phase runtimes.  
`ingestionType` |  `enum (`[IngestionType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#IngestionType)`)` Optional. Immutable. The type of the ingestion run.  
  
## State

The status of the ingestion run.

Enums  
---  
`STATE_UNSPECIFIED` | The status is unspecified.  
`SUCCEEDED` | The ingestion was successful.  
`FAILED` | The ingestion failed.  
`PROCESSING` | The ingestion is being processed.  
  
## IngestionPhase

A phase of the ingestion run.

JSON representation  
---  
      
    
    {
      "phase": enum ([Phase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#Phase)),
      "startTime": string,
      "endTime": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#State_1)),
      "details": string
    }  
  
Fields  
---  
`phase` |  `enum (`[Phase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#Phase)`)` Required. Name of the phase.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Start time of the phase.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. End time of the phase.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs#State_1)`)` Optional. State of the phase. Set by the caller on append, so it's an input, not a resource state.  
`details` |  `string` Optional. Details about the phase.  
  
## Phase

Enum for the name of the phase.

Enums  
---  
`PHASE_UNSPECIFIED` | The phase is unspecified.  
`READ_SOURCE_MENU` | Reading the source menu.  
`PARSE_SOURCE_MENU` | Parsing the source menu.  
`BRAND_SPECIFIC_VALIDATION` | Validating the brand specific configuration.  
`BRAND_AGNOSTIC_VALIDATION` | Validating the brand agnostic configuration.  
`CREATE_MENU` | Creating the menu.  
  
## State

The execution state of the phase.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unspecified.  
`SUCCEEDED` | The phase completed successfully.  
`FAILED` | The phase failed.  
  
## IngestionType

The type of the ingestion run.

Enums  
---  
`INGESTION_TYPE_UNSPECIFIED` | The ingestion type is unspecified.  
`MENU_UPDATE` | A regular menu update.  
`PRODUCT_OUTAGE_UPDATE` | A product outage update (e.g., product out of stock).  
  
## Methods  
  
---  
  
### `[appendIngestionPhase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs/appendIngestionPhase)`

|  Appends an ingestion phase to an ingestion log.  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs/create)`

|  Creates an ingestion log.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs/delete)`

|  Deletes the specified ingestion log.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs/get)`

|  Gets an ingestion log.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.ingestionLogs/list)`

|  Lists ingestion logs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
