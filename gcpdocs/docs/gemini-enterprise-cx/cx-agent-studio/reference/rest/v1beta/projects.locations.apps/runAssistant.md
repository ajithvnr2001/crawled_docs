---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runAssistant/
title: Method: projects.locations.apps.runAssistant \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:24:17.150450+00:00
---

# Method: projects.locations.apps.runAssistant  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runAssistant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.runAssistant Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * RunAssistantRequest.InteractionType
  * AssistantOutput
    * JSON representation



Runs the assistant agent for the specified assistant session.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{app=projects/*/locations/*/apps/*}:runAssistant`

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
      "message": {
        object ([AssistantMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantMessage))
      },
      "interactionType": enum ([RunAssistantRequest.InteractionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runAssistant#RunAssistantRequest.InteractionType))
    }  
  
Fields  
---  
`assistantSession` |  `string` Required. The assistant session to be used to run the assistant. Format: `projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistantSession}`  
`message` |  `object (`[AssistantMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantMessage)`)` Required. The message to send to the assistant agent.  
`interactionType` |  `enum (`[RunAssistantRequest.InteractionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runAssistant#RunAssistantRequest.InteractionType)`)` Optional. Different interaction types for the assistant message.  
  
### Response body

Response message for `[AssistantService.RunAssistant](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runAssistant#google.cloud.ces.v1beta.AssistantService.RunAssistant)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "output": {
        object ([AssistantOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runAssistant#AssistantOutput))
      },
      "state": enum ([AssistantSessionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantSessionState))
    }  
  
Fields  
---  
`output` |  `object (`[AssistantOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runAssistant#AssistantOutput)`)` Required. The output from the assistant agent.  
`state` |  `enum (`[AssistantSessionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantSessionState)`)` Output only. The status of the assistant session.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `app` resource:

  * `ces.apps.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## RunAssistantRequest.InteractionType

The type of interaction for the message sent to the assistant.

Enums  
---  
`INTERACTION_TYPE_UNSPECIFIED` | The default value. This value is used if the type is not specified.  
`NEW_MESSAGE` | The message is a user input. User input is provided in the chunk list.  
`POLL` | The message is for polling the state of the assistant session.  
`DISMISS` | The message is to dismiss the assistant session pending review. This will change the state of the assistant session to idle.  
  
## AssistantOutput

The output from the assistant agent.

JSON representation  
---  
      
    
    {
      "message": {
        object ([AssistantMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantMessage))
      },
      "userResponseSuggestions": {
        object ([UserResponseSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#UserResponseSuggestions))
      }
    }  
  
Fields  
---  
`message` |  `object (`[AssistantMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#AssistantMessage)`)` Required. The response from the assistant agent.  
`userResponseSuggestions` |  `object (`[UserResponseSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions#UserResponseSuggestions)`)` Output only. Suggested user responses from the assistant agent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
