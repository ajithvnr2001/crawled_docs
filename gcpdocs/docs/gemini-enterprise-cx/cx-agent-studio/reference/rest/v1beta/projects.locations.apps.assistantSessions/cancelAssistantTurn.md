---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/cancelAssistantTurn/
title: Method: projects.locations.apps.assistantSessions.cancelAssistantTurn \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:40:50.967957+00:00
---

# Method: projects.locations.apps.assistantSessions.cancelAssistantTurn  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.assistantSessions/cancelAssistantTurn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.assistantSessions.cancelAssistantTurn Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Cancels the assistant session's in-flight turn, if any: the explicit user stop for a turn running detached from any stream. A cancel landing on a task that does not host the turn preempts it through the session turn epoch instead, ending it within one lease renewal.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{name=projects/*/locations/*/apps/*/assistantSessions/*}:cancelAssistantTurn`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The assistant session whose in-flight turn to cancel.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "turnId": string
    }  
  
Fields  
---  
`turnId` |  `string` Optional. The turn to cancel; empty cancels whichever turn is running. A cancel naming a turn that is no longer the running one is a no-op.  
  
### Response body

Response for assistantSessions.cancelAssistantTurn.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "cancelled": boolean
    }  
  
Fields  
---  
`cancelled` |  `boolean` Whether an in-flight turn was found and asked to stop (directly on this task, or through an epoch preemption for a turn hosted elsewhere).  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.assistantSessions.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
