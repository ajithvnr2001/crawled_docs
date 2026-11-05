---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions
title: REST Resource: projects.locations.apps.assistantSessions \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:28:06.388384+00:00
---

# REST Resource: projects.locations.apps.assistantSessions  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.assistantSessions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AssistantSession
    * JSON representation
  * AssistantMessage
    * JSON representation
  * AssistantChunk
    * JSON representation
  * TypedPayload
    * JSON representation
  * AssistantSessionState
  * UserResponseSuggestions
    * JSON representation
  * AssistantSessionArtifact
    * JSON representation
  * SessionCheckpoint
    * JSON representation
  * ActiveTurnInfo
    * JSON representation
  * ActiveTurnInfo.Status
  * Methods



## Resource: AssistantSession

An assistant session represents a conversation between a user and the assistant agent.

JSON representation  
---  
      
    
    {
      "name": string,
      "requestor": string,
      "messages": [
        {
          object ([AssistantMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantMessage))
        }
      ],
      "state": enum ([AssistantSessionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantSessionState)),
      "createTime": string,
      "updateTime": string,
      "userResponseSuggestions": {
        object ([UserResponseSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#UserResponseSuggestions))
      },
      "displayName": string,
      "artifacts": [
        {
          object ([AssistantSessionArtifact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantSessionArtifact))
        }
      ],
      "sessionCheckpoint": {
        object ([SessionCheckpoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#SessionCheckpoint))
      },
      "activeTurn": {
        object ([ActiveTurnInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#ActiveTurnInfo))
      },
      "touchedApps": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The unique identifier of the session. Format: `projects/{project}/locations/{location}/apps/{app}/assistantSessions/{session}`  
`requestor` |  `string` Output only. The user who initiated the session.  
`messages[]` |  `object (`[AssistantMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantMessage)`)` Optional. History of messages in the session.  
`state` |  `enum (`[AssistantSessionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantSessionState)`)` Output only. The status of the assistant session.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the assistant session was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the assistant session was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`userResponseSuggestions` |  `object (`[UserResponseSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#UserResponseSuggestions)`)` Output only. Suggested user responses from the assistant agent.  
`displayName` |  `string` Optional. The display name of the assistant session.  
`artifacts[]` |  `object (`[AssistantSessionArtifact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantSessionArtifact)`)` Output only. Document artifacts (e.g. generated TDDs in markdown) produced by the assistant in this session. Pointers only; the file content lives in the customer's Cloud Storage bucket.  
`sessionCheckpoint` |  `object (`[SessionCheckpoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#SessionCheckpoint)`)` Output only. Session checkpoint containing user intent and rolling history summary.  
`activeTurn` |  `object (`[ActiveTurnInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#ActiveTurnInfo)`)` Output only. Attachment info for this session's currently running turn. Unset when no turn is running.  
`touchedApps[]` |  `string` Output only. Apps this session has targeted or changed (project-scoped sessions only), for history tags. Format: `projects/{project}/locations/{location}/apps/{app}`  
  
## AssistantMessage

A message in an assistant session.

JSON representation  
---  
      
    
    {
      "role": string,
      "chunks": [
        {
          object ([AssistantChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantChunk))
        }
      ],
      "eventTime": string,
      "attachedGcsUris": [
        string
      ]
    }  
  
Fields  
---  
`role` |  `string` Required. Role within the conversation "user" or "model".  
`chunks[]` |  `object (`[AssistantChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantChunk)`)` Optional. Content of the message as chunks.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Timestamp when the message was sent or received.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attachedGcsUris[]` |  `string` Optional. Cloud Storage URIs for files uploaded by the user during this turn. This allows attachments to be persisted and rendered in the session history UI. Example: "gs://cxas-transient-uploads/uuid/prd.pdf"  
  
## AssistantChunk

A chunk of data in an assistant message.

JSON representation  
---  
      
    
    {
      "createTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string,
      "thought": string,
      "payload": {
        object
      },
      "typedPayload": {
        object ([TypedPayload](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#TypedPayload))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when the chunk was created or emitted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Data in the chunk. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` Optional. Text data.  
`thought` |  `string` Optional. Thought generated by the model.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Payload which contains structured responses like the quality report, agent version name, suggested responses etc.  
`typedPayload` |  `object (`[TypedPayload](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#TypedPayload)`)` Optional. Typed payload which contains structured responses.  
End of mutually exclusive fields.  
  
## TypedPayload

Payload with a type. Used by the assistant history (`AssistantChunk`) and by the streaming `typedPayload` event; lives here because both assistant_service.proto and session_service.proto need it.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "type": string,
      "value": {
        object
      },
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`displayName` |  `string` Required. The display name of the payload.  
`type` |  `string` Required. The type of the payload.  
`value` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The value of the payload.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The metadata of the payload.  
  
## AssistantSessionState

The status of the assistant session.

Enums  
---  
`ASSISTANT_SESSION_STATE_UNSPECIFIED` | The default value. This value is used if the status is not specified.  
`PROCESSING` | The assistant agent is processing the request as a long running task.  
`IDLE` | The assistant agent is idle and does not have any pending requests or response.  
`PENDING_REVIEW` | The assistant agent is done processing a long running task and has a response ready for the user.  
  
## UserResponseSuggestions

Suggested user responses from the assistant agent.

JSON representation  
---  
      
    
    {
      "suggestions": [
        string
      ]
    }  
  
Fields  
---  
`suggestions[]` |  `string` Required. The assistant suggested user responses. These are suggestions for the user on how to interact with the assistant.  
  
## AssistantSessionArtifact

A document artifact generated by the assistant within a session, stored as a file in the customer's Cloud Storage bucket.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "gcsUri": string,
      "mimeType": string,
      "createTime": string,
      "turnIndex": integer
    }  
  
Fields  
---  
`id` |  `string` Output only. The unique identifier of the artifact within the session.  
`displayName` |  `string` Output only. The file name shown to the user, e.g. "hotel_booking_tdd.md".  
`gcsUri` |  `string` Output only. The Cloud Storage object holding the artifact content. Example: "gs://{project}-agent-assist-artifacts/agent-assist-generated/1_tdd.md"  
`mimeType` |  `string` Output only. The IANA media type of the artifact content, e.g. "text/markdown".  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the artifact was persisted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`turnIndex` |  `integer` Output only. Index of the message in [AssistantSession.messages] whose turn produced the artifact, for placing the artifact chip when history is restored.  
  
## SessionCheckpoint

Session checkpoint containing inferred user intent for session title and UI.

JSON representation  
---  
      
    
    {
      "userIntent": string
    }  
  
Fields  
---  
`userIntent` |  `string` Inferred user goal or topic for the session (e.g. "Building E-Commerce Support Agent").  
  
## ActiveTurnInfo

Live-attachment info for a session turn that is currently running, disconnected from its client, or parked for pickup by another server task.

JSON representation  
---  
      
    
    {
      "turnId": string,
      "status": enum ([ActiveTurnInfo.Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#ActiveTurnInfo.Status)),
      "startTime": string,
      "lastProgressTime": string,
      "orphanDeadlineTime": string
    }  
  
Fields  
---  
`turnId` |  `string` Identifies the turn; echoed by resume snapshots on the streaming API.  
`status` |  `enum (`[ActiveTurnInfo.Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#ActiveTurnInfo.Status)`)` Current attachment status.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the turn started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastProgressTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the turn last persisted progress.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`orphanDeadlineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the turn will be wound down if no client attaches.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ActiveTurnInfo.Status

How the running turn currently relates to clients and server tasks.

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecified.  
`RUNNING` | The turn is executing with at least one client attached.  
`DISCONNECTED` | The turn is executing with no client attached.  
`RESUMING` | The turn is parked for pickup: the next attach continues it.  
`ABANDONED` | The turn's server lease has lapsed and no task is driving it; the next read seals it to a committed partial. Not attachable.  
  
## Methods  
  
---  
  
### `[cancelAssistantTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/cancelAssistantTurn)`

|  Cancels the assistant session's in-flight turn, if any: the explicit user stop for a turn running detached from any stream.  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/create)`

|  Creates a new assistant session in the given app.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/delete)`

|  Deletes the specified assistant session.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/get)`

|  Gets details of the specified assistant session.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/list)`

|  Lists all assistant sessions in the given app.  
  
### `[streamChatAiAssistant](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant)`

|  Runs Arc, the AI assistant, for the specified assistant session in a streaming fashion.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
