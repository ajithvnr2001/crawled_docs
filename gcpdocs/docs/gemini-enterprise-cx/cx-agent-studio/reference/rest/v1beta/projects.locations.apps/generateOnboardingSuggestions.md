---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions/
title: Method: projects.locations.apps.generateOnboardingSuggestions \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:27:11.874277+00:00
---

# Method: projects.locations.apps.generateOnboardingSuggestions  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.generateOnboardingSuggestions Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * GenerateOnboardingSuggestionsResponse.UserProfile
  * AssistantSuggestion
    * JSON representation
  * AssistantSuggestion.LoadSession
    * JSON representation
  * AssistantSuggestion.Icon
  * AssistantSuggestion.Source



Generates personalized onboarding suggestions for the Arc zero state: classifies the requesting user (new / exploring / returning) from their assistant-session history in the app and returns suggestion chips (resume a session, continue work, or start something new) to render before any message is sent.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{name=projects/*/locations/*/apps/*}:generateOnboardingSuggestions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The app whose zero state is being rendered. Format: `projects/{project}/locations/{location}/apps/{app}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "maxSuggestions": integer
    }  
  
Fields  
---  
`maxSuggestions` |  `integer` Optional. Maximum number of suggestions to return. Defaults to 4 when unset.  
  
### Response body

Response message for `[SessionService.GenerateOnboardingSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#google.cloud.ces.v1beta.SessionService.GenerateOnboardingSuggestions)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "userProfile": enum ([GenerateOnboardingSuggestionsResponse.UserProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#GenerateOnboardingSuggestionsResponse.UserProfile)),
      "suggestions": [
        {
          object ([AssistantSuggestion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#AssistantSuggestion))
        }
      ],
      "contextToken": string
    }  
  
Fields  
---  
`userProfile` |  `enum (`[GenerateOnboardingSuggestionsResponse.UserProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#GenerateOnboardingSuggestionsResponse.UserProfile)`)` Classification of the requesting user's history.  
`suggestions[]` |  `object (`[AssistantSuggestion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#AssistantSuggestion)`)` Personalized suggestions, ranked most relevant first.  
`contextToken` |  `string` Opaque token capturing the onboarding snapshot used to generate these suggestions. Clients echo it on the first `StreamChatAiAssistantRequest` so the server can reuse the snapshot.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.assistantSessions.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## GenerateOnboardingSuggestionsResponse.UserProfile

Classification of the requesting user's history with the assistant in this app.

Enums  
---  
`USER_PROFILE_UNSPECIFIED` | Unspecified profile.  
`NEW` | No assistant sessions containing messages.  
`EXPLORING` | One or two assistant sessions containing messages.  
`RETURNING` | More than two assistant sessions containing messages.  
  
## AssistantSuggestion

A single personalized onboarding suggestion chip for Arc's zero state.

JSON representation  
---  
      
    
    {
      "suggestionId": string,
      "label": string,
      "rationale": string,
      "icon": enum ([AssistantSuggestion.Icon](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#AssistantSuggestion.Icon)),
      "source": enum ([AssistantSuggestion.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#AssistantSuggestion.Source)),
      "candidateType": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "seedPrompt": string,
      "loadSession": {
        object ([AssistantSuggestion.LoadSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#AssistantSuggestion.LoadSession))
      },
      "sendMessage": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`suggestionId` |  `string` Stable identifier for this suggestion, round-tripped by clients in interaction logging.  
`label` |  `string` Chip label shown to the user (at most 60 characters).  
`rationale` |  `string` Optional short explanation of why this suggestion is shown (tooltip / rationale popover).  
`icon` |  `enum (`[AssistantSuggestion.Icon](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#AssistantSuggestion.Icon)`)` Icon hint for the chip.  
`source` |  `enum (`[AssistantSuggestion.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#AssistantSuggestion.Source)`)` How this suggestion was produced.  
`candidateType` |  `string` Rule-table candidate type in kebab-case (e.g. "resume-pending-review"), for metrics.  
What activating the chip does. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`seedPrompt` |  `string` Prefill the composer with this text; the user reviews and sends.  
`loadSession` |  `object (`[AssistantSuggestion.LoadSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateOnboardingSuggestions#AssistantSuggestion.LoadSession)`)` Open an existing assistant session.  
`sendMessage` |  `string` Prefill the composer with this text and submit immediately. Only used for quick-reply chips inside an active onboarding conversation.  
End of mutually exclusive fields.  
  
## AssistantSuggestion.LoadSession

Parameters for the loadSession action.

JSON representation  
---  
      
    
    {
      "assistantSessionId": string
    }  
  
Fields  
---  
`assistantSessionId` |  `string` Identifier of the assistant session to open (the final segment of the AssistantSession resource name).  
  
## AssistantSuggestion.Icon

Icon hint for the chip.

Enums  
---  
`ICON_UNSPECIFIED` | Unspecified icon.  
`RESUME` | Resume a previous session.  
`BUILD` | Build something new.  
`EVALUATE` | Evaluation-related suggestion.  
`DEPLOY` | Deployment-related suggestion.  
`EXPLORE` | Exploration / discovery suggestion.  
`FIX` | Fix an error or failing state.  
  
## AssistantSuggestion.Source

How this suggestion was produced.

Enums  
---  
`SOURCE_UNSPECIFIED` | Unspecified source.  
`RULE` | Deterministic rule-table candidate with template phrasing.  
`LLM_RANKED` | Rule-table candidate re-ranked and phrased by the LLM phrasing step.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
