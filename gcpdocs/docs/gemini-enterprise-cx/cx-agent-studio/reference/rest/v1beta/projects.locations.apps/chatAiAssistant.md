---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/chatAiAssistant/
title: Method: projects.locations.apps.chatAiAssistant \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:48:46.121361+00:00
---

# Method: projects.locations.apps.chatAiAssistant  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/chatAiAssistant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.chatAiAssistant Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Runs Arc, the AI assistant, for the specified assistant session.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{app=projects/*/locations/*/apps/*}:chatAiAssistant`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`app` |  `string` Required. The app to run assistant for. Format: `projects/{project}/locations/{location}/apps/{app}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "assistantSession": string,
      "message": string,
      "attachedGcsUris": [
        string
      ],
      "contextToken": string
    }  
  
Fields  
---  
`assistantSession` |  `string` Required. The assistant session to be used to run the assistant. Format: `projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistantSession}`  
`message` |  `string` Required. The message to send to the assistant agent.  
`attachedGcsUris[]` |  `string` Optional. Cloud Storage URIs for files uploaded by the user during this turn. Example: "gs://cxas-transient-uploads/uuid/prd.pdf"  
`contextToken` |  `string` Optional. Opaque onboarding context token returned by `[SessionService.GenerateOnboardingSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#google.cloud.ces.v1beta.SessionService.GenerateOnboardingSuggestions)`. When set and still fresh, the server reuses the onboarding snapshot computed for the zero state instead of recomputing it for the first conversation turn.  
  
### Response body

Response message for `[AssistantService.ChatAiAssistant](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/chatAiAssistant#google.cloud.ces.v1beta.AssistantService.ChatAiAssistant)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "eventId": string,
      "eventTime": string,
      "uiEvent": {
        object ([UiEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/UiEvent))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "textChunk": string,
      "statusMessage": string,
      "sessionCheckpoint": {
        object ([SessionCheckpoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#SessionCheckpoint))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`eventId` |  `string` Unique identifier for the event.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the event occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uiEvent` |  `object (`[UiEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/UiEvent)`)` Optional. UI event payload.  
The event payload. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`textChunk` |  `string` Text Token (for streaming Gemini responses word-by-word)  
`statusMessage` |  `string` Simple status update  
`sessionCheckpoint` |  `object (`[SessionCheckpoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#SessionCheckpoint)`)` Session checkpoint/compaction recap event containing user intent and rolling summary.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `app` resource:

  * `ces.apps.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
