---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant/
title: Method: projects.locations.apps.assistantSessions.streamChatAiAssistant \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:48:15.362034+00:00
---

# Method: projects.locations.apps.assistantSessions.streamChatAiAssistant  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.assistantSessions.streamChatAiAssistant Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * AssistantConfirmationResponse
    * JSON representation
  * StreamChatAiAssistantRequest.ClientCapability
  * OperationCompletedEvent
    * JSON representation
  * ArtifactChunk
    * JSON representation
  * ArtifactChunk.State
  * OptionQuestionsChunk
    * JSON representation
  * OptionQuestionsChunk.Question
    * JSON representation
  * OptionQuestionsChunk.Option
    * JSON representation
  * AssistantConfirmationRequest
    * JSON representation
  * AssistantConfirmationRequest.Target
    * JSON representation
  * TurnResumeSnapshot
    * JSON representation
  * TurnHandoffEvent
    * JSON representation
  * TurnHandoffEvent.Reason
  * TurnCompletedEvent
    * JSON representation
  * TurnCompletedEvent.Reason
  * TurnMetadata
    * JSON representation
  * TurnMetadata.ContractStreamingPhase



Runs Arc, the AI assistant, for the specified assistant session in a streaming fashion.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{name=projects/*/locations/*/apps/*/assistantSessions/*}:streamChatAiAssistant`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The assistant session to be used to run the assistant. Format: `projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistantSession}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "message": string,
      "attachedGcsUris": [
        string
      ],
      "contextToken": string,
      "confirmationResponse": {
        object ([AssistantConfirmationResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationResponse))
      },
      "clientCapabilities": [
        enum ([StreamChatAiAssistantRequest.ClientCapability](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#StreamChatAiAssistantRequest.ClientCapability))
      ],
      "operationCompletedEvent": {
        object ([OperationCompletedEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OperationCompletedEvent))
      },
      "resumeFromSequenceNumber": string,
      "attachOnly": boolean
    }  
  
Fields  
---  
`message` |  `string` Optional. The message to send to the assistant agent. May be empty when `confirmationResponse` is set (answering a pending confirmation without adding a new message); at least one of the two must be provided.  
`attachedGcsUris[]` |  `string` Optional. Cloud Storage URIs for files uploaded by the user during this turn. Example: "gs://cxas-transient-uploads/uuid/prd.pdf"  
`contextToken` |  `string` Optional. Opaque onboarding context token returned by `[SessionService.GenerateOnboardingSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#google.cloud.ces.v1beta.SessionService.GenerateOnboardingSuggestions)`. When set and still fresh, the server reuses the onboarding snapshot computed for the zero state instead of recomputing it for the first conversation turn.  
`confirmationResponse` |  `object (`[AssistantConfirmationResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationResponse)`)` Optional. The user's answer to a pending `[AssistantConfirmationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationRequest)`. When set, the server resumes the paused agent with this answer instead of (or in addition to) starting a new prompt turn.  
`clientCapabilities[]` |  `enum (`[StreamChatAiAssistantRequest.ClientCapability](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#StreamChatAiAssistantRequest.ClientCapability)`)` Optional. Response features this client can render. The server only emits events that need a capability (e.g. `confirmationRequest`) when the capability is declared, so older clients never receive events they would silently drop.  
`operationCompletedEvent` |  `object (`[OperationCompletedEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OperationCompletedEvent)`)` Optional. Resumes an assistant session paused waiting for a client-managed long-running operation to complete.  
`resumeFromSequenceNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Optional cursor to resume and replay events from an in-flight or completed turn.  
`attachOnly` |  `boolean` Optional. Optional flag to attach to an existing in-flight turn without submitting a new message.  
  
### Response body

Response message for `[SessionService.StreamChatAiAssistant](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#google.cloud.ces.v1beta.SessionService.StreamChatAiAssistant)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "eventId": string,
      "eventTime": string,
      "uiEvent": {
        object ([UiEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/UiEvent))
      },
      "turnMetadata": {
        object ([TurnMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnMetadata))
      },
      "sequenceNumber": string,
      "turnInProgress": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "textChunk": string,
      "status": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Status))
      },
      "thoughtChunk": string,
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse))
      },
      "artifactChunk": {
        object ([ArtifactChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#ArtifactChunk))
      },
      "optionQuestionsChunk": {
        object ([OptionQuestionsChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OptionQuestionsChunk))
      },
      "confirmationRequest": {
        object ([AssistantConfirmationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationRequest))
      },
      "sessionCheckpoint": {
        object ([SessionCheckpoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#SessionCheckpoint))
      },
      "resumeSnapshot": {
        object ([TurnResumeSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnResumeSnapshot))
      },
      "handoff": {
        object ([TurnHandoffEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnHandoffEvent))
      },
      "turnCompleted": {
        object ([TurnCompletedEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnCompletedEvent))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`eventId` |  `string` Unique identifier for the event.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the event occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uiEvent` |  `object (`[UiEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/UiEvent)`)` Optional. UI event payload.  
`turnMetadata` |  `object (`[TurnMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnMetadata)`)` Optional. Turn-level metadata and intent categorization.  
`sequenceNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Monotonically increasing sequence number for this session turn.  
`turnInProgress` |  `boolean` Optional. Indicates whether the turn is still actively running in the background.  
The event payload. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`textChunk` |  `string` Text Token (for streaming Gemini responses word-by-word).  
`status` |  `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Status)`)` Simple status update.  
`thoughtChunk` |  `string` Thought text chunk (agent's reasoning before generating response).  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall)`)` Tool call execution event.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse)`)` Tool call response event.  
`artifactChunk` |  `object (`[ArtifactChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#ArtifactChunk)`)` Generated-document artifact event (live preview deltas + final Cloud Storage pointer).  
`optionQuestionsChunk` |  `object (`[OptionQuestionsChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OptionQuestionsChunk)`)` Structured clarification options parsed out of the model turn. The console renders these as a selectable option list instead of raw text.  
`confirmationRequest` |  `object (`[AssistantConfirmationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationRequest)`)` A blocking confirmation the agent paused on. The agent resumes when the answer arrives on a later request's `confirmationResponse`. Only sent to clients that declared the CONFIRMATION_CARDS capability on the request.  
`sessionCheckpoint` |  `object (`[SessionCheckpoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#SessionCheckpoint)`)` Session checkpoint/compaction recap event containing user intent and rolling summary.  
`resumeSnapshot` |  `object (`[TurnResumeSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnResumeSnapshot)`)` A compacted replay of an in-flight turn, sent as the first event of every attach or resume before any live event. The client replaces any locally rendered state for this turn with the snapshot's contents.  
`handoff` |  `object (`[TurnHandoffEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnHandoffEvent)`)` Tells the client to silently reconnect with resumeFromSequenceNumber: the task serving this stream is going away and the turn will continue elsewhere. Not an error; the stream completes normally after this event.  
`turnCompleted` |  `object (`[TurnCompletedEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnCompletedEvent)`)` The turn has ended. Sent as the last event of every turn, on the original stream and on every attached or resumed stream, so clients can end the turn on an explicit signal instead of inferring it from stream closure.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.assistantSessions.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## AssistantConfirmationResponse

The user's answer to an `[AssistantConfirmationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationRequest)`, sent on the next `[SessionService.StreamChatAiAssistant](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#google.cloud.ces.v1beta.SessionService.StreamChatAiAssistant)` call to resume the paused agent.

JSON representation  
---  
      
    
    {
      "confirmationId": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "confirmed": boolean,
      "answerText": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`confirmationId` |  `string` The `[AssistantConfirmationRequest.confirmation_id](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationRequest.FIELDS.confirmation_id)` being answered.  
The user's answer. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`confirmed` |  `boolean` Binary answer: true approves the paused action, false declines it.  
`answerText` |  `string` The chosen option's submitText, or free-form user text. The paused action is cancelled and the text is handed to the agent to act on.  
End of mutually exclusive fields.  
  
## StreamChatAiAssistantRequest.ClientCapability

Response features a client can declare.

Enums  
---  
`CLIENT_CAPABILITY_UNSPECIFIED` | Unspecified capability; ignored.  
`CONFIRMATION_CARDS` | The client renders `[AssistantConfirmationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationRequest)` cards and answers them via `confirmationResponse`.  
`CLIENT_MANAGED_LRO` | The client manages long-running operations out-of-band by polling the operation and sending `operationCompletedEvent` to resume the turn. If not declared, the server manages LRO polling and completes the turn inline.  
`PROJECT_SCOPE` | The client renders project-scope events: `typedPayload` cards, `targetApp` on tool calls and responses, `targets` on confirmation requests and `touchedApps` on turn completion.  
  
## OperationCompletedEvent

Event sent by the client or background worker to resume an assistant session after an asynchronous Long-Running Operation (LRO) completes.

JSON representation  
---  
      
    
    {
      "operationName": string,
      "targetResourceName": string,
      "operationType": string,
      "status": string,
      "deduplicationToken": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Status))
      },
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`operationName` |  `string` The operation resource name (e.g. `operations/{op}`).  
`targetResourceName` |  `string` The primary resource targeted or produced by the operation (e.g. evaluation run ID, app ID, dataset ID).  
`operationType` |  `string` The operation type or tool name (e.g. "run_evaluation", "copy_app", "export_app").  
`status` |  `string` Status of the operation run (e.g. "SUCCEEDED", "FAILED", "CANCELLED").  
`deduplicationToken` |  `string` Optional deduplication token (e.g. UUID) to prevent duplicate turn execution from concurrent browser tabs.  
`error` |  `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Status)`)` Optional canonical error status if the operation failed.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional structured result metadata (e.g. pass_rate, total_examples, export_uri).  
  
## ArtifactChunk

A streamed fragment of a document artifact (e.g. a markdown TDD) that the assistant is generating. Content deltas stream while the document is being written so clients can render a live preview; the FINALIZED chunk carries the Cloud Storage URI once the file has been persisted.

JSON representation  
---  
      
    
    {
      "artifactId": string,
      "displayName": string,
      "mimeType": string,
      "contentDelta": string,
      "gcsUri": string,
      "state": enum ([ArtifactChunk.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#ArtifactChunk.State)),
      "targetApp": string
    }  
  
Fields  
---  
`artifactId` |  `string` Identifier of the artifact, stable across all chunks of one artifact within the stream.  
`displayName` |  `string` The file name shown to the user, e.g. "hotel_booking_tdd.md". Set on STARTED (and repeated on FINALIZED).  
`mimeType` |  `string` The IANA media type of the artifact content, e.g. "text/markdown".  
`contentDelta` |  `string` Incremental artifact content. Set on DELTA chunks.  
`gcsUri` |  `string` The Cloud Storage object the artifact was persisted to. Set on FINALIZED chunks.  
`state` |  `enum (`[ArtifactChunk.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#ArtifactChunk.State)`)` Lifecycle position of this chunk.  
`targetApp` |  `string` Output only. The app this artifact was produced for, when it was produced for one. Format: `projects/{project}/locations/{location}/apps/{app}`  
  
## ArtifactChunk.State

Lifecycle position of this chunk within the artifact's stream.

Enums  
---  
`STATE_UNSPECIFIED` | Unused default.  
`STARTED` | The assistant started generating the artifact.  
`DELTA` | A content increment; contentDelta is set.  
`FINALIZED` | The artifact was persisted; gcsUri is set.  
`FAILED` | Generation or persistence failed; the artifact was not saved.  
`CLOSED` | The document finished streaming: its content was fully delivered via contentDelta chunks. Persistence may still follow; a FINALIZED chunk with a gcsUri is sent if and when the artifact is saved.  
  
## OptionQuestionsChunk

Structured clarification options the assistant asks the user to choose among, transduced server-side out of the model's turn (the option block is stripped from the streamed and persisted text). The console renders a keyboard-navigable option list docked above the composer.

JSON representation  
---  
      
    
    {
      "questions": [
        {
          object ([OptionQuestionsChunk.Question](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OptionQuestionsChunk.Question))
        }
      ]
    }  
  
Fields  
---  
`questions[]` |  `object (`[OptionQuestionsChunk.Question](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OptionQuestionsChunk.Question)`)` The questions asked this turn. More than one entry drives the console's "1 of N" pager.  
  
## OptionQuestionsChunk.Question

One question with its options.

JSON representation  
---  
      
    
    {
      "question": string,
      "options": [
        {
          object ([OptionQuestionsChunk.Option](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OptionQuestionsChunk.Option))
        }
      ]
    }  
  
Fields  
---  
`question` |  `string` The question header text.  
`options[]` |  `object (`[OptionQuestionsChunk.Option](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OptionQuestionsChunk.Option)`)` The selectable options, in presentation order.  
  
## OptionQuestionsChunk.Option

A single selectable option.

JSON representation  
---  
      
    
    {
      "title": string,
      "details": string,
      "submitText": string
    }  
  
Fields  
---  
`title` |  `string` Short plain-text option title (no markdown, no numbering).  
`details` |  `string` Optional trade-off details shown as secondary text.  
`submitText` |  `string` Optional message text to send when the option is chosen; defaults to `title` when empty.  
  
## AssistantConfirmationRequest

A blocking question or confirmation the assistant needs answered before an agent action can proceed. The requesting agent is paused and resumes only when the answer arrives on a later `[StreamChatAiAssistantRequest.confirmation_response](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#body.request_body.FIELDS.confirmation_response)`.

JSON representation  
---  
      
    
    {
      "confirmationId": string,
      "context": string,
      "positiveLabel": string,
      "negativeLabel": string,
      "questions": [
        {
          object ([OptionQuestionsChunk.Question](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OptionQuestionsChunk.Question))
        }
      ],
      "tool": string,
      "agentName": string,
      "expireTime": string,
      "targets": [
        {
          object ([AssistantConfirmationRequest.Target](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationRequest.Target))
        }
      ]
    }  
  
Fields  
---  
`confirmationId` |  `string` Identifier correlating this request with its response. Opaque to clients; must be echoed verbatim on the answering request.  
`context` |  `string` Context describing what is being confirmed (e.g. the action the agent wants to take, or the question it needs answered). Rendered as plain text, not Markdown.  
`positiveLabel` |  `string` Label for the approving action of a binary confirmation (e.g. "Publish"). Unset when `questions` is populated.  
`negativeLabel` |  `string` Label for the declining action of a binary confirmation (e.g. "Not yet"). Unset when `questions` is populated.  
`questions[]` |  `object (`[OptionQuestionsChunk.Question](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#OptionQuestionsChunk.Question)`)` Multi-choice form of the confirmation. When populated, the card renders a selectable option list and the chosen option's submitText (or free-form user text) is returned as `[AssistantConfirmationResponse.answer_text](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationResponse.FIELDS.answer_text)`.  
`tool` |  `string` Name of the tool call the agent paused on (e.g. "update_app"), for the card header. Unset for pure questions.  
`agentName` |  `string` Display label of the agent that raised the confirmation (e.g. `"Contract Architect"`), for the card header.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time after which this confirmation can no longer be answered. An expired card renders as inactive, and the server declines the confirmation on the next turn so the paused agent does not wait indefinitely.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`targets[]` |  `object (`[AssistantConfirmationRequest.Target](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#AssistantConfirmationRequest.Target)`)` Everything the confirmed action will change, so the console can render "Update 2 apps" and one badge per app. Empty for legacy single-target cards.  
  
## AssistantConfirmationRequest.Target

One resource the confirmed action will change.

JSON representation  
---  
      
    
    {
      "resource": string,
      "displayName": string,
      "action": string,
      "targetApp": string
    }  
  
Fields  
---  
`resource` |  `string` The resource that will change, as a full resource name.  
`displayName` |  `string` Display name of the resource or app, for the card.  
`action` |  `string` The action, e.g. `CREATE`, `UPDATE`, `DELETE`, `COPY`, `LINK`.  
`targetApp` |  `string` The app the resource belongs to, or empty for a location-scoped action such as creating an app. Format: `projects/{project}/locations/{location}/apps/{app}`  
  
## TurnResumeSnapshot

A compacted replay of an in-flight turn: everything needed to render the turn's visible output so far, plus the position live events continue from.

JSON representation  
---  
      
    
    {
      "turnId": string,
      "resolvedSequenceNumber": string,
      "events": [
        {
          object ([StreamChatAiAssistantResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#body.StreamChatAiAssistantResponse))
        }
      ],
      "orphanDeadlineTime": string
    }  
  
Fields  
---  
`turnId` |  `string` Identifies the turn being attached to.  
`resolvedSequenceNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The position this snapshot represents. Live events follow with sequenceNumber strictly greater than this. When lower than the resumeFromSequenceNumber the client requested, flushed progress lags what the client already rendered: the client must discard its rendered content of this turn beyond this position before applying the snapshot.  
`events[]` |  `object (`[StreamChatAiAssistantResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#body.StreamChatAiAssistantResponse)`)` Compacted events reconstructing the turn's visible output, in render order, using the same event shapes as live streaming.  
`orphanDeadlineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When the turn will be wound down if no client remains attached.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## TurnHandoffEvent

Emitted before this task stops serving the stream mid-turn (e.g. a server restart). The turn's state is persisted; a reconnect carrying resumeFromSequenceNumber continues it on another task.

JSON representation  
---  
      
    
    {
      "turnId": string,
      "reason": enum ([TurnHandoffEvent.Reason](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnHandoffEvent.Reason))
    }  
  
Fields  
---  
`turnId` |  `string` Identifies the turn to resume.  
`reason` |  `enum (`[TurnHandoffEvent.Reason](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnHandoffEvent.Reason)`)` Why the stream is handing off.  
  
## TurnHandoffEvent.Reason

Why the stream is handing off.

Enums  
---  
`REASON_UNSPECIFIED` | Unspecified.  
`SERVER_RESTART` | The serving task is shutting down (release push or rescheduling).  
  
## TurnCompletedEvent

Terminal event of a turn (see StreamChatAiAssistantResponse.turn_completed).

JSON representation  
---  
      
    
    {
      "turnId": string,
      "reason": enum ([TurnCompletedEvent.Reason](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnCompletedEvent.Reason)),
      "finalSequenceNumber": string,
      "touchedApps": [
        string
      ]
    }  
  
Fields  
---  
`turnId` |  `string` Identifier of the turn that ended; matches TurnResumeSnapshot.turn_id and ActiveTurnInfo.turn_id.  
`reason` |  `enum (`[TurnCompletedEvent.Reason](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnCompletedEvent.Reason)`)` Why the turn ended.  
`finalSequenceNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Sequence number of the last event the turn produced. A client whose cursor is lower missed content and should reload the session to see it.  
`touchedApps[]` |  `string` Apps this turn targeted or changed, so the console can refresh exactly those apps' stores. Project-scoped sessions only. Format: `projects/{project}/locations/{location}/apps/{app}`  
  
## TurnCompletedEvent.Reason

Why the turn ended, so a client that attached late can word the outcome instead of guessing from an empty stream.

Enums  
---  
`REASON_UNSPECIFIED` | Unspecified.  
`COMPLETED` | The turn ran to completion; the session holds its committed output.  
`ABANDONED` | No task was driving the turn any more; it was sealed to a committed partial and cannot be continued.  
`RESUME_UNAVAILABLE` | This server does not serve attach or resume for the session, so nothing was tailed; the client should reload the session instead.  
  
## TurnMetadata

Turn-level metadata and intent categorization.

JSON representation  
---  
      
    
    {
      "contractRelated": boolean,
      "contractFinalized": boolean,
      "contractStreamingPhase": enum ([TurnMetadata.ContractStreamingPhase](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnMetadata.ContractStreamingPhase)),
      "contractDraftComplete": boolean
    }  
  
Fields  
---  
`contractRelated` |  `boolean` Indicates whether this assistant turn was contract-related (e.g. contract drafting, alignment, extraction, or revision).  
`contractFinalized` |  `boolean` Set on the final artifact event of a turn whose contract draft was published (a revision was activated). Terminal for the clarification flow of this draft: contractProgress is authoritative and complete.  
`contractStreamingPhase` |  `enum (`[TurnMetadata.ContractStreamingPhase](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/streamChatAiAssistant#TurnMetadata.ContractStreamingPhase)`)` Set only on in-flight progress estimates emitted while a contract artifact fence is streaming, and on the revision-turn-start event. Unset on authoritative payloads.  
`contractDraftComplete` |  `boolean` Set on the terminal event of a contract draft whose every placeholder is resolved (contractProgress is 100%), whether or not the draft was published. Clients complete and dismiss the contract progress display on it; publication is reported separately by contractFinalized.  
  
## TurnMetadata.ContractStreamingPhase

Streaming phase of the contract progress payload.

Enums  
---  
`CONTRACT_STREAMING_PHASE_UNSPECIFIED` | The payload is authoritative (computed from a complete contract document, a persisted snapshot, or the pre-draft state). Clients must replace any previously received progress with it.  
`DRAFTING` | An initial contract draft is streaming. contractProgress is an in-flight estimate: non-decreasing within one artifact fence, capped below the authoritative range, with pillarBreakdowns carrying totalItemCount == 0 to mark estimated pillar states.  
`REVISING` | A revision of an existing contract is streaming (for example after an annotation submission). Same estimate semantics as DRAFTING.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
